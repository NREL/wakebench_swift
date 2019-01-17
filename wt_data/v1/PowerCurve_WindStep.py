import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sys
try:
    # sys.path.append('C:/_libs/weio'); 
    import weio 
except:
    print('\n>>> This script needs the python package `weio` from https://github.com/ebranlard/weio\n')
    raise 


def powerCurvePostProWindStep(outfile,wndfile=None,tWindow=20,ColMap={},WS=None,KeepAll=False):
    def renameCol(x):
        for k,v in ColMap.items():
            if x==v:
                return k
        return x

    # --- Reading wind and output file
    print('Reading input...')
    out = weio.FASTOutFile(outfile).toDataFrame()
    wnd = weio.FASTWndFile(wndfile).toDataFrame()

    if len(ColMap)>0:
        out.rename(columns=renameCol,inplace=True)
    #units=['('s.split('[')[1].split(']')[0] for s in out.columns.values
    # --- Looping on wind values, and averaging data over a window
    if WS is None:
        WS = np.sort(np.unique(wnd['WindSpeed_[m/s]']))
    print(WS)
    tWS = out['WS_[m/s]'].values
    t   = out['Time_[s]'].values
    tol =0.01
    Iall = np.arange(len(t))
    result=None
    for i,ws in enumerate(WS):
        b = abs(tWS-ws)<tol
        I = Iall[b]
        iEnd = I[-1]
        tEnd = t[iEnd]
        tStart = t[iEnd]-tWindow
        IWindow=(t>tStart) & (t<tEnd)
        print('WS ',ws,' t ',tStart,'-', tEnd)
        MeanValues = pd.DataFrame(out[IWindow].mean()).transpose()
        if i==0:
            result = MeanValues.copy()
        else:
            result=result.append(MeanValues, ignore_index=True)

    # --- Sorting by WS
    result.sort_values(['WS_[m/s]'],inplace=True)
    result.reset_index(drop=True,inplace=True) 
    
    # --- Eliminating unnecessary columns
    if len(ColMap)>0 and (not KeepAll):
        ColNames = list(ColMap.keys())
    else:
        ColNames = result.columns.values
    result = result[ColNames]
    
    # --- Rounding
    result=result.round(4)
    #result.plot(x='Wind1VelX',y=I)
    #plt.show()
    return result 




# --------------------------------------------------------------------------------}
# --- Aero performances 
# --------------------------------------------------------------------------------{
# workdir='FAST7_model/'
# # OutFile=glob.glob(os.path.join(workdir,'*.outb'))[0]
# bTipLoss=True
# if bTipLoss:
#     WndFile = glob.glob(os.path.join(workdir,'Wind','*.wnd'))[0]
#     ElmFile = glob.glob(os.path.join(workdir,'SNLV27.elm'))[0]
#     ADFile  = glob.glob(os.path.join(workdir ,'SNLV27_AeroDyn.dat'))[0]
#     sFlag   = '_WithTipLoss'
# else:
#     WndFile = glob.glob(os.path.join(workdir,'Wind','*.wnd'))[0]
#     ElmFile = glob.glob(os.path.join(workdir,'SNL*_NoTL.elm'))[0]
#     ADFile  = glob.glob(os.path.join(workdir,'*AeroDyn*_NoTL.dat'))[0]
#     sFlag   = '_NoTipLoss'
# print(ElmFile)
# 
# 
# wnd = weio.FASTWndFile(WndFile).toDataFrame()
# # --- Aero Data
# ad = weio.FASTInFile(ADFile)
# r=ad['BldAeroNodes'][:,0]
# rho=ad['Rho']
# print('radius',r)
# print('rho',rho)
# 
# #WS=np.sort([11,10,9])
# WS=None
# ColMap = {}        
# ColMap['WS_[m/s]']        = 'VX20'
# ColMap['Time_[s]']        = 'Time'
# # 
# result = powerCurvePostProWindStep(ElmFile,WndFile,tWindow=20,ColMap=ColMap,WS=WS,KeepAll=True)
# result.to_csv('Simulated_data/AeroPerformances'+sFlag+'_unsorted.csv',sep='\t',index=False,float_format='%.4f')
# 
# WS = result['WS_[m/s]'].values
# 
# # Scaling Dynamic pressure to Vrel
# rho = 1.064032027823
# cols = [col for col in result.columns if 'DynPres' in col] 
# result[cols] = np.sqrt(2*result[cols]/1.06403)
# 
# # --- Rearranging by radius, category and wind speed
# 
# ColPatterns    = ['AxInd','TanInd','CNorm','CTang','Alpha','CLift','CDrag','DynPres']
# NewColPatterns = ['a'    ,'a\''   ,'Cn'   ,'Ct'   ,'Alpha','Cl'   ,'Cd'   ,'Vrel'   ]
# ColUnits       = ['-'    ,'-'     ,'-'    ,'-'    ,'deg'  ,'-'    ,'-'    ,'m/s'    ]
# 
# cols = [[col for col in result.columns if cp in col] for cp in ColPatterns]
# 
# df=pd.DataFrame(data=r,columns=['r_[m]'])
# for i in range(len(ColPatterns)):
#     A=result[cols[i]].transpose().copy()
#     A.reset_index(drop=True,inplace=True)
#     A.columns=['{}_(ws={})_[{}]'.format(NewColPatterns[i],ws,ColUnits[i]) for ws in WS]
#     df=pd.concat([df, A], axis=1)
# 
# df.to_csv('Simulated_data/AeroPerformances'+sFlag+'.csv',sep='\t',index=False,float_format='%.4f')
# 


