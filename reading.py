import cv2


def img_read():
	img = cv2.imread('Resources/chungus.png')
	cv2.imshow("Output", img)
	cv2.waitKey(0)


def video_read():
	cap = cv2.VideoCapture('Resources/sample.mp4')
	while True:
		success, img = cap.read()
		cv2.imshow('Video', img)
		# waitKey returns a 32 bit int and waits for keyboard input
		# 32 bit & 0xFF gives the last 8 bits -> 256 which is max ascii
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break


def webcam_read():
	cap = cv2.VideoCapture(0)
	cap.set(3, 640)
	cap.set(4, 480)
	cap.set(10, 100)
	while True:
		success, img = cap.read()
		cv2.imshow('Video', img)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break


if __name__ == '__main__':
	webcam_read()
