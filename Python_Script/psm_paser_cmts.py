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
outputFileName  = 'subscriber_cmts.txt'
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
            market = system
            customerId = row[0]
            if 'ALCL' in row[1]:
                subscriberId = str(row[1]).encode('utf-8').hex().upper()
            else:
                subscriberId = str(row[1]).upper()
            speed = row[2]
            node = row[3]
            zipcode = row[4]
            mduid = row[5]
            bypass = row[6]
            spam = row[7]
            redirect = row[8]
            bandott = row[9]
            classcode = row[10]
            classname = row[11]
            mduname = row[12]
            street = row[13]
            facicode = row[14]
            faciname = row[15]
            modelname = row[16]
            cmts_node = row[17]

            result = ('{' + '"id":{},"method":"object.set","params":'.format(index) +
                      '{"type":"subscriber","assignedId":' +
                      '"{}",'.format(subscriberId) + '"attributes":{' +
                      '"market":"{}",'.format(market) +
                      '"customerid":"{}",'.format(customerId) +
                      '"speed":"{}",'.format(speed) +
                      '"node":"{}",'.format(node) +
                      '"zipcode":"{}",'.format(zipcode) +
                      '"mduid":"{}",'.format(mduid) +
                      '"bypass":"{}",'.format(bypass) +
                      '"spam":"{}",'.format(spam) +
                      '"redirect":"{}",'.format(redirect) +
                      '"bandott":"{}",'.format(bandott) +
                      '"classcode":"{}",'.format(classcode) +
                      '"classname":"{}",'.format(classname) +
                      '"mduname":"{}",'.format(mduname) +
                      '"street":"{}",'.format(street) +
                      '"facicode":"{}",'.format(facicode) +
                      '"faciname":"{}",'.format(faciname) +
                      '"modelname":"{}",'.format(modelname) +
                      '"cmts_node":"{}"'.format(cmts_node) +
                      '}}}'
                      )
            subIdCount += 1

            with open(outputFile, 'a') as out:
                out.write(result + '\n')