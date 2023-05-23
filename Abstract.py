# Abstract class nedir ?

    # - soyut classlara denir. child classlar için şablon görevi görürler ve kullanılacak ortak fonksiyonları kendi içlerinde tutarlar.
    # - abstract class dan br nesne yaratılamaz. bu bir kuraldır. yapılmaya çalışılırsa hata verir.
    # - abstract class içerisinde tanımlı olan metotları muhakkak kullanmak gerekir. 

# bir class ı abstract class yapmak için neler yapmalıyız.

from abc import ABC,abstractmethod  # Python'da abstract class tanımlamak için abc (Abstract Base Classes) modülü kullanılır. Bu modül, abstract class'ların tanımlanması ve kullanılması için gerekli araçları sağlar. abc modülündeki ABC sınıfını ve abstractmethod dekoratörünü kullanarak bir abstract class tanımlanır.

class Animal(ABC):   # super class

    @abstractmethod             # bu metot soyuttur ve kesinlikle kullanmamız gerekir amacıyla @abstractmethod yazdık. / @abstractmethod yazmaz isek soyut olmuyor ve kullanılmasa da olur.
    def walk(self):
        print("walk")

    @abstractmethod             # bu metot soyuttur ve kesinlikle kullanmamız gerekir amacıyla @abstractmethod yazdık./ @abstractmethod yazmaz isek soyut olmuyor ve kullanılmasa da olur.
    def run(self):
        print("run")

class Bird(Animal): # child class
    def __init__(self):
        print("bird")
    def walk(self):
        return super().walk()
    def run(self):
        return super().run()

# a = Animal()          # 1.kural gereği abstract class dan nesne türetilmez.
b1 = Bird()

b1.walk()
b1.run()


####################################################################################################################################################################################################################################################################################################################################
# - chatgpt tanımı :

    # Bir abstract class (soyut sınıf), diğer sınıfların temel özelliklerini ve davranışlarını tanımlayan, somutlaştırılamayan bir sınıftır. 
    # Bir abstract class, doğrudan bir örnek (instance) oluşturulamaz, ancak diğer sınıflar tarafından miras alınabilir.
    # Abstract class'lar, kalıtım yoluyla diğer sınıflara bir şablondan veya bir arayüzden davranışlar sağlamak amacıyla kullanılır.
    # Bu sınıfın amacı, ortak özelliklere ve metotlara sahip alt sınıfların birleşik bir arabirimini tanımlamaktır.
    # Alt sınıflar, abstract class'ın metotlarını uygulamak ve gerektiğinde özelleştirmek zorundadır.
    # Python'da abstract class tanımlamak için abc (Abstract Base Classes) modülü kullanılır. 
    # Bu modül, abstract class'ların tanımlanması ve kullanılması için gerekli araçları sağlar. 
    # abc modülündeki ABC sınıfını ve abstractmethod dekoratörünü kullanarak bir abstract class tanımlanır.

# modüller ile ilgili chatgpt cevabı : 

# Python, geniş bir standart kütüphaneyle birlikte gelir ve bu kütüphane birçok modül içerir. 
# Standart kütüphanedeki modüller, Python dilinin kendisiyle birlikte dağıtılır ve Python yüklenirken otomatik olarak yüklenir.
# Python'ın standart kütüphanesinde yüzlerce modül bulunur.
# Bunlar arasında dosya işlemleri, ağ programlama, veri işleme, matematiksel işlemler, metin işleme, zaman yönetimi, grafikler, veritabanı işlemleri ve daha pek çok konuda yardımcı işlevler sunan modüller bulunmaktadır.
# Bunun dışında, Python topluluğu tarafından geliştirilen ve Python Package Index (PyPI) adı verilen bir depoda yer alan binlerce üçüncü taraf modül bulunmaktadır.
# Bu üçüncü taraf modüller, Python diline ek işlevler ve özellikler eklemek için kullanılır. 
# Örneğin, veri analizi için Pandas, web uygulamaları için Flask, makine öğrenmesi için scikit-learn gibi popüler üçüncü taraf modüller bulunmaktadır.
# Bu nedenle, Python'da kaç tane modül olduğunu kesin bir sayıyla belirtmek zordur. 
# Standart kütüphanedeki modüllerle birlikte binlerce üçüncü taraf modül bulunmaktadır. 
# Python modül ekosistemi oldukça zengin ve çeşitlidir, böylece çeşitli ihtiyaçlara yönelik birçok hazır çözüm sunulmaktadır.

