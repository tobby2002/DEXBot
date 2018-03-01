# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bot_item_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.setEnabled(True)
        widget.resize(480, 138)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
        widget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_frame = QtWidgets.QFrame(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_frame.sizePolicy().hasHeightForWidth())
        self.widget_frame.setSizePolicy(sizePolicy)
        self.widget_frame.setMinimumSize(QtCore.QSize(480, 137))
        self.widget_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_frame.setAutoFillBackground(False)
        self.widget_frame.setStyleSheet(".QFrame { border: 1px solid #005B78; border-radius: 4px; }\n"
"* { background-color: white; }\n"
"")
        self.widget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.widget_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.widget_frame.setObjectName("widget_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget_3 = QtWidgets.QWidget(self.widget_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, 1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.botname_label = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.botname_label.setFont(font)
        self.botname_label.setStyleSheet("color: #005B78;")
        self.botname_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.botname_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.botname_label.setObjectName("botname_label")
        self.horizontalLayout_4.addWidget(self.botname_label)
        self.strategy_label = QtWidgets.QLabel(self.widget_3)
        self.strategy_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.strategy_label.setFont(font)
        self.strategy_label.setAutoFillBackground(False)
        self.strategy_label.setStyleSheet("color: #005B78;")
        self.strategy_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.strategy_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.strategy_label.setObjectName("strategy_label")
        self.horizontalLayout_4.addWidget(self.strategy_label)
        self.edit_button = QtWidgets.QPushButton(self.widget_3)
        self.edit_button.setMaximumSize(QtCore.QSize(28, 16777215))
        self.edit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_button.setStyleSheet("border: 0;")
        self.edit_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/bot_widget/img/pen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_button.setIcon(icon)
        self.edit_button.setObjectName("edit_button")
        self.horizontalLayout_4.addWidget(self.edit_button)
        self.remove_button = QtWidgets.QPushButton(self.widget_3)
        self.remove_button.setMaximumSize(QtCore.QSize(28, 16777215))
        self.remove_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove_button.setStyleSheet("border: 0;")
        self.remove_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/bot_widget/img/bin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_button.setIcon(icon1)
        self.remove_button.setIconSize(QtCore.QSize(20, 20))
        self.remove_button.setObjectName("remove_button")
        self.horizontalLayout_4.addWidget(self.remove_button)
        self.gridLayout_6.addWidget(self.widget_3, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_6 = QtWidgets.QWidget(self.widget_frame)
        self.widget_6.setMinimumSize(QtCore.QSize(130, 0))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.currency_label = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.currency_label.setFont(font)
        self.currency_label.setStyleSheet("color: #005B78;")
        self.currency_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.currency_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.currency_label.setObjectName("currency_label")
        self.verticalLayout_5.addWidget(self.currency_label)
        self.profit_label = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.profit_label.setFont(font)
        self.profit_label.setStyleSheet("color: #00D05A;")
        self.profit_label.setLineWidth(1)
        self.profit_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.profit_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.profit_label.setObjectName("profit_label")
        self.verticalLayout_5.addWidget(self.profit_label)
        self.gridLayout_3.addWidget(self.widget_6, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.widget_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.widget_7 = QtWidgets.QWidget(self.widget_4)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buy_label = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buy_label.setFont(font)
        self.buy_label.setStyleSheet("color: #005B78;")
        self.buy_label.setObjectName("buy_label")
        self.horizontalLayout.addWidget(self.buy_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.sell_label = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sell_label.setFont(font)
        self.sell_label.setStyleSheet("color: #005B78;")
        self.sell_label.setObjectName("sell_label")
        self.horizontalLayout.addWidget(self.sell_label)
        self.verticalLayout_4.addWidget(self.widget_7)
        self.widget_2 = QtWidgets.QWidget(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.order_slider = QtWidgets.QSlider(self.widget_2)
        self.order_slider.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.order_slider.sizePolicy().hasHeightForWidth())
        self.order_slider.setSizePolicy(sizePolicy)
        self.order_slider.setStyleSheet("QSlider::groove:horizontal {\n"
"height: 2px;\n"
"background: #005B78;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"background: #005B78;\n"
"width: 15px;\n"
"margin: -5px 0;\n"
"}\n"
"QSlider {\n"
"border-left: 2px solid  #005B78;\n"
"border-right: 2px solid  #005B78;\n"
"}")
        self.order_slider.setMaximum(100)
        self.order_slider.setSliderPosition(50)
        self.order_slider.setTracking(False)
        self.order_slider.setOrientation(QtCore.Qt.Horizontal)
        self.order_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.order_slider.setObjectName("order_slider")
        self.horizontalLayout_3.addWidget(self.order_slider)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.gridLayout.addWidget(self.widget_4, 0, 1, 2, 1)
        self.widget_5 = QtWidgets.QWidget(self.widget_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pause_button = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pause_button.sizePolicy().hasHeightForWidth())
        self.pause_button.setSizePolicy(sizePolicy)
        self.pause_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pause_button.setStyleSheet("border: 0;\n"
"")
        self.pause_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/bot_widget/img/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_button.setIcon(icon2)
        self.pause_button.setIconSize(QtCore.QSize(30, 30))
        self.pause_button.setObjectName("pause_button")
        self.horizontalLayout_2.addWidget(self.pause_button)
        self.play_button = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy)
        self.play_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.play_button.setStatusTip("")
        self.play_button.setStyleSheet("border: 0;")
        self.play_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/bot_widget/img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_button.setIcon(icon3)
        self.play_button.setIconSize(QtCore.QSize(30, 30))
        self.play_button.setObjectName("play_button")
        self.horizontalLayout_2.addWidget(self.play_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addWidget(self.widget_5, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_frame, 0, 0, 1, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "widget"))
        self.botname_label.setText(_translate("widget", "Botname"))
        self.strategy_label.setText(_translate("widget", "SIMPLE STRATEGY"))
        self.currency_label.setText(_translate("widget", "BTS/USD"))
        self.profit_label.setText(_translate("widget", "+0.0%"))
        self.buy_label.setText(_translate("widget", "Buy"))
        self.sell_label.setText(_translate("widget", "Sell"))

from dexbot.resources import icons_rc
