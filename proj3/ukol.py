
alpha = 0.1
gamma = 0.9

pole = [None,
        0.14,0.084,0.07,-0.190,-0.009,
        1,0.147,0.008,-1,-0.498,
        0.640,0.097,-0.101,-0.337,-0.171,
        0.183,0.038,-0.008,-0.067,-0.031]

reward = [None,
          0,0,0,0,0,
          1,0,0,-1,0,
          0,0,0,0,0,
          0,0,0,0,0]

route = [None,1,2,7,8,13,18,17,16,11,6]

counter = 0
for i in range(1,len(route) + 1):
    try:
        # print(pole[route[i]], alpha ,reward[route[i+1]] , gamma*pole[route[i+1]] , pole[route[i]])
        pole[route[i]] =  round(pole[route[i]] + round(alpha*(reward[route[i+1]] + round(gamma*pole[route[i+1]],3) - pole[route[i]]),3),3)
        print(pole[route[i]])
    except IndexError:
        continue

print(pole)