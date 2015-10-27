# Writes needed information to a .txt file
# with either -neg or -pos depending on type of scan.
def writeTxt(inputList, filename_mzXML, polarity):
    filename = filename_mzXML[:len(filename_mzXML)-6]
    if polarity == 1:
        newFile = open(filename + "-neg.txt", "w")
        for i in inputList:
            newFile.write(str(i) + "\n")
    if polarity == 0:
        newFile = open(filename + "-pos.txt", "w")
        for i in inputList:
            newFile.write(str(i) + "\n")
