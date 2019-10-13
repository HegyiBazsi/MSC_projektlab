#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
                help="path to trained model model")
ap.add_argument("-l", "--labelbin", required=True,
                help="path to label binarizer")
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])
output = image.copy()

# pre-process the image in the exact same manner as training
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.resize(image, (128, 128))
image = image.reshape((1, 128, 128))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

# load the trained convolutional neural network and the label binarizer
print("[INFO] loading network...")
model = load_model(args["model"])
lb = pickle.loads(open(args["labelbin"], "rb").read())
# classify the input image
print("[INFO] classifying image...")
proba = model.predict(image)[0]


for i in range(4):
	label = lb.classes_[i]
	filename = args["image"][args["image"].rfind(os.path.sep) + 1:]
	correct = "correct" if filename.rfind(label) != -1 else "incorrect"
	label = "{}: {:.2f}% ({})".format(label, proba[i] * 100, correct)
	print("class: ", lb.classes_[i], "result: ", proba[i] * 100, "\n")
	result = np.where(proba == np.amax(proba))
	# print('Returned tuple of arrays :', result)
	# print('List of Indices of maximum element :', result[0])
	best_class = lb.classes_[result]
	best_result = np.amax(proba)

final_result = (str(best_class) + " " +str(best_result))
print(final_result)

output = imutils.resize(output, width=600)
cv2.putText(output, 'final prediction:{}'.format(final_result), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,
			cv2.LINE_AA)
cv2.imshow("Output", output)
cv2.waitKey(0)

# Terminal Command to run on an example:
# python classify.py --model <MODEL_NAME>.model --labelbin lb.pickle --image examples/<FILE_NAME.jpg>
# python test.py --model model2.h --labelbin lb.pickle --image frame240.jpg
# image exits on the press of a key
