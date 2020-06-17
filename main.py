import cv2
import numpy as np
import math

# importing the video file
vid = cv2.VideoCapture("video.mp4")

while(vid.isOpened()):
    # reading a single frame
    ret, frame = vid.read()

    # filtering by a threshold
    _, threshold_frame = cv2.threshold(frame, 150, 255, cv2.THRESH_BINARY)

    # creating a blob detector options object
    params = cv2.SimpleBlobDetector_Params()

    # setting up the optional parameters to pass to the blob detector
    # filtering out the blobs which has area less than 500 pixels
    params.filterByArea = True
    params.minArea = 500

    # creating a blob detector object with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # detecting blobs of the threshhold_frame and getting keypoint objects of the blobs
    keypoints = detector.detect(threshold_frame)

    # creating a new frame from the original frame with circles marking the blob positions according to the area of the blob
    keypoints_frame = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # setting up the font to display area value
    font = cv2.FONT_HERSHEY_PLAIN

    # placing area values of each blob of the keypoint_frame in the middle of the circle indicating the blob
    for keyPoint in keypoints:
        keypoints_frame = cv2.putText(keypoints_frame, str(int (keyPoint.size/2 * keyPoint.size/2 * math.pi )) , (int(keyPoint.pt[0]), int(keyPoint.pt[1])) , font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # output the keypoint_frame
    cv2.imshow('Blobs', keypoints_frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()