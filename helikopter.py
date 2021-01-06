class Helicopter(SilahliKuvvetler):
    def __init__(self,name,yearOfStart,origin):
       SilahliKuvvetler.__init__(self, name, yearOfStart)
       self.origin=origin


    def bilgileri_goster(self):
        "bilgileri_goster fonksiyonuyla helikopterin adı,kullanıma başlama yılı ve originine ait bilgileri görebiliyoruz."
        return print("Helikopterin Adı: {} Kullanıma Başlama Yılı: {}  Origin: {} ".format(self.name,self.yearOfStart,self.origin))  


    def length(self,length):
        self.length=length
        "uzunluk fonksiyonuyla helikopterin uzunluğuna(metre cinsinden) ait bilgileri görebiliyoruz."
        if self.length<15.0:
            print("Bu helikopterin uzunluğu: {} ve küçük helikopter kategorisine girer".format(self.length))
        if 15.0<=self.length<=20.0:
            print("Bu helikopterin uzunluğu: {} ve orta helikopter kategorisine girer".format(self.length))
        else:
            print("Bu helikopterin uzunluğu: {} ve büyük helikopter kategorisine girer".format(self.length))


    def max_kalkış_kütlesi(self,masse1):
        self.masse1=masse1
        "max_kalkış_kütlesi fonksiyonuyla helikopterin maksimum kalkış kütlesiyle(kg cinsinden ve helikopterin kütlesi hariç) hangi sınıfa ait olduğunu görebiliyoruz."
        if self.masse1< 2300:
            print("Bu helikopter 1.kategoridedir")
        if 2300<=self.masse1< 5000:
            print("Bu helikopter 2.kategoridedir")
        if 5000<=self.masse1< 9000:
            print("Bu helikopter 3.kategoridedir")
        if 9000<=self.masse1< 13500:
            print("Bu helikopter 4.kategoridedir")
        if 13500<=self.masse1< 19500:
            print("Bu helikopter 5.kategoridedir")
        if 19500<=self.masse1< 27000:
            print("Bu helikopter 6.kategoridedir")

#masse1 helikopter kütlesi hariç, masse2 helikopter kütlesi dahil
    def distance(self,masse2):
        self.masse2=masse2
        "distance fonksiyonu helikopter toplam kütlesine göre FATO(Son yaklaşma ve kalkış alanı) kenarı ile uçak pisti kenarı arasındaki mesafeyi görebiliyoruz."

        if self.masse2<2720:
            print("60m")
        if 2720<=self.masse2<5760:
            print("120m")
        if 5760<=self.masse2<100.000:
            print("180m")
        else:
            print("250m")
       
#Ornek bir helikopter nesnesi oluşturuyoruz
NATO_Helicopter_90= Helicopter("NH90",1995,"Fransa,Almanya,İtalya,Hollanda")

NATO_Helicopter_90.bilgileri_goster()

#Helikopterin uzunluğuna göre helikopterin hangi uzunluk kategorisine girdiğini öğreniyoruz.               
NATO_Helicopter_90.length(16.180)

#Maksimum kalkış kütlesine göre helikopterin hangi kategoriye girdiğini öğreniyoruz
NATO_Helicopter_90.max_kalkış_kütlesi(4200)

#Toplam helikopter kütlesine göre olması gereken FATO(Son yaklaşma ve kalkış alanı) kenarı ile uçak pisti kenarı arasındaki mesafeyi görebiliyoruz.
NATO_Helicopter_90.distance(10600)



            
