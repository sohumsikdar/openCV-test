import cv2
import numpy as np


def read_img():
	img = cv2.imread('Resources/prague.png')
	return img


def show_img(img):
	cv2.imshow('img', img)
	cv2.waitKey(0)


def grey_img():
	img = read_img()
	img_greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# show_img(img_greyscale)
	return img_greyscale


def blur_img():
	img = read_img()
	img_blurred = cv2.GaussianBlur(img, (5, 5), 1)
	# show_img(img_blurred)
	return img_blurred


def canny_img():
	img = read_img()
	img_canny = cv2.Canny(img, 100, 100)
	show_img(img_canny)
	return img_canny


def dilated_img():
	kernel = np.ones((5, 5), np.uint8)
	img = canny_img()
	img_dilation = cv2.dilate(img, kernel, iterations=1)
	show_img(img_dilation)
	return img_dilation


def eroded_img():
	kernel = np.ones((5, 5), np.uint8)
	img = dilated_img()
	img_erosion = cv2.erode(img, kernel, iterations=1)
	show_img(img_erosion)
	return img_erosion


if __name__ == '__main__':
	# grey_img()
	# blur_img()
	# canny_img()
	# eroded_img()
	# dilated_img()
	pass
