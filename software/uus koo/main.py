from pyexpat.errors import XML_ERROR_UNKNOWN_ENCODING
import image_processor
import camera
import motion
import cv2
import time

typedef struct __attribute__((packed)) Command {
  int16_t speed1;
  int16_t speed2;
  int16_t speed3;
  uint16_t throwerSpeed;
  uint8_t disableFailsafe; // 1 to disable failsafe, anything else to enable
  uint16_t delimiter;
} Command;

disable_failsafe = 0

struct.pack('<hhhHBH', speed1, speed2, speed3, thrower_speed, disable_failsafe, 0xAAAA)