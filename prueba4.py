import cv2
import time
import numpy as np
import RPi.GPIO as GPIO
from time import sleep
import math
#led_pin=40
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(led_pin,GPIO.OUT)
#pwm_led=GPIO.PWM(led_pin,50)
#pwm_led.start(7.5)
#pwm_led.ChangeDutyCycle(12.5)
#pwm_led=GPIO.PWM(led_pin,0)
demora=1/1000
PI=3.141592653589793
In1=3
In2=5
In3=7
In4=11
step_ang=38
dir_ang=22 
step_dist=32
dir_dist=37
FC1=15
FC2=16
FC3=18
FC4=19
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(dir_ang,GPIO.OUT)
GPIO.setup(step_ang,GPIO.OUT)
GPIO.setup(dir_dist,GPIO.OUT)
GPIO.setup(step_dist,GPIO.OUT)
GPIO.setup(FC1,GPIO.IN)
GPIO.setup(FC2,GPIO.IN)
GPIO.setup(FC3,GPIO.IN)
GPIO.setup(FC4,GPIO.IN)
def angulo_nema(sentido,angle):
    demora_ang=250/1000
    steps=200*angle/(360)
    cont=0
    GPIO.output(dir_ang,sentido)
    print(GPIO.input(FC1))
    while(cont<=steps and GPIO.input(FC2) and GPIO.input(FC2) and GPIO.input(FC3) and GPIO.input(FC4)):
        GPIO.output(step_ang,0)
        GPIO.output(step_ang,1)
        sleep(demora_ang)
        cont+=1
        #print(cont)
    GPIO.output(step_ang,0)
def encerar_ang():
    demora_ang=250/1000
    angle=5
    steps=200*angle/(360)
    cont=0
    angulo_nema(0,230)
    GPIO.output(dir_ang,1)
    while(cont<=steps):
        GPIO.output(step_ang,0)
        GPIO.output(step_ang,1)
        sleep(demora_ang)
        cont+=1
        #print(cont)
    GPIO.output(step_ang,0)    
def desplazar_nema(sentido,dist):
    radio=0.6
    perimetro=2*PI*radio
    angle=360*dist/perimetro
    demora_ang=1/1000
    steps=200*angle/(360)
    cont=0
    print("hola")
    print(GPIO.input(FC2) and GPIO.input(FC2) and GPIO.input(FC3) and GPIO.input(FC4))
    GPIO.output(dir_dist,sentido)
    while(cont<=steps and GPIO.input(FC2) and GPIO.input(FC2) and GPIO.input(FC3) and GPIO.input(FC4)):
        GPIO.output(step_dist,0)
        GPIO.output(step_dist,1)
        sleep(demora_ang)
        cont+=1
        #print(cont)
    GPIO.output(step_dist,0)
def encerar_dist():
    desplazar_nema(1,55)
    radio=0.6
    dist=1
    perimetro=2*PI*radio
    angle=360*dist/perimetro
    demora_ang=1/1000
    steps=200*angle/(360)
    cont=0
    GPIO.output(dir_dist,0)
    while(cont<=steps):
        GPIO.output(step_dist,0)
        GPIO.output(step_dist,1)
        sleep(demora_ang)
        cont+=1
        #print(cont)
    GPIO.output(step_dist,0)
    
def angulo_stepper(sentido,angle,motor):
  In1=3
  In2=5
  In3=7
  In4=11
  steps=4096*angle/360
  print(steps)
  i=1
  cont=0
  if(sentido==0):
      i=1
      while(cont<=steps and GPIO.input(FC2) and GPIO.input(FC2) and GPIO.input(FC3) and GPIO.input(FC4)):
        if(i<=8):
          bobinas(i,motor)
          sleep(demora)
          i+=1
          cont+=1
        else:
          i=1
          bobinas(i,motor)
          sleep(demora)
          i+=1
          cont+=1
  else:
      i=8
      while(cont<=steps and GPIO.input(FC2) and GPIO.input(FC2) and GPIO.input(FC3) and GPIO.input(FC4)):
        if(i>=1):
          bobinas(i,motor)
          sleep(demora)
          i-=1
          cont+=1
        else:
          i=8
          bobinas(i,motor)
          sleep(demora)
          i-=1
          cont+=1    
  GPIO.output(In1,0)
  GPIO.output(In2,0)
  GPIO.output(In3,0)
  GPIO.output(In4,0)

