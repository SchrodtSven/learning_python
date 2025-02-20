from turtle import Turtle
from random import random

# t = Turtle()
# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)


star = Turtle() 

star.right(75) 
star.forward(100) 

for i in range(4): 
	star.right(144) 
	star.forward(100) 
star.screen.mainloop()

