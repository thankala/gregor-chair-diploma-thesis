import time
from gpio.gpio_controller import GpioController

class PickAndFlipAndPress:
    def __init__(self):
        print("\n \n pick_and_flip_and_press service has just started \n \n")
        gpio = GpioController()

    def start_working(self):
        try:
            print('PickAndFlipAndPress Started')
            gpio.init_pins()
            gpio.gpio_control('grip_f', 0.7)
            gpio.gpio_control('grip_b', 0.7)
            time.sleep(0.5)
            gpio.gpio_control('grip_f', 0.7)
            gpio.gpio_control('grip_b', 0.7)
            time.sleep(0.5)        
            print('PickAndFlipAndPress Finished')
            return
        except (ConnectionResetError, OSError) as e:
            print(e)
