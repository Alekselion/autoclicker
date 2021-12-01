import cv2
import random
import numpy as np
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
        shake_image = image[border:image_h-border, border:image_w-border]

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mouth_len = int(face_landmarks.landmark[17].y * image_h) - int(face_landmarks.landmark[0].y * image_h)
                mouth_w = mouth_len * 3
                mouth_h = mouth_len

                # top mouth
                x1 = int(face_landmarks.landmark[13].x * image_w)
                y1 = int(face_landmarks.landmark[13].y * image_h)

                # bottom mouth
                x2 = int(face_landmarks.landmark[14].x * image_w)
                y2 = int(face_landmarks.landmark[14].y * image_h)

                # distance
                length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                
                if length > 30:
                    # red image
                    canvas = np.zeros(image.shape, np.uint8)
                    canvas[:, :, :] = (0, 0, 255)
                    image = cv2.bitwise_and(image, canvas)

                    # shaking
                    if moveTo[0] == "none":
                        if moveTo[1] == "none":  # nothing
                            shake_image = image[border:image_h-border, border:image_w-border]
                        elif moveTo[1] == "left":  # left shift
                            shake_image = image[border:image_h-border, border-shift:image_w-border-shift]
                        elif moveTo[1] == "right":  # right shift
                            shake_image = image[border:image_h-border, border+shift:image_w-border+shift]
                    
                    elif moveTo[0] == "top":
                        if moveTo[1] == "none":  # top shift
                            shake_image = image[border-shift:image_h-border-shift, border:image_w-border]
                        elif moveTo[1] == "left":  # top-left shift
                            shake_image = image[border-shift:image_h-border-shift, border-shift:image_w-border-shift]
                        elif moveTo[1] == "right":  # top-right shift
                            shake_image = image[border-shift:image_h-border-shift, border+shift:image_w-border+shift]
                    
                    elif moveTo[0] == "bottom":
                        if moveTo[1] == "none":  # bottom shift
                            shake_image = image[border+shift:image_h-border+shift, border:image_w-border]
                        elif moveTo[1] == "left":  # bottom-left shift
                            shake_image = image[border+shift:image_h-border+shift, border-shift:image_w-border-shift]
                        elif moveTo[1] == "right":  # bottom-right shift
                            shake_image = image[border+shift:image_h-border+shift, border+shift:image_w-border+shift]

        cv2.imshow("image", shake_image) 
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()