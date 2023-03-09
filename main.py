import sqlite3 as sql
from time import sleep
import sys

conn = sql.connect('students.db')
cur = conn.cursor()

print('\nÖğrenci veritabanına bağlantı kuruldu.\n\n')
sleep(1.5)

def menu():
    print('\t1-Öğrenci ekle\n')
    print('\t2-Öğrenci sil\n')
    print('\t3-Öğrenci tablosunu yazdır\n')
    print('\t4-Çıkış\n')
    
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
    

while(True):
    print('\n')
    menu()
    menuChoice = int(input('Lütfen yapmak istediğiniz işlemin yanındaki rakamı giriniz: '))
    print('\n')
    match(menuChoice):
        case 1:
            sleep(1)
            info = str(input('\tLütfen öğrencinin isim soyisim ve yaşını aralarında birer boşluk olacak şekilde giriniz: '))
            info_split = info.split(' ')
            name = info_split[0]
            lastname = info_split[1]
            age = int(info_split[2])
            insert(name, lastname, age)
            print('\t%s %s [%d] veritabanına başarıyla kaydedildi.\n\n'%(name, lastname, age))
            sleep(1.5)
        case 2:
            sleep(1)
            print('\t1-Tüm bilgilere göre sil\n')
            print('\t2-İsme göre sil\n')
            print('\t3-Soyisme göre sil\n')
            print('\t4-Yaşa göre sil\n')
            deleteChoice = int(input('Seçiminizi giriniz: '))
            print('\n')
            if deleteChoice == 1:
                info = str(input('\tSilmek istediğiniz öğrencinin ismini soyismini ve yaşını aralarında birer boşluk olacak şekilde giriniz: '))
                info_split = info.split(' ')
                name = info_split[0]
                lastname = info_split[1]
                age = int(info_split[2])
                delete_Info(name, lastname, age)
                print('\t%s %s [%d] veritabanından başarıyla silindi.\n\n'%(name, lastname, age))
                sleep(1.5)
            elif deleteChoice == 2:
                name = str(input('\tSilmek istediğiniz öğrencinin ismini giriniz: '))
                delete_Name(name)
                print('\t%s isimli öğrenci(ler) veritabanından başarıyla silindi.'%(name))
                sleep(1.5)
            elif deleteChoice == 3:
                lastname = str(input('Silmek istediğiniz öğrencinin soyismini giriniz: '))
                delete_Lastname(lastname)
                print('\t%s soyisimli öğrenci(ler) veritabanından başarıyla silindi.\n\n'%(lastname))
                sleep(1.5)
        
            elif deleteChoice == 4:
                print('\t1-Yaşa göre sil\n')
                print('\t2-Herhangi bir "x" yaşının altındakileri sil\n')
                print('\t3-Herhangi bir "x" yaşının üstündekileri sil\n')
                ageChoice = int(input('Seçiminizi giriniz: '))
                print('\n')
                if ageChoice == 1:
                    age_D = int(input('\tLütfen yaş giriniz: '))
                    delete_Age(age_D)
                    print('\t%d yaşlı öğrenci(ler) veritabanından başarıyla silindi.'%(age_D))
                    sleep(1.5)
                if ageChoice == 2:
                    age_D = int(input('\tLütfen yaş giriniz: '))
                    delete_Age_below(age_D)
                    print('\t%d yaşından küçük öğrenci(ler) veritabanından başarıyla silindi.'%(age_D))
                    sleep(1.5)
                if ageChoice == 3:
                    age_D = int(input('\tLütfen yaş giriniz: '))
                    delete_Age_above(age_D)
                    print('\t%d yaşından büyük öğrenci(ler) veritabanından başarıyla silindi.'%(age_D))
                    sleep(1.5)
            else:
                print('HATALI GİRİŞ YAPILDI!')
                sleep(1.5)
        case 3:
            sleep(1)
            print('\t1-İsim soyisim ve yaşları yazdır\n')
            print('\t2-İsimleri yazdır\n')
            print('\t3-Soyisimleri yazdır\n')
            print('\t4- Yaşları yazdır\n')
            dataChoice = int(input('Seçiminizi giriniz: '))
            print('\n')
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
                loopBreak = int(input('\n\tDevam etmek için "5" giriniz: '))
        case 4:
            exit()
                
                
            
            
    
            
                