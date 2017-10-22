# loading and preprocessing of image data

import numpy as np
import scipy.misc.imread

import os
import sys

class PreProcessing:

	def __init__(self, train_dir):
		self.train_dir = train_dir

	def load_paths_labels(self):
		img_paths = []
		img_labels = []

		letter_dirs = os.listdir(self.train_dir) 
		letter_dirs = filter(lambda x:x!='.DS_Store', letter_dirs)
		print(letter_dirs)
		for letter_dir in letter_dirs:
			label_dirs = os.listdir(self.train_dir+'/'+letter_dir) 
			label_dirs = filter(lambda x:x!='.DS_Store', label_dirs)
			for label_dir in label_dirs:
				img_fns = os.listdir(self.train_dir+'/'+letter_dir +'/'+label_dir)
				label_dirs = filter(lambda x:x!='.DS_Store', img_fns)
				for img_fn in img_fns:
					img_dir = self.train_dir+'/'+letter_dir +'/'+label_dir + '/'+img_fn
					img_paths.append(img_dir)
					img_labels.append(label_dir)
		return img_paths, img_labels

	def get_img_array(self, img_paths):
		x = [imread(path) for path in img_paths]
		x = np.array(x)
		return x





if __name__ == '__main__':
	train_dir = '/Users/dwalter/Classes/6.819/mini_places_challenge/data/images/train'
	pre = PreProcessing(train_dir)
	x_paths, y = pre.load_paths_labels()
	x = pre.get_img_array(x_paths)
