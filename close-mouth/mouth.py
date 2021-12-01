import cv2
import random
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
mp_drawing_styles = mp.solutions.drawing_styles
drawing_spec = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1)
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)
cap.set(3, 400)
cap.set(4, 450)
while cap.isOpened():
    success, image = cap.read()
    if success:
        image = cv2.flip(image, 1)
        image_h, image_w = image.shape[:2]

        # shaking parameters
        border = 50
        shift = random.randint(1, border)
        moveTo = []
        moveTo.append(random.choice(["top", "bottom", "none"]))
        moveTo.append(random.choice(["left", "right", "none"]))

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:

                mouth_len = int(face_landmarks.landmark[17].y * image_h) - int(face_landmarks.landmark[0].y * image_h)
                mouth_w = mouth_len * 3
                mouth_h = mouth_len

                # area mouth
                x = int(face_landmarks.landmark[13].x * image_w - mouth_w / 2)
                y = int(((face_landmarks.landmark[13].y + face_landmarks.landmark[14].y) / 2) * image_h - mouth_h / 2)
                cv2.rectangle(image, (x, y), (x + mouth_w, y + mouth_h), (255, 255, 255), -1)

                # center mouth
                cx = int(face_landmarks.landmark[13].x * image_w)
                cy = int(((face_landmarks.landmark[13].y + face_landmarks.landmark[14].y) / 2) * image_h)
                cv2.circle(image, (cx, cy), 10, (0, 255, 0), -1)

                # top mouth
                x1 = int(face_landmarks.landmark[13].x * image_w)
                y1 = int(face_landmarks.landmark[13].y * image_h)
                cv2.circle(image, (x1, y1), 10, (0, 0, 255), -1)

                # bottom mouth
                x2 = int(face_landmarks.landmark[14].x * image_w)
                y2 = int(face_landmarks.landmark[14].y * image_h)
                cv2.circle(image, (x2, y2), 10, (255, 0, 0), -1)

        cv2.imshow("image", image)
                
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()