def desplazar_stepper(dist,radio,sentido,motor):
  demora=1/1000
  if(motor=="rotor"):
      In1=29
      In2=31
      In3=33
      In4=35
  elif(motor=="grua"):
      In1=24
      In2=26
      In3=21
      In4=23
  elif(motor=="iman"):
      In1=3
      In2=5
      In3=7
      In4=11
  perimetro=2*PI*radio
  angle=360*dist/perimetro
  print(angle)
  steps=4096*angle/360
  print(steps)
  i=1
  cont=0
  print("FC1")
  print(GPIO.input(FC1))
  print("FC2")
  print(GPIO.input(FC2))
  print("FC3")
  print(GPIO.input(FC3))
  print("FC4")
  print(GPIO.input(FC4))
  if(sentido==1):
      i=1
      print("condicion: {}".format(cont<=steps and GPIO.input(FC1) and GPIO.input(FC2) and GPIO.input(FC3) and GPIO.input(FC4)))
      while(cont<=steps and GPIO.input(FC2) and GPIO.input(FC2) and GPIO.input(FC3) and GPIO.input(FC4)):
        if(i<=8):
          bobinas(i,motor)
          sleep(demora)
          i+=1
          cont+=1
        else:
          i=1
          bobinas(i,motor)
          sleep(demora)
          i+=1
          cont+=1
  else:
      print("condicion: {}".format(cont<=steps and GPIO.input(FC1) and GPIO.input(FC2) and GPIO.input(FC3) and GPIO.input(FC4)))
      i=8
      while(cont<=steps and GPIO.input(FC2) and GPIO.input(FC2) and GPIO.input(FC3) and GPIO.input(FC4)):
        if(i>=1):
          bobinas(i,motor)
          sleep(demora)
          i-=1
          cont+=1
        else:
          i=8
          bobinas(i,motor)
          sleep(demora)
          i-=1
          cont+=1
  print(In2)    
  GPIO.output(In1,0)
  GPIO.output(In2,0)
  GPIO.output(In3,0)
  GPIO.output(In4,0)
  
def bobinas(n,motor):
    if(motor=="iman"):
      In1=3
      In2=5
      In3=7
      In4=11
    if(motor=="grua"):
      In1=24
      In2=26
      In3=21
      In4=23
    print(n) 
    if(n==1):
      GPIO.output(In1,1)
      GPIO.output(In2,0)
      GPIO.output(In3,0)
      GPIO.output(In4,0)
      
    elif(n==2):
      GPIO.output(In1,1)
      GPIO.output(In2,1)
      GPIO.output(In3,0)
      GPIO.output(In4,0)
      
    elif(n==3):
      GPIO.output(In1,0)
      GPIO.output(In2,1)
      GPIO.output(In3,0)
      GPIO.output(In4,0)
      
    elif(n==4):
      GPIO.output(In1,0)
      GPIO.output(In2,1)
      GPIO.output(In3,1)
      GPIO.output(In4,0)
      
    elif(n==5):
      GPIO.output(In1,0)
      GPIO.output(In2,0)
      GPIO.output(In3,1)
      GPIO.output(In4,0)
      
    elif(n==6):
      GPIO.output(In1,0)
      GPIO.output(In2,0)
      GPIO.output(In3,1)
      GPIO.output(In4,1)
      
    elif(n==7):
      GPIO.output(In1,0)
      GPIO.output(In2,0)
      GPIO.output(In3,0)
      GPIO.output(In4,1)
      
    elif(n==8):
      GPIO.output(In1,1)
      GPIO.output(In2,0)
      GPIO.output(In3,0)
      GPIO.output(In4,1)
#angulo_nema(0,45)
#angulo_stepper(1,360)
#desplazar_stepper(30,1,1,"iman")
#angulo_stepper(0,360*2,"iman")
#desplazar_nema(0,20)

GPIO.setup(40,GPIO.OUT)
GPIO.output(40,0)
encerar_dist()
sleep(2)
encerar_ang()
#angulo_nema(1,45)
#sleep(1)
#desplazar_nema(0,20)
def capturar(cap):
    ret,img = cap.read()
    cv2.imshow('Frame', img)
    cv2.imwrite('/home/pi/Pictures/'+str(num)+'.jpg',img)
