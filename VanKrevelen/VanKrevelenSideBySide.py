'''
Takes a csv as an input and works through the compounds to extract the number of C, H, O, and N
present. It also notes if N is present and marks those points, then calculates the ratios of
H:C, O:C, and N:C and plots them and generates side by side 3D plots to create a stereoscopic
effect.
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
from mpl_toolkits.mplot3d import Axes3D

usage_mesg = 'VanKrevelenSideBySide.py <csv file(s)>'


# Checks if files are available.
filename_csv = sys.argv[1]
if not os.access(filename_csv, os.R_OK):
    print "%s is not accessible." % filename_csv
    print usage_mesg
    sys.exit(1)

if (len(sys.argv) == 2):
    filename_csv = sys.argv[1]
    elementalList = extractNeededElementalData(filename_csv)
    ratiosList = processElementalData(elementalList)
    # Note, at this point the elementalList and ratiosList will not be aligned
    # because the processing of the ratios removes lines where not all 3 elements
    # were present (rare occurance but may happen)

# Graphs the data provided and labels axes

area = 10.0

fig = plt.figure(figsize=(17, 7))
fig.suptitle('Van Krevelen Diagram - Side By Side', fontsize=14, fontweight='bold')
ax = fig.add_subplot(121, projection='3d')

ax.set_xlabel('O:C Ratio')
ax.set_ylabel('H:C Ratio')
ax.set_zlabel('N:C Ratio')

# Creates a list for plotting purposes where two elements are lists of compounds with N and without respectively
listByN = [[], []]
withN = None
withoutN = None
for i in range(len(ratiosList[2])):
    if ratiosList[2][i]:
        listByN[0].append([ratiosList[1][i], ratiosList[0][i], ratiosList[3][i], 'r', '^'])
    else:
        listByN[1].append([ratiosList[1][i], ratiosList[0][i], ratiosList[3][i], 'b', 'o'])

counter = 0
for i in listByN:
    for j in i:
        if counter == 0:
            withN = ax.scatter(xs=j[0], ys=j[1], zs=j[2], s=15.0, c=j[3], marker=j[4], alpha=.25)
        else:
            withoutN = ax.scatter(xs=j[0], ys=j[1], zs=j[2], s=15.0, c=j[3], marker=j[4], alpha=.25)
    counter += 1

plt.legend((withN, withoutN), ('Does have N', 'Does not have N'), scatterpoints=1, loc='lower left', ncol=1, fontsize=9)

'''
Second plot.
'''
ax2 = fig.add_subplot(122, projection='3d')

ax2.set_xlabel('O:C Ratio')
ax2.set_ylabel('H:C Ratio')
ax2.set_zlabel('N:C Ratio')

counter = 0
for i in listByN:
    for j in i:
        if counter == 0:
            withN = ax2.scatter(xs=j[0], ys=j[1], zs=j[2], s=15.0, c=j[3], marker=j[4], alpha=.25)
        else:
            withoutN = ax2.scatter(xs=j[0], ys=j[1], zs=j[2], s=15.0, c=j[3], marker=j[4], alpha=.25)
    counter += 1

ax2.azim -= 6

plt.legend((withN, withoutN), ('Does have N', 'Does not have N'), scatterpoints=1, loc='lower left', ncol=1, fontsize=9)
# END SECOND PLOT CODE


plt.show()

print("done")
