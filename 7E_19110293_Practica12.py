import matplotlib.pyplot as plt
import pylab
import cv2
import numpy as np
 
img = plt.imread ("Perro.jpg") #Lea la imagen aquí
 
plt.imshow (img) # Muestra la imagen leída
pylab.show()
 
fil = np.array ([[-1, -1, -1], # Este es el filtro establecido, que es el núcleo de convolución
                [ -1, 8, -1],
                [  -1, -1, -1]])
 
res = cv2.filter2D (img, -5, fil) #Utilice la función de convolución de opencv


plt.imshow (res) #Muestra la imagen después de la convolución
plt.imsave("res.jpg",res)
pylab.show()

filtro = np.array ([[0, 1, 0], # Este es el filtro establecido, que es el núcleo de convolución
                    [1, -4, 1],
                    [0, 1, 0]])
 
res2 = cv2.filter2D (img, -1, filtro)

plt.imshow (res2) #Muestra la imagen después de la convolución
plt.imsave("res2.jpg",res2)
pylab.show()

filtro2 = np.array ([[1, 1, 1], # Este es el filtro establecido, que es el núcleo de convolución
                    [1, -7, 1],
                    [1, 1, 1]])
 
res3 = cv2.filter2D (img, -1, filtro2)

plt.imshow (res3) #Muestra la imagen después de la convolución
plt.imsave("res3.jpg",res3)
pylab.show()
