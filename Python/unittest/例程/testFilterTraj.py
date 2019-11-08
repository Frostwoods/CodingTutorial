import os
import sys
DIRNAME = os.path.dirname(__file__)
sys.path.append(os.path.join(DIRNAME))

import unittest
from ddt import ddt, data, unpack
import numpy as np
from filterTraj import *
# import filterTraj as targetCode

@ddt
class TestFilterFunctions(unittest.TestCase):
  def setUp(self):
    self.sheepId=0
    self.wolfId=1
    self.masterId=2
    self.distractorId=3
    self.stateIndex=0
    self.positionIndex=[0,1]
    self.timeWindow=6
    self.maxCircleNumber=3

  @data(((0,1),(1,0),np.pi/2),\
        ((0,1),(0,2),0),\
        ((0,1),(0,-1),np.pi))
  @unpack
  def testCalculateIncludedAngle(self,v1,v2,groundTruthAngle):
    #pass
    angle=calculateIncludedAngle(v1,v2)
    truthValue = np.array_equal(angle,groundTruthAngle)    
    self.assertTrue(truthValue) 

  @data(((0,1),(2,1),False),\
        ((0.5,1),(0.6,-2),True),\
        ((0.5,0),(0.6,0),True),\
        ((1.5,0),(1.6,0),False))
  @unpack
  def testIsCrossAxis(self,pos1,pos2,groundTruthIsCross):
     #bug in parallel situation
     isCross=isCrossAxis(pos1,pos2)
     truthValue = np.array_equal(isCross,groundTruthIsCross)
     self.assertTrue(truthValue)

  @data(([[[[4, 7], [4, 6],[3, 6]]],\
        [[[4, 8], [4, 7],[4, 8]]],\
        [[[4, 9], [4, 8],[3, 8]]],\
        [[[4, 10], [4, 9],[3, 9]]],\
        [[[4, 11], [4, 10],[3, 10]]]],0),\

        ([[[[3, 6], [4, 6],[3, 6]]],\
        [[[3, 7], [4, 7],[3, 7]]],\
        [[[3, 8], [4, 8],[3, 8]]],\
        [[[3, 9], [4, 9],[3, 9]]],\
        [[[3, 10], [4, 10],[3, 10]]]],np.pi/2),\
    )
  @unpack 	 
  def testCalculateChasingDeviation(self,traj,groundTruthMeanDeviation):
    calculateChasingDeviation=CalculateChasingDeviation(self.sheepId, self.wolfId, self.stateIndex, self.positionIndex)
    meanChasingDeviation=calculateChasingDeviation(traj)
    truthValue = np.array_equal(meanChasingDeviation,groundTruthMeanDeviation)
    self.assertTrue(truthValue)

  @data(([[[[4, 7], [4, 6],[3, 6],[0, 0]]],\
        [[[4, 8], [4, 7],[4, 8],[3, 4]]],\
        [[[4, 9], [4, 8],[3, 8],[3, 5]]],\
        [[[4, 10], [4, 9],[3, 9],[3, 6]]],\
        [[[4, 11], [4, 10],[3, 10],[4, 6]]]],2),\

        ([[[[3, 6], [4, 6],[3, 6],[3, 6]]],\
        [[[3, 7], [4, 7],[3, 7],[3, 6]]],\
        [[[3, 8], [4, 8],[3, 8],[3, 6]]],\
        [[[3, 9], [4, 9],[3, 9],[3, 6]]],\
        [[[3, 10], [4, 10],[3, 10],[3, 6]]]],0),\
    )
  @unpack
  def testCalculateDistractorMoveDistance(self,traj,groundTruthMeanDistance):
    calculateDistractorMoveDistance=CalculateDistractorMoveDistance(self.distractorId, self.stateIndex, self.positionIndex)
    distractorSpeed=calculateDistractorMoveDistance(traj)
    truthValue = np.array_equal(distractorSpeed,groundTruthMeanDistance)
    self.assertTrue(truthValue)


 	# def IsAllInAngelRange(self):


  @data((0,np.pi,1),\
        (np.pi/2,np.pi/2,0),\
        (np.pi/4,np.pi*3/4,True))
  @unpack
  def UntestCountCirclesBetweenWolfAndMaster(self,lowBound,upBound,groundTruthCircleRatio):
    # RatioError because of different units
    traj =[[[[0, 0], [4, 6],[3, 6]]],\
        [[[0, 0], [4, 7],[4, 8]]],\
        [[[0, 0], [4, 8],[3, 8]]],\
        [[[0, 0], [4, 9],[3, 9]]],\
        [[[0, 0], [4, 7],[4, 8]]],\
        [[[0, 0], [4, 8],[3, 8]]],\
        [[[0, 0], [4, 9],[3, 9]]],\
        [[[0, 0], [4, 7],[4, 8]]],\
        [[[0, 0], [4, 8],[3, 8]]],\
        [[[0, 0], [4, 9],[3, 9]]],\
        [[[0, 0], [4, 10],[3, 10]]]]
    timeWindow=1
    findCirleMove=IsAllInAngelRange(lowBound,upBound)
    velocityIndex=0
    countCirclesBetweenWolfAndMaster=CountCirclesBetweenWolfAndMaster(self.wolfId, self.masterId,self.stateIndex, self.positionIndex,velocityIndex,self.timeWindow,findCirleMove)
    circleRatio=countCirclesBetweenWolfAndMaster(traj)
    print(circleRatio,'crossRatio')
    truthValue = np.array_equal(circleRatio,groundTruthCircleRatio)
    self.assertTrue(truthValue)

  @data(([[[[0, 0], [4, 6],[3, 6]]],\
        [[[0, 0], [4, 7],[4, 8]]],\
        [[[0, 0], [4, 8],[3, 8]]],\
        [[[0, 0], [4, 8],[3, 8]]],\
        [[[0, 0], [4, 9],[3, 9]]],\
        [[[0, 0], [4, 10],[3, 10]]]],0),\

        ([[[[0, 0], [4, 6],[3, 6]]],\
        [[[3, 6], [4, 7],[3, 7]]],\
        [[[4, 9], [4, 8],[3, 8]]],\
        [[[0, 0], [4, 9],[3, 9]]],\
        [[[0, 0], [4, 10],[3, 10]]]],2/5),\

    )
  @unpack
  def testCountSheepCrossRope(self,traj,groundTruthCrossRatio):
    #pass
    countSheepCrossRope=CountSheepCrossRope(self.sheepId, self.wolfId, self.masterId,self.stateIndex, self.positionIndex,tranformCoordinates,isCrossAxis)
    crossRatio=countSheepCrossRope(np.array(traj))    
    truthValue = np.array_equal(crossRatio,groundTruthCrossRatio)
    self.assertTrue(truthValue)

  @data((10,1),\
        (0,0),\
        (5,3/11))
  @unpack  
  def testCountSheepInCorner(self,cornerSize,groundTruthCornerRatio):
    #unpasstest  ratio bug
    traj =[[[[1, 1], [4, 6],[3, 6]]],\
        [[[4, 4], [4, 7],[4, 8]]],\
        [[[-4, -4], [4, 8],[3, 8]]],\
        [[[6, -6], [4, 9],[3, 9]]],\
        [[[-6, 6], [4, 7],[4, 8]]],\
        [[[8, 8], [4, 8],[3, 8]]],\
        [[[9, 5], [4, 9],[3, 9]]],\
        [[[1, 9], [4, 7],[4, 8]]],\
        [[[1, 10], [4, 8],[3, 8]]],\
        [[[8, 1], [4, 9],[3, 9]]],\
        [[[1, 5], [4, 10],[3, 10]]]]
    spaceSize=10
    countWolfInCorner=CountSheepInCorner(self.sheepId,self.stateIndex, self.positionIndex,spaceSize,cornerSize,isInCorner)
    wolfCornerRatio=countWolfInCorner(np.array(traj))
    truthValue = np.array_equal(wolfCornerRatio,groundTruthCornerRatio)
    self.assertTrue(truthValue)

  @data((100,1),\
        (0,0),\
        (2,2/11))
  @unpack 
  def testCountCollision(self,collisionRadius,groundTruthCollisionRatio):
    traj =[[[[0, 0], [4, 6],[3, 6]]],\
        [[[0, 0], [4, 7],[4, 8]]],\
        [[[0, 0], [4, 8],[3, 8]]],\
        [[[0, 0], [4, 9],[3, 9]]],\
        [[[0, 0], [4, 7],[4, 8]]],\
        [[[5, 9], [4, 8],[3, 8]]],\
        [[[4, 8], [4, 9],[3, 9]]],\
        [[[0, 0], [4, 7],[4, 8]]],\
        [[[0, 0], [4, 8],[3, 8]]],\
        [[[0, 0], [4, 9],[3, 9]]],\
        [[[0, 0], [4, 10],[3, 10]]]]
    countCollision=CountCollision(self.sheepId,self.wolfId,self.stateIndex, self.positionIndex,collisionRadius,isCollision)
    collisionRatio=countCollision(np.array(traj))
    truthValue = np.array_equal(collisionRatio,groundTruthCollisionRatio)
    self.assertTrue(truthValue)
if __name__ == '__main__':
    unittest.main()
