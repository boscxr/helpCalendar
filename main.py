import json
import datetime
import random
from secrets import choice
from telnetlib import SE

with open('data.json', 'r') as f:
    data = json.load(f)
f.close()

selection = None
selection1 = None

my_date = datetime.date.today()
year, week_num, day_of_week = my_date.isocalendar()


random.seed(1) #random number generator
sequence = [i for i in data ['Ayudadores']]
for x in data['Ayudados']:
    while selection == selection1:
        selection=choice(sequence)

    print("Ayudador: "+selection+"\n Ayudado: "+x+"\n No. Semana: "+str(week_num)+"\n")
    selection1 = selection
    week_num += 1


