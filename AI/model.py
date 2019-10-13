import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.layers import Convolution2D, MaxPooling2D

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

from keras import backend as K
K.set_image_dim_ordering('th')
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Flatten
from sklearn import preprocessing
from warnings import filterwarnings

# W A R N I N G    H A N D L I N G
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.logging.set_verbosity(tf.logging.ERROR)
filterwarnings('ignore')

PATH = os.getcwd()
data_path = PATH + '/data'
data_dir_list = os.listdir(data_path)

img_rows = 128
img_cols = 128
num_channel = 1
num_epoch = 10

# Number of classes
num_of_classes = 4

img_data_list = []

for dataset in data_dir_list:
    img_list = os.listdir(data_path + '/' + dataset)
    print('Loaded the images of datasets-'+'{}\n'.format(dataset))
    for img in img_list:
        input_img = cv2.imread(data_path + '/' + dataset + '/' + img)
        input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
        input_img_resize = cv2.resize(input_img,(128, 128))
        img_data_list.append(input_img_resize)

img_data = np.array(img_data_list)
img_data = img_data.astype('float32')
img_data /= 255
print(img_data.shape)

if num_channel == 1:
    if K.image_dim_ordering() == 'th':
        img_data = np.expand_dims(img_data, axis=1)
        print(img_data.shape)
    else:
        img_data = np.expand_dims(img_data, axis=4)
        print(img_data.shape)
else:
    if K.image_dim_ordering() == 'th':
        img_data = np.rollaxis(img_data, 3, 1)
        print(img_data.shape)

USE_SKLEARN_PREPOCESSING = False

if USE_SKLEARN_PREPOCESSING:
    def image_to_feature_vector(image, size=(128, 128)):
        return cv2.resize(image, size).flatten()

    img_data_list = []
    for dataset in data_dir_list:
        img_list = os.listdir(data_path + '/' + dataset)
        print("Loaded the images of dataset-"+"{}\n".format(dataset))
        for img in img_list:
            input_img = cv2.imread(data_path + "/" + dataset + "/" + img)
            input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
            input_img_flatten = image_to_feature_vector(input_img, (128, 128))
            img_data_list.append(input_img_flatten)

    img_data = np.array(img_data_list)
    img_data = img_data.astype('float32')
    print(img_data.shape)
    img_data_scaled = preprocessing.scale(img_data)
    print(img_data_scaled.shape)

    print(np.mean(img_data_scaled))
    print(np.std(img_data_scaled))

    print(img_data_scaled.mean(axis=0))
    print(img_data_scaled.std(axis=0))

    if K.image_dim_ordering() == 'th':
        img_data_scaled = img_data_scaled.reshape(img_data.shape[0], num_channel, img_rows, img_cols)
        print(img_data_scaled.shape)

    else:
        img_data_scaled = img_data_scaled.reshape(img_data.shape[0], img_rows, img_cols, num_channel)
        print(img_data_scaled.shape)

    if K.image_dim_ordering() == 'th':
        img_data_scaled = img_data_scaled.reshape(img_data.shape[0], num_channel, img_rows, img_cols)
        print(img_data_scaled.shape)

    else:
        img_data_scaled = img_data_scaled.reshape(img_data.shape[0], img_rows, img_cols, num_channel)
        print(img_data_scaled.shape)

if USE_SKLEARN_PREPOCESSING:
    img_data = img_data_scaled

# LABELING
num_classes = 4
num_of_samples = img_data.shape[0]
labels = np.ones((num_of_samples,),dtype='int64')

labels[0:202] = 0
labels[202:404] = 1
labels[404:606] = 2
labels[606:] = 3

names = ["rect", "star", "circle", "else"]

# One hot coding
Y = np_utils.to_categorical(labels, num_classes)

# Shaffle
x, y = shuffle(img_data, Y, random_state=2)

# Split
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=2)

# Model variables
input_shape = img_data[0].shape
number_of_filters = 32                      # Integer, the dimensionality of the output space
kernel_size = (3, 3)                        # An integer or tuple/list of 2 integers, specifying
activation_function = ("relu", "sigmoid")   # Activation function to use
size_of_pool = (2, 2)                       # Integer, size of the max pooling windows.
num_of_strides = 2                          # Integer, or None. Factor by which to downscale.
dense_units = (128, 4)                      # Positive integer, dimensionality of the output space.
type_of_optimizer = "adamax"                # String (name of optimizer) or optimizer instance
loss_function = "binary_crossentropy"       # String (name of objective function) or objective function
type_of_metrics = ["accuracy"]              # List of metrics to be evaluated by the model during training and testing

# M O D E L    B U I L D I N G
model = Sequential()    # The Sequential model is a linear stack of layers.
# First convolution layer
model.add(Convolution2D(number_of_filters, kernel_size, input_shape=input_shape, activation=activation_function[0]))
# First max pooling layer
model.add(MaxPooling2D(pool_size=size_of_pool, strides=num_of_strides))
# Second convolution layer
model.add(Convolution2D(number_of_filters, kernel_size, activation=activation_function[0]))
# Second max pooling layer
model.add(MaxPooling2D(pool_size=size_of_pool, strides=num_of_strides))
# Third convolution layer
model.add(Convolution2D(number_of_filters, kernel_size, activation=activation_function[0]))
# Third max pooling layer
model.add(MaxPooling2D(pool_size=size_of_pool, strides=num_of_strides))
# Flattening the net
model.add(Flatten())
# Fully connecting
model.add(Dense(units=dense_units[0], activation=activation_function[0]))
# Fully connecting
model.add(Dense(units=dense_units[1], activation=activation_function[1]))
# Compiling the model
model.compile(optimizer=type_of_optimizer, loss=loss_function, metrics=type_of_metrics)

# Viewing mode config
model.summary()
model.get_config()
model.layers[0].get_config()
model.layers[0].get_weights()
np.shape(model.layers[0].get_weights()[0])

# Training
model_log = model.fit(  X_train, Y_train,
                        batch_size=None,
                        epochs=num_epoch,
                        steps_per_epoch=100,
                        verbose=1,
                        validation_data=(X_test, Y_test),
                        validation_steps=10)

loss, accuracy = model.evaluate(X_test, Y_test, verbose=False)

plt.plot(model_log.history['acc'])
plt.plot(model_log.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['training', 'validation'], loc='best')
plt.show()

# # Save
# model_json = model.to_json()
# with open("model.json", "w") as json_file:
#     json_file.write(model_json)
# # serialize weights to HDF5
# model.save_weights("model.h5")
model.save("model.h5")
print("Saved model to disk")
