import threading
from streamdeck import DeviceManager
from PIL import Image, ImageDraw, ImageFont

class StreamDeckInterface:
    def __init__(self):
        self.deck = DeviceManager().enumerate()[0] if DeviceManager().enumerate() else None
        if self.deck:
            self.deck.open()
            self.deck.set_brightness(50)
            self.deck.reset()
            self.prepare_buttons()

            # Button action mappings
            self.button_actions = {
                0: self.action1,
                1: self.action2
                # More button mappings
            }

            # Register button press callback
            self.deck.set_key_callback(self.key_pressed)

    def prepare_buttons(self):
        for key in range(self.deck.key_count()):
            self.set_button_image(key, f"Button {key}")

    def set_button_image(self, key, text):
        image = Image.new("RGB", self.deck.key_image_format(), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.text((5, 5), text, fill=(255, 255, 255), font=font)
        self.deck.set_key_image(key, image)

    def key_pressed(self, deck, key, state):
        if state:
            action = self.button_actions.get(key)
            if action:
                threading.Thread(target=action).start()

    def action1(self):
        print("Action 1 triggered")

    def action2(self):
        print("Action 2 triggered")

    def close(self):
        if self.deck:
            self.deck.reset()
            self.deck.close()

# Example usage
if __name__ == '__main__':
    sd_interface = StreamDeckInterface()
    try:
        input("Press Enter to exit at any time.\n")
    finally:
        sd_interface.close()
