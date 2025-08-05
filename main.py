from machine import Pin
from utime import sleep

print("Hello, ESP32!")

ledverde = Pin(15, Pin.OUT)
ledAmarelo = Pin(12, Pin.OUT)
ledRed = Pin(14, Pin.OUT)

while True:
  ledverde.on()
  print('LuzVerde Ligada!!')
  sleep(20)
  ledverde.off()
  sleep(0.5)

  ledAmarelo.on()
  print('Luz amarela Ligada!!')
  sleep(10)
  ledAmarelo.off()
  sleep(0.5)

  ledRed.on()
  print('Luz vermelha ligada')
  sleep(7)
  ledRed.off
  sleep(0.5)




