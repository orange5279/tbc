import os
import csv

# Parameter Define
#####################################################
# data_dir: Where the subscriber csv file store
# subsFileList: a List(), where all csv filename
# outputFilePath: the result output path
# outputFileName: the result output filename
#####################################################
# change data_dir where subscriber csv file store
# filename format must be <SO>.csv, for large SO, the file name should be <SO>.<ID>.csv
#
# for example: NTY.1.csv, NTY.2.csv
# the market (system SO) in all file is NTY
data_dir = 'D:\\'
subsFileList = [file for file in os.listdir(data_dir) if '.csv' in file]

# check does output file exist, if not create it
outputFilePath  = 'D:\\'
outputFileName  = 'cmts_node.txt'
outputFile      = outputFilePath + outputFileName

if os.path.exists(outputFile):
    os.remove(outputFile)
else:
    f = open(outputFile, 'w')
    f.close()

# subIdCount represent as JSON RPC ID
subIdCount = 1

# read each file and parser to JSON RPC format
for subFile in subsFileList:
    with open(data_dir+subFile, newline='') as sourceFile:
        dataReader = csv.reader(sourceFile, delimiter=',', quotechar='|')
        system = subFile.split('.')[0]
        for row in dataReader:
            index = subIdCount
            subscriberId = str(row[0]).upper()
            cmts_node = row[1]

            result = ('{' + '"id":{},"method":"object.set","params":'.format(index) +
                      '{"type":"subscriber","assignedId":' +
                      '"{}",'.format(subscriberId) + '"attributes":{' +
                      '"cmts_node":"{}"'.format(cmts_node) +
                      '}}}'
                      )
            subIdCount += 1

            with open(outputFile, 'a') as out:
                out.write(result + '\n')