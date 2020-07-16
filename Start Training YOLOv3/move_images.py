import os

imgList=os.listdir('images')
txtList=os.listdir('labels')
dataTxt=["train.txt", "test.txt"]
path = os.path.join("/home",os.getlogin(),"YOLOv3-Series","darknet","data")
for data in dataTxt:
    os.rename(data, os.path.join(path, data))

path = os.path.join(path,"obj")
makeDirectoryCommand = "mkdir -p \"{}\"".format(path)
os.system(makeDirectoryCommand)


for image in imgList:
    os.rename(os.path.join("images", image), os.path.join(path, image))
for txt in txtList:
    os.rename(os.path.join("labels", txt), os.path.join(path, txt))
print("Done")