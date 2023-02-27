#include <math.h>
#define PI 3.141592
import RPi.GPIO as GPIO
from time import sleep
import cv2

#cap = cv2.VideoCapture(0)
demora=1/1000
PI=3.141592653589793
FC_in=18
FC_out=19
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(FC_in,GPIO.IN)
GPIO.setup(FC_out,GPIO.IN)
#def angulo_nema(angulo,sentido):
def angulo_stepper(sentido,angle,motor):
  In1=29
  In2=31
  In3=33
  In4=35
  steps=4096*angle/360
  print(steps)
  i=1
  cont=0
  if(sentido==-1):
      i=1
      while(cont<=steps and GPIO.input(FC_in) and GPIO.input(FC_out)):
        if(i<=8):
          bobinas2(i,motor)
          sleep(demora)
          i+=1
          cont+=1
        else:
          i=1
          bobinas2(i,motor)
          sleep(demora)
          i+=1
          cont+=1
  else:
      i=8
      while(cont<=steps and GPIO.input(FC_in) and GPIO.input(FC_out)):
        if(i>=1):
          bobinas2(i,motor)
          sleep(demora)
          i-=1
          cont+=1
        else:
          i=8
          bobinas2(i,motor)
          sleep(demora)
          i-=1
          cont+=1    
  GPIO.output(In1,0)
  GPIO.output(In2,0)
  GPIO.output(In3,0)
  GPIO.output(In4,0)

def desplazar_stepper(dist,radio,sentido,motor):
  #motor="grua"  
  if(motor=="rotor"):
      In1=29
      In2=31
      In3=33
      In4=35
  elif(motor=="grua"):
      In1=24
      In2=19
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
  i=1
  cont=0
  if(sentido==1):
      i=1
      while(cont<=steps and GPIO.input(FC_in) and GPIO.input(FC_out)):
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
      while(cont<=steps and GPIO.input(FC_in) and GPIO.input(FC_out)):
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
  print(In1)  
  GPIO.output(In1,0)
  GPIO.output(In2,0)
  GPIO.output(In3,0)
  GPIO.output(In4,0)
  
  
# def Encerar():
#     i=1
#     while(1):
#         if(i<=8):
#           bobinas(i)
#           sleep(demora)
#           i+=1
#           cont+=1
#         else:
#           i=1
#           bobinas(i)
#           sleep(demora)
#           i+=1
#           cont+=1
#       if(carrera.lectura):
#           break()   

def bobinas2(n,motor):
    In1=29
    In2=31
    In3=33
    In4=35
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
      
def bobinas(n,motor):
    if(motor=="rotor"):
      In1=29
      In2=31
      In3=33
      In4=35
    if(motor=="grua"):
      In1=24
      In2=19
      In3=21
      In4=23
    elif(motor=="iman"):
      In1=3
      In2=5
      In3=7
      In4=11
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
      
def capturar(cap):
    ret,img = cap.read()
    cv2.imshow('Frame', img)
    cv2.imwrite('/home/pi/Pictures/'+str(num)+'.jpg',img)
    
desplazar_stepper(30,0.5,-1,"grua")
#angulo_stepper(-1,360)
#desplazar_stepper(10,1,1,"iman")
#sleep(1)
#desplazar_stepper(5,1,-1,"iman")
#desplazar_stepper(5,1,-1,"grua")
