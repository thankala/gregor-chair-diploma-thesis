import time
from gpio.gpio_controller import GpioController

class PickAndPlace:
    def __init__(self):
        print("\n \n PickAndPlace has just started \n \n")
        gpio = GpioController()

    def start_working(self):
        try:
            print('Doing PickAndPlace')
            gpio.init_pins()
            gpio.gpio_control('elbow_f', 1.1)
            time.sleep(0.5)
            gpio.gpio_control('elbow_b', 1.35)
            time.sleep(0.5)
            print('PickAndPlace finished')
            return
        except (ConnectionResetError, OSError) as e:
            print(e)
