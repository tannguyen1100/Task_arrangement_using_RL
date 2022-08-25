import random
from csv import reader, writer
random.seed()

def getTProcMax(choseComputers, qTables):
    tser = 0
    temp_computer_tProc = {}
    for i in range(len(choseComputers)):
        label = f"{i+1}{choseComputers[i]}"
        q = next(filter(lambda x: x.getLabel() == label, qTables))
        if q.getComputer().getId() in temp_computer_tProc.keys():
            temp_computer_tProc[choseComputers[i]] = temp_computer_tProc[choseComputers[i]] + q.getTProc()
        else:
            temp_computer_tProc[choseComputers[i]] = q.getTProc()
        
    tser = max(temp_computer_tProc.values())
    return tser

def getTProc(choseComputers, qTables):
    tser = 0
    temp_computer_tProc = {}
    for i in range(len(choseComputers)):
        label = f"{i+1}{choseComputers[i]}"
        q = next(filter(lambda x: x.getLabel() == label, qTables))
        if q.getComputer().getId() in temp_computer_tProc.keys():
            temp_computer_tProc[choseComputers[i]] = temp_computer_tProc[choseComputers[i]] + q.getTProc()
        else:
            temp_computer_tProc[choseComputers[i]] = q.getTProc()
        
    tser = sum(temp_computer_tProc.values())
    return tser

def addOne(array, limit):
    check = True
    i = 1
    global check_overflow 
    check_overflow = False
    if len(array) == 0:
        check_overflow = True
    while(check and (len(array) != 0)):
        if array[-i] + 1 < limit[-i]:
            array[-i] = array[-i] + 1
            check = False
        else:
            array[-i] = 0
            array[:-i] = addOne(array[:-i], limit[:-i])[1].copy()
            check = False
    return check_overflow, array

def LinearSearch(tasks, qTables):
    MAX = 99999
    tser_min = MAX
    temp_action = [0]*len(tasks)
    action = [0]*len(tasks)
    best_action = [0]*len(tasks)
    limitComputer = [len(t.getDesComputers()) for t in tasks]
    j=0
    check = False
    while(check == False):
        for i in range(len(tasks)):
            action[i] = tasks[i].getDesComputers()[temp_action[i]].getId()
        tser = getTProcMax(action, qTables)
        if tser < tser_min:
            tser_min = tser
            best_action = action.copy()
        check, temp_action = addOne(temp_action, limitComputer)

    return best_action, tser_min
            
def OptimizationRL(tasks, qTables, limit_tser,alpha, episode, epsilon):
    G = 0 #Q_value reward

    tSer_min = limit_tser
    best_tSer = 0
    values = {}
    optimal_run = [0]*len(tasks)
    first_meet_episode = 0
    Q_table_combination = []


    for e in range(episode):
        episode_run = []
        
        epsilon = epsilon
        if e == 0:
            for t in tasks:
                # episode_run.append([c.getId() for c in t.getDesComputers()][random.randint(0, len(t.getDesComputers())-1)])
                episode_run.append([c.getId() for c in t.getDesComputers()][0])
        
        else:
            for t in tasks:
                selection = random.randint(1,10)
                if selection <= (epsilon)*10:
                    episode_run.append(random.choice([c.getId() for c in t.getDesComputers()]))
                    
                else:
                    values = filter(lambda x: x.getTask() == t, qTables)
                    values = list(values)
                    q_max = max(values, key=lambda v: v.getValue())
                    episode_run.append(q_max.getComputer().getId())

        tser = getTProcMax(episode_run, qTables)

        if tser < limit_tser:
            if tser < tSer_min:
                first_meet_episode = e + 1
                optimal_run = episode_run.copy()
                tSer_min = tser
                best_tSer = tSer_min
            # G = (limit_tser - tser)
            G = 1
        elif tser > limit_tser:
            G = -1
            # G = (limit_tser - tser) / tser
        else:
            G = 0

        if G != 0:
            for i in range(len(tasks)):
                label = f"{tasks[i].getId()}{episode_run[i]}"
                q = next(filter(lambda x: x.getLabel() == label, qTables))
                q.setValue(q.getValue() + alpha * ((G - q.getValue())))

        Q_table_combination.append([q.getValue() for q in qTables])
        # print(episode_run, end="\t")
        # print(getTProcMax(episode_run, qTables), end="\t")
        # print([q.getValue() for q in qTables])
        
    
    return first_meet_episode, best_tSer, optimal_run, Q_table_combination