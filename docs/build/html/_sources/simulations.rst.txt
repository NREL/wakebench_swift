.. _simulations:

Benchmark Simulations
=====================

General Guidelines
------------------

- Simulation tools should be used to the limit of their capabilities. Two-dimensional, steady-state solutions are accepted for low-fidelity models. Mid- and high-fidelity models are expected to provide time series of three-dimensional flow fields from which the mean quantities will be diagnosed.
- Time-stepped simulations should be run to convergence, for statistically representative 10-minute conditions. The minimum recommended time of simulation is 60 minutes, so that six realizations of a 10-minute period may be combined to produce a statistically significant representation of the flow field under the prescribed inflow. Whenever possible, 100+ minutes of simulation should be the target.
- The choice of domain size, grid spacing, time step, and other model configuration parameters is left to the discretion of the participant.
- All provided results must observe the variable definitions and units as explicitly defined in :ref:`glossary`.

Turbine Model
-------------

The turbine present at the SWiFT test site is a modified version of a Vestas V27. The data related to the wind turbine is stored in the github repository under the folder `wt_data <https://github.com/NREL/wakebench_swift/tree/master/wt_data>`_. A version number is used to accommodate for potential versions of the turbine model that may be released in the future. For now, only one version is present: ``v1``, and it is considered the official wind-turbine model for this benchmark unless specified otherwise.

The folder  ``wt_data/v1/`` has the following subfolders:

- `FAST7_model`: Contains the simulation model for the program `FAST7 <https://nwtc.nrel.gov/FAST7>`_.  All the necessary files, including the FAST binary are provided in this folder. The model was developed by C. Kelley and J. White from Sandia National Laboratories. The model was tuned to match the measurements data (see the report mentioned below). Since most measurements were present below rated wind speed, the data are only provided for this range of wind speeds.

- `OpenFAST_model`: Contains the model for `OpenFAST <https://openfast.readthedocs.io/>`_  1 and 2. It is recommended to use the `OpenFAST2` model (`\_OF2`) since the aerodynamic module received some important updates between `OpenFAST1` and `OpenFAST2` which affects the results.

- `OpenFAST_model_NALU`: Containes the `OpenFAST1` model, adjusted such that it can be used directly within NALU (`WakeMod=0` and `CompInflow=2`)


- `Raw_model`: To ease the implementation of the turbine model into another format than the FAST format, simple CSV files are provided in this directory. The data matches the data present in the `FAST_model` but its format should be straightforward to read. This folder contains:
   - ``OperationalConditions.csv``: Pitch and Rotational Speed as function of wind speed.
   - ``AD*.csv``: Profile polars
   - ``Blade_Aero.csv``: Relevant aerodynamic data for the blade (chord, twist, and airfoil)
   - ``Blade_Structure.csv``: Relevant structural data for the blade (Mass, Stiffnesses, etc.)
   - ``Tower_Structure.csv``: Relevant structural data for the tower (Mass, Stiffnesses, etc.)
- `Simulated_data`: This folder contains simulated data obtained using the FAST model. These can be useful to compare the results from another model to the FAST results. Such data includes:
   - ``RotorPerformances.csv``: Pitch, Rotational Speed, Power, Thrust, Blade Root Flapwise (out-of-plane) moment, as function of wind speed, as obtained by the FAST7 model.
   - ``RotorPerformances_OF2.csv``: Similar data but obtained with the `OpenFAST2` model
   - ``AeroPerformances.csv``: Loads and inductions along the span of the blade for different wind speed as obtained by the FAST7 model

Benchmark participants who choose not to use FAST or OpenFAST for their simulations are responsible for porting this turbine model to their simulation platform, and encouraged to share their developed model with the community.


The following publications may be used as references for further details on the model:

- Christopher L. Kelley and Jonathan White, *An Update to the SWiFT V27 Reference Model*, Sandia report SAND2018-11893, 2018 (:download:`download <../../supporting_material/SAND_V27_FAST_Update.pdf>`)
- Brian R. Resor and Bruce LeBlanc - *An Aeroelastic Reference Model for the SWIFT Turbines*, Sandia report SAND2014-19136, 2014