GPIO.setup(40,GPIO.OUT)
GPIO.output(40,0)
num = 1
cap = cv2.VideoCapture(0)
colores = input("Ingrese un color (Rojo,Azul,Amarillo): ")
#capturar(cap)

while True:
    ret,img = cap.read()
    cv2.imshow('Frame', img)
    if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite('/home/pi/Pictures/'+str(num)+'.jpg',img)
            print('Capture '+str(num)+' Listo!')
            num = num + 1
    if num==2:
            break
cap.release()
cv2.destroyAllWindows()

# if colores=="Azul":
#     colorbajo = np.array([100,100,20],np.uint8) #azulbajo
#     coloralto = np.array([125,255,255],np.uint8) #azulalto
# elif colores=="Amarillo":
#     colorbajo = np.array([15,100,20],np.uint8) #amarillobajo
#     coloralto = np.array([45,255,255],np.uint8) #amarilloalto
# elif colores=="Rojo":
#     colorbajo = np.array([175,100,20],np.uint8) #rojobajo
#     coloralto = np.array([179,255,255],np.uint8) #rojoalto
# 
# recorrido = 0

if colores=="Azul":
    x=-5
    y=-5
    azulbajo = np.array([100,100,20],np.uint8) #azulbajo
    azulalto = np.array([125,255,255],np.uint8) #azulalto

    im = cv2.imread('/home/pi/Pictures/1.jpg')
    frameHSV = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,azulbajo,azulalto)
    contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
    for c in contornos:
      area = cv2.contourArea(c)
      if area > 2:
        M = cv2.moments(c)
        if (M["m00"]==0): M["m00"]=1
        x = int(M["m10"]/M["m00"])
        y = int(M['m01']/M['m00'])
        print(x)
        print(y)
        cv2.circle(im, (x,y), 7, (0,255,0), -1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(im, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
        nuevoContorno = cv2.convexHull(c)
        cv2.drawContours(im, [nuevoContorno], 0, (255,0,0), 3)
        

    height, width = im.shape[:2] 

    print("The height of the image is: ", height) 
    print("The width of the image is: ", width) 

    if(x>0 and y>0):
        xfinal = x
        yfinal = y
        xdig = xfinal
        ydig = height-yfinal
        print(xdig)
        print(ydig)
        yanalog = (ydig*28)/height
        xanalog = (xdig*39)/width
        print(yanalog)
        print(xanalog)
        xanalogf = abs(19.5-xanalog)
        yanalogf = yanalog
        print("y",yanalogf)
        print("x",xanalogf)
        # Sacamos Angulo y recorrido
        angulo = (np.arctan((yanalogf+11)/xanalogf))*180/3.141592653589793
        if(xanalog>19.5):
            angulofinal = angulo
        else:
            angulofinal = 180-angulo
        recorrido = np.sqrt((xanalogf**2)+(yanalogf**2))
        print(angulo)
        print("El RECORRIDO POR EL MOTOR DE PASO ES", recorrido)
        print("El ANGULO FINAL ES", angulofinal)
        ciclo = round((angulofinal/18)+2.5,2)
        print(ciclo)
        ciclo2 = 9
        recorrido2 = 8-recorrido
    else:
        print("No se encontro nada")
        
elif colores=="Amarillo":
    x=-5
    y=-5
    amarillobajo = np.array([15,100,20],np.uint8) #amarillobajo
    amarilloalto = np.array([45,255,255],np.uint8) #amarilloalto

    im = cv2.imread('/home/pi/Pictures/1.jpg')
    frameHSV = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,amarillobajo,amarilloalto)
    contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
    for c in contornos:
      area = cv2.contourArea(c)
      if area > 2:
        M = cv2.moments(c)
        if (M["m00"]==0): M["m00"]=1
        x = int(M["m10"]/M["m00"])
        y = int(M['m01']/M['m00'])
        print(x)
        print(y)
        cv2.circle(im, (x,y), 7, (0,255,0), -1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(im, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
        nuevoContorno = cv2.convexHull(c)
        cv2.drawContours(im, [nuevoContorno], 0, (255,0,0), 3)
        

    height, width = im.shape[:2] 

    print("The height of the image is: ", height) 
    print("The width of the image is: ", width) 
    
    if(x>0 and y>0):
        xfinal = x
        yfinal = y
        xdig = xfinal
        ydig = height-yfinal
        print(xdig)
        print(ydig)
        yanalog = (ydig*28)/height
        xanalog = (xdig*39)/width
        print(yanalog)
        print(xanalog)
        xanalogf = abs(19.5-xanalog)
        yanalogf = yanalog
        print("y",yanalogf)
        print("x",xanalogf)
        # Sacamos Angulo y recorrido
        angulo = (np.arctan((yanalogf+11)/xanalogf))*180/3.141592653589793
        if(xanalog>19.5):
            angulofinal = angulo
        else:
            angulofinal = 180-angulo
        recorrido = np.sqrt((xanalogf*2)+(yanalogf*2))
        print(angulo)
        print("El RECORRIDO POR EL MOTOR DE PASO ES", recorrido)
        print("El ANGULO FINAL ES", angulofinal)
        ciclo = round((angulofinal/18)+2.5,2)
        print(ciclo)
        ciclo2 = 7.5
        recorrido2 = 7-recorrido
    else:
        print("No se encontro nada")


elif colores=="Rojo":
    x=-5
    y=-5
    rojobajo = np.array([175,100,20],np.uint8) #rojobajo
    rojoalto = np.array([179,255,255],np.uint8) #rojoalto
    
    im = cv2.imread('/home/pi/Pictures/1.jpg')
    frameHSV = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,rojobajo,rojoalto)
    contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
    for c in contornos:
      area = cv2.contourArea(c)
      if area > 2:
        M = cv2.moments(c)
        if (M["m00"]==0): M["m00"]=1
        x = int(M["m10"]/M["m00"])
        y = int(M['m01']/M['m00'])
        print(x)
        print(y)
        cv2.circle(im, (x,y), 7, (0,255,0), -1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(im, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
        nuevoContorno = cv2.convexHull(c)
        cv2.drawContours(im, [nuevoContorno], 0, (255,0,0), 3)
        

    height, width = im.shape[:2] 

    print("The height of the image is: ", height) 
    print("The width of the image is: ", width) 

    if(x>0 and y>0):
        xfinal = x
        yfinal = y
        xdig = xfinal
        ydig = height-yfinal
        print(xdig)
        print(ydig)
        yanalog = (ydig*28)/height
        xanalog = (xdig*39)/width
        print(yanalog)
        print(xanalog)
        xanalogf = abs(19.5-xanalog)
        yanalogf = yanalog
        print("y",yanalogf)
        print("x",xanalogf)
        # Sacamos Angulo y recorrido
        angulo = (np.arctan((yanalogf)/xanalogf))*180/3.141592653589793
        finalangulo = (np.arctan(((yanalogf+11))/xanalogf))*180/3.141592653589793
        if(xanalog>19.5):
            angulofinal = finalangulo
        else:
            angulofinal = 180-finalangulo
        recorrido = np.sqrt((xanalogf**2)+((yanalogf)**2))
        print(angulo)
        print("El RECORRIDO POR EL MOTOR DE PASO ES", recorrido)
        print("El ANGULO FINAL ES", angulofinal)
    
        #hipotenusa = (yanalogf+2)/math.sin(angulofinal)
        #print(hipotenusa)
        #valorD = hipotenusa-7
        #print("valor de d",valorD)
        
    else:
        print("No se encontro nada")

if(x>0 and y>0):
    #pwm_led=GPIO.PWM(led_pin,50)

    #desfase=20-20*angulofinal/180
    #angulo_nema(1,angulofinal+desfase)
   
    
    angulo_nema(1,angulofinal+10)
    desplazar_nema(0,recorrido)
    sleep(2)
    #pwm_led=GPIO.PWM(led_pin,0)
    #angulo_stepper(1,360*3,"iman")
    #sleep(1)
    GPIO.output(40,1)
    sleep(6)
    GPIO.output(40,0)
    #angulo_stepper(-1,360*3,"iman")
    #angulo_nema(0,angulofinal)
    #desplazar_nema(1,recorrido)
    #GPIO.output(40,0)
    
    
    
    
    #sleep(1)
    #desplazar_stepper(5,1,-1,"iman")

    #desplazar_stepper(recorrido2,0.2,1,"grua")
    #desplazar_stepper(5,1,1,"iman")
    #sleep(1)
    #desplazar_stepper(5,1,-1,"iman")



