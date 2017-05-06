# EmmeDomotica RestClient
# Author SamuelFinocchio
# Init date 05/05/2017

import json
import requests

class EmmeDomotica:
    error = Exception("Bad request")

    # Initializes api address
    # Defaults to localhost if address is not specified
    # Defaults to 80 if port is not specified
    def __init__(self, address = "http://127.0.0.1", port = 80):
        self.apiAddress = address + ":" + str(port)

    # Returns an array of list containt all the available devices
    def getDevices(self):
        resp = requests.get(self.apiAddress + "/device/read")
        if(resp.status_code != requests.codes.ok):
            raise self.error
        else:
            return json.loads(resp.text)

    # Returns a single device specified by a mac address
    def getDevice(self, macAddress):
        devicesList = self.getDevices()
        for device in devicesList:
            if(device['mac_address'] == macAddress):
                return device
        raise Exception("Device not found")
    
    # Creates a post request with device parameters creating a device
    def addDevice(self, descrizione, macAddress, status = 0, numberValue = 0, charValue = ""):
        device = {"mac_address": macAddress, "descrizione": descrizione, "status": status, "number_value": numberValue, "char_value": charValue}
        resp = requests.post(self.apiAddress + "/device/create", json = device)
        # Status code <> 200
        if(resp.status_code != requests.codes.ok):
            raise self.error

    # Creates a put request altering the record of every parameter specified
    def updateDevice(self, descrizione, macAddress, status, numberValue, charValue):
        device = {"descrizione": descrizione, "status": status, "number_value": numberValue, "char_value": charValue}
        resp = requests.put(self.apiAddress + "/device/update/" + macAddress, json = device)
        # Status code <> 200
        if(resp.status_code != requests.codes.ok):
            raise self.error
    
    # Creates a delete request deleting the device identified by the mac address specified
    def deleteDevice(self, macAddress): 
        resp = requests.delete(self.apiAddress + "/device/delete/" + macAddress)
        # Status code <> 200
        if(resp.status_code != requests.codes.ok):
            raise self.error