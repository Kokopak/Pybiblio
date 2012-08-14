#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PySide import QtCore,  QtGui
import sys


class Diainfo(QtGui.QDialog):

    def __init__(self):
        super(Diainfo, self).__init__()
        self.initUi()

    def initUi(self):

        layout = QtGui.QGridLayout()
        self.aut_lab = QtGui.QLabel()
        self.tit_lab = QtGui.QLabel()
        self.gen_lab = QtGui.QLabel()

        layout.addWidget(self.aut_lab, 0, 0)
        layout.addWidget(self.tit_lab, 1, 0)
        layout.addWidget(self.gen_lab, 2, 0)


        self.setLayout(layout)
        self.setWindowTitle("PyBiblio")

