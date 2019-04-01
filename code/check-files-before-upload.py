# # load packages
import os, glob, sys
import pandas as pd
import numpy as np
import xarray
import matplotlib.pyplot as plt

try:
    main_dir =  sys.argv[1]
    print(" ")
    print("Will check files inside {0}".format(main_dir))
    print(" ")
except:
    print(" !!!!!!! ")
    print("Must pass argument: absolute path to directory with .txt and .nc files.")
    print(" !!!!!!! ")

# # define some fixed parameters

# rotor diameter of V27
D     = 27.0
# hub height of V27
z_hub = 32.1
# rotor radius
R      = D/2.
# points tracing rotor outline in meters
yRotor = np.asarray([ 0.0 + R * np.cos(np.radians(a)) for a in np.arange(0,361,5) ])
zRotor = np.asarray([ z_hub + R * np.sin(np.radians(a)) for a in np.arange(0,361,5) ])
# points tracing rotor outline normalized against rotor diameter
yRotorNorm = np.asarray([yR/D for yR in yRotor])
zRotorNorm = np.asarray([(zR-z_hub)/D for zR in zRotor])

# # list of files

wtg_files = glob.glob(os.path.join(main_dir,'*wtg*.txt'))
nc_files  = glob.glob(os.path.join(main_dir,'*.nc'))

# # turbine files

expected_variables = [  'hub_wind_speed_[m_s-1]',
                        'rotor_power_[kW]',
                        'rotor_torque_[N_m]',
                        'rotor_speed_[rpm]',
                        'blade_pitch_[deg]',
                        'blade_root_flap_moment_[N_m]',
                        'blade_root_edge_moment_[N_m]',
                        'generator_power_[kW]',
                        'generator_torque_[N_m]',
                        'aero_thrust_force_[N]',
                        'aero_thrust_coefficient_[-]',
                        'total_thrust_force_[N]'  ]

# # run some checks

print("Checking ...")
for wtg_file in wtg_files:

    print(os.path.split(wtg_file)[-1])
    print(" ")

    # 1. check that it can be easily read
    print("File...")
    try:
        df = pd.read_csv(wtg_file,comment='#')
    except:
        print("Cannot read it.")
        break
    print("...OK")
    print(" ")

    # in the case of steady-state files, set variables as column names to be
    # consistent with time-stepping files
    if "steady" in wtg_file:
        df = df.set_index("name").T

    # 2. Check that all variables are there
    print("Variables...")
    avail_cols = df.columns
    for var in expected_variables:
        if var not in avail_cols:
            print("Missing or wrong units in {0}".format(var))
            break
    print("...OK")
    print(" ")

    # 3. See which benchmark data is being read
    mean_power = df['rotor_power_[kW]'].mean()
    if (mean_power>60):
        benchmark_id = 'swift_neutral_evolution'
    elif (mean_power<25):
        benchmark_id = 'swift_stable_evolution'
    elif ((mean_power>30)&(mean_power<60)):
        benchmark_id = 'swift_unstable_dynamics'
    else:
        print("...this mean power does not clearly indicate which benchmark case is being analyzed.")
        break

    # 4. Read measurements
    measurement_summary = glob.glob("{0}_wtg_summary.csv".format(benchmark_id))
    try:
        measurements = pd.read_csv(measurement_summary[0], index_col=[0])
    except:
	print("!!!!!!!!!!!!!!!!!")
	print("Could not find summary file which has measurement data. Please go get it and put it here.") 
	print("!!!!!!!!!!!!!!!!!")
        variables = ["rotor_speed_[rpm]","blade_root_flap_moment_[N_m]","generator_torque_[N_m]","generator_power_[kW]"]
        measurements = pd.DataFrame(columns=["mean","median"],index=variables)
        measurements[:] = np.nan

    # 5. Compare measurements and simulation
    print("{0:40s}{1:<20s}{2:<20s}".format(" ","measured","simulated"))
    print("{0:40s}{1:<20s}{2:<20s}".format(" ","--------","---------"))
    for qoi in measurements.index:
        meas_mean = measurements.loc[qoi,'mean']
        sim_mean  = df[qoi].mean()
        print("{0:40s}{1:<20.2f}{2:<20.2f}".format(qoi,meas_mean,sim_mean))

        perc_diff = np.abs(((meas_mean-sim_mean)/meas_mean)*100)

        if (perc_diff>25):
            print(" !!!!!!! ")
            print("Check your values for {0}".format(qoi))
            print(" !!!!!!! ")

# # flow files (inflow & wake)

print(" ")
print("Checking ...")

# which downstream distances are available for this dataset?
available_x = np.unique([p.split('_uvw_')[-1].split('D')[0] for p in nc_files])

# a dictionary to keep each xarray (one for each x)
xarrs = {}

