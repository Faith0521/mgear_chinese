"""Blueprint Tab UI - Tab for configuring blueprint guide inheritance."""

import mgear.core.pyqt as gqt
QtGui, QtCore, QtWidgets, wrapInstance = gqt.qt_import()


class Ui_BlueprintTab(object):
    """UI class for the Blueprint configuration tab."""

    def setupUi(self, Form):
        """Set up the UI widgets for the Blueprint tab.

        Args:
            Form: The parent widget/form to set up.
        """
        Form.setObjectName("BlueprintTab")
        Form.resize(500, 400)

        self.mainLayout = QtWidgets.QVBoxLayout(Form)
        self.mainLayout.setObjectName("mainLayout")

        # =====================================================================
        # Enable Blueprint GroupBox
        # =====================================================================
        self.blueprint_groupBox = QtWidgets.QGroupBox(Form)
        self.blueprint_groupBox.setObjectName("blueprint_groupBox")
        self.blueprint_groupBox.setTitle("Blueprint Guide")

        self.blueprint_layout = QtWidgets.QVBoxLayout(self.blueprint_groupBox)
        self.blueprint_layout.setObjectName("blueprint_layout")

        # Enable checkbox
        self.useBlueprint_checkBox = QtWidgets.QCheckBox(self.blueprint_groupBox)
        self.useBlueprint_checkBox.setObjectName("useBlueprint_checkBox")
        self.useBlueprint_checkBox.setText("Enable Blueprint Guide")
        self.useBlueprint_checkBox.setToolTip(
            "When enabled, settings will be inherited from the blueprint guide file.\n"
            "Use the 'Use Local Override' checkboxes on each section to customize specific settings."
        )
        self.blueprint_layout.addWidget(self.useBlueprint_checkBox)

        # Path selection layout
        self.path_layout = QtWidgets.QHBoxLayout()
        self.path_layout.setObjectName("path_layout")

        self.blueprint_label = QtWidgets.QLabel(self.blueprint_groupBox)
        self.blueprint_label.setObjectName("blueprint_label")
        self.blueprint_label.setText("蓝图路径:")
        self.path_layout.addWidget(self.blueprint_label)

        self.blueprint_lineEdit = QtWidgets.QLineEdit(self.blueprint_groupBox)
        self.blueprint_lineEdit.setObjectName("blueprint_lineEdit")
        self.blueprint_lineEdit.setPlaceholderText(".sgt文件的相对或绝对路径")
        self.blueprint_lineEdit.setToolTip(
            "蓝图引导模板(.sgt文件)的路径。\n\n"
            "支持:\n"
            "- 绝对路径: C:/projects/guides/blueprint.sgt\n"
            "- 相对路径: 使用MGEAR_SHIFTER_CUSTOMSTEP_PATH环境变量解析"
        )
        self.path_layout.addWidget(self.blueprint_lineEdit)

        self.blueprint_pushButton = QtWidgets.QPushButton(self.blueprint_groupBox)
        self.blueprint_pushButton.setObjectName("blueprint_pushButton")
        self.blueprint_pushButton.setText("...")
        self.blueprint_pushButton.setMaximumWidth(30)
        self.blueprint_pushButton.setToolTip("Browse for blueprint guide file")
        self.path_layout.addWidget(self.blueprint_pushButton)

        self.blueprint_layout.addLayout(self.path_layout)

        # Status label
        self.blueprint_status_label = QtWidgets.QLabel(self.blueprint_groupBox)
        self.blueprint_status_label.setObjectName("blueprint_status_label")
        self.blueprint_status_label.setText("")
        self.blueprint_status_label.setWordWrap(True)
        self.blueprint_layout.addWidget(self.blueprint_status_label)

        self.mainLayout.addWidget(self.blueprint_groupBox)

        # =====================================================================
        # Information GroupBox
        # =====================================================================
        self.info_groupBox = QtWidgets.QGroupBox(Form)
        self.info_groupBox.setObjectName("info_groupBox")
        self.info_groupBox.setTitle("蓝图引导工作原理")

        self.info_layout = QtWidgets.QVBoxLayout(self.info_groupBox)
        self.info_layout.setObjectName("info_layout")

        self.info_label = QtWidgets.QLabel(self.info_groupBox)
        self.info_label.setObjectName("info_label")
        self.info_label.setWordWrap(True)
        self.info_label.setText(
            "<p><b>蓝图引导</b>是一个序列化的引导模板(.sgt文件)，"
            "作为骨骼设置的基础配置。</p>"
            "<p><b>工作原理:</b></p>"
            "<ol>"
            "<li>启用蓝图并选择一个.sgt文件</li>"
            "<li>默认情况下，所有部分将从蓝图继承设置</li>"
            "<li>使用每个部分上的'本地覆盖'复选框来自定义特定设置</li>"
            "<li>当某个部分被覆盖时，它将使用本地值而非蓝图值</li>"
            "</ol>"
            "<p><b>优势:</b></p>"
            "<ul>"
            "<li>在多个角色之间标准化骨骼设置</li>"
            "<li>仅覆盖每个角色不同的部分</li>"
            "<li>对蓝图的更改会自动传播到使用它的所有角色</li>"
            "</ul>"
        )
        self.info_layout.addWidget(self.info_label)

        self.mainLayout.addWidget(self.info_groupBox)

        # =====================================================================
        # Bottom Spacer
        # =====================================================================
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.mainLayout.addItem(spacerItem)

        QtCore.QMetaObject.connectSlotsByName(Form)