# chatgpt örneği : 

from abc import ABC, abstractmethod

class Sekil(ABC):
    @abstractmethod              # bu metot soyuttur ve kesinlikle kullanmamız gerekir amacıyla @abstractmethod yazdık./ @abstractmethod yazmaz isek soyut olmuyor ve kullanılmasa da olur.
    def alan(self):
        pass

    @abstractmethod              # bu metot soyuttur ve kesinlikle kullanmamız gerekir amacıyla @abstractmethod yazdık./ @abstractmethod yazmaz isek soyut olmuyor ve kullanılmasa da olur.
    def cevre(self):
        pass

class Dikdortgen(Sekil):
    def __init__(self, en, boy):
        self.en = en
        self.boy = boy

    def alan(self):
        return self.en * self.boy

    def cevre(self):
        return 2 * (self.en + self.boy)

dikdortgen = Dikdortgen(4, 5)
print(dikdortgen.alan())  # 20
print(dikdortgen.cevre())  # 18


# Bu örnekte, Sekil adında bir abstract class tanımlanmıştır. 
# Sekil sınıfı, alan() ve cevre() adında soyut metotları içerir. 
# Bu metotlar, alt sınıflar tarafından uygulanması gereken metotlardır.
# Dikdortgen sınıfı, Sekil sınıfından miras alır ve alan() ve cevre() metotlarını uygular. 
# Dikdortgen sınıfı, Sekil abstract class'ını temsil eden bir alt sınıftır.
# Bu şekilde, abstract class'lar alt sınıfların belirli metotları uygulamasını sağlar ve ortak bir davranış şablonu sunar. 
# Abstract class'lar, kodun daha modüler, sürdürülebilir ve genişletilebilir olmasına yardımcı olur.

####################################################################################################################################################################################################################################################################################################################################


from abc import ABC , abstractmethod

class Hayvan(ABC):
    def __init__(self,isim,yas):
        self.isim = isim
        self.yas = yas
    
    @abstractmethod                 # bu metot soyuttur ve kesinlikle kullanmamız gerekir amacıyla @abstractmethod yazdık./ @abstractmethod yazmaz isek soyut olmuyor ve kullanılmasa da olur.
    def ses_cikar(self):
        pass

class Kedi(Hayvan):
    def __init__(self, isim, yas):
        super().__init__(isim, yas)

    def ses_cikar(self):
        return "miyav"
    
class Kopek(Hayvan):
    def __init__(self, isim, yas):
        super().__init__(isim, yas)
    
    def ses_cikar(self):
        return "hav hav"

class Kus(Hayvan):
    def __init__(self, isim, yas):
        super().__init__(isim, yas)
    
    def ses_cikar(self):
        return "cik cik"
    
class Ordek(Hayvan):
    def __init__(self, isim, yas):
        super().__init__(isim, yas)
    def ses_cikar(self):
        return "vak vak"
# hayvan1 = Hayvan()        Hayvan classı abstract olduğundan nesne türetemeyiz
hayvan2 = Kedi("minnoş",3)
hayvan3 = Kus("kanarya",1)
hayvan4 = Kopek("karabaş",1)
hayvan5 = Ordek("paytak",2)

