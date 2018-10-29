class TocColdException(Exception):

    def __init__(self, temp):
        super().__init__("Temperature {} is below absolute zero !".format(temp))

def celcuis_to_kelvin(temp):
    if temp < -273.15:
        raise TocColdException(temp)
    return temp + 273.15


print(celcuis_to_kelvin(-360))
