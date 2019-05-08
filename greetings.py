import datetime
from datetime import timedelta
import pandas as pd
import numpy as np

#date vars
now = datetime.datetime.now()
day = now.strftime("%Y-%m-%d")
hour = now.strftime("%H:%M")
weekDay = now.strftime("%A") 
tmrw = datetime.datetime.today()+timedelta(days=1)
tomorow = tmrw.strftime("%Y-%m-%d")
ytd = datetime.datetime.today()+timedelta(days=-1)
yesterday = ytd.strftime("%Y-%m-%d")

#CSV vars 
greetings = pd.read_csv("./data/saludos.csv", delimiter=';') 
people = pd.read_csv("./data/personas.csv", delimiter=';') 
greetings = greetings.dropna()
people = people.dropna()

def dayAndHour():
    msg = str(hour)+'\n'+str(day)
    return msg

def momentOfWeek():
    if weekDay == 'Saturday' or weekDay == 'Sunday':
        index = 'Weekend'
    elif weekDay == 'Friday' and str(hour) > '15:00' :
        index = 'FridayAfternoon'
    else:
        index = weekDay
    return index

def momentOfDay():
    if str(hour) > '08:00' and str(hour) < '10:30':
        index = 'Mañana'
    elif str(hour) > '15:00' and str(hour) < '16:30':
        index = 'Tarde'
    elif str(hour) > '18:30' and str(hour) < '20:30':
        index = 'Noche'
    elif str(hour) > '20:30' and str(hour) < '08:00':
        index = 'Madrugada'
    else:    
        print("Soy hora intermedia") 
        index = ''  
    return index

def getUnkownMessage():
    randomUnknownIndex = np.random.randint(len(greetings['Unknown']))
    mensaje = greetings['Unknown'][randomUnknownIndex]
    return mensaje

def getPersonIdx(name):
    personName = name.replace('_', ' ')
    idx = int(np.flatnonzero(people['Nombre']==personName))
    return idx

def isBirthday(idx):
    años = int(day[:4])-int(people['Cumpleaños'][idx][:4])
    if day[5:] == people['Cumpleaños'][idx][5:]:
        index = 'Cumpleaños'
        ##COJE MENSAJE RANDOM DE LA COLUMNA CUMPLEAÑOS Y añade el mensaje con los años personalizados
        ##saca index random o el del cumple personalizADO?
        if people['Idioma'][idx] =='Euskera':
            mensaje = 'Zorionak'
        else:
            mensaje = '¡Feliz '+str(años)+' '+people['Mote'][idx]+'!'
    elif tomorow[5:] == people['Cumpleaños'][idx][5:]:
        mensaje = people['Mote'][idx] +'\n'+'¡Mañana es tu cumple!'
    elif yesterday[5:] == people['Cumpleaños'][idx][5:]:
        mensaje = people['Mote'][idx]+'\n'+'¿Qué tal tu cumple ayer?'
    else: #No es el cumpleaños      
        mensaje = ''  
    return mensaje

def chooseMessage(idx):
    ##DEFINE PRIORIDADES
    #1. Cumpleaños (dia previo, actual y posterior)
    #2. Llegada trabajo, postComida, hora salida
    #3. mensajes default de los días de la semana
    if len(isBirthday(idx))>0:
        mensaje = isBirthday(idx)
    elif len(momentOfDay())>0:
        momentoDia = momentOfDay()
        randomIndexDia = np.random.randint(len(greetings[momentoDia]))
        mensaje = people['Mote'][idx]+'\n'+greetings[momentoDia][randomIndexDia]
    else:
        momentoSemana = momentOfWeek()
        randomIndexSemana = np.random.randint(len(greetings[momentoSemana]))
        mensaje = people['Mote'][idx]+'\n'+greetings[momentoSemana][randomIndexSemana]

    return mensaje


#print(getUnkownMessage())
#personaReconocida = "Daniel_Molinillo"
#personaReconocida = "Horacio_Panella" 
#idx = getPersonIdx(personaReconocida)
#print(isBirthday(getPersonIdx(personaReconocida)))

#print(chooseMessage(getPersonIdx(personaReconocida)))
#cumpleaños = people['Cumpleaños'][idx]

#momentoDia = momentOfDay()
#momentoSemana = momentOfWeek()
#print('momentoDia',len(momentOfDay())>0)
#print('momentoSemana',momentoSemana)

#randomIndexDia = np.random.randint(len(greetings[momentoDia]))
#print("randomIndex dia",randomIndexDia)
#print("saludo momentoDia",greetings[momentoDia][randomIndexDia])

#randomIndexSemana = np.random.randint(len(greetings[momentoSemana]))
#print("randomIndex semana",randomIndexSemana)
#print("saludo momentoSemana",greetings[momentoSemana][randomIndexSemana])

#print(len(greetings[momentoDia]))
#print('NaN' in greetings[momentoDia])


#print('idx persona',idx)
#print('cumpleaños',cumpleaños[0][:4])
#print('day',day[:4])
#años = int(day[:4])-int(cumpleaños[0][:4])
#print("años", años)
#esCumpleaños = isBirthday(idx)
#print("es cumpleaños?", esCumpleaños)

#print(str(day))
#print(str(hour))
#print("weekDay", str(weekDay))
#print("isWeekend", str(isWeekend))
#print(momentoDelDia)

######PRIORIDADES
# 1. ES CUMPLEAÑOS (DIA PREVIO, DIA CUMPLE, DIA POSTERIOR)
#esCumpleaños = isBirthday(idx) ==> SI NO ES EMPTY ES PRIORIDAD 1
# 2. 


#####MENSAJES SEGUN CONTADOR DE VECES POR DIA POR USUARIO

# 
#    
###si es viernes desde las 14.00 buen finde
###si es viernes por la mañana: buen viernes, ya queda poco
###