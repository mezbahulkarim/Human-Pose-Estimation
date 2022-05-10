#%%
#IMPORTS 
import cv2
import mediapipe as mp
import time

#%%
#Load Video 
vid = cv2.VideoCapture('golf.mp4')

# %%      
                #Frame by Frame Processing

#Setting up Mediapipe
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

prev_time=0

#Read each Frame and Track Landmarks 
while True:
    #Read next frame, convert to rgb 
    success, image = vid.read()
    
    if(success == False):
        print("ERROR READING FRAME!")
        break
   
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)       
      
    #Mark 'landmarks' using Mediapipe
    landmarks = pose.process(rgb)
    if(landmarks.pose_landmarks):
        mpDraw.draw_landmarks(image, landmarks.pose_landmarks, mpPose.POSE_CONNECTIONS)

    #FPS Calculator 
    present_time = time.time()
    fps = 1/(present_time-prev_time)
    prev_time = present_time

    #Display Frame
    cv2.putText(image, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (0, 255, 0), 3)
    cv2.imshow("Image", image)
    cv2.waitKey(1)
