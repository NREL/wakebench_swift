import numpy as np
from copy import deepcopy
from floris.simulation import Floris
from floris.utilities import Vec3

class MyFlorisInterface(object):

    def __init__(self,inputfile,D=27.0,zhub=32.1,sampling_resolution=1.0):
        self.D = D
        self.zhub = zhub
        self.ds = sampling_resolution
        self.flor = Floris(inputfile)

    def update_flow(self,**kwargs):
        self.flor.farm.flow_field.reinitialize_flow_field(**kwargs)

    def get_horizontal_profile(self, x_D):
        ff = deepcopy(self.flor.farm.flow_field)
        bounds = (
            x_D*self.D, x_D*self.D,
            -1.5*self.D, 1.5*self.D,
            self.zhub, self.zhub
        )
        Ny = 1 + (bounds[3] - bounds[2])/self.ds
        res = Vec3(1, Ny, 1)
        #print(res)
        ff.reinitialize_flow_field(bounds_to_set=bounds, with_resolution=res)
        ff.calculate_wake()
        assert np.min(ff.x) == np.max(ff.x)
        assert np.min(ff.z) == np.max(ff.z)
        return np.squeeze(ff.y), np.squeeze(ff.u)

    def get_vertical_profile(self, x_D):
        ff = deepcopy(self.flor.farm.flow_field)
        bounds = (
            x_D*self.D, x_D*self.D,
            0, 0,
            self.zhub - self.D, self.zhub + 2*self.D,
        )
        Nz = 1 + (bounds[5] - bounds[4])/self.ds
        res = Vec3(1, 1, Nz)
        #print(res)
        ff.reinitialize_flow_field(bounds_to_set=bounds, with_resolution=res)
        ff.calculate_wake()
        assert np.min(ff.x) == np.max(ff.x)
        assert np.min(ff.y) == np.max(ff.y)
        return np.squeeze(ff.z), np.squeeze(ff.u)

    def get_downstream_plane(self, x_D):
        ff = deepcopy(self.flor.farm.flow_field)
        bounds = (
            x_D*self.D, x_D*self.D,
            -2*self.D, 2*self.D,
            self.zhub-self.D, self.zhub+2*self.D,
        )
        Ny = 1 + (bounds[3] - bounds[2])/self.ds
        Nz = 1 + (bounds[5] - bounds[4])/self.ds
        res = Vec3(1, Ny, Nz)
        #print(res)
        ff.reinitialize_flow_field(bounds_to_set=bounds, with_resolution=res)
        ff.calculate_wake()
        assert np.min(ff.x) == np.max(ff.x)
        return np.squeeze(ff.y), np.squeeze(ff.z), np.squeeze(ff.u)
