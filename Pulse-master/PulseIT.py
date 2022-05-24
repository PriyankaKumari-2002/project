from retinaface.pulse_retina import PulseMonitor
import cv2
import traceback
import retinaface.pulse_retina
#from retinaface import pulse_retina
processor = retinaface.pulse_retina.PulseMonitor()

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    try:
        processor.frame_in = frame
        processor.run()
  
        cv2.imshow("Frame", processor.frame_out)
        cv2.waitKey(1)

    except Exception as e:
        traceback.print_exc()
