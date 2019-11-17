import numpy as np
import unittest
from ddt import ddt, data, unpack
from dataAnalysis import *


@ddt
class TestAnalysisFunctions(unittest.TestCase):
    def setUp(self):
        self.testParameter = 0

    @data((('0, 0, 0, 0, 0, 0, 0, 0, 0, 0'), 0.0), \
          (('2, 0, 1, 1, 0, 1, 1, 1, 1, 2'), 0.1), \
          (('0, 0, 0, 0, 0, 0, 0, 0, 0, 2'), 1.0))
    @unpack
    def testCalculateFirstIntentStepRatio(self, goalList, groundTruthRatio):
        # pass
        firstIntentStepRatio = calculateFirstIntentStepRatio(goalList)
        truthValue = np.array_equal(firstIntentStepRatio, groundTruthRatio)
        self.assertTrue(truthValue)

    @data((('0, 0, 0, 0, 0, 0'), 1), \
          (('0, 0, 1, 1, 0, 1, 1, 1'), 1), \
          (('0, 0, 1, 1, 0, 2, 2, 1'), 0), \
          (('0, 1, 1, 0, 0, 2, 2, 0, 2'), 0))
    @unpack
    def testCalculateGoalCommit(self, goalList, groundTruthAnswer):
        # pass
        isGoalCommit = calculateGoalCommit(goalList)
        truthValue = np.array_equal(isGoalCommit, groundTruthAnswer)
        self.assertTrue(truthValue)

    @data(('5', ' 4', ('[6, 7], [5, 7], [5, 6], [5, 5], [5, 4]'), 1), \
          ('4', ' 8', ('[8, 6], [8, 7], [8, 8], [9, 8], [10, 8]'), 2))
    @unpack
    def testCalculateFinalGoal(self, bean1GridX, bean1GridY, trajectory, groundTruthAnswer):
        # pass
        finalGoal = calculateFinalGoal(bean1GridX, bean1GridY, trajectory)
        truthValue = np.array_equal(finalGoal, groundTruthAnswer)
        self.assertTrue(truthValue)

    @data((1, ('0, 0, 0, 0, 0, 0, 1, 1, 2'), 1), \
          (1, ('0, 0, 0, 0, 0, 0, 2, 1, 1'), 0), \
          (1, ('0, 0, 0, 0, 0, 0, 0, 0, 0'), 1))
    @unpack
    def testCalculateIntentGoalAccord(self, finalGoal, goalList, groundTruthAnswer):
        # pass
        isIntentGoalAccord = calculateIntentGoalAccord(finalGoal, goalList)
        truthValue = np.array_equal(isIntentGoalAccord, groundTruthAnswer)
        self.assertTrue(truthValue)

    @data(((2544, 2785, 3025, 3219, 3443, 3718, 4062, 4392, 5170, 5474), [9]), \
          ((1000, 2000, 3000, 4000), [2, 3, 4]))
    @unpack
    def testCalculateMaxReactionTimeStep(self, timeList, groundTruthStep):
        # pass
        maxReactionTimeStep = calculateMaxReactionTimeStep(timeList)
        truthValue = np.array_equal(maxReactionTimeStep, groundTruthStep)
        self.assertTrue(truthValue)


if __name__ == '__main__':
    unittest.main()
