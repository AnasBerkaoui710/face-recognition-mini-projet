import cv2
import face_recognition
from simple_facerec import SimpleFacerec


# encodages des visages depuis "Images"
sfr=SimpleFacerec()
sfr.load_encoding_images("Images/")


#loading the camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # detection de visage
    face_location, face_names = sfr.detect_known_faces(frame)
    for face_location, name in zip(face_location, face_names):
        top, right, bottom, left = face_location[0], face_location[1], face_location[2], face_location[3]


        cv2.putText(frame, name,(left, top - 5 ), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)


    cv2.imshow("Frame",frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()