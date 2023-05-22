class BankaHesabi(object):
    def __init__(self,name,surname,money):
        self.name = name
        self.surname = surname
        self.money = money
    

p1 = BankaHesabi("name1","surname1",3000)
p2 = BankaHesabi("name2","surname2",5000)
p3 = BankaHesabi("name3","surname3",30000)

print(p1.money)
print(p3.surname)
print(p2.name)

p1.money = 000  # / galip derviş in parasını sıfırladık.

print(p1.money)

# attribute lere dışardan erişime kapatmamız gerekiyor. 

# self.money ifadesini self.__money olarak değiştirdiğimizde private bir attribute olur ve dışardan erişime kapalı olur.
# aynı durum metotlar için de geçerlidi. def metot(self): şeklinde tanımlanan bir metotu def__metot(self): yaparsak dışardan erişime kapalı olur.

class BankaHesabi2(object):
    def __init__(self,name,surname,money):
        self.name = name
        self.surname = surname
        self.__money = money          

p11 = BankaHesabi2("name11","surname11",3000)
p22 = BankaHesabi2("name22","surname22",5000)
p33 = BankaHesabi2("name33","surname33",30000)
p44 = BankaHesabi2("name44","surname44",2000000)

# print(p44.__money)      # / AttributeError: 'BankaHesabi2' object has no attribute '__money'

# get ve set kavrmları

# gizlediğimiz attribute leri görüntüleyebilir ve düzeltebiliriz. get getirmek , set güncellemek anlamına gelir.


class BankaHesabi3(object):
    def __init__(self,name,surname,money):
        self.name = name
        self.surname = surname
        self.__money = money    
    def getMoney(self):                     # gizlenen bir attribute u bu şekilde görebiliriz.
        return self.__money
    def setMoney(self , amount):
        self.__money = amount               # gizlenen bir attribute u bu şekilde değiştirebiliriz.
    def __Zam(self):                        # bir metotu da bu şekilde gizleyebiliriz.
        self.__money = self.__money + 500   
    

p111 = BankaHesabi3("name111","surname111",3000)
p222 = BankaHesabi3("name222","surname222",5000)
p333 = BankaHesabi3("name333","surname333",30000)
p444 = BankaHesabi3("name444","surname444",2000000)

# print(p4.__money)

print(p444.getMoney())
print(p222.getMoney())
p333.setMoney(80000)
print(p333.getMoney())

p444.Zam()                          # / AttributeError: 'BankaHesabi3' object has no attribute 'Zam' / Zam metotu gizli olduğundan erişime bulamadı.
print(p444.getMoney())