# --------------------------------------------------------------------------------}
# --- Operating conditions 
# --------------------------------------------------------------------------------{
# --- Operating Conditions and Rotor Performances
bF7=False
if bF7:
    ColMap = {}        
    ColMap['WS_[m/s]']            = 'WindVxi_[m/s]'
    ColMap['RotSpeed_[rpm]']      = 'RotSpeed_[rpm]'
    ColMap['BldPitch_[deg]']      = 'BldPitch1_[deg]'
    ColMap['TSR_[-]']             = 'TSR_[-]'
    ColMap['AeroCp_[-]']          = 'RotCp_[-]'
    ColMap['AeroCt_[-]']          = 'RotCt_[-]'
    ColMap['AeroPower_[kW]']      = 'GenPwr_[kW]'
    ColMap['BldRootFlapM_[kN.m]'] = 'RootMyc1_[kN·m]'
#     ColMap['AeroThrust_[kN]']     = 'Rt[kN]'
    ColMap['Thrust_[kN]']         = 'LSShftFxa_[kN]'
else:
    ColMap = {}        
    ColMap['WS_[m/s]']            = 'Wind1VelX_[m/s]'
    ColMap['RotSpeed_[rpm]']      = 'RotSpeed_[rpm]'
    ColMap['BldPitch_[deg]']      = 'BldPitch1_[deg]'
    ColMap['TSR_[-]']             = 'RtTSR_[-]'
    ColMap['AeroCp_[-]']          = 'RtAeroCp_[-]'
    ColMap['AeroCt_[-]']          = 'RtAeroCt_[-]'
    ColMap['AeroPower_[kW]']      = 'GenPwr_[kW]'
    ColMap['BldRootFlapM_[kN.m]'] = 'RootMyc1_[kN-m]'
    ColMap['AeroThrust_[kN]']     = 'RtAeroFxh_[N]' # have to scale it
    ColMap['Thrust_[kN]']         = 'LSShftFxa_[kN]'

WndFile='FAST7_model/Wind/StepWindSweep_m1mps.wnd'
if bF7:
    OutFile='FAST7_model/SNLV27_F7.outb'
    suffix='_F7'
else:
    OutFile='OpenFAST_model/SNLV27_OF2.outb'
    suffix='_OF2'


# --- Compute mean values as function of wind speed
result = powerCurvePostProWindStep(OutFile,WndFile,20,ColMap)
result['AeroThrust_[kN]']= result['AeroThrust_[kN]']/1000
result['WS_[m/s]']= np.round(result['WS_[m/s]']*10)/10
print(result)

# --- Export Operating conditions
ICond=['WS_[m/s]','RotSpeed_[rpm]','BldPitch_[deg]']                             
result[ICond].to_csv('Raw_model/OperatingConditions'+suffix+'.csv'   ,sep='\t',index=False,float_format='%.4f')

# --- Export rotor performances

result.to_csv       ('Simulated_data/RotorPerformances'+suffix+'.csv',sep='\t',index=False,float_format='%.4f')







