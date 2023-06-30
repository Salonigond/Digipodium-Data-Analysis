from turtle import *
speed('fastest')
pencolor('purple')
pensize(2)
for i in range(100):
    fd(100 - i)
    rt(60)
    circle(60,270)
    dot(10,'green')
mainloop()