class MobilePhone:
    def __init__(self, network_type="4G", dualsim=False, front_cam="5MP", rear_cam="8MP", ram="2GB", storage="16GB"):
        self.ScreenType = "Touch Screen"
        self.NetworkType = network_type
        self.DualSim = dualsim
        self.FrontCamera = front_cam
        self.RearCamera = rear_cam
        self.RAM = ram
        self.Storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self, number):
        print(f"Receiving call from {number}...")

    def take_a_picture(self, camera="rear"):
        if camera == "front":
            print(f"Taking a picture with front camera ({self.FrontCamera})")
        else:
            print(f"Taking a picture with rear camera ({self.RearCamera})")

class Samsung(MobilePhone):
    def __init__(self, network_type="5G", dualsim=True, front_cam="12MP", rear_cam="64MP", ram="8GB", storage="128GB"):
        super().__init__(network_type, dualsim, front_cam, rear_cam, ram, storage)
        self.Brand = "Samsung"

class Apple(MobilePhone):
    def __init__(self, network_type="5G", dualsim=False, front_cam="12MP", rear_cam="12MP", ram="6GB", storage="128GB"):
        super().__init__(network_type, dualsim, front_cam, rear_cam, ram, storage)
        self.Brand = "Apple"

iphone1 = Apple()
iphone2 = Apple(network_type="4G", dualsim=True, front_cam="10MP", rear_cam="12MP", ram="4GB", storage="64GB")
samsung1 = Samsung()
samsung2 = Samsung(network_type="4G", dualsim=False, front_cam="8MP", rear_cam="32MP", ram="4GB", storage="64GB")

iphone1.make_call("1234567890")
iphone2.take_a_picture("front")
samsung1.receive_call("9876543210")