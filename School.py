"""Soru 2: "School" Adında Bir Sınıf Oluşturun
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
view_teacher_list(self): Okulda çalışan öğretmenlerin listesini görüntülemek için kullanılan bir yöntemdir. Öğretmen adlarını ve branşlarını listeler."""
class School:
    def __init__(self, name, foundation_year):
        self.name=name
        self.foundation_year=foundation_year
        self.students=[]    # Öğrenci bilgileri burada saklanır (liste)
        self.teachers={}     # Öğretmen bilgileri burada saklanır (sözlük)
    
    """Yeni bir öğrenci ekler."""
    def add_new_student(self, student_name, student_class):
        self.students.append({"name": student_name, "class":student_class})
        print(f"ogrenci eklendi: {student_name}, sinif: {student_class}")

    """Yeni bir öğretmen ekler."""
    def add_new_teacher(self, teacher_name,branch):
        self.teachers[teacher_name]=branch
        print(f"ogretmen eklendi: {teacher_name}, brans: {branch}")

    """Tüm öğrencilerin listesini gösterir."""
    def view_student_list(self):
        print(f"\n{self.name} okuldaki ogrenciler:")
        for student in self.students:
            print(f"ad: {student['name']}, sinif: {student['class']}")
    
    """Tüm öğretmenlerin listesini gösterir."""
    def view_teacher_list(self):
        print(f"\n{self.name} okuldaki ogretmenler")
        for teacher, branch in self.teachers.items():
            print(f"ad: {teacher}, brans: {branch}")

# Okul nesnesi oluşturma
school=School("anadolu lisesi",2000)

# Yeni öğrenciler ekleme
school.add_new_student('hasan yilmaz','8-b')
school.add_new_student('nazmi deniz','7-a')

# Yeni öğretmenler ekleme
school.add_new_teacher('ali temiz','matematik')
school.add_new_teacher('kemal yurt','fen')

# Öğrenci listesini görüntüleme
school.view_student_list()

# Öğretmen listesini görüntüleme
school.view_teacher_list()

