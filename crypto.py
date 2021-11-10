from cryptography.fernet import Fernet
import os
import requests
import json
import csv

apiKey = "ZWU1OTkwZTQtNWQwOS00OGY4LThlOTMtNTdhYTYwMjNmOThkOmFiaElWVFhxT1VKel93TnJoMU1zTUIwRWZhUC1Rc3poSXVjNzJUcVlhT1hTaFE4cGw0VnJ6M3NHR24yWW4tNDdXZEZvRnBYS0xvMnl6RXIzQ0hEQnh3"
API_ENDPOINT = "https://sdkms.fortanix.com"
key_id = "aed7fd1d-8358-48dd-b450-8393d6b46d08"
key = Fernet.generate_key()
 
 
def app_login():
    path = API_ENDPOINT + "/sys/v1/session/auth"
    response = requests.post(path, headers={'Authorization': 'Basic %s' %  apiKey})
    json_resp = json.loads(response.text)
    return json_resp['access_token']

def get_key():
    token = app_login()
    path = API_ENDPOINT + "/crypto/v1/keys/"+ key_id + "/export"
    response = requests.get(path, headers={'Authorization': 'Basic %s' %  apiKey})
    json_resp = json.loads(response.text)
    return(json_resp['value'])

def encrypt(file_path):
    key = get_key()
    print("Key is..." + key)
    fernet = Fernet(key)
    fd = open(file_path)
    plainText = fd.read()
    fd.close()

    #Encrypt data
    encMessage = fernet.encrypt(plainText.encode())

    print("Encryption done ...")

    fd = open(file_path + ".enc", "wb")
    fd.write(encMessage)
    fd.close()

def decrypt(file_path):
    key = get_key()
    print("Key is..." + key)
    fernet = Fernet(key)
    fd = open(file_path,"rb")
    encMessage = fd.read()
    fd.close()
    
    print("The len of encMessage is" + str(len(encMessage)))
    #Decrypt data
    plainText = fernet.decrypt(encMessage).decode()
    print("Decryption done ...")

    fd = open("/data/CC.csv.enc.dec","w")
    fd.write(plainText)
    fd.close()

if __name__ == "__main__":
    print("Running...")
    # encrypt("data/CC.csv")
    #decrypt("data/CC.csv.enc")
