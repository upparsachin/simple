# import the opencv library
import cv2


camera_url = 'rtsp://admin:123@192.168.0.109:8554/profile0'
vid = cv2.VideoCapture(camera_url)

print(vid.get(3), vid.get(4))


while(T
    ret, frame = vid.read()
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break

vid.release()
cv2.destroyAllWindows()

