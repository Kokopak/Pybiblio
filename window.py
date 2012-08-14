#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PySide import QtGui
import sys
from model import Livre, session
import diabook


class Window(QtGui.QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.initUi()

    def initUi(self):
        a = session.query(Livre).all()

        layout = QtGui.QGridLayout()
        self.liste = QtGui.QListWidget()

        for el in a:
            self.liste.addItem(el.titre)

        self.add_livre = QtGui.QPushButton("Ajouter un livre")
        self.add_livre.clicked.connect(self.add_book)
        self.del_livre = QtGui.QPushButton("Supprimer ce livre")
        self.del_livre.clicked.connect(self.del_book)
        self.edi_livre = QtGui.QPushButton("Editer ce livre")
        self.edi_livre.clicked.connect(self.edi_book)

        layout.addWidget(self.liste, 0, 1)
        layout.addWidget(self.add_livre, 1, 1)
        layout.addWidget(self.del_livre, 2, 1)
        layout.addWidget(self.edi_livre, 3, 1)

        self.setLayout(layout)
        self.setWindowTitle("PyBiblio")
        self.setWindowIcon(QtGui.QIcon('book.png'))
        self.show()

    def add_book(self):

        el = diabook.Diabook()
        el.exec_()

        auteur = el.aut_line.text()
        titre = el.tit_line.text()
        genre = el.gen_line.text()
        
        a = Livre(auteur, titre, genre)
        session.add(a)
        session.commit()
        self.liste.addItem(titre)

    def del_book(self):
        a = self.liste.currentItem().text()
        b = session.query(Livre).filter_by(titre = a).first()
        session.delete(b)
        item = self.liste.takeItem(self.liste.currentRow())
        item = None
        msgbox = QtGui.QMessageBox()
        msgbox.information(self, "Suppression", (u"Le livre: \"%s\" a bien était supprimé !" % unicode(a)))

    def edi_book(self):
        a = self.liste.currentItem().text()
        b = session.query(Livre).filter_by(titre = a).first()
        el = diabook.Diabook() 
        el.exec_()

        auteur = el.aut_line.text()
        titre = el.tit_line.text()
        genre = el.gen_line.text()

        b.auteur = auteur
        b.titre = titre
        b.genre = genre

        session.commit()
        item = self.liste.takeItem(self.liste.currentRow())
        item.setText(titre)
        self.liste.addItem(item)

def main():
    app = QtGui.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':  
    main()



