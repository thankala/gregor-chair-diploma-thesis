import time

class PickAndInsert:
    def __init__(self):
        print("\n \n PickAndInsert Service started \n \n")

    def start_working(self, device):
        try:
            print('PickAndInsert Started')
            from gpio.gpio_controller import GpioController
            gpio = GpioController()
            gpio.init_pins()
            gpio.gpio_control('wrist_f', 1.1)
            time.sleep(0.5)
            gpio.gpio_control('wrist_b', 1.105)
            time.sleep(0.5)
            print('PickAndInsert Finished')
            return
        except (ConnectionResetError, OSError) as e:
            print(e)
