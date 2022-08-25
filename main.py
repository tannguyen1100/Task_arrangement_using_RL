import csv
from q_table import QTable
from task import Task
from computer import Computer
from function import OptimizationRL, LinearSearch
import random, time
import matplotlib.pyplot as plt
import numpy as np


# random.seed(8)
random.seed(88)
tasks = []
computers= []
qTables = []

TASK_NUM = 10
COMPUTER_NUM = 5

for i in range(COMPUTER_NUM):
    c = Computer(id=i+1, name=f"C{i+1}")
    computers.append(c)

for i in range(TASK_NUM):
    t = Task(id=i+1)
    number_of_choices = random.randint(1, 3)
    random_choices = random.sample(computers, number_of_choices)
    t.setDesComputers(sorted(random_choices, key=lambda x: x.getId()))
    tasks.append(t)


i = 1
for t in tasks:
    for c in t.getDesComputers():
        tProc = random.randint(1,5)
        qTables.append(QTable(id=i, computer=c, task=t, tProc=tProc))
        i = i + 1

with open('action.csv', 'w', newline="") as f:
    header = ['task', 'computer', 'action', 'time']
    writer = csv.writer(f)
    writer.writerow(header)
    for q in qTables:
        writer.writerow([q.getTask(), q.getComputer(), q.getLabel(), q.getTProc()])
        

"""
    Linear Search
"""

# print("LN Search")
# start_time = time.time()
best_action_LN, tserLN = LinearSearch(tasks, qTables)
# print("time processing: ", end="")
# print(f"{(time.time() - start_time)} seconds")
# print(f"best_run: {best_action_LN} in {tserLN} ts")
# print("-------------------------")


'''
    RL optimazation
'''

limit_tser = [9.5, 13, 30]
alpha = 0.1
epsilon = 0.1
episode = 100

start_time = time.time()



#change time limit

# 1 seed
# random.seed()
# fig = plt.figure()
# xpoints = np.array(range(1,episode+1))
# axes = fig.subplots(nrows=1, ncols=3)
# fig.suptitle('Time limit parameter')


# i = 0
# for tl in limit_tser:
#     for q in qTables:
#         q.setValue(0)

#     meet_episode, tserRL, optimal_run, Q_table = OptimizationRL(tasks, qTables,tl, alpha, episode, epsilon)
#     sumQ = []

#     print("RL optimization")
#     print("time processing: ", end="")
#     print(f"{(time.time() - start_time)} seconds")
#     print(f"best_run: {optimal_run} in {tserRL} ts in episode {meet_episode}")

#     for q in Q_table:
#         sumQ.append(sum(q))

#     ypoints = np.array(sumQ)
#     axes[i].set_title(f'Scenario {i+1}: time limit = {tl}')
#     axes[i].set(xlabel='episode', ylabel='Sum of V')
#     axes[i].plot(xpoints,ypoints)
#     i = i + 1

# plt.show()



#random 100


number_of_test = 100
fig = plt.figure()
xpoints = np.array(range(1,number_of_test+1))
axes = fig.subplots(nrows=1, ncols=3)
fig.suptitle('How close of the result')

j = 0
for tl in limit_tser:
    tserRL_arr = []
    # print(f"RL optimization tl = {tl}")
    for i in range(number_of_test):

        for q in qTables:
            q.setValue(0)
        
        random.seed()

        meet_episode, tserRL, optimal_run, Q_table = OptimizationRL(tasks, qTables,tl, alpha, episode, epsilon)
        tserRL_arr.append(abs(tserRL - tserLN))

        ypoints = np.array(tserRL_arr)

        
    axes[j].set_title(f'Scenario {j+1}: time limit = {tl}')
    axes[j].set(xlabel='Test number', ylabel='|optimal time - best time|')
    axes[j].plot(xpoints,ypoints, 'o', markersize=2)
    j = j + 1

plt.show()
          
                
               

    

