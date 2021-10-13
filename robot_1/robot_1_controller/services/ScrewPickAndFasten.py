import time


class ScrewPickAndFasten:
    COMPLETED_MESSAGE = '{"ScrewPickAndFasten": "finished"}'

    def __init__(self):
        print("\n \n ScrewPickAndFasten service started \n \n")

    def start_working(self, device):
        try:
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
            print('ScrewPickAndFasten finished..')
            print('Replying to WT server...')
            encoded_response = self.COMPLETED_MESSAGE
            return encoded_response
        except (ConnectionResetError, OSError) as e:
            print(e)
