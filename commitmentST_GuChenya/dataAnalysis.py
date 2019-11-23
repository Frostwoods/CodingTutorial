def calculateFirstIntentStep(goalList):
    goalList = eval(goalList)
    intent1 = goalList.index(1) + 1 if 1 in goalList else 99
    intent2 = goalList.index(2) + 1 if 2 in goalList else 99
    if intent1 < intent2:
        firstIntentStep = intent1
    elif intent2 < intent1:
        firstIntentStep = intent2
    else:
        firstIntentStep = len(goalList)
    return firstIntentStep


def calculateFirstIntentStepRatio(goalList):
    firstIntentStepRatio = calculateFirstIntentStep(goalList) / len(eval(goalList))
    return firstIntentStepRatio


def calculateGoalCommit(goalList):
    goalList = eval(goalList)
    goal1Step = [goalList.index(goalList[i]) + 1 for i in range(len(goalList)) if goalList[i] == 1]
    goal2Step = [goalList.index(goalList[i]) + 1 for i in range(len(goalList)) if goalList[i] == 2]
    numGoal1 = len(goal1Step)
    numGoal2 = len(goal2Step)
    if (numGoal1 != 0 and numGoal2 == 0) or (numGoal2 != 0 and numGoal1 == 0):
        isGoalCommit = 1
    elif numGoal1 != 0 and numGoal2 != 0:
        isGoalCommit = 0
    else:
        isGoalCommit = 1
    return isGoalCommit


def calculateFinalGoal(bean1GridX, bean1GridY, trajectory):
    trajectory = eval(trajectory)
    finalStep = trajectory[len(trajectory) - 1]
    if finalStep[0] == bean1GridX and finalStep[1] == bean1GridY:
        finalGoal = 1
    else:
        finalGoal = 2
    return finalGoal


def calculateFirstIntentGoalAccord(finalGoal, goalList):
    firstIntentStep = calculateFirstIntentStep(goalList)
    if firstIntentStep != len(eval(goalList)):
        firstIntent = eval(goalList)[firstIntentStep - 1]
        if firstIntent == finalGoal:
            isFirstIntentGoalAccord = 1
        else:
            isFirstIntentGoalAccord = 0
    else:
        isFirstIntentGoalAccord = 1
    return isFirstIntentGoalAccord


def calculateIsTimeMaxNextNoisePoint(timeList, noisePoint):
    timeList = eval(timeList)
    noisePoint = eval(noisePoint)
    noisePointNextStep = [i + 1 for i in noisePoint]
    timeGap = [timeList[i + 1] - timeList[i] for i in range(len(timeList) - 1)]
    maxReactTimeStep = [i + 2 for i, x in enumerate(timeGap) if x == max(timeGap)]
    if [i for i in maxReactTimeStep if i in noisePointNextStep] != []:
        isTimeMaxNextNoisePoint = 1
    else:
        isTimeMaxNextNoisePoint = 0
    return isTimeMaxNextNoisePoint
