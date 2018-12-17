.. _swift_neutral_evolution:

Neutral Benchmark
=================

.. pull-quote::

    **This exercise will reveal how well different models perform under the most commonly simulated stratification condition.**

This benchmark focuses on "Wake Evolution under Nearly Neutral Atmospheric Conditions". The validation focuses on the mean characteristics of a single wake as it propagates in a neutral atmosphere.  The objective of this exercise is to evaluate the ability of various models to simulate the downstream evolution of a single wake under the simplest possible environmental conditions: flat terrain, no weather events, and nearly neutral atmospheric conditions.

This benchmark welcomes all models. This document provides detailed, quantitative information necessary to engage in this specific SWiFT Benchmark. For general information about the SWiFT Benchmarks, see :ref:`the_swift_benchmarks`.

The Measurements
----------------

Wake measurements were collected between 1 D and 5 D downstream of the rotor, and the validation focuses on mean wake characteristics at these distances. In addition, models will be cross-compared for quantities of interest for which measurements are not available.


The Simulation
--------------

Participants are asked to simulate the mean wake behind a single turbine (between 1 D and 8 D) operating in a neutral atmosphere under the inflow described below. Please observe the :ref:`simulation guidelines <simulations>` for information that is common to all SWiFT benchmarks (e.g., turbine model, requested output files).


**Inflow Conditions**

The information below should be used by the benchmark participants to simulate atmospheric inflow (in the case of higher-fidelity models) or to constrain the parameters used to initialize the model (in the case of lower-fidelity models). Not all information given will necessarily be used to perform the simulations. Note that the values provided refer to the ensemble average of six 10-minute temporal averages.

.. table::
    :widths: 10 40 10 10 30

    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | Variable                                          | Short Description                          | Value      | Unit  | Remark                                                                           |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle \overline{U}_{hub} \rangle`        | Mean hub-height wind speed                 | 8.3        | m/s   |                                                                                  |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle \overline{TI}_{hub} \rangle`       | Mean hub-height turbulence intensity       | 10.8       | %     |                                                                                  |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle \alpha\rangle`                     | Mean wind-speed profile power-law exponent | 0.14       | \-    |                                                                                  |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`z_0`                                       | Roughness length                           | 0.005-0.05 | m     | Ensemble range for intercept of :math:`[\log(z),U]` curve from sonic measurements|
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`z_i`                                       | Atmospheric boundary layer height          | -          | m     | No measurements available                                                        |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle z/L \rangle`                       | Stability parameter                        | 0.004      | \-    | Computed from sonic measurements at :math:`z=10` m                               |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle u_* \rangle`                       | Friction velocity                          | 0.44       | m/s   | Computed from sonic measurements at :math:`z=10` m                               |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle \overline{w'\theta_v'} \rangle`    | Kinematic vertical turbulent heat flux     | -0.002     | K m/s | Computed from sonic measurements at :math:`z=10` m                               |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle \theta_v \rangle_0`                | Virtual potential temperature near ground  | 314.4      | K     | Computed from temperature and pressure sensors at :math:`z=2` m                  |
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+
    | :math:`\langle \rho \rangle_{hub}`                | Air density                                | 1.02       | kg m-3| Total air density, considers dry air and water vapor                             |    
    +---------------------------------------------------+--------------------------------------------+------------+-------+----------------------------------------------------------------------------------+

**Turbine Operation**

Please see :ref:`turbine model <simulations>` details.
