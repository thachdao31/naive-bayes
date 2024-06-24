from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

from PyQt5 import QtWidgets, QtCore, QtGui
import pyodbc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.df = self.connectToDb()
        # Sử dụng DataFrame để thực hiện các tác vụ khác
        self.X = self.df.drop(columns=['infected'])
        self.y = self.df['infected']

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 571, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 100, 1001, 331))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.time = QtWidgets.QPlainTextEdit(self.groupBox)
        self.time.setGeometry(QtCore.QRect(100, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.time.setFont(font)
        self.time.setObjectName("time")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(230, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.trt = QtWidgets.QPlainTextEdit(self.groupBox)
        self.trt.setGeometry(QtCore.QRect(280, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.trt.setFont(font)
        self.trt.setObjectName("trt")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(410, 40, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.age = QtWidgets.QPlainTextEdit(self.groupBox)
        self.age.setGeometry(QtCore.QRect(460, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.age.setFont(font)
        self.age.setObjectName("age")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(590, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.wtkg = QtWidgets.QPlainTextEdit(self.groupBox)
        self.wtkg.setGeometry(QtCore.QRect(670, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wtkg.setFont(font)
        self.wtkg.setObjectName("wtkg")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(810, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.hemo = QtWidgets.QPlainTextEdit(self.groupBox)
        self.hemo.setGeometry(QtCore.QRect(870, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.hemo.setFont(font)
        self.hemo.setObjectName("hemo")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(30, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.homo = QtWidgets.QPlainTextEdit(self.groupBox)
        self.homo.setGeometry(QtCore.QRect(100, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.homo.setFont(font)
        self.homo.setObjectName("homo")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(230, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.drugs = QtWidgets.QPlainTextEdit(self.groupBox)
        self.drugs.setGeometry(QtCore.QRect(280, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.drugs.setFont(font)
        self.drugs.setObjectName("drugs")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(400, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.karnof = QtWidgets.QPlainTextEdit(self.groupBox)
        self.karnof.setGeometry(QtCore.QRect(460, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.karnof.setFont(font)
        self.karnof.setObjectName("karnof")
        self.oprior = QtWidgets.QPlainTextEdit(self.groupBox)
        self.oprior.setGeometry(QtCore.QRect(670, 80, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.oprior.setFont(font)
        self.oprior.setObjectName("oprior")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(600, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.z30 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.z30.setGeometry(QtCore.QRect(870, 80, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.z30.setFont(font)
        self.z30.setObjectName("z30")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(810, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.preanti = QtWidgets.QPlainTextEdit(self.groupBox)
        self.preanti.setGeometry(QtCore.QRect(100, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.preanti.setFont(font)
        self.preanti.setObjectName("preanti")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(30, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(230, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.race = QtWidgets.QPlainTextEdit(self.groupBox)
        self.race.setGeometry(QtCore.QRect(280, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.race.setFont(font)
        self.race.setObjectName("race")
        self.gender = QtWidgets.QPlainTextEdit(self.groupBox)
        self.gender.setGeometry(QtCore.QRect(460, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gender.setFont(font)
        self.gender.setObjectName("gender")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(390, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.str2 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.str2.setGeometry(QtCore.QRect(670, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.str2.setFont(font)
        self.str2.setObjectName("str2")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(600, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.strat = QtWidgets.QPlainTextEdit(self.groupBox)
        self.strat.setGeometry(QtCore.QRect(870, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.strat.setFont(font)
        self.strat.setObjectName("strat")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(800, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.symptom = QtWidgets.QPlainTextEdit(self.groupBox)
        self.symptom.setGeometry(QtCore.QRect(100, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.symptom.setFont(font)
        self.symptom.setObjectName("symptom")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(20, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.treat = QtWidgets.QPlainTextEdit(self.groupBox)
        self.treat.setGeometry(QtCore.QRect(280, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.treat.setFont(font)
        self.treat.setObjectName("treat")
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(220, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.offtrt = QtWidgets.QPlainTextEdit(self.groupBox)
        self.offtrt.setGeometry(QtCore.QRect(460, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.offtrt.setFont(font)
        self.offtrt.setObjectName("offtrt")
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(390, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.cd40 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.cd40.setGeometry(QtCore.QRect(670, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cd40.setFont(font)
        self.cd40.setObjectName("cd40")
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(600, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.cd420 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.cd420.setGeometry(QtCore.QRect(870, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cd420.setFont(font)
        self.cd420.setObjectName("cd420")
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setGeometry(QtCore.QRect(800, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.cd80 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.cd80.setGeometry(QtCore.QRect(100, 270, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cd80.setFont(font)
        self.cd80.setObjectName("cd80")
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setGeometry(QtCore.QRect(30, 280, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.cd820 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.cd820.setGeometry(QtCore.QRect(280, 270, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cd820.setFont(font)
        self.cd820.setObjectName("cd820")
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setGeometry(QtCore.QRect(220, 280, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setGeometry(QtCore.QRect(390, 280, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 450, 1001, 121))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(90, 50, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit_27 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_27.setGeometry(QtCore.QRect(330, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plainTextEdit_27.setFont(font)
        self.plainTextEdit_27.setObjectName("plainTextEdit_27")
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setGeometry(QtCore.QRect(450, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.plainTextEdit_28 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_28.setGeometry(QtCore.QRect(330, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plainTextEdit_28.setFont(font)
        self.plainTextEdit_28.setObjectName("plainTextEdit_28")
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        self.label_30.setGeometry(QtCore.QRect(450, 60, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.naive_bayes)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ứng dụng chẩn đoán bệnh nhân mắc bệnh AIDS"))
        self.groupBox.setTitle(_translate("MainWindow", "Nhập thông tin bệnh nhân"))
        self.label_2.setText(_translate("MainWindow", "1. thời gian"))
        self.label_3.setText(_translate("MainWindow", "2. TRT"))
        self.label_4.setText(_translate("MainWindow", "3. Tuổi"))
        self.label_5.setText(_translate("MainWindow", "4. Cân nặng"))
        self.label_10.setText(_translate("MainWindow", "5. Hemo"))
        self.label_11.setText(_translate("MainWindow", "6. Homo"))
        self.label_12.setText(_translate("MainWindow", "6. Drug"))
        self.label_13.setText(_translate("MainWindow", "7. karnof"))
        self.label_14.setText(_translate("MainWindow", "8. Oprior"))
        self.label_15.setText(_translate("MainWindow", "9. Z30"))
        self.label_16.setText(_translate("MainWindow", "10. preanti"))
        self.label_17.setText(_translate("MainWindow", "11. race"))
        self.label_18.setText(_translate("MainWindow", "12. Gender"))
        self.label_19.setText(_translate("MainWindow", "13. STR2"))
        self.label_20.setText(_translate("MainWindow", "14. Strat"))
        self.label_21.setText(_translate("MainWindow", "15. Symptom"))
        self.label_22.setText(_translate("MainWindow", "16. Treat"))
        self.label_23.setText(_translate("MainWindow", "18. Offtrt"))
        self.label_24.setText(_translate("MainWindow", "19. CD40"))
        self.label_25.setText(_translate("MainWindow", "20. CD420"))
        self.label_26.setText(_translate("MainWindow", "21. CD80"))
        self.label_27.setText(_translate("MainWindow", "22. CD820"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Kết quả chẩn đoán"))
        self.pushButton.setText(_translate("MainWindow", "Chấn đoán"))
        self.label_29.setText(_translate("MainWindow", "% người bệnh mắc bệnh"))
        self.label_30.setText(_translate("MainWindow", "% người bệnh không mắc bệnh"))

    # def predict(self):
        # Bước 6: Nhập dữ liệu của bệnh nhân mới
        return {
            'time': self.time.toPlainText(),
            'trt': self.trt.toPlainText(),
            'age': self.age.toPlainText(),
            'wtkg': self.wtkg.toPlainText(),
            'hemo': self.hemo.toPlainText(),
            'homo': self.homo.toPlainText(),
            'drugs': self.drugs.toPlainText(),
            'karnof': self.karnof.toPlainText(),
            'oprior': self.oprior.toPlainText(),
            'z30': self.z30.toPlainText(),
            'preanti': self.preanti.toPlainText(),
            'race': self.race.toPlainText(),
            'gender': self.gender.toPlainText(),
            'str2': self.str2.toPlainText(),
            'strat': self.strat.toPlainText(),
            'symptom': self.symptom.toPlainText(),
            'treat': self.treat.toPlainText(),
            'offtrt': self.offtrt.toPlainText(),
            'cd40': self.cd40.toPlainText(),
            'cd420': self.cd420.toPlainText(),
            'cd80': self.cd80.toPlainText(),
            'cd820': self.cd820.toPlainText()
        }

    def naive_bayes(self):
        # Bước 3: Chia dữ liệu thành tập huấn luyện và tập kiểm tra
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        # Bước 4: Triển khai mô hình Naive Bayes Gauss và huấn luyện
        model = GaussianNB()
        model.fit(X_train, y_train)

        # Bước 5: Dự đoán trên tập kiểm tra và đánh giá mô hình
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Hiển thị kết quả
        # print("Accuracy:", accuracy)
        # print("Classification Report:\n", classification_report(y_test, y_pred))


        # Bước 6: Nhập dữ liệu của bệnh nhân mới
        new_patient = {
            'time': self.time.toPlainText(),
            'trt': self.trt.toPlainText(),
            'age': self.age.toPlainText(),
            'wtkg': self.wtkg.toPlainText(),
            'hemo': self.hemo.toPlainText(),
            'homo': self.homo.toPlainText(),
            'drugs': self.drugs.toPlainText(),
            'karnof': self.karnof.toPlainText(),
            'oprior': self.oprior.toPlainText(),
            'z30': self.z30.toPlainText(),
            'preanti': self.preanti.toPlainText(),
            'race': self.race.toPlainText(),
            'gender': self.gender.toPlainText(),
            'str2': self.str2.toPlainText(),
            'strat': self.strat.toPlainText(),
            'symptom': self.symptom.toPlainText(),
            'treat': self.treat.toPlainText(),
            'offtrt': self.offtrt.toPlainText(),
            'cd40': self.cd40.toPlainText(),
            'cd420': self.cd420.toPlainText(),
            'cd80': self.cd80.toPlainText(),
            'cd820': self.cd820.toPlainText()
        }

        # Chuyển đổi dữ liệu bệnh nhân mới thành DataFrame
        new_patient_df = pd.DataFrame([new_patient])

        # Bước 7: Dự đoán khả năng mắc bệnh của bệnh nhân mới
        # làm tròn để hiển thị kết quả theo %
        new_patient_pred = np.round(model.predict(new_patient_df)*100, 2)
        new_patient_proba = np.round(model.predict_proba(new_patient_df)*100, 2)

        # Hiển thị kết quả dự đoán
        print("Prediction for new patient:", new_patient_pred[0])
        print("Probability of being infected:", new_patient_proba[0][1])
        print("Probability of not being infected:", new_patient_proba[0][0])
        self.plainTextEdit_27.setPlainText(str(new_patient_proba[0][1]))
        self.plainTextEdit_28.setPlainText(str(new_patient_proba[0][0]))

    def connectToDb(self):
        # Thông tin kết nối SQL Server
        server = 'localhost'
        database = 'naive_bayes'
        conn = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;')
        sql_query = "SELECT * FROM dbo.aids"
        df = pd.read_sql(sql_query, conn)
        return df


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    