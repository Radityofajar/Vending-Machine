        global dataList
        for i in range(0, 28):
            data = (ser.readline().split()[0].decode("ascii"))
            dataList[i] = data        
        
        self.stok1 = QPushButton(self.centralwidget)
        self.stok1.setGeometry(QRect(20, 200, 200, 200))
        self.stok1.setObjectName("stok1")
        if (dataList[0] == '0'):
            self.stok1.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px; background-image : url(img/stok1.jpg);")
            self.stok1.resize(200, 200)
            stok_1 = 'a'
            self.stok1.clicked.connect(lambda: self.clickme(stok_1))
            self.stok1.clicked.connect(self.funcPaymentSys)
        else:
            self.stok1.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px; background-image : url(img/no.jpg);")
            self.stok1.resize(200, 200)

        self.stok2 = QPushButton(self.centralwidget)
        self.stok2.setGeometry(QRect(300, 200, 200, 200))
        self.stok2.setObjectName("stok2")
        if (dataList[1] == '0'):
            self.stok2.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok2.jpg);")
            self.stok2.resize(200, 200)
            stok_2 = 'b'
            self.stok2.clicked.connect(lambda: self.clickme(stok_2))
            self.stok2.clicked.connect(self.funcPaymentSys)
        else:
            self.stok2.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok2.resize(200, 200)

        self.stok3 = QPushButton(self.centralwidget)
        self.stok3.setGeometry(QRect(580, 200, 200, 200))
        self.stok3.setObjectName("stok3")
        if (dataList[2] == '0'):
            self.stok3.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok3.jpg);")
            self.stok3.resize(200, 200)
            stok_3 = 'c'
            self.stok3.clicked.connect(lambda: self.clickme(stok_3))
            self.stok3.clicked.connect(self.funcPaymentSys)
        else:
            self.stok3.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok3.resize(200, 200)

        self.stok4 = QPushButton(self.centralwidget)
        self.stok4.setGeometry(QRect(860, 200, 200, 200))
        self.stok4.setObjectName("stok4")
        if (dataList[3] == '0'):
            self.stok4.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px; background-image : url(img/stok4.jpg);")
            self.stok4.resize(200, 200)
            stok_4 = 'd'
            self.stok4.clicked.connect(lambda: self.clickme(stok_4))
            self.stok4.clicked.connect(self.funcPaymentSys)
        else:
            self.stok4.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px; background-image : url(img/no.jpg);")
            self.stok4.resize(200, 200)

        self.stok5 = QPushButton(self.centralwidget)
        self.stok5.setGeometry(QRect(20, 445, 200, 200))
        self.stok5.setObjectName("stok5")
        if (dataList[4] == '0'):
            self.stok5.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok5.jpg);")
            self.stok5.resize(200, 200)
            stok_5 = 'e'
            self.stok5.clicked.connect(lambda: self.clickme(stok_5))
            self.stok5.clicked.connect(self.funcPaymentSys)
        else:
            self.stok5.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok5.jpg);")
            self.stok5.resize(200, 200)

        self.stok6 = QPushButton(self.centralwidget)
        self.stok6.setGeometry(QRect(300, 445, 200, 200))
        self.stok6.setObjectName("stok6")
        if (dataList[5] == '0'):
            self.stok6.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok6.jpg);")
            self.stok6.resize(200, 200)
            stok_6 = 'f'
            self.stok6.clicked.connect(lambda: self.clickme(stok_6))
            self.stok6.clicked.connect(self.funcPaymentSys)
        else:
            self.stok6.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok6.resize(200, 200)

        self.stok7 = QPushButton(self.centralwidget)
        self.stok7.setGeometry(QRect(580, 445, 200, 200))
        self.stok7.setObjectName("stok7")
        if (dataList[6] == '0'):
            self.stok7.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok7.jpg);")
            self.stok7.resize(200, 200)
            stok_7 = 'g'
            self.stok7.clicked.connect(lambda: self.clickme(stok_7))
            self.stok7.clicked.connect(self.funcPaymentSys)
        else:
            self.stok7.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok7.resize(200, 200)

        self.stok8 = QPushButton(self.centralwidget)
        self.stok8.setGeometry(QRect(860, 445, 200, 200))
        self.stok8.setObjectName("stok8")
        if (dataList[7] == '0'):
            self.stok8.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok8.jpg);")
            self.stok8.resize(200, 200)
            stok_8 = 'h'
            self.stok8.clicked.connect(lambda: self.clickme(stok_8))
            self.stok8.clicked.connect(self.funcPaymentSys)
        else:
            self.stok8.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok8.resize(200, 200)

        self.stok9 = QPushButton(self.centralwidget)
        self.stok9.setGeometry(QRect(20, 690, 200, 200))
        self.stok9.setObjectName("stok9")
        if (dataList[8] == '0'):
            self.stok9.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok9.jpg);")
            self.stok9.resize(200, 200)
            stok_9 = 'i'
            self.stok9.clicked.connect(lambda: self.clickme(stok_9))
            self.stok9.clicked.connect(self.funcPaymentSys)
        else:
            self.stok9.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok9.resize(200, 200)

        self.stok10 = QPushButton(self.centralwidget)
        self.stok10.setGeometry(QRect(300, 690, 200, 200))
        self.stok10.setObjectName("stok10")
        if (dataList[9] == '0'):
            self.stok10.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok10.jpg);")
            self.stok10.resize(200, 200)
            stok_10 = 'j'
            self.stok10.clicked.connect(lambda: self.clickme(stok_10))
            self.stok10.clicked.connect(self.funcPaymentSys)
        else:
            self.stok10.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok10.resize(200, 200)

        self.stok11 = QPushButton(self.centralwidget)
        self.stok11.setGeometry(QRect(580, 690, 200, 200))
        self.stok11.setObjectName("stok11")
        if (dataList[10] == '0'):
            self.stok11.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok11.jpg);")
            self.stok11.resize(200, 200)
            stok_11 = 'k'
            self.stok11.clicked.connect(lambda: self.clickme(stok_11))
            self.stok11.clicked.connect(self.funcPaymentSys)
        else:
            self.stok11.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok11.resize(200, 200)

        self.stok12 = QPushButton(self.centralwidget)
        self.stok12.setGeometry(QRect(860, 690, 200, 200))
        self.stok12.setObjectName("stok12")
        if (dataList[11] == '0'):
            self.stok12.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok12.jpg);")
            self.stok12.resize(200, 200)
            stok_12 = 'l'
            self.stok12.clicked.connect(lambda: self.clickme(stok_12))
            self.stok12.clicked.connect(self.funcPaymentSys)
        else:
            self.stok12.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok12.resize(200, 200)

        self.stok13 = QPushButton(self.centralwidget)
        self.stok13.setGeometry(QRect(20, 935, 200, 200))
        self.stok13.setObjectName("stok13")
        if (dataList[12] == '0'):
            self.stok13.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok13.jpg);")
            self.stok13.resize(200, 200)
            stok_13 = 'm'
            self.stok13.clicked.connect(lambda: self.clickme(stok_13))
            self.stok13.clicked.connect(self.funcPaymentSys)
        else:
            self.stok13.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok13.resize(200, 200)

        self.stok14 = QPushButton(self.centralwidget)
        self.stok14.setGeometry(QRect(300, 935, 200, 200))
        self.stok14.setObjectName("stok14")
        if (dataList[13] == '0'):
            self.stok14.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok14.jpg);")
            self.stok14.resize(200, 200)
            stok_14 = 'n'
            self.stok14.clicked.connect(lambda: self.clickme(stok_14))
            self.stok14.clicked.connect(self.funcPaymentSys)
        else:
            self.stok14.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok14.resize(200, 200)

        self.stok15 = QPushButton(self.centralwidget)
        self.stok15.setGeometry(QRect(580, 935, 200, 200))
        self.stok15.setObjectName("stok15")
        if (dataList[14] == '0'):
            self.stok15.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok15.jpg);")
            self.stok15.resize(200, 200)
            stok_15 = 'o'
            self.stok15.clicked.connect(lambda: self.clickme(stok_15))
            self.stok15.clicked.connect(self.funcPaymentSys)
        else:
            self.stok15.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok15.resize(200, 200)

        self.stok16 = QPushButton(self.centralwidget)
        self.stok16.setGeometry(QRect(860, 935, 200, 200))
        self.stok16.setObjectName("stok16")
        if (dataList[15] == '0'):
            self.stok16.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok16.jpg);")
            self.stok16.resize(200, 200)
            stok_16 = 'p'
            self.stok16.clicked.connect(lambda: self.clickme(stok_16))
            self.stok16.clicked.connect(self.funcPaymentSys)
        else:
            self.stok16.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok16.resize(200, 200)

        self.stok17 = QPushButton(self.centralwidget)
        self.stok17.setGeometry(QRect(20, 1180, 200, 200))
        self.stok17.setObjectName("stok17")
        if (dataList[16] == '0'):
            self.stok17.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok17.jpg);")
            self.stok17.resize(200, 200)
            stok_17 = 'q'
            self.stok17.clicked.connect(lambda: self.clickme(stok_17))
            self.stok17.clicked.connect(self.funcPaymentSys)
        else:
            self.stok17.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok17.resize(200, 200)

        self.stok18 = QPushButton(self.centralwidget)
        self.stok18.setGeometry(QRect(300, 1180, 200, 200))
        self.stok18.setObjectName("stok18")
        if (dataList[17] == '0'):
            self.stok18.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok18.jpg);")
            self.stok18.resize(200, 200)
            stok_18 = 'r'
            self.stok18.clicked.connect(lambda: self.clickme(stok_18))
            self.stok18.clicked.connect(self.funcPaymentSys)
        else:
            self.stok18.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok18.resize(200, 200)

        self.stok19 = QPushButton(self.centralwidget)
        self.stok19.setGeometry(QRect(580, 1180, 200, 200))
        self.stok19.setObjectName("stok19")
        if (dataList[18] == '0'):
            self.stok19.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok19.jpg);")
            self.stok19.resize(200, 200)
            stok_19 = 's'
            self.stok19.clicked.connect(lambda: self.clickme(stok_19))
            self.stok19.clicked.connect(self.funcPaymentSys)
        else:
            self.stok19.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok19.resize(200, 200)

        self.stok20 = QPushButton(self.centralwidget)
        self.stok20.setGeometry(QRect(860, 1180, 200, 200))
        self.stok20.setObjectName("stok20")
        if (dataList[19] == '0'):
            self.stok20.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok20.jpg);")
            self.stok20.resize(200, 200)
            stok_20 = 't'
            self.stok20.clicked.connect(lambda: self.clickme(stok_20))
            self.stok20.clicked.connect(self.funcPaymentSys)
        else:
            self.stok20.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok20.resize(200, 200)

        self.stok21 = QPushButton(self.centralwidget)
        self.stok21.setGeometry(QRect(20, 1425, 200, 200))
        self.stok21.setObjectName("stok21")
        if (dataList[20] == '0'):
            self.stok21.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok21.jpg);")
            self.stok21.resize(200, 200)
            stok_21 = 'u'
            self.stok21.clicked.connect(lambda: self.clickme(stok_21))
            self.stok21.clicked.connect(self.funcPaymentSys)
        else:
            self.stok21.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok21.resize(200, 200)

        self.stok22 = QPushButton(self.centralwidget)
        self.stok22.setGeometry(QRect(300, 1425, 200, 200))
        self.stok22.setObjectName("stok22")
        if (dataList[21] == '0'):
            self.stok22.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok22.jpg);")
            self.stok22.resize(200, 200)
            stok_22 = 'v'
            self.stok22.clicked.connect(lambda: self.clickme(stok_22))
            self.stok22.clicked.connect(self.funcPaymentSys)
        else:
            self.stok22.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok22.resize(200, 200)

        self.stok23 = QPushButton(self.centralwidget)
        self.stok23.setGeometry(QRect(580, 1425, 200, 200))
        self.stok23.setObjectName("stok23")
        if (dataList[22] == '0'):
            self.stok23.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok23.jpg);")
            self.stok23.resize(200, 200)
            stok_23 = 'w'
            self.stok23.clicked.connect(lambda: self.clickme(stok_23))
            self.stok23.clicked.connect(self.funcPaymentSys)
        else:
            self.stok23.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok23.resize(200, 200)

        self.stok24 = QPushButton(self.centralwidget)
        self.stok24.setGeometry(QRect(860, 1425, 200, 200))
        self.stok24.setObjectName("stok24")
        if (dataList[23] == '0'):
            self.stok24.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok24.jpg);")
            self.stok24.resize(200, 200)
            stok_24 = 'x'
            self.stok24.clicked.connect(lambda: self.clickme(stok_24))
            self.stok24.clicked.connect(self.funcPaymentSys)
        else:
            self.stok24.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok24.resize(200, 200)

        self.stok25 = QPushButton(self.centralwidget)
        self.stok25.setGeometry(QRect(20, 1670, 200, 200))
        self.stok25.setObjectName("stok25")
        if (dataList[24] == '0'):
            self.stok25.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok25.jpg);")
            self.stok25.resize(200, 200)
            stok_25 = 'y'
            self.stok25.clicked.connect(lambda: self.clickme(stok_25))
            self.stok25.clicked.connect(self.funcPaymentSys)
        else:
            self.stok25.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok25.resize(200, 200)

        self.stok26 = QPushButton(self.centralwidget)
        self.stok26.setGeometry(QRect(300, 1670, 200, 200))
        self.stok26.setObjectName("stok26")
        if (dataList[25] == '0'):
            self.stok26.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok26.jpg);")
            self.stok26.resize(200, 200)
            stok_26 = 'z'
            self.stok26.clicked.connect(lambda: self.clickme(stok_26))
            self.stok26.clicked.connect(self.funcPaymentSys)
        else:
            self.stok26.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok26.resize(200, 200)

        self.stok27 = QPushButton(self.centralwidget)
        self.stok27.setGeometry(QRect(580, 1670, 200, 200))
        self.stok27.setObjectName("stok27")
        if (dataList[26] == '0'):
            self.stok27.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok27.jpg);")
            self.stok27.resize(200, 200)
            stok_27 = 'A'
            self.stok27.clicked.connect(lambda: self.clickme(stok_27))
            self.stok27.clicked.connect(self.funcPaymentSys)
        else:
            self.stok27.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok27.resize(200, 200)

        self.stok28 = QPushButton(self.centralwidget)
        self.stok28.setGeometry(QRect(860, 1670, 200, 200))
        self.stok28.setObjectName("stok28")
        if (dataList[27] == '0'):
            self.stok28.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok28.jpg);")
            self.stok28.resize(200, 200)
            stok_28 = 'B'
            self.stok28.clicked.connect(lambda: self.clickme(stok_28))
            self.stok28.clicked.connect(self.funcPaymentSys)
        else:
            self.stok28.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok28.resize(200, 200)
