import cv2


def read_img():
	img = cv2.imread('Resources/prague.png')
	return img


def show_img(img):
	cv2.imshow('img', img)
	cv2.waitKey(0)


def resize_img():
	img = read_img()
	img_resized = cv2.resize(img, (500, 300))
	show_img(img_resized)
	return img_resized


def crop_img():
	img = read_img()
	img_cropped = img[0:500][200:900]
	show_img(img_cropped)
	return img_cropped


if __name__ == '__main__':
	# resize_img()
	# crop_img()
	pass
