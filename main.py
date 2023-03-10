import sqlite3 as sql
from time import sleep
import sys
import os

conn = sql.connect('students.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS STUDENTS(
    name text,
    lastname text,
    age integer
)""")

def menu():
    print('1-Öğrenci ekle')
    print('2-Öğrenci sil')
    print('3-Öğrenci tablosunu yazdır')
    print('4-Çıkış')
    
def insert(name, lastname, age):
    add_command = """INSERT INTO STUDENTS VALUES {} """
    add_data = (name, lastname, age)
    cur.execute(add_command.format(add_data))
    conn.commit()

def delete_Info(name, lastname, age):
    delete_command = """DELETE from Students WHERE name = '{}' AND lastname = '{}' AND age = {} """
    cur.execute(delete_command.format(name, lastname, age))
    conn.commit()

def delete_Name(name):
    delete_command = """DELETE from Students WHERE name = '{}' """
    cur.execute(delete_command.format(name))
    conn.commit()

def delete_Lastname(lastname):
    delete_command = """DELETE from Students WHERE lastname = '{}' """
    cur.execute(delete_command.format(lastname))
    conn.commit()

def delete_Age(age):
    delete_command = """DELETE from Students WHERE age = {} """
    cur.execute(delete_command.format(age))
    conn.commit()

def delete_Age_below(age):
    delete_command = """DELETE from Students WHERE age < {} """
    cur.execute(delete_command.format(age))
    conn.commit()

def delete_Age_above(age):
    delete_command = """DELETE from Students WHERE age > {} """
    cur.execute(delete_command.format(age))
    conn.commit()

def get_datas_Fullname():
    get_command = """SELECT * from Students"""
    data = cur.execute(get_command)
    print(data.fetchall())

def get_datas_Name():
    get_command = """SELECT name from Students"""
    data = cur.execute(get_command)
    print(data.fetchall())

def get_datas_Lastname():
    get_command = """SELECT lastname from Students"""
    data = cur.execute(get_command)
    print(data.fetchall())

def get_datas_Age():
    get_command = """SELECT age from Students"""
    data = cur.execute(get_command)
    print(data.fetchall())

def exit():
    print('Çıkış yapılıyor...')
    sleep(2)
    sys.exit()
    


clear = lambda: os.system('cls')
print('Öğrenci veritabanına bağlantı kuruldu.')
sleep(1)
clear()

while(True):
    menu()
    print('\n')
    menuChoice = int(input('Lütfen yapmak istediğiniz işlemin yanındaki rakamı giriniz: '))
    clear()
    match(menuChoice):
        case 1:
            info = str(input('Lütfen öğrencinin isim soyisim ve yaşını aralarında birer boşluk olacak şekilde giriniz: '))
            info_split = info.split(' ')
            name = info_split[0]
            lastname = info_split[1]
            age = int(info_split[2])
            insert(name, lastname, age)
            print('%s %s [%d] veritabanına başarıyla kaydedildi.'%(name, lastname, age))
            sleep(1.5)
            clear()
        case 2:
            print('1-Tüm bilgilere göre sil')
            print('2-İsme göre sil')
            print('3-Soyisme göre sil')
            print('4-Yaşa göre sil\n')
            deleteChoice = int(input('Seçiminizi giriniz: '))
            clear()
            if deleteChoice == 1:
                info = str(input('Silmek istediğiniz öğrencinin ismini soyismini ve yaşını aralarında birer boşluk olacak şekilde giriniz: '))
                info_split = info.split(' ')
                name = info_split[0]
                lastname = info_split[1]
                age = int(info_split[2])
                delete_Info(name, lastname, age)
                print('%s %s [%d] veritabanından başarıyla silindi.'%(name, lastname, age))
                sleep(1.5)
                clear()
            elif deleteChoice == 2:
                name = str(input('Silmek istediğiniz öğrencinin ismini giriniz: '))
                delete_Name(name)
                print('%s isimli öğrenci(ler) veritabanından başarıyla silindi.'%(name))
                sleep(1.5)
                clear()
            elif deleteChoice == 3:
                lastname = str(input('Silmek istediğiniz öğrencinin soyismini giriniz: '))
                delete_Lastname(lastname)
                print('%s soyisimli öğrenci(ler) veritabanından başarıyla silindi.'%(lastname))
                sleep(1.5)
                clear()
            elif deleteChoice == 4:
                print('1-Yaşa göre sil\n')
                print('2-Herhangi bir "x" yaşının altındakileri sil')
                print('3-Herhangi bir "x" yaşının üstündekileri sil\n')
                ageChoice = int(input('Seçiminizi giriniz: '))
                clear()
                if ageChoice == 1:
                    age_D = int(input('Lütfen yaş giriniz: '))
                    delete_Age(age_D)
                    print('%d yaşlı öğrenci(ler) veritabanından başarıyla silindi.'%(age_D))
                    sleep(1.5)
                    clear()
                if ageChoice == 2:
                    age_D = int(input('Lütfen yaş giriniz: '))
                    delete_Age_below(age_D)
                    print('%d yaşından küçük öğrenci(ler) veritabanından başarıyla silindi.'%(age_D))
                    sleep(1.5)
                    clear()
                if ageChoice == 3:
                    age_D = int(input('Lütfen yaş giriniz: '))
                    delete_Age_above(age_D)
                    print('%d yaşından büyük öğrenci(ler) veritabanından başarıyla silindi.'%(age_D))
                    sleep(1.5)
                    clear()
            else:
                print('HATALI GİRİŞ YAPILDI!')
                sleep(1.5)
                clear()
        case 3:
            print('1-İsim soyisim ve yaşları yazdır')
            print('2-İsimleri yazdır')
            print('3-Soyisimleri yazdır')
            print('4- Yaşları yazdır\n')
            dataChoice = int(input('Seçiminizi giriniz: '))
            clear()
            loopBreak = None
            while(loopBreak != 5):
                if dataChoice == 1:
                    get_datas_Fullname()
                elif dataChoice == 2:
                    get_datas_Name()
                elif dataChoice == 3:
                    get_datas_Lastname()
                elif dataChoice == 4:
                    get_datas_Age()
                else:
                    print('HATALI GİRİŞ YAPILDI!')
                    sleep(1.5)
                loopBreak = int(input('\nDevam etmek için "5" giriniz: '))
                clear()
        case 4:
            exit()   