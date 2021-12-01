import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

fingertips = [4, 8, 12, 16, 20]

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
                myHand = {}
                mylmList = []
                for lm in handLms.landmark:
                    px, py = int(lm.x * width), int(lm.y * height)
                    mylmList.append([px, py])

                myHand["lmList"] = mylmList
                myHand["type"] = "Left" if handType.classification[0].label == "Left" else "Right"
                allHands.append(myHand)
                
            hand1 = allHands[0]
            lmList1 = hand1["lmList"]
            handType1 = hand1["type"]

            # find fingers
            if results.multi_hand_landmarks:
                fingers = []

                # thumb (1 hand)
                if handType1 == "Left":
                    fingers.append(1) if lmList1[fingertips[0]][0] > lmList1[fingertips[0]-1][0] else fingers.append(0)
                else:
                    fingers.append(1) if lmList1[fingertips[0]][0] < lmList1[fingertips[0]-1][0] else fingers.append(0)

                # other fingers (1 hand)
                for id in range(1, 5):
                    fingers.append(1) if lmList1[fingertips[id]][1] < lmList1[fingertips[id]-2][1] else fingers.append(0)

                if len(allHands) == 2:
                    hand2 = allHands[1]
                    lmList2 = hand2["lmList"]
                    handType2 = hand2["type"]

                    # thumb (2 hand)
                    if handType2 == "Left":
                        fingers.append(1) if lmList2[fingertips[0]][0] > lmList2[fingertips[0]-1][0] else fingers.append(0)
                    else:
                        fingers.append(1) if lmList2[fingertips[0]][0] < lmList2[fingertips[0]-1][0] else fingers.append(0)

                    # other fingers (2 hand)
                    for id in range(1, 5):
                        fingers.append(1) if lmList2[fingertips[id]][1] < lmList2[fingertips[id]-2][1] else fingers.append(0)

                countFingers = fingers.count(1)
                cv2.putText(image, str(countFingers), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 255), 10)

        cv2.imshow("Image", image)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()