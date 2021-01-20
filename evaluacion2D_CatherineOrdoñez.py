#Graficar lo siguiente: Si el ultimo digito de tu numero de control es impar
# 1. El Centro del primer rectángulo debe tocar una esquina del segundo rectángulo.
# 2. El Centro del circulo debe tocar una esquina del primer rectángulo.
# 3. El radio del circulo debe ser la mitad del lado mas largo del rectángulo.
# 4. Los rectángulos son del mismo tamaño.
# 5. Para sacar el radio del circulo deberás usar el ultimo digito de tu numero de control y multiplicarlo por 5.
# 6. Aplicar Rz=El penúltimo digito de tu numero de control * 6 y posteriormente Sx= El ultimo digito de tu numero de control / 5 y Sy= El penúltimo digito de tu numero de control/5.
# 7. Si cualquier digo usado es 0 entonces usa la unidad para sustituirlo.
# 8. Usar colores basados en tus tres últimos dígitos de tu numero de control divididos entre 10.

#Alumna: Catherine Montserrat Ordoñez Mendoza
# 18390057


#PROFE NO PUDE SUBIRLO AL GIT, NP ENTENDÍ A TIEMPO EL FUNIONAMIENTO Y YA ME QUEDAN POCOS MINUTOS
#ASÍ QUE SE LO MANDO ASÍ. PERDON.

import numpy as np
import matplotlib.pyplot as plt

plt.axis([-100,100,-100,100])
plt.grid(True)
plt.title('Examen 2D Catherine Ordoñez')

#Dibujuar el circulo
xc=0
yc=0
r=7*5

p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100

xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)

for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=xc+r*np.sin(p)
    plt.plot([xlast,xp], [ylast,yp], color=(0,.5,.7))
    xlast=xp
    ylast=yp
        
plt.scatter(xc,yc,s=10, color= 'r')
plt.text(13,3,'r=35', color='k')

#Dibujar el rectangulo central, que tiene al circulo justo en el medio
x1=-35
x2=35
y1=35
y2=-35

plt.plot([x1,x1],[y1,y2],linewidth=1,color=(.5,0,.7))
plt.plot([x2,x2],[y1,y2],linewidth=1,color=(.5,0,.7))
plt.plot([x1,x2],[y1,y1],linewidth=1,color=(.5,0,.7))
plt.plot([x1,x2],[y2,y2],linewidth=1,color=(.5,0,.7))
plt.text(-20,37,'lado 1=r*2=70', color=('k'))

#Cuadro cuya esquina está en el centro del circulo
x=np.array([xc,xc,xc+2*r,xc+2*r,xc])
y=np.array([yc,yc-2*r,yc-2*r,yc,yc])
plt.plot(x,y, color=(.5,.7,0))
plt.text(13,-78,'lado1=lado2=70', color=('k'))

plt.show()


