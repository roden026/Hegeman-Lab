'''
Runs a batch of .csv files to generate multiple heatmaps. This code is less commented but
opperates mostly the same as the VanKrevelenHeatmap.py script so consult that if more
help is needed.
'''
import sys
import os
from extractNeededElementalData import extractNeededElementalData
from processElementalData import processElementalData
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import six
import dateutil
import itertools
import heatmap



def compareXY(XY1, XY2):
    '''
    Little function to make the testing to see if the points are close a bit easier.
    '''

    # These define what is close enough to count
    X_ADJUST = .20
    Y_ADJUST = .15

    okay = False

    if XY1[0] < XY2[0] + X_ADJUST and XY1[0] > XY2[0] - X_ADJUST:
        if XY1[1] < XY2[1] + Y_ADJUST and XY1[1] > XY2[1] - Y_ADJUST:
            okay = True
 
    return okay

'''
Files to test in a list

Example:
mappingFiles = [
"CoreAminoAcids.csv",
"FattyAcyls.csv",
"Flavonoids.csv",
"Glycerolipids.csv",
"Glycerophospholipids.csv",
"monosac.csv",
"Polyketides.csv",
"PrenolLipids.csv",
"Saccharolipids.csv",
"Sphingolipids.csv",
"SterolLipids.csv",
"Terpenoids.csv",
"AllLipids.csv"
]
'''
mappingFiles = ["example-pos.csv"]


for files in mappingFiles:
    filename_csv = files
    elementalList = extractNeededElementalData(filename_csv)
    ratiosList = processElementalData(elementalList)
    #Note, at this point the elementalList and ratiosList will not be aligned
    #because the processing of the ratios removes lines where not all 3 elements
    #were present (rare occurance but may happen)

    PERCENT_NEAR = .15

    y = 0
    tList = []
    for x in ratiosList[1]:
        tHelp = (x, ratiosList[0][y])
        tList.append(tHelp)
        y += 1

    filteredtups = []

    for pair in tList:
        counter = 0
        for compair in tList:
            if compareXY(pair,compair):
                counter += 1
        if counter > (len(tList) * PERCENT_NEAR):
            filteredtups.append(pair)

    hm = heatmap.Heatmap()
    img = hm.heatmap(filteredtups, dotsize = 100, opacity = 250, scheme='classic', area=((0,0),(1.4,2.5)))


    # Graphs the data provided and labels axes

    fig = plt.figure()
    fig.suptitle('Van Krevelen Heatmap', fontsize=14, fontweight='bold')
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)

    ax.set_xlabel('O:C Ratio')
    ax.set_ylabel('H:C Ratio')

    # Creates a list for plotting purposes where two elements are lists of compounds with N and without respectively
    listByN = [[],[]]
    withN = None
    withoutN = None
    for i in range(len(ratiosList[2])):
        if ratiosList[2][i]:
            listByN[0].append([ratiosList[1][i],ratiosList[0][i], 'r', '^'])
        else:
            listByN[1].append([ratiosList[1][i],ratiosList[0][i], 'b', 'o'])

    counter = 0
    for i in listByN:
        for j in i:
            if counter == 0:
               withN = plt.scatter(j[0], j[1], 15.0, j[2], j[3], alpha = .25)
            else:
                withoutN = plt.scatter(j[0], j[1], 15.0, j[2], j[3], alpha = .25)
        counter += 1

    myaximage = ax.imshow(img, aspect='auto' ,extent=(0,1.4,0,2.5), alpha=1, zorder=-1)

    # NOTE: Figures saved, not displayed.
    plt.savefig(files[:len(files) - 4] + ".pdf")

    print "done with " + files
print "Done!"


























