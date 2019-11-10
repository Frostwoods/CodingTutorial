import os
import pandas as pd
import numpy as np
import math


def calculateGoalCommit(goalList):
    goal1Step = [goalList.index(goalList[i]) + 1 for i in range(len(goalList)) if goalList[i] == 1]
    goal2Step = [goalList.index(goalList[i]) + 1 for i in range(len(goalList)) if goalList[i] == 2]
    numGoal1 = len(goal1Step)
    numGoal2 = len(goal2Step)
    if (numGoal1 != 0 and numGoal2 == 0) or (numGoal2 != 0 and numGoal1 == 0):
        isGoalCommit = 'Yes'
    elif numGoal1 != 0 and numGoal2 != 0:
        isGoalCommit = 'No'
    else:
        isGoalCommit = 'Did not make a commitment'
    return isGoalCommit


def calculateFirstIntentStep(goalList):
    firstIntent = 0
    if 1 in goalList:
        firstIntent = goalList.index(1) + 1
    if 2 in goalList:
        firstIntent = goalList.index(2) + 1
    firstIntentStepRatio = firstIntent / len(goalList)
    return firstIntentStepRatio


def calculateMaxReactionTimeStep(timeList):
    timeGap = [timeList[i + 1] - timeList[i] for i in range(len(timeList) - 1)]
    maxReactionTimeStep = [i + 2 for i, x in enumerate(timeGap) if x == max(timeGap)]
    return maxReactionTimeStep
