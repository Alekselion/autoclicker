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
        height, width = image.shape[:2]
        if results.multi_hand_landmarks:  # hand found
            for handType, handLms in zip(results.multi_handedness, results.multi_hand_landmarks):
                mylmList = []
                xList = []
                yList = []
                for id, lm in enumerate(handLms.landmark):
                    px, py = int(lm.x * width), int(lm.y * height)
                    mylmList.append([px, py])
                    xList.append(px)
                    yList.append(py)

                # bounding box
                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                boxW, boxH = xmax - xmin, ymax - ymin
                bbox = xmin, ymin, boxW, boxH
                cx, cy = bbox[0] + (bbox[2] // 2), bbox[1] + (bbox[3] // 2)  # center

                leftRight = "Left" if handType.classification[0].label == "Left" else "Right"
                
                # draw hands
                mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
                
                # draw bouding box and center
                cv2.rectangle(image, (bbox[0]-20, bbox[1]-20), (bbox[0] + bbox[2]+20, bbox[1] + bbox[3]+20), (0, 255, 0), 2)
                cv2.putText(image, leftRight, (bbox[0]-30, bbox[1]-30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
                cv2.circle(image, (cx, cy), 8, (0, 255, 0), -1)
                
        cv2.imshow("Image", image)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()