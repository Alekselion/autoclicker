import cv2

idCam = 0
cap = cv2.VideoCapture(idCam)
cap.set(3, 400)
cap.set(4, 450)
while cap.isOpened():
    success, image = cap.read()
    if success:
        if idCam == 0:
            image = cv2.flip(image, 1)

        cv2.imshow("Image", image)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()