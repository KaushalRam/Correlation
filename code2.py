import csv 
import numpy as np 

def getDataSource(data_path):
    size_of_tv=[]
    average_time_spent=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row['Size of TV']))
            average_time_spent.append(float(row['\tAverage time spent ']))
    return{'x':size_of_tv,'y':average_time_spent}

def findCorelation(dataSource):
    correlation=np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation between size of TV and average time spent: \n',correlation[0,1])

def setup():
    data_path ='tv.csv'
    dataSource=getDataSource(data_path)
    findCorelation(dataSource)

setup()

