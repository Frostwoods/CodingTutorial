import os
import glob
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from dataAnalysis import *

DIRNAME = os.path.dirname(__file__)


def main():
    resultsPath = DIRNAME + '/human'
    resultsDF = pd.concat(map(pd.read_csv, glob.glob(os.path.join(resultsPath, '*.csv'))), sort=False)
    # trialNum = resultsDF.shape[0]  # 总试次
    subNum = len(resultsDF['name'].unique())
    # eachSubTrialNum = trialNum / subNum  # 每个被试的trial数
    resultsDF['goalCommitment'] = resultsDF.apply(lambda x: calculateGoalCommit(x['goal']), axis=1)
    normalTrail = resultsDF[resultsDF['noiseNumber'] != 'special']
    specialTrail = resultsDF[resultsDF['noiseNumber'] == 'special']
    meanDF = pd.DataFrame()
    meanDF['goalCommitNormal'] = normalTrail.groupby("name")['goalCommitment'].mean()
    meanDF['goalCommitSpecail'] = specialTrail.groupby("name")['goalCommitment'].mean()
    goalCommitMeanNormal = np.mean(meanDF['goalCommitNormal'])
    goalCommitMeanSpecail = np.mean(meanDF['goalCommitSpecail'])
    # meanDF.to_csv("meandF.csv")
    print('Goal commitment probability')
    print('Normal trial:', goalCommitMeanNormal)
    print('Specail trial:', goalCommitMeanSpecail)

    plt.title('Goal commitment - Human')
    x = np.arange(2)
    y1 = [goalCommitMeanNormal, 1 - goalCommitMeanNormal]
    y2 = [goalCommitMeanSpecail, 1 - goalCommitMeanSpecail]
    width = 0.3
    std_err1 = np.std(meanDF['goalCommitNormal'], ddof=1) / math.sqrt(subNum - 1)
    std_err2 = np.std(meanDF['goalCommitSpecail'], ddof=1) / math.sqrt(subNum - 1)
    error_attri = {'elinewidth': 1, 'ecolor': 'black', 'capsize': 3}
    plt.bar(x, y1, width, align='center', yerr=std_err1, error_kw=error_attri, label='normal trial', alpha=1)
    plt.bar(x + width, y2, width, align='center', yerr=std_err2, error_kw=error_attri, label='special trial', alpha=1)
    names = ['consist', 'inconsist']
    plt.xticks(x + width / 2, names)
    plt.ylabel('Probability')
    plt.ylim((0, 1))
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
