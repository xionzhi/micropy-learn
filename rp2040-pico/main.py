from time import sleep
from common.led import click_led

def starting():
    for i in range(7):
        click_led(25, i%2)
        sleep(0.1)

starting()
