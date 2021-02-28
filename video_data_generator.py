#train a neural network from input video feed
import numpy as np
import cv2
vid = cv2.VideoCapture('trackmania_test_vid.mp4')
w = 1280//2
h = 720//2

vid_data = np.empty((360, 640, 3))
#print(vid_data.shape)


def process_frame(img):
    global vid_data
    img = cv2.resize(img, (w, h))
    cv2.imshow('Frame', img)
    cv2.waitKey(1)
    vid_data = np.append(vid_data, img, axis=0)
    #print(img.shape)


# Read until video is completed
n = 0
while vid.isOpened():
    # Capture frame-by-frame
    ret, frame = vid.read()
    if ret:
        #print("frame = {}".format(frame.shape))
        process_frame(frame)
        n = n + 1
        '''
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
        break
        '''
    else:
        break

# When everything done, release the video capture object
vid.release()

# Closes all the frames
cv2.destroyAllWindows()
print(vid_data.shape)
vid_data = vid_data.reshape((vid_data.shape[0], -1))
print(vid_data.shape)
# n = 1340
#print('No. of frames = {}'.format(n))

np.savetxt("trackmania_vid_data2D_360x640.csv", vid_data, delimiter=",")

#50580,320,3 ---> 281,180,320,3
#101160,640,3 ---> 281,360,640,3
