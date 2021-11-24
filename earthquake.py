import cv2
import random

cap = cv2.VideoCapture(0)
cap.set(3, 400)
cap.set(4, 450)
while cap.isOpened():
    success, image = cap.read()
    if success:
        image = cv2.flip(image, 1)
        height, width = image.shape[:2]

        # shaking parameters
        border = 50
        shift = random.randint(1, border)
        moveTo = []
        moveTo.append(random.choice(["top", "bottom", "none"]))
        moveTo.append(random.choice(["left", "right", "none"]))
        
        # shaking
        if moveTo[0] == "none":
            if moveTo[1] == "none":  # nothing
                shake_image = image[border:height-border, border:width-border]
            elif moveTo[1] == "left":  # left shift
                shake_image = image[border:height-border, border-shift:width-border-shift]
            elif moveTo[1] == "right":  # right shift
                shake_image = image[border:height-border, border+shift:width-border+shift]
        
        elif moveTo[0] == "top":
            if moveTo[1] == "none":  # top shift
                shake_image = image[border-shift:height-border-shift, border:width-border]
            elif moveTo[1] == "left":  # top-left shift
                shake_image = image[border-shift:height-border-shift, border-shift:width-border-shift]
            elif moveTo[1] == "right":  # top-right shift
                shake_image = image[border-shift:height-border-shift, border+shift:width-border+shift]
        
        elif moveTo[0] == "bottom":
            if moveTo[1] == "none":  # bottom shift
                shake_image = image[border+shift:height-border+shift, border:width-border]
            elif moveTo[1] == "left":  # bottom-left shift
                shake_image = image[border+shift:height-border+shift, border-shift:width-border-shift]
            elif moveTo[1] == "right":  # bottom-right shift
                shake_image = image[border+shift:height-border+shift, border+shift:width-border+shift]
            
        cv2.imshow("image", shake_image)
                
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()