class Bankomat:
    def __init__(self, karta):
        self.__sum = 50000000
        self.karta = karta
        self.num = karta.num
        self.muddat = karta.muddat
        self.ruxsat = False
        self.urun = 3

    def pin(self):
        if int(str(self.muddat).split(".")[1]) > 2023:
            while True:
                if self.urun == 0:
                    print("Xato urunishlaringiz soni 3 taga yetdi. Kartangiz bloklandi!!!\nBankimiz ofislariga tashrif buyurishingizni so'raymiz!")
                    exit()
                if int(input("Parolni kiriting: ")) == self.karta.getPin():
                    self.ruxsat = True
                    break
                self.urun -= 1
        else: 
            print("Kartangiz muddati tugagan. Biz uni blokladik.\nKartangizni yangisiga almashtirish uchun bankimiz ofislariga tashrif buyuring!")


    def menyu(self):
        if self.ruxsat:
            print("""
1 - Balans                           2 - Naqd pul
3 - Karta parolini o'zgartir         4 - Sms xabarnomani ulash
5 - Ortga                            6 - Chiqish""")
            buyruq  = int(input(">>> "))
            if buyruq == 1:
                print(self.balans())
            elif buyruq == 2:
                self.naqdPul()
            elif buyruq == 3:
                self.changePin()
            elif buyruq == 4:
                pass
            elif buyruq == 5:
                self.back()
            else:
                exit()


    def balans(self):
        return self.karta.getBalans()
    
    def naqdPul(self):
        summa = int(input("Pul miqdorini kiriting: "))
        if summa < self.karta.getBalans():
            self.__sum -= summa
            self.karta.setBalans(summa)
            print("Pul muvaffaqiyatli yechildi.")
        else: 
            print("Kartangizda mul qidori yetarli emas!!!")

        
    def changePin(self):
        if int(input("Hozirgi parolingizni kiriting: ")) == self.karta.getPin():
            newPin = int(input("Yangi parolni kiriting: "))
            self.karta.setPin(newPin)

    def back(self):
        self.menyu()



class Karta:
    def __init__(self, num, muddat):
        self.num = num
        self.muddat = muddat
        self.__pin = 1111
        self.__balans = 3000000

    def getPin(self):
        return self.__pin
    
    def getBalans(self):
        return self.__balans
    
    def setBalans(self, summa):
        self.__balans -= summa

    def setPin(self, newPin):
        self.__pin = newPin





k1 = Karta(8600145875982405, 10.2028)
b1 = Bankomat(k1)
b1.pin()
b1.menyu()


