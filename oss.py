import os

# print(os.getcwd())

# تغییر فایل اجرای پایتون
# os.chdir('/home/mohammadgoodarzi/Desktop/project_python')
# print(os.getcwd())

# چه متویاتی وجود دارد
# print(os.listdir())

# ایجاد پوشه
# os.mkdir('test')

# ایجاد پوشه های تو در تو
# os.makedirs('test/test2')

# حذف یک پوشه
# os.rmdir('test')

# حذف پوشه های تو در تو
# os.removedirs('test/test2')

# تغییر نام یک فایل
# os.rename('1.py', 'question_1.py')

# environ variable
# print(os.environ)

# practice with madule os
# print(os.getcwd())

# os.chdir('../../')
# print(os.getcwd())

# name = ['mohamad', 'ali', 'reza', 'alireza']
# print(sorted(name))


def vi(file_name):
    if not os.path.exists(file_name):
        raise Exception('File Does Not Exist')
    else:
        while True:
            type_here = input('')
            if type_here == '!q':
                break
            elif type_here == 'cat':
                print(type_here)
            elif type_here == 'close':
                pass


# f1 = vi('./test')


def rm(file_name, folder):
    current_folder = '/home/mohammadgoodarzi/Desktop/project_python/mini_linux'
    folder = current_folder
    if not os.path.exists(file_name):
        raise Exception('File Does Not Exist')
    else:
        os.remove(file_name)


# remove_file = rm('test')

# my_tuple = ("apple", "banana", "cherry")
#
# print(len(my_tuple[0]))







