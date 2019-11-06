.. _lessons:

Lessons Learned
===============

In addition to the model validation results and conclusion (which are pending review for journal publication), the definition and execution of the SWiFT benchmarks yielded several lessons which should be taken into account in future benchmarks:

**Recommendations for successful model validation benchmarks**

- Perform the entire exercise in house before releasing it to outside participants;
- Enforce comparibility in the simulation setup across participants by requiring minimum spatial and temporal discretization, simulation length, spin up time, and domain size when applicable;
- For validation exercises focusing on the turbine response and wake, consider generating the turbulent inflow in house and providing the flow fields to all modelers so that differences in inflow won’t affect turbine model/wake model performance analyses;
- When releasing the exercise to the public:
	- Define a clear sequence of events. The preferred framework is composed of three phases: calibration, blind comparison, iteration:
		- Calibration phase: provides opportunity for modelers to blindly calibrate their models and iterate on their solution;
		- Blind comparison phase: results from different models are inter-compared without releasing the measurement data;
		- Iteration: modelers can improve their model or simulation setup after having seen model-measurement comparison.
	- Provide a consistent reference (github and/or webpage) that participants can always go to for latest information. Keep a timeline of events in this reference page. Keep this page up-to-date.
	- Provide an easy-to-use code (e.g. python script) that takes the model output of each participant and ensures that it meets the needs of the benchmark organizers. This will minimize the time spent debugging issues with specific data files that do not conform to required specifications and e-mail communication required to address errors made by modelers when preparing their data and uploading it.
	- Require that modelers provide timestamps in the file names of each file that they submit, and that the timestamp follow a specific and consistent format, e.g. YYYY_MM_DD;
	- Define a consistent and unambiguous coordinate system to be used;
	- For diagnostic variables (e.g. turbulence kinetic energy) or variables that require normalization (e.g. thrust coefficient) be explicit and unambiguous on how they should be computed.
