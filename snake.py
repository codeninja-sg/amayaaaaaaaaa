import tinkter as tk
import random

root = tk.(TK)
root.title("Snake - 1")

SIZE = 20
W = 400
H = 400

canvas = tk.Canvas(root, width=W, hight=H, bg="white")
canvas.pack()

snake = [(10, 10)]
dx = 1
dy = 0

food =(random.randint(0, W//SIZE - 1),
       random.randite(0,H//SIZE - 1))

def draw():
    canvas.delete("all")

    fx, fy = food
    canvas.create_rectangle(fx*SIZE, fy*SIZE,
                            fx*SIZE+SIZE, fy*SIZE+SIZE
                            fill="green")
    
    def game_loop():
        global snake, food]
        
