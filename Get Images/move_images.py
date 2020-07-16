import os

imgList=os.listdir('images')
path = os.path.join("/home",os.getlogin(),"YOLOv3-Series","OpenLabelling","images")
makeDirectoryCommand = "mkdir -p \"{}\"".format(path)
os.system(makeDirectoryCommand)


for image in imgList:
    os.rename(os.path.join("images", image), os.path.join(path, image))
print("Done")