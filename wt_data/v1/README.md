# Folder content:

- FAST7\ _model: contains FAST7 model
- OpenFAST\ _model: contains OpenFAST1&2 model (and FAST8 model). The only differences between these models is the definition of the aerodyn files, and the executable used to run the scripts. The main files for the OpenFAST2 model is SNLV27_OF2.fst, for OpenFAST1 SNLV27_OF1.fst, for Fast8 SNLV27_F8.fst.
- Raw_models: contains the same data as the models in a simple tabulated format.  The different between the aerodynamic definition in FAST and OpenFAST is such that "r" in the file "Blade_Aero.csv" is the distance from the rotor apex to a blade station. In the file "Blade_Aero_OF2.csv" the varaible "BldSpan" is the distance from the blade root to an aerodynamic station
 
  


