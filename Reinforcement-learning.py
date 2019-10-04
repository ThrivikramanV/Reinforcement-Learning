import numpy as np
from pandas import DataFrame

#initialising the rewards
START = 0
BLANK = 0
MINE = -100
POWER = +10
END = +100

#initialising the game environment
game_environ = {0:START, 1:BLANK, 2:MINE, 3:MINE, 4:POWER, 5:MINE, 6:POWER, 7:BLANK, 8:END}

#giving the agent controls/actions
actions = {0:'left',1:'right',2:'up',3:'down'}

#initialising the Q Table - 9 states, 4 actions
Q_table = []
for i in range(9):
    Q_table.append([])
    for j in range(4):
        Q_table[i].append(0)

#learning rate
alpha = 0.05

#discount factor
gamma = 0.8

#epsilon greedy policy - exploration and exploitation trade-off
epsilon = 1000

def movement(s,a):
    if a==0:
        if s!=0 and s!=3 and s!=6:
            s-=1
    if a==1:
        if s!=2 and s!=5 and s!=8:
            s+=1
    if a==2:
        if s!=0 and s!=1 and s!=2:
            s-=3
    if a==3:
        if s!=6 and s!=7 and s!=8:
            s+=3
    return(s)

#training loop - updating the Q Table
#with every step, there is a punishment of -5 points, to ensure minimum no. of steps
#Q Table is printed for every 100 iterations
for i in range(1,1001):
    s=0
    run = True
    while run:
        if epsilon>=500:
            a=np.random.choice(list(actions))
        else:
            a = Q_table[s].index(max(Q_table[s]))
        new_s=movement(s,a)
        if new_s != s:
            Q_table[s][a] = Q_table[s][a] + alpha*( (game_environ[new_s] - 5) + gamma*max(Q_table[new_s]) - Q_table[s][a])
            if new_s==2 or new_s==3 or new_s==5 or new_s==8:
                run = False
            s=new_s
    epsilon-=1
    if i%100==0:
        print(i,'th Iteration',sep='')
        print(DataFrame(Q_table,['S0','S1','S2','S3','S4','S5','S6','S7','S8'],['LEFT','RIGHT','UP','DOWN']))
        print()
