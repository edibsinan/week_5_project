"""Soru 1: "Rectangle" Adında Bir Python Sınıfı Oluşturun
Bu sınıf, bir dikdörtgeni temsil eder ve aşağıdaki özelliklere ve
 yöntemlere sahip olmalıdır:

Özellikler:

width (bir tam sayı)
height (bir tam sayı)
Yöntemler:

area(self): Dikdörtgenin alanını hesaplayan ve döndüren 
bir yöntem.

perimeter(self): Dikdörtgenin çevresini hesaplayan ve döndüren bir yöntem.
"Rectangle" sınıfından bir örnek oluşturun, 
genişliğini 5, yüksekliğini 7 olarak ayarlayın ve 
ardından alanını ve çevresini yazdırın."""
class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    
    def area(self):
        # dikdortgein alanini hesaplar
        return self.width*self.height
    
    def perimeter(self):
        # dikdortgein cevresini hesaplar
        return 2*(self.width+self.height)
    
rectangle=Rectangle(5,7)

print(f'Dikdortgenin alani: {rectangle.area()}')
print(f'dikdortgenin cevresi: {rectangle.perimeter()}')