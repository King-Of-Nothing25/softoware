from pyexpat.errors import XML_ERROR_UNKNOWN_ENCODING
import image_processor
import camera
import motion
import cv2
import time
import serial
import struct

def main_loop():
  debug = True

  ser = serial.Serial("")
    
  cam = camera.RealsenseCamera(exposure = 100)
    
  processor = image_processor.ImageProcessor(cam, debug=debug)

  processor.start()

  start = time.time()
  fps = 0
  frame = 0
  frame_cnt = 0

  try:
    while True:
      processedData = processor.process_frame(aligned_depth=False)

      frame_cnt += 1
      frame += 1
      if frame % 30 == 0:
        frame = 0
        end = time.time()
        fps = 30 / (end - start)
        start = end
        print("FPS: {}, framecount: {}".format(fps, frame_cnt))
        print("ball_count: {}".format(len(processedData.balls)))
        try:              
           print(processedData.balls[0].size)
           robo_x =processedData.balls[0].x
           robo_x -= 424
           robo_y =processedData.balls[0].y
           robo_y -= 320
           print("x: ",processedData.balls[0].x)
           print("y: ",processedData.balls[0].y)
        except:
          pass

        #send motor data
        ser = serial.

        #if (robo_y == 320 & robo_x == 424):
        #    print("nice")
                

        #if (frame_cnt > 1000):
        #    break

        if debug:
          debug_frame = processedData.debug_frame

          cv2.imshow('debug', debug_frame)

          k = cv2.waitKey(1) & 0xff
          if k == ord('q'):
            break
  except KeyboardInterrupt:
    print("closing...")
  finally:
    cv2.destroyAllWindows()
    processor.stop()

main_loop()
'''
typedef struct __attribute__((packed)) Command {
  int16_t speed1;
  int16_t speed2;
  int16_t speed3;
  uint16_t throwerSpeed;
  uint8_t disableFailsafe; // 1 to disable failsafe, anything else to enable
  uint16_t delimiter;
} Command;
'''
disable_failsafe = 0

speed1 = 10
speed2 = 20
speed3 = 30
thrower_speed = 10


struct.pack('<hhhHBH', speed1, speed2, speed3, thrower_speed, disable_failsafe, 0xAAAA)