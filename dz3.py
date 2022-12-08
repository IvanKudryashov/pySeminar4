# В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, 
# которые имеют средний балл более «4».
lib = "seminar4/test.txt"
with open(lib, 'r', encoding='utf-8') as f:
    spisok = f.read().split('\n')
def change_spisok(spisok: list) -> str:
    file_spisok = ''
    for name in spisok:
        if name.count('5'):
            name = name.upper()
        string = name + '\n'                              
        file_spisok += string
    return file_spisok  
with open(lib, 'w', encoding='utf-8') as f:
            f.write(change_spisok(spisok))