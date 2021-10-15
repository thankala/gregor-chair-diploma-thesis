import time
from gpio.gpio_controller import GpioController

class PickAndInsert:
    def __init__(self):
        print("\n \n PickAndInsert Service started \n \n")
        gpio = GpioController()

    def start_working(self):
        try:
            print('PickAndInsert Started')
            gpio.init_pins()
            gpio.gpio_control('wrist_f', 1.1)
            time.sleep(0.5)
            gpio.gpio_control('wrist_b', 1.105)
            time.sleep(0.5)
            print('PickAndInsert Finished')
            return 'ok'
        except (ConnectionResetError, OSError) as e:
            return e
