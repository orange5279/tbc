import os
import csv

# Parameter Define
#####################################################
# data_dir: Where the subscriber csv file store
# subsFileList: a List(), where all csv filename
# outputFile: the result output filename
####################################################
# Notice:
# 1. filename must be '<SO>.csv', for large SO, the file name should be <SO>.<ID>.csv
#    for example: NTY.1.csv & NTY.2.csv, thus both of row data in the file will add to NTY as market attribute
#
# 2. suggest remove csv header, or may error in API or garbage data
#
#

data_dir = '/Users/bearwei/Desktop/psm0731/'
# subsFileList = [file for file in os.listdir(data_dir) if '.csv' in file]
subsFileList = ['NTY_GPON_MAP.csv']

# check does output file exist, if yes delete it else create it
outputFile = '/Users/bearwei/Desktop/psm0731/pon.txt'
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
            subscriberId = str(row[0]).encode('utf-8').hex().upper()
            gateway = row[1]
            interface = row[2]

            result = ('{' + '"id":{},"method":"object.set","params":'.format(index) +
                      '{"type":"subscriber","assignedId":' +
                      '"{}",'.format(subscriberId) + '"attributes":{' +
                      '"ipdr_CmtsName":"{}",'.format(gateway) +
                      '"ipdr_MdName":"{}"'.format(interface) +
                      '}}}'
                      )
            subIdCount += 1

            with open(outputFile, 'a') as out:
                out.write(result + '\n')

