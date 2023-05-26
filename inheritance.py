# inheritance nedir ? 

# pyhton dilinde genel olarak üzerine koyarak ilerlemek esas olduğundan dolayı inheritance diye bir kavram ortaya çıkmıştır.
# inheritance daha önce benzer olarak üretilen class dan birebir metot veya attribute lerinin alınması olarak düşünebiliriz.
# parent ve child class lar olmak üzere 2 türlü class vardır.

# 1- child class ne demektir ?

# parent class ın attribute lerini ve metotlarını kullanabilen class demekttir.
# herhangi bir sayı sınırı olmaksızın bir parent class dan sınırsız sayıda child class tanımlanabilir.
# parent classı ile gelen metotlara ilave olarak başka metotlar da ilave edebiliriz.

# 2- parent class ne demektir ?

# herhangi bir yerden inheritance olarak bir şey almayan class lara denir.


class Animal():                     # parent class
    def __init__(self):
        print("animal is created")
    def toString(self):
        print("animal")
    def walk(self):
        print("animal is walking")


class Monkey(Animal):
    def __init__(self):
        super().__init__()          # Monkey bir child class olduğundan dolayı bu satır parent class init kısmına bağlantı içeriyor.
        print("monkey is created")
    def toString(self):             #aynı isim parent class da da var ancak burada da tanımlayarak onu ezmiş olduk.
        print("monkey")
    def Climb(self):
        print("monkey can climb")
    
m1 = Monkey()       # / animal is created   # / monkey is created  önce dış katmak olan Animal oluşturuldu , daha sonra Monkey olan iç katman oluştu.

m1.walk()
m1.toString()

class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("birds is created")

    def Fly(self):
        print("birds can fly")


b1 = Bird()                 # ezmediğimiz için hem inheritance den gelen print hem de child içerisindeki print aynı anda çalıştı.

b1.Fly()                # Bird class ında tanımladığımız için Bird Classındaki işlemleri yaptı.
b1.walk()               # inheritance olarak aldığı parent classındaki işlemleri yaptı.
b1.toString()           # inheritance olarak aldığı parent classındaki işlemleri yaptı.

####################################################

# kalıtım üzerinde bi web sitesi örneği yapalım.

class WebSitesi():
    def __init__(self,name,surname):        # Websitesi class ı 2 adet parametre alıyor. name ve surname
        self.name = name
        self.surname = surname

    def LoginInfo(self):
        print("LoginInfo ile giriş yapılıyor... 2 parametre ister name , surname")   #LoginIfo() metodunu çağırınca ekrana bunları yazdır dedik.

w1 = WebSitesi("name","surname")            # w1 nesnesi türettik. 

print(w1)       # <__main__.WebSitesi object at 0x000001FAE0F4EA90>

w1.LoginInfo()      # Websitesi classında tanımlanan LoginInfo fonksiyonunu oluşturulan w1 nesnesi üzerinden çağırdık.

w2 = WebSitesi("name2","surname2")

w2.LoginInfo()
print(w2.name)
print(w2.surname)


class Websitei2(WebSitesi):
    def __init__(self, name, surname,ids):
        super().__init__(name, surname)
        self.ids = ids

    def Login(self):
        print("Login ile giriş yapılıyor... 3 parametre ister name , surname , id")
    

w2 = Websitei2("cem","uzan","123")      # Websitesi2 classı üzerinden bir nesne oluşturmak ister isek girmemiz gereken 3 tane parametre var.

print(w2.ids)                           # Websitesi2 classına ait olan ids attribute unu çağırabiliriz.
print(w2.name)                          # inheritance olarak gelen name atribute unu çağırabiliriz.
print(w2.surname)                       # inheritance olarak gelen surname atribute unu çağırabiliriz.
w2.Login()                              # Websitesi2 classına ait olan Login() metodunu çağırabilriz.
w2.LoginInfo()                          # inheritance olarak gelen LogiInfo() metodunu çağırabiliriz.


class Websitesi3(WebSitesi):
    def __init__(self, name, surname,email):        # websitesi 3 için kullanılacak 3 attribut
        super().__init__(name, surname)
        self.email = email

    def LoginEmailli(self):
        print("LoginEmailli ile giriş yapılıyor. 3 parametre ister , name , surname , email")


w3 = Websitesi3("name3","surname3",email="sedatmengu@gmail.com")
    
w3.LoginEmailli()
print(w3.name)
print(w3.email)
print(w3.surname)
w3.LoginInfo()
