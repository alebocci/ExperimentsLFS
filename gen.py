import shutil
import secrets
import math
import os

infrTemplate = 'infr_template.yaml'
tempConf='tmpConf.txt'
configTemplate='config_template.yaml'
tempSim='tmpSim.txt'

if not os.path.exists("input"):
    os.mkdir('input')

os.chdir('input')
if not os.path.exists("points"):
    os.mkdir('points')
if not os.path.exists("experiments"):
    os.mkdir('experiments')
os.chdir('..')



seeds = []
for i in range(0,10):
    seeds.append(secrets.randbelow(1_000_000_000))


cloud = 1
fog = 7
edge = 14

config = []
tot = 50

def findConf(tot):
    c = math.ceil(tot/22)
    f = math.ceil(tot/22*7)
    e = tot - c - f
    return (c,f,e, tot)

while(tot<=220):
    config.append(findConf(tot))
    tot += 5

for c in config:
    with open(tempConf,'w') as t:
        t.write('number_of_nodes:\n  cloud: '+str(c[0])+'\n  fog: '+str(c[1])+'\n  edge: '+str(c[2])+'\n\n')

    os.chdir('input')
    os.chdir('points')
    with open(str(c)+'.yaml','wb') as dest:
        os.chdir('..')
        os.chdir('..')
        with open(tempConf,'rb') as head:
            with open(infrTemplate, 'rb') as tail:
                shutil.copyfileobj(head,dest)
                shutil.copyfileobj(tail,dest)

for s in seeds:
    with open(tempSim,'w') as t:
        t.write('simulator:\n  epochs : 200\n  function_duration : 1\n  seed : '+str(s)+'\n  use_padding : true\n  max_placement_time : 1\n\n')

    os.chdir('input')
    os.chdir('experiments')
    with open(str(s)+'_pad.yaml','wb') as dest:
        os.chdir('..')
        os.chdir('..')
        with open(tempSim,'rb') as head:
            with open(configTemplate, 'rb') as tail:
                shutil.copyfileobj(head,dest)
                shutil.copyfileobj(tail,dest)

for s in seeds:
    with open(tempSim,'w') as t:
        t.write('simulator:\n  epochs : 200\n  function_duration : 1\n  seed : '+str(s)+'\n  use_padding : false\n  max_placement_time : 1\n\n')

    os.chdir('input')
    os.chdir('experiments')
    with open(str(s)+'_nopad.yaml','wb') as dest:
        os.chdir('..')
        os.chdir('..')
        with open(tempSim,'rb') as head:
            with open(configTemplate, 'rb') as tail:
                shutil.copyfileobj(head,dest)
                shutil.copyfileobj(tail,dest)