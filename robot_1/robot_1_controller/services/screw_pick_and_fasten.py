import time
from gpio.gpio_controller import GpioController

class ScrewPickAndFasten:
    def __init__(self):
        print("\n \n ScrewPickAndFasten Service started \n \n")
        gpio = GpioController()

    def start_working(self):
        try:
            print('ScrewPickAndFasten Started')
            gpio.init_pins()
            gpio.gpio_control('led', 1)
            time.sleep(0.5)
            gpio.gpio_control('led', 1)
            time.sleep(0.5)
            gpio.gpio_control('led', 1)
            time.sleep(0.5)
            gpio.gpio_control('led', 1)
            time.sleep(0.5)
            print('ScrewPickAndFasten Finished')
            return
        except (ConnectionResetError, OSError) as e:
            print(e)
