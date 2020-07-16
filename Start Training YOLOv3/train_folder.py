import os

path='data/images/'



imgList=os.listdir('images')

print((len(imgList)/5)*4)

trainFile=open('train.txt','w')
testFile=open('test.txt','w')
count=0


for img in imgList:

    ## trainset 80% of dataset
    if count<=int((len(imgList)/5)*4):
        imgPath=path+ img +'\n'
        trainFile.write(imgPath)

    ## testset 20% of dataset
    elif count>int((len(imgList)/5)*4):
        imgPath=path+ img +'\n'
        testFile.write(imgPath)
    count=count+1

