import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

# read camera
idCam = 0
widthImage, heightImage = 640, 480
cap = cv2.VideoCapture(idCam)
cap.set(3, widthImage)
cap.set(4, heightImage)
while cap.isOpened():
    success, image = cap.read()
    if success:
        if idCam == 0:
            image = cv2.flip(image, 1)
            
        # find hands
        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        allHands = []
        if results.multi_hand_landmarks:  # hand found
            for handType, handLms in zip(results.multi_handedness, results.multi_hand_landmarks):
                mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)  # draw
                
        cv2.imshow("Image", image)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()