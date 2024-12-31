# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHeaderView, QLCDNumber,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1484, 777)
        self.actionDashboard = QAction(MainWindow)
        self.actionDashboard.setObjectName(u"actionDashboard")
        self.actionInventory_Management = QAction(MainWindow)
        self.actionInventory_Management.setObjectName(u"actionInventory_Management")
        self.actionOrder_Management = QAction(MainWindow)
        self.actionOrder_Management.setObjectName(u"actionOrder_Management")
        self.actionSatistics = QAction(MainWindow)
        self.actionSatistics.setObjectName(u"actionSatistics")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionStations = QAction(MainWindow)
        self.actionStations.setObjectName(u"actionStations")
        self.actionInventoryDashboard = QAction(MainWindow)
        self.actionInventoryDashboard.setObjectName(u"actionInventoryDashboard")
        self.actionStatistics = QAction(MainWindow)
        self.actionStatistics.setObjectName(u"actionStatistics")
        self.actionOrdersDashboard = QAction(MainWindow)
        self.actionOrdersDashboard.setObjectName(u"actionOrdersDashboard")
        self.actionAdd_Order = QAction(MainWindow)
        self.actionAdd_Order.setObjectName(u"actionAdd_Order")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAutosave = QAction(MainWindow)
        self.actionAutosave.setObjectName(u"actionAutosave")
        self.actionAutosave.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1351, 761))
        self.stackedWidget.setMinimumSize(QSize(1351, 761))
        self.stackedWidget.setMaximumSize(QSize(1471, 761))
        self.StationsPage = QWidget()
        self.StationsPage.setObjectName(u"StationsPage")
        self.tabWidget = QTabWidget(self.StationsPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 1131, 671))
        self.tabWidget.setMinimumSize(QSize(1131, 446))
        self.tabWidget.setMaximumSize(QSize(1131, 671))
        self.ForkStation = QWidget()
        self.ForkStation.setObjectName(u"ForkStation")
        self.gridLayout_17 = QGridLayout(self.ForkStation)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.ForksOrderInformationBox = QGroupBox(self.ForkStation)
        self.ForksOrderInformationBox.setObjectName(u"ForksOrderInformationBox")
        self.ForksOrderInformationBox.setMinimumSize(QSize(281, 385))
        self.gridLayout_13 = QGridLayout(self.ForksOrderInformationBox)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.LightsLabel_2 = QLabel(self.ForksOrderInformationBox)
        self.LightsLabel_2.setObjectName(u"LightsLabel_2")

        self.gridLayout_13.addWidget(self.LightsLabel_2, 11, 0, 1, 1)

        self.line_3 = QFrame(self.ForksOrderInformationBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_13.addWidget(self.line_3, 2, 0, 1, 4)

        self.BikeType_2 = QLabel(self.ForksOrderInformationBox)
        self.BikeType_2.setObjectName(u"BikeType_2")

        self.gridLayout_13.addWidget(self.BikeType_2, 1, 2, 1, 2)

        self.horizontalSpacer_57 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_57, 10, 1, 1, 2)

        self.horizontalSpacer_53 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_53, 5, 1, 1, 2)

        self.horizontalSpacer_51 = QSpacerItem(103, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_51, 3, 2, 1, 2)

        self.PedalType_2 = QLabel(self.ForksOrderInformationBox)
        self.PedalType_2.setObjectName(u"PedalType_2")

        self.gridLayout_13.addWidget(self.PedalType_2, 5, 3, 1, 1)

        self.OrderNumberLabel_2 = QLabel(self.ForksOrderInformationBox)
        self.OrderNumberLabel_2.setObjectName(u"OrderNumberLabel_2")

        self.gridLayout_13.addWidget(self.OrderNumberLabel_2, 0, 0, 1, 1)

        self.OrderNumber_2 = QLabel(self.ForksOrderInformationBox)
        self.OrderNumber_2.setObjectName(u"OrderNumber_2")

        self.gridLayout_13.addWidget(self.OrderNumber_2, 0, 2, 1, 2)

        self.SeatLabel_2 = QLabel(self.ForksOrderInformationBox)
        self.SeatLabel_2.setObjectName(u"SeatLabel_2")

        self.gridLayout_13.addWidget(self.SeatLabel_2, 12, 0, 1, 1)

        self.horizontalSpacer_50 = QSpacerItem(96, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_50, 3, 0, 1, 1)

        self.horizontalSpacer_49 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_49, 1, 1, 1, 1)

        self.PartsLabel_2 = QLabel(self.ForksOrderInformationBox)
        self.PartsLabel_2.setObjectName(u"PartsLabel_2")
        self.PartsLabel_2.setScaledContents(False)
        self.PartsLabel_2.setWordWrap(False)

        self.gridLayout_13.addWidget(self.PartsLabel_2, 3, 1, 1, 1)

        self.PedalLabel_2 = QLabel(self.ForksOrderInformationBox)
        self.PedalLabel_2.setObjectName(u"PedalLabel_2")

        self.gridLayout_13.addWidget(self.PedalLabel_2, 5, 0, 1, 1)

        self.horizontalSpacer_52 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_52, 4, 1, 1, 2)

        self.Colour_2 = QLabel(self.ForksOrderInformationBox)
        self.Colour_2.setObjectName(u"Colour_2")

        self.gridLayout_13.addWidget(self.Colour_2, 4, 3, 1, 1)

        self.horizontalSpacer_48 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_48, 0, 1, 1, 1)

        self.LightsType_2 = QLabel(self.ForksOrderInformationBox)
        self.LightsType_2.setObjectName(u"LightsType_2")

        self.gridLayout_13.addWidget(self.LightsType_2, 11, 3, 1, 1)

        self.ChainLabel_2 = QLabel(self.ForksOrderInformationBox)
        self.ChainLabel_2.setObjectName(u"ChainLabel_2")

        self.gridLayout_13.addWidget(self.ChainLabel_2, 7, 0, 1, 1)

        self.ColourLabel_2 = QLabel(self.ForksOrderInformationBox)
        self.ColourLabel_2.setObjectName(u"ColourLabel_2")

        self.gridLayout_13.addWidget(self.ColourLabel_2, 4, 0, 1, 1)

        self.GearsLabel_2 = QLabel(self.ForksOrderInformationBox)
        self.GearsLabel_2.setObjectName(u"GearsLabel_2")

        self.gridLayout_13.addWidget(self.GearsLabel_2, 8, 0, 1, 1)

        self.BrakesType_2 = QLabel(self.ForksOrderInformationBox)
        self.BrakesType_2.setObjectName(u"BrakesType_2")

        self.gridLayout_13.addWidget(self.BrakesType_2, 10, 3, 1, 1)

        self.horizontalSpacer_58 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_58, 11, 1, 1, 2)

        self.horizontalSpacer_56 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_56, 8, 1, 1, 2)

        self.GearType_2 = QLabel(self.ForksOrderInformationBox)
        self.GearType_2.setObjectName(u"GearType_2")

        self.gridLayout_13.addWidget(self.GearType_2, 8, 3, 1, 1)

        self.BikeTypeLabel_2 = QLabel(self.ForksOrderInformationBox)
        self.BikeTypeLabel_2.setObjectName(u"BikeTypeLabel_2")

        self.gridLayout_13.addWidget(self.BikeTypeLabel_2, 1, 0, 1, 1)

        self.BrakesLabel_2 = QLabel(self.ForksOrderInformationBox)
        self.BrakesLabel_2.setObjectName(u"BrakesLabel_2")

        self.gridLayout_13.addWidget(self.BrakesLabel_2, 10, 0, 1, 1)

        self.ChainType_2 = QLabel(self.ForksOrderInformationBox)
        self.ChainType_2.setObjectName(u"ChainType_2")

        self.gridLayout_13.addWidget(self.ChainType_2, 7, 3, 1, 1)

        self.SeatType_2 = QLabel(self.ForksOrderInformationBox)
        self.SeatType_2.setObjectName(u"SeatType_2")

        self.gridLayout_13.addWidget(self.SeatType_2, 12, 3, 1, 1)

        self.WheelsLabel_2 = QLabel(self.ForksOrderInformationBox)
        self.WheelsLabel_2.setObjectName(u"WheelsLabel_2")

        self.gridLayout_13.addWidget(self.WheelsLabel_2, 9, 0, 1, 1)

        self.WheelType_2 = QLabel(self.ForksOrderInformationBox)
        self.WheelType_2.setObjectName(u"WheelType_2")

        self.gridLayout_13.addWidget(self.WheelType_2, 9, 3, 1, 1)

        self.horizontalSpacer_54 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_54, 9, 1, 1, 2)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_55, 7, 1, 1, 2)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_59, 12, 1, 1, 2)


        self.gridLayout_17.addWidget(self.ForksOrderInformationBox, 0, 0, 3, 1)

        self.ForkStationInventoryBox = QGroupBox(self.ForkStation)
        self.ForkStationInventoryBox.setObjectName(u"ForkStationInventoryBox")
        self.gridLayout_15 = QGridLayout(self.ForkStationInventoryBox)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.ForkStationTubularSteelInventoryLabel = QLabel(self.ForkStationInventoryBox)
        self.ForkStationTubularSteelInventoryLabel.setObjectName(u"ForkStationTubularSteelInventoryLabel")

        self.gridLayout_15.addWidget(self.ForkStationTubularSteelInventoryLabel, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)

        self.ForkStationTubularSteelInventoryCount = QLCDNumber(self.ForkStationInventoryBox)
        self.ForkStationTubularSteelInventoryCount.setObjectName(u"ForkStationTubularSteelInventoryCount")
        self.ForkStationTubularSteelInventoryCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_15.addWidget(self.ForkStationTubularSteelInventoryCount, 0, 2, 1, 1)

        self.horizontalSpacer_175 = QSpacerItem(38, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_175, 0, 3, 1, 1)

        self.ForkStationTubularSteelRequiredLabel = QLabel(self.ForkStationInventoryBox)
        self.ForkStationTubularSteelRequiredLabel.setObjectName(u"ForkStationTubularSteelRequiredLabel")

        self.gridLayout_15.addWidget(self.ForkStationTubularSteelRequiredLabel, 0, 4, 1, 1)

        self.ForkStationTubularSteelRequiredCount = QLCDNumber(self.ForkStationInventoryBox)
        self.ForkStationTubularSteelRequiredCount.setObjectName(u"ForkStationTubularSteelRequiredCount")
        self.ForkStationTubularSteelRequiredCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_15.addWidget(self.ForkStationTubularSteelRequiredCount, 0, 5, 1, 1)

        self.ForkStationForkInventory = QGroupBox(self.ForkStationInventoryBox)
        self.ForkStationForkInventory.setObjectName(u"ForkStationForkInventory")
        self.gridLayout_56 = QGridLayout(self.ForkStationForkInventory)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.ForkStationInventoryTotalForksLabel = QLabel(self.ForkStationForkInventory)
        self.ForkStationInventoryTotalForksLabel.setObjectName(u"ForkStationInventoryTotalForksLabel")

        self.gridLayout_56.addWidget(self.ForkStationInventoryTotalForksLabel, 0, 0, 1, 1)

        self.horizontalSpacer_103 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer_103, 0, 1, 1, 1)

        self.ForkStationInventoryTotalForksCount = QLCDNumber(self.ForkStationForkInventory)
        self.ForkStationInventoryTotalForksCount.setObjectName(u"ForkStationInventoryTotalForksCount")
        self.ForkStationInventoryTotalForksCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_56.addWidget(self.ForkStationInventoryTotalForksCount, 0, 2, 1, 1)

        self.ForkStationInventoryNormalForksLabel = QLabel(self.ForkStationForkInventory)
        self.ForkStationInventoryNormalForksLabel.setObjectName(u"ForkStationInventoryNormalForksLabel")

        self.gridLayout_56.addWidget(self.ForkStationInventoryNormalForksLabel, 1, 0, 1, 1)

        self.horizontalSpacer_131 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer_131, 1, 1, 1, 1)

        self.ForkStationInventoryNormalForksCount = QLCDNumber(self.ForkStationForkInventory)
        self.ForkStationInventoryNormalForksCount.setObjectName(u"ForkStationInventoryNormalForksCount")
        self.ForkStationInventoryNormalForksCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_56.addWidget(self.ForkStationInventoryNormalForksCount, 1, 2, 1, 1)

        self.ForkStationInventorySportsForksLabel = QLabel(self.ForkStationForkInventory)
        self.ForkStationInventorySportsForksLabel.setObjectName(u"ForkStationInventorySportsForksLabel")

        self.gridLayout_56.addWidget(self.ForkStationInventorySportsForksLabel, 2, 0, 1, 1)

        self.horizontalSpacer_144 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer_144, 2, 1, 1, 1)

        self.ForkStationInventorySportsForksCount = QLCDNumber(self.ForkStationForkInventory)
        self.ForkStationInventorySportsForksCount.setObjectName(u"ForkStationInventorySportsForksCount")
        self.ForkStationInventorySportsForksCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_56.addWidget(self.ForkStationInventorySportsForksCount, 2, 2, 1, 1)

        self.ForkStationInventoryKidsForksLabel = QLabel(self.ForkStationForkInventory)
        self.ForkStationInventoryKidsForksLabel.setObjectName(u"ForkStationInventoryKidsForksLabel")

        self.gridLayout_56.addWidget(self.ForkStationInventoryKidsForksLabel, 3, 0, 1, 1)

        self.horizontalSpacer_145 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer_145, 3, 1, 1, 1)

        self.ForkStationInventoryKidsForksCount = QLCDNumber(self.ForkStationForkInventory)
        self.ForkStationInventoryKidsForksCount.setObjectName(u"ForkStationInventoryKidsForksCount")
        self.ForkStationInventoryKidsForksCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_56.addWidget(self.ForkStationInventoryKidsForksCount, 3, 2, 1, 1)


        self.gridLayout_15.addWidget(self.ForkStationForkInventory, 1, 0, 1, 6)


        self.gridLayout_17.addWidget(self.ForkStationInventoryBox, 0, 1, 2, 1)

        self.ForkStationBox = QGroupBox(self.ForkStation)
        self.ForkStationBox.setObjectName(u"ForkStationBox")
        self.gridLayout_3 = QGridLayout(self.ForkStationBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ForkStationForkLabel = QLabel(self.ForkStationBox)
        self.ForkStationForkLabel.setObjectName(u"ForkStationForkLabel")

        self.gridLayout_3.addWidget(self.ForkStationForkLabel, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.ForkWeldedButton = QPushButton(self.ForkStationBox)
        self.ForkWeldedButton.setObjectName(u"ForkWeldedButton")
        self.ForkWeldedButton.setEnabled(True)

        self.gridLayout_3.addWidget(self.ForkWeldedButton, 1, 0, 1, 3)

        self.ForkStationForkValue = QLabel(self.ForkStationBox)
        self.ForkStationForkValue.setObjectName(u"ForkStationForkValue")

        self.gridLayout_3.addWidget(self.ForkStationForkValue, 0, 2, 1, 1)


        self.gridLayout_17.addWidget(self.ForkStationBox, 0, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 429, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_8, 1, 2, 2, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 429, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_7, 2, 1, 1, 1)

        self.tabWidget.addTab(self.ForkStation, "")
        self.FrameStation = QWidget()
        self.FrameStation.setObjectName(u"FrameStation")
        self.gridLayout_16 = QGridLayout(self.FrameStation)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.GroupBoxOrder = QGroupBox(self.FrameStation)
        self.GroupBoxOrder.setObjectName(u"GroupBoxOrder")
        self.GroupBoxOrder.setMinimumSize(QSize(281, 385))
        self.GroupBoxOrder.setFlat(False)
        self.GroupBoxOrder.setCheckable(False)
        self.gridLayout = QGridLayout(self.GroupBoxOrder)
        self.gridLayout.setObjectName(u"gridLayout")
        self.LightsType = QLabel(self.GroupBoxOrder)
        self.LightsType.setObjectName(u"LightsType")

        self.gridLayout.addWidget(self.LightsType, 11, 2, 1, 1)

        self.Colour = QLabel(self.GroupBoxOrder)
        self.Colour.setObjectName(u"Colour")

        self.gridLayout.addWidget(self.Colour, 4, 2, 1, 1)

        self.GearType = QLabel(self.GroupBoxOrder)
        self.GearType.setObjectName(u"GearType")

        self.gridLayout.addWidget(self.GearType, 8, 2, 1, 1)

        self.BrakesType = QLabel(self.GroupBoxOrder)
        self.BrakesType.setObjectName(u"BrakesType")

        self.gridLayout.addWidget(self.BrakesType, 10, 2, 1, 1)

        self.SeatLabel = QLabel(self.GroupBoxOrder)
        self.SeatLabel.setObjectName(u"SeatLabel")

        self.gridLayout.addWidget(self.SeatLabel, 12, 0, 1, 1)

        self.ChainLabel = QLabel(self.GroupBoxOrder)
        self.ChainLabel.setObjectName(u"ChainLabel")

        self.gridLayout.addWidget(self.ChainLabel, 7, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_13, 4, 1, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(96, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_22, 3, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_16, 7, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 1, 1, 1, 1)

        self.PedalLabel = QLabel(self.GroupBoxOrder)
        self.PedalLabel.setObjectName(u"PedalLabel")

        self.gridLayout.addWidget(self.PedalLabel, 5, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_14, 5, 1, 1, 1)

        self.BrakesLabel = QLabel(self.GroupBoxOrder)
        self.BrakesLabel.setObjectName(u"BrakesLabel")

        self.gridLayout.addWidget(self.BrakesLabel, 10, 0, 1, 1)

        self.BikeTypeLabel = QLabel(self.GroupBoxOrder)
        self.BikeTypeLabel.setObjectName(u"BikeTypeLabel")

        self.gridLayout.addWidget(self.BikeTypeLabel, 1, 0, 1, 1)

        self.ColourLabel = QLabel(self.GroupBoxOrder)
        self.ColourLabel.setObjectName(u"ColourLabel")

        self.gridLayout.addWidget(self.ColourLabel, 4, 0, 1, 1)

        self.BikeType = QLabel(self.GroupBoxOrder)
        self.BikeType.setObjectName(u"BikeType")

        self.gridLayout.addWidget(self.BikeType, 1, 2, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_19, 11, 1, 1, 1)

        self.SeatType = QLabel(self.GroupBoxOrder)
        self.SeatType.setObjectName(u"SeatType")

        self.gridLayout.addWidget(self.SeatType, 12, 2, 1, 1)

        self.line = QFrame(self.GroupBoxOrder)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 3)

        self.ChainType = QLabel(self.GroupBoxOrder)
        self.ChainType.setObjectName(u"ChainType")

        self.gridLayout.addWidget(self.ChainType, 7, 2, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_18, 10, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)

        self.OrderNumberLabel = QLabel(self.GroupBoxOrder)
        self.OrderNumberLabel.setObjectName(u"OrderNumberLabel")

        self.gridLayout.addWidget(self.OrderNumberLabel, 0, 0, 1, 1)

        self.GearsLabel = QLabel(self.GroupBoxOrder)
        self.GearsLabel.setObjectName(u"GearsLabel")

        self.gridLayout.addWidget(self.GearsLabel, 8, 0, 1, 1)

        self.LightsLabel = QLabel(self.GroupBoxOrder)
        self.LightsLabel.setObjectName(u"LightsLabel")

        self.gridLayout.addWidget(self.LightsLabel, 11, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_20, 12, 1, 1, 1)

        self.PedalType = QLabel(self.GroupBoxOrder)
        self.PedalType.setObjectName(u"PedalType")

        self.gridLayout.addWidget(self.PedalType, 5, 2, 1, 1)

        self.OrderNumber = QLabel(self.GroupBoxOrder)
        self.OrderNumber.setObjectName(u"OrderNumber")

        self.gridLayout.addWidget(self.OrderNumber, 0, 2, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(103, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_21, 3, 2, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_17, 8, 1, 1, 1)

        self.PartsLabel = QLabel(self.GroupBoxOrder)
        self.PartsLabel.setObjectName(u"PartsLabel")
        self.PartsLabel.setScaledContents(False)
        self.PartsLabel.setWordWrap(False)

        self.gridLayout.addWidget(self.PartsLabel, 3, 1, 1, 1)

        self.WheelsLabel = QLabel(self.GroupBoxOrder)
        self.WheelsLabel.setObjectName(u"WheelsLabel")

        self.gridLayout.addWidget(self.WheelsLabel, 9, 0, 1, 1)

        self.WheelType = QLabel(self.GroupBoxOrder)
        self.WheelType.setObjectName(u"WheelType")

        self.gridLayout.addWidget(self.WheelType, 9, 2, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_15, 9, 1, 1, 1)


        self.gridLayout_16.addWidget(self.GroupBoxOrder, 0, 0, 3, 1)

        self.FrameStationInventoryBox = QGroupBox(self.FrameStation)
        self.FrameStationInventoryBox.setObjectName(u"FrameStationInventoryBox")
        self.gridLayout_14 = QGridLayout(self.FrameStationInventoryBox)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.FrameStationInventoryTubularSteelLabel = QLabel(self.FrameStationInventoryBox)
        self.FrameStationInventoryTubularSteelLabel.setObjectName(u"FrameStationInventoryTubularSteelLabel")

        self.gridLayout_14.addWidget(self.FrameStationInventoryTubularSteelLabel, 0, 0, 1, 1)

        self.FrameStationInventoryTubularSteelCount = QLCDNumber(self.FrameStationInventoryBox)
        self.FrameStationInventoryTubularSteelCount.setObjectName(u"FrameStationInventoryTubularSteelCount")
        self.FrameStationInventoryTubularSteelCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_14.addWidget(self.FrameStationInventoryTubularSteelCount, 0, 1, 1, 1)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_45, 0, 2, 1, 1)

        self.FrameStationInventoryRequiredTubularSteelLabel = QLabel(self.FrameStationInventoryBox)
        self.FrameStationInventoryRequiredTubularSteelLabel.setObjectName(u"FrameStationInventoryRequiredTubularSteelLabel")

        self.gridLayout_14.addWidget(self.FrameStationInventoryRequiredTubularSteelLabel, 0, 3, 1, 1)

        self.FrameStationInventoryRequiredTubularSteelCount = QLCDNumber(self.FrameStationInventoryBox)
        self.FrameStationInventoryRequiredTubularSteelCount.setObjectName(u"FrameStationInventoryRequiredTubularSteelCount")
        self.FrameStationInventoryRequiredTubularSteelCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_14.addWidget(self.FrameStationInventoryRequiredTubularSteelCount, 0, 4, 1, 1)

        self.FrameStationFrameInventoryBox = QGroupBox(self.FrameStationInventoryBox)
        self.FrameStationFrameInventoryBox.setObjectName(u"FrameStationFrameInventoryBox")
        self.gridLayout_55 = QGridLayout(self.FrameStationFrameInventoryBox)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.FrameStationTotalFrameLabel = QLabel(self.FrameStationFrameInventoryBox)
        self.FrameStationTotalFrameLabel.setObjectName(u"FrameStationTotalFrameLabel")

        self.gridLayout_55.addWidget(self.FrameStationTotalFrameLabel, 0, 0, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_55.addItem(self.horizontalSpacer_23, 0, 1, 1, 1)

        self.FrameStationTotalFrameCount = QLCDNumber(self.FrameStationFrameInventoryBox)
        self.FrameStationTotalFrameCount.setObjectName(u"FrameStationTotalFrameCount")
        self.FrameStationTotalFrameCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_55.addWidget(self.FrameStationTotalFrameCount, 0, 2, 1, 1)

        self.FrameStationNormalFrameLabel = QLabel(self.FrameStationFrameInventoryBox)
        self.FrameStationNormalFrameLabel.setObjectName(u"FrameStationNormalFrameLabel")

        self.gridLayout_55.addWidget(self.FrameStationNormalFrameLabel, 1, 0, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_55.addItem(self.horizontalSpacer_24, 1, 1, 1, 1)

        self.FrameStationNormalFrameCount = QLCDNumber(self.FrameStationFrameInventoryBox)
        self.FrameStationNormalFrameCount.setObjectName(u"FrameStationNormalFrameCount")
        self.FrameStationNormalFrameCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_55.addWidget(self.FrameStationNormalFrameCount, 1, 2, 1, 1)

        self.FrameStationSportsFrameLabel = QLabel(self.FrameStationFrameInventoryBox)
        self.FrameStationSportsFrameLabel.setObjectName(u"FrameStationSportsFrameLabel")

        self.gridLayout_55.addWidget(self.FrameStationSportsFrameLabel, 2, 0, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_55.addItem(self.horizontalSpacer_25, 2, 1, 1, 1)

        self.FrameStationSportsFrameCount = QLCDNumber(self.FrameStationFrameInventoryBox)
        self.FrameStationSportsFrameCount.setObjectName(u"FrameStationSportsFrameCount")
        self.FrameStationSportsFrameCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_55.addWidget(self.FrameStationSportsFrameCount, 2, 2, 1, 1)

        self.FrameStationKidsFrameLabel = QLabel(self.FrameStationFrameInventoryBox)
        self.FrameStationKidsFrameLabel.setObjectName(u"FrameStationKidsFrameLabel")

        self.gridLayout_55.addWidget(self.FrameStationKidsFrameLabel, 3, 0, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_55.addItem(self.horizontalSpacer_26, 3, 1, 1, 1)

        self.FrameStationKidsFrameCount = QLCDNumber(self.FrameStationFrameInventoryBox)
        self.FrameStationKidsFrameCount.setObjectName(u"FrameStationKidsFrameCount")
        self.FrameStationKidsFrameCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_55.addWidget(self.FrameStationKidsFrameCount, 3, 2, 1, 1)


        self.gridLayout_14.addWidget(self.FrameStationFrameInventoryBox, 1, 0, 1, 5)


        self.gridLayout_16.addWidget(self.FrameStationInventoryBox, 0, 1, 2, 1)

        self.FrameWeldingStation = QGroupBox(self.FrameStation)
        self.FrameWeldingStation.setObjectName(u"FrameWeldingStation")
        self.gridLayout_2 = QGridLayout(self.FrameWeldingStation)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.FrameWeldingStationLabel = QLabel(self.FrameWeldingStation)
        self.FrameWeldingStationLabel.setObjectName(u"FrameWeldingStationLabel")

        self.gridLayout_2.addWidget(self.FrameWeldingStationLabel, 0, 0, 1, 1)

        self.horizontalSpacer_102 = QSpacerItem(118, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_102, 0, 1, 1, 1)

        self.FrameWeldingStationType = QLabel(self.FrameWeldingStation)
        self.FrameWeldingStationType.setObjectName(u"FrameWeldingStationType")

        self.gridLayout_2.addWidget(self.FrameWeldingStationType, 0, 2, 1, 1)

        self.FrameWeldingStationButton = QPushButton(self.FrameWeldingStation)
        self.FrameWeldingStationButton.setObjectName(u"FrameWeldingStationButton")

        self.gridLayout_2.addWidget(self.FrameWeldingStationButton, 1, 0, 1, 3)


        self.gridLayout_16.addWidget(self.FrameWeldingStation, 0, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 429, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_6, 1, 2, 2, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 429, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_5, 2, 1, 1, 1)

        self.tabWidget.addTab(self.FrameStation, "")
        self.ChassisAssembly = QWidget()
        self.ChassisAssembly.setObjectName(u"ChassisAssembly")
        self.gridLayout_59 = QGridLayout(self.ChassisAssembly)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.ChassisOrder = QGroupBox(self.ChassisAssembly)
        self.ChassisOrder.setObjectName(u"ChassisOrder")
        self.ChassisOrder.setMinimumSize(QSize(281, 385))
        self.gridLayout_25 = QGridLayout(self.ChassisOrder)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.BrakesLabel_3 = QLabel(self.ChassisOrder)
        self.BrakesLabel_3.setObjectName(u"BrakesLabel_3")

        self.gridLayout_25.addWidget(self.BrakesLabel_3, 10, 0, 1, 1)

        self.OrderNumber_3 = QLabel(self.ChassisOrder)
        self.OrderNumber_3.setObjectName(u"OrderNumber_3")

        self.gridLayout_25.addWidget(self.OrderNumber_3, 0, 2, 1, 2)

        self.SeatLabel_3 = QLabel(self.ChassisOrder)
        self.SeatLabel_3.setObjectName(u"SeatLabel_3")

        self.gridLayout_25.addWidget(self.SeatLabel_3, 12, 0, 1, 1)

        self.horizontalSpacer_64 = QSpacerItem(96, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_64, 3, 0, 1, 1)

        self.LightsType_3 = QLabel(self.ChassisOrder)
        self.LightsType_3.setObjectName(u"LightsType_3")

        self.gridLayout_25.addWidget(self.LightsType_3, 11, 3, 1, 1)

        self.ChainLabel_3 = QLabel(self.ChassisOrder)
        self.ChainLabel_3.setObjectName(u"ChainLabel_3")

        self.gridLayout_25.addWidget(self.ChainLabel_3, 7, 0, 1, 1)

        self.horizontalSpacer_62 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_62, 0, 1, 1, 1)

        self.BrakesType_3 = QLabel(self.ChassisOrder)
        self.BrakesType_3.setObjectName(u"BrakesType_3")

        self.gridLayout_25.addWidget(self.BrakesType_3, 10, 3, 1, 1)

        self.GearsLabel_3 = QLabel(self.ChassisOrder)
        self.GearsLabel_3.setObjectName(u"GearsLabel_3")

        self.gridLayout_25.addWidget(self.GearsLabel_3, 8, 0, 1, 1)

        self.BikeTypeLabel_3 = QLabel(self.ChassisOrder)
        self.BikeTypeLabel_3.setObjectName(u"BikeTypeLabel_3")

        self.gridLayout_25.addWidget(self.BikeTypeLabel_3, 1, 0, 1, 1)

        self.LightsLabel_3 = QLabel(self.ChassisOrder)
        self.LightsLabel_3.setObjectName(u"LightsLabel_3")

        self.gridLayout_25.addWidget(self.LightsLabel_3, 11, 0, 1, 1)

        self.horizontalSpacer_67 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_67, 5, 1, 1, 2)

        self.horizontalSpacer_70 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_70, 8, 1, 1, 2)

        self.horizontalSpacer_71 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_71, 10, 1, 1, 2)

        self.BikeType_3 = QLabel(self.ChassisOrder)
        self.BikeType_3.setObjectName(u"BikeType_3")

        self.gridLayout_25.addWidget(self.BikeType_3, 1, 2, 1, 2)

        self.OrderNumberLabel_3 = QLabel(self.ChassisOrder)
        self.OrderNumberLabel_3.setObjectName(u"OrderNumberLabel_3")

        self.gridLayout_25.addWidget(self.OrderNumberLabel_3, 0, 0, 1, 1)

        self.PedalType_3 = QLabel(self.ChassisOrder)
        self.PedalType_3.setObjectName(u"PedalType_3")

        self.gridLayout_25.addWidget(self.PedalType_3, 5, 3, 1, 1)

        self.ColourLabel_3 = QLabel(self.ChassisOrder)
        self.ColourLabel_3.setObjectName(u"ColourLabel_3")

        self.gridLayout_25.addWidget(self.ColourLabel_3, 4, 0, 1, 1)

        self.Colour_3 = QLabel(self.ChassisOrder)
        self.Colour_3.setObjectName(u"Colour_3")

        self.gridLayout_25.addWidget(self.Colour_3, 4, 3, 1, 1)

        self.ChainType_3 = QLabel(self.ChassisOrder)
        self.ChainType_3.setObjectName(u"ChainType_3")

        self.gridLayout_25.addWidget(self.ChainType_3, 7, 3, 1, 1)

        self.horizontalSpacer_66 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_66, 4, 1, 1, 2)

        self.PedalLabel_3 = QLabel(self.ChassisOrder)
        self.PedalLabel_3.setObjectName(u"PedalLabel_3")

        self.gridLayout_25.addWidget(self.PedalLabel_3, 5, 0, 1, 1)

        self.horizontalSpacer_63 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_63, 1, 1, 1, 1)

        self.GearType_3 = QLabel(self.ChassisOrder)
        self.GearType_3.setObjectName(u"GearType_3")

        self.gridLayout_25.addWidget(self.GearType_3, 8, 3, 1, 1)

        self.SeatType_3 = QLabel(self.ChassisOrder)
        self.SeatType_3.setObjectName(u"SeatType_3")

        self.gridLayout_25.addWidget(self.SeatType_3, 12, 3, 1, 1)

        self.horizontalSpacer_72 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_72, 11, 1, 1, 2)

        self.PartsLabel_3 = QLabel(self.ChassisOrder)
        self.PartsLabel_3.setObjectName(u"PartsLabel_3")
        self.PartsLabel_3.setScaledContents(False)
        self.PartsLabel_3.setWordWrap(False)

        self.gridLayout_25.addWidget(self.PartsLabel_3, 3, 1, 1, 1)

        self.line_4 = QFrame(self.ChassisOrder)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_25.addWidget(self.line_4, 2, 0, 1, 4)

        self.horizontalSpacer_65 = QSpacerItem(103, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_65, 3, 2, 1, 2)

        self.WheelsLabel_3 = QLabel(self.ChassisOrder)
        self.WheelsLabel_3.setObjectName(u"WheelsLabel_3")

        self.gridLayout_25.addWidget(self.WheelsLabel_3, 9, 0, 1, 1)

        self.WheelType_3 = QLabel(self.ChassisOrder)
        self.WheelType_3.setObjectName(u"WheelType_3")

        self.gridLayout_25.addWidget(self.WheelType_3, 9, 3, 1, 1)

        self.horizontalSpacer_68 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_68, 9, 1, 1, 2)

        self.horizontalSpacer_69 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_69, 7, 1, 1, 2)

        self.horizontalSpacer_73 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_73, 12, 1, 1, 2)


        self.gridLayout_59.addWidget(self.ChassisOrder, 0, 0, 2, 1)

        self.ChassisStationInventoryBox = QGroupBox(self.ChassisAssembly)
        self.ChassisStationInventoryBox.setObjectName(u"ChassisStationInventoryBox")
        self.gridLayout_58 = QGridLayout(self.ChassisStationInventoryBox)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.ChassisInventoryFramesBox = QGroupBox(self.ChassisStationInventoryBox)
        self.ChassisInventoryFramesBox.setObjectName(u"ChassisInventoryFramesBox")
        self.gridLayout_34 = QGridLayout(self.ChassisInventoryFramesBox)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.ChassisInventoryTotalFramesLabel = QLabel(self.ChassisInventoryFramesBox)
        self.ChassisInventoryTotalFramesLabel.setObjectName(u"ChassisInventoryTotalFramesLabel")

        self.gridLayout_34.addWidget(self.ChassisInventoryTotalFramesLabel, 0, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_34.addItem(self.horizontalSpacer_12, 0, 1, 1, 1)

        self.ChassisInventoryTotalFramesCount = QLCDNumber(self.ChassisInventoryFramesBox)
        self.ChassisInventoryTotalFramesCount.setObjectName(u"ChassisInventoryTotalFramesCount")
        self.ChassisInventoryTotalFramesCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_34.addWidget(self.ChassisInventoryTotalFramesCount, 0, 2, 1, 1)

        self.ChassisInventoryNormalFramesLabel = QLabel(self.ChassisInventoryFramesBox)
        self.ChassisInventoryNormalFramesLabel.setObjectName(u"ChassisInventoryNormalFramesLabel")

        self.gridLayout_34.addWidget(self.ChassisInventoryNormalFramesLabel, 1, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_34.addItem(self.horizontalSpacer_9, 1, 1, 1, 1)

        self.ChassisInventoryNormalFramesCount = QLCDNumber(self.ChassisInventoryFramesBox)
        self.ChassisInventoryNormalFramesCount.setObjectName(u"ChassisInventoryNormalFramesCount")
        self.ChassisInventoryNormalFramesCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_34.addWidget(self.ChassisInventoryNormalFramesCount, 1, 2, 1, 1)

        self.ChassisInventorySportsFramesLabel = QLabel(self.ChassisInventoryFramesBox)
        self.ChassisInventorySportsFramesLabel.setObjectName(u"ChassisInventorySportsFramesLabel")

        self.gridLayout_34.addWidget(self.ChassisInventorySportsFramesLabel, 2, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_34.addItem(self.horizontalSpacer_10, 2, 1, 1, 1)

        self.ChassisInventorySportsFramesCount = QLCDNumber(self.ChassisInventoryFramesBox)
        self.ChassisInventorySportsFramesCount.setObjectName(u"ChassisInventorySportsFramesCount")
        self.ChassisInventorySportsFramesCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_34.addWidget(self.ChassisInventorySportsFramesCount, 2, 2, 1, 1)

        self.ChassisInventoryKidsFramesLabel = QLabel(self.ChassisInventoryFramesBox)
        self.ChassisInventoryKidsFramesLabel.setObjectName(u"ChassisInventoryKidsFramesLabel")

        self.gridLayout_34.addWidget(self.ChassisInventoryKidsFramesLabel, 3, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_34.addItem(self.horizontalSpacer_11, 3, 1, 1, 1)

        self.ChassisInventoryKidsFramesCount = QLCDNumber(self.ChassisInventoryFramesBox)
        self.ChassisInventoryKidsFramesCount.setObjectName(u"ChassisInventoryKidsFramesCount")
        self.ChassisInventoryKidsFramesCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_34.addWidget(self.ChassisInventoryKidsFramesCount, 3, 2, 1, 1)


        self.gridLayout_58.addWidget(self.ChassisInventoryFramesBox, 0, 0, 1, 1)

        self.ChassisInventoryForksBox = QGroupBox(self.ChassisStationInventoryBox)
        self.ChassisInventoryForksBox.setObjectName(u"ChassisInventoryForksBox")
        self.gridLayout_35 = QGridLayout(self.ChassisInventoryForksBox)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.ChassisInventoryTotalForksLabel = QLabel(self.ChassisInventoryForksBox)
        self.ChassisInventoryTotalForksLabel.setObjectName(u"ChassisInventoryTotalForksLabel")

        self.gridLayout_35.addWidget(self.ChassisInventoryTotalForksLabel, 0, 0, 1, 1)

        self.horizontalSpacer_61 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_61, 0, 1, 1, 1)

        self.ChassisInventoryTotalForksCount = QLCDNumber(self.ChassisInventoryForksBox)
        self.ChassisInventoryTotalForksCount.setObjectName(u"ChassisInventoryTotalForksCount")
        self.ChassisInventoryTotalForksCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_35.addWidget(self.ChassisInventoryTotalForksCount, 0, 2, 1, 1)

        self.ChassisInventoryNormalForksLabel = QLabel(self.ChassisInventoryForksBox)
        self.ChassisInventoryNormalForksLabel.setObjectName(u"ChassisInventoryNormalForksLabel")

        self.gridLayout_35.addWidget(self.ChassisInventoryNormalForksLabel, 1, 0, 1, 1)

        self.horizontalSpacer_60 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_60, 1, 1, 1, 1)

        self.ChassisInventoryNormalForksCount = QLCDNumber(self.ChassisInventoryForksBox)
        self.ChassisInventoryNormalForksCount.setObjectName(u"ChassisInventoryNormalForksCount")
        self.ChassisInventoryNormalForksCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_35.addWidget(self.ChassisInventoryNormalForksCount, 1, 2, 1, 1)

        self.ChassisInventorySportsForksLabel = QLabel(self.ChassisInventoryForksBox)
        self.ChassisInventorySportsForksLabel.setObjectName(u"ChassisInventorySportsForksLabel")

        self.gridLayout_35.addWidget(self.ChassisInventorySportsForksLabel, 2, 0, 1, 1)

        self.horizontalSpacer_47 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_47, 2, 1, 1, 1)

        self.ChassisInventorySportsForksCount = QLCDNumber(self.ChassisInventoryForksBox)
        self.ChassisInventorySportsForksCount.setObjectName(u"ChassisInventorySportsForksCount")
        self.ChassisInventorySportsForksCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_35.addWidget(self.ChassisInventorySportsForksCount, 2, 2, 1, 1)

        self.ChassisInventoryKidsForksLabel = QLabel(self.ChassisInventoryForksBox)
        self.ChassisInventoryKidsForksLabel.setObjectName(u"ChassisInventoryKidsForksLabel")

        self.gridLayout_35.addWidget(self.ChassisInventoryKidsForksLabel, 3, 0, 1, 1)

        self.horizontalSpacer_46 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_46, 3, 1, 1, 1)

        self.ChassisInventoryKidsForksCount = QLCDNumber(self.ChassisInventoryForksBox)
        self.ChassisInventoryKidsForksCount.setObjectName(u"ChassisInventoryKidsForksCount")
        self.ChassisInventoryKidsForksCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_35.addWidget(self.ChassisInventoryKidsForksCount, 3, 2, 1, 1)


        self.gridLayout_58.addWidget(self.ChassisInventoryForksBox, 0, 1, 1, 1)

        self.ChassisInventoryChassisBox = QGroupBox(self.ChassisStationInventoryBox)
        self.ChassisInventoryChassisBox.setObjectName(u"ChassisInventoryChassisBox")
        self.gridLayout_36 = QGridLayout(self.ChassisInventoryChassisBox)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.ChassisInventoryTotalChassisLabel = QLabel(self.ChassisInventoryChassisBox)
        self.ChassisInventoryTotalChassisLabel.setObjectName(u"ChassisInventoryTotalChassisLabel")

        self.gridLayout_36.addWidget(self.ChassisInventoryTotalChassisLabel, 0, 0, 1, 1)

        self.horizontalSpacer_176 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_36.addItem(self.horizontalSpacer_176, 0, 1, 1, 1)

        self.ChassisInventoryTotalChassisCount = QLCDNumber(self.ChassisInventoryChassisBox)
        self.ChassisInventoryTotalChassisCount.setObjectName(u"ChassisInventoryTotalChassisCount")
        self.ChassisInventoryTotalChassisCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_36.addWidget(self.ChassisInventoryTotalChassisCount, 0, 2, 1, 1)

        self.ChassisInventoryNormalChassisLabel = QLabel(self.ChassisInventoryChassisBox)
        self.ChassisInventoryNormalChassisLabel.setObjectName(u"ChassisInventoryNormalChassisLabel")

        self.gridLayout_36.addWidget(self.ChassisInventoryNormalChassisLabel, 1, 0, 1, 1)

        self.horizontalSpacer_177 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_36.addItem(self.horizontalSpacer_177, 1, 1, 1, 1)

        self.ChassisInventoryNormalChassisCount = QLCDNumber(self.ChassisInventoryChassisBox)
        self.ChassisInventoryNormalChassisCount.setObjectName(u"ChassisInventoryNormalChassisCount")
        self.ChassisInventoryNormalChassisCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_36.addWidget(self.ChassisInventoryNormalChassisCount, 1, 2, 1, 1)

        self.ChassisInventorySportsChassisLabel = QLabel(self.ChassisInventoryChassisBox)
        self.ChassisInventorySportsChassisLabel.setObjectName(u"ChassisInventorySportsChassisLabel")

        self.gridLayout_36.addWidget(self.ChassisInventorySportsChassisLabel, 2, 0, 1, 1)

        self.horizontalSpacer_178 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_36.addItem(self.horizontalSpacer_178, 2, 1, 1, 1)

        self.ChassisInventorySportsChassisCount = QLCDNumber(self.ChassisInventoryChassisBox)
        self.ChassisInventorySportsChassisCount.setObjectName(u"ChassisInventorySportsChassisCount")
        self.ChassisInventorySportsChassisCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_36.addWidget(self.ChassisInventorySportsChassisCount, 2, 2, 1, 1)

        self.ChassisInventoryKidsChassisLabel = QLabel(self.ChassisInventoryChassisBox)
        self.ChassisInventoryKidsChassisLabel.setObjectName(u"ChassisInventoryKidsChassisLabel")

        self.gridLayout_36.addWidget(self.ChassisInventoryKidsChassisLabel, 3, 0, 1, 1)

        self.horizontalSpacer_179 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_36.addItem(self.horizontalSpacer_179, 3, 1, 1, 1)

        self.ChassisInventoryKidsChassisCount = QLCDNumber(self.ChassisInventoryChassisBox)
        self.ChassisInventoryKidsChassisCount.setObjectName(u"ChassisInventoryKidsChassisCount")
        self.ChassisInventoryKidsChassisCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_36.addWidget(self.ChassisInventoryKidsChassisCount, 3, 2, 1, 1)


        self.gridLayout_58.addWidget(self.ChassisInventoryChassisBox, 1, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 321, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_58.addItem(self.verticalSpacer_10, 1, 1, 1, 1)


        self.gridLayout_59.addWidget(self.ChassisStationInventoryBox, 0, 1, 2, 1)

        self.ChassisAssemblyBox = QGroupBox(self.ChassisAssembly)
        self.ChassisAssemblyBox.setObjectName(u"ChassisAssemblyBox")
        self.gridLayout_4 = QGridLayout(self.ChassisAssemblyBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.ChassisAssemblyTypeLabel = QLabel(self.ChassisAssemblyBox)
        self.ChassisAssemblyTypeLabel.setObjectName(u"ChassisAssemblyTypeLabel")

        self.gridLayout_4.addWidget(self.ChassisAssemblyTypeLabel, 0, 0, 1, 1)

        self.horizontalSpacer_180 = QSpacerItem(47, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_180, 0, 1, 1, 1)

        self.ChassisAssemblyType = QLabel(self.ChassisAssemblyBox)
        self.ChassisAssemblyType.setObjectName(u"ChassisAssemblyType")

        self.gridLayout_4.addWidget(self.ChassisAssemblyType, 0, 2, 1, 1)

        self.ChassisAssemblyButton = QPushButton(self.ChassisAssemblyBox)
        self.ChassisAssemblyButton.setObjectName(u"ChassisAssemblyButton")

        self.gridLayout_4.addWidget(self.ChassisAssemblyButton, 1, 0, 1, 3)


        self.gridLayout_59.addWidget(self.ChassisAssemblyBox, 0, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 426, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_59.addItem(self.verticalSpacer_9, 1, 2, 1, 1)

        self.tabWidget.addTab(self.ChassisAssembly, "")
        self.Painting = QWidget()
        self.Painting.setObjectName(u"Painting")
        self.gridLayout_62 = QGridLayout(self.Painting)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.PaintingStationInventoryBox = QGroupBox(self.Painting)
        self.PaintingStationInventoryBox.setObjectName(u"PaintingStationInventoryBox")
        self.gridLayout_61 = QGridLayout(self.PaintingStationInventoryBox)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.verticalSpacer_11 = QSpacerItem(20, 321, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_61.addItem(self.verticalSpacer_11, 1, 3, 1, 1)

        self.PaintingChassisInventoryBox = QGroupBox(self.PaintingStationInventoryBox)
        self.PaintingChassisInventoryBox.setObjectName(u"PaintingChassisInventoryBox")
        self.gridLayout_40 = QGridLayout(self.PaintingChassisInventoryBox)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.PaintStationInventoryTotalChassisLabel = QLabel(self.PaintingChassisInventoryBox)
        self.PaintStationInventoryTotalChassisLabel.setObjectName(u"PaintStationInventoryTotalChassisLabel")

        self.gridLayout_40.addWidget(self.PaintStationInventoryTotalChassisLabel, 0, 0, 1, 1)

        self.horizontalSpacer_196 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_196, 0, 1, 1, 1)

        self.PaintStationInventoryTotalChassisCount = QLCDNumber(self.PaintingChassisInventoryBox)
        self.PaintStationInventoryTotalChassisCount.setObjectName(u"PaintStationInventoryTotalChassisCount")
        self.PaintStationInventoryTotalChassisCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_40.addWidget(self.PaintStationInventoryTotalChassisCount, 0, 2, 1, 1)

        self.PaintStationInventoryNormalChassisLabel = QLabel(self.PaintingChassisInventoryBox)
        self.PaintStationInventoryNormalChassisLabel.setObjectName(u"PaintStationInventoryNormalChassisLabel")

        self.gridLayout_40.addWidget(self.PaintStationInventoryNormalChassisLabel, 1, 0, 1, 1)

        self.horizontalSpacer_197 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_197, 1, 1, 1, 1)

        self.PaintStationInventoryNormalChassisLabelCount = QLCDNumber(self.PaintingChassisInventoryBox)
        self.PaintStationInventoryNormalChassisLabelCount.setObjectName(u"PaintStationInventoryNormalChassisLabelCount")
        self.PaintStationInventoryNormalChassisLabelCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_40.addWidget(self.PaintStationInventoryNormalChassisLabelCount, 1, 2, 1, 1)

        self.PaintStationInventorySportsChassisLabel = QLabel(self.PaintingChassisInventoryBox)
        self.PaintStationInventorySportsChassisLabel.setObjectName(u"PaintStationInventorySportsChassisLabel")

        self.gridLayout_40.addWidget(self.PaintStationInventorySportsChassisLabel, 2, 0, 1, 1)

        self.horizontalSpacer_198 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_198, 2, 1, 1, 1)

        self.PaintStationInventorySportsChassisCount = QLCDNumber(self.PaintingChassisInventoryBox)
        self.PaintStationInventorySportsChassisCount.setObjectName(u"PaintStationInventorySportsChassisCount")
        self.PaintStationInventorySportsChassisCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_40.addWidget(self.PaintStationInventorySportsChassisCount, 2, 2, 1, 1)

        self.PaintStationInventoryKidsChassisLabel = QLabel(self.PaintingChassisInventoryBox)
        self.PaintStationInventoryKidsChassisLabel.setObjectName(u"PaintStationInventoryKidsChassisLabel")

        self.gridLayout_40.addWidget(self.PaintStationInventoryKidsChassisLabel, 3, 0, 1, 1)

        self.horizontalSpacer_199 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_199, 3, 1, 1, 1)

        self.PaintStationInventoryKidsChassisCount = QLCDNumber(self.PaintingChassisInventoryBox)
        self.PaintStationInventoryKidsChassisCount.setObjectName(u"PaintStationInventoryKidsChassisCount")
        self.PaintStationInventoryKidsChassisCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_40.addWidget(self.PaintStationInventoryKidsChassisCount, 3, 2, 1, 1)


        self.gridLayout_61.addWidget(self.PaintingChassisInventoryBox, 0, 3, 1, 1)

        self.PaintInventoryBox = QGroupBox(self.PaintingStationInventoryBox)
        self.PaintInventoryBox.setObjectName(u"PaintInventoryBox")
        self.gridLayout_60 = QGridLayout(self.PaintInventoryBox)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.horizontalSpacer_201 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_60.addItem(self.horizontalSpacer_201, 0, 1, 1, 2)

        self.PaintStationRedPaintCount = QLCDNumber(self.PaintInventoryBox)
        self.PaintStationRedPaintCount.setObjectName(u"PaintStationRedPaintCount")
        self.PaintStationRedPaintCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_60.addWidget(self.PaintStationRedPaintCount, 4, 3, 1, 1)

        self.horizontalSpacer_270 = QSpacerItem(30, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_60.addItem(self.horizontalSpacer_270, 8, 2, 1, 1)

        self.PaintStationOrangePaintLabel = QLabel(self.PaintInventoryBox)
        self.PaintStationOrangePaintLabel.setObjectName(u"PaintStationOrangePaintLabel")

        self.gridLayout_60.addWidget(self.PaintStationOrangePaintLabel, 6, 0, 1, 1)

        self.PaintStationOrangePaintCount = QLCDNumber(self.PaintInventoryBox)
        self.PaintStationOrangePaintCount.setObjectName(u"PaintStationOrangePaintCount")
        self.PaintStationOrangePaintCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_60.addWidget(self.PaintStationOrangePaintCount, 6, 3, 1, 1)

        self.PaintStationBluePaintCount = QLCDNumber(self.PaintInventoryBox)
        self.PaintStationBluePaintCount.setObjectName(u"PaintStationBluePaintCount")
        self.PaintStationBluePaintCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_60.addWidget(self.PaintStationBluePaintCount, 3, 3, 1, 1)

        self.PaintStationWhitePaintLabel = QLabel(self.PaintInventoryBox)
        self.PaintStationWhitePaintLabel.setObjectName(u"PaintStationWhitePaintLabel")

        self.gridLayout_60.addWidget(self.PaintStationWhitePaintLabel, 0, 0, 1, 1)

        self.PaintStationPurplePaintLabel = QLabel(self.PaintInventoryBox)
        self.PaintStationPurplePaintLabel.setObjectName(u"PaintStationPurplePaintLabel")

        self.gridLayout_60.addWidget(self.PaintStationPurplePaintLabel, 8, 0, 1, 1)

        self.PaintStationBlackPaintCount = QLCDNumber(self.PaintInventoryBox)
        self.PaintStationBlackPaintCount.setObjectName(u"PaintStationBlackPaintCount")
        self.PaintStationBlackPaintCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_60.addWidget(self.PaintStationBlackPaintCount, 1, 3, 1, 1)

        self.PaintStationBluePaintLabel = QLabel(self.PaintInventoryBox)
        self.PaintStationBluePaintLabel.setObjectName(u"PaintStationBluePaintLabel")

        self.gridLayout_60.addWidget(self.PaintStationBluePaintLabel, 3, 0, 1, 2)

        self.PaintStationBlackPaintLabel = QLabel(self.PaintInventoryBox)
        self.PaintStationBlackPaintLabel.setObjectName(u"PaintStationBlackPaintLabel")

        self.gridLayout_60.addWidget(self.PaintStationBlackPaintLabel, 1, 0, 1, 1)

        self.horizontalSpacer_269 = QSpacerItem(30, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_60.addItem(self.horizontalSpacer_269, 7, 2, 1, 1)

        self.horizontalSpacer_204 = QSpacerItem(30, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_60.addItem(self.horizontalSpacer_204, 3, 2, 1, 1)

        self.horizontalSpacer_266 = QSpacerItem(30, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_60.addItem(self.horizontalSpacer_266, 4, 2, 1, 1)

        self.PaintStationGreyPaintCount = QLCDNumber(self.PaintInventoryBox)
        self.PaintStationGreyPaintCount.setObjectName(u"PaintStationGreyPaintCount")
        self.PaintStationGreyPaintCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_60.addWidget(self.PaintStationGreyPaintCount, 2, 3, 1, 1)

        self.PaintStationGreenPaintCount = QLCDNumber(self.PaintInventoryBox)
        self.PaintStationGreenPaintCount.setObjectName(u"PaintStationGreenPaintCount")
        self.PaintStationGreenPaintCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_60.addWidget(self.PaintStationGreenPaintCount, 5, 3, 1, 1)

        self.horizontalSpacer_203 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_60.addItem(self.horizontalSpacer_203, 2, 1, 1, 2)

        self.PaintStationPurplePaintCount = QLCDNumber(self.PaintInventoryBox)
        self.PaintStationPurplePaintCount.setObjectName(u"PaintStationPurplePaintCount")
        self.PaintStationPurplePaintCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_60.addWidget(self.PaintStationPurplePaintCount, 8, 3, 1, 1)

        self.horizontalSpacer_268 = QSpacerItem(30, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_60.addItem(self.horizontalSpacer_268, 6, 2, 1, 1)

        self.horizontalSpacer_267 = QSpacerItem(30, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_60.addItem(self.horizontalSpacer_267, 5, 2, 1, 1)

        self.horizontalSpacer_202 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_60.addItem(self.horizontalSpacer_202, 1, 1, 1, 2)

        self.PaintStationGreenPaintLabel = QLabel(self.PaintInventoryBox)
        self.PaintStationGreenPaintLabel.setObjectName(u"PaintStationGreenPaintLabel")

        self.gridLayout_60.addWidget(self.PaintStationGreenPaintLabel, 5, 0, 1, 1)

        self.PaintStationRedPaintLabel = QLabel(self.PaintInventoryBox)
        self.PaintStationRedPaintLabel.setObjectName(u"PaintStationRedPaintLabel")

        self.gridLayout_60.addWidget(self.PaintStationRedPaintLabel, 4, 0, 1, 1)

        self.PaintStationGreyPaintLabel = QLabel(self.PaintInventoryBox)
        self.PaintStationGreyPaintLabel.setObjectName(u"PaintStationGreyPaintLabel")

        self.gridLayout_60.addWidget(self.PaintStationGreyPaintLabel, 2, 0, 1, 1)

        self.PaintStationPinkPaintLabel = QLabel(self.PaintInventoryBox)
        self.PaintStationPinkPaintLabel.setObjectName(u"PaintStationPinkPaintLabel")

        self.gridLayout_60.addWidget(self.PaintStationPinkPaintLabel, 7, 0, 1, 1)

        self.PaintStationWhitePaintCount = QLCDNumber(self.PaintInventoryBox)
        self.PaintStationWhitePaintCount.setObjectName(u"PaintStationWhitePaintCount")
        self.PaintStationWhitePaintCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_60.addWidget(self.PaintStationWhitePaintCount, 0, 3, 1, 1)

        self.PaintStationPinkPaintCount = QLCDNumber(self.PaintInventoryBox)
        self.PaintStationPinkPaintCount.setObjectName(u"PaintStationPinkPaintCount")
        self.PaintStationPinkPaintCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_60.addWidget(self.PaintStationPinkPaintCount, 7, 3, 1, 1)

        self.PaintStationYellowPaintLabel = QLabel(self.PaintInventoryBox)
        self.PaintStationYellowPaintLabel.setObjectName(u"PaintStationYellowPaintLabel")

        self.gridLayout_60.addWidget(self.PaintStationYellowPaintLabel, 10, 0, 1, 1)

        self.horizontalSpacer_276 = QSpacerItem(30, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_60.addItem(self.horizontalSpacer_276, 10, 2, 1, 1)

        self.PaintStationYellowPaintCount = QLCDNumber(self.PaintInventoryBox)
        self.PaintStationYellowPaintCount.setObjectName(u"PaintStationYellowPaintCount")
        self.PaintStationYellowPaintCount.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_60.addWidget(self.PaintStationYellowPaintCount, 10, 3, 1, 1)


        self.gridLayout_61.addWidget(self.PaintInventoryBox, 0, 0, 2, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_61.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.gridLayout_62.addWidget(self.PaintingStationInventoryBox, 0, 1, 2, 1)

        self.PaintingStationBox = QGroupBox(self.Painting)
        self.PaintingStationBox.setObjectName(u"PaintingStationBox")
        self.gridLayout_5 = QGridLayout(self.PaintingStationBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.PaintStationChassisLabel = QLabel(self.PaintingStationBox)
        self.PaintStationChassisLabel.setObjectName(u"PaintStationChassisLabel")

        self.gridLayout_5.addWidget(self.PaintStationChassisLabel, 0, 0, 1, 1)

        self.horizontalSpacer_74 = QSpacerItem(113, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_74, 0, 1, 1, 1)

        self.PaintStationChassisValue = QLabel(self.PaintingStationBox)
        self.PaintStationChassisValue.setObjectName(u"PaintStationChassisValue")

        self.gridLayout_5.addWidget(self.PaintStationChassisValue, 0, 2, 1, 1)

        self.PaintStationColourLabel = QLabel(self.PaintingStationBox)
        self.PaintStationColourLabel.setObjectName(u"PaintStationColourLabel")

        self.gridLayout_5.addWidget(self.PaintStationColourLabel, 1, 0, 1, 1)

        self.horizontalSpacer_75 = QSpacerItem(113, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_75, 1, 1, 1, 1)

        self.PaintStationColourValue = QLabel(self.PaintingStationBox)
        self.PaintStationColourValue.setObjectName(u"PaintStationColourValue")

        self.gridLayout_5.addWidget(self.PaintStationColourValue, 1, 2, 1, 1)

        self.PaintedButton = QPushButton(self.PaintingStationBox)
        self.PaintedButton.setObjectName(u"PaintedButton")

        self.gridLayout_5.addWidget(self.PaintedButton, 2, 0, 1, 3)


        self.gridLayout_62.addWidget(self.PaintingStationBox, 0, 2, 1, 1)

        self.PaintOrder = QGroupBox(self.Painting)
        self.PaintOrder.setObjectName(u"PaintOrder")
        self.PaintOrder.setMinimumSize(QSize(281, 385))
        self.gridLayout_27 = QGridLayout(self.PaintOrder)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.GearsLabel_5 = QLabel(self.PaintOrder)
        self.GearsLabel_5.setObjectName(u"GearsLabel_5")

        self.gridLayout_27.addWidget(self.GearsLabel_5, 8, 0, 1, 1)

        self.GearType_5 = QLabel(self.PaintOrder)
        self.GearType_5.setObjectName(u"GearType_5")

        self.gridLayout_27.addWidget(self.GearType_5, 8, 3, 1, 1)

        self.horizontalSpacer_93 = QSpacerItem(103, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_93, 3, 2, 1, 2)

        self.ColourLabel_5 = QLabel(self.PaintOrder)
        self.ColourLabel_5.setObjectName(u"ColourLabel_5")

        self.gridLayout_27.addWidget(self.ColourLabel_5, 4, 0, 1, 1)

        self.BikeTypeLabel_5 = QLabel(self.PaintOrder)
        self.BikeTypeLabel_5.setObjectName(u"BikeTypeLabel_5")

        self.gridLayout_27.addWidget(self.BikeTypeLabel_5, 1, 0, 1, 1)

        self.horizontalSpacer_95 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_95, 5, 1, 1, 2)

        self.horizontalSpacer_99 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_99, 10, 1, 1, 2)

        self.line_6 = QFrame(self.PaintOrder)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_27.addWidget(self.line_6, 2, 0, 1, 4)

        self.Colour_5 = QLabel(self.PaintOrder)
        self.Colour_5.setObjectName(u"Colour_5")

        self.gridLayout_27.addWidget(self.Colour_5, 4, 3, 1, 1)

        self.PedalLabel_5 = QLabel(self.PaintOrder)
        self.PedalLabel_5.setObjectName(u"PedalLabel_5")

        self.gridLayout_27.addWidget(self.PedalLabel_5, 5, 0, 1, 1)

        self.PedalType_5 = QLabel(self.PaintOrder)
        self.PedalType_5.setObjectName(u"PedalType_5")

        self.gridLayout_27.addWidget(self.PedalType_5, 5, 3, 1, 1)

        self.BrakesLabel_5 = QLabel(self.PaintOrder)
        self.BrakesLabel_5.setObjectName(u"BrakesLabel_5")

        self.gridLayout_27.addWidget(self.BrakesLabel_5, 10, 0, 1, 1)

        self.SeatType_5 = QLabel(self.PaintOrder)
        self.SeatType_5.setObjectName(u"SeatType_5")

        self.gridLayout_27.addWidget(self.SeatType_5, 12, 3, 1, 1)

        self.ChainLabel_5 = QLabel(self.PaintOrder)
        self.ChainLabel_5.setObjectName(u"ChainLabel_5")

        self.gridLayout_27.addWidget(self.ChainLabel_5, 7, 0, 1, 1)

        self.horizontalSpacer_100 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_100, 11, 1, 1, 2)

        self.horizontalSpacer_98 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_98, 8, 1, 1, 2)

        self.BrakesType_5 = QLabel(self.PaintOrder)
        self.BrakesType_5.setObjectName(u"BrakesType_5")

        self.gridLayout_27.addWidget(self.BrakesType_5, 10, 3, 1, 1)

        self.SeatLabel_5 = QLabel(self.PaintOrder)
        self.SeatLabel_5.setObjectName(u"SeatLabel_5")

        self.gridLayout_27.addWidget(self.SeatLabel_5, 12, 0, 1, 1)

        self.OrderNumber_5 = QLabel(self.PaintOrder)
        self.OrderNumber_5.setObjectName(u"OrderNumber_5")

        self.gridLayout_27.addWidget(self.OrderNumber_5, 0, 2, 1, 2)

        self.ChainType_5 = QLabel(self.PaintOrder)
        self.ChainType_5.setObjectName(u"ChainType_5")

        self.gridLayout_27.addWidget(self.ChainType_5, 7, 3, 1, 1)

        self.horizontalSpacer_90 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_90, 0, 1, 1, 1)

        self.horizontalSpacer_92 = QSpacerItem(96, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_92, 3, 0, 1, 1)

        self.horizontalSpacer_91 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_91, 1, 1, 1, 1)

        self.OrderNumberLabel_5 = QLabel(self.PaintOrder)
        self.OrderNumberLabel_5.setObjectName(u"OrderNumberLabel_5")

        self.gridLayout_27.addWidget(self.OrderNumberLabel_5, 0, 0, 1, 1)

        self.LightsType_5 = QLabel(self.PaintOrder)
        self.LightsType_5.setObjectName(u"LightsType_5")

        self.gridLayout_27.addWidget(self.LightsType_5, 11, 3, 1, 1)

        self.PartsLabel_5 = QLabel(self.PaintOrder)
        self.PartsLabel_5.setObjectName(u"PartsLabel_5")
        self.PartsLabel_5.setScaledContents(False)
        self.PartsLabel_5.setWordWrap(False)

        self.gridLayout_27.addWidget(self.PartsLabel_5, 3, 1, 1, 1)

        self.BikeType_5 = QLabel(self.PaintOrder)
        self.BikeType_5.setObjectName(u"BikeType_5")

        self.gridLayout_27.addWidget(self.BikeType_5, 1, 2, 1, 2)

        self.horizontalSpacer_94 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_94, 4, 1, 1, 2)

        self.LightsLabel_5 = QLabel(self.PaintOrder)
        self.LightsLabel_5.setObjectName(u"LightsLabel_5")

        self.gridLayout_27.addWidget(self.LightsLabel_5, 11, 0, 1, 1)

        self.WheelsLabel_5 = QLabel(self.PaintOrder)
        self.WheelsLabel_5.setObjectName(u"WheelsLabel_5")

        self.gridLayout_27.addWidget(self.WheelsLabel_5, 9, 0, 1, 1)

        self.WheelType_5 = QLabel(self.PaintOrder)
        self.WheelType_5.setObjectName(u"WheelType_5")

        self.gridLayout_27.addWidget(self.WheelType_5, 9, 3, 1, 1)

        self.horizontalSpacer_96 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_96, 9, 1, 1, 2)

        self.horizontalSpacer_97 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_97, 7, 1, 1, 2)

        self.horizontalSpacer_101 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_101, 12, 1, 1, 2)


        self.gridLayout_62.addWidget(self.PaintOrder, 0, 0, 2, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 396, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_62.addItem(self.verticalSpacer_12, 1, 2, 1, 1)

        self.tabWidget.addTab(self.Painting, "")
        self.PedalAssembly = QWidget()
        self.PedalAssembly.setObjectName(u"PedalAssembly")
        self.gridLayout_12 = QGridLayout(self.PedalAssembly)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.PedalsOrder = QGroupBox(self.PedalAssembly)
        self.PedalsOrder.setObjectName(u"PedalsOrder")
        self.PedalsOrder.setMinimumSize(QSize(281, 385))
        self.gridLayout_26 = QGridLayout(self.PedalsOrder)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.horizontalSpacer_76 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_76, 0, 1, 1, 1)

        self.line_5 = QFrame(self.PedalsOrder)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_26.addWidget(self.line_5, 2, 0, 1, 4)

        self.BrakesLabel_4 = QLabel(self.PedalsOrder)
        self.BrakesLabel_4.setObjectName(u"BrakesLabel_4")

        self.gridLayout_26.addWidget(self.BrakesLabel_4, 10, 0, 1, 1)

        self.PartsLabel_4 = QLabel(self.PedalsOrder)
        self.PartsLabel_4.setObjectName(u"PartsLabel_4")
        self.PartsLabel_4.setScaledContents(False)
        self.PartsLabel_4.setWordWrap(False)

        self.gridLayout_26.addWidget(self.PartsLabel_4, 3, 1, 1, 1)

        self.GearType_4 = QLabel(self.PedalsOrder)
        self.GearType_4.setObjectName(u"GearType_4")

        self.gridLayout_26.addWidget(self.GearType_4, 8, 3, 1, 1)

        self.OrderNumberLabel_4 = QLabel(self.PedalsOrder)
        self.OrderNumberLabel_4.setObjectName(u"OrderNumberLabel_4")

        self.gridLayout_26.addWidget(self.OrderNumberLabel_4, 0, 0, 1, 1)

        self.horizontalSpacer_84 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_84, 8, 1, 1, 2)

        self.SeatType_4 = QLabel(self.PedalsOrder)
        self.SeatType_4.setObjectName(u"SeatType_4")

        self.gridLayout_26.addWidget(self.SeatType_4, 12, 3, 1, 1)

        self.horizontalSpacer_86 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_86, 11, 1, 1, 2)

        self.GearsLabel_4 = QLabel(self.PedalsOrder)
        self.GearsLabel_4.setObjectName(u"GearsLabel_4")

        self.gridLayout_26.addWidget(self.GearsLabel_4, 8, 0, 1, 1)

        self.PedalType_4 = QLabel(self.PedalsOrder)
        self.PedalType_4.setObjectName(u"PedalType_4")

        self.gridLayout_26.addWidget(self.PedalType_4, 5, 3, 1, 1)

        self.BikeTypeLabel_4 = QLabel(self.PedalsOrder)
        self.BikeTypeLabel_4.setObjectName(u"BikeTypeLabel_4")

        self.gridLayout_26.addWidget(self.BikeTypeLabel_4, 1, 0, 1, 1)

        self.ColourLabel_4 = QLabel(self.PedalsOrder)
        self.ColourLabel_4.setObjectName(u"ColourLabel_4")

        self.gridLayout_26.addWidget(self.ColourLabel_4, 4, 0, 1, 1)

        self.BikeType_4 = QLabel(self.PedalsOrder)
        self.BikeType_4.setObjectName(u"BikeType_4")

        self.gridLayout_26.addWidget(self.BikeType_4, 1, 2, 1, 2)

        self.horizontalSpacer_80 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_80, 4, 1, 1, 2)

        self.horizontalSpacer_85 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_85, 10, 1, 1, 2)

        self.ChainType_4 = QLabel(self.PedalsOrder)
        self.ChainType_4.setObjectName(u"ChainType_4")

        self.gridLayout_26.addWidget(self.ChainType_4, 7, 3, 1, 1)

        self.horizontalSpacer_81 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_81, 5, 1, 1, 2)

        self.BrakesType_4 = QLabel(self.PedalsOrder)
        self.BrakesType_4.setObjectName(u"BrakesType_4")

        self.gridLayout_26.addWidget(self.BrakesType_4, 10, 3, 1, 1)

        self.Colour_4 = QLabel(self.PedalsOrder)
        self.Colour_4.setObjectName(u"Colour_4")

        self.gridLayout_26.addWidget(self.Colour_4, 4, 3, 1, 1)

        self.LightsType_4 = QLabel(self.PedalsOrder)
        self.LightsType_4.setObjectName(u"LightsType_4")

        self.gridLayout_26.addWidget(self.LightsType_4, 11, 3, 1, 1)

        self.horizontalSpacer_78 = QSpacerItem(96, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_78, 3, 0, 1, 1)

        self.LightsLabel_4 = QLabel(self.PedalsOrder)
        self.LightsLabel_4.setObjectName(u"LightsLabel_4")

        self.gridLayout_26.addWidget(self.LightsLabel_4, 11, 0, 1, 1)

        self.SeatLabel_4 = QLabel(self.PedalsOrder)
        self.SeatLabel_4.setObjectName(u"SeatLabel_4")

        self.gridLayout_26.addWidget(self.SeatLabel_4, 12, 0, 1, 1)

        self.horizontalSpacer_77 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_77, 1, 1, 1, 1)

        self.PedalLabel_4 = QLabel(self.PedalsOrder)
        self.PedalLabel_4.setObjectName(u"PedalLabel_4")

        self.gridLayout_26.addWidget(self.PedalLabel_4, 5, 0, 1, 1)

        self.OrderNumber_4 = QLabel(self.PedalsOrder)
        self.OrderNumber_4.setObjectName(u"OrderNumber_4")

        self.gridLayout_26.addWidget(self.OrderNumber_4, 0, 2, 1, 2)

        self.ChainLabel_4 = QLabel(self.PedalsOrder)
        self.ChainLabel_4.setObjectName(u"ChainLabel_4")

        self.gridLayout_26.addWidget(self.ChainLabel_4, 7, 0, 1, 1)

        self.horizontalSpacer_79 = QSpacerItem(103, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_79, 3, 2, 1, 2)

        self.WheelsLabel_4 = QLabel(self.PedalsOrder)
        self.WheelsLabel_4.setObjectName(u"WheelsLabel_4")

        self.gridLayout_26.addWidget(self.WheelsLabel_4, 9, 0, 1, 1)

        self.WheelType_4 = QLabel(self.PedalsOrder)
        self.WheelType_4.setObjectName(u"WheelType_4")

        self.gridLayout_26.addWidget(self.WheelType_4, 9, 3, 1, 1)

        self.horizontalSpacer_82 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_82, 9, 1, 1, 2)

        self.horizontalSpacer_83 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_83, 7, 1, 1, 2)

        self.horizontalSpacer_87 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_87, 12, 1, 1, 2)


        self.gridLayout_12.addWidget(self.PedalsOrder, 0, 0, 2, 1)

        self.PedalStationInventoryBox = QGroupBox(self.PedalAssembly)
        self.PedalStationInventoryBox.setObjectName(u"PedalStationInventoryBox")
        self.gridLayout_64 = QGridLayout(self.PedalStationInventoryBox)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.PedalStationChassisInventoryBox_2 = QGroupBox(self.PedalStationInventoryBox)
        self.PedalStationChassisInventoryBox_2.setObjectName(u"PedalStationChassisInventoryBox_2")
        self.gridLayout_37 = QGridLayout(self.PedalStationChassisInventoryBox_2)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.PedalStationInventoryTotalChassisLabel_2 = QLabel(self.PedalStationChassisInventoryBox_2)
        self.PedalStationInventoryTotalChassisLabel_2.setObjectName(u"PedalStationInventoryTotalChassisLabel_2")

        self.gridLayout_37.addWidget(self.PedalStationInventoryTotalChassisLabel_2, 0, 0, 1, 1)

        self.horizontalSpacer_191 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_37.addItem(self.horizontalSpacer_191, 0, 1, 1, 2)

        self.PedalStationInventoryTotalChassis_2 = QLCDNumber(self.PedalStationChassisInventoryBox_2)
        self.PedalStationInventoryTotalChassis_2.setObjectName(u"PedalStationInventoryTotalChassis_2")
        self.PedalStationInventoryTotalChassis_2.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_37.addWidget(self.PedalStationInventoryTotalChassis_2, 0, 3, 1, 1)

        self.PedalStationInventoryNormalChassisLabel_2 = QLabel(self.PedalStationChassisInventoryBox_2)
        self.PedalStationInventoryNormalChassisLabel_2.setObjectName(u"PedalStationInventoryNormalChassisLabel_2")

        self.gridLayout_37.addWidget(self.PedalStationInventoryNormalChassisLabel_2, 1, 0, 1, 1)

        self.horizontalSpacer_192 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_37.addItem(self.horizontalSpacer_192, 1, 1, 1, 2)

        self.PedalStationInventoryNormalChassis_2 = QLCDNumber(self.PedalStationChassisInventoryBox_2)
        self.PedalStationInventoryNormalChassis_2.setObjectName(u"PedalStationInventoryNormalChassis_2")
        self.PedalStationInventoryNormalChassis_2.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_37.addWidget(self.PedalStationInventoryNormalChassis_2, 1, 3, 1, 1)

        self.PedalStationInventoryTotalSportsChassisLabel_2 = QLabel(self.PedalStationChassisInventoryBox_2)
        self.PedalStationInventoryTotalSportsChassisLabel_2.setObjectName(u"PedalStationInventoryTotalSportsChassisLabel_2")

        self.gridLayout_37.addWidget(self.PedalStationInventoryTotalSportsChassisLabel_2, 2, 0, 1, 1)

        self.horizontalSpacer_193 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_37.addItem(self.horizontalSpacer_193, 2, 1, 1, 2)

        self.PedalStationInventorySportsChassis_2 = QLCDNumber(self.PedalStationChassisInventoryBox_2)
        self.PedalStationInventorySportsChassis_2.setObjectName(u"PedalStationInventorySportsChassis_2")
        self.PedalStationInventorySportsChassis_2.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_37.addWidget(self.PedalStationInventorySportsChassis_2, 2, 3, 1, 1)

        self.PedalStationInventoryTotalKidsChassisLabel_2 = QLabel(self.PedalStationChassisInventoryBox_2)
        self.PedalStationInventoryTotalKidsChassisLabel_2.setObjectName(u"PedalStationInventoryTotalKidsChassisLabel_2")

        self.gridLayout_37.addWidget(self.PedalStationInventoryTotalKidsChassisLabel_2, 3, 0, 1, 1)

        self.horizontalSpacer_194 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_37.addItem(self.horizontalSpacer_194, 3, 1, 1, 2)

        self.PedalStationInventoryKidsChassis_2 = QLCDNumber(self.PedalStationChassisInventoryBox_2)
        self.PedalStationInventoryKidsChassis_2.setObjectName(u"PedalStationInventoryKidsChassis_2")
        self.PedalStationInventoryKidsChassis_2.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_37.addWidget(self.PedalStationInventoryKidsChassis_2, 3, 3, 1, 1)

        self.PedalStationInventoryTotalKidsChassisLabel_3 = QLabel(self.PedalStationChassisInventoryBox_2)
        self.PedalStationInventoryTotalKidsChassisLabel_3.setObjectName(u"PedalStationInventoryTotalKidsChassisLabel_3")

        self.gridLayout_37.addWidget(self.PedalStationInventoryTotalKidsChassisLabel_3, 4, 0, 1, 2)

        self.horizontalSpacer_195 = QSpacerItem(30, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_37.addItem(self.horizontalSpacer_195, 4, 2, 1, 1)

        self.PedalStationInventoryKidsChassis_3 = QLCDNumber(self.PedalStationChassisInventoryBox_2)
        self.PedalStationInventoryKidsChassis_3.setObjectName(u"PedalStationInventoryKidsChassis_3")
        self.PedalStationInventoryKidsChassis_3.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_37.addWidget(self.PedalStationInventoryKidsChassis_3, 4, 3, 1, 1)


        self.gridLayout_64.addWidget(self.PedalStationChassisInventoryBox_2, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(241, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_64.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.PedalStationChassisInventoryBox = QGroupBox(self.PedalStationInventoryBox)
        self.PedalStationChassisInventoryBox.setObjectName(u"PedalStationChassisInventoryBox")
        self.gridLayout_63 = QGridLayout(self.PedalStationChassisInventoryBox)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.PedalStationInventoryTotalChassisLabel = QLabel(self.PedalStationChassisInventoryBox)
        self.PedalStationInventoryTotalChassisLabel.setObjectName(u"PedalStationInventoryTotalChassisLabel")

        self.gridLayout_63.addWidget(self.PedalStationInventoryTotalChassisLabel, 0, 0, 1, 1)

        self.horizontalSpacer_187 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_63.addItem(self.horizontalSpacer_187, 0, 1, 1, 1)

        self.PedalStationInventoryTotalChassis = QLCDNumber(self.PedalStationChassisInventoryBox)
        self.PedalStationInventoryTotalChassis.setObjectName(u"PedalStationInventoryTotalChassis")
        self.PedalStationInventoryTotalChassis.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_63.addWidget(self.PedalStationInventoryTotalChassis, 0, 2, 1, 1)

        self.horizontalSpacer_88 = QSpacerItem(258, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_63.addItem(self.horizontalSpacer_88, 0, 3, 1, 1)

        self.PedalStationInventoryChassisTable = QTableWidget(self.PedalStationChassisInventoryBox)
        if (self.PedalStationInventoryChassisTable.columnCount() < 2):
            self.PedalStationInventoryChassisTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.PedalStationInventoryChassisTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.PedalStationInventoryChassisTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.PedalStationInventoryChassisTable.setObjectName(u"PedalStationInventoryChassisTable")

        self.gridLayout_63.addWidget(self.PedalStationInventoryChassisTable, 1, 0, 1, 4)


        self.gridLayout_64.addWidget(self.PedalStationChassisInventoryBox, 1, 0, 1, 2)


        self.gridLayout_12.addWidget(self.PedalStationInventoryBox, 0, 1, 2, 1)

        self.groupBox_3 = QGroupBox(self.PedalAssembly)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_6.addWidget(self.pushButton_2, 5, 0, 1, 3)

        self.label_39 = QLabel(self.groupBox_3)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_6.addWidget(self.label_39, 0, 0, 1, 1)

        self.label_38 = QLabel(self.groupBox_3)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_6.addWidget(self.label_38, 0, 2, 1, 1)

        self.label_85 = QLabel(self.groupBox_3)
        self.label_85.setObjectName(u"label_85")

        self.gridLayout_6.addWidget(self.label_85, 4, 0, 1, 1)

        self.label_40 = QLabel(self.groupBox_3)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_6.addWidget(self.label_40, 4, 2, 1, 1)

        self.horizontalSpacer_181 = QSpacerItem(77, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_181, 4, 1, 1, 1)

        self.horizontalSpacer_89 = QSpacerItem(73, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_89, 0, 1, 1, 1)

        self.horizontalSpacer_130 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_130, 1, 1, 1, 1)

        self.label_60 = QLabel(self.groupBox_3)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_6.addWidget(self.label_60, 1, 0, 1, 1)

        self.label_59 = QLabel(self.groupBox_3)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_6.addWidget(self.label_59, 1, 2, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_3, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 441, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer, 1, 2, 1, 1)

        self.tabWidget.addTab(self.PedalAssembly, "")
        self.DriveChainAssembly = QWidget()
        self.DriveChainAssembly.setObjectName(u"DriveChainAssembly")
        self.gridLayout_66 = QGridLayout(self.DriveChainAssembly)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.DriveChainOrder = QGroupBox(self.DriveChainAssembly)
        self.DriveChainOrder.setObjectName(u"DriveChainOrder")
        self.DriveChainOrder.setMinimumSize(QSize(281, 385))
        self.gridLayout_29 = QGridLayout(self.DriveChainOrder)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.horizontalSpacer_119 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_119, 1, 1, 1, 1)

        self.ColourLabel_7 = QLabel(self.DriveChainOrder)
        self.ColourLabel_7.setObjectName(u"ColourLabel_7")

        self.gridLayout_29.addWidget(self.ColourLabel_7, 4, 0, 1, 1)

        self.SeatLabel_7 = QLabel(self.DriveChainOrder)
        self.SeatLabel_7.setObjectName(u"SeatLabel_7")

        self.gridLayout_29.addWidget(self.SeatLabel_7, 12, 0, 1, 1)

        self.SeatType_7 = QLabel(self.DriveChainOrder)
        self.SeatType_7.setObjectName(u"SeatType_7")

        self.gridLayout_29.addWidget(self.SeatType_7, 12, 3, 1, 1)

        self.LightsLabel_7 = QLabel(self.DriveChainOrder)
        self.LightsLabel_7.setObjectName(u"LightsLabel_7")

        self.gridLayout_29.addWidget(self.LightsLabel_7, 11, 0, 1, 1)

        self.horizontalSpacer_121 = QSpacerItem(103, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_121, 3, 2, 1, 2)

        self.horizontalSpacer_118 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_118, 0, 1, 1, 1)

        self.horizontalSpacer_122 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_122, 4, 1, 1, 2)

        self.BrakesLabel_7 = QLabel(self.DriveChainOrder)
        self.BrakesLabel_7.setObjectName(u"BrakesLabel_7")

        self.gridLayout_29.addWidget(self.BrakesLabel_7, 10, 0, 1, 1)

        self.horizontalSpacer_120 = QSpacerItem(96, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_120, 3, 0, 1, 1)

        self.ChainType_7 = QLabel(self.DriveChainOrder)
        self.ChainType_7.setObjectName(u"ChainType_7")

        self.gridLayout_29.addWidget(self.ChainType_7, 7, 3, 1, 1)

        self.horizontalSpacer_128 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_128, 11, 1, 1, 2)

        self.PartsLabel_7 = QLabel(self.DriveChainOrder)
        self.PartsLabel_7.setObjectName(u"PartsLabel_7")
        self.PartsLabel_7.setScaledContents(False)
        self.PartsLabel_7.setWordWrap(False)

        self.gridLayout_29.addWidget(self.PartsLabel_7, 3, 1, 1, 1)

        self.PedalLabel_7 = QLabel(self.DriveChainOrder)
        self.PedalLabel_7.setObjectName(u"PedalLabel_7")

        self.gridLayout_29.addWidget(self.PedalLabel_7, 5, 0, 1, 1)

        self.horizontalSpacer_123 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_123, 5, 1, 1, 2)

        self.GearType_7 = QLabel(self.DriveChainOrder)
        self.GearType_7.setObjectName(u"GearType_7")

        self.gridLayout_29.addWidget(self.GearType_7, 8, 3, 1, 1)

        self.LightsType_7 = QLabel(self.DriveChainOrder)
        self.LightsType_7.setObjectName(u"LightsType_7")

        self.gridLayout_29.addWidget(self.LightsType_7, 11, 3, 1, 1)

        self.BikeType_7 = QLabel(self.DriveChainOrder)
        self.BikeType_7.setObjectName(u"BikeType_7")

        self.gridLayout_29.addWidget(self.BikeType_7, 1, 2, 1, 2)

        self.Colour_7 = QLabel(self.DriveChainOrder)
        self.Colour_7.setObjectName(u"Colour_7")

        self.gridLayout_29.addWidget(self.Colour_7, 4, 3, 1, 1)

        self.BrakesType_7 = QLabel(self.DriveChainOrder)
        self.BrakesType_7.setObjectName(u"BrakesType_7")

        self.gridLayout_29.addWidget(self.BrakesType_7, 10, 3, 1, 1)

        self.line_8 = QFrame(self.DriveChainOrder)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_29.addWidget(self.line_8, 2, 0, 1, 4)

        self.OrderNumberLabel_7 = QLabel(self.DriveChainOrder)
        self.OrderNumberLabel_7.setObjectName(u"OrderNumberLabel_7")

        self.gridLayout_29.addWidget(self.OrderNumberLabel_7, 0, 0, 1, 1)

        self.horizontalSpacer_127 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_127, 10, 1, 1, 2)

        self.horizontalSpacer_126 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_126, 8, 1, 1, 2)

        self.BikeTypeLabel_7 = QLabel(self.DriveChainOrder)
        self.BikeTypeLabel_7.setObjectName(u"BikeTypeLabel_7")

        self.gridLayout_29.addWidget(self.BikeTypeLabel_7, 1, 0, 1, 1)

        self.ChainLabel_7 = QLabel(self.DriveChainOrder)
        self.ChainLabel_7.setObjectName(u"ChainLabel_7")

        self.gridLayout_29.addWidget(self.ChainLabel_7, 7, 0, 1, 1)

        self.PedalType_7 = QLabel(self.DriveChainOrder)
        self.PedalType_7.setObjectName(u"PedalType_7")

        self.gridLayout_29.addWidget(self.PedalType_7, 5, 3, 1, 1)

        self.OrderNumber_7 = QLabel(self.DriveChainOrder)
        self.OrderNumber_7.setObjectName(u"OrderNumber_7")

        self.gridLayout_29.addWidget(self.OrderNumber_7, 0, 2, 1, 2)

        self.GearsLabel_7 = QLabel(self.DriveChainOrder)
        self.GearsLabel_7.setObjectName(u"GearsLabel_7")

        self.gridLayout_29.addWidget(self.GearsLabel_7, 8, 0, 1, 1)

        self.WheelsLabel_7 = QLabel(self.DriveChainOrder)
        self.WheelsLabel_7.setObjectName(u"WheelsLabel_7")

        self.gridLayout_29.addWidget(self.WheelsLabel_7, 9, 0, 1, 1)

        self.WheelType_7 = QLabel(self.DriveChainOrder)
        self.WheelType_7.setObjectName(u"WheelType_7")

        self.gridLayout_29.addWidget(self.WheelType_7, 9, 3, 1, 1)

        self.horizontalSpacer_124 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_124, 9, 1, 1, 2)

        self.horizontalSpacer_125 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_125, 7, 1, 1, 2)

        self.horizontalSpacer_129 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_129, 12, 1, 1, 2)


        self.gridLayout_66.addWidget(self.DriveChainOrder, 0, 0, 1, 1)

        self.DCStationInventoryBox = QGroupBox(self.DriveChainAssembly)
        self.DCStationInventoryBox.setObjectName(u"DCStationInventoryBox")
        self.gridLayout_42 = QGridLayout(self.DCStationInventoryBox)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.DCStationGearInventoryBox = QGroupBox(self.DCStationInventoryBox)
        self.DCStationGearInventoryBox.setObjectName(u"DCStationGearInventoryBox")
        self.gridLayout_38 = QGridLayout(self.DCStationGearInventoryBox)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.DCStationInventoryTotalGearLabel = QLabel(self.DCStationGearInventoryBox)
        self.DCStationInventoryTotalGearLabel.setObjectName(u"DCStationInventoryTotalGearLabel")

        self.gridLayout_38.addWidget(self.DCStationInventoryTotalGearLabel, 0, 0, 1, 1)

        self.horizontalSpacer_200 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_38.addItem(self.horizontalSpacer_200, 0, 1, 1, 2)

        self.DCStationInventoryTotalGearCounter = QLCDNumber(self.DCStationGearInventoryBox)
        self.DCStationInventoryTotalGearCounter.setObjectName(u"DCStationInventoryTotalGearCounter")
        self.DCStationInventoryTotalGearCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_38.addWidget(self.DCStationInventoryTotalGearCounter, 0, 3, 1, 1)

        self.DCStationInventoryNormalGearLabel = QLabel(self.DCStationGearInventoryBox)
        self.DCStationInventoryNormalGearLabel.setObjectName(u"DCStationInventoryNormalGearLabel")

        self.gridLayout_38.addWidget(self.DCStationInventoryNormalGearLabel, 1, 0, 1, 1)

        self.horizontalSpacer_205 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_38.addItem(self.horizontalSpacer_205, 1, 1, 1, 2)

        self.DCStationInventoryNormalGearCounter = QLCDNumber(self.DCStationGearInventoryBox)
        self.DCStationInventoryNormalGearCounter.setObjectName(u"DCStationInventoryNormalGearCounter")
        self.DCStationInventoryNormalGearCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_38.addWidget(self.DCStationInventoryNormalGearCounter, 1, 3, 1, 1)

        self.DCStationInventorySporsGearLabel = QLabel(self.DCStationGearInventoryBox)
        self.DCStationInventorySporsGearLabel.setObjectName(u"DCStationInventorySporsGearLabel")

        self.gridLayout_38.addWidget(self.DCStationInventorySporsGearLabel, 2, 0, 1, 1)

        self.horizontalSpacer_206 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_38.addItem(self.horizontalSpacer_206, 2, 1, 1, 2)

        self.DCStationInventorySportsGearCounter = QLCDNumber(self.DCStationGearInventoryBox)
        self.DCStationInventorySportsGearCounter.setObjectName(u"DCStationInventorySportsGearCounter")
        self.DCStationInventorySportsGearCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_38.addWidget(self.DCStationInventorySportsGearCounter, 2, 3, 1, 1)

        self.DCStationInventoryKidsGearLabel = QLabel(self.DCStationGearInventoryBox)
        self.DCStationInventoryKidsGearLabel.setObjectName(u"DCStationInventoryKidsGearLabel")

        self.gridLayout_38.addWidget(self.DCStationInventoryKidsGearLabel, 3, 0, 1, 1)

        self.horizontalSpacer_207 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_38.addItem(self.horizontalSpacer_207, 3, 1, 1, 2)

        self.DCStationInventoryKidsGearCounter = QLCDNumber(self.DCStationGearInventoryBox)
        self.DCStationInventoryKidsGearCounter.setObjectName(u"DCStationInventoryKidsGearCounter")
        self.DCStationInventoryKidsGearCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_38.addWidget(self.DCStationInventoryKidsGearCounter, 3, 3, 1, 1)

        self.DCStationInventoryPremiumGearLabel = QLabel(self.DCStationGearInventoryBox)
        self.DCStationInventoryPremiumGearLabel.setObjectName(u"DCStationInventoryPremiumGearLabel")

        self.gridLayout_38.addWidget(self.DCStationInventoryPremiumGearLabel, 4, 0, 1, 2)

        self.horizontalSpacer_208 = QSpacerItem(30, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_38.addItem(self.horizontalSpacer_208, 4, 2, 1, 1)

        self.DCStationInventoryPremiumGearCounter = QLCDNumber(self.DCStationGearInventoryBox)
        self.DCStationInventoryPremiumGearCounter.setObjectName(u"DCStationInventoryPremiumGearCounter")
        self.DCStationInventoryPremiumGearCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_38.addWidget(self.DCStationInventoryPremiumGearCounter, 4, 3, 1, 1)


        self.gridLayout_42.addWidget(self.DCStationGearInventoryBox, 0, 0, 1, 1)

        self.DCStationChainInventory = QGroupBox(self.DCStationInventoryBox)
        self.DCStationChainInventory.setObjectName(u"DCStationChainInventory")
        self.gridLayout_39 = QGridLayout(self.DCStationChainInventory)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.DCStationInventoryTotalChainLabel = QLabel(self.DCStationChainInventory)
        self.DCStationInventoryTotalChainLabel.setObjectName(u"DCStationInventoryTotalChainLabel")

        self.gridLayout_39.addWidget(self.DCStationInventoryTotalChainLabel, 0, 0, 1, 1)

        self.horizontalSpacer_209 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_39.addItem(self.horizontalSpacer_209, 0, 1, 1, 2)

        self.DCStationInventoryTotalChainCounter = QLCDNumber(self.DCStationChainInventory)
        self.DCStationInventoryTotalChainCounter.setObjectName(u"DCStationInventoryTotalChainCounter")
        self.DCStationInventoryTotalChainCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_39.addWidget(self.DCStationInventoryTotalChainCounter, 0, 3, 1, 1)

        self.DCStationInventoryNormalChainLabel = QLabel(self.DCStationChainInventory)
        self.DCStationInventoryNormalChainLabel.setObjectName(u"DCStationInventoryNormalChainLabel")

        self.gridLayout_39.addWidget(self.DCStationInventoryNormalChainLabel, 1, 0, 1, 1)

        self.horizontalSpacer_210 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_39.addItem(self.horizontalSpacer_210, 1, 1, 1, 2)

        self.DCStationInventoryNormalChainCounter = QLCDNumber(self.DCStationChainInventory)
        self.DCStationInventoryNormalChainCounter.setObjectName(u"DCStationInventoryNormalChainCounter")
        self.DCStationInventoryNormalChainCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_39.addWidget(self.DCStationInventoryNormalChainCounter, 1, 3, 1, 1)

        self.DCStationInventorySportsChainLabel = QLabel(self.DCStationChainInventory)
        self.DCStationInventorySportsChainLabel.setObjectName(u"DCStationInventorySportsChainLabel")

        self.gridLayout_39.addWidget(self.DCStationInventorySportsChainLabel, 2, 0, 1, 1)

        self.horizontalSpacer_211 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_39.addItem(self.horizontalSpacer_211, 2, 1, 1, 2)

        self.DCStationInventorySportsChainCounter = QLCDNumber(self.DCStationChainInventory)
        self.DCStationInventorySportsChainCounter.setObjectName(u"DCStationInventorySportsChainCounter")
        self.DCStationInventorySportsChainCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_39.addWidget(self.DCStationInventorySportsChainCounter, 2, 3, 1, 1)

        self.DCStationInventoryKidsChainLabel = QLabel(self.DCStationChainInventory)
        self.DCStationInventoryKidsChainLabel.setObjectName(u"DCStationInventoryKidsChainLabel")

        self.gridLayout_39.addWidget(self.DCStationInventoryKidsChainLabel, 3, 0, 1, 1)

        self.horizontalSpacer_212 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_39.addItem(self.horizontalSpacer_212, 3, 1, 1, 2)

        self.DCStationInventoryKidsChainCounter = QLCDNumber(self.DCStationChainInventory)
        self.DCStationInventoryKidsChainCounter.setObjectName(u"DCStationInventoryKidsChainCounter")
        self.DCStationInventoryKidsChainCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_39.addWidget(self.DCStationInventoryKidsChainCounter, 3, 3, 1, 1)

        self.DCStationInventoryPremiumChainLabel = QLabel(self.DCStationChainInventory)
        self.DCStationInventoryPremiumChainLabel.setObjectName(u"DCStationInventoryPremiumChainLabel")

        self.gridLayout_39.addWidget(self.DCStationInventoryPremiumChainLabel, 4, 0, 1, 2)

        self.horizontalSpacer_213 = QSpacerItem(30, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_39.addItem(self.horizontalSpacer_213, 4, 2, 1, 1)

        self.DCStationInventoryPremiumChainCounter = QLCDNumber(self.DCStationChainInventory)
        self.DCStationInventoryPremiumChainCounter.setObjectName(u"DCStationInventoryPremiumChainCounter")
        self.DCStationInventoryPremiumChainCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_39.addWidget(self.DCStationInventoryPremiumChainCounter, 4, 3, 1, 1)


        self.gridLayout_42.addWidget(self.DCStationChainInventory, 0, 1, 1, 1)

        self.DCStationChassisInventoryBox = QGroupBox(self.DCStationInventoryBox)
        self.DCStationChassisInventoryBox.setObjectName(u"DCStationChassisInventoryBox")
        self.gridLayout_41 = QGridLayout(self.DCStationChassisInventoryBox)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.DCStationInventoryTotalChassisLabel = QLabel(self.DCStationChassisInventoryBox)
        self.DCStationInventoryTotalChassisLabel.setObjectName(u"DCStationInventoryTotalChassisLabel")

        self.gridLayout_41.addWidget(self.DCStationInventoryTotalChassisLabel, 0, 0, 1, 1)

        self.horizontalSpacer_188 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_41.addItem(self.horizontalSpacer_188, 0, 1, 1, 1)

        self.DCStationInventoryTotalChassis = QLCDNumber(self.DCStationChassisInventoryBox)
        self.DCStationInventoryTotalChassis.setObjectName(u"DCStationInventoryTotalChassis")
        self.DCStationInventoryTotalChassis.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_41.addWidget(self.DCStationInventoryTotalChassis, 0, 2, 1, 1)

        self.horizontalSpacer_182 = QSpacerItem(258, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_41.addItem(self.horizontalSpacer_182, 0, 3, 1, 1)

        self.DCStationChassisInventoryTable = QTableWidget(self.DCStationChassisInventoryBox)
        if (self.DCStationChassisInventoryTable.columnCount() < 3):
            self.DCStationChassisInventoryTable.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.DCStationChassisInventoryTable.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.DCStationChassisInventoryTable.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.DCStationChassisInventoryTable.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.DCStationChassisInventoryTable.setObjectName(u"DCStationChassisInventoryTable")
        self.DCStationChassisInventoryTable.setMinimumSize(QSize(491, 211))

        self.gridLayout_41.addWidget(self.DCStationChassisInventoryTable, 1, 0, 1, 4)


        self.gridLayout_42.addWidget(self.DCStationChassisInventoryBox, 1, 0, 1, 2)


        self.gridLayout_66.addWidget(self.DCStationInventoryBox, 0, 1, 1, 1)

        self.DCAssembly = QGroupBox(self.DriveChainAssembly)
        self.DCAssembly.setObjectName(u"DCAssembly")
        self.gridLayout_8 = QGridLayout(self.DCAssembly)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.DCAssemblyChassisValue = QLabel(self.DCAssembly)
        self.DCAssemblyChassisValue.setObjectName(u"DCAssemblyChassisValue")

        self.gridLayout_8.addWidget(self.DCAssemblyChassisValue, 0, 2, 1, 2)

        self.horizontalSpacer_183 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_183, 5, 1, 1, 1)

        self.horizontalSpacer_117 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_117, 1, 1, 1, 1)

        self.horizontalSpacer_116 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_116, 0, 1, 1, 1)

        self.DCAssembledButton = QPushButton(self.DCAssembly)
        self.DCAssembledButton.setObjectName(u"DCAssembledButton")

        self.gridLayout_8.addWidget(self.DCAssembledButton, 7, 0, 1, 4)

        self.horizontalSpacer_184 = QSpacerItem(47, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_184, 6, 1, 1, 2)

        self.DCAssemblyGearLabel = QLabel(self.DCAssembly)
        self.DCAssemblyGearLabel.setObjectName(u"DCAssemblyGearLabel")

        self.gridLayout_8.addWidget(self.DCAssemblyGearLabel, 6, 0, 1, 1)

        self.DCAssemblyChassisLabel = QLabel(self.DCAssembly)
        self.DCAssemblyChassisLabel.setObjectName(u"DCAssemblyChassisLabel")

        self.gridLayout_8.addWidget(self.DCAssemblyChassisLabel, 0, 0, 1, 1)

        self.DCAssemblyGearValue = QLabel(self.DCAssembly)
        self.DCAssemblyGearValue.setObjectName(u"DCAssemblyGearValue")

        self.gridLayout_8.addWidget(self.DCAssemblyGearValue, 6, 3, 1, 1)

        self.DCAssemblyColourLabel = QLabel(self.DCAssembly)
        self.DCAssemblyColourLabel.setObjectName(u"DCAssemblyColourLabel")

        self.gridLayout_8.addWidget(self.DCAssemblyColourLabel, 1, 0, 1, 1)

        self.DCAssemblyColourValue = QLabel(self.DCAssembly)
        self.DCAssemblyColourValue.setObjectName(u"DCAssemblyColourValue")

        self.gridLayout_8.addWidget(self.DCAssemblyColourValue, 1, 2, 1, 2)

        self.DCAssemblyChainValue = QLabel(self.DCAssembly)
        self.DCAssemblyChainValue.setObjectName(u"DCAssemblyChainValue")

        self.gridLayout_8.addWidget(self.DCAssemblyChainValue, 5, 2, 1, 2)

        self.DCAssemblyChainLabel = QLabel(self.DCAssembly)
        self.DCAssemblyChainLabel.setObjectName(u"DCAssemblyChainLabel")

        self.gridLayout_8.addWidget(self.DCAssemblyChainLabel, 5, 0, 1, 1)

        self.DCAssemblyPedalValue = QLabel(self.DCAssembly)
        self.DCAssemblyPedalValue.setObjectName(u"DCAssemblyPedalValue")

        self.gridLayout_8.addWidget(self.DCAssemblyPedalValue, 3, 3, 1, 1)

        self.horizontalSpacer_271 = QSpacerItem(77, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_271, 3, 1, 1, 1)

        self.DCAssemblyPedalLabel = QLabel(self.DCAssembly)
        self.DCAssemblyPedalLabel.setObjectName(u"DCAssemblyPedalLabel")

        self.gridLayout_8.addWidget(self.DCAssemblyPedalLabel, 3, 0, 1, 1)


        self.gridLayout_66.addWidget(self.DCAssembly, 0, 2, 1, 1)

        self.tabWidget.addTab(self.DriveChainAssembly, "")
        self.WheelAssembly = QWidget()
        self.WheelAssembly.setObjectName(u"WheelAssembly")
        self.gridLayout_67 = QGridLayout(self.WheelAssembly)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.WheelsOrder = QGroupBox(self.WheelAssembly)
        self.WheelsOrder.setObjectName(u"WheelsOrder")
        self.WheelsOrder.setMinimumSize(QSize(281, 385))
        self.gridLayout_28 = QGridLayout(self.WheelsOrder)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.Colour_6 = QLabel(self.WheelsOrder)
        self.Colour_6.setObjectName(u"Colour_6")

        self.gridLayout_28.addWidget(self.Colour_6, 4, 3, 1, 1)

        self.OrderNumber_6 = QLabel(self.WheelsOrder)
        self.OrderNumber_6.setObjectName(u"OrderNumber_6")

        self.gridLayout_28.addWidget(self.OrderNumber_6, 0, 2, 1, 2)

        self.horizontalSpacer_112 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_112, 8, 1, 1, 2)

        self.SeatType_6 = QLabel(self.WheelsOrder)
        self.SeatType_6.setObjectName(u"SeatType_6")

        self.gridLayout_28.addWidget(self.SeatType_6, 14, 3, 1, 1)

        self.line_7 = QFrame(self.WheelsOrder)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_28.addWidget(self.line_7, 2, 0, 1, 4)

        self.LightsType_6 = QLabel(self.WheelsOrder)
        self.LightsType_6.setObjectName(u"LightsType_6")

        self.gridLayout_28.addWidget(self.LightsType_6, 13, 3, 1, 1)

        self.horizontalSpacer_104 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_104, 0, 1, 1, 1)

        self.OrderNumberLabel_6 = QLabel(self.WheelsOrder)
        self.OrderNumberLabel_6.setObjectName(u"OrderNumberLabel_6")

        self.gridLayout_28.addWidget(self.OrderNumberLabel_6, 0, 0, 1, 1)

        self.BikeTypeLabel_6 = QLabel(self.WheelsOrder)
        self.BikeTypeLabel_6.setObjectName(u"BikeTypeLabel_6")

        self.gridLayout_28.addWidget(self.BikeTypeLabel_6, 1, 0, 1, 1)

        self.horizontalSpacer_105 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_105, 1, 1, 1, 1)

        self.horizontalSpacer_114 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_114, 13, 1, 1, 2)

        self.PedalType_6 = QLabel(self.WheelsOrder)
        self.PedalType_6.setObjectName(u"PedalType_6")

        self.gridLayout_28.addWidget(self.PedalType_6, 5, 3, 1, 1)

        self.PedalLabel_6 = QLabel(self.WheelsOrder)
        self.PedalLabel_6.setObjectName(u"PedalLabel_6")

        self.gridLayout_28.addWidget(self.PedalLabel_6, 5, 0, 1, 1)

        self.LightsLabel_6 = QLabel(self.WheelsOrder)
        self.LightsLabel_6.setObjectName(u"LightsLabel_6")

        self.gridLayout_28.addWidget(self.LightsLabel_6, 13, 0, 1, 1)

        self.ChainType_6 = QLabel(self.WheelsOrder)
        self.ChainType_6.setObjectName(u"ChainType_6")

        self.gridLayout_28.addWidget(self.ChainType_6, 7, 3, 1, 1)

        self.BikeType_6 = QLabel(self.WheelsOrder)
        self.BikeType_6.setObjectName(u"BikeType_6")

        self.gridLayout_28.addWidget(self.BikeType_6, 1, 2, 1, 2)

        self.horizontalSpacer_109 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_109, 5, 1, 1, 2)

        self.BrakesType_6 = QLabel(self.WheelsOrder)
        self.BrakesType_6.setObjectName(u"BrakesType_6")

        self.gridLayout_28.addWidget(self.BrakesType_6, 12, 3, 1, 1)

        self.ColourLabel_6 = QLabel(self.WheelsOrder)
        self.ColourLabel_6.setObjectName(u"ColourLabel_6")

        self.gridLayout_28.addWidget(self.ColourLabel_6, 4, 0, 1, 1)

        self.GearsLabel_6 = QLabel(self.WheelsOrder)
        self.GearsLabel_6.setObjectName(u"GearsLabel_6")

        self.gridLayout_28.addWidget(self.GearsLabel_6, 8, 0, 1, 1)

        self.ChainLabel_6 = QLabel(self.WheelsOrder)
        self.ChainLabel_6.setObjectName(u"ChainLabel_6")

        self.gridLayout_28.addWidget(self.ChainLabel_6, 7, 0, 1, 1)

        self.horizontalSpacer_108 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_108, 4, 1, 1, 2)

        self.horizontalSpacer_113 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_113, 12, 1, 1, 2)

        self.horizontalSpacer_107 = QSpacerItem(103, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_107, 3, 2, 1, 2)

        self.BrakesLabel_6 = QLabel(self.WheelsOrder)
        self.BrakesLabel_6.setObjectName(u"BrakesLabel_6")

        self.gridLayout_28.addWidget(self.BrakesLabel_6, 12, 0, 1, 1)

        self.SeatLabel_6 = QLabel(self.WheelsOrder)
        self.SeatLabel_6.setObjectName(u"SeatLabel_6")

        self.gridLayout_28.addWidget(self.SeatLabel_6, 14, 0, 1, 1)

        self.horizontalSpacer_106 = QSpacerItem(96, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_106, 3, 0, 1, 1)

        self.PartsLabel_6 = QLabel(self.WheelsOrder)
        self.PartsLabel_6.setObjectName(u"PartsLabel_6")
        self.PartsLabel_6.setScaledContents(False)
        self.PartsLabel_6.setWordWrap(False)

        self.gridLayout_28.addWidget(self.PartsLabel_6, 3, 1, 1, 1)

        self.GearType_6 = QLabel(self.WheelsOrder)
        self.GearType_6.setObjectName(u"GearType_6")

        self.gridLayout_28.addWidget(self.GearType_6, 8, 3, 1, 1)

        self.WheelType_6 = QLabel(self.WheelsOrder)
        self.WheelType_6.setObjectName(u"WheelType_6")

        self.gridLayout_28.addWidget(self.WheelType_6, 9, 3, 1, 1)

        self.WheelsLabel_6 = QLabel(self.WheelsOrder)
        self.WheelsLabel_6.setObjectName(u"WheelsLabel_6")

        self.gridLayout_28.addWidget(self.WheelsLabel_6, 9, 0, 1, 1)

        self.horizontalSpacer_110 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_110, 9, 1, 1, 2)

        self.horizontalSpacer_111 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_111, 7, 1, 1, 2)

        self.horizontalSpacer_115 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_115, 14, 1, 1, 2)


        self.gridLayout_67.addWidget(self.WheelsOrder, 0, 0, 1, 1)

        self.ChassisStationInventoryBox_5 = QGroupBox(self.WheelAssembly)
        self.ChassisStationInventoryBox_5.setObjectName(u"ChassisStationInventoryBox_5")
        self.gridLayout_43 = QGridLayout(self.ChassisStationInventoryBox_5)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.PedalStationChassisInventoryBox_8 = QGroupBox(self.ChassisStationInventoryBox_5)
        self.PedalStationChassisInventoryBox_8.setObjectName(u"PedalStationChassisInventoryBox_8")
        self.gridLayout_44 = QGridLayout(self.PedalStationChassisInventoryBox_8)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.PedalStationInventoryTotalKidsChassisLabel_11 = QLabel(self.PedalStationChassisInventoryBox_8)
        self.PedalStationInventoryTotalKidsChassisLabel_11.setObjectName(u"PedalStationInventoryTotalKidsChassisLabel_11")

        self.gridLayout_44.addWidget(self.PedalStationInventoryTotalKidsChassisLabel_11, 3, 0, 1, 1)

        self.PedalStationInventoryKidsChassis_10 = QLCDNumber(self.PedalStationChassisInventoryBox_8)
        self.PedalStationInventoryKidsChassis_10.setObjectName(u"PedalStationInventoryKidsChassis_10")
        self.PedalStationInventoryKidsChassis_10.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_44.addWidget(self.PedalStationInventoryKidsChassis_10, 3, 3, 1, 1)

        self.PedalStationInventoryTotalSportsChassisLabel_7 = QLabel(self.PedalStationChassisInventoryBox_8)
        self.PedalStationInventoryTotalSportsChassisLabel_7.setObjectName(u"PedalStationInventoryTotalSportsChassisLabel_7")

        self.gridLayout_44.addWidget(self.PedalStationInventoryTotalSportsChassisLabel_7, 2, 0, 1, 1)

        self.PedalStationInventorySportsChassis_7 = QLCDNumber(self.PedalStationChassisInventoryBox_8)
        self.PedalStationInventorySportsChassis_7.setObjectName(u"PedalStationInventorySportsChassis_7")
        self.PedalStationInventorySportsChassis_7.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_44.addWidget(self.PedalStationInventorySportsChassis_7, 2, 3, 1, 1)

        self.PedalStationInventoryTotalChassis_7 = QLCDNumber(self.PedalStationChassisInventoryBox_8)
        self.PedalStationInventoryTotalChassis_7.setObjectName(u"PedalStationInventoryTotalChassis_7")
        self.PedalStationInventoryTotalChassis_7.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_44.addWidget(self.PedalStationInventoryTotalChassis_7, 0, 3, 1, 1)

        self.PedalStationInventoryTotalChassisLabel_7 = QLabel(self.PedalStationChassisInventoryBox_8)
        self.PedalStationInventoryTotalChassisLabel_7.setObjectName(u"PedalStationInventoryTotalChassisLabel_7")

        self.gridLayout_44.addWidget(self.PedalStationInventoryTotalChassisLabel_7, 0, 0, 1, 1)

        self.PedalStationInventoryNormalChassis_7 = QLCDNumber(self.PedalStationChassisInventoryBox_8)
        self.PedalStationInventoryNormalChassis_7.setObjectName(u"PedalStationInventoryNormalChassis_7")
        self.PedalStationInventoryNormalChassis_7.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_44.addWidget(self.PedalStationInventoryNormalChassis_7, 1, 3, 1, 1)

        self.horizontalSpacer_215 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_44.addItem(self.horizontalSpacer_215, 1, 1, 1, 2)

        self.PedalStationInventoryKidsChassis_11 = QLCDNumber(self.PedalStationChassisInventoryBox_8)
        self.PedalStationInventoryKidsChassis_11.setObjectName(u"PedalStationInventoryKidsChassis_11")
        self.PedalStationInventoryKidsChassis_11.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_44.addWidget(self.PedalStationInventoryKidsChassis_11, 4, 3, 1, 1)

        self.horizontalSpacer_217 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_44.addItem(self.horizontalSpacer_217, 3, 1, 1, 2)

        self.PedalStationInventoryNormalChassisLabel_6 = QLabel(self.PedalStationChassisInventoryBox_8)
        self.PedalStationInventoryNormalChassisLabel_6.setObjectName(u"PedalStationInventoryNormalChassisLabel_6")

        self.gridLayout_44.addWidget(self.PedalStationInventoryNormalChassisLabel_6, 1, 0, 1, 1)

        self.horizontalSpacer_214 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_44.addItem(self.horizontalSpacer_214, 0, 1, 1, 2)

        self.horizontalSpacer_216 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_44.addItem(self.horizontalSpacer_216, 2, 1, 1, 2)

        self.horizontalSpacer_218 = QSpacerItem(30, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_44.addItem(self.horizontalSpacer_218, 4, 2, 1, 1)

        self.PedalStationInventoryTotalKidsChassisLabel_12 = QLabel(self.PedalStationChassisInventoryBox_8)
        self.PedalStationInventoryTotalKidsChassisLabel_12.setObjectName(u"PedalStationInventoryTotalKidsChassisLabel_12")

        self.gridLayout_44.addWidget(self.PedalStationInventoryTotalKidsChassisLabel_12, 4, 0, 1, 2)


        self.gridLayout_43.addWidget(self.PedalStationChassisInventoryBox_8, 0, 0, 1, 1)

        self.PedalStationChassisInventoryBox_10 = QGroupBox(self.ChassisStationInventoryBox_5)
        self.PedalStationChassisInventoryBox_10.setObjectName(u"PedalStationChassisInventoryBox_10")
        self.gridLayout_46 = QGridLayout(self.PedalStationChassisInventoryBox_10)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.PedalStationInventoryTotalChassisLabel_9 = QLabel(self.PedalStationChassisInventoryBox_10)
        self.PedalStationInventoryTotalChassisLabel_9.setObjectName(u"PedalStationInventoryTotalChassisLabel_9")

        self.gridLayout_46.addWidget(self.PedalStationInventoryTotalChassisLabel_9, 0, 0, 1, 1)

        self.horizontalSpacer_189 = QSpacerItem(62, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_46.addItem(self.horizontalSpacer_189, 0, 1, 1, 1)

        self.PedalStationInventoryTotalChassis_9 = QLCDNumber(self.PedalStationChassisInventoryBox_10)
        self.PedalStationInventoryTotalChassis_9.setObjectName(u"PedalStationInventoryTotalChassis_9")
        self.PedalStationInventoryTotalChassis_9.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_46.addWidget(self.PedalStationInventoryTotalChassis_9, 0, 2, 1, 1)

        self.horizontalSpacer_185 = QSpacerItem(258, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_46.addItem(self.horizontalSpacer_185, 0, 3, 1, 1)

        self.tableWidget_3 = QTableWidget(self.PedalStationChassisInventoryBox_10)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setMinimumSize(QSize(491, 211))

        self.gridLayout_46.addWidget(self.tableWidget_3, 1, 0, 1, 4)


        self.gridLayout_43.addWidget(self.PedalStationChassisInventoryBox_10, 1, 0, 1, 2)

        self.horizontalSpacer_186 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_43.addItem(self.horizontalSpacer_186, 0, 1, 1, 1)


        self.gridLayout_67.addWidget(self.ChassisStationInventoryBox_5, 0, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.WheelAssembly)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_7 = QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_93 = QLabel(self.groupBox_6)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout_7.addWidget(self.label_93, 5, 2, 1, 1)

        self.label_96 = QLabel(self.groupBox_6)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_7.addWidget(self.label_96, 7, 2, 1, 1)

        self.pushButton_15 = QPushButton(self.groupBox_6)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout_7.addWidget(self.pushButton_15, 8, 0, 1, 3)

        self.label_97 = QLabel(self.groupBox_6)
        self.label_97.setObjectName(u"label_97")

        self.gridLayout_7.addWidget(self.label_97, 7, 0, 1, 1)

        self.label_94 = QLabel(self.groupBox_6)
        self.label_94.setObjectName(u"label_94")

        self.gridLayout_7.addWidget(self.label_94, 6, 0, 1, 1)

        self.horizontalSpacer_222 = QSpacerItem(44, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_222, 7, 1, 1, 1)

        self.horizontalSpacer_190 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_190, 0, 1, 1, 1)

        self.label_89 = QLabel(self.groupBox_6)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_7.addWidget(self.label_89, 0, 2, 1, 1)

        self.horizontalSpacer_220 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_220, 5, 1, 1, 1)

        self.label_91 = QLabel(self.groupBox_6)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_7.addWidget(self.label_91, 1, 2, 1, 1)

        self.label_95 = QLabel(self.groupBox_6)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_7.addWidget(self.label_95, 6, 2, 1, 1)

        self.label_92 = QLabel(self.groupBox_6)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_7.addWidget(self.label_92, 5, 0, 1, 1)

        self.label_90 = QLabel(self.groupBox_6)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_7.addWidget(self.label_90, 1, 0, 1, 1)

        self.horizontalSpacer_221 = QSpacerItem(47, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_221, 6, 1, 1, 1)

        self.horizontalSpacer_219 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_219, 1, 1, 1, 1)

        self.label_88 = QLabel(self.groupBox_6)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_7.addWidget(self.label_88, 0, 0, 1, 1)

        self.horizontalSpacer_272 = QSpacerItem(77, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_272, 2, 1, 1, 1)

        self.label_42 = QLabel(self.groupBox_6)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_7.addWidget(self.label_42, 2, 2, 1, 1)

        self.label_107 = QLabel(self.groupBox_6)
        self.label_107.setObjectName(u"label_107")

        self.gridLayout_7.addWidget(self.label_107, 2, 0, 1, 1)


        self.gridLayout_67.addWidget(self.groupBox_6, 0, 2, 1, 1)

        self.tabWidget.addTab(self.WheelAssembly, "")
        self.BrakeAssembly = QWidget()
        self.BrakeAssembly.setObjectName(u"BrakeAssembly")
        self.gridLayout_68 = QGridLayout(self.BrakeAssembly)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.BrakesOrder = QGroupBox(self.BrakeAssembly)
        self.BrakesOrder.setObjectName(u"BrakesOrder")
        self.BrakesOrder.setMinimumSize(QSize(281, 385))
        self.gridLayout_30 = QGridLayout(self.BrakesOrder)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.horizontalSpacer_135 = QSpacerItem(103, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_135, 3, 2, 1, 2)

        self.horizontalSpacer_134 = QSpacerItem(96, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_134, 3, 0, 1, 1)

        self.BrakesLabel_8 = QLabel(self.BrakesOrder)
        self.BrakesLabel_8.setObjectName(u"BrakesLabel_8")

        self.gridLayout_30.addWidget(self.BrakesLabel_8, 10, 0, 1, 1)

        self.OrderNumberLabel_8 = QLabel(self.BrakesOrder)
        self.OrderNumberLabel_8.setObjectName(u"OrderNumberLabel_8")

        self.gridLayout_30.addWidget(self.OrderNumberLabel_8, 0, 0, 1, 1)

        self.PedalLabel_8 = QLabel(self.BrakesOrder)
        self.PedalLabel_8.setObjectName(u"PedalLabel_8")

        self.gridLayout_30.addWidget(self.PedalLabel_8, 5, 0, 1, 1)

        self.ColourLabel_8 = QLabel(self.BrakesOrder)
        self.ColourLabel_8.setObjectName(u"ColourLabel_8")

        self.gridLayout_30.addWidget(self.ColourLabel_8, 4, 0, 1, 1)

        self.PartsLabel_8 = QLabel(self.BrakesOrder)
        self.PartsLabel_8.setObjectName(u"PartsLabel_8")
        self.PartsLabel_8.setScaledContents(False)
        self.PartsLabel_8.setWordWrap(False)

        self.gridLayout_30.addWidget(self.PartsLabel_8, 3, 1, 1, 1)

        self.horizontalSpacer_142 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_142, 11, 1, 1, 2)

        self.horizontalSpacer_141 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_141, 10, 1, 1, 2)

        self.ChainType_8 = QLabel(self.BrakesOrder)
        self.ChainType_8.setObjectName(u"ChainType_8")

        self.gridLayout_30.addWidget(self.ChainType_8, 7, 3, 1, 1)

        self.Colour_8 = QLabel(self.BrakesOrder)
        self.Colour_8.setObjectName(u"Colour_8")

        self.gridLayout_30.addWidget(self.Colour_8, 4, 3, 1, 1)

        self.SeatType_8 = QLabel(self.BrakesOrder)
        self.SeatType_8.setObjectName(u"SeatType_8")

        self.gridLayout_30.addWidget(self.SeatType_8, 12, 3, 1, 1)

        self.horizontalSpacer_137 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_137, 5, 1, 1, 2)

        self.BikeType_8 = QLabel(self.BrakesOrder)
        self.BikeType_8.setObjectName(u"BikeType_8")

        self.gridLayout_30.addWidget(self.BikeType_8, 1, 2, 1, 2)

        self.GearType_8 = QLabel(self.BrakesOrder)
        self.GearType_8.setObjectName(u"GearType_8")

        self.gridLayout_30.addWidget(self.GearType_8, 8, 3, 1, 1)

        self.horizontalSpacer_140 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_140, 8, 1, 1, 2)

        self.horizontalSpacer_132 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_132, 0, 1, 1, 1)

        self.BikeTypeLabel_8 = QLabel(self.BrakesOrder)
        self.BikeTypeLabel_8.setObjectName(u"BikeTypeLabel_8")

        self.gridLayout_30.addWidget(self.BikeTypeLabel_8, 1, 0, 1, 1)

        self.GearsLabel_8 = QLabel(self.BrakesOrder)
        self.GearsLabel_8.setObjectName(u"GearsLabel_8")

        self.gridLayout_30.addWidget(self.GearsLabel_8, 8, 0, 1, 1)

        self.PedalType_8 = QLabel(self.BrakesOrder)
        self.PedalType_8.setObjectName(u"PedalType_8")

        self.gridLayout_30.addWidget(self.PedalType_8, 5, 3, 1, 1)

        self.OrderNumber_8 = QLabel(self.BrakesOrder)
        self.OrderNumber_8.setObjectName(u"OrderNumber_8")

        self.gridLayout_30.addWidget(self.OrderNumber_8, 0, 2, 1, 2)

        self.horizontalSpacer_136 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_136, 4, 1, 1, 2)

        self.BrakesType_8 = QLabel(self.BrakesOrder)
        self.BrakesType_8.setObjectName(u"BrakesType_8")

        self.gridLayout_30.addWidget(self.BrakesType_8, 10, 3, 1, 1)

        self.line_9 = QFrame(self.BrakesOrder)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_30.addWidget(self.line_9, 2, 0, 1, 4)

        self.SeatLabel_8 = QLabel(self.BrakesOrder)
        self.SeatLabel_8.setObjectName(u"SeatLabel_8")

        self.gridLayout_30.addWidget(self.SeatLabel_8, 12, 0, 1, 1)

        self.LightsType_8 = QLabel(self.BrakesOrder)
        self.LightsType_8.setObjectName(u"LightsType_8")

        self.gridLayout_30.addWidget(self.LightsType_8, 11, 3, 1, 1)

        self.LightsLabel_8 = QLabel(self.BrakesOrder)
        self.LightsLabel_8.setObjectName(u"LightsLabel_8")

        self.gridLayout_30.addWidget(self.LightsLabel_8, 11, 0, 1, 1)

        self.ChainLabel_8 = QLabel(self.BrakesOrder)
        self.ChainLabel_8.setObjectName(u"ChainLabel_8")

        self.gridLayout_30.addWidget(self.ChainLabel_8, 7, 0, 1, 1)

        self.horizontalSpacer_133 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_133, 1, 1, 1, 1)

        self.WheelsLabel_8 = QLabel(self.BrakesOrder)
        self.WheelsLabel_8.setObjectName(u"WheelsLabel_8")

        self.gridLayout_30.addWidget(self.WheelsLabel_8, 9, 0, 1, 1)

        self.WheelType_8 = QLabel(self.BrakesOrder)
        self.WheelType_8.setObjectName(u"WheelType_8")

        self.gridLayout_30.addWidget(self.WheelType_8, 9, 3, 1, 1)

        self.horizontalSpacer_138 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_138, 9, 1, 1, 2)

        self.horizontalSpacer_139 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_139, 7, 1, 1, 2)

        self.horizontalSpacer_143 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_143, 12, 1, 1, 2)


        self.gridLayout_68.addWidget(self.BrakesOrder, 0, 0, 1, 1)

        self.BrakeStationInventoryBox = QGroupBox(self.BrakeAssembly)
        self.BrakeStationInventoryBox.setObjectName(u"BrakeStationInventoryBox")
        self.gridLayout_45 = QGridLayout(self.BrakeStationInventoryBox)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.BrakeStationBrakeInventoryBox = QGroupBox(self.BrakeStationInventoryBox)
        self.BrakeStationBrakeInventoryBox.setObjectName(u"BrakeStationBrakeInventoryBox")
        self.gridLayout_47 = QGridLayout(self.BrakeStationBrakeInventoryBox)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.BrakeStationKidsBrakeLabel = QLabel(self.BrakeStationBrakeInventoryBox)
        self.BrakeStationKidsBrakeLabel.setObjectName(u"BrakeStationKidsBrakeLabel")

        self.gridLayout_47.addWidget(self.BrakeStationKidsBrakeLabel, 3, 0, 1, 1)

        self.BrakeStationKidsBrakeCounter = QLCDNumber(self.BrakeStationBrakeInventoryBox)
        self.BrakeStationKidsBrakeCounter.setObjectName(u"BrakeStationKidsBrakeCounter")
        self.BrakeStationKidsBrakeCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_47.addWidget(self.BrakeStationKidsBrakeCounter, 3, 3, 1, 1)

        self.BrakeStationSportBrakeLabel = QLabel(self.BrakeStationBrakeInventoryBox)
        self.BrakeStationSportBrakeLabel.setObjectName(u"BrakeStationSportBrakeLabel")

        self.gridLayout_47.addWidget(self.BrakeStationSportBrakeLabel, 2, 0, 1, 1)

        self.BrakeStationSportBrakeCounter = QLCDNumber(self.BrakeStationBrakeInventoryBox)
        self.BrakeStationSportBrakeCounter.setObjectName(u"BrakeStationSportBrakeCounter")
        self.BrakeStationSportBrakeCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_47.addWidget(self.BrakeStationSportBrakeCounter, 2, 3, 1, 1)

        self.BrakeStationTotalBrakeCounter = QLCDNumber(self.BrakeStationBrakeInventoryBox)
        self.BrakeStationTotalBrakeCounter.setObjectName(u"BrakeStationTotalBrakeCounter")
        self.BrakeStationTotalBrakeCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_47.addWidget(self.BrakeStationTotalBrakeCounter, 0, 3, 1, 1)

        self.BrakeStationTotalBrakeLabel = QLabel(self.BrakeStationBrakeInventoryBox)
        self.BrakeStationTotalBrakeLabel.setObjectName(u"BrakeStationTotalBrakeLabel")

        self.gridLayout_47.addWidget(self.BrakeStationTotalBrakeLabel, 0, 0, 1, 1)

        self.BrakeStationNormalBrakeCounter = QLCDNumber(self.BrakeStationBrakeInventoryBox)
        self.BrakeStationNormalBrakeCounter.setObjectName(u"BrakeStationNormalBrakeCounter")
        self.BrakeStationNormalBrakeCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_47.addWidget(self.BrakeStationNormalBrakeCounter, 1, 3, 1, 1)

        self.horizontalSpacer_223 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_47.addItem(self.horizontalSpacer_223, 1, 1, 1, 2)

        self.BrakeStationPremiumBrakeCounter = QLCDNumber(self.BrakeStationBrakeInventoryBox)
        self.BrakeStationPremiumBrakeCounter.setObjectName(u"BrakeStationPremiumBrakeCounter")
        self.BrakeStationPremiumBrakeCounter.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_47.addWidget(self.BrakeStationPremiumBrakeCounter, 4, 3, 1, 1)

        self.horizontalSpacer_224 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_47.addItem(self.horizontalSpacer_224, 3, 1, 1, 2)

        self.BrakeStationNormalBrakeLabel = QLabel(self.BrakeStationBrakeInventoryBox)
        self.BrakeStationNormalBrakeLabel.setObjectName(u"BrakeStationNormalBrakeLabel")

        self.gridLayout_47.addWidget(self.BrakeStationNormalBrakeLabel, 1, 0, 1, 1)

        self.horizontalSpacer_225 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_47.addItem(self.horizontalSpacer_225, 0, 1, 1, 2)

        self.horizontalSpacer_226 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_47.addItem(self.horizontalSpacer_226, 2, 1, 1, 2)

        self.horizontalSpacer_227 = QSpacerItem(30, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_47.addItem(self.horizontalSpacer_227, 4, 2, 1, 1)

        self.BrakeStationPremiumBrakeLabel = QLabel(self.BrakeStationBrakeInventoryBox)
        self.BrakeStationPremiumBrakeLabel.setObjectName(u"BrakeStationPremiumBrakeLabel")

        self.gridLayout_47.addWidget(self.BrakeStationPremiumBrakeLabel, 4, 0, 1, 2)


        self.gridLayout_45.addWidget(self.BrakeStationBrakeInventoryBox, 0, 0, 1, 1)

        self.BrakeStationChassisInventoryBox = QGroupBox(self.BrakeStationInventoryBox)
        self.BrakeStationChassisInventoryBox.setObjectName(u"BrakeStationChassisInventoryBox")
        self.gridLayout_48 = QGridLayout(self.BrakeStationChassisInventoryBox)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.BrakeStationInventoryTotalChassisLabel = QLabel(self.BrakeStationChassisInventoryBox)
        self.BrakeStationInventoryTotalChassisLabel.setObjectName(u"BrakeStationInventoryTotalChassisLabel")

        self.gridLayout_48.addWidget(self.BrakeStationInventoryTotalChassisLabel, 0, 0, 1, 1)

        self.horizontalSpacer_228 = QSpacerItem(62, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_48.addItem(self.horizontalSpacer_228, 0, 1, 1, 1)

        self.BrakeStationInventoryTotalChassis = QLCDNumber(self.BrakeStationChassisInventoryBox)
        self.BrakeStationInventoryTotalChassis.setObjectName(u"BrakeStationInventoryTotalChassis")
        self.BrakeStationInventoryTotalChassis.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_48.addWidget(self.BrakeStationInventoryTotalChassis, 0, 2, 1, 1)

        self.horizontalSpacer_229 = QSpacerItem(258, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_48.addItem(self.horizontalSpacer_229, 0, 3, 1, 1)

        self.BrakeStationChassisInventoryTable = QTableWidget(self.BrakeStationChassisInventoryBox)
        if (self.BrakeStationChassisInventoryTable.columnCount() < 6):
            self.BrakeStationChassisInventoryTable.setColumnCount(6)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.BrakeStationChassisInventoryTable.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.BrakeStationChassisInventoryTable.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.BrakeStationChassisInventoryTable.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.BrakeStationChassisInventoryTable.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.BrakeStationChassisInventoryTable.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.BrakeStationChassisInventoryTable.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        self.BrakeStationChassisInventoryTable.setObjectName(u"BrakeStationChassisInventoryTable")
        self.BrakeStationChassisInventoryTable.setMinimumSize(QSize(491, 211))

        self.gridLayout_48.addWidget(self.BrakeStationChassisInventoryTable, 1, 0, 1, 4)


        self.gridLayout_45.addWidget(self.BrakeStationChassisInventoryBox, 1, 0, 1, 2)

        self.horizontalSpacer_230 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_45.addItem(self.horizontalSpacer_230, 0, 1, 1, 1)


        self.gridLayout_68.addWidget(self.BrakeStationInventoryBox, 0, 1, 1, 1)

        self.BrakeAssemblyBox = QGroupBox(self.BrakeAssembly)
        self.BrakeAssemblyBox.setObjectName(u"BrakeAssemblyBox")
        self.gridLayout_9 = QGridLayout(self.BrakeAssemblyBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.BrakeAssemblyGearValue = QLabel(self.BrakeAssemblyBox)
        self.BrakeAssemblyGearValue.setObjectName(u"BrakeAssemblyGearValue")

        self.gridLayout_9.addWidget(self.BrakeAssemblyGearValue, 6, 2, 1, 1)

        self.BrakeAssemblyWheelValue = QLabel(self.BrakeAssemblyBox)
        self.BrakeAssemblyWheelValue.setObjectName(u"BrakeAssemblyWheelValue")

        self.gridLayout_9.addWidget(self.BrakeAssemblyWheelValue, 7, 2, 1, 1)

        self.BrakeAssemblyChainLabel = QLabel(self.BrakeAssemblyBox)
        self.BrakeAssemblyChainLabel.setObjectName(u"BrakeAssemblyChainLabel")

        self.gridLayout_9.addWidget(self.BrakeAssemblyChainLabel, 5, 0, 1, 1)

        self.BrakeAssemblyBrakeLabel = QLabel(self.BrakeAssemblyBox)
        self.BrakeAssemblyBrakeLabel.setObjectName(u"BrakeAssemblyBrakeLabel")

        self.gridLayout_9.addWidget(self.BrakeAssemblyBrakeLabel, 8, 0, 1, 1)

        self.BrakeAssemblyColourLabel = QLabel(self.BrakeAssemblyBox)
        self.BrakeAssemblyColourLabel.setObjectName(u"BrakeAssemblyColourLabel")

        self.gridLayout_9.addWidget(self.BrakeAssemblyColourLabel, 1, 0, 1, 1)

        self.horizontalSpacer_232 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_232, 1, 1, 1, 1)

        self.BrakeAssemblyGearLabel = QLabel(self.BrakeAssemblyBox)
        self.BrakeAssemblyGearLabel.setObjectName(u"BrakeAssemblyGearLabel")

        self.gridLayout_9.addWidget(self.BrakeAssemblyGearLabel, 6, 0, 1, 1)

        self.BrakeAssemblyBrakeValue = QLabel(self.BrakeAssemblyBox)
        self.BrakeAssemblyBrakeValue.setObjectName(u"BrakeAssemblyBrakeValue")

        self.gridLayout_9.addWidget(self.BrakeAssemblyBrakeValue, 8, 2, 1, 1)

        self.horizontalSpacer_234 = QSpacerItem(47, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_234, 6, 1, 1, 1)

        self.horizontalSpacer_235 = QSpacerItem(44, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_235, 7, 1, 1, 1)

        self.horizontalSpacer_231 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_231, 0, 1, 1, 1)

        self.horizontalSpacer_236 = QSpacerItem(44, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_236, 8, 1, 1, 1)

        self.BrakeAssemblyChassisLabel = QLabel(self.BrakeAssemblyBox)
        self.BrakeAssemblyChassisLabel.setObjectName(u"BrakeAssemblyChassisLabel")

        self.gridLayout_9.addWidget(self.BrakeAssemblyChassisLabel, 0, 0, 1, 1)

        self.BrakeAssemblyAssembledButton = QPushButton(self.BrakeAssemblyBox)
        self.BrakeAssemblyAssembledButton.setObjectName(u"BrakeAssemblyAssembledButton")

        self.gridLayout_9.addWidget(self.BrakeAssemblyAssembledButton, 9, 0, 1, 3)

        self.BrakeAssemblyWheelLabel = QLabel(self.BrakeAssemblyBox)
        self.BrakeAssemblyWheelLabel.setObjectName(u"BrakeAssemblyWheelLabel")

        self.gridLayout_9.addWidget(self.BrakeAssemblyWheelLabel, 7, 0, 1, 1)

        self.horizontalSpacer_233 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_233, 5, 1, 1, 1)

        self.BrakeAssemblyChassisType = QLabel(self.BrakeAssemblyBox)
        self.BrakeAssemblyChassisType.setObjectName(u"BrakeAssemblyChassisType")

        self.gridLayout_9.addWidget(self.BrakeAssemblyChassisType, 0, 2, 1, 1)

        self.BrakeAssemblyChainValue = QLabel(self.BrakeAssemblyBox)
        self.BrakeAssemblyChainValue.setObjectName(u"BrakeAssemblyChainValue")

        self.gridLayout_9.addWidget(self.BrakeAssemblyChainValue, 5, 2, 1, 1)

        self.BrakeAssemblyColourValue = QLabel(self.BrakeAssemblyBox)
        self.BrakeAssemblyColourValue.setObjectName(u"BrakeAssemblyColourValue")

        self.gridLayout_9.addWidget(self.BrakeAssemblyColourValue, 1, 2, 1, 1)

        self.horizontalSpacer_273 = QSpacerItem(77, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_273, 2, 1, 1, 1)

        self.BrakeAssemblyPedalValue = QLabel(self.BrakeAssemblyBox)
        self.BrakeAssemblyPedalValue.setObjectName(u"BrakeAssemblyPedalValue")

        self.gridLayout_9.addWidget(self.BrakeAssemblyPedalValue, 2, 2, 1, 1)

        self.BrakeAssemblyPedalLabel = QLabel(self.BrakeAssemblyBox)
        self.BrakeAssemblyPedalLabel.setObjectName(u"BrakeAssemblyPedalLabel")

        self.gridLayout_9.addWidget(self.BrakeAssemblyPedalLabel, 2, 0, 1, 1)


        self.gridLayout_68.addWidget(self.BrakeAssemblyBox, 0, 2, 1, 1)

        self.tabWidget.addTab(self.BrakeAssembly, "")
        self.lightAssembly = QWidget()
        self.lightAssembly.setObjectName(u"lightAssembly")
        self.gridLayout_69 = QGridLayout(self.lightAssembly)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.LightsOrder = QGroupBox(self.lightAssembly)
        self.LightsOrder.setObjectName(u"LightsOrder")
        self.LightsOrder.setMinimumSize(QSize(281, 385))
        self.gridLayout_31 = QGridLayout(self.LightsOrder)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.BikeTypeLabel_9 = QLabel(self.LightsOrder)
        self.BikeTypeLabel_9.setObjectName(u"BikeTypeLabel_9")

        self.gridLayout_31.addWidget(self.BikeTypeLabel_9, 1, 0, 1, 1)

        self.horizontalSpacer_150 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_150, 4, 1, 1, 2)

        self.PartsLabel_9 = QLabel(self.LightsOrder)
        self.PartsLabel_9.setObjectName(u"PartsLabel_9")
        self.PartsLabel_9.setScaledContents(False)
        self.PartsLabel_9.setWordWrap(False)

        self.gridLayout_31.addWidget(self.PartsLabel_9, 3, 1, 1, 1)

        self.BrakesType_9 = QLabel(self.LightsOrder)
        self.BrakesType_9.setObjectName(u"BrakesType_9")

        self.gridLayout_31.addWidget(self.BrakesType_9, 10, 3, 1, 1)

        self.GearType_9 = QLabel(self.LightsOrder)
        self.GearType_9.setObjectName(u"GearType_9")

        self.gridLayout_31.addWidget(self.GearType_9, 8, 3, 1, 1)

        self.ColourLabel_9 = QLabel(self.LightsOrder)
        self.ColourLabel_9.setObjectName(u"ColourLabel_9")

        self.gridLayout_31.addWidget(self.ColourLabel_9, 4, 0, 1, 1)

        self.OrderNumberLabel_9 = QLabel(self.LightsOrder)
        self.OrderNumberLabel_9.setObjectName(u"OrderNumberLabel_9")

        self.gridLayout_31.addWidget(self.OrderNumberLabel_9, 0, 0, 1, 1)

        self.horizontalSpacer_154 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_154, 8, 1, 1, 2)

        self.GearsLabel_9 = QLabel(self.LightsOrder)
        self.GearsLabel_9.setObjectName(u"GearsLabel_9")

        self.gridLayout_31.addWidget(self.GearsLabel_9, 8, 0, 1, 1)

        self.Colour_9 = QLabel(self.LightsOrder)
        self.Colour_9.setObjectName(u"Colour_9")

        self.gridLayout_31.addWidget(self.Colour_9, 4, 3, 1, 1)

        self.BrakesLabel_9 = QLabel(self.LightsOrder)
        self.BrakesLabel_9.setObjectName(u"BrakesLabel_9")

        self.gridLayout_31.addWidget(self.BrakesLabel_9, 10, 0, 1, 1)

        self.PedalType_9 = QLabel(self.LightsOrder)
        self.PedalType_9.setObjectName(u"PedalType_9")

        self.gridLayout_31.addWidget(self.PedalType_9, 5, 3, 1, 1)

        self.PedalLabel_9 = QLabel(self.LightsOrder)
        self.PedalLabel_9.setObjectName(u"PedalLabel_9")

        self.gridLayout_31.addWidget(self.PedalLabel_9, 5, 0, 1, 1)

        self.line_10 = QFrame(self.LightsOrder)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_31.addWidget(self.line_10, 2, 0, 1, 4)

        self.ChainType_9 = QLabel(self.LightsOrder)
        self.ChainType_9.setObjectName(u"ChainType_9")

        self.gridLayout_31.addWidget(self.ChainType_9, 7, 3, 1, 1)

        self.horizontalSpacer_149 = QSpacerItem(103, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_149, 3, 2, 1, 2)

        self.SeatLabel_9 = QLabel(self.LightsOrder)
        self.SeatLabel_9.setObjectName(u"SeatLabel_9")

        self.gridLayout_31.addWidget(self.SeatLabel_9, 12, 0, 1, 1)

        self.horizontalSpacer_146 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_146, 0, 1, 1, 1)

        self.horizontalSpacer_148 = QSpacerItem(96, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_148, 3, 0, 1, 1)

        self.LightsLabel_9 = QLabel(self.LightsOrder)
        self.LightsLabel_9.setObjectName(u"LightsLabel_9")

        self.gridLayout_31.addWidget(self.LightsLabel_9, 11, 0, 1, 1)

        self.LightsType_9 = QLabel(self.LightsOrder)
        self.LightsType_9.setObjectName(u"LightsType_9")

        self.gridLayout_31.addWidget(self.LightsType_9, 11, 3, 1, 1)

        self.horizontalSpacer_155 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_155, 10, 1, 1, 2)

        self.BikeType_9 = QLabel(self.LightsOrder)
        self.BikeType_9.setObjectName(u"BikeType_9")

        self.gridLayout_31.addWidget(self.BikeType_9, 1, 2, 1, 2)

        self.ChainLabel_9 = QLabel(self.LightsOrder)
        self.ChainLabel_9.setObjectName(u"ChainLabel_9")

        self.gridLayout_31.addWidget(self.ChainLabel_9, 7, 0, 1, 1)

        self.SeatType_9 = QLabel(self.LightsOrder)
        self.SeatType_9.setObjectName(u"SeatType_9")

        self.gridLayout_31.addWidget(self.SeatType_9, 12, 3, 1, 1)

        self.horizontalSpacer_151 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_151, 5, 1, 1, 2)

        self.horizontalSpacer_147 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_147, 1, 1, 1, 1)

        self.horizontalSpacer_156 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_156, 11, 1, 1, 2)

        self.OrderNumber_9 = QLabel(self.LightsOrder)
        self.OrderNumber_9.setObjectName(u"OrderNumber_9")

        self.gridLayout_31.addWidget(self.OrderNumber_9, 0, 2, 1, 2)

        self.WheelsLabel_9 = QLabel(self.LightsOrder)
        self.WheelsLabel_9.setObjectName(u"WheelsLabel_9")

        self.gridLayout_31.addWidget(self.WheelsLabel_9, 9, 0, 1, 1)

        self.WheelType_9 = QLabel(self.LightsOrder)
        self.WheelType_9.setObjectName(u"WheelType_9")

        self.gridLayout_31.addWidget(self.WheelType_9, 9, 3, 1, 1)

        self.horizontalSpacer_152 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_152, 9, 1, 1, 2)

        self.horizontalSpacer_153 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_153, 7, 1, 1, 2)

        self.horizontalSpacer_157 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_157, 12, 1, 1, 2)


        self.gridLayout_69.addWidget(self.LightsOrder, 0, 0, 1, 1)

        self.ChassisStationInventoryBox_7 = QGroupBox(self.lightAssembly)
        self.ChassisStationInventoryBox_7.setObjectName(u"ChassisStationInventoryBox_7")
        self.gridLayout_49 = QGridLayout(self.ChassisStationInventoryBox_7)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.PedalStationChassisInventoryBox_12 = QGroupBox(self.ChassisStationInventoryBox_7)
        self.PedalStationChassisInventoryBox_12.setObjectName(u"PedalStationChassisInventoryBox_12")
        self.gridLayout_50 = QGridLayout(self.PedalStationChassisInventoryBox_12)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.horizontalSpacer_237 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_50.addItem(self.horizontalSpacer_237, 1, 1, 1, 2)

        self.horizontalSpacer_241 = QSpacerItem(30, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_50.addItem(self.horizontalSpacer_241, 2, 2, 1, 1)

        self.horizontalSpacer_239 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_50.addItem(self.horizontalSpacer_239, 0, 1, 1, 2)

        self.PedalStationInventoryNormalChassis_9 = QLCDNumber(self.PedalStationChassisInventoryBox_12)
        self.PedalStationInventoryNormalChassis_9.setObjectName(u"PedalStationInventoryNormalChassis_9")
        self.PedalStationInventoryNormalChassis_9.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_50.addWidget(self.PedalStationInventoryNormalChassis_9, 1, 3, 1, 1)

        self.PedalStationInventoryTotalChassisLabel_11 = QLabel(self.PedalStationChassisInventoryBox_12)
        self.PedalStationInventoryTotalChassisLabel_11.setObjectName(u"PedalStationInventoryTotalChassisLabel_11")

        self.gridLayout_50.addWidget(self.PedalStationInventoryTotalChassisLabel_11, 0, 0, 1, 1)

        self.PedalStationInventoryKidsChassis_15 = QLCDNumber(self.PedalStationChassisInventoryBox_12)
        self.PedalStationInventoryKidsChassis_15.setObjectName(u"PedalStationInventoryKidsChassis_15")
        self.PedalStationInventoryKidsChassis_15.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_50.addWidget(self.PedalStationInventoryKidsChassis_15, 2, 3, 1, 1)

        self.PedalStationInventoryNormalChassisLabel_8 = QLabel(self.PedalStationChassisInventoryBox_12)
        self.PedalStationInventoryNormalChassisLabel_8.setObjectName(u"PedalStationInventoryNormalChassisLabel_8")

        self.gridLayout_50.addWidget(self.PedalStationInventoryNormalChassisLabel_8, 1, 0, 1, 1)

        self.PedalStationInventoryTotalKidsChassisLabel_16 = QLabel(self.PedalStationChassisInventoryBox_12)
        self.PedalStationInventoryTotalKidsChassisLabel_16.setObjectName(u"PedalStationInventoryTotalKidsChassisLabel_16")

        self.gridLayout_50.addWidget(self.PedalStationInventoryTotalKidsChassisLabel_16, 2, 0, 1, 2)

        self.PedalStationInventoryTotalChassis_11 = QLCDNumber(self.PedalStationChassisInventoryBox_12)
        self.PedalStationInventoryTotalChassis_11.setObjectName(u"PedalStationInventoryTotalChassis_11")
        self.PedalStationInventoryTotalChassis_11.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_50.addWidget(self.PedalStationInventoryTotalChassis_11, 0, 3, 1, 1)


        self.gridLayout_49.addWidget(self.PedalStationChassisInventoryBox_12, 0, 0, 1, 1)

        self.PedalStationChassisInventoryBox_13 = QGroupBox(self.ChassisStationInventoryBox_7)
        self.PedalStationChassisInventoryBox_13.setObjectName(u"PedalStationChassisInventoryBox_13")
        self.gridLayout_51 = QGridLayout(self.PedalStationChassisInventoryBox_13)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.PedalStationInventoryTotalChassisLabel_12 = QLabel(self.PedalStationChassisInventoryBox_13)
        self.PedalStationInventoryTotalChassisLabel_12.setObjectName(u"PedalStationInventoryTotalChassisLabel_12")

        self.gridLayout_51.addWidget(self.PedalStationInventoryTotalChassisLabel_12, 0, 0, 1, 1)

        self.horizontalSpacer_242 = QSpacerItem(62, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_51.addItem(self.horizontalSpacer_242, 0, 1, 1, 1)

        self.PedalStationInventoryTotalChassis_12 = QLCDNumber(self.PedalStationChassisInventoryBox_13)
        self.PedalStationInventoryTotalChassis_12.setObjectName(u"PedalStationInventoryTotalChassis_12")
        self.PedalStationInventoryTotalChassis_12.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_51.addWidget(self.PedalStationInventoryTotalChassis_12, 0, 2, 1, 1)

        self.horizontalSpacer_243 = QSpacerItem(258, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_51.addItem(self.horizontalSpacer_243, 0, 3, 1, 1)

        self.tableWidget_5 = QTableWidget(self.PedalStationChassisInventoryBox_13)
        if (self.tableWidget_5.columnCount() < 7):
            self.tableWidget_5.setColumnCount(7)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, __qtablewidgetitem22)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setMinimumSize(QSize(491, 211))

        self.gridLayout_51.addWidget(self.tableWidget_5, 1, 0, 1, 4)


        self.gridLayout_49.addWidget(self.PedalStationChassisInventoryBox_13, 1, 0, 1, 2)

        self.horizontalSpacer_244 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_49.addItem(self.horizontalSpacer_244, 0, 1, 1, 1)


        self.gridLayout_69.addWidget(self.ChassisStationInventoryBox_7, 0, 1, 1, 1)

        self.groupBox_8 = QGroupBox(self.lightAssembly)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_10 = QGridLayout(self.groupBox_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_219 = QLabel(self.groupBox_8)
        self.label_219.setObjectName(u"label_219")

        self.gridLayout_10.addWidget(self.label_219, 8, 0, 1, 1)

        self.horizontalSpacer_251 = QSpacerItem(44, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_251, 9, 1, 1, 1)

        self.label_222 = QLabel(self.groupBox_8)
        self.label_222.setObjectName(u"label_222")

        self.gridLayout_10.addWidget(self.label_222, 9, 2, 1, 1)

        self.horizontalSpacer_246 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_246, 1, 1, 1, 1)

        self.label_213 = QLabel(self.groupBox_8)
        self.label_213.setObjectName(u"label_213")

        self.gridLayout_10.addWidget(self.label_213, 5, 0, 1, 1)

        self.label_210 = QLabel(self.groupBox_8)
        self.label_210.setObjectName(u"label_210")

        self.gridLayout_10.addWidget(self.label_210, 0, 2, 1, 1)

        self.horizontalSpacer_250 = QSpacerItem(44, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_250, 8, 1, 1, 1)

        self.label_214 = QLabel(self.groupBox_8)
        self.label_214.setObjectName(u"label_214")

        self.gridLayout_10.addWidget(self.label_214, 5, 2, 1, 1)

        self.label_212 = QLabel(self.groupBox_8)
        self.label_212.setObjectName(u"label_212")

        self.gridLayout_10.addWidget(self.label_212, 1, 2, 1, 1)

        self.label_216 = QLabel(self.groupBox_8)
        self.label_216.setObjectName(u"label_216")

        self.gridLayout_10.addWidget(self.label_216, 6, 2, 1, 1)

        self.label_218 = QLabel(self.groupBox_8)
        self.label_218.setObjectName(u"label_218")

        self.gridLayout_10.addWidget(self.label_218, 7, 2, 1, 1)

        self.horizontalSpacer_245 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_245, 0, 1, 1, 1)

        self.pushButton_17 = QPushButton(self.groupBox_8)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout_10.addWidget(self.pushButton_17, 10, 0, 1, 3)

        self.label_211 = QLabel(self.groupBox_8)
        self.label_211.setObjectName(u"label_211")

        self.gridLayout_10.addWidget(self.label_211, 1, 0, 1, 1)

        self.label_215 = QLabel(self.groupBox_8)
        self.label_215.setObjectName(u"label_215")

        self.gridLayout_10.addWidget(self.label_215, 6, 0, 1, 1)

        self.horizontalSpacer_249 = QSpacerItem(44, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_249, 7, 1, 1, 1)

        self.horizontalSpacer_248 = QSpacerItem(47, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_248, 6, 1, 1, 1)

        self.label_217 = QLabel(self.groupBox_8)
        self.label_217.setObjectName(u"label_217")

        self.gridLayout_10.addWidget(self.label_217, 7, 0, 1, 1)

        self.label_221 = QLabel(self.groupBox_8)
        self.label_221.setObjectName(u"label_221")

        self.gridLayout_10.addWidget(self.label_221, 9, 0, 1, 1)

        self.horizontalSpacer_247 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_247, 5, 1, 1, 1)

        self.label_209 = QLabel(self.groupBox_8)
        self.label_209.setObjectName(u"label_209")

        self.gridLayout_10.addWidget(self.label_209, 0, 0, 1, 1)

        self.label_220 = QLabel(self.groupBox_8)
        self.label_220.setObjectName(u"label_220")

        self.gridLayout_10.addWidget(self.label_220, 8, 2, 1, 1)

        self.horizontalSpacer_274 = QSpacerItem(77, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_274, 2, 1, 1, 1)

        self.label_44 = QLabel(self.groupBox_8)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_10.addWidget(self.label_44, 2, 2, 1, 1)

        self.label_109 = QLabel(self.groupBox_8)
        self.label_109.setObjectName(u"label_109")

        self.gridLayout_10.addWidget(self.label_109, 2, 0, 1, 1)


        self.gridLayout_69.addWidget(self.groupBox_8, 0, 2, 1, 1)

        self.tabWidget.addTab(self.lightAssembly, "")
        self.SeatAssembly = QWidget()
        self.SeatAssembly.setObjectName(u"SeatAssembly")
        self.gridLayout_70 = QGridLayout(self.SeatAssembly)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.SeatsOrder = QGroupBox(self.SeatAssembly)
        self.SeatsOrder.setObjectName(u"SeatsOrder")
        self.SeatsOrder.setMinimumSize(QSize(281, 385))
        self.gridLayout_32 = QGridLayout(self.SeatsOrder)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.PedalType_10 = QLabel(self.SeatsOrder)
        self.PedalType_10.setObjectName(u"PedalType_10")

        self.gridLayout_32.addWidget(self.PedalType_10, 5, 3, 1, 1)

        self.horizontalSpacer_164 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_164, 4, 1, 1, 2)

        self.SeatLabel_10 = QLabel(self.SeatsOrder)
        self.SeatLabel_10.setObjectName(u"SeatLabel_10")

        self.gridLayout_32.addWidget(self.SeatLabel_10, 14, 0, 1, 1)

        self.BikeTypeLabel_10 = QLabel(self.SeatsOrder)
        self.BikeTypeLabel_10.setObjectName(u"BikeTypeLabel_10")

        self.gridLayout_32.addWidget(self.BikeTypeLabel_10, 1, 0, 1, 1)

        self.LightsLabel_10 = QLabel(self.SeatsOrder)
        self.LightsLabel_10.setObjectName(u"LightsLabel_10")

        self.gridLayout_32.addWidget(self.LightsLabel_10, 13, 0, 1, 1)

        self.horizontalSpacer_160 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_160, 0, 1, 1, 1)

        self.Colour_10 = QLabel(self.SeatsOrder)
        self.Colour_10.setObjectName(u"Colour_10")

        self.gridLayout_32.addWidget(self.Colour_10, 4, 3, 1, 1)

        self.PedalLabel_10 = QLabel(self.SeatsOrder)
        self.PedalLabel_10.setObjectName(u"PedalLabel_10")

        self.gridLayout_32.addWidget(self.PedalLabel_10, 5, 0, 1, 1)

        self.horizontalSpacer_168 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_168, 8, 1, 1, 2)

        self.horizontalSpacer_170 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_170, 13, 1, 1, 2)

        self.GearType_10 = QLabel(self.SeatsOrder)
        self.GearType_10.setObjectName(u"GearType_10")

        self.gridLayout_32.addWidget(self.GearType_10, 8, 3, 1, 1)

        self.LightsType_10 = QLabel(self.SeatsOrder)
        self.LightsType_10.setObjectName(u"LightsType_10")

        self.gridLayout_32.addWidget(self.LightsType_10, 13, 3, 1, 1)

        self.ChainType_10 = QLabel(self.SeatsOrder)
        self.ChainType_10.setObjectName(u"ChainType_10")

        self.gridLayout_32.addWidget(self.ChainType_10, 7, 3, 1, 1)

        self.horizontalSpacer_169 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_169, 12, 1, 1, 2)

        self.ChainLabel_10 = QLabel(self.SeatsOrder)
        self.ChainLabel_10.setObjectName(u"ChainLabel_10")

        self.gridLayout_32.addWidget(self.ChainLabel_10, 7, 0, 1, 1)

        self.BrakesType_10 = QLabel(self.SeatsOrder)
        self.BrakesType_10.setObjectName(u"BrakesType_10")

        self.gridLayout_32.addWidget(self.BrakesType_10, 12, 3, 1, 1)

        self.horizontalSpacer_165 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_165, 5, 1, 1, 2)

        self.BrakesLabel_10 = QLabel(self.SeatsOrder)
        self.BrakesLabel_10.setObjectName(u"BrakesLabel_10")

        self.gridLayout_32.addWidget(self.BrakesLabel_10, 12, 0, 1, 1)

        self.horizontalSpacer_162 = QSpacerItem(96, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_162, 3, 0, 1, 1)

        self.PartsLabel_10 = QLabel(self.SeatsOrder)
        self.PartsLabel_10.setObjectName(u"PartsLabel_10")
        self.PartsLabel_10.setScaledContents(False)
        self.PartsLabel_10.setWordWrap(False)

        self.gridLayout_32.addWidget(self.PartsLabel_10, 3, 1, 1, 1)

        self.BikeType_10 = QLabel(self.SeatsOrder)
        self.BikeType_10.setObjectName(u"BikeType_10")

        self.gridLayout_32.addWidget(self.BikeType_10, 1, 2, 1, 2)

        self.GearsLabel_10 = QLabel(self.SeatsOrder)
        self.GearsLabel_10.setObjectName(u"GearsLabel_10")

        self.gridLayout_32.addWidget(self.GearsLabel_10, 8, 0, 1, 1)

        self.OrderNumber_10 = QLabel(self.SeatsOrder)
        self.OrderNumber_10.setObjectName(u"OrderNumber_10")

        self.gridLayout_32.addWidget(self.OrderNumber_10, 0, 2, 1, 2)

        self.horizontalSpacer_163 = QSpacerItem(103, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_163, 3, 2, 1, 2)

        self.SeatType_10 = QLabel(self.SeatsOrder)
        self.SeatType_10.setObjectName(u"SeatType_10")

        self.gridLayout_32.addWidget(self.SeatType_10, 14, 3, 1, 1)

        self.ColourLabel_10 = QLabel(self.SeatsOrder)
        self.ColourLabel_10.setObjectName(u"ColourLabel_10")

        self.gridLayout_32.addWidget(self.ColourLabel_10, 4, 0, 1, 1)

        self.line_11 = QFrame(self.SeatsOrder)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_32.addWidget(self.line_11, 2, 0, 1, 4)

        self.OrderNumberLabel_10 = QLabel(self.SeatsOrder)
        self.OrderNumberLabel_10.setObjectName(u"OrderNumberLabel_10")

        self.gridLayout_32.addWidget(self.OrderNumberLabel_10, 0, 0, 1, 1)

        self.horizontalSpacer_161 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_161, 1, 1, 1, 1)

        self.horizontalSpacer_166 = QSpacerItem(61, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_166, 9, 1, 1, 2)

        self.WheelsLabel_10 = QLabel(self.SeatsOrder)
        self.WheelsLabel_10.setObjectName(u"WheelsLabel_10")

        self.gridLayout_32.addWidget(self.WheelsLabel_10, 9, 0, 1, 1)

        self.WheelType_10 = QLabel(self.SeatsOrder)
        self.WheelType_10.setObjectName(u"WheelType_10")

        self.gridLayout_32.addWidget(self.WheelType_10, 9, 3, 1, 1)

        self.horizontalSpacer_171 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_171, 14, 1, 1, 2)

        self.horizontalSpacer_167 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_167, 7, 1, 1, 2)


        self.gridLayout_70.addWidget(self.SeatsOrder, 0, 0, 1, 1)

        self.ChassisStationInventoryBox_8 = QGroupBox(self.SeatAssembly)
        self.ChassisStationInventoryBox_8.setObjectName(u"ChassisStationInventoryBox_8")
        self.gridLayout_52 = QGridLayout(self.ChassisStationInventoryBox_8)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.PedalStationChassisInventoryBox_14 = QGroupBox(self.ChassisStationInventoryBox_8)
        self.PedalStationChassisInventoryBox_14.setObjectName(u"PedalStationChassisInventoryBox_14")
        self.gridLayout_53 = QGridLayout(self.PedalStationChassisInventoryBox_14)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.horizontalSpacer_259 = QSpacerItem(30, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_259, 2, 1, 1, 1)

        self.horizontalSpacer_238 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_238, 1, 1, 1, 1)

        self.PedalStationInventoryNormalChassis_10 = QLCDNumber(self.PedalStationChassisInventoryBox_14)
        self.PedalStationInventoryNormalChassis_10.setObjectName(u"PedalStationInventoryNormalChassis_10")
        self.PedalStationInventoryNormalChassis_10.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_53.addWidget(self.PedalStationInventoryNormalChassis_10, 1, 2, 1, 1)

        self.horizontalSpacer_263 = QSpacerItem(61, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_263, 3, 1, 1, 1)

        self.PedalStationInventoryKidsChassis_16 = QLCDNumber(self.PedalStationChassisInventoryBox_14)
        self.PedalStationInventoryKidsChassis_16.setObjectName(u"PedalStationInventoryKidsChassis_16")
        self.PedalStationInventoryKidsChassis_16.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_53.addWidget(self.PedalStationInventoryKidsChassis_16, 2, 2, 1, 1)

        self.PedalStationInventoryKidsChassis_17 = QLCDNumber(self.PedalStationChassisInventoryBox_14)
        self.PedalStationInventoryKidsChassis_17.setObjectName(u"PedalStationInventoryKidsChassis_17")
        self.PedalStationInventoryKidsChassis_17.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_53.addWidget(self.PedalStationInventoryKidsChassis_17, 3, 2, 1, 1)

        self.PedalStationInventoryTotalKidsChassisLabel_17 = QLabel(self.PedalStationChassisInventoryBox_14)
        self.PedalStationInventoryTotalKidsChassisLabel_17.setObjectName(u"PedalStationInventoryTotalKidsChassisLabel_17")

        self.gridLayout_53.addWidget(self.PedalStationInventoryTotalKidsChassisLabel_17, 2, 0, 1, 1)

        self.PedalStationInventoryNormalChassisLabel_9 = QLabel(self.PedalStationChassisInventoryBox_14)
        self.PedalStationInventoryNormalChassisLabel_9.setObjectName(u"PedalStationInventoryNormalChassisLabel_9")

        self.gridLayout_53.addWidget(self.PedalStationInventoryNormalChassisLabel_9, 1, 0, 1, 1)

        self.horizontalSpacer_264 = QSpacerItem(64, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_264, 5, 1, 1, 1)

        self.horizontalSpacer_240 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_240, 0, 1, 1, 1)

        self.PedalStationInventoryTotalChassisLabel_13 = QLabel(self.PedalStationChassisInventoryBox_14)
        self.PedalStationInventoryTotalChassisLabel_13.setObjectName(u"PedalStationInventoryTotalChassisLabel_13")

        self.gridLayout_53.addWidget(self.PedalStationInventoryTotalChassisLabel_13, 0, 0, 1, 1)

        self.PedalStationInventoryTotalChassis_13 = QLCDNumber(self.PedalStationChassisInventoryBox_14)
        self.PedalStationInventoryTotalChassis_13.setObjectName(u"PedalStationInventoryTotalChassis_13")
        self.PedalStationInventoryTotalChassis_13.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_53.addWidget(self.PedalStationInventoryTotalChassis_13, 0, 2, 1, 1)

        self.PedalStationInventoryTotalKidsChassisLabel_18 = QLabel(self.PedalStationChassisInventoryBox_14)
        self.PedalStationInventoryTotalKidsChassisLabel_18.setObjectName(u"PedalStationInventoryTotalKidsChassisLabel_18")

        self.gridLayout_53.addWidget(self.PedalStationInventoryTotalKidsChassisLabel_18, 3, 0, 1, 1)

        self.PedalStationInventoryKidsChassis_18 = QLCDNumber(self.PedalStationChassisInventoryBox_14)
        self.PedalStationInventoryKidsChassis_18.setObjectName(u"PedalStationInventoryKidsChassis_18")
        self.PedalStationInventoryKidsChassis_18.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_53.addWidget(self.PedalStationInventoryKidsChassis_18, 5, 2, 1, 1)

        self.PedalStationInventoryTotalKidsChassisLabel_19 = QLabel(self.PedalStationChassisInventoryBox_14)
        self.PedalStationInventoryTotalKidsChassisLabel_19.setObjectName(u"PedalStationInventoryTotalKidsChassisLabel_19")

        self.gridLayout_53.addWidget(self.PedalStationInventoryTotalKidsChassisLabel_19, 5, 0, 1, 1)


        self.gridLayout_52.addWidget(self.PedalStationChassisInventoryBox_14, 0, 0, 1, 1)

        self.PedalStationChassisInventoryBox_15 = QGroupBox(self.ChassisStationInventoryBox_8)
        self.PedalStationChassisInventoryBox_15.setObjectName(u"PedalStationChassisInventoryBox_15")
        self.gridLayout_54 = QGridLayout(self.PedalStationChassisInventoryBox_15)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.horizontalSpacer_261 = QSpacerItem(258, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_54.addItem(self.horizontalSpacer_261, 0, 3, 1, 1)

        self.horizontalSpacer_260 = QSpacerItem(62, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_54.addItem(self.horizontalSpacer_260, 0, 1, 1, 1)

        self.PedalStationInventoryTotalChassis_14 = QLCDNumber(self.PedalStationChassisInventoryBox_15)
        self.PedalStationInventoryTotalChassis_14.setObjectName(u"PedalStationInventoryTotalChassis_14")
        self.PedalStationInventoryTotalChassis_14.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_54.addWidget(self.PedalStationInventoryTotalChassis_14, 0, 2, 1, 1)

        self.PedalStationInventoryTotalChassisLabel_14 = QLabel(self.PedalStationChassisInventoryBox_15)
        self.PedalStationInventoryTotalChassisLabel_14.setObjectName(u"PedalStationInventoryTotalChassisLabel_14")

        self.gridLayout_54.addWidget(self.PedalStationInventoryTotalChassisLabel_14, 0, 0, 1, 1)

        self.tableWidget_6 = QTableWidget(self.PedalStationChassisInventoryBox_15)
        if (self.tableWidget_6.columnCount() < 8):
            self.tableWidget_6.setColumnCount(8)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(7, __qtablewidgetitem30)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setMinimumSize(QSize(491, 211))

        self.gridLayout_54.addWidget(self.tableWidget_6, 1, 0, 1, 4)


        self.gridLayout_52.addWidget(self.PedalStationChassisInventoryBox_15, 1, 0, 1, 2)

        self.horizontalSpacer_262 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_52.addItem(self.horizontalSpacer_262, 0, 1, 1, 1)


        self.gridLayout_70.addWidget(self.ChassisStationInventoryBox_8, 0, 1, 1, 1)

        self.groupBox_9 = QGroupBox(self.SeatAssembly)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_11 = QGridLayout(self.groupBox_9)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_227 = QLabel(self.groupBox_9)
        self.label_227.setObjectName(u"label_227")

        self.gridLayout_11.addWidget(self.label_227, 5, 0, 1, 1)

        self.label_237 = QLabel(self.groupBox_9)
        self.label_237.setObjectName(u"label_237")

        self.gridLayout_11.addWidget(self.label_237, 10, 0, 1, 1)

        self.horizontalSpacer_265 = QSpacerItem(44, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_265, 10, 1, 1, 1)

        self.label_224 = QLabel(self.groupBox_9)
        self.label_224.setObjectName(u"label_224")

        self.gridLayout_11.addWidget(self.label_224, 0, 2, 1, 1)

        self.label_228 = QLabel(self.groupBox_9)
        self.label_228.setObjectName(u"label_228")

        self.gridLayout_11.addWidget(self.label_228, 5, 2, 1, 1)

        self.label_234 = QLabel(self.groupBox_9)
        self.label_234.setObjectName(u"label_234")

        self.gridLayout_11.addWidget(self.label_234, 8, 2, 1, 1)

        self.label_230 = QLabel(self.groupBox_9)
        self.label_230.setObjectName(u"label_230")

        self.gridLayout_11.addWidget(self.label_230, 6, 2, 1, 1)

        self.label_223 = QLabel(self.groupBox_9)
        self.label_223.setObjectName(u"label_223")

        self.gridLayout_11.addWidget(self.label_223, 0, 0, 1, 1)

        self.horizontalSpacer_258 = QSpacerItem(44, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_258, 9, 1, 1, 1)

        self.label_226 = QLabel(self.groupBox_9)
        self.label_226.setObjectName(u"label_226")

        self.gridLayout_11.addWidget(self.label_226, 1, 2, 1, 1)

        self.label_235 = QLabel(self.groupBox_9)
        self.label_235.setObjectName(u"label_235")

        self.gridLayout_11.addWidget(self.label_235, 9, 0, 1, 1)

        self.label_225 = QLabel(self.groupBox_9)
        self.label_225.setObjectName(u"label_225")

        self.gridLayout_11.addWidget(self.label_225, 1, 0, 1, 1)

        self.horizontalSpacer_253 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_253, 1, 1, 1, 1)

        self.label_231 = QLabel(self.groupBox_9)
        self.label_231.setObjectName(u"label_231")

        self.gridLayout_11.addWidget(self.label_231, 7, 0, 1, 1)

        self.horizontalSpacer_255 = QSpacerItem(47, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_255, 6, 1, 1, 1)

        self.label_238 = QLabel(self.groupBox_9)
        self.label_238.setObjectName(u"label_238")

        self.gridLayout_11.addWidget(self.label_238, 10, 2, 1, 1)

        self.horizontalSpacer_257 = QSpacerItem(44, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_257, 8, 1, 1, 1)

        self.horizontalSpacer_252 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_252, 0, 1, 1, 1)

        self.label_233 = QLabel(self.groupBox_9)
        self.label_233.setObjectName(u"label_233")

        self.gridLayout_11.addWidget(self.label_233, 8, 0, 1, 1)

        self.label_232 = QLabel(self.groupBox_9)
        self.label_232.setObjectName(u"label_232")

        self.gridLayout_11.addWidget(self.label_232, 7, 2, 1, 1)

        self.label_229 = QLabel(self.groupBox_9)
        self.label_229.setObjectName(u"label_229")

        self.gridLayout_11.addWidget(self.label_229, 6, 0, 1, 1)

        self.horizontalSpacer_256 = QSpacerItem(44, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_256, 7, 1, 1, 1)

        self.horizontalSpacer_254 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_254, 5, 1, 1, 1)

        self.pushButton_18 = QPushButton(self.groupBox_9)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout_11.addWidget(self.pushButton_18, 13, 0, 1, 3)

        self.label_236 = QLabel(self.groupBox_9)
        self.label_236.setObjectName(u"label_236")

        self.gridLayout_11.addWidget(self.label_236, 9, 2, 1, 1)

        self.horizontalSpacer_275 = QSpacerItem(77, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_275, 3, 1, 1, 1)

        self.label_45 = QLabel(self.groupBox_9)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_11.addWidget(self.label_45, 3, 2, 1, 1)

        self.label_110 = QLabel(self.groupBox_9)
        self.label_110.setObjectName(u"label_110")

        self.gridLayout_11.addWidget(self.label_110, 3, 0, 1, 1)


        self.gridLayout_70.addWidget(self.groupBox_9, 0, 2, 1, 1)

        self.tabWidget.addTab(self.SeatAssembly, "")
        self.stackedWidget.addWidget(self.StationsPage)
        self.InventoryDashboardPage = QWidget()
        self.InventoryDashboardPage.setObjectName(u"InventoryDashboardPage")
        self.Inventory_DashboardGroupBox = QGroupBox(self.InventoryDashboardPage)
        self.Inventory_DashboardGroupBox.setObjectName(u"Inventory_DashboardGroupBox")
        self.Inventory_DashboardGroupBox.setGeometry(QRect(10, 0, 1331, 680))
        self.Inventory_DashboardGroupBox.setMinimumSize(QSize(1331, 680))
        self.Inventory_DashboardGroupBox.setMaximumSize(QSize(1421, 680))
        self.gridLayout_75 = QGridLayout(self.Inventory_DashboardGroupBox)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.Inevntory_RawMaterialsGroupBox = QGroupBox(self.Inventory_DashboardGroupBox)
        self.Inevntory_RawMaterialsGroupBox.setObjectName(u"Inevntory_RawMaterialsGroupBox")
        self.Inevntory_RawMaterialsGroupBox.setAutoFillBackground(False)
        self.Inevntory_RawMaterialsGroupBox.setStyleSheet(u"")
        self.Inevntory_RawMaterialsGroupBox.setFlat(False)
        self.Inevntory_RawMaterialsGroupBox.setCheckable(False)
        self.gridLayout_20 = QGridLayout(self.Inevntory_RawMaterialsGroupBox)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.Inventory_RawMaterial_Label = QLabel(self.Inevntory_RawMaterialsGroupBox)
        self.Inventory_RawMaterial_Label.setObjectName(u"Inventory_RawMaterial_Label")

        self.gridLayout_20.addWidget(self.Inventory_RawMaterial_Label, 1, 0, 1, 1)

        self.Inventory_RawMaterial_Increase = QPushButton(self.Inevntory_RawMaterialsGroupBox)
        self.Inventory_RawMaterial_Increase.setObjectName(u"Inventory_RawMaterial_Increase")

        self.gridLayout_20.addWidget(self.Inventory_RawMaterial_Increase, 1, 2, 1, 1)

        self.Inventory_RawMaterial_Decrease = QPushButton(self.Inevntory_RawMaterialsGroupBox)
        self.Inventory_RawMaterial_Decrease.setObjectName(u"Inventory_RawMaterial_Decrease")

        self.gridLayout_20.addWidget(self.Inventory_RawMaterial_Decrease, 1, 3, 1, 1)

        self.Inventory_RawMaterial_LCDCount = QLCDNumber(self.Inevntory_RawMaterialsGroupBox)
        self.Inventory_RawMaterial_LCDCount.setObjectName(u"Inventory_RawMaterial_LCDCount")

        self.gridLayout_20.addWidget(self.Inventory_RawMaterial_LCDCount, 1, 1, 1, 1)

        self.Inventory_RawMaterials_PaintGroupBox = QGroupBox(self.Inevntory_RawMaterialsGroupBox)
        self.Inventory_RawMaterials_PaintGroupBox.setObjectName(u"Inventory_RawMaterials_PaintGroupBox")
        self.gridLayout_18 = QGridLayout(self.Inventory_RawMaterials_PaintGroupBox)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.Inventory_RawMaterial_BlackPaintLabel = QLabel(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_BlackPaintLabel.setObjectName(u"Inventory_RawMaterial_BlackPaintLabel")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_BlackPaintLabel, 0, 0, 1, 1)

        self.Inventory_RawMaterial_BlackPaintCount = QLCDNumber(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_BlackPaintCount.setObjectName(u"Inventory_RawMaterial_BlackPaintCount")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_BlackPaintCount, 0, 1, 1, 1)

        self.Inventory_RawMaterial_BlackPaintIncrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_BlackPaintIncrease.setObjectName(u"Inventory_RawMaterial_BlackPaintIncrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_BlackPaintIncrease, 0, 2, 1, 1)

        self.Inventory_RawMaterial_BlackPaintDecrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_BlackPaintDecrease.setObjectName(u"Inventory_RawMaterial_BlackPaintDecrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_BlackPaintDecrease, 0, 3, 1, 1)

        self.Inventory_RawMaterial_BluePaintLabel = QLabel(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_BluePaintLabel.setObjectName(u"Inventory_RawMaterial_BluePaintLabel")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_BluePaintLabel, 1, 0, 1, 1)

        self.Inventory_RawMaterial_BluePaintCount = QLCDNumber(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_BluePaintCount.setObjectName(u"Inventory_RawMaterial_BluePaintCount")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_BluePaintCount, 1, 1, 1, 1)

        self.Inventory_RawMaterial_BluePaintIncrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_BluePaintIncrease.setObjectName(u"Inventory_RawMaterial_BluePaintIncrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_BluePaintIncrease, 1, 2, 1, 1)

        self.Inventory_RawMaterial_BluePaintDecrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_BluePaintDecrease.setObjectName(u"Inventory_RawMaterial_BluePaintDecrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_BluePaintDecrease, 1, 3, 1, 1)

        self.Inventory_RawMaterial_GreenPaintLabel = QLabel(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_GreenPaintLabel.setObjectName(u"Inventory_RawMaterial_GreenPaintLabel")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_GreenPaintLabel, 2, 0, 1, 1)

        self.Inventory_RawMaterial_GreenPaintCount = QLCDNumber(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_GreenPaintCount.setObjectName(u"Inventory_RawMaterial_GreenPaintCount")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_GreenPaintCount, 2, 1, 1, 1)

        self.Inventory_RawMaterial_GreenPaintIncrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_GreenPaintIncrease.setObjectName(u"Inventory_RawMaterial_GreenPaintIncrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_GreenPaintIncrease, 2, 2, 1, 1)

        self.Inventory_RawMaterial_GreenPaintDecrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_GreenPaintDecrease.setObjectName(u"Inventory_RawMaterial_GreenPaintDecrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_GreenPaintDecrease, 2, 3, 1, 1)

        self.Inventory_RawMaterial_GreyPaintLabel = QLabel(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_GreyPaintLabel.setObjectName(u"Inventory_RawMaterial_GreyPaintLabel")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_GreyPaintLabel, 3, 0, 1, 1)

        self.Inventory_RawMaterial_GreyPaintCount = QLCDNumber(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_GreyPaintCount.setObjectName(u"Inventory_RawMaterial_GreyPaintCount")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_GreyPaintCount, 3, 1, 1, 1)

        self.Inventory_RawMaterial_GreyIncrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_GreyIncrease.setObjectName(u"Inventory_RawMaterial_GreyIncrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_GreyIncrease, 3, 2, 1, 1)

        self.Inventory_RawMaterial_GreyPaintDecrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_GreyPaintDecrease.setObjectName(u"Inventory_RawMaterial_GreyPaintDecrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_GreyPaintDecrease, 3, 3, 1, 1)

        self.Inventory_RawMaterial_OrangePaintLabel = QLabel(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_OrangePaintLabel.setObjectName(u"Inventory_RawMaterial_OrangePaintLabel")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_OrangePaintLabel, 4, 0, 1, 1)

        self.Inventory_RawMaterial_OrangePaintCount = QLCDNumber(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_OrangePaintCount.setObjectName(u"Inventory_RawMaterial_OrangePaintCount")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_OrangePaintCount, 4, 1, 1, 1)

        self.Inventory_RawMaterial_OrangePaintIncrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_OrangePaintIncrease.setObjectName(u"Inventory_RawMaterial_OrangePaintIncrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_OrangePaintIncrease, 4, 2, 1, 1)

        self.Inventory_RawMaterial_OrangePaintDecrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_OrangePaintDecrease.setObjectName(u"Inventory_RawMaterial_OrangePaintDecrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_OrangePaintDecrease, 4, 3, 1, 1)

        self.Inventory_RawMaterial_PinkPaintLabel = QLabel(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_PinkPaintLabel.setObjectName(u"Inventory_RawMaterial_PinkPaintLabel")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_PinkPaintLabel, 5, 0, 1, 1)

        self.Inventory_RawMaterial_PinkPaintCount = QLCDNumber(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_PinkPaintCount.setObjectName(u"Inventory_RawMaterial_PinkPaintCount")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_PinkPaintCount, 5, 1, 1, 1)

        self.Inventory_RawMaterial_PinkPaintIncrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_PinkPaintIncrease.setObjectName(u"Inventory_RawMaterial_PinkPaintIncrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_PinkPaintIncrease, 5, 2, 1, 1)

        self.Inventory_RawMaterial_PinkPaintDecrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_PinkPaintDecrease.setObjectName(u"Inventory_RawMaterial_PinkPaintDecrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_PinkPaintDecrease, 5, 3, 1, 1)

        self.Inventory_RawMaterial_PurplePaintLabel = QLabel(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_PurplePaintLabel.setObjectName(u"Inventory_RawMaterial_PurplePaintLabel")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_PurplePaintLabel, 6, 0, 1, 1)

        self.Inventory_RawMaterial_PurplePaintCount = QLCDNumber(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_PurplePaintCount.setObjectName(u"Inventory_RawMaterial_PurplePaintCount")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_PurplePaintCount, 6, 1, 1, 1)

        self.Inventory_RawMaterial_PurplePaintIncrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_PurplePaintIncrease.setObjectName(u"Inventory_RawMaterial_PurplePaintIncrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_PurplePaintIncrease, 6, 2, 1, 1)

        self.Inventory_RawMaterial_PurplePaintDecrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_PurplePaintDecrease.setObjectName(u"Inventory_RawMaterial_PurplePaintDecrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_PurplePaintDecrease, 6, 3, 1, 1)

        self.Inventory_RawMaterial_RedPaintLabel = QLabel(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_RedPaintLabel.setObjectName(u"Inventory_RawMaterial_RedPaintLabel")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_RedPaintLabel, 7, 0, 1, 1)

        self.Inventory_RawMaterial_RedPaintCount = QLCDNumber(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_RedPaintCount.setObjectName(u"Inventory_RawMaterial_RedPaintCount")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_RedPaintCount, 7, 1, 1, 1)

        self.Inventory_RawMaterial_RedPaintIncrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_RedPaintIncrease.setObjectName(u"Inventory_RawMaterial_RedPaintIncrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_RedPaintIncrease, 7, 2, 1, 1)

        self.Inventory_RawMaterial_RedPaintDecrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_RedPaintDecrease.setObjectName(u"Inventory_RawMaterial_RedPaintDecrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_RedPaintDecrease, 7, 3, 1, 1)

        self.Inventory_RawMaterial_YellowPaintLabel = QLabel(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_YellowPaintLabel.setObjectName(u"Inventory_RawMaterial_YellowPaintLabel")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_YellowPaintLabel, 8, 0, 1, 1)

        self.Inventory_RawMaterial_YellowPaintCount = QLCDNumber(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_YellowPaintCount.setObjectName(u"Inventory_RawMaterial_YellowPaintCount")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_YellowPaintCount, 8, 1, 1, 1)

        self.Inventory_RawMaterial_YellowPaintIncrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_YellowPaintIncrease.setObjectName(u"Inventory_RawMaterial_YellowPaintIncrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_YellowPaintIncrease, 8, 2, 1, 1)

        self.Inventory_RawMaterial_YellowPaintDecrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_YellowPaintDecrease.setObjectName(u"Inventory_RawMaterial_YellowPaintDecrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_YellowPaintDecrease, 8, 3, 1, 1)

        self.Inventory_RawMaterial_WhitePaintLabel = QLabel(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_WhitePaintLabel.setObjectName(u"Inventory_RawMaterial_WhitePaintLabel")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_WhitePaintLabel, 9, 0, 1, 1)

        self.Inventory_RawMaterial_WhitePaintCount = QLCDNumber(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_WhitePaintCount.setObjectName(u"Inventory_RawMaterial_WhitePaintCount")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_WhitePaintCount, 9, 1, 1, 1)

        self.Inventory_RawMaterial_WhitePaintIncrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_WhitePaintIncrease.setObjectName(u"Inventory_RawMaterial_WhitePaintIncrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_WhitePaintIncrease, 9, 2, 1, 1)

        self.Inventory_RawMaterial_WhitePaintDecrease = QPushButton(self.Inventory_RawMaterials_PaintGroupBox)
        self.Inventory_RawMaterial_WhitePaintDecrease.setObjectName(u"Inventory_RawMaterial_WhitePaintDecrease")

        self.gridLayout_18.addWidget(self.Inventory_RawMaterial_WhitePaintDecrease, 9, 3, 1, 1)


        self.gridLayout_20.addWidget(self.Inventory_RawMaterials_PaintGroupBox, 2, 0, 1, 4)

        self.Inventory_RawMaterial_InventoryControlLabel = QLabel(self.Inevntory_RawMaterialsGroupBox)
        self.Inventory_RawMaterial_InventoryControlLabel.setObjectName(u"Inventory_RawMaterial_InventoryControlLabel")

        self.gridLayout_20.addWidget(self.Inventory_RawMaterial_InventoryControlLabel, 0, 2, 1, 2)

        self.Inventory_RawMaterial_InventoryLabel = QLabel(self.Inevntory_RawMaterialsGroupBox)
        self.Inventory_RawMaterial_InventoryLabel.setObjectName(u"Inventory_RawMaterial_InventoryLabel")

        self.gridLayout_20.addWidget(self.Inventory_RawMaterial_InventoryLabel, 0, 1, 1, 1)

        self.Inventory_RawMaterial_ItemLabel = QLabel(self.Inevntory_RawMaterialsGroupBox)
        self.Inventory_RawMaterial_ItemLabel.setObjectName(u"Inventory_RawMaterial_ItemLabel")

        self.gridLayout_20.addWidget(self.Inventory_RawMaterial_ItemLabel, 0, 0, 1, 1)


        self.gridLayout_75.addWidget(self.Inevntory_RawMaterialsGroupBox, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 101, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_75.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.Inventory_DashboardGroupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(1074, 629))
        self.gridLayout_74 = QGridLayout(self.groupBox_2)
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.PartsInventory_PedalsGroupBox_6 = QGroupBox(self.groupBox_2)
        self.PartsInventory_PedalsGroupBox_6.setObjectName(u"PartsInventory_PedalsGroupBox_6")
        self.gridLayout_57 = QGridLayout(self.PartsInventory_PedalsGroupBox_6)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.Inventory_Parts_Pedals_NormalLabel_6 = QLabel(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_NormalLabel_6.setObjectName(u"Inventory_Parts_Pedals_NormalLabel_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_NormalLabel_6, 0, 0, 1, 1)

        self.Inventory_Parts_Pedals_NormalCount_6 = QLCDNumber(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_NormalCount_6.setObjectName(u"Inventory_Parts_Pedals_NormalCount_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_NormalCount_6, 0, 1, 1, 1)

        self.Inventory_Parts_Pedals_NormalIncrease_6 = QPushButton(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_NormalIncrease_6.setObjectName(u"Inventory_Parts_Pedals_NormalIncrease_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_NormalIncrease_6, 0, 2, 1, 1)

        self.Inventory_RawMaterial_BlackPaintDecrease_7 = QPushButton(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_RawMaterial_BlackPaintDecrease_7.setObjectName(u"Inventory_RawMaterial_BlackPaintDecrease_7")

        self.gridLayout_57.addWidget(self.Inventory_RawMaterial_BlackPaintDecrease_7, 0, 3, 1, 1)

        self.Inventory_Parts_Pedals_SportsLabel_6 = QLabel(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_SportsLabel_6.setObjectName(u"Inventory_Parts_Pedals_SportsLabel_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_SportsLabel_6, 1, 0, 1, 1)

        self.Inventory_Parts_Pedals_SportsCount_6 = QLCDNumber(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_SportsCount_6.setObjectName(u"Inventory_Parts_Pedals_SportsCount_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_SportsCount_6, 1, 1, 1, 1)

        self.Inventory_Parts_Pedals_SportsIncrease_6 = QPushButton(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_SportsIncrease_6.setObjectName(u"Inventory_Parts_Pedals_SportsIncrease_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_SportsIncrease_6, 1, 2, 1, 1)

        self.Inventory_Parts_Pedals_SportsDecrease_6 = QPushButton(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_SportsDecrease_6.setObjectName(u"Inventory_Parts_Pedals_SportsDecrease_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_SportsDecrease_6, 1, 3, 1, 1)

        self.Inventory_Parts_Pedals_KidsLabel_6 = QLabel(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_KidsLabel_6.setObjectName(u"Inventory_Parts_Pedals_KidsLabel_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_KidsLabel_6, 2, 0, 1, 1)

        self.Inventory_Parts_Pedals_KidsCount_6 = QLCDNumber(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_KidsCount_6.setObjectName(u"Inventory_Parts_Pedals_KidsCount_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_KidsCount_6, 2, 1, 1, 1)

        self.Inventory_Parts_Pedals_KidsIncrease_6 = QPushButton(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_KidsIncrease_6.setObjectName(u"Inventory_Parts_Pedals_KidsIncrease_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_KidsIncrease_6, 2, 2, 1, 1)

        self.Inventory_Parts_Pedals_KidsDecrease_6 = QPushButton(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_KidsDecrease_6.setObjectName(u"Inventory_Parts_Pedals_KidsDecrease_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_KidsDecrease_6, 2, 3, 1, 1)

        self.Inventory_Parts_Pedals_PremiumLabel_6 = QLabel(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_PremiumLabel_6.setObjectName(u"Inventory_Parts_Pedals_PremiumLabel_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_PremiumLabel_6, 3, 0, 1, 1)

        self.Inventory_Parts_Pedals_PremiumCount_6 = QLCDNumber(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_PremiumCount_6.setObjectName(u"Inventory_Parts_Pedals_PremiumCount_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_PremiumCount_6, 3, 1, 1, 1)

        self.Inventory_Parts_Pedals_PremiumIncrease_6 = QPushButton(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_PremiumIncrease_6.setObjectName(u"Inventory_Parts_Pedals_PremiumIncrease_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_PremiumIncrease_6, 3, 2, 1, 1)

        self.Inventory_Parts_Pedals_PremiumDecrease_6 = QPushButton(self.PartsInventory_PedalsGroupBox_6)
        self.Inventory_Parts_Pedals_PremiumDecrease_6.setObjectName(u"Inventory_Parts_Pedals_PremiumDecrease_6")

        self.gridLayout_57.addWidget(self.Inventory_Parts_Pedals_PremiumDecrease_6, 3, 3, 1, 1)


        self.gridLayout_74.addWidget(self.PartsInventory_PedalsGroupBox_6, 1, 1, 1, 1)

        self.PartsInventory_PedalsGroupBox_4 = QGroupBox(self.groupBox_2)
        self.PartsInventory_PedalsGroupBox_4.setObjectName(u"PartsInventory_PedalsGroupBox_4")
        self.gridLayout_24 = QGridLayout(self.PartsInventory_PedalsGroupBox_4)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.Inventory_Parts_Pedals_PremiumCount_4 = QLCDNumber(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_PremiumCount_4.setObjectName(u"Inventory_Parts_Pedals_PremiumCount_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_PremiumCount_4, 3, 1, 1, 1)

        self.Inventory_Parts_Pedals_NormalIncrease_4 = QPushButton(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_NormalIncrease_4.setObjectName(u"Inventory_Parts_Pedals_NormalIncrease_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_NormalIncrease_4, 0, 2, 1, 1)

        self.Inventory_Parts_Pedals_KidsIncrease_4 = QPushButton(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_KidsIncrease_4.setObjectName(u"Inventory_Parts_Pedals_KidsIncrease_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_KidsIncrease_4, 2, 2, 1, 1)

        self.Inventory_Parts_Pedals_KidsDecrease_4 = QPushButton(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_KidsDecrease_4.setObjectName(u"Inventory_Parts_Pedals_KidsDecrease_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_KidsDecrease_4, 2, 3, 1, 1)

        self.Inventory_Parts_Pedals_SportsCount_4 = QLCDNumber(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_SportsCount_4.setObjectName(u"Inventory_Parts_Pedals_SportsCount_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_SportsCount_4, 1, 1, 1, 1)

        self.Inventory_Parts_Pedals_KidsCount_4 = QLCDNumber(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_KidsCount_4.setObjectName(u"Inventory_Parts_Pedals_KidsCount_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_KidsCount_4, 2, 1, 1, 1)

        self.Inventory_Parts_Pedals_NormalCount_4 = QLCDNumber(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_NormalCount_4.setObjectName(u"Inventory_Parts_Pedals_NormalCount_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_NormalCount_4, 0, 1, 1, 1)

        self.Inventory_Parts_Pedals_PremiumIncrease_4 = QPushButton(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_PremiumIncrease_4.setObjectName(u"Inventory_Parts_Pedals_PremiumIncrease_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_PremiumIncrease_4, 3, 2, 1, 1)

        self.Inventory_Parts_Pedals_PremiumDecrease_4 = QPushButton(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_PremiumDecrease_4.setObjectName(u"Inventory_Parts_Pedals_PremiumDecrease_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_PremiumDecrease_4, 3, 3, 1, 1)

        self.Inventory_Parts_Pedals_SportsDecrease_4 = QPushButton(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_SportsDecrease_4.setObjectName(u"Inventory_Parts_Pedals_SportsDecrease_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_SportsDecrease_4, 1, 3, 1, 1)

        self.Inventory_Parts_Pedals_SportsIncrease_4 = QPushButton(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_SportsIncrease_4.setObjectName(u"Inventory_Parts_Pedals_SportsIncrease_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_SportsIncrease_4, 1, 2, 1, 1)

        self.Inventory_RawMaterial_BlackPaintDecrease_5 = QPushButton(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_RawMaterial_BlackPaintDecrease_5.setObjectName(u"Inventory_RawMaterial_BlackPaintDecrease_5")

        self.gridLayout_24.addWidget(self.Inventory_RawMaterial_BlackPaintDecrease_5, 0, 3, 1, 1)

        self.Inventory_Parts_Pedals_PremiumLabel_4 = QLabel(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_PremiumLabel_4.setObjectName(u"Inventory_Parts_Pedals_PremiumLabel_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_PremiumLabel_4, 3, 0, 1, 1)

        self.Inventory_Parts_Pedals_NormalLabel_4 = QLabel(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_NormalLabel_4.setObjectName(u"Inventory_Parts_Pedals_NormalLabel_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_NormalLabel_4, 0, 0, 1, 1)

        self.Inventory_Parts_Pedals_KidsLabel_4 = QLabel(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_KidsLabel_4.setObjectName(u"Inventory_Parts_Pedals_KidsLabel_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_KidsLabel_4, 2, 0, 1, 1)

        self.Inventory_Parts_Pedals_SportsLabel_4 = QLabel(self.PartsInventory_PedalsGroupBox_4)
        self.Inventory_Parts_Pedals_SportsLabel_4.setObjectName(u"Inventory_Parts_Pedals_SportsLabel_4")

        self.gridLayout_24.addWidget(self.Inventory_Parts_Pedals_SportsLabel_4, 1, 0, 1, 1)


        self.gridLayout_74.addWidget(self.PartsInventory_PedalsGroupBox_4, 0, 1, 1, 1)

        self.PartsInventory_PedalsGroupBox_2 = QGroupBox(self.groupBox_2)
        self.PartsInventory_PedalsGroupBox_2.setObjectName(u"PartsInventory_PedalsGroupBox_2")
        self.gridLayout_22 = QGridLayout(self.PartsInventory_PedalsGroupBox_2)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.Inventory_Parts_Pedals_NormalLabel_2 = QLabel(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_NormalLabel_2.setObjectName(u"Inventory_Parts_Pedals_NormalLabel_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_NormalLabel_2, 0, 0, 1, 1)

        self.Inventory_Parts_Pedals_NormalCount_2 = QLCDNumber(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_NormalCount_2.setObjectName(u"Inventory_Parts_Pedals_NormalCount_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_NormalCount_2, 0, 1, 1, 1)

        self.Inventory_Parts_Pedals_NormalIncrease_2 = QPushButton(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_NormalIncrease_2.setObjectName(u"Inventory_Parts_Pedals_NormalIncrease_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_NormalIncrease_2, 0, 2, 1, 1)

        self.Inventory_RawMaterial_BlackPaintDecrease_3 = QPushButton(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_RawMaterial_BlackPaintDecrease_3.setObjectName(u"Inventory_RawMaterial_BlackPaintDecrease_3")

        self.gridLayout_22.addWidget(self.Inventory_RawMaterial_BlackPaintDecrease_3, 0, 3, 1, 1)

        self.Inventory_Parts_Pedals_SportsLabel_2 = QLabel(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_SportsLabel_2.setObjectName(u"Inventory_Parts_Pedals_SportsLabel_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_SportsLabel_2, 1, 0, 1, 1)

        self.Inventory_Parts_Pedals_SportsCount_2 = QLCDNumber(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_SportsCount_2.setObjectName(u"Inventory_Parts_Pedals_SportsCount_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_SportsCount_2, 1, 1, 1, 1)

        self.Inventory_Parts_Pedals_SportsIncrease_2 = QPushButton(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_SportsIncrease_2.setObjectName(u"Inventory_Parts_Pedals_SportsIncrease_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_SportsIncrease_2, 1, 2, 1, 1)

        self.Inventory_Parts_Pedals_SportsDecrease_2 = QPushButton(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_SportsDecrease_2.setObjectName(u"Inventory_Parts_Pedals_SportsDecrease_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_SportsDecrease_2, 1, 3, 1, 1)

        self.Inventory_Parts_Pedals_KidsLabel_2 = QLabel(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_KidsLabel_2.setObjectName(u"Inventory_Parts_Pedals_KidsLabel_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_KidsLabel_2, 2, 0, 1, 1)

        self.Inventory_Parts_Pedals_KidsCount_2 = QLCDNumber(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_KidsCount_2.setObjectName(u"Inventory_Parts_Pedals_KidsCount_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_KidsCount_2, 2, 1, 1, 1)

        self.Inventory_Parts_Pedals_KidsIncrease_2 = QPushButton(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_KidsIncrease_2.setObjectName(u"Inventory_Parts_Pedals_KidsIncrease_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_KidsIncrease_2, 2, 2, 1, 1)

        self.Inventory_Parts_Pedals_KidsDecrease_2 = QPushButton(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_KidsDecrease_2.setObjectName(u"Inventory_Parts_Pedals_KidsDecrease_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_KidsDecrease_2, 2, 3, 1, 1)

        self.Inventory_Parts_Pedals_PremiumLabel_2 = QLabel(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_PremiumLabel_2.setObjectName(u"Inventory_Parts_Pedals_PremiumLabel_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_PremiumLabel_2, 3, 0, 1, 1)

        self.Inventory_Parts_Pedals_PremiumCount_2 = QLCDNumber(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_PremiumCount_2.setObjectName(u"Inventory_Parts_Pedals_PremiumCount_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_PremiumCount_2, 3, 1, 1, 1)

        self.Inventory_Parts_Pedals_PremiumIncrease_2 = QPushButton(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_PremiumIncrease_2.setObjectName(u"Inventory_Parts_Pedals_PremiumIncrease_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_PremiumIncrease_2, 3, 2, 1, 1)

        self.Inventory_Parts_Pedals_PremiumDecrease_2 = QPushButton(self.PartsInventory_PedalsGroupBox_2)
        self.Inventory_Parts_Pedals_PremiumDecrease_2.setObjectName(u"Inventory_Parts_Pedals_PremiumDecrease_2")

        self.gridLayout_22.addWidget(self.Inventory_Parts_Pedals_PremiumDecrease_2, 3, 3, 1, 1)


        self.gridLayout_74.addWidget(self.PartsInventory_PedalsGroupBox_2, 1, 0, 1, 1)

        self.PartsInventory_PedalsGroupBox = QGroupBox(self.groupBox_2)
        self.PartsInventory_PedalsGroupBox.setObjectName(u"PartsInventory_PedalsGroupBox")
        self.gridLayout_21 = QGridLayout(self.PartsInventory_PedalsGroupBox)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.Inventory_Parts_Pedals_NormalLabel = QLabel(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_NormalLabel.setObjectName(u"Inventory_Parts_Pedals_NormalLabel")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_NormalLabel, 0, 0, 1, 1)

        self.Inventory_Parts_Pedals_NormalCount = QLCDNumber(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_NormalCount.setObjectName(u"Inventory_Parts_Pedals_NormalCount")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_NormalCount, 0, 1, 1, 1)

        self.Inventory_Parts_Pedals_NormalIncrease = QPushButton(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_NormalIncrease.setObjectName(u"Inventory_Parts_Pedals_NormalIncrease")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_NormalIncrease, 0, 2, 1, 1)

        self.Inventory_RawMaterial_BlackPaintDecrease_2 = QPushButton(self.PartsInventory_PedalsGroupBox)
        self.Inventory_RawMaterial_BlackPaintDecrease_2.setObjectName(u"Inventory_RawMaterial_BlackPaintDecrease_2")

        self.gridLayout_21.addWidget(self.Inventory_RawMaterial_BlackPaintDecrease_2, 0, 3, 1, 1)

        self.Inventory_Parts_Pedals_SportsLabel = QLabel(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_SportsLabel.setObjectName(u"Inventory_Parts_Pedals_SportsLabel")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_SportsLabel, 1, 0, 1, 1)

        self.Inventory_Parts_Pedals_SportsCount = QLCDNumber(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_SportsCount.setObjectName(u"Inventory_Parts_Pedals_SportsCount")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_SportsCount, 1, 1, 1, 1)

        self.Inventory_Parts_Pedals_SportsIncrease = QPushButton(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_SportsIncrease.setObjectName(u"Inventory_Parts_Pedals_SportsIncrease")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_SportsIncrease, 1, 2, 1, 1)

        self.Inventory_Parts_Pedals_SportsDecrease = QPushButton(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_SportsDecrease.setObjectName(u"Inventory_Parts_Pedals_SportsDecrease")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_SportsDecrease, 1, 3, 1, 1)

        self.Inventory_Parts_Pedals_KidsLabel = QLabel(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_KidsLabel.setObjectName(u"Inventory_Parts_Pedals_KidsLabel")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_KidsLabel, 2, 0, 1, 1)

        self.Inventory_Parts_Pedals_KidsCount = QLCDNumber(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_KidsCount.setObjectName(u"Inventory_Parts_Pedals_KidsCount")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_KidsCount, 2, 1, 1, 1)

        self.Inventory_Parts_Pedals_KidsIncrease = QPushButton(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_KidsIncrease.setObjectName(u"Inventory_Parts_Pedals_KidsIncrease")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_KidsIncrease, 2, 2, 1, 1)

        self.Inventory_Parts_Pedals_KidsDecrease = QPushButton(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_KidsDecrease.setObjectName(u"Inventory_Parts_Pedals_KidsDecrease")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_KidsDecrease, 2, 3, 1, 1)

        self.Inventory_Parts_Pedals_PremiumLabel = QLabel(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_PremiumLabel.setObjectName(u"Inventory_Parts_Pedals_PremiumLabel")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_PremiumLabel, 3, 0, 1, 1)

        self.Inventory_Parts_Pedals_PremiumCount = QLCDNumber(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_PremiumCount.setObjectName(u"Inventory_Parts_Pedals_PremiumCount")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_PremiumCount, 3, 1, 1, 1)

        self.Inventory_Parts_Pedals_PremiumIncrease = QPushButton(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_PremiumIncrease.setObjectName(u"Inventory_Parts_Pedals_PremiumIncrease")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_PremiumIncrease, 3, 2, 1, 1)

        self.Inventory_Parts_Pedals_PremiumDecrease = QPushButton(self.PartsInventory_PedalsGroupBox)
        self.Inventory_Parts_Pedals_PremiumDecrease.setObjectName(u"Inventory_Parts_Pedals_PremiumDecrease")

        self.gridLayout_21.addWidget(self.Inventory_Parts_Pedals_PremiumDecrease, 3, 3, 1, 1)


        self.gridLayout_74.addWidget(self.PartsInventory_PedalsGroupBox, 0, 0, 1, 1)

        self.PartsInventory_PedalsGroupBox_5 = QGroupBox(self.groupBox_2)
        self.PartsInventory_PedalsGroupBox_5.setObjectName(u"PartsInventory_PedalsGroupBox_5")
        self.gridLayout_33 = QGridLayout(self.PartsInventory_PedalsGroupBox_5)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.Inventory_Parts_Pedals_NormalLabel_5 = QLabel(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_NormalLabel_5.setObjectName(u"Inventory_Parts_Pedals_NormalLabel_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_NormalLabel_5, 0, 0, 1, 1)

        self.Inventory_Parts_Pedals_NormalCount_5 = QLCDNumber(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_NormalCount_5.setObjectName(u"Inventory_Parts_Pedals_NormalCount_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_NormalCount_5, 0, 1, 1, 1)

        self.Inventory_Parts_Pedals_NormalIncrease_5 = QPushButton(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_NormalIncrease_5.setObjectName(u"Inventory_Parts_Pedals_NormalIncrease_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_NormalIncrease_5, 0, 2, 1, 1)

        self.Inventory_RawMaterial_BlackPaintDecrease_6 = QPushButton(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_RawMaterial_BlackPaintDecrease_6.setObjectName(u"Inventory_RawMaterial_BlackPaintDecrease_6")

        self.gridLayout_33.addWidget(self.Inventory_RawMaterial_BlackPaintDecrease_6, 0, 3, 1, 1)

        self.Inventory_Parts_Pedals_SportsLabel_5 = QLabel(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_SportsLabel_5.setObjectName(u"Inventory_Parts_Pedals_SportsLabel_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_SportsLabel_5, 1, 0, 1, 1)

        self.Inventory_Parts_Pedals_SportsCount_5 = QLCDNumber(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_SportsCount_5.setObjectName(u"Inventory_Parts_Pedals_SportsCount_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_SportsCount_5, 1, 1, 1, 1)

        self.Inventory_Parts_Pedals_SportsIncrease_5 = QPushButton(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_SportsIncrease_5.setObjectName(u"Inventory_Parts_Pedals_SportsIncrease_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_SportsIncrease_5, 1, 2, 1, 1)

        self.Inventory_Parts_Pedals_SportsDecrease_5 = QPushButton(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_SportsDecrease_5.setObjectName(u"Inventory_Parts_Pedals_SportsDecrease_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_SportsDecrease_5, 1, 3, 1, 1)

        self.Inventory_Parts_Pedals_KidsLabel_5 = QLabel(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_KidsLabel_5.setObjectName(u"Inventory_Parts_Pedals_KidsLabel_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_KidsLabel_5, 2, 0, 1, 1)

        self.Inventory_Parts_Pedals_KidsCount_5 = QLCDNumber(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_KidsCount_5.setObjectName(u"Inventory_Parts_Pedals_KidsCount_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_KidsCount_5, 2, 1, 1, 1)

        self.Inventory_Parts_Pedals_KidsIncrease_5 = QPushButton(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_KidsIncrease_5.setObjectName(u"Inventory_Parts_Pedals_KidsIncrease_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_KidsIncrease_5, 2, 2, 1, 1)

        self.Inventory_Parts_Pedals_KidsDecrease_5 = QPushButton(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_KidsDecrease_5.setObjectName(u"Inventory_Parts_Pedals_KidsDecrease_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_KidsDecrease_5, 2, 3, 1, 1)

        self.Inventory_Parts_Pedals_PremiumLabel_5 = QLabel(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_PremiumLabel_5.setObjectName(u"Inventory_Parts_Pedals_PremiumLabel_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_PremiumLabel_5, 3, 0, 1, 1)

        self.Inventory_Parts_Pedals_PremiumCount_5 = QLCDNumber(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_PremiumCount_5.setObjectName(u"Inventory_Parts_Pedals_PremiumCount_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_PremiumCount_5, 3, 1, 1, 1)

        self.Inventory_Parts_Pedals_PremiumIncrease_5 = QPushButton(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_PremiumIncrease_5.setObjectName(u"Inventory_Parts_Pedals_PremiumIncrease_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_PremiumIncrease_5, 3, 2, 1, 1)

        self.Inventory_Parts_Pedals_PremiumDecrease_5 = QPushButton(self.PartsInventory_PedalsGroupBox_5)
        self.Inventory_Parts_Pedals_PremiumDecrease_5.setObjectName(u"Inventory_Parts_Pedals_PremiumDecrease_5")

        self.gridLayout_33.addWidget(self.Inventory_Parts_Pedals_PremiumDecrease_5, 3, 3, 1, 1)


        self.gridLayout_74.addWidget(self.PartsInventory_PedalsGroupBox_5, 2, 1, 1, 1)

        self.PartsInventory_PedalsGroupBox_3 = QGroupBox(self.groupBox_2)
        self.PartsInventory_PedalsGroupBox_3.setObjectName(u"PartsInventory_PedalsGroupBox_3")
        self.gridLayout_23 = QGridLayout(self.PartsInventory_PedalsGroupBox_3)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.Inventory_Parts_Pedals_KidsCount_3 = QLCDNumber(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_KidsCount_3.setObjectName(u"Inventory_Parts_Pedals_KidsCount_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_KidsCount_3, 2, 1, 1, 1)

        self.Inventory_Parts_Pedals_NormalCount_3 = QLCDNumber(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_NormalCount_3.setObjectName(u"Inventory_Parts_Pedals_NormalCount_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_NormalCount_3, 0, 1, 1, 1)

        self.Inventory_RawMaterial_BlackPaintDecrease_4 = QPushButton(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_RawMaterial_BlackPaintDecrease_4.setObjectName(u"Inventory_RawMaterial_BlackPaintDecrease_4")

        self.gridLayout_23.addWidget(self.Inventory_RawMaterial_BlackPaintDecrease_4, 0, 3, 1, 1)

        self.Inventory_Parts_Pedals_NormalLabel_3 = QLabel(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_NormalLabel_3.setObjectName(u"Inventory_Parts_Pedals_NormalLabel_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_NormalLabel_3, 0, 0, 1, 1)

        self.Inventory_Parts_Pedals_PremiumIncrease_3 = QPushButton(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_PremiumIncrease_3.setObjectName(u"Inventory_Parts_Pedals_PremiumIncrease_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_PremiumIncrease_3, 3, 2, 1, 1)

        self.Inventory_Parts_Pedals_SportsCount_3 = QLCDNumber(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_SportsCount_3.setObjectName(u"Inventory_Parts_Pedals_SportsCount_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_SportsCount_3, 1, 1, 1, 1)

        self.Inventory_Parts_Pedals_PremiumCount_3 = QLCDNumber(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_PremiumCount_3.setObjectName(u"Inventory_Parts_Pedals_PremiumCount_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_PremiumCount_3, 3, 1, 1, 1)

        self.Inventory_Parts_Pedals_NormalIncrease_3 = QPushButton(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_NormalIncrease_3.setObjectName(u"Inventory_Parts_Pedals_NormalIncrease_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_NormalIncrease_3, 0, 2, 1, 1)

        self.Inventory_Parts_Pedals_SportsIncrease_3 = QPushButton(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_SportsIncrease_3.setObjectName(u"Inventory_Parts_Pedals_SportsIncrease_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_SportsIncrease_3, 1, 2, 1, 1)

        self.Inventory_Parts_Pedals_SportsDecrease_3 = QPushButton(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_SportsDecrease_3.setObjectName(u"Inventory_Parts_Pedals_SportsDecrease_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_SportsDecrease_3, 1, 3, 1, 1)

        self.Inventory_Parts_Pedals_KidsDecrease_3 = QPushButton(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_KidsDecrease_3.setObjectName(u"Inventory_Parts_Pedals_KidsDecrease_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_KidsDecrease_3, 2, 3, 1, 1)

        self.Inventory_Parts_Pedals_KidsLabel_3 = QLabel(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_KidsLabel_3.setObjectName(u"Inventory_Parts_Pedals_KidsLabel_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_KidsLabel_3, 2, 0, 1, 1)

        self.Inventory_Parts_Pedals_PremiumDecrease_3 = QPushButton(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_PremiumDecrease_3.setObjectName(u"Inventory_Parts_Pedals_PremiumDecrease_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_PremiumDecrease_3, 3, 3, 1, 1)

        self.Inventory_Parts_Pedals_PremiumLabel_3 = QLabel(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_PremiumLabel_3.setObjectName(u"Inventory_Parts_Pedals_PremiumLabel_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_PremiumLabel_3, 3, 0, 1, 1)

        self.Inventory_Parts_Pedals_SportsLabel_3 = QLabel(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_SportsLabel_3.setObjectName(u"Inventory_Parts_Pedals_SportsLabel_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_SportsLabel_3, 1, 0, 1, 1)

        self.Inventory_Parts_Pedals_KidsIncrease_3 = QPushButton(self.PartsInventory_PedalsGroupBox_3)
        self.Inventory_Parts_Pedals_KidsIncrease_3.setObjectName(u"Inventory_Parts_Pedals_KidsIncrease_3")

        self.gridLayout_23.addWidget(self.Inventory_Parts_Pedals_KidsIncrease_3, 2, 2, 1, 1)


        self.gridLayout_74.addWidget(self.PartsInventory_PedalsGroupBox_3, 2, 0, 1, 1)

        self.PartsInventory_PedalsGroupBox_7 = QGroupBox(self.groupBox_2)
        self.PartsInventory_PedalsGroupBox_7.setObjectName(u"PartsInventory_PedalsGroupBox_7")
        self.gridLayout_73 = QGridLayout(self.PartsInventory_PedalsGroupBox_7)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.Inventory_Parts_Pedals_NormalLabel_10 = QLabel(self.PartsInventory_PedalsGroupBox_7)
        self.Inventory_Parts_Pedals_NormalLabel_10.setObjectName(u"Inventory_Parts_Pedals_NormalLabel_10")

        self.gridLayout_73.addWidget(self.Inventory_Parts_Pedals_NormalLabel_10, 0, 0, 1, 1)

        self.Inventory_Parts_Pedals_NormalCount_10 = QLCDNumber(self.PartsInventory_PedalsGroupBox_7)
        self.Inventory_Parts_Pedals_NormalCount_10.setObjectName(u"Inventory_Parts_Pedals_NormalCount_10")

        self.gridLayout_73.addWidget(self.Inventory_Parts_Pedals_NormalCount_10, 0, 1, 1, 1)

        self.Inventory_Parts_Pedals_NormalIncrease_10 = QPushButton(self.PartsInventory_PedalsGroupBox_7)
        self.Inventory_Parts_Pedals_NormalIncrease_10.setObjectName(u"Inventory_Parts_Pedals_NormalIncrease_10")

        self.gridLayout_73.addWidget(self.Inventory_Parts_Pedals_NormalIncrease_10, 0, 2, 1, 1)

        self.Inventory_RawMaterial_BlackPaintDecrease_11 = QPushButton(self.PartsInventory_PedalsGroupBox_7)
        self.Inventory_RawMaterial_BlackPaintDecrease_11.setObjectName(u"Inventory_RawMaterial_BlackPaintDecrease_11")

        self.gridLayout_73.addWidget(self.Inventory_RawMaterial_BlackPaintDecrease_11, 0, 3, 1, 1)

        self.Inventory_Parts_Pedals_PremiumLabel_10 = QLabel(self.PartsInventory_PedalsGroupBox_7)
        self.Inventory_Parts_Pedals_PremiumLabel_10.setObjectName(u"Inventory_Parts_Pedals_PremiumLabel_10")
        self.Inventory_Parts_Pedals_PremiumLabel_10.setWordWrap(True)

        self.gridLayout_73.addWidget(self.Inventory_Parts_Pedals_PremiumLabel_10, 1, 0, 1, 1)

        self.Inventory_Parts_Pedals_PremiumCount_10 = QLCDNumber(self.PartsInventory_PedalsGroupBox_7)
        self.Inventory_Parts_Pedals_PremiumCount_10.setObjectName(u"Inventory_Parts_Pedals_PremiumCount_10")

        self.gridLayout_73.addWidget(self.Inventory_Parts_Pedals_PremiumCount_10, 1, 1, 1, 1)

        self.Inventory_Parts_Pedals_PremiumIncrease_10 = QPushButton(self.PartsInventory_PedalsGroupBox_7)
        self.Inventory_Parts_Pedals_PremiumIncrease_10.setObjectName(u"Inventory_Parts_Pedals_PremiumIncrease_10")

        self.gridLayout_73.addWidget(self.Inventory_Parts_Pedals_PremiumIncrease_10, 1, 2, 1, 1)

        self.Inventory_Parts_Pedals_PremiumDecrease_10 = QPushButton(self.PartsInventory_PedalsGroupBox_7)
        self.Inventory_Parts_Pedals_PremiumDecrease_10.setObjectName(u"Inventory_Parts_Pedals_PremiumDecrease_10")

        self.gridLayout_73.addWidget(self.Inventory_Parts_Pedals_PremiumDecrease_10, 1, 3, 1, 1)


        self.gridLayout_74.addWidget(self.PartsInventory_PedalsGroupBox_7, 0, 2, 1, 1)


        self.gridLayout_75.addWidget(self.groupBox_2, 0, 1, 2, 1)

        self.stackedWidget.addWidget(self.InventoryDashboardPage)
        self.InventoryStatisticsPage = QWidget()
        self.InventoryStatisticsPage.setObjectName(u"InventoryStatisticsPage")
        self.label_3 = QLabel(self.InventoryStatisticsPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 100, 171, 20))
        self.stackedWidget.addWidget(self.InventoryStatisticsPage)
        self.OrdersPage = QWidget()
        self.OrdersPage.setObjectName(u"OrdersPage")
        self.label_5 = QLabel(self.OrdersPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 81, 20))
        self.Orders_Table = QTableWidget(self.OrdersPage)
        if (self.Orders_Table.columnCount() < 11):
            self.Orders_Table.setColumnCount(11)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.Orders_Table.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.Orders_Table.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.Orders_Table.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.Orders_Table.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.Orders_Table.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.Orders_Table.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.Orders_Table.setHorizontalHeaderItem(6, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.Orders_Table.setHorizontalHeaderItem(7, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.Orders_Table.setHorizontalHeaderItem(8, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.Orders_Table.setHorizontalHeaderItem(9, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.Orders_Table.setHorizontalHeaderItem(10, __qtablewidgetitem41)
        self.Orders_Table.setObjectName(u"Orders_Table")
        self.Orders_Table.setGeometry(QRect(10, 30, 1251, 621))
        self.stackedWidget.addWidget(self.OrdersPage)
        self.NewOrderPage = QWidget()
        self.NewOrderPage.setObjectName(u"NewOrderPage")
        self.NewOrderGroupBox = QGroupBox(self.NewOrderPage)
        self.NewOrderGroupBox.setObjectName(u"NewOrderGroupBox")
        self.NewOrderGroupBox.setGeometry(QRect(10, 20, 958, 447))
        self.gridLayout_19 = QGridLayout(self.NewOrderGroupBox)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.BikeSelectionGroupBox = QGroupBox(self.NewOrderGroupBox)
        self.BikeSelectionGroupBox.setObjectName(u"BikeSelectionGroupBox")
        self.BikeSelectionGroupBox.setMinimumSize(QSize(332, 396))
        self.formLayout_2 = QFormLayout(self.BikeSelectionGroupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.NewOrder_BikeTypeLabel = QLabel(self.BikeSelectionGroupBox)
        self.NewOrder_BikeTypeLabel.setObjectName(u"NewOrder_BikeTypeLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.NewOrder_BikeTypeLabel)

        self.NewOrder_BikeTypeComboBox = QComboBox(self.BikeSelectionGroupBox)
        self.NewOrder_BikeTypeComboBox.addItem("")
        self.NewOrder_BikeTypeComboBox.addItem("")
        self.NewOrder_BikeTypeComboBox.addItem("")
        self.NewOrder_BikeTypeComboBox.setObjectName(u"NewOrder_BikeTypeComboBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.NewOrder_BikeTypeComboBox)

        self.NewOrder_PartsLabel = QLabel(self.BikeSelectionGroupBox)
        self.NewOrder_PartsLabel.setObjectName(u"NewOrder_PartsLabel")
        self.NewOrder_PartsLabel.setScaledContents(False)
        self.NewOrder_PartsLabel.setWordWrap(False)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.NewOrder_PartsLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout_2.setItem(1, QFormLayout.FieldRole, self.horizontalSpacer_3)

        self.NewOrder_ColourLabel = QLabel(self.BikeSelectionGroupBox)
        self.NewOrder_ColourLabel.setObjectName(u"NewOrder_ColourLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.NewOrder_ColourLabel)

        self.NewOrder_ColourComboBox = QComboBox(self.BikeSelectionGroupBox)
        self.NewOrder_ColourComboBox.addItem("")
        self.NewOrder_ColourComboBox.addItem("")
        self.NewOrder_ColourComboBox.addItem("")
        self.NewOrder_ColourComboBox.addItem("")
        self.NewOrder_ColourComboBox.addItem("")
        self.NewOrder_ColourComboBox.addItem("")
        self.NewOrder_ColourComboBox.addItem("")
        self.NewOrder_ColourComboBox.addItem("")
        self.NewOrder_ColourComboBox.addItem("")
        self.NewOrder_ColourComboBox.addItem("")
        self.NewOrder_ColourComboBox.setObjectName(u"NewOrder_ColourComboBox")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.NewOrder_ColourComboBox)

        self.NewOrder_PedalLabel = QLabel(self.BikeSelectionGroupBox)
        self.NewOrder_PedalLabel.setObjectName(u"NewOrder_PedalLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.NewOrder_PedalLabel)

        self.NewOrder_PedalTypeComboBox = QComboBox(self.BikeSelectionGroupBox)
        self.NewOrder_PedalTypeComboBox.addItem("")
        self.NewOrder_PedalTypeComboBox.addItem("")
        self.NewOrder_PedalTypeComboBox.addItem("")
        self.NewOrder_PedalTypeComboBox.addItem("")
        self.NewOrder_PedalTypeComboBox.setObjectName(u"NewOrder_PedalTypeComboBox")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.NewOrder_PedalTypeComboBox)

        self.NewOrder_ChainLabel = QLabel(self.BikeSelectionGroupBox)
        self.NewOrder_ChainLabel.setObjectName(u"NewOrder_ChainLabel")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.NewOrder_ChainLabel)

        self.NewOrder_ChainTypeComboBox = QComboBox(self.BikeSelectionGroupBox)
        self.NewOrder_ChainTypeComboBox.addItem("")
        self.NewOrder_ChainTypeComboBox.addItem("")
        self.NewOrder_ChainTypeComboBox.addItem("")
        self.NewOrder_ChainTypeComboBox.addItem("")
        self.NewOrder_ChainTypeComboBox.setObjectName(u"NewOrder_ChainTypeComboBox")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.NewOrder_ChainTypeComboBox)

        self.NewOrder_GearsLabel = QLabel(self.BikeSelectionGroupBox)
        self.NewOrder_GearsLabel.setObjectName(u"NewOrder_GearsLabel")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.NewOrder_GearsLabel)

        self.NewOrder_GearTypeComboBox = QComboBox(self.BikeSelectionGroupBox)
        self.NewOrder_GearTypeComboBox.addItem("")
        self.NewOrder_GearTypeComboBox.addItem("")
        self.NewOrder_GearTypeComboBox.addItem("")
        self.NewOrder_GearTypeComboBox.addItem("")
        self.NewOrder_GearTypeComboBox.setObjectName(u"NewOrder_GearTypeComboBox")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.NewOrder_GearTypeComboBox)

        self.NewOrder_WheelsLabel = QLabel(self.BikeSelectionGroupBox)
        self.NewOrder_WheelsLabel.setObjectName(u"NewOrder_WheelsLabel")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.NewOrder_WheelsLabel)

        self.NewOrder_WheelTypeComboBox = QComboBox(self.BikeSelectionGroupBox)
        self.NewOrder_WheelTypeComboBox.addItem("")
        self.NewOrder_WheelTypeComboBox.addItem("")
        self.NewOrder_WheelTypeComboBox.addItem("")
        self.NewOrder_WheelTypeComboBox.addItem("")
        self.NewOrder_WheelTypeComboBox.setObjectName(u"NewOrder_WheelTypeComboBox")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.NewOrder_WheelTypeComboBox)

        self.NewOrder_BrakesLabel = QLabel(self.BikeSelectionGroupBox)
        self.NewOrder_BrakesLabel.setObjectName(u"NewOrder_BrakesLabel")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.NewOrder_BrakesLabel)

        self.NewOrder_BrakeTypeComboBox = QComboBox(self.BikeSelectionGroupBox)
        self.NewOrder_BrakeTypeComboBox.addItem("")
        self.NewOrder_BrakeTypeComboBox.addItem("")
        self.NewOrder_BrakeTypeComboBox.addItem("")
        self.NewOrder_BrakeTypeComboBox.addItem("")
        self.NewOrder_BrakeTypeComboBox.setObjectName(u"NewOrder_BrakeTypeComboBox")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.NewOrder_BrakeTypeComboBox)

        self.NewOrder_LightsLabel = QLabel(self.BikeSelectionGroupBox)
        self.NewOrder_LightsLabel.setObjectName(u"NewOrder_LightsLabel")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.NewOrder_LightsLabel)

        self.NewOrder_LightTypeComboBox = QComboBox(self.BikeSelectionGroupBox)
        self.NewOrder_LightTypeComboBox.addItem("")
        self.NewOrder_LightTypeComboBox.addItem("")
        self.NewOrder_LightTypeComboBox.setObjectName(u"NewOrder_LightTypeComboBox")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.NewOrder_LightTypeComboBox)

        self.NewOrder_SeatLabel = QLabel(self.BikeSelectionGroupBox)
        self.NewOrder_SeatLabel.setObjectName(u"NewOrder_SeatLabel")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.NewOrder_SeatLabel)

        self.NewOrder_SeatTypeComboBox = QComboBox(self.BikeSelectionGroupBox)
        self.NewOrder_SeatTypeComboBox.addItem("")
        self.NewOrder_SeatTypeComboBox.addItem("")
        self.NewOrder_SeatTypeComboBox.addItem("")
        self.NewOrder_SeatTypeComboBox.addItem("")
        self.NewOrder_SeatTypeComboBox.setObjectName(u"NewOrder_SeatTypeComboBox")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.NewOrder_SeatTypeComboBox)


        self.gridLayout_19.addWidget(self.BikeSelectionGroupBox, 0, 0, 1, 1)

        self.CustomerInformationGroupBox = QGroupBox(self.NewOrderGroupBox)
        self.CustomerInformationGroupBox.setObjectName(u"CustomerInformationGroupBox")
        self.CustomerInformationGroupBox.setMinimumSize(QSize(591, 291))
        self.formLayout = QFormLayout(self.CustomerInformationGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.NewOrder_NameLabel = QLabel(self.CustomerInformationGroupBox)
        self.NewOrder_NameLabel.setObjectName(u"NewOrder_NameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.NewOrder_NameLabel)

        self.NewOrder_NameLineEdit = QLineEdit(self.CustomerInformationGroupBox)
        self.NewOrder_NameLineEdit.setObjectName(u"NewOrder_NameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.NewOrder_NameLineEdit)

        self.NewOrder_EmailLabel = QLabel(self.CustomerInformationGroupBox)
        self.NewOrder_EmailLabel.setObjectName(u"NewOrder_EmailLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.NewOrder_EmailLabel)

        self.NewOrder_EmailLineEdit = QLineEdit(self.CustomerInformationGroupBox)
        self.NewOrder_EmailLineEdit.setObjectName(u"NewOrder_EmailLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.NewOrder_EmailLineEdit)

        self.NewOrder_PhoneLabel = QLabel(self.CustomerInformationGroupBox)
        self.NewOrder_PhoneLabel.setObjectName(u"NewOrder_PhoneLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.NewOrder_PhoneLabel)

        self.NewOrder_PhoneLineEdit = QLineEdit(self.CustomerInformationGroupBox)
        self.NewOrder_PhoneLineEdit.setObjectName(u"NewOrder_PhoneLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.NewOrder_PhoneLineEdit)

        self.NewOrder_AddressLine1Label = QLabel(self.CustomerInformationGroupBox)
        self.NewOrder_AddressLine1Label.setObjectName(u"NewOrder_AddressLine1Label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.NewOrder_AddressLine1Label)

        self.NewOrder_AddressLine1LineEdit = QLineEdit(self.CustomerInformationGroupBox)
        self.NewOrder_AddressLine1LineEdit.setObjectName(u"NewOrder_AddressLine1LineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.NewOrder_AddressLine1LineEdit)

        self.NewOrder_AddressLine2Label = QLabel(self.CustomerInformationGroupBox)
        self.NewOrder_AddressLine2Label.setObjectName(u"NewOrder_AddressLine2Label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.NewOrder_AddressLine2Label)

        self.NewOrder_AddressLine2LineEdit = QLineEdit(self.CustomerInformationGroupBox)
        self.NewOrder_AddressLine2LineEdit.setObjectName(u"NewOrder_AddressLine2LineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.NewOrder_AddressLine2LineEdit)

        self.NewOrder_CityLabel = QLabel(self.CustomerInformationGroupBox)
        self.NewOrder_CityLabel.setObjectName(u"NewOrder_CityLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.NewOrder_CityLabel)

        self.NewOrder_CityLineEdit = QLineEdit(self.CustomerInformationGroupBox)
        self.NewOrder_CityLineEdit.setObjectName(u"NewOrder_CityLineEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.NewOrder_CityLineEdit)

        self.NewOrder_PostcodeLabel = QLabel(self.CustomerInformationGroupBox)
        self.NewOrder_PostcodeLabel.setObjectName(u"NewOrder_PostcodeLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.NewOrder_PostcodeLabel)

        self.NewOrder_PostcodeLineEdit = QLineEdit(self.CustomerInformationGroupBox)
        self.NewOrder_PostcodeLineEdit.setObjectName(u"NewOrder_PostcodeLineEdit")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.NewOrder_PostcodeLineEdit)

        self.NewOrder_SubmitOrderButton = QPushButton(self.CustomerInformationGroupBox)
        self.NewOrder_SubmitOrderButton.setObjectName(u"NewOrder_SubmitOrderButton")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.NewOrder_SubmitOrderButton)


        self.gridLayout_19.addWidget(self.CustomerInformationGroupBox, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.NewOrderPage)
        self.StationStatisticsPage = QWidget()
        self.StationStatisticsPage.setObjectName(u"StationStatisticsPage")
        self.label_2 = QLabel(self.StationStatisticsPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 20, 271, 20))
        self.stackedWidget.addWidget(self.StationStatisticsPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1484, 25))
        self.menuBike_Factory_Dashboard = QMenu(self.menubar)
        self.menuBike_Factory_Dashboard.setObjectName(u"menuBike_Factory_Dashboard")
        self.menuInventory_Management = QMenu(self.menubar)
        self.menuInventory_Management.setObjectName(u"menuInventory_Management")
        self.menuOrders = QMenu(self.menubar)
        self.menuOrders.setObjectName(u"menuOrders")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuBike_Factory_Dashboard.menuAction())
        self.menubar.addAction(self.menuInventory_Management.menuAction())
        self.menubar.addAction(self.menuOrders.menuAction())
        self.menuBike_Factory_Dashboard.addAction(self.actionStations)
        self.menuBike_Factory_Dashboard.addAction(self.actionSatistics)
        self.menuBike_Factory_Dashboard.addSeparator()
        self.menuBike_Factory_Dashboard.addSeparator()
        self.menuInventory_Management.addAction(self.actionInventoryDashboard)
        self.menuInventory_Management.addAction(self.actionStatistics)
        self.menuOrders.addAction(self.actionOrdersDashboard)
        self.menuOrders.addAction(self.actionAdd_Order)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionAutosave)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.actionInventory_Management.setText(QCoreApplication.translate("MainWindow", u"Inventory Management", None))
        self.actionOrder_Management.setText(QCoreApplication.translate("MainWindow", u"Order Management", None))
        self.actionSatistics.setText(QCoreApplication.translate("MainWindow", u"Satistics", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionStations.setText(QCoreApplication.translate("MainWindow", u"Stations", None))
#if QT_CONFIG(shortcut)
        self.actionStations.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionInventoryDashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#if QT_CONFIG(tooltip)
        self.actionInventoryDashboard.setToolTip(QCoreApplication.translate("MainWindow", u"Inventory Dashboard", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionInventoryDashboard.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionStatistics.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.actionOrdersDashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#if QT_CONFIG(shortcut)
        self.actionOrdersDashboard.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionAdd_Order.setText(QCoreApplication.translate("MainWindow", u"New Order", None))
#if QT_CONFIG(shortcut)
        self.actionAdd_Order.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAutosave.setText(QCoreApplication.translate("MainWindow", u"Autosave", None))
#if QT_CONFIG(shortcut)
        self.actionAutosave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.ForksOrderInformationBox.setTitle(QCoreApplication.translate("MainWindow", u"Order Information", None))
        self.LightsLabel_2.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.BikeType_2.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.PedalType_2.setText(QCoreApplication.translate("MainWindow", u"Pedal Type", None))
        self.OrderNumberLabel_2.setText(QCoreApplication.translate("MainWindow", u"Order Number:", None))
        self.OrderNumber_2.setText(QCoreApplication.translate("MainWindow", u"[Order Number]", None))
        self.SeatLabel_2.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.PartsLabel_2.setText(QCoreApplication.translate("MainWindow", u"Parts", None))
        self.PedalLabel_2.setText(QCoreApplication.translate("MainWindow", u"Pedals", None))
        self.Colour_2.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.LightsType_2.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.ChainLabel_2.setText(QCoreApplication.translate("MainWindow", u"Chains", None))
        self.ColourLabel_2.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.GearsLabel_2.setText(QCoreApplication.translate("MainWindow", u"Gears", None))
        self.BrakesType_2.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.GearType_2.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.BikeTypeLabel_2.setText(QCoreApplication.translate("MainWindow", u"Bike Type:", None))
        self.BrakesLabel_2.setText(QCoreApplication.translate("MainWindow", u"Brakes", None))
        self.ChainType_2.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.SeatType_2.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.WheelsLabel_2.setText(QCoreApplication.translate("MainWindow", u"Wheels", None))
        self.WheelType_2.setText(QCoreApplication.translate("MainWindow", u"Wheel Type:", None))
        self.ForkStationInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Station Inventory", None))
        self.ForkStationTubularSteelInventoryLabel.setText(QCoreApplication.translate("MainWindow", u"Tubular Steel", None))
        self.ForkStationTubularSteelRequiredLabel.setText(QCoreApplication.translate("MainWindow", u"Required for Order:", None))
        self.ForkStationForkInventory.setTitle(QCoreApplication.translate("MainWindow", u"Forks Inventory", None))
        self.ForkStationInventoryTotalForksLabel.setText(QCoreApplication.translate("MainWindow", u"Total Forks", None))
        self.ForkStationInventoryNormalForksLabel.setText(QCoreApplication.translate("MainWindow", u"Normal Forks", None))
        self.ForkStationInventorySportsForksLabel.setText(QCoreApplication.translate("MainWindow", u"Sports Forks", None))
        self.ForkStationInventoryKidsForksLabel.setText(QCoreApplication.translate("MainWindow", u"Kids Forks", None))
        self.ForkStationBox.setTitle(QCoreApplication.translate("MainWindow", u"Fork Welding Station", None))
        self.ForkStationForkLabel.setText(QCoreApplication.translate("MainWindow", u"Fork Type:", None))
        self.ForkWeldedButton.setText(QCoreApplication.translate("MainWindow", u"Fork Welded", None))
        self.ForkStationForkValue.setText(QCoreApplication.translate("MainWindow", u"[Fork Type]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ForkStation), QCoreApplication.translate("MainWindow", u"Forks", None))
        self.GroupBoxOrder.setTitle(QCoreApplication.translate("MainWindow", u"Order Information", None))
        self.LightsType.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.Colour.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.GearType.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.BrakesType.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.SeatLabel.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.ChainLabel.setText(QCoreApplication.translate("MainWindow", u"Chains", None))
        self.PedalLabel.setText(QCoreApplication.translate("MainWindow", u"Pedals", None))
        self.BrakesLabel.setText(QCoreApplication.translate("MainWindow", u"Brakes", None))
        self.BikeTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Bike Type:", None))
        self.ColourLabel.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.BikeType.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.SeatType.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.ChainType.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.OrderNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Order Number:", None))
        self.GearsLabel.setText(QCoreApplication.translate("MainWindow", u"Gears", None))
        self.LightsLabel.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.PedalType.setText(QCoreApplication.translate("MainWindow", u"Pedal Type", None))
        self.OrderNumber.setText(QCoreApplication.translate("MainWindow", u"[Order Number]", None))
        self.PartsLabel.setText(QCoreApplication.translate("MainWindow", u"Parts", None))
        self.WheelsLabel.setText(QCoreApplication.translate("MainWindow", u"Wheels", None))
        self.WheelType.setText(QCoreApplication.translate("MainWindow", u"Wheel Type:", None))
        self.FrameStationInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Station Inventory", None))
        self.FrameStationInventoryTubularSteelLabel.setText(QCoreApplication.translate("MainWindow", u"Tubular Steel", None))
        self.FrameStationInventoryRequiredTubularSteelLabel.setText(QCoreApplication.translate("MainWindow", u"Required for Order:", None))
        self.FrameStationFrameInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Frames Inventory", None))
        self.FrameStationTotalFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Total Frames", None))
        self.FrameStationNormalFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Normal Frames", None))
        self.FrameStationSportsFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Sports Frames", None))
        self.FrameStationKidsFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Kids Frames", None))
        self.FrameWeldingStation.setTitle(QCoreApplication.translate("MainWindow", u"Frame Welding Station", None))
        self.FrameWeldingStationLabel.setText(QCoreApplication.translate("MainWindow", u"Frame Type:", None))
        self.FrameWeldingStationType.setText(QCoreApplication.translate("MainWindow", u"[Frame Type]", None))
        self.FrameWeldingStationButton.setText(QCoreApplication.translate("MainWindow", u"Frame Welded", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FrameStation), QCoreApplication.translate("MainWindow", u"Frames", None))
        self.ChassisOrder.setTitle(QCoreApplication.translate("MainWindow", u"Order Information", None))
        self.BrakesLabel_3.setText(QCoreApplication.translate("MainWindow", u"Brakes", None))
        self.OrderNumber_3.setText(QCoreApplication.translate("MainWindow", u"[Order Number]", None))
        self.SeatLabel_3.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.LightsType_3.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.ChainLabel_3.setText(QCoreApplication.translate("MainWindow", u"Chains", None))
        self.BrakesType_3.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.GearsLabel_3.setText(QCoreApplication.translate("MainWindow", u"Gears", None))
        self.BikeTypeLabel_3.setText(QCoreApplication.translate("MainWindow", u"Bike Type:", None))
        self.LightsLabel_3.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.BikeType_3.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.OrderNumberLabel_3.setText(QCoreApplication.translate("MainWindow", u"Order Number:", None))
        self.PedalType_3.setText(QCoreApplication.translate("MainWindow", u"Pedal Type", None))
        self.ColourLabel_3.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.Colour_3.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.ChainType_3.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.PedalLabel_3.setText(QCoreApplication.translate("MainWindow", u"Pedals", None))
        self.GearType_3.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.SeatType_3.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.PartsLabel_3.setText(QCoreApplication.translate("MainWindow", u"Parts", None))
        self.WheelsLabel_3.setText(QCoreApplication.translate("MainWindow", u"Wheels", None))
        self.WheelType_3.setText(QCoreApplication.translate("MainWindow", u"Wheel Type:", None))
        self.ChassisStationInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Station Inventory", None))
        self.ChassisInventoryFramesBox.setTitle(QCoreApplication.translate("MainWindow", u"Frames Inventory", None))
        self.ChassisInventoryTotalFramesLabel.setText(QCoreApplication.translate("MainWindow", u"Total Frames", None))
        self.ChassisInventoryNormalFramesLabel.setText(QCoreApplication.translate("MainWindow", u"Normal Frames", None))
        self.ChassisInventorySportsFramesLabel.setText(QCoreApplication.translate("MainWindow", u"Sports Frames", None))
        self.ChassisInventoryKidsFramesLabel.setText(QCoreApplication.translate("MainWindow", u"Kids Frames", None))
        self.ChassisInventoryForksBox.setTitle(QCoreApplication.translate("MainWindow", u"Forks Inventory", None))
        self.ChassisInventoryTotalForksLabel.setText(QCoreApplication.translate("MainWindow", u"Total Forks", None))
        self.ChassisInventoryNormalForksLabel.setText(QCoreApplication.translate("MainWindow", u"Normal Forks", None))
        self.ChassisInventorySportsForksLabel.setText(QCoreApplication.translate("MainWindow", u"Sports Forks", None))
        self.ChassisInventoryKidsForksLabel.setText(QCoreApplication.translate("MainWindow", u"Kids Forks", None))
        self.ChassisInventoryChassisBox.setTitle(QCoreApplication.translate("MainWindow", u"Chassis Inventory", None))
        self.ChassisInventoryTotalChassisLabel.setText(QCoreApplication.translate("MainWindow", u"Total Chassis", None))
        self.ChassisInventoryNormalChassisLabel.setText(QCoreApplication.translate("MainWindow", u"Normal Chassis", None))
        self.ChassisInventorySportsChassisLabel.setText(QCoreApplication.translate("MainWindow", u"Sports Chassis", None))
        self.ChassisInventoryKidsChassisLabel.setText(QCoreApplication.translate("MainWindow", u"Kids Chassis", None))
        self.ChassisAssemblyBox.setTitle(QCoreApplication.translate("MainWindow", u"Chassis Assembly", None))
        self.ChassisAssemblyTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Chassis Type:", None))
        self.ChassisAssemblyType.setText(QCoreApplication.translate("MainWindow", u"[Chassis Type]", None))
        self.ChassisAssemblyButton.setText(QCoreApplication.translate("MainWindow", u"Chassis Assembled", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ChassisAssembly), QCoreApplication.translate("MainWindow", u"Chassis Assembly", None))
        self.PaintingStationInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Station Inventory", None))
        self.PaintingChassisInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Chassis Inventory", None))
        self.PaintStationInventoryTotalChassisLabel.setText(QCoreApplication.translate("MainWindow", u"Total Chassis", None))
        self.PaintStationInventoryNormalChassisLabel.setText(QCoreApplication.translate("MainWindow", u"Normal Chassis", None))
        self.PaintStationInventorySportsChassisLabel.setText(QCoreApplication.translate("MainWindow", u"Sports Chassis", None))
        self.PaintStationInventoryKidsChassisLabel.setText(QCoreApplication.translate("MainWindow", u"Kids Chassis", None))
        self.PaintInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Paint Inventory", None))
        self.PaintStationOrangePaintLabel.setText(QCoreApplication.translate("MainWindow", u"Orange", None))
        self.PaintStationWhitePaintLabel.setText(QCoreApplication.translate("MainWindow", u"White", None))
        self.PaintStationPurplePaintLabel.setText(QCoreApplication.translate("MainWindow", u"Purple", None))
        self.PaintStationBluePaintLabel.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.PaintStationBlackPaintLabel.setText(QCoreApplication.translate("MainWindow", u"Black", None))
        self.PaintStationGreenPaintLabel.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.PaintStationRedPaintLabel.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.PaintStationGreyPaintLabel.setText(QCoreApplication.translate("MainWindow", u"Grey", None))
        self.PaintStationPinkPaintLabel.setText(QCoreApplication.translate("MainWindow", u"Pink", None))
        self.PaintStationYellowPaintLabel.setText(QCoreApplication.translate("MainWindow", u"Yellow", None))
        self.PaintingStationBox.setTitle(QCoreApplication.translate("MainWindow", u"Paint Station", None))
        self.PaintStationChassisLabel.setText(QCoreApplication.translate("MainWindow", u"Chassis:", None))
        self.PaintStationChassisValue.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.PaintStationColourLabel.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.PaintStationColourValue.setText(QCoreApplication.translate("MainWindow", u"[Colour]", None))
        self.PaintedButton.setText(QCoreApplication.translate("MainWindow", u"Painted", None))
        self.PaintOrder.setTitle(QCoreApplication.translate("MainWindow", u"Order Information", None))
        self.GearsLabel_5.setText(QCoreApplication.translate("MainWindow", u"Gears", None))
        self.GearType_5.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.ColourLabel_5.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.BikeTypeLabel_5.setText(QCoreApplication.translate("MainWindow", u"Bike Type:", None))
        self.Colour_5.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.PedalLabel_5.setText(QCoreApplication.translate("MainWindow", u"Pedals", None))
        self.PedalType_5.setText(QCoreApplication.translate("MainWindow", u"Pedal Type", None))
        self.BrakesLabel_5.setText(QCoreApplication.translate("MainWindow", u"Brakes", None))
        self.SeatType_5.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.ChainLabel_5.setText(QCoreApplication.translate("MainWindow", u"Chains", None))
        self.BrakesType_5.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.SeatLabel_5.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.OrderNumber_5.setText(QCoreApplication.translate("MainWindow", u"[Order Number]", None))
        self.ChainType_5.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.OrderNumberLabel_5.setText(QCoreApplication.translate("MainWindow", u"Order Number:", None))
        self.LightsType_5.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.PartsLabel_5.setText(QCoreApplication.translate("MainWindow", u"Parts", None))
        self.BikeType_5.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.LightsLabel_5.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.WheelsLabel_5.setText(QCoreApplication.translate("MainWindow", u"Wheels", None))
        self.WheelType_5.setText(QCoreApplication.translate("MainWindow", u"Wheel Type:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Painting), QCoreApplication.translate("MainWindow", u"Painting", None))
        self.PedalsOrder.setTitle(QCoreApplication.translate("MainWindow", u"Order Information", None))
        self.BrakesLabel_4.setText(QCoreApplication.translate("MainWindow", u"Brakes", None))
        self.PartsLabel_4.setText(QCoreApplication.translate("MainWindow", u"Parts", None))
        self.GearType_4.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.OrderNumberLabel_4.setText(QCoreApplication.translate("MainWindow", u"Order Number:", None))
        self.SeatType_4.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.GearsLabel_4.setText(QCoreApplication.translate("MainWindow", u"Gears", None))
        self.PedalType_4.setText(QCoreApplication.translate("MainWindow", u"Pedal Type", None))
        self.BikeTypeLabel_4.setText(QCoreApplication.translate("MainWindow", u"Bike Type:", None))
        self.ColourLabel_4.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.BikeType_4.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.ChainType_4.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.BrakesType_4.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.Colour_4.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.LightsType_4.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.LightsLabel_4.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.SeatLabel_4.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.PedalLabel_4.setText(QCoreApplication.translate("MainWindow", u"Pedals", None))
        self.OrderNumber_4.setText(QCoreApplication.translate("MainWindow", u"[Order Number]", None))
        self.ChainLabel_4.setText(QCoreApplication.translate("MainWindow", u"Chains", None))
        self.WheelsLabel_4.setText(QCoreApplication.translate("MainWindow", u"Wheels", None))
        self.WheelType_4.setText(QCoreApplication.translate("MainWindow", u"Wheel Type:", None))
        self.PedalStationInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Station Inventory", None))
        self.PedalStationChassisInventoryBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Pedal Inventory", None))
        self.PedalStationInventoryTotalChassisLabel_2.setText(QCoreApplication.translate("MainWindow", u"Total Pedals", None))
        self.PedalStationInventoryNormalChassisLabel_2.setText(QCoreApplication.translate("MainWindow", u"Normal Pedals", None))
        self.PedalStationInventoryTotalSportsChassisLabel_2.setText(QCoreApplication.translate("MainWindow", u"Sports Pedals", None))
        self.PedalStationInventoryTotalKidsChassisLabel_2.setText(QCoreApplication.translate("MainWindow", u"Kids Pedals", None))
        self.PedalStationInventoryTotalKidsChassisLabel_3.setText(QCoreApplication.translate("MainWindow", u"Premium Pedals", None))
        self.PedalStationChassisInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Chassis Inventory", None))
        self.PedalStationInventoryTotalChassisLabel.setText(QCoreApplication.translate("MainWindow", u"Total Chassis", None))
        ___qtablewidgetitem = self.PedalStationInventoryChassisTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Chassis Type", None));
        ___qtablewidgetitem1 = self.PedalStationInventoryChassisTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Paint Colour", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Pedal Assembly", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" Assembled", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Chassis Type:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Pedal Type:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"[Pedal Type]", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"[Colour]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PedalAssembly), QCoreApplication.translate("MainWindow", u"Pedals", None))
        self.DriveChainOrder.setTitle(QCoreApplication.translate("MainWindow", u"Order Information", None))
        self.ColourLabel_7.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.SeatLabel_7.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.SeatType_7.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.LightsLabel_7.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.BrakesLabel_7.setText(QCoreApplication.translate("MainWindow", u"Brakes", None))
        self.ChainType_7.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.PartsLabel_7.setText(QCoreApplication.translate("MainWindow", u"Parts", None))
        self.PedalLabel_7.setText(QCoreApplication.translate("MainWindow", u"Pedals", None))
        self.GearType_7.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.LightsType_7.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.BikeType_7.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.Colour_7.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.BrakesType_7.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.OrderNumberLabel_7.setText(QCoreApplication.translate("MainWindow", u"Order Number:", None))
        self.BikeTypeLabel_7.setText(QCoreApplication.translate("MainWindow", u"Bike Type:", None))
        self.ChainLabel_7.setText(QCoreApplication.translate("MainWindow", u"Chains", None))
        self.PedalType_7.setText(QCoreApplication.translate("MainWindow", u"Pedal Type", None))
        self.OrderNumber_7.setText(QCoreApplication.translate("MainWindow", u"[Order Number]", None))
        self.GearsLabel_7.setText(QCoreApplication.translate("MainWindow", u"Gears", None))
        self.WheelsLabel_7.setText(QCoreApplication.translate("MainWindow", u"Wheels", None))
        self.WheelType_7.setText(QCoreApplication.translate("MainWindow", u"Wheel Type:", None))
        self.DCStationInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Station Inventory", None))
        self.DCStationGearInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Gear Inventory", None))
        self.DCStationInventoryTotalGearLabel.setText(QCoreApplication.translate("MainWindow", u"Total Gears", None))
        self.DCStationInventoryNormalGearLabel.setText(QCoreApplication.translate("MainWindow", u"Normal Gears", None))
        self.DCStationInventorySporsGearLabel.setText(QCoreApplication.translate("MainWindow", u"Sports Gears", None))
        self.DCStationInventoryKidsGearLabel.setText(QCoreApplication.translate("MainWindow", u"Kids Gears", None))
        self.DCStationInventoryPremiumGearLabel.setText(QCoreApplication.translate("MainWindow", u"Premium Gears", None))
        self.DCStationChainInventory.setTitle(QCoreApplication.translate("MainWindow", u"Chain Inventory", None))
        self.DCStationInventoryTotalChainLabel.setText(QCoreApplication.translate("MainWindow", u"Total Chains", None))
        self.DCStationInventoryNormalChainLabel.setText(QCoreApplication.translate("MainWindow", u"Normal Chain", None))
        self.DCStationInventorySportsChainLabel.setText(QCoreApplication.translate("MainWindow", u"Sports Chain", None))
        self.DCStationInventoryKidsChainLabel.setText(QCoreApplication.translate("MainWindow", u"Kids Chain", None))
        self.DCStationInventoryPremiumChainLabel.setText(QCoreApplication.translate("MainWindow", u"Premium Chain", None))
        self.DCStationChassisInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Chassis Inventory", None))
        self.DCStationInventoryTotalChassisLabel.setText(QCoreApplication.translate("MainWindow", u"Total Chassis", None))
        ___qtablewidgetitem2 = self.DCStationChassisInventoryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Chassis Type", None));
        ___qtablewidgetitem3 = self.DCStationChassisInventoryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Paint Colour", None));
        ___qtablewidgetitem4 = self.DCStationChassisInventoryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Pedal Type", None));
        self.DCAssembly.setTitle(QCoreApplication.translate("MainWindow", u"Drive Chain Assembly", None))
        self.DCAssemblyChassisValue.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.DCAssembledButton.setText(QCoreApplication.translate("MainWindow", u"Drive Chain Assembled", None))
        self.DCAssemblyGearLabel.setText(QCoreApplication.translate("MainWindow", u"Gear Type:", None))
        self.DCAssemblyChassisLabel.setText(QCoreApplication.translate("MainWindow", u"Chassis Type:", None))
        self.DCAssemblyGearValue.setText(QCoreApplication.translate("MainWindow", u"[Gear Type]", None))
        self.DCAssemblyColourLabel.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.DCAssemblyColourValue.setText(QCoreApplication.translate("MainWindow", u"[Colour]", None))
        self.DCAssemblyChainValue.setText(QCoreApplication.translate("MainWindow", u"[Chain Type]", None))
        self.DCAssemblyChainLabel.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.DCAssemblyPedalValue.setText(QCoreApplication.translate("MainWindow", u"[Pedal Type]", None))
        self.DCAssemblyPedalLabel.setText(QCoreApplication.translate("MainWindow", u"Pedal Type:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DriveChainAssembly), QCoreApplication.translate("MainWindow", u"Drive Chain", None))
        self.WheelsOrder.setTitle(QCoreApplication.translate("MainWindow", u"Order Information", None))
        self.Colour_6.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.OrderNumber_6.setText(QCoreApplication.translate("MainWindow", u"[Order Number]", None))
        self.SeatType_6.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.LightsType_6.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.OrderNumberLabel_6.setText(QCoreApplication.translate("MainWindow", u"Order Number:", None))
        self.BikeTypeLabel_6.setText(QCoreApplication.translate("MainWindow", u"Bike Type:", None))
        self.PedalType_6.setText(QCoreApplication.translate("MainWindow", u"Pedal Type", None))
        self.PedalLabel_6.setText(QCoreApplication.translate("MainWindow", u"Pedals", None))
        self.LightsLabel_6.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.ChainType_6.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.BikeType_6.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.BrakesType_6.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.ColourLabel_6.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.GearsLabel_6.setText(QCoreApplication.translate("MainWindow", u"Gears", None))
        self.ChainLabel_6.setText(QCoreApplication.translate("MainWindow", u"Chains", None))
        self.BrakesLabel_6.setText(QCoreApplication.translate("MainWindow", u"Brakes", None))
        self.SeatLabel_6.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.PartsLabel_6.setText(QCoreApplication.translate("MainWindow", u"Parts", None))
        self.GearType_6.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.WheelType_6.setText(QCoreApplication.translate("MainWindow", u"Wheel Type:", None))
        self.WheelsLabel_6.setText(QCoreApplication.translate("MainWindow", u"Wheels", None))
        self.ChassisStationInventoryBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Station Inventory", None))
        self.PedalStationChassisInventoryBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Wheel Inventory", None))
        self.PedalStationInventoryTotalKidsChassisLabel_11.setText(QCoreApplication.translate("MainWindow", u"Kids Wheels", None))
        self.PedalStationInventoryTotalSportsChassisLabel_7.setText(QCoreApplication.translate("MainWindow", u"Sports Wheels", None))
        self.PedalStationInventoryTotalChassisLabel_7.setText(QCoreApplication.translate("MainWindow", u"Total Wheels", None))
        self.PedalStationInventoryNormalChassisLabel_6.setText(QCoreApplication.translate("MainWindow", u"Normal Wheels", None))
        self.PedalStationInventoryTotalKidsChassisLabel_12.setText(QCoreApplication.translate("MainWindow", u"Premium Wheels", None))
        self.PedalStationChassisInventoryBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Chassis Inventory", None))
        self.PedalStationInventoryTotalChassisLabel_9.setText(QCoreApplication.translate("MainWindow", u"Total Chassis", None))
        ___qtablewidgetitem5 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Chassis", None));
        ___qtablewidgetitem6 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Colour", None));
        ___qtablewidgetitem7 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Pedal", None));
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Gear", None));
        ___qtablewidgetitem9 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Chain", None));
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Wheel Assembly", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"[Chain Type]", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"[Wheel Type]", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Wheels Assembled", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Wheel Type:", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Gear Type:", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"[Colour]", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"[Gear Type]", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Chassis Type:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"[Pedal Type]", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Pedal Type:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.WheelAssembly), QCoreApplication.translate("MainWindow", u"Wheels", None))
        self.BrakesOrder.setTitle(QCoreApplication.translate("MainWindow", u"Order Information", None))
        self.BrakesLabel_8.setText(QCoreApplication.translate("MainWindow", u"Brakes", None))
        self.OrderNumberLabel_8.setText(QCoreApplication.translate("MainWindow", u"Order Number:", None))
        self.PedalLabel_8.setText(QCoreApplication.translate("MainWindow", u"Pedals", None))
        self.ColourLabel_8.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.PartsLabel_8.setText(QCoreApplication.translate("MainWindow", u"Parts", None))
        self.ChainType_8.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.Colour_8.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.SeatType_8.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.BikeType_8.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.GearType_8.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.BikeTypeLabel_8.setText(QCoreApplication.translate("MainWindow", u"Bike Type:", None))
        self.GearsLabel_8.setText(QCoreApplication.translate("MainWindow", u"Gears", None))
        self.PedalType_8.setText(QCoreApplication.translate("MainWindow", u"Pedal Type", None))
        self.OrderNumber_8.setText(QCoreApplication.translate("MainWindow", u"[Order Number]", None))
        self.BrakesType_8.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.SeatLabel_8.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.LightsType_8.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.LightsLabel_8.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.ChainLabel_8.setText(QCoreApplication.translate("MainWindow", u"Chains", None))
        self.WheelsLabel_8.setText(QCoreApplication.translate("MainWindow", u"Wheels", None))
        self.WheelType_8.setText(QCoreApplication.translate("MainWindow", u"Wheel Type:", None))
        self.BrakeStationInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Station Inventory", None))
        self.BrakeStationBrakeInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Brakes Inventory", None))
        self.BrakeStationKidsBrakeLabel.setText(QCoreApplication.translate("MainWindow", u"Kids Brakes", None))
        self.BrakeStationSportBrakeLabel.setText(QCoreApplication.translate("MainWindow", u"Sports Brakes", None))
        self.BrakeStationTotalBrakeLabel.setText(QCoreApplication.translate("MainWindow", u"Total Brakes", None))
        self.BrakeStationNormalBrakeLabel.setText(QCoreApplication.translate("MainWindow", u"Normal Brakes", None))
        self.BrakeStationPremiumBrakeLabel.setText(QCoreApplication.translate("MainWindow", u"Premium Brakes", None))
        self.BrakeStationChassisInventoryBox.setTitle(QCoreApplication.translate("MainWindow", u"Chassis Inventory", None))
        self.BrakeStationInventoryTotalChassisLabel.setText(QCoreApplication.translate("MainWindow", u"Total Chassis", None))
        ___qtablewidgetitem10 = self.BrakeStationChassisInventoryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Chassis", None));
        ___qtablewidgetitem11 = self.BrakeStationChassisInventoryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Colour", None));
        ___qtablewidgetitem12 = self.BrakeStationChassisInventoryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Pedal", None));
        ___qtablewidgetitem13 = self.BrakeStationChassisInventoryTable.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Gear", None));
        ___qtablewidgetitem14 = self.BrakeStationChassisInventoryTable.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Chain", None));
        ___qtablewidgetitem15 = self.BrakeStationChassisInventoryTable.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Wheels", None));
        self.BrakeAssemblyBox.setTitle(QCoreApplication.translate("MainWindow", u"Brake Assembly", None))
        self.BrakeAssemblyGearValue.setText(QCoreApplication.translate("MainWindow", u"[Gear Type]", None))
        self.BrakeAssemblyWheelValue.setText(QCoreApplication.translate("MainWindow", u"[Wheel Type]", None))
        self.BrakeAssemblyChainLabel.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.BrakeAssemblyBrakeLabel.setText(QCoreApplication.translate("MainWindow", u"Brake Type:", None))
        self.BrakeAssemblyColourLabel.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.BrakeAssemblyGearLabel.setText(QCoreApplication.translate("MainWindow", u"Gear Type:", None))
        self.BrakeAssemblyBrakeValue.setText(QCoreApplication.translate("MainWindow", u"[Brake Type]", None))
        self.BrakeAssemblyChassisLabel.setText(QCoreApplication.translate("MainWindow", u"Chassis Type:", None))
        self.BrakeAssemblyAssembledButton.setText(QCoreApplication.translate("MainWindow", u"Brakes Assembled", None))
        self.BrakeAssemblyWheelLabel.setText(QCoreApplication.translate("MainWindow", u"Wheel Type:", None))
        self.BrakeAssemblyChassisType.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.BrakeAssemblyChainValue.setText(QCoreApplication.translate("MainWindow", u"[Chain Type]", None))
        self.BrakeAssemblyColourValue.setText(QCoreApplication.translate("MainWindow", u"[Colour]", None))
        self.BrakeAssemblyPedalValue.setText(QCoreApplication.translate("MainWindow", u"[Pedal Type]", None))
        self.BrakeAssemblyPedalLabel.setText(QCoreApplication.translate("MainWindow", u"Pedal Type", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BrakeAssembly), QCoreApplication.translate("MainWindow", u"Brakes", None))
        self.LightsOrder.setTitle(QCoreApplication.translate("MainWindow", u"Order Information", None))
        self.BikeTypeLabel_9.setText(QCoreApplication.translate("MainWindow", u"Bike Type:", None))
        self.PartsLabel_9.setText(QCoreApplication.translate("MainWindow", u"Parts", None))
        self.BrakesType_9.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.GearType_9.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.ColourLabel_9.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.OrderNumberLabel_9.setText(QCoreApplication.translate("MainWindow", u"Order Number:", None))
        self.GearsLabel_9.setText(QCoreApplication.translate("MainWindow", u"Gears", None))
        self.Colour_9.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.BrakesLabel_9.setText(QCoreApplication.translate("MainWindow", u"Brakes", None))
        self.PedalType_9.setText(QCoreApplication.translate("MainWindow", u"Pedal Type", None))
        self.PedalLabel_9.setText(QCoreApplication.translate("MainWindow", u"Pedals", None))
        self.ChainType_9.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.SeatLabel_9.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.LightsLabel_9.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.LightsType_9.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.BikeType_9.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.ChainLabel_9.setText(QCoreApplication.translate("MainWindow", u"Chains", None))
        self.SeatType_9.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.OrderNumber_9.setText(QCoreApplication.translate("MainWindow", u"[Order Number]", None))
        self.WheelsLabel_9.setText(QCoreApplication.translate("MainWindow", u"Wheels", None))
        self.WheelType_9.setText(QCoreApplication.translate("MainWindow", u"Wheel Type:", None))
        self.ChassisStationInventoryBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Station Inventory", None))
        self.PedalStationChassisInventoryBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Lights Inventory", None))
        self.PedalStationInventoryTotalChassisLabel_11.setText(QCoreApplication.translate("MainWindow", u"Total Lights", None))
        self.PedalStationInventoryNormalChassisLabel_8.setText(QCoreApplication.translate("MainWindow", u"Normal Lights", None))
        self.PedalStationInventoryTotalKidsChassisLabel_16.setText(QCoreApplication.translate("MainWindow", u"Premium LEDs", None))
        self.PedalStationChassisInventoryBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Chassis Inventory", None))
        self.PedalStationInventoryTotalChassisLabel_12.setText(QCoreApplication.translate("MainWindow", u"Total Chassis", None))
        ___qtablewidgetitem16 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Chassis", None));
        ___qtablewidgetitem17 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Colour", None));
        ___qtablewidgetitem18 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Pedal", None));
        ___qtablewidgetitem19 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Gear", None));
        ___qtablewidgetitem20 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Chain", None));
        ___qtablewidgetitem21 = self.tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Wheels", None));
        ___qtablewidgetitem22 = self.tableWidget_5.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Brakes", None));
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Light Assembly", None))
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"Brake Type:", None))
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"[Light Type]", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"[Chain Type]", None))
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"[Colour]", None))
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"[Gear Type]", None))
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"[Wheel Type]", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Lights Assembled", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"Gear Type:", None))
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"Wheel Type:", None))
        self.label_221.setText(QCoreApplication.translate("MainWindow", u"Light Type:", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"Chassis Type:", None))
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"[Brake Type]", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"[Pedal Type]", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Pedal Type", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lightAssembly), QCoreApplication.translate("MainWindow", u"Lights", None))
        self.SeatsOrder.setTitle(QCoreApplication.translate("MainWindow", u"Order Information", None))
        self.PedalType_10.setText(QCoreApplication.translate("MainWindow", u"Pedal Type", None))
        self.SeatLabel_10.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.BikeTypeLabel_10.setText(QCoreApplication.translate("MainWindow", u"Bike Type:", None))
        self.LightsLabel_10.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.Colour_10.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.PedalLabel_10.setText(QCoreApplication.translate("MainWindow", u"Pedals", None))
        self.GearType_10.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.LightsType_10.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.ChainType_10.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.ChainLabel_10.setText(QCoreApplication.translate("MainWindow", u"Chains", None))
        self.BrakesType_10.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.BrakesLabel_10.setText(QCoreApplication.translate("MainWindow", u"Brakes", None))
        self.PartsLabel_10.setText(QCoreApplication.translate("MainWindow", u"Parts", None))
        self.BikeType_10.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.GearsLabel_10.setText(QCoreApplication.translate("MainWindow", u"Gears", None))
        self.OrderNumber_10.setText(QCoreApplication.translate("MainWindow", u"[Order Number]", None))
        self.SeatType_10.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.ColourLabel_10.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.OrderNumberLabel_10.setText(QCoreApplication.translate("MainWindow", u"Order Number:", None))
        self.WheelsLabel_10.setText(QCoreApplication.translate("MainWindow", u"Wheels", None))
        self.WheelType_10.setText(QCoreApplication.translate("MainWindow", u"Wheel Type:", None))
        self.ChassisStationInventoryBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Station Inventory", None))
        self.PedalStationChassisInventoryBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Seat Inventory", None))
        self.PedalStationInventoryTotalKidsChassisLabel_17.setText(QCoreApplication.translate("MainWindow", u"Sports Seats", None))
        self.PedalStationInventoryNormalChassisLabel_9.setText(QCoreApplication.translate("MainWindow", u"Normal Seats", None))
        self.PedalStationInventoryTotalChassisLabel_13.setText(QCoreApplication.translate("MainWindow", u"Total Seats", None))
        self.PedalStationInventoryTotalKidsChassisLabel_18.setText(QCoreApplication.translate("MainWindow", u"Kids Seats", None))
        self.PedalStationInventoryTotalKidsChassisLabel_19.setText(QCoreApplication.translate("MainWindow", u"Premium Seats", None))
        self.PedalStationChassisInventoryBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Chassis Inventory", None))
        self.PedalStationInventoryTotalChassisLabel_14.setText(QCoreApplication.translate("MainWindow", u"Total Chassis", None))
        ___qtablewidgetitem23 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Chassis", None));
        ___qtablewidgetitem24 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Colour", None));
        ___qtablewidgetitem25 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Pedal", None));
        ___qtablewidgetitem26 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Gear", None));
        ___qtablewidgetitem27 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Chain", None));
        ___qtablewidgetitem28 = self.tableWidget_6.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Wheels", None));
        ___qtablewidgetitem29 = self.tableWidget_6.horizontalHeaderItem(6)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Brakes", None));
        ___qtablewidgetitem30 = self.tableWidget_6.horizontalHeaderItem(7)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Lights", None));
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Light Assembly", None))
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"Chain Type:", None))
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"Seat Type:", None))
        self.label_224.setText(QCoreApplication.translate("MainWindow", u"[Bike Type]", None))
        self.label_228.setText(QCoreApplication.translate("MainWindow", u"[Chain Type]", None))
        self.label_234.setText(QCoreApplication.translate("MainWindow", u"[Brake Type]", None))
        self.label_230.setText(QCoreApplication.translate("MainWindow", u"[Gear Type]", None))
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"Chassis Type:", None))
        self.label_226.setText(QCoreApplication.translate("MainWindow", u"[Colour]", None))
        self.label_235.setText(QCoreApplication.translate("MainWindow", u"Light Type:", None))
        self.label_225.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.label_231.setText(QCoreApplication.translate("MainWindow", u"Wheel Type:", None))
        self.label_238.setText(QCoreApplication.translate("MainWindow", u"[Seat Type]", None))
        self.label_233.setText(QCoreApplication.translate("MainWindow", u"Brake Type:", None))
        self.label_232.setText(QCoreApplication.translate("MainWindow", u"[Wheel Type]", None))
        self.label_229.setText(QCoreApplication.translate("MainWindow", u"Gear Type:", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Seat Assembled", None))
        self.label_236.setText(QCoreApplication.translate("MainWindow", u"[Light Type]", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"[Pedal Type]", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Pedal Type", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SeatAssembly), QCoreApplication.translate("MainWindow", u"Seats", None))
        self.Inventory_DashboardGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Inventory Dashboard", None))
        self.Inevntory_RawMaterialsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Raw Materials", None))
        self.Inventory_RawMaterial_Label.setText(QCoreApplication.translate("MainWindow", u"Tubular Steel", None))
        self.Inventory_RawMaterial_Increase.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_Decrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_RawMaterials_PaintGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Paint", None))
        self.Inventory_RawMaterial_BlackPaintLabel.setText(QCoreApplication.translate("MainWindow", u"Black", None))
        self.Inventory_RawMaterial_BlackPaintIncrease.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_BlackPaintDecrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_RawMaterial_BluePaintLabel.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.Inventory_RawMaterial_BluePaintIncrease.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_BluePaintDecrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_RawMaterial_GreenPaintLabel.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.Inventory_RawMaterial_GreenPaintIncrease.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_GreenPaintDecrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_RawMaterial_GreyPaintLabel.setText(QCoreApplication.translate("MainWindow", u"Grey", None))
        self.Inventory_RawMaterial_GreyIncrease.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_GreyPaintDecrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_RawMaterial_OrangePaintLabel.setText(QCoreApplication.translate("MainWindow", u"Orange", None))
        self.Inventory_RawMaterial_OrangePaintIncrease.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_OrangePaintDecrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_RawMaterial_PinkPaintLabel.setText(QCoreApplication.translate("MainWindow", u"Pink", None))
        self.Inventory_RawMaterial_PinkPaintIncrease.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_PinkPaintDecrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_RawMaterial_PurplePaintLabel.setText(QCoreApplication.translate("MainWindow", u"Purple", None))
        self.Inventory_RawMaterial_PurplePaintIncrease.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_PurplePaintDecrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_RawMaterial_RedPaintLabel.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.Inventory_RawMaterial_RedPaintIncrease.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_RedPaintDecrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_RawMaterial_YellowPaintLabel.setText(QCoreApplication.translate("MainWindow", u"Yellow", None))
        self.Inventory_RawMaterial_YellowPaintIncrease.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_YellowPaintDecrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_RawMaterial_WhitePaintLabel.setText(QCoreApplication.translate("MainWindow", u"White", None))
        self.Inventory_RawMaterial_WhitePaintIncrease.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_WhitePaintDecrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_RawMaterial_InventoryControlLabel.setText(QCoreApplication.translate("MainWindow", u"Inventory Controls", None))
        self.Inventory_RawMaterial_InventoryLabel.setText(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.Inventory_RawMaterial_ItemLabel.setText(QCoreApplication.translate("MainWindow", u"Item", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Parts Inventory", None))
        self.PartsInventory_PedalsGroupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Brakes", None))
        self.Inventory_Parts_Pedals_NormalLabel_6.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Inventory_Parts_Pedals_NormalIncrease_6.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_BlackPaintDecrease_7.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_SportsLabel_6.setText(QCoreApplication.translate("MainWindow", u"Sports", None))
        self.Inventory_Parts_Pedals_SportsIncrease_6.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_SportsDecrease_6.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_KidsLabel_6.setText(QCoreApplication.translate("MainWindow", u"Kids", None))
        self.Inventory_Parts_Pedals_KidsIncrease_6.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_KidsDecrease_6.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_PremiumLabel_6.setText(QCoreApplication.translate("MainWindow", u"Premium", None))
        self.Inventory_Parts_Pedals_PremiumIncrease_6.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_PremiumDecrease_6.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.PartsInventory_PedalsGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Wheels", None))
        self.Inventory_Parts_Pedals_NormalIncrease_4.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_KidsIncrease_4.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_KidsDecrease_4.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_PremiumIncrease_4.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_PremiumDecrease_4.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_SportsDecrease_4.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_SportsIncrease_4.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_BlackPaintDecrease_5.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_PremiumLabel_4.setText(QCoreApplication.translate("MainWindow", u"Premium", None))
        self.Inventory_Parts_Pedals_NormalLabel_4.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Inventory_Parts_Pedals_KidsLabel_4.setText(QCoreApplication.translate("MainWindow", u"Kids", None))
        self.Inventory_Parts_Pedals_SportsLabel_4.setText(QCoreApplication.translate("MainWindow", u"Sports", None))
        self.PartsInventory_PedalsGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Gears", None))
        self.Inventory_Parts_Pedals_NormalLabel_2.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Inventory_Parts_Pedals_NormalIncrease_2.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_BlackPaintDecrease_3.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_SportsLabel_2.setText(QCoreApplication.translate("MainWindow", u"Sports", None))
        self.Inventory_Parts_Pedals_SportsIncrease_2.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_SportsDecrease_2.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_KidsLabel_2.setText(QCoreApplication.translate("MainWindow", u"Kids", None))
        self.Inventory_Parts_Pedals_KidsIncrease_2.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_KidsDecrease_2.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_PremiumLabel_2.setText(QCoreApplication.translate("MainWindow", u"Premium", None))
        self.Inventory_Parts_Pedals_PremiumIncrease_2.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_PremiumDecrease_2.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.PartsInventory_PedalsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Pedals", None))
        self.Inventory_Parts_Pedals_NormalLabel.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Inventory_Parts_Pedals_NormalIncrease.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_BlackPaintDecrease_2.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_SportsLabel.setText(QCoreApplication.translate("MainWindow", u"Sports", None))
        self.Inventory_Parts_Pedals_SportsIncrease.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_SportsDecrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_KidsLabel.setText(QCoreApplication.translate("MainWindow", u"Kids", None))
        self.Inventory_Parts_Pedals_KidsIncrease.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_KidsDecrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_PremiumLabel.setText(QCoreApplication.translate("MainWindow", u"Premium", None))
        self.Inventory_Parts_Pedals_PremiumIncrease.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_PremiumDecrease.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.PartsInventory_PedalsGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Seats", None))
        self.Inventory_Parts_Pedals_NormalLabel_5.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Inventory_Parts_Pedals_NormalIncrease_5.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_BlackPaintDecrease_6.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_SportsLabel_5.setText(QCoreApplication.translate("MainWindow", u"Sports", None))
        self.Inventory_Parts_Pedals_SportsIncrease_5.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_SportsDecrease_5.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_KidsLabel_5.setText(QCoreApplication.translate("MainWindow", u"Kids", None))
        self.Inventory_Parts_Pedals_KidsIncrease_5.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_KidsDecrease_5.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_PremiumLabel_5.setText(QCoreApplication.translate("MainWindow", u"Premium", None))
        self.Inventory_Parts_Pedals_PremiumIncrease_5.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_PremiumDecrease_5.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.PartsInventory_PedalsGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Chains", None))
        self.Inventory_RawMaterial_BlackPaintDecrease_4.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_NormalLabel_3.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Inventory_Parts_Pedals_PremiumIncrease_3.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_NormalIncrease_3.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_SportsIncrease_3.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_SportsDecrease_3.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_KidsDecrease_3.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_KidsLabel_3.setText(QCoreApplication.translate("MainWindow", u"Kids", None))
        self.Inventory_Parts_Pedals_PremiumDecrease_3.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_PremiumLabel_3.setText(QCoreApplication.translate("MainWindow", u"Premium", None))
        self.Inventory_Parts_Pedals_SportsLabel_3.setText(QCoreApplication.translate("MainWindow", u"Sports", None))
        self.Inventory_Parts_Pedals_KidsIncrease_3.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.PartsInventory_PedalsGroupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.Inventory_Parts_Pedals_NormalLabel_10.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Inventory_Parts_Pedals_NormalIncrease_10.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_RawMaterial_BlackPaintDecrease_11.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.Inventory_Parts_Pedals_PremiumLabel_10.setText(QCoreApplication.translate("MainWindow", u"Premium LEDs", None))
        self.Inventory_Parts_Pedals_PremiumIncrease_10.setText(QCoreApplication.translate("MainWindow", u"Increase", None))
        self.Inventory_Parts_Pedals_PremiumDecrease_10.setText(QCoreApplication.translate("MainWindow", u"Decrease", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Inventory Statistics", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Orders Page", None))
        ___qtablewidgetitem31 = self.Orders_Table.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Order ID", None));
        ___qtablewidgetitem32 = self.Orders_Table.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Customer ID", None));
        ___qtablewidgetitem33 = self.Orders_Table.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Bike Type", None));
        ___qtablewidgetitem34 = self.Orders_Table.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Colour", None));
        ___qtablewidgetitem35 = self.Orders_Table.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Pedals", None));
        ___qtablewidgetitem36 = self.Orders_Table.horizontalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Gears", None));
        ___qtablewidgetitem37 = self.Orders_Table.horizontalHeaderItem(6)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Chains", None));
        ___qtablewidgetitem38 = self.Orders_Table.horizontalHeaderItem(7)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Wheels", None));
        ___qtablewidgetitem39 = self.Orders_Table.horizontalHeaderItem(8)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Brakes", None));
        ___qtablewidgetitem40 = self.Orders_Table.horizontalHeaderItem(9)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Lights", None));
        ___qtablewidgetitem41 = self.Orders_Table.horizontalHeaderItem(10)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Seat", None));
        self.NewOrderGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"New Order", None))
        self.BikeSelectionGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Bike Selection", None))
        self.NewOrder_BikeTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Bike Type:", None))
        self.NewOrder_BikeTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.NewOrder_BikeTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Sports", None))
        self.NewOrder_BikeTypeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Kids", None))

        self.NewOrder_PartsLabel.setText(QCoreApplication.translate("MainWindow", u"Parts", None))
        self.NewOrder_ColourLabel.setText(QCoreApplication.translate("MainWindow", u"Colour:", None))
        self.NewOrder_ColourComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Black", None))
        self.NewOrder_ColourComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.NewOrder_ColourComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Green", None))
        self.NewOrder_ColourComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Grey", None))
        self.NewOrder_ColourComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Orange", None))
        self.NewOrder_ColourComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Pink", None))
        self.NewOrder_ColourComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Purple", None))
        self.NewOrder_ColourComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Red", None))
        self.NewOrder_ColourComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Yellow", None))
        self.NewOrder_ColourComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"White", None))

        self.NewOrder_PedalLabel.setText(QCoreApplication.translate("MainWindow", u"Pedals", None))
        self.NewOrder_PedalTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.NewOrder_PedalTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Sports", None))
        self.NewOrder_PedalTypeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Kids", None))
        self.NewOrder_PedalTypeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Premium", None))

        self.NewOrder_ChainLabel.setText(QCoreApplication.translate("MainWindow", u"Chains", None))
        self.NewOrder_ChainTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.NewOrder_ChainTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Sports", None))
        self.NewOrder_ChainTypeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Kids", None))
        self.NewOrder_ChainTypeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Premium", None))

        self.NewOrder_GearsLabel.setText(QCoreApplication.translate("MainWindow", u"Gears", None))
        self.NewOrder_GearTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.NewOrder_GearTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Sports", None))
        self.NewOrder_GearTypeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Kids", None))
        self.NewOrder_GearTypeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Premium", None))

        self.NewOrder_WheelsLabel.setText(QCoreApplication.translate("MainWindow", u"Wheels", None))
        self.NewOrder_WheelTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.NewOrder_WheelTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Sports", None))
        self.NewOrder_WheelTypeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Kids", None))
        self.NewOrder_WheelTypeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Premium", None))

        self.NewOrder_BrakesLabel.setText(QCoreApplication.translate("MainWindow", u"Brakes", None))
        self.NewOrder_BrakeTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.NewOrder_BrakeTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Sports", None))
        self.NewOrder_BrakeTypeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Kids", None))
        self.NewOrder_BrakeTypeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Premium", None))

        self.NewOrder_LightsLabel.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.NewOrder_LightTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.NewOrder_LightTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Premium LEDs", None))

        self.NewOrder_SeatLabel.setText(QCoreApplication.translate("MainWindow", u"Seat", None))
        self.NewOrder_SeatTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.NewOrder_SeatTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Sports", None))
        self.NewOrder_SeatTypeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Kids", None))
        self.NewOrder_SeatTypeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Premium", None))

        self.CustomerInformationGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Customer Information", None))
        self.NewOrder_NameLabel.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.NewOrder_EmailLabel.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.NewOrder_PhoneLabel.setText(QCoreApplication.translate("MainWindow", u"Phone:", None))
        self.NewOrder_AddressLine1Label.setText(QCoreApplication.translate("MainWindow", u"Address Line 1:", None))
        self.NewOrder_AddressLine2Label.setText(QCoreApplication.translate("MainWindow", u"Address Line 2:", None))
        self.NewOrder_CityLabel.setText(QCoreApplication.translate("MainWindow", u"City:", None))
        self.NewOrder_PostcodeLabel.setText(QCoreApplication.translate("MainWindow", u"Postcode:", None))
        self.NewOrder_SubmitOrderButton.setText(QCoreApplication.translate("MainWindow", u"Submit Order", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Station Statistics Page", None))
        self.menuBike_Factory_Dashboard.setTitle(QCoreApplication.translate("MainWindow", u"Bike Factory", None))
        self.menuInventory_Management.setTitle(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.menuOrders.setTitle(QCoreApplication.translate("MainWindow", u"Orders", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

