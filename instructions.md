1.first we get codes for detection 

	a. open this link ==> https://github.com/Vivek06Sharma11/Yolov3
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

	a. open cmd and paste command "wget https://pjreddie.com/media/files/yolov3.weights"
	b. when download completed copy "yolov3.weights" and paste in "weights" folder under in our project folder "Yolov3"

2. Now run convert_weights.py in Yolov3 project folder
3. after that now run video.py file 