print(hayvan2.isim)
print(hayvan2.yas)
print(hayvan2.ses_cikar())
print(hayvan3.isim)
print(hayvan3.yas)
print(hayvan3.ses_cikar())
print(hayvan4.isim)
print(hayvan4.yas)
print(hayvan4.ses_cikar())
print(hayvan5.isim)
print(hayvan5.yas)
print(hayvan5.ses_cikar())

# Bu örnekte, Hayvan adında bir abstract class tanımlanmıştır. Hayvan sınıfı, isim ve yas adında özelliklere sahiptir ve ses_cikar() adında soyut bir metodu vardır.
# Kedi, Kopek ve Ordek sınıfları, Hayvan sınıfından miras alır ve ses_cikar() metotunu uygular. Her bir alt sınıf, kendine özgü bir ses_cikar() metodu tanımlar.
# Her alt sınıf, Hayvan abstract class'ının özelliklerini ve metotlarını kullanır. Alt sınıflar, Hayvan sınıfının ses_cikar() metodunu kendi ihtiyaçlarına göre uygulayarak, ilgili hayvanın sesini çıkarır.
# Bu şekilde, Kedi, Kopek ve Ordek sınıfları, Hayvan abstract class'ının metotlarını uygular ve kendi seslerini çıkarır.
#  Her alt sınıf, soyut metodu kendi ihtiyaçlarına göre özelleştirir ve farklı hayvanların seslerini temsil eder.

###########################################################################################################################################################################################################


# sinan erdinç örneği : 

class AbstractDatabase:
    def connect(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()


class MsSql(AbstractDatabase):
    def connect(self):
        print("connected to mssql")


class MongoDB(AbstractDatabase):
    def connect(self):
        print("connected to mongodb")



MongoDB().connect() # connected to mongodb      # connect() metodu için bir mesaj verildiği için mesaj ekrana geldi.
MongoDB().close() # NotImplementedError         # close() metodu kullanılmadığı için ve inheritance olarak "AbstractDatabase" aldığı için orada tanımlı olan hata mesajı verdi ve program durdu.


from abc import ABCMeta, abstractmethod


class AbstractDatabase(metaclass=ABCMeta):
    @abstractmethod
    def connect(self): pass                 # @abstractmethod yazarak zorunlu hale getirdik.

    @abstractmethod                         # @abstractmethod yazarak zorunlu hale getirdik.
    def close(self): pass

    def retry(self): pass                   # @abstractmethod yazmadığımız için zorunlu değil.


class MsSql(AbstractDatabase):
    def connect(self):
        print("connected to mssql")

    def close(self):
        print("connection is closed")


class MongoDB(AbstractDatabase):
    def connect(self):
        print("connected to mongodb")

    def close(self):
        print("connection is closed")


MongoDB().connect()
MongoDB().retry()


# AbstractDatabase sınıfı, ABCMeta metaclass'ını kullanarak bir abstract sınıf olarak tanımlanmıştır. c
# onnect() ve close() metotları @abstractmethod dekoratörü ile zorunlu hale getirilmiştir.
# MsSql ve MongoDB sınıfları, AbstractDatabase sınıfından miras alır ve zorunlu olan connect() ve close() metotlarını uygular.
# MsSql sınıfı, connect() ve close() metotlarını uygun şekilde tanımlar ve mesajları ekrana yazdırır.
# MongoDB sınıfı da connect() ve close() metotlarını uygun şekilde tanımlar ve mesajları ekrana yazdırır.
# MongoDB().connect() çağrısı, "connected to mongodb" mesajını ekrana yazdırır, çünkü connect() metodu MongoDB sınıfında tanımlanmıştır.
# MongoDB().retry() çağrısı, retry() metodu AbstractDatabase sınıfında tanımlanmadığı için hata vermez ve normal bir şekilde çalışır.
# Bu örnekte, abstract sınıfın ABCMeta metaclass'ını kullanarak tanımlanması ve @abstractmethod dekoratörünün metotlara uygulanmasıyla, alt sınıfların belirli metotları uygulamak zorunda olduğu sağlanmış olur.