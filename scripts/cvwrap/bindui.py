import maya.cmds as cmds
if cmds.about(api=True) >= 201700:
    from PySide2 import QtWidgets as QtGui
else:
    from PySide import QtGui
from functools import partial
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

_win = None
def show():
    global _win
    if _win == None:
        _win = BindingDialog()
    _win.show()


class BindingDialog(MayaQWidgetBaseMixin, QtGui.QDialog):

    def __init__(self, parent=None):
        super(BindingDialog, self).__init__(parent)
        self.resize(600, 200)
        self.setWindowTitle('cvWrap 重新绑定')
        vbox = QtGui.QVBoxLayout(self)

        label_width = 130

        hbox = QtGui.QHBoxLayout()
        vbox.addLayout(hbox)
        label = QtGui.QLabel('要重新绑定的组件:')
        label.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        label.setMinimumWidth(label_width)
        label.setMaximumWidth(label_width)
        hbox.addWidget(label)
        self.components_to_rebind = QtGui.QLineEdit()
        self.components_to_rebind.textChanged.connect(self.populate_cvwrap_dropdown)
        hbox.addWidget(self.components_to_rebind)
        button = QtGui.QPushButton('设置组件')
        button.released.connect(partial(self.set_selected_text, widget=self.components_to_rebind))
        hbox.addWidget(button)

        hbox = QtGui.QHBoxLayout()
        vbox.addLayout(hbox)
        label = QtGui.QLabel('要重新绑定到的面:')
        label.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        label.setMinimumWidth(label_width)
        label.setMaximumWidth(label_width)
        hbox.addWidget(label)
        self.target_faces = QtGui.QLineEdit()
        hbox.addWidget(self.target_faces)
        button = QtGui.QPushButton('设置面')
        button.released.connect(partial(self.set_selected_text, widget=self.target_faces))
        hbox.addWidget(button)

        hbox = QtGui.QHBoxLayout()
        vbox.addLayout(hbox)
        label = QtGui.QLabel('cvWrap节点:')
        label.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        label.setMinimumWidth(label_width)
        label.setMaximumWidth(label_width)
        hbox.addWidget(label)
        self.cvwrap_combo = QtGui.QComboBox()
        hbox.addWidget(self.cvwrap_combo)

        hbox = QtGui.QHBoxLayout()
        vbox.addLayout(hbox)
        label = QtGui.QLabel('采样半径:')
        label.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        label.setMinimumWidth(label_width)
        label.setMaximumWidth(label_width)
        hbox.addWidget(label)
        self.sample_radius = QtGui.QDoubleSpinBox()
        self.sample_radius.setValue(0.1)
        self.sample_radius.setRange(0, 100)
        self.sample_radius.setDecimals(2)
        self.sample_radius.setSingleStep(.1)
        hbox.addWidget(self.sample_radius)

        vbox.addStretch()

        hbox = QtGui.QHBoxLayout()
        vbox.addLayout(hbox)
        button = QtGui.QPushButton('重新绑定')
        button.released.connect(self.rebind)
        hbox.addWidget(button)

    def set_selected_text(self, widget):
        sel = cmds.ls(sl=True)
        text = ' '.join(sel)
        widget.setText(text)

    def populate_cvwrap_dropdown(self, text):
        node = text.split()
        if not node:
            return
        node = node[0].split('.')
        if not node:
            return
        node = node[0]
        wrap_nodes = [x for x in cmds.listHistory(node, pdo=True) or []
                      if cmds.nodeType(x) == 'cvWrap']
        self.cvwrap_combo.clear()
        self.cvwrap_combo.addItems(wrap_nodes)

    def rebind(self):
        components = self.components_to_rebind.text().split()
        faces = self.target_faces.text().split()
        wrap_node = self.cvwrap_combo.currentText()
        radius = self.sample_radius.value()
        # Make sure the faces are actual faces.  If they are not, convert to faces.
        cmds.select(faces)
        cmds.ConvertSelectionToFaces()
        faces = cmds.ls(sl=True)

        cmds.select(components)
        cmds.ConvertSelectionToVertices()
        cmds.select(faces, add=True)
        cmds.cvWrap(rb=wrap_node, radius=radius)
        print 'Rebounded vertices'

