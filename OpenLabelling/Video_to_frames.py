import cv2 
import os

cap=cv2.VideoCapture("videoplayback (7).mp4")
makeDirectoryCommand = "mkdir -p \"{}\"".format("images")
os.system(makeDirectoryCommand)
# cap=cv2.VideoCapture("/home/vivek/Test_Videos/test1.mp4")
i=0
prop=cv2.CAP_PROP_FRAME_COUNT
total=int(cap.get(prop))
print(total)
print(total)
while 1:
    for i in range(total):
        _,frame=cap.read()
        if i>=40:
            cv2.imwrite("images/frame_{:06}.jpg".format(i),frame)
            print("images/frame_{:06}.jpg".format(i))
        if _ == False:
            break
        
    break
cap.release()
cv2.destroyAllWindows()
print("Done")