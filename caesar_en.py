#A python application to illustrate Caesar Cipher Technique
def encrypt(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		if (char.isupper()):
			# Encrypt uppercase characters
			result += chr((ord(char) + s-65) % 26 + 65)
		else:
			# Encrypt lowercase characters
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result

def decrypt(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		if (char.isupper()):
			# Decrypt uppercase characters
			result += chr((ord(char) - s-65) % 26 + 65)
		else:
			# Decrypt lowercase characters
			result += chr((ord(char) - s - 97) % 26 + 97)

	return result

while True:
	t=input("Enter e for encrypting a text using Caesar Cipher Encryption\nEnter d for decrypting a text using Caesar Cipher Encryption method\nEnter any other key for exit\n")
	match t:
		case "e":
			text=input("Enter the text for Encrypting: ")
			shift=int(input("Enter the value of shift: "))
			print('After Encryption the text is '+ encrypt(text,shift))
			print('\n')
		case "d":
			text=input("Enter the text for Decrypting: ")
			shift=int(input("Enter the value of shift: "))
			print('After Decryption the text is '+decrypt(text,shift))
			print('\n')
		case _:
			print('Application is aborted.')
			break