import numpy as np
from sklearn.neighbors import KDTree

class ReverseGeocoder():

    def __init__(self, geo_data):
        self.geo_data = geo_data

        coord_arr = np.asarray(list((d[3], d[4]) for d in self.geo_data))

        self.tree = KDTree(coord_arr)

    def nearest_geodata(self, lon, lat):
        value = (lon, lat)

        index = self.tree.query([value])[1][0][0]

        return self.geo_data[index]
