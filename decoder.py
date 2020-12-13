import base64
# github.com/onurilyastokay
# onurilyastokay.com.tr
def menu():
    print("""********** DECODE MENU **********
    [1] Base16
    [2] Base32
    [3] Base64
    [4] Base85
    [5] Binary
    [6] Hex
    [9] All
    [0] Quit""")

def decrypt16(value16):
    try:
        decode16 = base64.b16decode(value16)
        dec16 = decode16.decode("UTF-8")
        print("Decoded with Base16: " + dec16)
    except:
        print("Value is not Base16.")

def decrypt32(value32):
    try:
        decode32 = base64.b32decode(value32)
        dec32= decode32.decode("UTF-8")
        print("Decoded with Base32: " + dec32)
    except:
        print("Value is not Base32.")

def decrypt64(value64):
    try:
        decode64 = base64.b64decode(value64)
        dec64 = decode64.decode("UTF-8")
        print("Decoded with Base64: " + dec64)
    except:
        print("Value is not Base64.")

def decrypt85(value85):
    try:
        decode85 = base64.a85decode(value85)
        dec85 = decode85.decode("UTF-8")
        print("Decoded with Base85: " + dec85)
    except:
        print("Value is not Base85.")

def decryptbin(binValue):
    try:
        binValue=binValue.replace(" ","")
        binary_int = int(binValue, 2)
        byte_number = binary_int.bit_length() + 7 // 8
        binary_array = binary_int.to_bytes(byte_number, "big")
        ascii_text = binary_array.decode()
        print("Decoded with Binary: " + ascii_text)
    except:
        print("Value is not Binary.")

def decrypthex(hexValue):
    try:
        decHex = bytes.fromhex(hexValue).decode('utf-8')
        print("Decoded with Hex: " + decHex)
    except:
        print("Value is not Hex.")

choice="null"
menu()
while choice != "0":
    choice=input("Choice: ")
    if choice == "0":
        break;
    value=input("Value: ")
    if choice=="1":
        decrypt16(value)
    elif choice=="2":
        decrypt32(value)
    elif choice=="3":
        decrypt64(value)
    elif choice=="4":
        decrypt85(value)
    elif choice=="5":
        decryptbin(value)
    elif  choice=="6":
        decrypthex(value)
    elif  choice=="9":
        decrypt16(value)
        decrypt32(value)
        decrypt64(value)
        decrypt85(value)
        decryptbin(value)
        decrypthex(value)
    else:
        print("Error: Wrong entry, try again.")