# Raspberry Pi Python code
The code for the 3 DOF robotic arm is written in python. 
The code calculates the required joint angles through a given point in space (inverse kinematics) through numpy library.
The calculated angles are then sent as instructions to hobby servo motors.
If the point is beyond robot's workspace then the LED would glow.
## Hardware Requirements
Raspberry Pi, 3 hobby servo motors, LED, Breadboard, jumper wires
