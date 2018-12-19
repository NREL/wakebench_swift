.. _swift_unstable_dynamics:

Unstable Benchmark
==================

.. pull-quote::

    **This exercise will reveal how well different models perform under unstable conditions, where large and active turbulent eddies often lead to wake meandering and accelerate wake recovery.**

This benchmark focuses on "Wake Dynamics under Unstable Atmospheric Conditions". The validation focuses on the dynamic characteristics of a single wake at a fixed downstream distance. The objective of this exercise is to evaluate the ability of various models to simulate the unsteady behavior of wakes, which is extremely relevant if models are to be used to diagnose the effects of turbulence on performance and reliability.

This benchmark welcomes all time-stepping models. This document provides detailed, quantitative information necessary to engage in this specific SWiFT Benchmark. For general information about the SWiFT Benchmarks, see :ref:`the_swift_benchmarks`.

The Measurements
----------------

Wake measurements were collected at 3 D downstream of the rotor, and the validation considers mean and dynamic wake characteristics at this distance. In addition, models will be cross-compared for quantities of interest and downstream distances for which measurements are not available.


The Simulation
--------------

Participants are asked to simulate the mean wake behind a single turbine (between 1 D and 8 D) operating in an unstable atmosphere under the inflow described below. Please observe the :ref:`simulation guidelines <simulations>` for information that is common to all SWiFT benchmarks (e.g., turbine model, requested output files).

**Inflow Conditions**

The information below should be used by the benchmark participants to simulate atmospheric inflow (in the case of higher-fidelity models) or to constrain the parameters used to initialize the model (in the case of lower-fidelity models). Not all information given will necessarily be used to perform the simulations. Note that the values provided refer to the ensemble average of five 10-minute temporal averages.

.. table::
    :widths: 10 40 10 10 30

    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | Variable                                          | Short Description                          | Value      | Unit  | Remark                                                                           |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle \overline{U}_{hub} \rangle`        | Mean hub-height wind speed                 | 6.7        | m/s   |                                                                                  |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle \overline{TI}_{hub} \rangle`       | Mean hub-height turbulence intensity       | 12.6       | %     |                                                                                  |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle \alpha\rangle`                     | Mean wind-speed profile power-law exponent | 0.14       | \-    |                                                                                  |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`z_0`                                       | Roughness length                           | 0.005-0.05 | m     | Value obtained from the neutral benchmark measurements                           |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`z_i`                                       | Atmospheric boundary layer height          | -          | m     | No measurements available                                                        |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle z/L \rangle`                       | Stability parameter                        | -0.089     | \-    | Computed from sonic measurements at :math:`z=10` m                               |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle u_* \rangle`                       | Friction velocity                          | 0.33       | m/s   | Computed from sonic measurements at :math:`z=10` m                               |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle \overline{w'\theta_v'} \rangle`    | Kinematic vertical turbulent heat flux     | 0.023      | K m/s | Computed from sonic measurements at :math:`z=10` m                               |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle \theta_v \rangle_0`                | Virtual potential temperature near ground  | 290.9      | K     | Computed from temperature and pressure sensors at :math:`z=2` m                  |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle \rho \rangle_{hub}`                | Air density                                | 1.09       | kg m-3| Total air density, considers dry air and water vapor                             |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+

**Turbine Operation**

Please see :ref:`turbine model <simulations>` details.
