#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Gaston Cebreiro
"""
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

# módulo de SciPy
from scipy import signal as sig

# un módulo adaptado a mis necesidades
from splane import bodePlot, pzmap
#%%  Inicialización de librerías
# Setup inline graphics: Esto lo hacemos para que el tamaño de la salida, 
# sea un poco más adecuada al tamaño del documento
mpl.rcParams['figure.figsize'] = (10,10)

#%% Esto tiene que ver con cuestiones de presentación de los gráficos,
# NO ES IMPORTANTE
fig_sz_x = 14
fig_sz_y = 13
fig_dpi = 80 # dpi

fig_font_family = 'Ubuntu'
fig_font_size = 16

plt.rcParams.update({'font.size':fig_font_size})
plt.rcParams.update({'font.family':fig_font_family})
#%%

#Selecciono los componentes

R3  = 1e3
C   = 1e-6   
#%% Simulamos Fase, Modulo y Diagrama de polos y ceros
wc = - 1/(C*R3)
wp = 1/(C*R3)

num = np.array([ 1, wc ])
den = np.array([ 1, wp ])


H = sig.TransferFunction( num, den )
# Graficamos el diagrama de polos y ceros
# Graficamos la respuesta en frecuencia para el modulo y la fase.
_, axes_hdl = bodePlot(H)

# para que se vea como uno intuye el módulo. Probar comentar las siguientes 2 líneas
plt.sca(axes_hdl[0])
plt.ylim([-1,1])



plt.gca

pzmap(H)

plt.show()

#%% Con valores normalizados en frecuencia
norma = 1e3   #Calculo norma = wo = 1000

wc_n = wc/norma
wp_n = wp/norma

num_n = np.array([ 1, wc_n ])
den_n = np.array([ 1, wp_n ])


Hn = sig.TransferFunction( num_n , den_n )
# Graficamos el diagrama de polos y ceros
# Graficamos la respuesta en frecuencia para el modulo y la fase.
_, axes_hdl = bodePlot(Hn)

# para que se vea como uno intuye el módulo. Probar comentar las siguientes 2 líneas
plt.sca(axes_hdl[0])
plt.ylim([-1,1])

plt.gca

pzmap(Hn)

plt.show()