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
ardından alanını ve çevresini yazdırın.


Soru 2: "School" Adında Bir Sınıf Oluşturun
Bu sınıf aşağıdaki özelliklere ve işlevlere sahip olmalıdır:
Özellikler:
    name
    foundation_year
    students
    teachers
Yöntemler:
add_new_student(self, student_name, class): Yeni bir öğrenciyi okula eklemek için kullanılan bir yöntemdir. Öğrencinin adı ve sınıfını alır ve "students" listesine ekler.
add_new_teacher(self, teacher_name, branch): Yeni bir öğretmeni okula eklemek için kullanılan bir yöntemdir. Öğretmenin adı ve branşını alır ve "teachers" sözlüğüne ekler.
view_student_list(self): Okula kayıtlı olan öğrencilerin listesini görüntülemek için kullanılan bir yöntemdir. Öğrenci adlarını ve sınıflarını listeler.
view_teacher_list(self): Okulda çalışan öğretmenlerin listesini görüntülemek için kullanılan bir yöntemdir. Öğretmen adlarını ve branşlarını listeler.


Soru 3: "Shape" Adında Bir Sınıf Oluşturun
Bu sınıf altında iki alt sınıf olan "Rectangle" ve "Square" sınıflarını oluşturun.

"Shape" sınıfının özellikleri:
width
height

"Rectangle" sınıfı:
"Shape" sınıfından miras alır ve ek olarak bir calculate_area() yöntemi ekler.

"Square" sınıfı:
"Shape" sınıfından miras alır ve aynı calculate_area() yöntemiyle karenin alanını hesaplar.

"Rectangle" ve "Square" sınıflarından birer örnek oluşturun, her birinin genişliğini ve yüksekliğini belirleyin, alanlarını hesaplayın ve sonuçları yazdırın.


Soru 4: "Vehicle" Adında Bir Sınıf Oluşturun
Bu sınıfın aşağıdaki özelliklere sahip olduğundan emin olun:
Özellikler:
make (Araç markası)
model (Araç modeli)
year (Aracın üretim yılı)
"Vehicle" sınıfını oluşturun ve iki türetilmiş alt sınıf oluşturun: "Off-Road Vehicle" (SUV) ve "SportsCar".

"Off-Road Vehicle" sınıfı:

"Vehicle" sınıfından miras alır ve ek olarak bir four_wheel_drive özelliği ekler.
"SportsCar" sınıfı:

"Vehicle" sınıfından miras alır ve bir max_speed özelliği ekler.
Her sınıftan birer örnek oluşturun, özelliklerini belirleyin ve bu özellikleri görüntülemek için bir program yazın.

Soru 5: "Customer" ve "Account" Sınıfı Oluşturun
"Account" sınıfı, "Customer" sınıfından miras almalı ve bir müşterinin banka hesap bilgilerini temsil etmelidir.

Customer Sınıfı Özellikleri:

name (müşteri adı)
surname (müşteri soyadı)
tc_identification (müşteri T.C. kimlik numarası)
phone (müşteri telefon numarası)
Account Sınıfı Özellikleri:

customer (bir Customer nesnesi)
account_number (hesap numarası)
balance (hesap bakiyesi)
Customer Sınıfı Yöntemi:

display_information(): Müşterinin adını, soyadını, T.C. kimlik numarasını ve telefon numarasını görüntüler.
Account Sınıfı Yöntemleri:

deposit(self, amount): Hesaba belirli bir miktar para yatıran bir yöntem.
money_check(self, amount): Hesaptan belirli bir miktar para çeken bir yöntem. Ancak, hesapta yeterli bakiye yoksa işlem gerçekleşmemeli ve bir mesaj görüntülenmelidir.
display_balance(): Hesap bakiyesini görüntüleyen bir yöntem.
Bu iki sınıfı oluşturun, ardından bir Customer nesnesi ve bir Account nesnesi oluşturun. Müşteri bilgilerini Account nesnesine ekleyin, hesap işlemleri yapın ve sonuçları görüntüleyin.
"""

