import cv2

img = cv2.imread("solar-system.jpg")

text1 = "Mercury"
cv2.putText(img, text1, (125, 250), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1, color=(255,255,255))
text2 = "Venus"
cv2.putText(img, text2, (190, 190), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1, color=(255,255,255))
text3 = "Earth"
cv2.putText(img, text3, (250, 250), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1, color=(255,255,255))
text4 = "Mars"
cv2.putText(img, text4, (375, 250), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1, color=(255,255,255))
text5 = "Jupiter"
cv2.putText(img, text5, (500, 390), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=2, color=(255,255,255))
text6 = "Saturn"
cv2.putText(img, text6, (780, 320), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1.5, color=(255,255,255))
text7 = "Uranus"
cv2.putText(img, text7, (980, 295), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1.5, color=(255,255,255))
text7 = "Neptune"
cv2.putText(img, text7, (1090, 290), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1.3, color=(255,255,255))
cv2.imwrite("solar-system-final.jpg", img)
cv2.imshow("Image.jpg", img)
cv2.waitKey(0)

