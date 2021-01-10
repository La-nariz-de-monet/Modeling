
rules = {}
rfile = open("Instructions.txt", "r")

for line in rfile:
    states = line.split(' ')
    if(states != ['\n']):
        read, write, move = states[1:4]
        if(write == '_'):
            write = ' '
        if(read == '_'):
            read = ' '
        next = states[4][:-1]
        if( states[0] in rules ):
            rules[states[0]][read] = { 'write' : write, 'move' : move, 'next': next }
        else:
            rules[states[0]] = { read : {} }
        rules[states[0]][read] = { 'write' : write, 'move' : move, 'next': next }


from time import time
file_pruebas = open('pruebas.txt', 'r')
#tiempo_by_len = {}
#tiempo_by_len['time'] = []
#by_num_steps = {}
#by_num_steps['steps'] = []
tiempo_by_len = {'longitud='+str(key): [] for key in range(1, 11)}
by_num_steps = {'longitud='+str(key): [] for key in range(1, 11)}
contador = 1 # Para llevar el control de la longitud: 11=2, 21=3, 31=4, 41=5, 51=6, 61=7, 71=8, 81=9, 91=10
for lines in file_pruebas:
    finish = False
    head = 2
    state = '0'
    #print("Write two binary numbers separated by a space")

    #contador = 1 # Para llevar el control de la longitud 11=2; 21=3; 31=4, 41=5, 51=6, 61=7, 71=8, 81=9, 91=10
    timer = [] # Para almacenar los tiempos y obtener el promedio del tiempo
    num_steps = 0 #Para contar el número de pasos
    tmp_steps = []


    line = lines[0:len(lines)-1] #para no leer el salto de linea
    tape = list('  '+str(line)+'  ')
    #print(line)
    start_time = time()
    # Aquí en while es donde se ejecutan las instrucciones para sumar los números
    while(not(finish)):
        #print("eNTRE")
        #num_steps += 1
        #print('State:',state,', head:', head-2, ', tape:', ''.join(tape[:head])+'|'+''.join(tape[head])+'|'+''.join(tape[head+1:]))
        read = tape[head]
        write = rules[state][read]['write']
        move = rules[state][read]['move']
        next = rules[state][read]['next']
        tape[head] = write


        if(move == 'r'):
            head += 1
        elif(move == 'l'):
            head -=1

        state = next
        if state == 'halt-accept':
            #print(num_steps)
            finish = True

        num_steps += 1

    tmp_steps.append(num_steps)
    elapsed_time = time()-start_time
    start_time = 0
    #print(tmp_steps)
    num_steps = 0 # Una vez efectuada la suma, reiniciamos los pasos
    #elapsed_time = time() - start_time # tiempo total
    contador += 1
    timer.append(elapsed_time)

    if contador == 11:
        promedio = float(sum(timer)/len(timer))
        promedio_steps = float(sum(tmp_steps)/len(tmp_steps))
        #tiempo_by_len['time'].append({'longitud=1': promedio})
        tiempo_by_len['longitud=1'].append(promedio)
        #by_num_steps['steps'].append({'longitud=1':promedio_steps})
        by_num_steps['longitud=1'].append(promedio_steps)
        timer = []
        tmp_steps = [] # reiniciamos el arreglo de pasos que nos servira para determinar el promedio

    if contador == 21:
        promedio = float(sum(timer)/len(timer))
        promedio_steps = float(sum(tmp_steps)/len(tmp_steps))
        #tiempo_by_len['time'].append({'longitud=2': promedio})
        tiempo_by_len['longitud=2'].append(promedio)
        #by_num_steps['steps'].append({'longitud=2':promedio_steps})
        by_num_steps['longitud=2'].append(promedio_steps)

        timer = []
        tmp_steps = []

    if contador == 31:
        promedio = float(sum(timer)/len(timer))
        promedio_steps = float(sum(tmp_steps)/len(tmp_steps))
        tiempo_by_len['longitud=3'].append(promedio)
        #tiempo_by_len['time'].append({'longitud=3':promedio})
        #by_num_steps['steps'].append({'longitud=3':promedio_steps})
        by_num_steps['longitud=3'].append(promedio_steps)
        timer = []
        tmp_steps = []

    if contador == 41:
        promedio = float(sum(timer)/len(timer))
        promedio_steps = float(sum(tmp_steps)/len(tmp_steps))
        tiempo_by_len['longitud=4'].append(promedio)
        #tiempo_by_len['time'].append({'longitud=4':promedio})
        #by_num_steps['steps'].append({'longitud=4':promedio_steps})
        by_num_steps['longitud=4'].append(promedio_steps)
        timer = []
        tmp_steps = []

    if contador == 51:
        promedio = float(sum(timer)/len(timer))
        promedio_steps = float(sum(tmp_steps)/len(tmp_steps))
        tiempo_by_len['longitud=5'].append(promedio)
        #tiempo_by_len['time'].append({'longitud=5':promedio})
        #by_num_steps['steps'].append({'longitud=5':promedio_steps})
        by_num_steps['longitud=5'].append(promedio_steps)
        timer = []
        tmp_steps = []

    if contador == 61:
        promedio = float(sum(timer)/len(timer))
        promedio_steps = float(sum(tmp_steps)/len(tmp_steps))
        tiempo_by_len['longitud=6'].append(promedio)
        #tiempo_by_len['time'].append({'longitud=6':promedio})
        #by_num_steps['steps'].append({'longitud=6':promedio_steps})
        by_num_steps['longitud=6'].append(promedio_steps)
        timer = []
        tmp_steps = []


    if contador == 71:
        promedio = float(sum(timer)/len(timer))
        promedio_steps = float(sum(tmp_steps)/len(tmp_steps))
        tiempo_by_len['longitud=7'].append(promedio)
        #tiempo_by_len['time'].append({'longitud=7':promedio})
        #by_num_steps['steps'].append({'longitud=7':promedio_steps})
        by_num_steps['longitud=7'].append(promedio_steps)
        timer = []
        tmp_steps = []

    if contador == 81:
        promedio = float(sum(timer)/len(timer))
        promedio_steps = float(sum(tmp_steps)/len(tmp_steps))
        tiempo_by_len['longitud=8'].append(promedio)
        #tiempo_by_len['time'].append({'longitud=8':promedio})
        #by_num_steps['steps'].append({'longitud=8':promedio_steps})
        by_num_steps['longitud=8'].append(promedio_steps)
        timer = []
        tmp_steps = []

    if contador == 91:
        promedio = float(sum(timer)/len(timer))
        promedio_steps = float(sum(tmp_steps)/len(tmp_steps))
        tiempo_by_len['longitud=9'].append(promedio)
        #tiempo_by_len['time'].append({'longitud=9':promedio})
        #by_num_steps['steps'].append({'longitud=9':promedio_steps})
        by_num_steps['longitud=9'].append(promedio_steps)
        timer = []
        tmp_steps = []

    if contador == 100:
        promedio = float(sum(timer)/len(timer))
        promedio_steps = float(sum(tmp_steps)/len(tmp_steps))
        tiempo_by_len['longitud=10'].append(promedio)
        #tiempo_by_len['time'].append({'longitud=10':promedio})
        #by_num_steps['steps'].append({'longitud=10':promedio_steps})
        by_num_steps['longitud=10'].append(promedio_steps)
        timer = []
        tmp_steps = []


print("Tiempo")
with open('time.txt', 'a') as file:
    for key, value in tiempo_by_len.items():
        value = f'{key} {value[0]}\n'
        file.write(value)


print("Pasos")
with open('steps.txt', 'a') as file:
    for key, value in by_num_steps.items():
        value = f'{key} {value[0]}\n'
        file.write(value)

print("Proceso terminado")
#print('\nFinish head:', head-2, ', tape:', ''.join(tape[:head])+'|'+''.join(tape[head])+'|'+''.join(tape[head+1:]))