.. _phase1:

Benchmark Phase 1: Code Calibration (COMPLETED)
-----------------------------------------------

    *The objective of this phase is to provide an opportunity for model calibration before the blind comparison.*

In Phase 1 of the benchmark, the wind-turbine wake is not yet considered. Instead, the atmospheric inflow and turbine response are considered. Participants are requested to submit their results for as many of the requested quantities as possible, according to the level of fidelity of their simulation tool. Publicly released python notebooks will show the analysis method used to compute diagnostics from the submitted results. This process is done to ensure consistency of the methodology across groups, and to guarantee repeatability of the analysis.

The calibration is used to modify inputs that are of high uncertainty to ensure that output quantities of interest are correct.

**Atmospheric Inflow**

During this exercise, the simulated atmospheric inflow is compared to measured atmospheric inflow (this may not be applicable to lower-fidelity models).
For the quantities of interest that were provided in the benchmark definition, the simulated values are simply compared to the range of acceptable values across the ensemble of measurements (which thus far has only been provided for roughness length).
For additional quantities of interest, the simulated values are compared to the mean and range of measured values within the ensemble that makes up this benchmark.

The inputs with high uncertainty which may need calibration include: roughness length, surface heat flux, atmospheric boundary layer height. The quantities of interest that will be considered can be found in :ref:`validation`. Participants are asked to submit the simulation setup information as well as the simulation results listed below.

- Simulation setup:
    - Upload a single file named ``<participant_id>_<YYYYMMDD>_simulation_setup.yaml``
        - A template for this file can be downloaded :download:`here <../../file_templates/template_YYYYMMDD_simulation_setup.yaml>`
        - ``<YYYYMMDD>`` is the file submission date
        - Requested parameters are:
            - Mesh grid spacing in the three spatial dimensions (:math:`\Delta x, \Delta y, \Delta z`)
            - Temporal resolution of the output (:math:`\Delta t`)
            - Number of points in each of the four dimensions (:math:`n_x, n_y, n_z, n_t`)
            - Any constants used to initialize the model (e.g., roughness lenght, inversion height and strength, surface heat flux, wake expansion coefficient...)
- Results for time-stepping simulation tools:
    - Upload a single file named ``<participant_id>_<YYYYMMDD>_uvw_<x>D.nc`` (format `NetCDF 4.0 <https://www.unidata.ucar.edu/software/netcdf/>`_)
        - A template for this file can be downloaded :download:`here <../../file_templates/template_YYYYMMDD_uvw_2D.nc>`
        - A sample writer for this file can be found in this :download:`jupyter notebook <../../code/example_write_netcdf.ipynb>`
        - ``<YYYYMMDD>`` is the file submission date
        - ``<x>`` is the downstream distance :math:`x` normalized by the rotor diameter :math:`D`
        - File should contain :math:`u,v,w` values, which are four-dimensional: :math:`(n_t \times n_x \times n_y \times n_z)`. For this submission, :math:`n_x=1` (:math:`x=-65~\mathrm{m}\sim-2.5\mathrm{D}`) and the time is given in units of seconds, since the start of the simulation usable time (i.e., not counting spin-up)
        - The length of the time series to be uploaded is left to the discretion of the participant. We request that the simulation be long enough so that its statistics are converged.
        - The sampling frequency of the time series to be uploaded should be at least 1 Hz.
- Results for steady-state simulation tools:
    - Upload a single file named ``<participant_id>_<YYYYMMDD>_uvw_<x>D_steady_state.nc``
        - Same as for time-stepping simulation tools, but now :math:`n_t=1`

**Wind Turbine Response**

Once the atmospheric inflow is verified to match the conditions specified within the benchmark (within an acceptable range, determined by the upper and lower bounds of the ensemble mean of each quantity considered), the turbine response is compared to measured values.

