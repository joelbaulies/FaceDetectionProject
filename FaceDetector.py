import cv2
import FaceDetectionModule as fdm
import time


cap = cv2.VideoCapture(0)
pTime = 0
detector = fdm.FaceDetector()
while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)
    print(bboxs)
    # img = cv2.resize(img, (960, 540))  # en caso de que el video sea muy grande
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(10)