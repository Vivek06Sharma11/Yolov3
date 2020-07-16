import os

imgList=os.listdir('images')
txtList=os.listdir('labels')
path = os.path.join("/home",os.getlogin(),"YOLOv3-Series","Start Training YOLOv3","images")
path1 = os.path.join("/home",os.getlogin(),"YOLOv3-Series","[part 5]Start Training YOLOv3","labels")
makeDirectoryCommand = "mkdir -p \"{}\"".format(path)
os.system(makeDirectoryCommand)
makeDirectoryCommand = "mkdir -p \"{}\"".format(path1)
os.system(makeDirectoryCommand)


for image in imgList:
    os.rename(os.path.join("images", image), os.path.join(path, image))
for txt in txtList:
    os.rename(os.path.join("labels", txt), os.path.join(path1, txt))
print("Done")