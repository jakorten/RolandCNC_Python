from pylibftdi import Driver
import pyftdi.serialext

def getFTDIDevicesFromSystem():
    dev_list = []
    for device in Driver().list_devices():
        # list_devices returns bytes rather than strings
        dev_info = map(lambda x: x.decode('latin1'), device)
        # device must always be this triple
        vendor, product, serial = dev_info
        
        if vendor == "FTDI":
            dev_list.append("%s:%s:%s" % (vendor, product, serial))
        return dev_list

if __name__ == '__main__':
    devices = getFTDIDevicesFromSystem()
    if devices is None:
        print("No FTDI device found: connect device and try again...")
    else:
        if len(devices) == 1:
            for device in devices:
                print("Found: " + str(device))
        else:
            print("There are more than one FTDI devices. \nMake sure only the board that interfaces with the Roland MDX-15 is connected.")

