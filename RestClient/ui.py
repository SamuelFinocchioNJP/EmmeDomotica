from EmmeDomotica import EmmeDomotica

# Initializing connection on localhost
restClient = EmmeDomotica("http://127.0.0.1", 8000)

# User menu
print "EmmeDomotica rest client"
print "1. To get a list of available devices"
print "1.1 To show detail of a specific device"
print "2. To add a device"
print "3. To edit an existing device"
print "4. To delete an existing device"
print "0. To exit EmmeDomotica rest client"

userChoice = "1"

# Loops until usere chooses to quit
while (userChoice != "0"):
    userChoice = str(raw_input("User choice: "))

    # Gets a list of devices
    if(userChoice == "1"):
        print restClient.getDevices()
        continue

    # Focus on a specified device
    if(userChoice == "1.1"):
        macAddress = raw_input("Select device by mac address: ")
        print restClient.getDevice(macAddress)
        continue

    # Adds a device
    if(userChoice == "2"):
        print "Adding a device"
        descrizione = str(raw_input("Description [led, door, bulb] (default led): ") or "led")
        macAddress = str(raw_input("Mac address: "))
        status = int(raw_input("Status [0, 1] (default 0): ") or 0)
        numberValue = int(raw_input("Number value [0..255] (default 0): ") or 0)
        charValue = raw_input("Char value (default empty)") or ""
        restClient.addDevice(descrizione, macAddress, status, numberValue, charValue)
        continue

    # Edits an existing device
    if(userChoice == "3"):
        print "Altering a device"
        macAddress = raw_input("Select device by mac address: ")
        print "New values for the selected device"
        descrizione = str(raw_input("Description [led, door, bulb] (default led): ") or "led")
        status = int(raw_input("Status [0, 1] (default 0): " or 0))
        numberValue = int(raw_input("Number value [0..255] (default 0): " or 0))
        charValue = raw_input("Char value (default empty)" or "")
        restClient.updateDevice(descrizione, macAddress, status, numberValue, charValue)
        continue

    # Deletes a device
    if(userChoice == "4"):
        print "Deleting a device"
        macAddress = raw_input("Select device by mac address: ")
        restClient.deleteDevice(macAddress)
        continue