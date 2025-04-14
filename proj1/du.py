import math

mapa = [[9,8,7,7,9,'Z',8,8,8,8],
        [9,9,9,9,9,'Z',7,6,8,8],
        [9,9,9,9,9,'Z',9,9,9,9],
        [7,9,'Z','Z','Z','Z','Z','Z','Z',9],
        [6,9,9,9,8,'Z',6,2,'Z',9],
        [3,3,3,3,3,'Z',4,5,'Z',9],
        [7,9,7,4,9,3,3,3,3,3],
        [9,8,8,2,9,'Z',8,8,9,9],
        [8,7,'Z','Z','Z','Z',7,5,6,6],
        [9,7,8,7,8,'Z',5,7,7,7]]

open = []
closed = []

bod1 = {
    "x" : 3,
    "y" : 7, 
    "value" : 2
}

bod2 = {
    "x" : 7,
    "y" : 4,
    "value": 'Z'
}


def count_heuristic(start_x,start_y,end_x,end_y):
    x = pow(end_x-start_x,2)
    x = x +pow(end_y-start_y,2)
    x = math.sqrt(x)
    x = abs(x)
    return x

class Square:
    def __init__(self, x, y,entry_value):
        self.x = x
        self.y = y
        self.entry_value = entry_value
        self.h = count_heuristic(x,y,7,4)
        self.g = 0
        self.f = self.g+self.h
        self.parent = "nic"
    
    def __str__(self):
        if (self.parent == "nic"):
            return "[" + str(self.x)+ ", " + str(self.y) + "], " + str(round(self.f,2))
        return "[" + str(self.x)+ ", " + str(self.y) + "], " + str(round(self.f,2)) + ", [" + str(self.parent.x)+ ", " + str(self.parent.y) + "]"



def find_lowest_f():
    global open
    if(bool(open) == False):
       return
    lowest = open[0]
    for i in open:
        if(lowest.f > i.f):
            lowest = i
    return lowest
    
def is_end(square):
    if(square.x == 7 and square.y == 4):
        return True
    else:
        return False

def find_neighbours(square):
    neighobours = []
    if(square.x-1>=0 and square.y - 1 >= 0):
        neighobours.append(all[square.x-1][square.y-1])
        # print( str(square.x-1) + str(square.y-1))

    if(square.x >=0 and square.y - 1 >= 0):
        neighobours.append(all[square.x][square.y-1])
        # print( str(square.x) + str(square.y-1))


    if(square.x+1<=9 and square.y - 1 >= 0):
        neighobours.append(all[square.x+1][square.y-1])
        # print( str(square.x+1) + str(square.y-1))


    if(square.x-1>=0 and square.y  >= 0):
        neighobours.append(all[square.x-1][square.y])
        # print( str(square.x-1) + str(square.y))


    if(square.x+1<=9 and square.y  >= 0):
        neighobours.append(all[square.x+1][square.y])
        # print( str(square.x+1) + str(square.y))


    if(square.x-1>=0 and square.y + 1 <= 9):
        neighobours.append(all[square.x-1][square.y+1])
        # print( str(square.x-1) + str(square.y+1))


    if(square.x>=0 and square.y + 1 <= 9):
        neighobours.append(all[square.x][square.y+1])
        # print( str(square.x) + str(square.y+1))

    if(square.x+1<=9 and square.y + 1 <= 9):
        neighobours.append(all[square.x+1][square.y+1])
        # print( str(square.x+1) + str(square.y+1))

    return neighobours

# square1 = Square(3,7,2)
# square2 = Square(7,4,'Z')
# 
# print(square1.h)

def g_toho_v_open(square):
    global open
    for i in open:
        if(i.x == square.x and i.y == square.y):
            return i.g
    #error
    return 0

def is_in_open(square):
    global open
    for i in open:
        if(i.x == square.x and i.y == square.y):
            return True
    return False

all = []
for i in range(0,10):
    sub = []
    for j in range(0,10):
        sub.append(Square(i,j,mapa[j][i]))
    all.append(sub)

#algo
#start to open
open.append(all[3][7])



current = ""
count = 1
while True:
    current = find_lowest_f()
# 
    # print("#####")
    # print(current)
    # print("#####")
    count = count + 1
    print("\n\n\n")
    print("iterace" + str(count))
    open.remove(current)
    print("remove:",end=" ")
    print(current)

    closed.append(current)


    if(is_end(current)):
        break

    neighbours = find_neighbours(current)

    for neighbour in neighbours:

        if(neighbour in closed or neighbour.entry_value == 'Z'):
            continue

        if(is_in_open(neighbour)==False or neighbour.g < g_toho_v_open(neighbour)):
    
            neighbour.parent = current
            neighbour.g = neighbour.entry_value + neighbour.parent.g
            neighbour.f = neighbour.h + neighbour.g
            if(is_in_open(neighbour)==False):
                open.append(neighbour)
                print("new:",end=" ")
                print(neighbour)
            # print(neighbour)

    # for i in open:
        # print(i)

# print(current)
# print(current.parent)
# print(current.parent.parent)
# print(current.parent.parent.parent)
# print(current.parent.parent.parent.parent)
# print(current.parent.parent.parent.parent.parent)


