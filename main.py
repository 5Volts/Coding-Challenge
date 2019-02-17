import numpy as np
import cv2
import os

def prepare_data_and_label():
	image_matrix = []
	label = []
	print("Loading Image Data...")
	list_of_img = os.listdir('training_set/cats')
	cat_label = np.array([1,0])
	for image in list_of_img:
		print(image,end='\r')
		cat_pixel = np.resize(cv2.imread('training_set/cats/'+image),(200,200,3))
		image_matrix.append(cat_pixel)
		label.append(cat_label)

	list_of_img = os.listdir('training_set/dogs')
	dog_label = np.array([0,1])
	for image in list_of_img:
		print(image,end='\r')
		dog_pixel = np.resize(cv2.imread('training_set/dogs/'+image),(200,200,3))
		image_matrix.append(dog_pixel)
		label.append(dog_label)
	print("Done loading.")
	return image_matrix,label

def prepare_test_data():
	image_matrix = []
	print("Loading Test Image...")
	list_of_img = os.listdir('test_set')
	for image in list_of_img:
		print(image,end='\r')
		pixel = np.resize(cv2.imread('test_set/'+image),(200,200,3))
		image_matrix.append(pixel)
	return image_matrix			

if __name__ == "__main__":
	image_pixel_data,label = prepare_data_and_label()
	test = prepare_test_data()
	test_label = []
	"""
	Here is where you will code your algorithm. The variables that hold the 
	image data is "image_pixel_data, label, text".

	image_pixel_data :: This is an array that contains all 1000 images of cats
	and dogs. All images are reduced to a 200 by 200 resolution.

	label :: This is an array that contains all 1000 labels for the images. 
	[1,0] is a cat while [0,1] is a dog.

	test :: This is an array that contains 100 images of unknown animal. You'll
	need to use your algorithm to create the labels for all images and append it 
	into the test_label array.

	test_label :: This is an empty array where you fill up the labels. Append [1,0]
	for cat images and [0,1] for dog images.

	"""

	# Here are some examples of how to manipulate the data
	print(image_pixel_data[0]) 	# This will print out the pixel value for the first image
	print(label[0]) 			# This will print out the label of the first image
	print(test[0]) 				# This will print out the pixel value for the first test image

