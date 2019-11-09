Step 1:
(Optional) Create a virtual environment

$ virtualenv -p python3 .
$ source bin/activate
 
Step 2:
Install the libraries and requirements
$ pip install -r requirements.txt

Step 3:
Go to "project_source" folder

Step 4:
run
$ python predict_disease.py


Weights for Cassava need to be put at files: 
/project_source/cassava/bin/yolo.weights
/project_source/cassava/ckpt/yolo-new-17400.data-00000-of-00001
/project_source/cassava/ckpt/yolo-new-17400.index
/project_source/cassava/ckpt/yolo-new-17400.meta
