import cv2
import numpy as np


def warp_perspective():
	img = cv2.imread('Resources/cards.png')
	width, height = 350, 225
	pts1 = np.float32([[115, 207], [887, 34], [215, 547], [1025, 356]])
	pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
	matrix = cv2.getPerspectiveTransform(pts1, pts2)
	warped_img = cv2.warpPerspective(img, matrix, (width, height))

	# cv2.imshow('warped img', warped_imp)
	# cv2.waitKey(0)

	return warped_img


def stack_img():
	img = warp_perspective()
	horizontal_stack = np.hstack((img, img))

	cv2.imshow('stacked imgs' ,horizontal_stack)
	cv2.waitKey(0)


if __name__ == '__main__':
	# warp_perspective()
	stack_img()