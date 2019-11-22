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
    humanResultsPath = DIRNAME + '/human'
    maxResultsPath = DIRNAME + '/max'
    softmaxResultsPath = DIRNAME + '/softmax'
    humanResultsDF = pd.concat(map(pd.read_csv, glob.glob(os.path.join(humanResultsPath, '*.csv'))), sort=False)
    maxResultsDF = pd.concat(map(pd.read_csv, glob.glob(os.path.join(maxResultsPath, '*.csv'))), sort=False)
    softmaxResultsDF = pd.concat(map(pd.read_csv, glob.glob(os.path.join(softmaxResultsPath, '*.csv'))), sort=False)
    subNum = len(humanResultsDF['name'].unique())
    humanNoiseTrail = humanResultsDF[humanResultsDF['noisePoint'] != '[]']
    maxNoiseTrail = maxResultsDF[maxResultsDF['noisePoint'] != '[]']
    softmaxNoiseTrail = softmaxResultsDF[softmaxResultsDF['noisePoint'] != '[]']
    humanNoiseTrail['isTimeMaxWhenNoisy'] = humanNoiseTrail.apply(
        lambda x: calculateIsTimeMaxNextNoise(x['reactionTime'], x['noisePoint']), axis=1)
    maxNoiseTrail['isTimeMaxWhenNoisy'] = maxNoiseTrail.apply(
        lambda x: calculateIsTimeMaxNextNoise(x['reactionTime'], x['noisePoint']), axis=1)
    softmaxNoiseTrail['isTimeMaxWhenNoisy'] = softmaxNoiseTrail.apply(
        lambda x: calculateIsTimeMaxNextNoise(x['reactionTime'], x['noisePoint']), axis=1)
    humanNormalTrail = humanNoiseTrail[humanNoiseTrail['noiseNumber'] != 'special']
    humanSpecialTrail = humanNoiseTrail[humanNoiseTrail['noiseNumber'] == 'special']
    maxNormalTrail = maxNoiseTrail[maxNoiseTrail['noiseNumber'] != 'special']
    maxSpecialTrail = maxNoiseTrail[maxNoiseTrail['noiseNumber'] == 'special']
    softmaxNormalTrail = softmaxNoiseTrail[softmaxNoiseTrail['noiseNumber'] != 'special']
    softmaxSpecialTrail = softmaxNoiseTrail[softmaxNoiseTrail['noiseNumber'] == 'special']
    humanMeanDF = pd.DataFrame()
    maxMeanDF = pd.DataFrame()
    softmaxMeanDF = pd.DataFrame()
    humanMeanDF['isTimeMaxWhenNoisyNormal'] = humanNormalTrail.groupby("name")['isTimeMaxWhenNoisy'].mean()
    humanMeanDF['isTimeMaxWhenNoisySpecail'] = humanSpecialTrail.groupby("name")['isTimeMaxWhenNoisy'].mean()
    maxMeanDF['isTimeMaxWhenNoisyNormal'] = maxNormalTrail.groupby("name")['isTimeMaxWhenNoisy'].mean()
    maxMeanDF['isTimeMaxWhenNoisySpecail'] = maxSpecialTrail.groupby("name")['isTimeMaxWhenNoisy'].mean()
    softmaxMeanDF['isTimeMaxWhenNoisyNormal'] = softmaxNormalTrail.groupby("name")['isTimeMaxWhenNoisy'].mean()
    softmaxMeanDF['isTimeMaxWhenNoisySpecail'] = softmaxSpecialTrail.groupby("name")['isTimeMaxWhenNoisy'].mean()
    humanIsTimeMaxWhenNoisyMeanNormal = np.mean(humanMeanDF['isTimeMaxWhenNoisyNormal'])
    humanIsTimeMaxWhenNoisyMeanSpecail = np.mean(humanMeanDF['isTimeMaxWhenNoisySpecail'])
    maxIsTimeMaxWhenNoisyMeanNormal = np.mean(maxMeanDF['isTimeMaxWhenNoisyNormal'])
    maxIsTimeMaxWhenNoisyMeanSpecail = np.mean(maxMeanDF['isTimeMaxWhenNoisySpecail'])
    softmaxIsTimeMaxWhenNoisyMeanNormal = np.mean(softmaxMeanDF['isTimeMaxWhenNoisyNormal'])
    softmaxIsTimeMaxWhenNoisyMeanSpecail = np.mean(softmaxMeanDF['isTimeMaxWhenNoisySpecail'])
    # humanMeanDF.to_csv("humanMeanDF.csv")
    print('If time is maximal next to noisy point')
    print(
    'Normal trial:', 'human:', humanIsTimeMaxWhenNoisyMeanNormal, 'max:', maxIsTimeMaxWhenNoisyMeanNormal, 'softmax:',
    softmaxIsTimeMaxWhenNoisyMeanNormal)
    print('Specail trial:', 'human:', humanIsTimeMaxWhenNoisyMeanSpecail, 'max:', maxIsTimeMaxWhenNoisyMeanSpecail,
          'softmax:',
          softmaxIsTimeMaxWhenNoisyMeanSpecail)

    plt.title('If time is maximal next to noisy point')
    x = np.arange(3)
    y1 = [humanIsTimeMaxWhenNoisyMeanNormal, maxIsTimeMaxWhenNoisyMeanNormal, softmaxIsTimeMaxWhenNoisyMeanNormal]
    y2 = [humanIsTimeMaxWhenNoisyMeanSpecail, maxIsTimeMaxWhenNoisyMeanSpecail, softmaxIsTimeMaxWhenNoisyMeanSpecail]
    width = 0.2
    std_err1 = [np.std(humanMeanDF['isTimeMaxWhenNoisyNormal'], ddof=1) / math.sqrt(subNum - 1),
                np.std(maxMeanDF['isTimeMaxWhenNoisyNormal'], ddof=1) / math.sqrt(subNum - 1),
                np.std(softmaxMeanDF['isTimeMaxWhenNoisyNormal'], ddof=1) / math.sqrt(subNum - 1)]
    std_err2 = [np.std(humanMeanDF['isTimeMaxWhenNoisySpecail'], ddof=1) / math.sqrt(subNum - 1),
                np.std(maxMeanDF['isTimeMaxWhenNoisySpecail'], ddof=1) / math.sqrt(subNum - 1),
                np.std(softmaxMeanDF['isTimeMaxWhenNoisySpecail'], ddof=1) / math.sqrt(subNum - 1)]
    error_attri = {'elinewidth': 1, 'ecolor': 'black', 'capsize': 3}
    plt.bar(x, y1, width, align='center', yerr=std_err1, error_kw=error_attri, label='normal trial', alpha=1)
    for a, b in zip(x, y1):
        plt.text(a, b + 0.01, '%.3f' % b, ha='center', va='bottom')
    plt.bar(x + width, y2, width, align='center', yerr=std_err2, error_kw=error_attri, label='special trial', alpha=1)
    for a, b in zip(x, y2):
        plt.text(a + width, b + 0.01, '%.3f' % b, ha='center', va='bottom')
    names = ['huamn', 'max', 'softmax']
    plt.xticks(x + width / 2, names)
    plt.ylabel('Probability')
    plt.ylim((0, 1))
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
