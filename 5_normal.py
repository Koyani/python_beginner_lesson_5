
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os, sys, shutil
import easy_5 as easy
while True:
    print('Choose what you would like to do: \n(1) Go to folder \n(2) List current directory \n(3) Create folders \n{4) Remove folders\n(q) Quit')
    choice  = input('Enter a number from 1-4; to quit enter "q": ')
    if choice == '1':
        print('You have chosen to go to folder. Please, follow the example to enter a valid folder path:\n C:\\Users\\molbi\\Desktop\\geekbrains\\python_beginning.')
        path = input("Enter path: ")
        try:
            os.chdir(path)
            print(f"changed to: {path}")
            break
        except OSError:
            print("The entered path is incorrect, try again")
    elif choice == '2':
        easy.list_directory(os.getcwd())
        break
    elif choice == '3':
        name = input("Enter directory name to remove: ")
        easy.remove_directory(name)
        break
    elif choice == '4':
        name = input("Enter directory name to create: ")
        easy.create_directory(name)
        break
    elif choice == 'q':
        print('You have chosen to quit the programm. Bye!!!')
        break
    else:
        continue