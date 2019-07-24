import secrets
import uuid

#random integer number uisng secrets
print("IV     =", secrets.token_hex(8))
print("Key    =", secrets.token_hex(8))
print("SU     = {" + str(uuid.uuid4()) + "}")
print("SYSWD  = {" + str(uuid.uuid4()) + "}")
