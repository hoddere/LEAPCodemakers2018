from turtle import *
from random import choice

bc = 'bluecar100x050.gif'; gc = 'greencar100x050.gif'
oc = 'orangecar100x050.gif'; rc = 'redcar100x050.gif'
yc = 'yellowcar100x050.gif'
rm = 'redmotorcycle060x044.gif'; tm = 'twomotorcycle060x042.gif'
bt = 'browntruck180x090.gif'; wt = 'whitetruck180x095.gif'

def setup_dock():
    global left_remain, right_remain
    clearscreen();
    bgpic('background.gif'); setup(width=1440, height=820)
    title("Load the Ferry!"); hideturtle()
    register_shape(bc); register_shape(gc)
    register_shape(oc); register_shape(rc)
    register_shape(yc)
    register_shape(rm); register_shape(tm)
    register_shape(bt); register_shape(wt)
    left_remain, right_remain = 24, 24

class Vehicle(Turtle):
    # pointing to the right, origin at the front
    def __init__(self, typ):
        Turtle.__init__(self, visible=False)
        self.shape(typ); self.up()
        self.height, self.width = int(typ[-7:-4]), int(typ[-11:-8])
        self.goto(- self.width // 2 - 720, self.height // 2 - 70)
        self.showturtle(); self.speed(1)
    def move_up(self, dx):
        self.forward(dx * 20)
    def board_left(self):
        global left_remain
        self.setheading(35); self.forward(9 * 20); self.setheading(0)
        self.forward((2 + left_remain) * 20)
        left_remain = left_remain - self.length()        
    def board_right(self):
        global right_remain
        self.forward((6 + right_remain) * 20)
        right_remain = right_remain - self.length()
    def length(self):
        return self.width // 20

def write_result():
    penup(); goto(-640, 300); pendown()
    if left_remain < 0: s = "Left left overfull by: %s\n" % -left_remain
    else: s = "Remaining on left lane: %s\n" % left_remain
    if right_remain < 0: s = s + "Right lane overfull by: %s\n" % -right_remain
    else: s = s + "Remaining on right lane: %s" % right_remain
    write(s, font=("Arial", 24, "bold"))

def operator():
    for i in range(len(queue)):            # for all vehicles in the queue
        if choice([True, False]):          # flip coin and
            queue[i].board_left()          # either board on the left
        else: queue[i].board_right()       # or board on the right
        for j in range(i + 1, len(queue)): # for all remaining vehicles
            queue[j].move_up(queue[i].length()) # move up by length of boarding vehicle

def random_queue():
    global queue
    setup_dock()
    queue, end = [], 36 # (visible) queue is 36m long
    for i in range(10): # random choice of 10 vehicles
        v = Vehicle(choice([bc, gc, oc, rc, yc, rm, tm, bt, wt]))
        v.move_up(end)
        end = end - v.length()
        queue.append(v)
    operator()
    write_result()

def test1():
    global queue
    setup_dock()
    end = 36 # (visible) queue is 36m long
    queue = [Vehicle(bt), Vehicle(oc), Vehicle(gc), Vehicle(bc), Vehicle(wt),
             Vehicle(rm), Vehicle(tm), Vehicle(wt)]
    for v in queue:
        v.move_up(end)
        end = end - v.length()
    operator()
    write_result()
    
def test2():
    global queue
    setup_dock()
    end = 36 # (visible) queue is 36m long
    queue = [Vehicle(wt), Vehicle(tm), Vehicle(rc), Vehicle(yc), Vehicle(rm),
             Vehicle(tm), Vehicle(yc), Vehicle(rc), Vehicle(oc), Vehicle(bc)]
    for v in queue:
        v.move_up(end)
        end = end - v.length()
    operator()
    write_result()
    
def test3():
    global queue
    setup_dock()
    end = 36 # (visible) queue is 36m long
    queue = [Vehicle(bt), Vehicle(bc), Vehicle(rm), Vehicle(tm), Vehicle(gc),
             Vehicle(oc), Vehicle(rc), Vehicle(yc), Vehicle(rm), Vehicle(tm),
             Vehicle(rm)]
    for v in queue:
        v.move_up(end)
        end = end - v.length()
    operator()
    write_result()
    
def test4():
    global queue
    setup_dock()
    end = 36 # (visible) queue is 36m long
    queue = [Vehicle(gc), Vehicle(oc), Vehicle(bt), Vehicle(rm), Vehicle(rc),
             Vehicle(yc), Vehicle(rm), Vehicle(rm), Vehicle(rm), Vehicle(rm),
             Vehicle(bc)]
    for v in queue:
        v.move_up(end)
        end = end - v.length()
    operator()
    write_result()
    
def test5():
    global queue
    setup_dock()
    end = 36 # (visible) queue is 36m long
    queue = [Vehicle(oc), Vehicle(bt), Vehicle(rc), Vehicle(wt), Vehicle(yc),
             Vehicle(rm), Vehicle(bc)]
    for v in queue:
        v.move_up(end)
        end = end - v.length()
    operator()
    write_result()
    
