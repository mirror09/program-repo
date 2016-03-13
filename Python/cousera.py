def companyBotStrategy(trainingData):
    a=0.0
    c=0.0
    for i in range(len(trainingData)):
        if(trainingData[i][1]==1):
            a+=trainingData[i][0]
            c+=trainingData[i][1]
    return a/c
    
trainingData= [[3,1], [6,1]]
print(companyBotStrategy(trainingData))
