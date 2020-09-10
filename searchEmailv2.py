import os
import time

init_time = time.process_time()

mainpath='/home/d3uslinux/Escritorio/'
filename='old amazon combo.txt'
fullpath= os.path.join(mainpath,filename)
emails=[]
emails_input=[]
with open(fullpath, encoding='latin1') as fichero:
    for linea in fichero:
        email=linea.strip().split(':')[0]
        load_print="Email extraido: {email} {check}".format(email=email, check=u"\u2713")
        print(load_print)
        emails.append(email)
print('--------------------------------------------')

while True:
    valor=input("Ingresar Email (0 para finalizar):")
    if valor == '0':
        break
    emails_input.append(valor)

print('--------------------------------------------')

rst =[email for email in emails_input if email in emails ]
elapsed_time = time.process_time() - init_time

#print results
for item in rst:
    x = "El email {cadena} EXISTE en la lista de correos cargada".format(cadena=item)
    print(x)
print('--------------------------------------------')
rst= 'Se procesaron {cantidad} correos, en {elapsed} sg'.format(cantidad=len(emails), elapsed=elapsed_time)
print(rst)


