encription=input("Enter the sentence you want to encrypt ")
shift=int(input("Enter the shifting number for the code "))

alphabet="abcdefghijklmnopqrstuvwxyz"

encript=""
decode=""

for letter in encription:
	numberLetter=alphabet.index(letter)
	newNumber= numberLetter+shift
	newLetter=alphabet[newNumber]

	encript+=newLetter

print(encript)

for letter in encript:
	numberLetter=alphabet.index(letter)
	newNumber=numberLetter-shift
	newLetter=alphabet[newNumber]

	decode+=newLetter

print(decode)