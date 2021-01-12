# Archivo para hacer las gráficas
def element_to_graph(file_name):
    """Function to generate x and y axis
    file_name = str file name
    """
    with open(file_name, 'r') as file:
        lineas = file.readlines()
        x_longitud = [i for i in range(1,11)]
        y_steps = {k: [] for k in range(1,11)}

        for linea in lineas:
            longitud, pasos = linea.split(' ')
            if longitud == 'longitud=1':
                y_steps[1].append(float(pasos[:-1]))
            elif longitud == 'longitud=2':
                y_steps[2].append(float(pasos[:-1]))
            elif longitud == 'longitud=3':
                y_steps[3].append(float(pasos[:-1]))
            elif longitud == 'longitud=4':
                y_steps[4].append(float(pasos[:-1]))
            elif longitud == 'longitud=5':
                y_steps[5].append(float(pasos[:-1]))
            elif longitud == 'longitud=6':
                y_steps[6].append(float(pasos[:-1]))
            elif longitud == 'longitud=7':
                y_steps[7].append(float(pasos[:-1]))
            elif longitud == 'longitud=8':
                y_steps[8].append(float(pasos[:-1]))
            elif longitud == 'longitud=9':
                y_steps[9].append(float(pasos[:-1]))
            elif longitud == 'longitud=10':
                y_steps[10].append(float(pasos[:-1]))

    for key, values in y_steps.items():
        y_steps[key] = sum(values)/len(values)
    
    y_step = list(y_steps.values())

    return(x_longitud, y_step)


import matplotlib
import matplotlib.pyplot as plt
x,y = element_to_graph('time.txt')
fig, ax = plt.subplots()
#Colocamos una etiqueta en el eje Y
ax.set_ylabel('Tiempo (s)')
#Colocamos una etiqueta en el eje X
ax.set_xlabel('Longitud de cadena')
ax.set_title('Tiempo para resolver la suma binaria')
#Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
plt.bar(x, y)
#plt.savefig('barras_simple.png')
plt.show()
