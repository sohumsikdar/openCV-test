import cv2


def grey_img():
	img = cv2.imread('Resources/prague.png')
	img_greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imshow('grey scale img', img_greyscale)
	cv2.waitKey(0)


def blur_img():
	img = cv2.imread('Resources/prague.png')
	img_blurred = cv2.GaussianBlur(img, (5, 5), 1)
	cv2.imshow('blurred img', img_blurred)
	cv2.waitKey(0)


def canny_img():
	img = cv2.imread('Resources/prague.png')
	img_canny = cv2.Canny(img, 100, 100)
	cv2.imshow('Canny img', img_canny)
	cv2.waitKey(0)


if __name__ == '__main__':
	grey_img()
	blur_img()
	canny_img()