# loop through these "x"
distance_count = 0
for x in available_x:

    # get file names just for this "x" (this avoids mixing files of different x/time in the case of people who ran several separate simulations for the same benchmark)
    inflow_paths = glob.glob(os.path.join(main_dir,"*_{0}D_*.nc".format(x)))
    if len(inflow_paths)==0:
        inflow_paths = glob.glob(os.path.join(main_dir,"*_{0}D*.nc".format(x)))

    # loop through files
    inflow_count = 0

    for inflow_path in inflow_paths:

        filename = os.path.split(inflow_path)[-1].split(".nc")[0]
        print(filename)

        # read the nc file for this specific downstream distance
        xarr_tmp = xarray.open_dataset(inflow_path)

        # lower-case all of the variable names and dimension names, and make sure time is always called "t"
        # need this for concatenation along time dimension right below
        variable_names = xarr_tmp.variables.keys()
        name_dict      = {}
        for variable_name in variable_names:
            name_dict[variable_name] = variable_name.lower()
            if variable_name.lower() == "time":
                name_dict[variable_name] = "t"
        xarr_tmp = xarr_tmp.rename(name_dict=name_dict)

        # if it's the first file, put it in the dictionary
        if inflow_count==0:
            xarr_this_distance = xarr_tmp.copy()
        # otherwise, concatenate with already existing xarray in the dictionary
        # if we are doing a second time around of this downstream distance, concatenate over time
        else:
            # if it's a time stepping model, it'll have a dt
            try:
                dt = np.diff(xarr_tmp.t.data)[2]
            # otherwise it's a bunch of steady-state runs, just assume dt=1
            except:
                dt = 1
            xarr_tmp.t.data = xarr_tmp.t.data - xarr_tmp.t.data[0] + np.max(xarr_this_distance.t.data) + dt
            xarr_this_distance = xarray.concat([xarr_this_distance,xarr_tmp],dim='t')

        inflow_count += 1

        xarr_tmp.close()

    # some participants have x = -2.4 or -2.6...
    # just make these dictionary keys (downstream distances) a bit more uniform by rounding them to the nearest 0.5
    this_d = round(float(x) * 2) / 2
    xarrs[this_d] = xarr_this_distance.copy()

    distance_count += 1

print(" ")

# # run some checks

# # plot and save flow contours
print(" ")
for x in xarrs.keys():
    fig = plt.figure(figsize=(3*5,5))
    ax  = {}
    i   = 1
    for component in ['u','v','w']:

        ax[i]  = fig.add_subplot(1,3,i,aspect='equal')

        y = (xarrs[x].y.values)/D
        z = (xarrs[x].z.values - z_hub)/D

        if "t" in xarrs[x].variables.keys():
            v = getattr(xarrs[x],component)
            v = v.mean("t")
            v = np.squeeze(v.data.T)
        else:
            v = np.squeeze(getattr(xarrs[x],component).data.T)

        p = ax[i].pcolormesh(y,z,v,cmap='Spectral')
        ax[i].plot(yRotorNorm, zRotorNorm, ls='--', lw=1, color='k')

        ax[i].set_ylim([-z_hub/D,1.5])
        ax[i].set_xlim([-1.34,1.34])
        ax[i].invert_xaxis()
        ax[i].set_title(component)

        clb = plt.colorbar(p, shrink=0.7)
        clb.set_label(r'{0} [m/s]'.format(component), labelpad=15, y=0.45)

        i+=1
    fig.suptitle("$x\sim$ {0} D".format(x),fontsize=20)
    fig.subplots_adjust(wspace=0.3)

    fname = "{0}_uvw_{1}D.png".format(benchmark_id,format(x))
    fig.savefig(fname)
    plt.clf()
    print("Saved {0}".format(fname))


# what distance exactly is the upstream distance for this dataset?

x_up = [x for x in xarrs.keys() if x<0][0]

# # plot and save velocity deficit

component = 'u'

print(" ")

for x in xarrs.keys():

    if "t" in xarrs[x].variables.keys():
        v_up = getattr(xarrs[x_up],component)
        v_up = v_up.mean("t")
        v_up = np.squeeze(v_up.data.T)
    else:
        v_up = np.squeeze(getattr(xarrs[x_up],component).data.T)

    if x>0:

        fig = plt.figure(figsize=(5,5))
        ax  = fig.add_subplot(1,1,1,aspect='equal')

        y = (xarrs[x].y.values)/D
        z = (xarrs[x].z.values - z_hub)/D

        if "t" in xarrs[x].variables.keys():
            v = getattr(xarrs[x],component)
            v = v.mean("t")
            v = np.squeeze(v.data.T)
        else:
            v = np.squeeze(getattr(xarrs[x],component).data.T)

        vd   = (v/v_up)-1.0

        p = ax.pcolormesh(y,z,vd,cmap='Spectral')
        ax.plot(yRotorNorm, zRotorNorm, ls='--', lw=1, color='k')

        ax.set_ylim([-z_hub/D,1.5])
        ax.set_xlim([-1.34,1.34])
        ax.invert_xaxis()
        ax.set_title(component)

        clb = plt.colorbar(p, shrink=0.7)
        clb.set_label(r'velocity deficit for {0} [-]'.format(component), labelpad=15, y=0.45)

        fig.suptitle("$x\sim$ {0} D".format(x),fontsize=20)

        fname = "{0}_u_deficit_{1}D.png".format(benchmark_id,format(x))
        fig.savefig(fname)
        plt.clf()
        print("Saved {0}".format(fname))

print(" ")
print(" ")
print("Please visually check that the flow data is correct via the saved figures.")
