import cv2
img = cv2.imread("solar-system.jpg")


cv2.putText(img,  
           "SUN",
           (5, 225),  
           cv2.FONT_HERSHEY_COMPLEX,
           1.5, 
           (255,255,255)
           )


cv2.putText(img,  
           "Mercury",
           (115, 185),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5, 
           (255,255,255)
           )

cv2.putText(img,  
           "Venes",
           (190, 260),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5, 
           (255,255,255)
           )

cv2.putText(img,  
           "Earth",
           (285, 175),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5, 
           (255,255,255)
           )

cv2.putText(img,  
           "Mars",
           (380, 260),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5, 
           (255,255,255)
           )

cv2.putText(img,  
           "Jupeter",
           (550, 50),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5, 
           (255,255,255)
           )

cv2.putText(img,  
           "Saturn",
           (770, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5, 
           (255,255,255)
           )

cv2.putText(img,  
           "Uranes",
           (970, 140),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5, 
           (255,255,255)
           )

cv2.putText(img,  
           "Neptune",
           (1105, 285),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5, 
           (255,255,255)
           )

cv2.imshow("output",img)
cv2.waitKey(0)