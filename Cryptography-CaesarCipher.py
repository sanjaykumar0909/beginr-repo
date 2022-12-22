alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):

  cryptText = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift
    new_letter = alphabet[new_position]
    cryptText += new_letter
  print(f"The encrypted text is {cryptText}")

def decrypt(cryptText, shift):
  text = ""
  for letter in cryptText:
    position = alphabet.index(letter)
    new_position = position - shift
    text += alphabet[new_position]
  print(f"The decrypted text is {text}")


if direction == "encrypt":
  encrypt(text, shift)
elif direction == "decrypt":
  decrypt(text, shift)
