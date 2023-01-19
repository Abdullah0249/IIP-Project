import cv2

webcam = cv2.VideoCapture(0)
cv2.namedWindow("Introduction to Image Processing Project")
image_counter=0
while True:
    ret,frame=webcam.read()
    if not ret:
        print("Failed to grab frame.")
        break
    cv2.imshow("Introduction to Image Processing Project",frame)

    k=cv2.waitKey(1)
    if k%256 == 27:
        print("Closing....")
        break
    if k%256 == 32:
        img_name="opencv_frame_{}.png".format (image_counter)
        cv2.imwrite(img_name,frame)
        print("{}written!".format(img_name))
        image_counter=+1
    if k%256 == 115:
        img=cv2.imread('opencv_frame_0.png')
        cv2.imshow("Captured Image",img)
        cv2.waitKey(0)
    

webcam.release()
cv2.destroyAllWindows()

