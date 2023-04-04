from machine import Pin
import time


def click_led(pin: int, value: int) -> int:
    pin = Pin(pin, Pin.OUT)
    return pin.value(value)

def test_click_led():
    for i in range(9):
        click_led(25, i%2)
        time.sleep(0.1)

if __name__ == '__main__':
    test_click_led()
