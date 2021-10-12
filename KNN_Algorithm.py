# 1. COLLECTING DATA
import csv
with open('irisdataset.csv', 'r') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        print(", ".join(row))


import random
def loaddataset(filename, split, trainingset=[], testset=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingset.append(dataset[x])
            else:
                testset.append(dataset[x])



trainingset=[]
testset=[]
loaddataset(r'irisdataset.csv', 0.66, trainingset, testset)
print('Train ' + repr(len(trainingset)))
print('Test ' + repr(len(testset)))






# 2. SIMILARITY....

# MEasuring K DIstance between the nearest neighbours...
import math
def euclideanDistance(instance1, instance2,lenght):
    distance = 0
    for x in range(lenght):
        distance += pow((instance1[x] - instance2[x]), 2)

    return math.sqrt(distance)


data = [2,2,2,'a']
data1 = [4,4,4,'b']
distance = euclideanDistance(data,data1, 3)
print('Distance: ' + repr(distance))



# FUnction which returns the nearest neighbour...
import operator
def getNeighbours(trainingset, testInstance, k):
    distance = []
    lenght = len(testInstance)-1
    for x in range(len(trainingset)):
        dist = euclideanDistance(testInstance, trainingset[x], lenght)
        distance.append((trainingset[x], dist))
    distance.sort(key=operator.itemgetter(1))
    neighbours = []
    for x in range(k):
        neighbours.append(distance[x][0])
        return neighbours



trainset = [[2,2,2,'a'], [4,4,4,'b']]
testInstance = [5,5,5]
k = 1
neighbours = getNeighbours(trainset, testInstance, 1)
print(neighbours)



import operator 
def getRespons(neighbours):
    classVotes = {}
    for x in range(len(neighbours)):
        response = neighbours[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1    
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


neighbours = [[1,1,1,'a'],[2,2,2,'a'],[3,3,3,'b']]
response = getRespons(neighbours)
print(response)


def getAccuracy(testset, predictions):
    correct = 0
    for x in range(len(testset)):
        if testset[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testset)))*100.0
       



testset = [[1,1,1,'a'],[2,2,2,'a'],[3,3,3,'b']]
predictions = ['a', 'a', 'a']
accuracy = getAccuracy(testset, predictions)
print(accuracy)




def main():
    trainingset = []
    testset = []
    split = 0.67
    loaddataset('irisdataset.csv', split, trainingset, testset)
    print ('Train set: ' + repr(len(trainingset)))
    print ('Test set: ' + repr(len(testset)))
    predictions = []
    k = 3
    for x in range(len(testset)):
        neighbours = getNeighbours(trainingset, testset[x], k)
        result = getRespons(neighbours)
        predictions.append(result)
        print('> Predicted' + repr(result) + ', actual=' + repr(testset[x][-1]))
    accuracy = getAccuracy(testset, predictions)
    print('Accuracy:' + repr(accuracy) + '%')    

main()