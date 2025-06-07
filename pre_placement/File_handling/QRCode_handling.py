from qrcode import QRCode

def read_write(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

text = "Hello Everyone "
r = QRCode()

r.add_data(read_write('pf/demo.txtlass ParkingSystem(object):

    def __init__(self, big, medium, small):

        self.big  = big
        self.medium = medium
        self.small = small

    def addCar(self, carType):
        
        if carType == 1 and self.big > 0:
            self.big -= 1
            return True
        elif carType == 2 and self.medium > 0:
            self.medium -= 1
            return True
        elif carType == 3 and self.small > 0:
            self.small -= 1
            return True
        else:
            return False
        
'))
r.make(fit=True)
img = r.make_image(fill_color="black",back_color="white")
img.save("myqr.png")


