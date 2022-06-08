#!/bin/python3
import UniquePrimes

while __name__ == "__main__":
	my_input = set()
	print("\"0\" for exit\n")
	while True:
		try:
			temp = int(input(f"Enter UniquePrime[{len(my_input)}]: "))
			if temp == 0:
				break
			if UniquePrimes.isUniquePrime(temp):
				my_input |= {temp}
			else:
				print(f"{temp} isn't UniquePrime")
		except Exception as err:
			print("There seems to be error!", err)
	
	print(str(sorted(list(my_input))).replace("[", "{").replace("]", "}"))
	
	encrypted = UniquePrimes.encrypt(my_input)
	print(encrypted)
	my_output = UniquePrimes.decrypt(encrypted)
			
	print(str(sorted(list(my_output))).replace("[", "{").replace("]", "}"))

	again = None
	while again not in [False, True]:
		again = input("Again? ").upper() 
		if again in ["0", "NO", "FALSE", "☐", "❎"]:
			again = False
		elif again in ["1", "YES", "TRUE", "☑", "✅"]:
			again = True
		else:
			again = None
			print("Invalid input, please pick binary digit!")
	
	if not again:
		break
