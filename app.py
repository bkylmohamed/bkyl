import face-recognition
import cv2
import numpy as np
import os



path='persons'
images=[]
classNames=[]
personslist=os.listdir(path)

for cl in personslist:
    curpersonn=cv2.imread(f'{path}/{cl}')
    images.append(curpersonn)
    classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    def findEncodeings(image):
        encodelist=[]

        for img in images:
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            encode=face_recognition.face_encodings(img)[0]
            encodelist.append(encode)
            return encodelist

            encodelistKnown=findEncodeings(images)
            print('Encoding Complete.')

            cap=cv2.VideoCapture(1)

            while True:
                _, img=cap.read()

                imgS=cv2.resize(img,(0,0) ,None,0.25,0.25)
                imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)


                faceCurentFrame=face_recognition.face_locations(imgS)
                encodeCurentFrame=face_recognition.face_encodings(imgS,faceCurentFrame )


                for encodeface,faceLoc in zip(encodeCurentFrame,faceCurentFrame):
                    matches=face_recognition.compare_faces(encodelistKnown, encodeface)
                    faceDis=face_recognition.face_distance(encodelistKnown, encodeface )
                    matchIndex=np.argmin(faceDis)

                    if matches[ matchIndex]:
                        name=classNames[ matchIndex].upper()
                        print(name)
                        y1, x2, y2, x1 =faceLoc
                        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4


                        cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
                        cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
                        cv2.putText(img,name,(x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


                        cv2.imshow('Face Recogntion',img)
                        cv2.waitKey(1)