The inputs with high uncertainty which may need calibration include: the aerodynamic model used, the BEM formulation, the generator torque constant. Participants are asked to submit the following results:

- Results for time-stepping simulation tools:
    - Upload a single file named ``<participant_id>_<YYYYMMDD>_wtg_response.txt``
        - A template for this file can be downloaded :download:`here <../../file_templates/template_YYYYMMDD_wtg_response.txt>`
        - ``<YYYYMMDD>`` is the file submission date
        - File shall have one column per variable (including time) and :math:`n_t` rows of data (don't upload the spin up!)
        - Requested variables are time series of hub-height wind speed at the turbine (m/s), rotor power (kW), rotor torque (N m), blade pitch for one blade (deg), blade root flapwise moment for one blade (N m), blade root edgewise moment for one blade (N m), generator power (kW), generator torque (N m), aerodynamic thrust force (N), thrust coefficient (-), total thrust force (N)
- Results for steady-state simulation tools:
    - Upload a single file named ``<participant_id>_<YYYYMMDD>_wtg_response_steady_state.txt``
        - A template for this file can be downloaded :download:`here <../../file_templates/template_YYYYMMDD_wtg_response_steady_state.txt>`
        - ``<YYYYMMDD>`` is the file submission date
        - File shall have two columns: variable name, variable value
        - Requested variables are the same as those requested for the time-stepping tools, and their value set to NaN (not -999.0) when model cannot simulate them

Benchmark Phase 2: Blind Comparison
-----------------------------------

In Phases 2 and 3 of the benchmark, the downstream evolution of the wind-turbine wake is considered. Phase 2 is composed of two parts. First, a code-to-code comparison is made without considering the wake measurements. Second, the simulation results are compared to measurements.

**Code-to-Code Comparison**

    *The objective of the first step in the blind comparison is to identify potential errors in model configuration, which might be evident in the form of outliers when the model results are cross-compared.*

**Code-to-Measurements Comparison**

    *The objective of the second step of the blind comparison is to provide a first assessment of the skill of the simulation tool.*

In both parts of this phase, participants are requested to submit their results for as many of the requested quantities as possible, according to the level of fidelity of their simulation tool. Publicly released python notebooks will show the analysis method used to compute diagnostics from the submitted results. This process is done to ensure consistency of the methodology across groups, and to guarantee repeatability of the analysis. Participants are asked to submit the simulation setup information as well as the simulation results listed below.

**Please keep results for each benchmark separate, in folders called neutral, unstable and stable.**

- Simulation setup:
    - Same format as in Phase 1

- Results for time-stepping simulation tools and for steady-state simulation tools:
    - Same as requested in Phase 1 for atmospheric inflow and turbine response
    - In addition to atmospheric inflow and turbine response, several netcdf files are uploaded to characterize the modeled flow in the wake: one for each :math:`x` distance (i.e., not only at :math:`x=-2.5` D, but also between :math:`x=1` D and :math:`x=8` D in :math:`1` D increments)
    - The number of uploaded files for characterization of the flow (inflow and wake) will be 9 (one per downstream distance). We are keeping these netcdf files separate for each :math:`x` because some participants have really high resolution meshes and adding more than one :math:`x` in there would make for files that are too large to download!

Benchmark Phase 3: Iteration
----------------------------

    *The objective of this phase is to interrogate results to understand where models work well and where improvements are required.*

**Please keep results for each benchmark separate, in folders called neutral, unstable and stable.**

In Phase 3, participants are encouraged to revise their simulations and submit updated results. Results from similar models are grouped accordingly to help identify potential improvements to the code or its use. No calibration of the models can be performed at this stage. The calibration is limited to Phase 1. At each iteration, participants are asked to submit the same files requested in Phase 2 in addition to:

- Description of updates to the simulation
    - Upload a single file named ``<participant_id>_<YYYYMMDD>_updates.txt``
        - ``<YYYYMMDD>`` is the file submission date
        - File contents clearly identify what was changed from the previous submission to the current, and why the changes were made
        - File can be freely formatted by participants
