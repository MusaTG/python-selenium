students = []

def addStudent():
    print("Öğrencinin")
    name = input("İsim: ")
    surname = input("Soyisim: ")
    lastName = name+" "+surname
    students.append(lastName)
    print(f"{lastName} isimli öğrenci eklendi.")
# addStudent()

def removeStudent():
    print("Silinecek Öğrencinin")
    name = input("İsim: ")
    surname = input("Soyisim: ")
    lastName = name+" "+surname
    if lastName in students:
        students.remove(lastName)
        print(f"{lastName} isimli öğrenci kaldırıldı.")
    else:
        print(f"{lastName} isimli öğrenci listede bulunamadı.")
# removeStudent()

def addMultipleStudent():
    count = input("Eklenecek Öğrenci Sayısı:")
    for index in range(int(count)):
        print(index+1)
        addStudent()
# addMultipleStudent()

def listStudents():
    for student in students:
        print(student)
# listStudents()

def numberStudent():
    print("Numara Öğrenme")
    name = input("İsim: ")
    surname = input("Soyisim: ")
    lastName = name+" "+surname
    if lastName not in students:
        print("Öğrenci bulunamadı.")
    else:
        print("Öğrenci No:", students.index(lastName))
# numberStudent()

def reomveMultipleStudent():
    while True:
        removeStudent()
        isRemove = input("Başka öğrenci silmek istiyor musunuz? (E/H):")
        if isRemove.lower() == "e":
            continue
        else:
            break

addMultipleStudent()
reomveMultipleStudent()