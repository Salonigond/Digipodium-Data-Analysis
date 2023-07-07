from turtle import*

def square(size, color = 'red'):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        fd(size)
        rt(90)
    end_fill()
    
    
def hexagon(size, color = 'pink'):
    fillcolor(color)
    begin_fill()
    for i in range(6):
        fd(size)
        rt(60)
    end_fill()
    

square(100,'blue')
square(50,'red')
hexagon(100)
hexagon(50)
square(25,'yellow')
end_fill()

mainloop()