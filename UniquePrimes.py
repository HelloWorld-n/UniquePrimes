#!/bin/python3
from math import sqrt, ceil, floor

def isPrime(num):
	if num == 2 or num == 3: 
		return True
	if num < 2 or num % 2 == 0: 
		return False
	if num < 9: 
		return True
	if num % 3 == 0: 
		return False
	r = int(num ** 0.5)
	f = 5
	while f <= r:
		if num % f == 0: 
			return False
		if num % (f + 2) == 0: 
			return False
		f += 6
	return True 

def isUniquePrime(num):
	num = int(num)
	
	if num <= 1:
		return False
	
	if isPrime(num):
		return True
	
	sroot = sqrt(num)
	if floor(sroot) == ceil(sroot):
		return isUniquePrime(sroot)
	else:
		return False

def encrypt(collection):
	encrypted = 1
	for item in collection:
		encrypted *= item
	return encrypted

def decrypt(encrypted):
	decrypted = set()
	testBase = 2
	while encrypted > 1:
		if encrypted % testBase == 0:
			while True:					
				testPower = 1
				while encrypted % (testBase ** testPower) == 0:
					testPower *= 2
				testPower //= 2
				decrypted |= {testBase ** testPower}
				encrypted //= testBase ** testPower
				if testPower == 0:
					break
		if testBase == 2:
			testBase += 1
		else:
			testBase += 2
	return decrypted - {1}
