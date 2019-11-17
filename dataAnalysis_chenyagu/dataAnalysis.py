def calculateFirstIntentStep(goalList):
    goalList = eval(goalList)
    intent1 = goalList.index(1) + 1 if 1 in goalList else 99
    intent2 = goalList.index(2) + 1 if 2 in goalList else 99
    if intent1 < intent2:
        firstIntentStep = intent1
    elif intent2 < intent1:
        firstIntentStep = intent2
    else:
        firstIntentStep = 0
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
    if finalStep[0] == eval(bean1GridX) and finalStep[1] == eval(bean1GridY):
        finalGoal = 1
    else:
        finalGoal = 2
    return finalGoal


def calculateIntentGoalAccord(finalGoal, goalList):
    firstIntentStep = calculateFirstIntentStep(goalList)
    if firstIntentStep != 0:
        firstIntent = eval(goalList)[firstIntentStep - 1]
        if firstIntent == finalGoal:
            isIntentGoalAccord = 1
        else:
            isIntentGoalAccord = 0
    else:
        isIntentGoalAccord = 1
    return isIntentGoalAccord


def calculateMaxReactionTimeStep(timeList):
    timeGap = [timeList[i + 1] - timeList[i] for i in range(len(timeList) - 1)]
    maxReactionTimeStep = [i + 2 for i, x in enumerate(timeGap) if x == max(timeGap)]
    return maxReactionTimeStep
