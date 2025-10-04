# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uiitxgpz.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QSplitter, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(723, 564)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 20))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setBaseSize(QSize(0, 0))
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionNext = QAction(MainWindow)
        self.actionNext.setObjectName(u"actionNext")
        self.actionNext.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.actionPrevious = QAction(MainWindow)
        self.actionPrevious.setObjectName(u"actionPrevious")
        self.actionPrevious.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionCapture = QAction(MainWindow)
        self.actionCapture.setObjectName(u"actionCapture")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainSplitter = QSplitter(self.centralwidget)
        self.mainSplitter.setObjectName(u"mainSplitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainSplitter.sizePolicy().hasHeightForWidth())
        self.mainSplitter.setSizePolicy(sizePolicy1)
        self.mainSplitter.setOrientation(Qt.Orientation.Horizontal)
        self.leftSplitter = QSplitter(self.mainSplitter)
        self.leftSplitter.setObjectName(u"leftSplitter")
        self.leftSplitter.setOrientation(Qt.Orientation.Vertical)
        self.frame_pdf = QFrame(self.leftSplitter)
        self.frame_pdf.setObjectName(u"frame_pdf")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.frame_pdf.sizePolicy().hasHeightForWidth())
        self.frame_pdf.setSizePolicy(sizePolicy2)
        self.frame_pdf.setMinimumSize(QSize(0, 0))
        self.frame_pdf.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pdf.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_pdf)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_pdf = QScrollArea(self.frame_pdf)
        self.scrollArea_pdf.setObjectName(u"scrollArea_pdf")
        self.scrollArea_pdf.setWidgetResizable(True)
        self.scrollAreaWidgetContents_pdf = QWidget()
        self.scrollAreaWidgetContents_pdf.setObjectName(u"scrollAreaWidgetContents_pdf")
        self.scrollAreaWidgetContents_pdf.setGeometry(QRect(0, 0, 278, 315))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_pdf)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pdf_render_label = QLabel(self.scrollAreaWidgetContents_pdf)
        self.pdf_render_label.setObjectName(u"pdf_render_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pdf_render_label.sizePolicy().hasHeightForWidth())
        self.pdf_render_label.setSizePolicy(sizePolicy3)
        self.pdf_render_label.setMouseTracking(True)
        self.pdf_render_label.setAutoFillBackground(False)
        self.pdf_render_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.pdf_render_label)

        self.scrollArea_pdf.setWidget(self.scrollAreaWidgetContents_pdf)

        self.verticalLayout_2.addWidget(self.scrollArea_pdf)

        self.leftSplitter.addWidget(self.frame_pdf)
        self.frame_image = QFrame(self.leftSplitter)
        self.frame_image.setObjectName(u"frame_image")
        self.frame_image.setMinimumSize(QSize(300, 0))
        self.frame_image.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_image.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_image)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_image = QLabel(self.frame_image)
        self.label_image.setObjectName(u"label_image")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy4)
        self.label_image.setMinimumSize(QSize(0, 100))
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_image)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_editor_imagePath = QLabel(self.frame_image)
        self.lbl_editor_imagePath.setObjectName(u"lbl_editor_imagePath")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lbl_editor_imagePath.sizePolicy().hasHeightForWidth())
        self.lbl_editor_imagePath.setSizePolicy(sizePolicy5)
        self.lbl_editor_imagePath.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_editor_imagePath)

        self.le_editor_imagePath = QLineEdit(self.frame_image)
        self.le_editor_imagePath.setObjectName(u"le_editor_imagePath")
        self.le_editor_imagePath.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.le_editor_imagePath)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.leftSplitter.addWidget(self.frame_image)
        self.mainSplitter.addWidget(self.leftSplitter)
        self.tab_editor = QTabWidget(self.mainSplitter)
        self.tab_editor.setObjectName(u"tab_editor")
        sizePolicy3.setHeightForWidth(self.tab_editor.sizePolicy().hasHeightForWidth())
        self.tab_editor.setSizePolicy(sizePolicy3)
        self.tab_editor.setMinimumSize(QSize(400, 0))
        self.tab_editor.setMaximumSize(QSize(700, 16777215))
        self.questionTab = QWidget()
        self.questionTab.setObjectName(u"questionTab")
        self.verticalLayout_4 = QVBoxLayout(self.questionTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.questionSplitter = QSplitter(self.questionTab)
        self.questionSplitter.setObjectName(u"questionSplitter")
        self.questionSplitter.setOrientation(Qt.Orientation.Vertical)
        self.questionPreviewFrame = QFrame(self.questionSplitter)
        self.questionPreviewFrame.setObjectName(u"questionPreviewFrame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.questionPreviewFrame.sizePolicy().hasHeightForWidth())
        self.questionPreviewFrame.setSizePolicy(sizePolicy6)
        self.questionPreviewFrame.setMinimumSize(QSize(0, 100))
        self.questionPreviewFrame.setBaseSize(QSize(0, 0))
        self.questionPreviewFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.questionPreviewFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_preview = QFormLayout(self.questionPreviewFrame)
        self.formLayout_preview.setObjectName(u"formLayout_preview")
        self.preview_groupBox = QGroupBox(self.questionPreviewFrame)
        self.preview_groupBox.setObjectName(u"preview_groupBox")
        self.gridLayout = QGridLayout(self.preview_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.preview_options_gridLayout = QGridLayout()
        self.preview_options_gridLayout.setObjectName(u"preview_options_gridLayout")
        self.we_question = QWebEngineView(self.preview_groupBox)
        self.we_question.setObjectName(u"we_question")
        sizePolicy6.setHeightForWidth(self.we_question.sizePolicy().hasHeightForWidth())
        self.we_question.setSizePolicy(sizePolicy6)
        self.we_question.setMinimumSize(QSize(0, 20))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(8)
        self.we_question.setFont(font)
        self.we_question.setAutoFillBackground(True)
        self.we_question.setUrl(QUrl(u"about:blank"))

        self.preview_options_gridLayout.addWidget(self.we_question, 1, 0, 1, 2)

        self.horizontalLayout_goto = QHBoxLayout()
        self.horizontalLayout_goto.setObjectName(u"horizontalLayout_goto")
        self.label_goto = QLabel(self.preview_groupBox)
        self.label_goto.setObjectName(u"label_goto")

        self.horizontalLayout_goto.addWidget(self.label_goto)

        self.spinBox_goto_question = QSpinBox(self.preview_groupBox)
        self.spinBox_goto_question.setObjectName(u"spinBox_goto_question")

        self.horizontalLayout_goto.addWidget(self.spinBox_goto_question)

        self.label_total_questions = QLabel(self.preview_groupBox)
        self.label_total_questions.setObjectName(u"label_total_questions")
        self.label_total_questions.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_goto.addWidget(self.label_total_questions)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_goto.addItem(self.horizontalSpacer)


        self.preview_options_gridLayout.addLayout(self.horizontalLayout_goto, 0, 0, 1, 2)


        self.gridLayout.addLayout(self.preview_options_gridLayout, 0, 0, 1, 1)


        self.formLayout_preview.setWidget(0, QFormLayout.ItemRole.FieldRole, self.preview_groupBox)

        self.questionSplitter.addWidget(self.questionPreviewFrame)
        self.questionEditorFrame = QFrame(self.questionSplitter)
        self.questionEditorFrame.setObjectName(u"questionEditorFrame")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.questionEditorFrame.sizePolicy().hasHeightForWidth())
        self.questionEditorFrame.setSizePolicy(sizePolicy7)
        self.questionEditorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.questionEditorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.editor_formLayout = QFormLayout(self.questionEditorFrame)
        self.editor_formLayout.setObjectName(u"editor_formLayout")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.editor_options_groupBox = QGroupBox(self.questionEditorFrame)
        self.editor_options_groupBox.setObjectName(u"editor_options_groupBox")
        self.editor_options_gridLayout = QGridLayout(self.editor_options_groupBox)
        self.editor_options_gridLayout.setObjectName(u"editor_options_gridLayout")
        self.editor_option1_label = QLabel(self.editor_options_groupBox)
        self.editor_option1_label.setObjectName(u"editor_option1_label")

        self.editor_options_gridLayout.addWidget(self.editor_option1_label, 1, 0, 1, 1)

        self.editor_option1_lineEdit = QLineEdit(self.editor_options_groupBox)
        self.editor_option1_lineEdit.setObjectName(u"editor_option1_lineEdit")

        self.editor_options_gridLayout.addWidget(self.editor_option1_lineEdit, 1, 1, 1, 1)

        self.editor_option3_label = QLabel(self.editor_options_groupBox)
        self.editor_option3_label.setObjectName(u"editor_option3_label")

        self.editor_options_gridLayout.addWidget(self.editor_option3_label, 3, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.editor_options_gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.editor_option2_label = QLabel(self.editor_options_groupBox)
        self.editor_option2_label.setObjectName(u"editor_option2_label")

        self.editor_options_gridLayout.addWidget(self.editor_option2_label, 2, 0, 1, 1)

        self.editor_option4_label = QLabel(self.editor_options_groupBox)
        self.editor_option4_label.setObjectName(u"editor_option4_label")

        self.editor_options_gridLayout.addWidget(self.editor_option4_label, 4, 0, 1, 1)

        self.editor_option2_lineEdit = QLineEdit(self.editor_options_groupBox)
        self.editor_option2_lineEdit.setObjectName(u"editor_option2_lineEdit")

        self.editor_options_gridLayout.addWidget(self.editor_option2_lineEdit, 2, 1, 1, 1)

        self.editor_option3_lineEdit = QLineEdit(self.editor_options_groupBox)
        self.editor_option3_lineEdit.setObjectName(u"editor_option3_lineEdit")

        self.editor_options_gridLayout.addWidget(self.editor_option3_lineEdit, 3, 1, 1, 1)

        self.editor_option4_lineEdit = QLineEdit(self.editor_options_groupBox)
        self.editor_option4_lineEdit.setObjectName(u"editor_option4_lineEdit")

        self.editor_options_gridLayout.addWidget(self.editor_option4_lineEdit, 4, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.editor_options_groupBox)


        self.editor_formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.verticalLayout_7)

        self.editor_metadata_gridLayout = QGridLayout()
        self.editor_metadata_gridLayout.setObjectName(u"editor_metadata_gridLayout")
        self.le_editor_answer = QLineEdit(self.questionEditorFrame)
        self.le_editor_answer.setObjectName(u"le_editor_answer")
        sizePolicy5.setHeightForWidth(self.le_editor_answer.sizePolicy().hasHeightForWidth())
        self.le_editor_answer.setSizePolicy(sizePolicy5)
        self.le_editor_answer.setMinimumSize(QSize(20, 0))
        self.le_editor_answer.setMaximumSize(QSize(30, 16777215))

        self.editor_metadata_gridLayout.addWidget(self.le_editor_answer, 0, 1, 1, 1)

        self.lbl_editor_answer = QLabel(self.questionEditorFrame)
        self.lbl_editor_answer.setObjectName(u"lbl_editor_answer")

        self.editor_metadata_gridLayout.addWidget(self.lbl_editor_answer, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.questionEditorFrame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.editor_metadata_gridLayout.addWidget(self.lineEdit, 0, 3, 1, 1)

        self.lbl_remark = QLabel(self.questionEditorFrame)
        self.lbl_remark.setObjectName(u"lbl_remark")

        self.editor_metadata_gridLayout.addWidget(self.lbl_remark, 0, 2, 1, 1)


        self.editor_formLayout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.editor_metadata_gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.editor_question_groupBox = QGroupBox(self.questionEditorFrame)
        self.editor_question_groupBox.setObjectName(u"editor_question_groupBox")
        self.verticalLayout_10 = QVBoxLayout(self.editor_question_groupBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.txt_editor_question = QTextEdit(self.editor_question_groupBox)
        self.txt_editor_question.setObjectName(u"txt_editor_question")
        self.txt_editor_question.setMinimumSize(QSize(0, 50))
        self.txt_editor_question.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.txt_editor_question.setTabChangesFocus(True)

        self.verticalLayout_10.addWidget(self.txt_editor_question)


        self.verticalLayout.addWidget(self.editor_question_groupBox)


        self.editor_formLayout.setLayout(0, QFormLayout.ItemRole.FieldRole, self.verticalLayout)

        self.questionSplitter.addWidget(self.questionEditorFrame)

        self.verticalLayout_4.addWidget(self.questionSplitter)

        self.tab_editor.addTab(self.questionTab, "")
        self.tableTab = QWidget()
        self.tableTab.setObjectName(u"tableTab")
        self.verticalLayout_5 = QVBoxLayout(self.tableTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableSplitter = QSplitter(self.tableTab)
        self.tableSplitter.setObjectName(u"tableSplitter")
        self.tableSplitter.setOrientation(Qt.Orientation.Vertical)
        self.tablePreviewFrame = QFrame(self.tableSplitter)
        self.tablePreviewFrame.setObjectName(u"tablePreviewFrame")
        sizePolicy2.setHeightForWidth(self.tablePreviewFrame.sizePolicy().hasHeightForWidth())
        self.tablePreviewFrame.setSizePolicy(sizePolicy2)
        self.tablePreviewFrame.setMinimumSize(QSize(0, 100))
        self.tablePreviewFrame.setBaseSize(QSize(0, 506))
        self.tablePreviewFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.tablePreviewFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.tablePreviewFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.we_match = QWebEngineView(self.tablePreviewFrame)
        self.we_match.setObjectName(u"we_match")
        sizePolicy2.setHeightForWidth(self.we_match.sizePolicy().hasHeightForWidth())
        self.we_match.setSizePolicy(sizePolicy2)
        self.we_match.setMinimumSize(QSize(0, 0))
        self.we_match.setBaseSize(QSize(0, 400))
        self.we_match.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_8.addWidget(self.we_match)

        self.tableSplitter.addWidget(self.tablePreviewFrame)
        self.tableEditorFrame = QFrame(self.tableSplitter)
        self.tableEditorFrame.setObjectName(u"tableEditorFrame")
        self.tableEditorFrame.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.tableEditorFrame.sizePolicy().hasHeightForWidth())
        self.tableEditorFrame.setSizePolicy(sizePolicy2)
        self.tableEditorFrame.setMinimumSize(QSize(0, 0))
        self.tableEditorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableEditorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.tableEditorFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tbl_match = QTableWidget(self.tableEditorFrame)
        if (self.tbl_match.columnCount() < 2):
            self.tbl_match.setColumnCount(2)
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font1);
        self.tbl_match.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem1.setFont(font1);
        self.tbl_match.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tbl_match.rowCount() < 4):
            self.tbl_match.setRowCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_match.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_match.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_match.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_match.setVerticalHeaderItem(3, __qtablewidgetitem5)
        self.tbl_match.setObjectName(u"tbl_match")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.tbl_match.sizePolicy().hasHeightForWidth())
        self.tbl_match.setSizePolicy(sizePolicy8)
        self.tbl_match.setMinimumSize(QSize(0, 0))
        self.tbl_match.setEditTriggers(QAbstractItemView.EditTrigger.CurrentChanged)
        self.tbl_match.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_match.horizontalHeader().setStretchLastSection(False)
        self.tbl_match.verticalHeader().setVisible(False)
        self.tbl_match.verticalHeader().setHighlightSections(False)

        self.verticalLayout_6.addWidget(self.tbl_match)

        self.tableSplitter.addWidget(self.tableEditorFrame)

        self.verticalLayout_5.addWidget(self.tableSplitter)

        self.tab_editor.addTab(self.tableTab, "")
        self.mainSplitter.addWidget(self.tab_editor)

        self.horizontalLayout.addWidget(self.mainSplitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 723, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.actionOpen)
        self.menubar.addAction(self.actionNext)
        self.menubar.addAction(self.actionPrevious)
        self.menubar.addAction(self.actionCapture)
        self.menubar.addAction(self.actionSave)

        self.retranslateUi(MainWindow)

        self.tab_editor.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Data Checker", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
#if QT_CONFIG(shortcut)
        self.actionNext.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Down", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrevious.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
#if QT_CONFIG(shortcut)
        self.actionPrevious.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionCapture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
#if QT_CONFIG(shortcut)
        self.actionCapture.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+C", None))
#endif // QT_CONFIG(shortcut)
        self.pdf_render_label.setText(QCoreApplication.translate("MainWindow", u"PDF render will appear here", None))
        self.label_image.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.lbl_editor_imagePath.setText(QCoreApplication.translate("MainWindow", u"Image path", None))
        self.preview_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.label_goto.setText(QCoreApplication.translate("MainWindow", u"Question:", None))
        self.label_total_questions.setText(QCoreApplication.translate("MainWindow", u"/ 180", None))
        self.editor_options_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.editor_option1_label.setText(QCoreApplication.translate("MainWindow", u"1.", None))
        self.editor_option3_label.setText(QCoreApplication.translate("MainWindow", u"3.", None))
        self.editor_option2_label.setText(QCoreApplication.translate("MainWindow", u"2.", None))
        self.editor_option4_label.setText(QCoreApplication.translate("MainWindow", u"4.", None))
        self.lbl_editor_answer.setText(QCoreApplication.translate("MainWindow", u"Answer", None))
        self.lbl_remark.setText(QCoreApplication.translate("MainWindow", u"Remark", None))
        self.editor_question_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Question", None))
        self.tab_editor.setTabText(self.tab_editor.indexOf(self.questionTab), QCoreApplication.translate("MainWindow", u"Question", None))
        ___qtablewidgetitem = self.tbl_match.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Column I", None));
        ___qtablewidgetitem1 = self.tbl_match.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Column II", None));
        self.tab_editor.setTabText(self.tab_editor.indexOf(self.tableTab), QCoreApplication.translate("MainWindow", u"Table", None))
    # retranslateUi

