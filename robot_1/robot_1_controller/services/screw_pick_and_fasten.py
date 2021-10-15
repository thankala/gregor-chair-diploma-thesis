import time

class ScrewPickAndFasten:
    def __init__(self):
        print("\n \n ScrewPickAndFasten Service started \n \n")

    def start_working(self, device):
        try:
            print('ScrewPickAndFasten Started')
            from gpio.gpio_controller import GpioController
            gpio = GpioController()
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
