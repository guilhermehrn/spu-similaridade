# -*- coding: utf-8-*-

from shapely.geometry import *
from pylab import *

class BilbiotecaGeometria:

    def uniao(self, obj1, obj2):
        return obj1.union(obj2)

    def intersecao(self, obj1, obj2):
        return obj1.intersection(obj2)

    def calculoArea(self, obj):
        return obj.area

    def listarCoordenadas(self, obj):
        return list(obj.exterior.coords)

    def envelope(self,obj):
        return obj.bounds

    def fechoConvexo(self,obj):
        return obj.convex_hull

    def delaunay(self,obj):
        return triangulate(obj)

    def csi(self, obj_1, obj_2):
        return self.calculoArea(self.intersecao(obj_1, obj_2)) / self.calculoArea(self.uniao(obj_1, obj_2))

    def mre(obj_1, obj_2):
        P = obj_1.length - obj_2.length
        S = calculoArea(uniao(obj_1, obj_2)) - calculoArea(intersecao(obj_1, obj_2))
        return abs((-S + sqrt(S*S - 4* P))/2)