import RPi.GPIO as GPIO                           ## Import GPIO Library.
import time                                 ## Import ‘time’ library for a delay.
from numpy import *

GPIO.setmode(GPIO.BOARD)                    ## Use BOARD pin numbering.
GPIO.setup(16, GPIO.OUT) 
GPIO.setup(18, GPIO.OUT) 
GPIO.setup(22, GPIO.OUT)                    ## set output.
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, GPIO.HIGH)
   
pwmA=GPIO.PWM(16,50) 
pwmA.start(0)
pwmB=GPIO.PWM(18,50)
pwmB.start(0) 
pwmC=GPIO.PWM(22,50)                        ##second parameter is PWM Frequency
pwmC.start(0)

x= 0                             ##giving coordinates of desired point
y= 8
z= 15

La = 8.0                  ##length of link1  
Lb = 10.0		       ##length of link2  
Lc = 5.0                  ##length of link3  

L = sqrt(y*y +z*z)					##inverse kinematics calculations
L0 = sqrt((y-La)*(y-La) + z*z)
Ra = arctan(z/x)
Rb = arccos((La*La + Lb*Lb - L*L)/(2*La*L0)) - arccos((Lb*Lb + L0*L0 -Lc*Lc)/(2*Lb*L0))
Rc = arccos((Lb*Lb + Lc*Lc - L0*L0)/(2*Lb*Lc))

if numpy.isnan(Ra) or numpy.isnan(Rb) or numpy.isnan(Rc):
   while(1):
      GPIO.output(15, GPIO.HIGH)
      time.sleep(5)
else:
   degreeA= degrees(Ra)              ## if degree<90 then simulation will display -(90-degree) | if degree>90 then simulation will display (90-degree)
   degreeB= degrees(Rb)              
   degreeC= degrees(Rc)
	 
   dutyA= float(degreeA)/36.0 + 5  ##degree to duty cycle converson
   dutyB= float(degreeB)/36.0 + 5
   dutyC= float(degreeC)/36.0 + 5

   while(1):
      pwmA.ChangeDutyCycle(dutyA)
      time.sleep(0.03)
      pwmB.ChangeDutyCycle(dutyB)
      time.sleep(0.03)
      pwmC.ChangeDutyCycle(dutyC)
      time.sleep(0.03)
 
time.sleep(1)
GPIO.cleanup()