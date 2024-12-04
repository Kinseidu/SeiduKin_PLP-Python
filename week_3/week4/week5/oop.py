# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Device Info: {self.brand} {self.model}"


# Smartphone class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery_life):
        super().__init__(brand, model)
        self.storage = storage
        self.battery_life = battery_life

    def make_call(self, number):
        return f"Dialing {number} from {self.brand} {self.model}..."

    def device_info(self):
        # Overriding the parent method to add more details
        base_info = super().device_info()
        return f"{base_info}, Storage: {self.storage}GB, Battery Life: {self.battery_life} hours"


# Example usage
smartphone = Smartphone("Apple", "iPhone 14", 256, 20)
print(smartphone.device_info())
print(smartphone.make_call("123-456-7890"))
