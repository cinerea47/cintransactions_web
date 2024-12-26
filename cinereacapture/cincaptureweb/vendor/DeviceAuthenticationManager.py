import hashlib
import random

from vendor.models import MDevice



class DeviceAuthenticationManager:
    def __init__(self):
        self.HASH_SALT_DEVICE = "jlfef344TTdqcx64364ehkjhskB9075DKSHFH4E5F7549SDKJ34ILWKJ382WEJKI8WEJ9H8532"

    def generate_secret_hash_code(self, pin_code):
        dk = hashlib.pbkdf2_hmac('sha256', pin_code.encode(), self.HASH_SALT_DEVICE.encode(), 100000)
        dk.hex()
        secret_code_hash = dk.hex()
        print("Pin Request Hash", pin_code)
        return secret_code_hash

    def generate_pin_hash(self):
        mPin_code = str(random.randint(23233, 99999))
        secret_hash = self.generate_secret_hash_code(mPin_code)
        return {"hash": secret_hash, "pin": mPin_code}

    def verify_activation_code(self, device, activation_code):
        pin = str(activation_code)
        dk = hashlib.pbkdf2_hmac('sha256', pin.encode(), self.HASH_SALT_DEVICE.encode(), 100000)
        request_hash = dk.hex()
        print("Verified Code", activation_code)
        print("Verified Code", request_hash)
        # print("stored Hash", device_run.activation_request_pin)
        if device.hash_code == request_hash:
            print("true verified secret hash")
            return True
        print("failed secret verification")
        return False

