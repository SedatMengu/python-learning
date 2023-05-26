class Hesapla(object):
    def __init__(self,a,b):
        self.value1=a
        self.value2=b
    def topla(self):
        return (self.value1 + self.value2)
    def carp(self):
        return (self.value1*self.value2)
    def cikar(self):
        return (self.value1 - self.value2)
    def bol(self):
        return (self.value1/self.value2)
    
        
# c1 = Hesapla(3,5)
# print(c1.topla())
# print(c1.carp())
# print(c1.bol())
# print(c1.cikar())


v1 = int(input("1.sayi : "))

secim = input("Yapılacak işlemi seçiniz : 1-topla , 2-cikar , 3-carp , 4-bol : ")

v2 = int(input("2.sayi : "))


c2 = Hesapla(v1,v2)
# print("girilen sayıların toplamı : {} ".format(c2.topla()))
# print("girilen sayıların farkı : {}".format(c2.cikar()))
# print("girilen sayıların carpimi : {}".format(c2.carp()))
# print("girilen sayıların farkı {}".format(c2.bol()))

try:
    if secim == "1":
        print("girilen sayıların toplamı : {}".format(v1 + v2))
    elif secim =="2":
        print("girilen sayıların farkı : {}".format(v1 - v2))
    elif secim =="3":
        print("girilen sayıların carpimi : {}".format(v1 * v2))
    elif secim=="4":
        print("girilen sayıların bolumu : {}".format(v1 / v2))
    else:
        print("hatalı bir değer girdiniz")
except ZeroDivisionError:
    print("sayı sıfıra bölünemez")





