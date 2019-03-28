# Folder content:

NOTE: THIS VERSION IS A BETA VERSION

All the files in this folder correspond to the version 2 of the V27 model. 

The changes made between version 2 and verions 1 are:

    - pitch angle            :  2deg      (1.666deg before)
    - distance Tower 2 Shaft : 1.05m      (1.50m before)
    - Gearbox efficiency     : 94.43%     (100% before)
    - Generator efficiency   : 96.35%     (100% before)
    - Region 2 constant      : 0.0004128  (0.0004421 before) 


The folder structure is similar to the one for the v1 version: 

- OpenFAST\ _model: contains OpenFAST2 model. The main files for the OpenFAST2 model is SNLV27_OF2.fst.
- Raw_models: contains the same data as the models in a simple tabulated format.  The different between the aerodynamic definition in FAST and OpenFAST is such that "r" in the file "Blade_Aero.csv" is the distance from the rotor apex to a blade station. In the file "Blade_Aero_OF2.csv" the variable "BldSpan" is the distance from the blade root to an aerodynamic station
- Simulated_data: contains results obtained by using OpenFAST2 program
 
  


