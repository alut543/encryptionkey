import time

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("Encryption Key (Ceaser Ciypher) v0.1")
print("\n")

message = input("Enter a message: ").lower()
shift = int(input("Enter a shift: "))
encrypted = ""

for character in message:
    if character in alphabet:
        position = alphabet.index(character)
        new_position = (position + shift) % 26
        encrypted = encrypted + alphabet[new_position]
    else:
        encrypted = encrypted + character

print("Please Wait..")
time.sleep(3)
print("Encrypted Message: ", encrypted)
