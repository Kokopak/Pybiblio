#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PySide import QtCore,  QtGui
import sys


class Diabook(QtGui.QDialog):

    def __init__(self):
        super(Diabook, self).__init__()
        self.initUi()

    def initUi(self):
        layout = QtGui.QGridLayout()

        self.aut_lab = QtGui.QLabel("Auteur: ")
        self.aut_line = QtGui.QLineEdit()
        self.tit_lab = QtGui.QLabel("Titre: ")
        self.tit_line = QtGui.QLineEdit()
        self.gen_lab = QtGui.QLabel("Genre: ")
        self.gen_line = QtGui.QLineEdit()
        self.com_lab = QtGui.QLabel("Commentaire: ")
        self.com_line = QtGui.QTextEdit()

        self.ok_bou = QtGui.QPushButton("Valider")
        self.ok_bou.clicked.connect(self.valid)


        layout.addWidget(self.aut_lab, 0, 0)
        layout.addWidget(self.aut_line, 1, 0)
        layout.addWidget(self.tit_lab, 2, 0)
        layout.addWidget(self.tit_line, 3, 0)
        layout.addWidget(self.gen_lab, 4, 0)
        layout.addWidget(self.gen_line, 5, 0)
        layout.addWidget(self.com_lab, 6, 0)
        layout.addWidget(self.com_line, 7, 0)
        layout.addWidget(self.ok_bou, 8, 0)


        self.setLayout(layout)
        self.setWindowTitle("PyBiblio")

    def valid(self):
        if self.aut_line.text() == "" or self.tit_line.text() == "" or self.gen_line.text() == "":
            msgBox = QtGui.QMessageBox()
            msgBox.warning(self, "Champ(s) incomplet(s)", "Champ(s) incomplet(s)")
            self.ignore()
        else:
            self.accept() 
