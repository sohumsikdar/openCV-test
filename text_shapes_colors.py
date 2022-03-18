import cv2
import numpy as np


def black_img():
	img = np.zeros((512, 512, 3), np.uint8)
	print(img)

	# cv2.imshow('black img', img)
	# cv2.waitKey(0)
	return img


def color_img():
	img = black_img()
	img[0:255] = 255, 0, 0
	img[256:512] = 0, 0, 255
	print(img)

	# cv2.imshow('coloured img', img)
	# cv2.waitKey(0)
	return img


def draw_line():
	img = black_img()
	cv2.line(img, (50, 30), (230, 390), (0, 255, 0), 3)

	cv2.imshow('img with line', img)
	cv2.waitKey(0)
	return img


def draw_rect():
	img = black_img()
	# cv2.FILLED
	cv2.rectangle(img, (120, 120), (392, 392), (186, 85, 211), cv2.FILLED)

	cv2.imshow('img with rect', img)
	cv2.waitKey(0)
	return img


def draw_circle():
	img = black_img()
	cv2.circle(img, (255, 255), 50, (127, 0, 127), cv2.FILLED)

	cv2.imshow('img with circle', img)
	cv2.waitKey(0)
	return img


def add_text():
	img = black_img()
	cv2.putText(img, 'NEEND AARHI HAI', (120, 255), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,190), 2)

	cv2.imshow('img with text', img)
	cv2.waitKey(0)
	return img


if __name__ == '__main__':
	# black_img()
	# color_img()
	# draw_line()
	# draw_rect()
	# draw_circle()
	add_text()