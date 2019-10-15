#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""DesignSPHysics Faces Configuration Dialog"""

from PySide import QtCore, QtGui

from mod.translation_tools import __

from mod.dataobjects.case import Case
from mod.dataobjects.simulation_object import SimulationObject
from mod.dataobjects.faces_property import FacesProperty


class FacesDialog(QtGui.QDialog):
    """ Defines a window with faces  """

    def __init__(self, selection_name, parent=None):
        super(FacesDialog, self).__init__(parent=parent)

        self.setWindowTitle(__("Faces configuration"))
        self.ok_button = QtGui.QPushButton(__("Ok"))
        self.cancel_button = QtGui.QPushButton(__("Cancel"))
        self.main_faces_layout = QtGui.QVBoxLayout()

        self.target_object: SimulationObject = Case.instance().get_simulation_object(selection_name)

        self.button_layout = QtGui.QHBoxLayout()
        self.button_layout.addWidget(self.ok_button)
        self.button_layout.addWidget(self.cancel_button)
        self.ok_button.clicked.connect(self.on_ok)
        self.cancel_button.clicked.connect(self.on_cancel)

        self.faces_layout = QtGui.QVBoxLayout()

        self.all_faces = QtGui.QCheckBox(__("All faces"))
        self.all_faces.setCheckState(QtCore.Qt.Checked)
        self.all_faces.toggled.connect(self.on_faces_checkbox)

        self.front_face = QtGui.QCheckBox(__("Front face"))
        self.back_face = QtGui.QCheckBox(__("Back face"))
        self.top_face = QtGui.QCheckBox(__("Top face"))
        self.bottom_face = QtGui.QCheckBox(__("Bottom face"))
        self.left_face = QtGui.QCheckBox(__("Left face"))
        self.right_face = QtGui.QCheckBox(__("Right face"))

        if self.target_object.faces_configuration:
            self.all_faces.setCheckState(QtCore.Qt.Checked if self.target_object.faces_configuration.all_faces else QtCore.Qt.Unchecked)
            self.front_face.setCheckState(QtCore.Qt.Checked if self.target_object.faces_configuration.front_face else QtCore.Qt.Unchecked)
            self.back_face.setCheckState(QtCore.Qt.Checked if self.target_object.faces_configuration.back_face else QtCore.Qt.Unchecked)
            self.top_face.setCheckState(QtCore.Qt.Checked if self.target_object.faces_configuration.top_face else QtCore.Qt.Unchecked)
            self.bottom_face.setCheckState(QtCore.Qt.Checked if self.target_object.faces_configuration.bottom_face else QtCore.Qt.Unchecked)
            self.left_face.setCheckState(QtCore.Qt.Checked if self.target_object.faces_configuration.left_face else QtCore.Qt.Unchecked)
            self.right_face.setCheckState(QtCore.Qt.Checked if self.target_object.faces_configuration.right_face else QtCore.Qt.Unchecked)
        
        self.all_faces.toggled.connect(self.on_faces_checkbox)

        self.faces_layout.addWidget(self.all_faces)
        self.faces_layout.addWidget(self.front_face)
        self.faces_layout.addWidget(self.back_face)
        self.faces_layout.addWidget(self.top_face)
        self.faces_layout.addWidget(self.bottom_face)
        self.faces_layout.addWidget(self.left_face)
        self.faces_layout.addWidget(self.right_face)

        self.main_faces_layout.addLayout(self.faces_layout)
        self.main_faces_layout.addLayout(self.button_layout)

        self.setLayout(self.main_faces_layout)

        self.on_faces_checkbox()

        self.exec_()

    def on_ok(self):

        fp = FacesProperty()
        fp.mk = self.target_object.mk

        if self.all_faces.isChecked():
            fp.all_faces = True
            fp.back_face = False
            fp.front_face = False
            fp.top_face = False
            fp.bottom_face = False
            fp.left_face = False
            fp.right_face = False
            fp.face_print = "all"
        else:
            fp.all_faces = False

            if self.front_face.isChecked():
                fp.front_face = True
                fp.face_print = "front"
            else:
                fp.front_face = False

            if self.back_face.isChecked():
                fp.back_face = True
                if fp.face_print != "":
                    fp.face_print += " | back"
                else:
                    fp.face_print = "back"
            else:
                fp.back_face = False

            if self.top_face.isChecked():
                fp.top_face = True
                if fp.face_print != "":
                    fp.face_print += " | top"
                else:
                    fp.face_print = "top"
            else:
                fp.top_face = False

            if self.bottom_face.isChecked():
                fp.bottom_face = True
                if fp.face_print != "":
                    fp.face_print += " | bottom"
                else:
                    fp.face_print = "bottom"
            else:
                fp.bottom_face = False

            if self.left_face.isChecked():
                fp.left_face = True
                if fp.face_print != "":
                    fp.face_print += " | left"
                else:
                    fp.face_print = "left"
            else:
                fp.left_face = False

            if self.right_face.isChecked():
                fp.right_face = True
                if fp.face_print != "":
                    fp.face_print += " | right"
                else:
                    fp.face_print = "right"
            else:
                fp.right_face = False

        self.target_object.faces_configuration = fp

        self.accept()

    def on_cancel(self):
        self.reject()

    def on_faces_checkbox(self):
        """ Checks the faces state """
        if self.all_faces.isChecked():
            self.front_face.setEnabled(False)
            self.back_face.setEnabled(False)
            self.top_face.setEnabled(False)
            self.bottom_face.setEnabled(False)
            self.left_face.setEnabled(False)
            self.right_face.setEnabled(False)
        else:
            self.front_face.setEnabled(True)
            self.back_face.setEnabled(True)
            self.top_face.setEnabled(True)
            self.bottom_face.setEnabled(True)
            self.left_face.setEnabled(True)
            self.right_face.setEnabled(True)
