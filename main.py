import easyocr
import cv2

capture=cv2.VideoCapture(0)
while True:
    ret,frame=capture.read()
    cv2.imshow('Color',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("MachineLearning.jpg",frame)
        break
capture.release()
cv2.destroyAllWindows()


# reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
# result = reader.readtext('chinese.jpg')