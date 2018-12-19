Each benchmark case, 

* swift_neutral_evolution
* swift_unstable_dynamics
* swift_stable_evolution

was defined based on measurements collected at the SWiFT facility. 

For each of the benchmark cases, a number of 10-minute periods was selected based on the similarity of their meteorological conditions. 
The .csv files in this folder represent the hub-height inflow to the wind turbines during each of the 10-minute periods used to define these benchmarks.

The case "swift_neutral_evolution" has six files. Each one is a 10-minute time series.
The case "swift_unstable_dynamics" has five files. Each one is a 10-minute time series.
The case "swift_stable_evolution" has six files. Each one is a 10-minute time series.

Each file contains

* u [m/s] is the wind velocity vector component along the main wind direction
* v [m/s] is the wind velocity vector component horizontally normal to the main wind direction
* w [m/s] is the wind velocity vector component normal to the ground

The provided values of u, v, w have undergone the following processing steps:

* original data provided by SNL (in the form of .mat files) are read in
* matlab datenum are interpolated to datetime and rounded to the closest 0.01 second
* data gaps shorter than 0.1 second are filled with a time-aware interpolation using adjacent valid values
* sonic yaw angle is computed and used to rotate the wind vector so that the mean "u" is along the main wind direction
* rotated u, v, w are saved into .csv files

Note that the velocity vector was not rotated with respect to the sonic pitch angle, which is often done for sites with complex terrain to remove the mean vertical velocity is zero and thereby ensure that the vertical velocity values reported refer to turbulence fluctuations and do not consider the contribution of upslope and downslope flows. This was assumed as an unnecessary step for the SWiFT site where the terrain is fairly flat and homogeneous. Applying a pitch correction would require time series longer than 10 minutes, which are not provided at this point.  

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
IMPORTANT NOTE 

To ensure consistency with the processing that was performed by the benchmark organizers to compute turbulence statistics, we recommend the following approach:

* Within each file, compute 10-minute mean and subtract from time series to obtain perturbations
* Linearly detrend the time series of perturbations
* Compute whichever turbulence statistics are of interest 
* Obtain an ensemble average of each statistics by computing the mean of the values obtained for all of the 10-minute periods for a given benchmark 
* Use this ensemble average to drive your idealized simulation of atmospheric turbulence
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
