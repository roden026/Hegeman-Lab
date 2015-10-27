# takes in list of values for C, H, O, and N and then computes the needed ratios
def processElementalData(elementalList):
    # 0 = H:C, 1 = O:C, 2 = Present/Not (True, False) 3 = N:C
    ratiosList = [[],[],[],[]]
    
    #Computes all the ratios and adds them to the ratiosList
    for line in elementalList:
        if len(line) == 4:

            HtoC = line[1]/line[0]
            ratiosList[0].append(HtoC)
            OtoC = line[2]/line[0]
            ratiosList[1].append(OtoC)
            if line[3] == 0:
                ratiosList[2].append(False)
            else:
                ratiosList[2].append(True)
            NtoC = line[3]/line[0]
            ratiosList[3].append(NtoC)
    return ratiosList
