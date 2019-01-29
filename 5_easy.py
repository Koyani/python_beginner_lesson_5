
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

for i in range(1, 10):
    dir_path = os.path.join(os.getcwd(), 'dir' + str(i))
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('The directory is already exists')
for i in range(1, 10):
    try:
        os.rmdir('dir' + str(i))
    except FileNotFoundError:
        print('No such directory')

def create_directories(name, n):
    import os
    for i in range(1, n):
        dir_path = os.path.join(os.getcwd(), name + str(i))
        print(dir_path)
        try:
            os.mkdir(dir_path)
            print(f'created: {name + str(i)}')
        except FileExistsError:
            print('The directory is already exists')

create_directories('dir_', 100)

def remove_directories (name, n):
    import os
    for i in range(1, n):
        try:
            os.rmdir(name + str(i))
            print(f'removed: {name + str(i)}')
        except FileNotFoundError:
            print('No such directory')
remove_directories('dir_', 100)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os
files = os.listdir(os.getcwd())
for name in files:
    print(name)

import os
def list_directory(path):
    import os
    files = os.listdir(path)
    for name in files:
        print(name)
list_directory("C:\\Users\\molbi\\Desktop\\geekbrains\\python_beginning")
list_directory(os.getcwd())


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil, os, sys
dir_path = os.path.join(os.getcwd(), 'New_Dir')
try:
    os.mkdir(dir_path)
except FileExistsError:
    print('The directory is already exists')
shutil.copy(str(sys.argv[0]),dir_path)
files = os.listdir(os.getcwd())

def copy_current_file(path):
    import shutil, os, sys
    dir_path = os.path.join((path), 'New_Dir')
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('The directory is already exists')
    shutil.copy(str(sys.argv[0]), dir_path)
    files = os.listdir(os.getcwd())

copy_current_file("C:\\Users\\molbi\\Desktop\\geekbrains\\python_beginning\\lesson_5\\")

