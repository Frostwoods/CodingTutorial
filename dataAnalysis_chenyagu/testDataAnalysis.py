import os
import sys
import numpy as np
import unittest
from ddt import ddt, data, unpack
from dataAnalysis import *

DIRNAME = os.path.dirname(__file__)
sys.path.append(os.path.join(DIRNAME))


@ddt
class TestAnalysisFunctions(unittest.TestCase):
    def setUp(self):
        self.testParameter = 0

    @data(((0, 0, 0, 0, 0, 0), 'Did not make a commitment'), \
          ((0, 0, 1, 1, 0, 1, 2, 1), 'No'), \
          ((0, 0, 0, 0, 0, 0, 0, 0, 0, 2), 'Yes'))
    @unpack
    def testCalculateGoalCommit(self, goalList, groundTruthAnswer):
        # pass
        isGoalCommit = calculateGoalCommit(goalList)
        truthValue = np.array_equal(isGoalCommit, groundTruthAnswer)
        self.assertTrue(truthValue)

    @data(((0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0.0), \
          ((2, 0, 1, 1, 0, 1, 1, 1, 1, 1), 0.1), \
          ((0, 0, 0, 0, 0, 0, 0, 0, 0, 2), 1.0))
    @unpack
    def testCalculateFirstIntentStep(self, goalList, groundTruthRatio):
        # pass
        firstIntentStepRatio = calculateFirstIntentStep(goalList)
        truthValue = np.array_equal(firstIntentStepRatio, groundTruthRatio)
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
