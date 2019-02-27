# Folder content:

All the files in this folder correspond to the version 1 of the V27 model. 

- FAST7\ _model: contains FAST7 model
- OpenFAST\ _model: contains OpenFAST1&2 model (and FAST8 model). The only differences between these models is the definition of the aerodyn files, and the executable used to run the scripts. The main files for the OpenFAST2 model is SNLV27_OF2.fst, for OpenFAST1 SNLV27_OF1.fst, for Fast8 SNLV27_F8.fst.
- OpenFAST\_model\_NALU: contains the OpenFAST1 and OpenFAST2 models, adjusted such that it can be used directly within NALU (`WakeMod=0` and `CompInflow`=2)
- Raw_models: contains the same data as the models in a simple tabulated format.  The different between the aerodynamic definition in FAST and OpenFAST is such that "r" in the file "Blade_Aero.csv" is the distance from the rotor apex to a blade station. In the file "Blade_Aero_OF2.csv" the variable "BldSpan" is the distance from the blade root to an aerodynamic station
- Simulated_data: contains results obtained by using the FAST7 and OpenFAST2 programs
 
  


