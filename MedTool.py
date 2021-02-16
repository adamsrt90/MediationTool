#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime, os, sys, re, PyQt5, openpyxl 
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


# In[2]:


starttime = str(datetime.datetime.now())
print(f'Mediation started on {starttime}!')
demands = []
offers = []
offertime = []
demandtime = []
mediationinfo = []
data = {"Demands": demands,
        "Demand_Time": demandtime,
       "Offers": offers,
       "Offer_Time": offertime}
counter = 0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1191, 837)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(613, 491))
        MainWindow.setMaximumSize(QtCore.QSize(1700, 1500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formLayout.setObjectName("formLayout")
        self.cASENUMBERLabel = QtWidgets.QLabel(self.centralwidget)
        self.cASENUMBERLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.cASENUMBERLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.cASENUMBERLabel.setObjectName("cASENUMBERLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.cASENUMBERLabel)
        self.cASENUMBERLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.cASENUMBERLineEdit.setObjectName("cASENUMBERLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cASENUMBERLineEdit)
        self.mEDIATORLabel = QtWidgets.QLabel(self.centralwidget)
        self.mEDIATORLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mEDIATORLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mEDIATORLabel.setObjectName("mEDIATORLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.mEDIATORLabel)
        self.mEDIATORLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.mEDIATORLineEdit.setObjectName("mEDIATORLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mEDIATORLineEdit)
        self.pLAINTIFFSATTORNEYLabel = QtWidgets.QLabel(self.centralwidget)
        self.pLAINTIFFSATTORNEYLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.pLAINTIFFSATTORNEYLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pLAINTIFFSATTORNEYLabel.setObjectName("pLAINTIFFSATTORNEYLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pLAINTIFFSATTORNEYLabel)
        self.pLAINTIFFSATTORNEYLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pLAINTIFFSATTORNEYLineEdit.setObjectName("pLAINTIFFSATTORNEYLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pLAINTIFFSATTORNEYLineEdit)
        self.pushButtonForm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonForm.setMinimumSize(QtCore.QSize(3, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonForm.setFont(font)
        self.pushButtonForm.setObjectName("pushButtonForm")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButtonForm)
        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButtonSave)
        self.horizontalLayout_3.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(10, 61, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_3.addWidget(self.listWidget)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineDemand1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineDemand1.setObjectName("lineDemand1")
        self.verticalLayout.addWidget(self.lineDemand1)
        self.pushButtonDemand1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDemand1.setObjectName("pushButtonDemand1")
        self.verticalLayout.addWidget(self.pushButtonDemand1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineOffer1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineOffer1.setObjectName("lineOffer1")
        self.verticalLayout_2.addWidget(self.lineOffer1)
        self.pushButtonOffer1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOffer1.setObjectName("pushButtonOffer1")
        self.verticalLayout_2.addWidget(self.pushButtonOffer1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem4)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(['Type','Amount','Time','Mid-Point'])
        self.tableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(900, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_5.addWidget(self.buttonBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.onlyInt = QtGui.QIntValidator()
        self.lineDemand1.setValidator(self.onlyInt)
        self.lineOffer1.setValidator(self.onlyInt)
        self.retranslateUi(MainWindow)
        self.pushButtonSave.clicked.connect(self.mediation_info)
        self.pushButtonForm.clicked.connect(self.listWidget.clear)
        self.pushButtonForm.clicked.connect(self.pLAINTIFFSATTORNEYLineEdit.clear)
        self.pushButtonForm.clicked.connect(self.mEDIATORLineEdit.clear)
        self.pushButtonForm.clicked.connect(self.cASENUMBERLineEdit.clear)
        self.buttonBox.rejected.connect(self.tableWidget.clearContents)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButtonForm.clicked.connect(self.listWidget.reset)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.buttonBox.rejected.connect(self.clear_data)
        self.buttonBox.rejected.connect(self.tableWidget.clearContents)
        self.buttonBox.accepted.connect(self.final_offers)
        self.pushButtonDemand1.clicked.connect(self.demand_update)
        self.pushButtonOffer1.clicked.connect(self.offer_update)
        self.pushButtonOffer1.clicked.connect(self.mid_point)
        self.pushButtonOffer1.clicked.connect(self.round_counter)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
      

   
    def mediation_info(self):
        '''grabs the mediation information from the
        form in the top left'''
        mediationinfo.append(self.cASENUMBERLineEdit.text())
        mediationinfo.append(self.mEDIATORLineEdit.text())
        mediationinfo.append(self.pLAINTIFFSATTORNEYLineEdit.text())
        
        if not self.cASENUMBERLineEdit.text() or not self.mEDIATORLineEdit or not self.pLAINTIFFSATTORNEYLineEdit:
            print("Please complete the form in the top left.")
        else:
            self.listWidget.addItem(self.cASENUMBERLineEdit.text())
            self.listWidget.addItem(self.mEDIATORLineEdit.text())
            self.listWidget.addItem(self.pLAINTIFFSATTORNEYLineEdit.text())
        
        
    def demand_update(self):
        '''updates the demand list of global variables.
        adds the dollar amount and time the demand was made to the demand list
        adds demand to list in order that the demand was made
        will use the form data to fill in demand argument'''
        demtime = str(datetime.datetime.now())
        dem = int(self.lineDemand1.text())
        print(f'This is the current demand and time {dem} {demtime.split()[1]}')
        demands.append(dem)
        demandtime.append(demtime.split()[1])
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition,0, QtWidgets.QTableWidgetItem('Demand'))
        self.tableWidget.setItem(rowPosition,1, QtWidgets.QTableWidgetItem(f'${dem}'))
        self.tableWidget.setItem(rowPosition,2, QtWidgets.QTableWidgetItem(demtime.split()[1]))
        

    def offer_update(self):
        '''updates the offer list of global variables
        adds the dollar amount and time the offer was made to the offer list
        adds offer to list in order that offer was made
        will use the form data to fill in offer argument'''
        offtime = str(datetime.datetime.now())
        off = int(self.lineOffer1.text())
        print(f'This is the current offer and time {off} {offtime.split()[1]}')
        offers.append(off)
        offertime.append(offtime.split()[1])
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition,0, QtWidgets.QTableWidgetItem('Offer'))
        self.tableWidget.setItem(rowPosition,1, QtWidgets.QTableWidgetItem(f'${off}'))
        self.tableWidget.setItem(rowPosition,2, QtWidgets.QTableWidgetItem(offtime.split()[1]))
        
    
    def mid_point(self):
        '''Will calculate the mid point between the latest demand and
        the later offer'''
        midTime = str(datetime.datetime.now())
        midPoint = (offers[-1] + demands[-1])/2
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition,0, QtWidgets.QTableWidgetItem('MidPoint'))
        self.tableWidget.setItem(rowPosition,1, QtWidgets.QTableWidgetItem('N/A'))
        self.tableWidget.setItem(rowPosition,2, QtWidgets.QTableWidgetItem(midTime.split()[1]))
        self.tableWidget.setItem(rowPosition,3, QtWidgets.QTableWidgetItem(f'${midPoint}'))
    
    def round_counter(self):
        '''Will keep track of the rounds of demands and offers
        uses the global variables for the counter'''
        global counter
        counter = counter +1
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition,0, QtWidgets.QTableWidgetItem(f'Round {counter}'))
        self.tableWidget.setItem(rowPosition,1, QtWidgets.QTableWidgetItem('N/A'))
        self.tableWidget.setItem(rowPosition,2, QtWidgets.QTableWidgetItem('N/A'))
        self.tableWidget.setItem(rowPosition,3, QtWidgets.QTableWidgetItem('N/A'))
        
    def final_offers(self): 
        '''
        Checks all fields are entered
        checks if DataFrames are equal length
        will save excel sheet to default directory
        '''
        case = str(self.cASENUMBERLineEdit.text())
        mediator = str(self.mEDIATORLineEdit.text())
        pltatt = str(self.pLAINTIFFSATTORNEYLineEdit.text())
        sheet_name = f'Mediation {mediator} and {pltatt}'
        sheet_info = sheet_name[:30] #sheet name cannot be longer than 31 characters
                                        
        if not case or not mediator or not pltatt:
            print("Please input the case number, mediator, or Plaintiff's Attorney")
        else:
            try:
                if len(data['Demands']) < len(data["Offers"]):
                    new_data = (len(data["Offers"]) - len(data['Demands']))
                    for i in range(0, new_data):
                        data['Demands'].append(i)
                        data['Demand_Time'].append(i)
                elif len(data['Offers']) < len(data['Demands']):
                    new_data = (len(data["Demands"]) - len(data['Offers']))
                    for i in range(0, new_data):
                        data['Offers'].append(i)
                        data['Offer_Time'].append(i)
                else:
                    df1 = pd.DataFrame(data)
                    df1['Start Time'] = starttime
                    df1['End Time'] = str(datetime.datetime.now())
                    df1.to_excel(case +".xlsx", sheet_name = sheet_info)
                    sys.exit(app.exec_())
            except Exception:
                pass
                

    
    def clear_data(self):
        '''sets the list variables to global and allows them to be cleared if mistakes were input'''
        global demands, offers, offertime, demandtime, data,df1, counter, mediationinfo
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        demands = []
        offers = []
        offertime = []
        demandtime = []
        mediationinfo = []
        data = {"Demands": demands,
                "Demand_Time": demandtime,
               "Offers": offers,
               "Offer_Time": offertime}
        df1 = pd.DataFrame(data)
        counter = 0
        print("All fields have been cleared")
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mediation Tracker"))
        self.cASENUMBERLabel.setText(_translate("MainWindow", "CASE NUMBER"))
        self.mEDIATORLabel.setText(_translate("MainWindow", "MEDIATOR"))
        self.pLAINTIFFSATTORNEYLabel.setText(_translate("MainWindow", "PLAINTIFF\'S ATTORNEY"))
        self.pushButtonForm.setText(_translate("MainWindow", "Clear Form"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save Information"))
        self.label.setText(_translate("MainWindow", "DEMAND"))
        self.pushButtonDemand1.setText(_translate("MainWindow", "Set Demand"))
        self.label_2.setText(_translate("MainWindow", "OFFER"))
        self.pushButtonOffer1.setText(_translate("MainWindow", "Set Offer"))



# In[3]:


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())


# In[ ]:




