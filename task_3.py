import csv


CSV_FILE = 'task_3.csv'
WORD_FILE = 'task_3_solution.txt'
all_data= []
full_name = []
emails = []
#0 Открываем файл и записываем в масив данные об сотрудниках
with open('task_file.txt','r') as file:
    for items in file:
        items = items.split(',')
        all_data.append(items)
        
    # Удаляем пробелы в начале строки
    for i in range(len(all_data)):
        for z in range(1, len(all_data[i])):
            if all_data[i][z][0] == ' ':
                all_data[i][z] = all_data[i][z][1::]
    header = all_data[0]
    
#1 -- отсеим людей через телефонный номер---------------------------------------

def tel_num():
    index_tel = -2
    index_defolt_num = [] #определяем индексы неподходящих сотрудников
    for line in all_data:
        if line[1] == '' or line[1] == ' ' or line[2] == ' 'or line[3] == ' ' or line[2] == '' or line[-1]=='':
            index_defolt_num.append(all_data.index(line))
            #отсеиваем по отсуствию Имени, Фамилии или Города
        if len(line[index_tel]) != 7:
            index_defolt_num.append(all_data.index(line))
            # Отсеиваем по количеству цифр в номере
        try:
            line[index_tel] = int(line[index_tel])
            # отсеиваем по наличию букв в номере
        except ValueError:
            index_defolt_num.append(all_data.index(line))
    index_defolt_num = list(set(index_defolt_num)) # убераем повторы в масиве
    index_defolt_num.sort() 
    index_defolt_num.reverse() # переворачиваем для удаления без ошибок методом pop()
    for item in index_defolt_num:
        all_data.pop(item)
    #создаем список из Имени и Фамилии
    for name in all_data:
        full_name.extend([[name[1],name[2]]])
# Eсли в числе больше одного нуля ("0000000") питон показывает как "0"

#2 Создаем почтовые адресса ---------------------------------------------------------------

def email_gen(list_of_names):
    index_first_name = 0
    index_last_name = 1 
    for i in list_of_names:
        letter = 1
        while i[index_last_name] + '.' + i[index_first_name][index_first_name:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[index_last_name] + '.' + i[index_first_name][index_first_name:letter] + '@company.io')
    # Вписываем почтовые адресса в полный список
    for index in range(len(emails)):
        all_data[index][0] = emails[index]
    return emails

#4  записываем в ворд и csv файлы ------------------------------------

def execute():
    tel_num()
    email_gen(full_name)
    #Ворд файл
    with open(WORD_FILE,'w') as word_file:
        # Делаем заголовок
        str_header = str()
        for item in header:
            if item != header[-1]:
                str_header = str_header + item + ', ' 
            else:
                str_header += item
        word_file.write(str_header)

        # Создаем из масива строчные данные
        for line in all_data:
            str_line = str()
            line[-2] = str(line[-2]) #Преобразуем номер в строку
            for item in line:
                if item != line[-1]:
                    str_line = str_line + item + ', ' 
                else:
                    str_line += item
            word_file.write(str_line)
        
    #csv файл
    # with open(CSV_FILE,'w',newline='') as csv_file:
        
    #     write = csv.writer(csv_file,delimiter=';')
    #     write.writerow(header)
    #     for item in all_data:
    #         item[-1]= item[-1][0:-1:] #тут мешается \n
    #         write.writerow([item[0],item[1], item[2], item[3],item[-1]])

execute()
