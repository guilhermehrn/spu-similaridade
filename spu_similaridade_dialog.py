# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SpuSimilaridadeDialog
                                 A QGIS plugin
 Análise de Similaridade 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-12-20
        git sha              : $Format:%H$
        copyright            : (C) 2019 by SPU
        email                : guilherme@dcc.ufmg.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import QgsProject
from .biblioteca_geometria import *

import shapely.wkt
# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'spu_similaridade_dialog_base.ui'))


class SpuSimilaridadeDialog(QtWidgets.QDialog, FORM_CLASS):

    def __init__ (self, iface, parent=None):
        """Constructor."""

        super(SpuSimilaridadeDialog, self).__init__(parent)

        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        self.iface = iface


        self.tuplaCamadaSelecionada1 = (0,'')
        self.tuplaCamadaSelecionada2 = (0,'')

        self.calcular.clicked.connect(self.calcularSimilaridade)

        #layers = QgsProject.instance().layerTreeRoot().findLayers()



        layers = iface.mapCanvas().layers()
        #print(layers)
        layer_list = []

        for layer in layers:
            layer_list.append(layer.name())

        self.camada1.addItems(layer_list)
        self.camada2.addItems(layer_list)


    def calcularSimilaridade(self):

        self.tuplaCamadaSelecionada1 = (self.camada1.currentIndex(), self.camada1.currentText())
        self.tuplaCamadaSelecionada2 = (self.camada2.currentIndex(), self.camada2.currentText())

        qlayerGeo1 = self.iface.mapCanvas().layer(self.tuplaCamadaSelecionada1[0]).getFeature(0).geometry().asWkt()
        qlayerGeo2 = self.iface.mapCanvas().layer(self.tuplaCamadaSelecionada2[0]).getFeature(0).geometry().asWkt()


        libGeometria = BibliotecaGeometria()

        layerObj1 = shapely.wkt.loads(qlayerGeo1)
        layerObj2 = shapely.wkt.loads(qlayerGeo2)

        csi = libGeometria.csi(layerObj1, layerObj2)
        mre = libGeometria.mre(layerObj1, layerObj2)

        self.textBrowser.clear()
        self.textBrowser_2.clear()

        self.textBrowser.insertPlainText(str(csi * 100) + "%")
        self.textBrowser_2.insertPlainText(str(mre))


        #print (csi, self.tuplaCamadaSelecionada1, layerObj1, layerObj2)



