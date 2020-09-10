import os
import time

init_time = time.process_time()

mainpath='/home/d3uslinux/Escritorio/'
filename='old amazon combo.txt'
fullpath= os.path.join(mainpath,filename)
emails=[]
with open(fullpath, encoding='latin1') as fichero:
    for linea in fichero:
        email=linea.strip().split(':')[0]
        load_print="Email extraido: {email} {check}".format(email=email, check=u"\u2713")
        print(load_print)
        emails.append(email)
print('--------------------------------------------')
cadena = input("Introduce el email a buscar: ")
print('--------------------------------------------')
if cadena in emails:
    rst = "El email {cadena} EXISTE en la lista de correos cargada".format(cadena=cadena)
    print(rst)
else:
    rst = "El email {cadena} no se encuentra en la lista de correos".format(cadena=cadena)
    print(rst)
elapsed_time = time.process_time() - init_time
print('--------------------------------------------')
rst= 'se procesaron {cantidad} correos, en {elapsed} sg'.format(cantidad=len(emails), elapsed=elapsed_time)
print(rst)

