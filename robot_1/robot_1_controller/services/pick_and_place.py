import time
#from main import device


class PickAndPlace:
    def __init__(self):
        print("\n \n PickAndPlace has just started \n \n")

    def start_working(self, device):
        try:
            print('Doing PickAndPlace')
            from gpio.gpio_controller import GpioController
            gpio = GpioController()
            gpio.init_pins()
            gpio.gpio_control('elbow_f', 1.1)
            time.sleep(0.5)
            gpio.gpio_control('elbow_b', 1.35)
            time.sleep(0.5)
            print('PickAndPlace finished')
            return response
        except (ConnectionResetError, OSError) as e:
            print(e)
