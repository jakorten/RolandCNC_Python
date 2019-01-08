from pylibftdi import Driver
import pyftdi.serialext
import time

vendor = ""
product = ""
serial = ""

def getFTDIDevicesFromSystem():
    global vendor
    global product
    global serial
    
    dev_list = []
    for device in Driver().list_devices():
        # list_devices returns bytes rather than strings
        dev_info = map(lambda x: x.decode('latin1'), device)
        # device must always be this triple
        vendor, product, serial = dev_info
        
        if vendor == "FTDI":
            dev_list.append("%s:%s:%s" % (vendor, product, serial))
        return dev_list

def findFTDIDevices():
    devices = getFTDIDevicesFromSystem()
    if devices is None:
        print("No FTDI device found: connect device and try again...\n")
    else:
        if len(devices) == 1:
            device = devices[0]
            print("Found: " + str(device))
            reset_callback()
            setModelToHome()
            return device
        else:
            print("There are more than one FTDI devices. \nMake sure only the board that interfaces with the Roland MDX-15 is connected.")

def reset_callback():
    str_cmd = ';;^IN;!MC0;^PA;!ZO0;;;^IN;!MC0;';
    print("Trying to reset device...")
    device = 'ftdi:///1'
    sendCommand(str_cmd)
    #port = pyftdi.serialext.serial_for_url(device, baudrate=9600, parity='N', rtscts=True)
    time.sleep(10)

def setModelToHome():
    global vendor
    global product
    global serial
    str_cmd = '^DF;!MC1;!PZ0,0;V15.0;Z0,0,0;!MC0;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'
    
    str_cmd = ';;^IN;!MC0;^PA;!ZO0;;;^IN;!MC0;'
    
    # Open a serial port on the second FTDI device interface (IF/2) @ 3Mbaud
    
    #vendor, product, serial = ftdi_device[0]
    # general syntax: protocol://vendor:product[:index|:serial]/interface
    device = 'ftdi://' + vendor + ':' + product + ":" + serial + '/1'
    print("Trying to connect to: " + device)
    device = 'ftdi:///1'
    port = pyftdi.serialext.serial_for_url(device, baudrate=9600, parity='N', rtscts=True)
    #port = pyftdi.serialext.serial_for_url('ftdi://ftdi:2232h/1', baudrate=3000000)
    #tty.usbserial-A700eYoJ

    # Send bytes
    b_command = bytes(str_cmd, 'utf-8')
    port.write(b_command)

def sendCommand(command):
    device = 'ftdi:///1'
    port = pyftdi.serialext.serial_for_url(device, baudrate=9600, parity='N', rtscts=True)
    b_command = bytes(command, 'utf-8')
    port.write(b_command)


if __name__ == '__main__':
    ftdi_device = findFTDIDevices()



