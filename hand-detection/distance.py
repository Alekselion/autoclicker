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
        if results.multi_hand_landmarks:
            for handType, handLms in zip(results.multi_handedness, results.multi_hand_landmarks):
                myHand = {}
                mylmList = []
                for id, lm in enumerate(handLms.landmark):
                    px, py = int(lm.x * width), int(lm.y * height)
                    mylmList.append([px, py])

                myHand["lmList"] = mylmList
                allHands.append(myHand)
                mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)  # draw hands

        if allHands:
            hand1 = allHands[0]
            lmList1 = hand1["lmList"]

            if len(allHands) == 2:
                hand2 = allHands[1]
                lmList2 = hand2["lmList"]

                # find distance
                x1, y1 = lmList1[8]  # left forefinger 
                x2, y2 = lmList2[8]  # right forefinger
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # center between fingers 
                length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # Euclidean norm
                
                # draw legth
                cv2.circle(image, (x1, y1), 8, (255, 0, 255), -1)  # left forefinger 
                cv2.circle(image, (x2, y2), 8, (255, 0, 255), -1)  # right forefinger
                cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), 2)  # line
                cv2.circle(image, (cx, cy), 8, (255, 0, 255), -1)  # center between fingers
                cv2.putText(image, f"length: {length:.2f}", (cx-100, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)

        cv2.imshow("Image", image)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()