For yolov3 detection using pre trained weight file:

1. first we get codes for detection 

	a. open this link "https://github.com/Vivek06Sharma11/Yolov3".
	b. there's big green button name "Code" click the button and now click on Download ZIP 
	c. go in your Download folder right click on Yolov3.zip or Yolov3.rar click on "extract here"
	d. open cmd and type command:
		1."pip install numpy"
		2."pip install opencv-python"
		3."pip install tensorboard"
		4."pip install tensorboard-plugin-wit"
		5."pip install tensorflow"
		6."pip install tensorflow-estimato"

our code need trained data for saving our time download pre-trained weight file

	a. open cmd and paste command "wget https://pjreddie.com/media/files/yolov3.weights".
	b. when download completed copy "yolov3.weights" and paste in "weights" folder under our project folder "Yolov3"

2. Now run "convert_weights.py" in "Yolov3" project folder #(Yolov3\convert_weights.py )
3. after that now run "video.py" file (for detecttion through your camera)


For train our own costom data:

1. Open "Yolov3" project folder if you didn't clone yet go to the link "https://github.com/Vivek06Sharma11/Yolov3"
	a. there's big green button name "Code" click the button and now click on Download ZIP 
	b. go in your Download folder right click on Yolov3.zip or Yolov3.rar click on "extract here"
	c. open cmd and type command:
		1."pip install numpy"
		2."pip install opencv-python"
		3."pip install tensorboard"
		4."pip install tensorboard-plugin-wit"
		5."pip install tensorflow"
		6."pip install tensorflow-estimato"

2. Get images or Dataset:
	a. Now go open directory "Get images" now open file "js_console.js" and copy all line (1-127) or (press ctrl+a and ctrl+c) #(Yolov3\Get images\js_console.js)

	b. Now go to the google and search what you want to detect for example search for cars 

	c. click on its "images" option

	d. Now scroll down until you see "show more" in google at the bottom of images list

	e. "Right Click" on any of "images" Click on "inspect" present at the very last

	f. Now paste what we have copied from "js_console.js" or "ctrl+v" on console

	g. It give you a "urls.txt" file in "Download" section put that "urls.txt" file into your "get images" folder present in "Yolov3" project folder  #(Yolov3\get images)

	h. And now run "download_images.py"

	i. It create a folder name "images" which start collecting all your cars images(need 1000-1500 images for better aquracy)

3. Labelling section:
	a. When above process finish now copy "images" folder and paste it in folder "Openlabelling" present in project folder "Yolov3" folder 
	
	b. Create open notepad and write all objects name that we want to be detect in a frame and save in same folder "Openlabelling" name as "obj.name"

	c. Now run "run.py" file it open a window of images where you need to labelling all images

	d. there would be 2 slide bar if 2 or more than 2 type of object you want to detect

	e. one slide bar is to "next" or "previous" the image and second one is to next and previous of name of the objects

	f. Now make a box where you find a car click "top left" of car and drag cursor to the "bottom right" to make a box and click again to release

	g. Do this for all 1000-1500 images you have collect

	h. It Create a "labels" name in which it generate .txt file (coordinates of boxes)
	
4. Creating "train.txt" and "test.txt" :

	a. When above process complete copy and paste "images" folder "labels" folder and "obj.name" file into "Start Training YOLOv3"

	a. Get into folder name "Start Training YOLOv3" in a project folder "Yolov3" and run file "train_folder.py"

	b. above line gives you 2 file "train.txt" and "test.txt"

5. Now its time to install "darknet" found in a link https://github.com/pjreddie/darknet
	a.click on big green button name "Code" now click on Download ZIP 
	b. go in your Download folder right click on "darknet.zip" or "Yolov3.rar" click on "extract here"

6. Now copy and paste all data "images" folder, "labels" folder, "train.txt" file, "test.txt" file and "obj.names" file all paste in "data" folder present in "darknet" folder

7. Now open "yolov3.cfg" file from "cfg" folder in "darknet" directory and make given changes(darknet\cfg\yolov3.cfg)
Note: clases = no. of object list present in "obj.names" file 
Note: for example classes = 1

	# Line 8 & 9: 
	width = 416, height = 416 

	# Line 20 
	max_batches = 6000 

	# Line 22 
	steps = 5400 

	#Line 603, 689, 776: ((filters = (classes + 5)*3))
	filters = 18

	#Line 610, 696, 783: (if there is 1 object for detection)
	classes = 1

8. open folder "example" from "darknet" directory, open "detector.c" at line 138, modify this line below:

if(i%1000==0 || (i < 1000 && i%100 == 0)){

9. now open "data" folder from "darknet" directory: (darknet\data)
Open notpad and write following line below
	classes= 1 #number of objects, in our case is 1
	train  = data/train.txt
	valid  = data/test.txt
	names = data/obj.names
	backup = backup
save this notepad file as "obj.data" and send to folder in "data" present in "darknet" directory

10. Open "Makefile" present in "darknet" folder and make change GPU = 1 ,CUDNN=1 and OPENCV=1 (darknet\Makefile)

Download "https://pjreddie.com/media/files/darknet53.conv.74" and put it in "darknet" folder

11. Now make darknet folder a zip file Or "right click" on darknet folder and click "send to" option and then press "compress" select .zip option
	a. Now open this link "https://drive.google.com/drive/u/0/my-drive"
	b. Now click on a "+ New" above od "My Drive" option and click on "Folder upload"
	c. Upload "darknet.zip" file in your google drive
	d. Again click on "+ New" above "My Drive" option and click on "Folder" and set its name as "backup"

Now its time to start train our data

1. search and open "google colab" in google OR click open "https://colab.research.google.com/"
2. To enable GPU, select "Runtime" -> "Change runtime type", in Hardware accelerator select "GPU"
3. Now write following:(press "shift+enter" to execute)
	a. from google.colab import drive
	drive.mount('/content/drive')   #(shift+enter)

	b. !unzip "/content/drive/My Drive/Sharing_storage1/darknet.zip" #(shift+enter)

	c. %cd /content/darknet 
	!make
	!chmod +x ./darknet  #(shift+enter)

	d. !rm /content/darknet/backup -r
	!ln -s /content/drive/'My Drive'/backup /content/darknet  #(shift+enter)

	e. !sudo apt install dos2unix  #(shift+enter)

	f. !dos2unix ./data/train.txt
	!dos2unix ./data/test.txt
	!dos2unix ./data/obj.data
	!dos2unix ./data/obj.names
	!dos2unix ./cfg/yolov3.cfg   #(shift+enter)

	g. %cd /content/darknet
	!./darknet detector train data/obj.data cfg/yolov3.cfg darknet53.conv.74  #(shift+enter)

Run this below command only when it stop training at the middle
Note: yolov3_900.weights = last weight saved in backup file
	a. !./darknet detector train data/obj.data cfg/yolov3.cfg backup/yolov3_900.weights

Now Let It Be

