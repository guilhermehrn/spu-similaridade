# -*- coding: utf-8-*-

from shapely.geometry import *
from pylab import *
class BilbiotecaGeometria:

    def uniao(obj1, obj2):
        return obj1.union(obj2)

    def intersecao(obj1, obj2):
        return obj1.intersection(obj2)

    def calculoArea(obj):
        return obj.area

    def listarCoordenadas(obj):
        return list(obj.exterior.coords)

    def envelope(obj):
        return obj.bounds

    def fechoConvexo(obj):
        return obj.convex_hull

    def delaunay(obj):
        return triangulate(obj)

    def csi(obj_1, obj_2):
        return calculo_area(intersecao(obj_1, obj_2)) / calculo_area(uniao(obj_1, obj_2))

    def mre(obj_1, obj_2):
        P = obj_1.length - obj_2.length
        S = calculo_area(uniao(obj_1, obj_2)) - calculo_area(intersecao(obj_1, obj_2))
        return abs((-S + sqrt(S*S - 4* P))/2)