#!/usr/bin/python
# coding: utf-8
import random, string, sys

green='\033[32m'
blue='\033[34m'
bold='\033[01m'
reset='\033[0m'

print green + '''
 ▄▄▄· ▄▄▄· .▄▄ · .▄▄ · ▄▄▌ ▐ ▄▌      ▄▄▄  ·▄▄▄▄   
▐█ ▄█▐█ ▀█ ▐█ ▀. ▐█ ▀. ██· █▌▐█▪     ▀▄ █·██▪ ██ 
 ██▀·▄█▀▀█ ▄▀▀▀█▄▄▀▀▀█▄██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌
▐█▪·•▐█ ▪▐▌▐█▄▪▐█▐█▄▪▐█▐█▌██▐█▌▐█▌.▐▌▐█•█▌██. ██ 
.▀    ▀  ▀  ▀▀▀▀  ▀▀▀▀  ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀▀▀▀▀▀• 
• ▌ ▄ ·. ▄▄▄ .▄▄▄   ▄▄ • ▄▄▄ .▄▄▄  
·██ ▐███▪▀▄.▀·▀▄ █·▐█ ▀ ▪▀▄.▀·▀▄ █·
▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▄ ▄█ ▀█▄▐▀▀▪▄▐▀▀▄ 
██ ██▌▐█▌▐█▄▄▌▐█•█▌▐█▄▪▐█▐█▄▄▌▐█•█▌
▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀·▀▀▀▀  ▀▀▀ .▀  ▀
		By : Mr Kara
		Thanks to : Lion Nufiliq , Omar Alma3lol
''' + reset
fileName = raw_input(bold + blue + "Input the name of the file: " + reset)

def phone_gen(newline):
	digit1 = "091"
	digit2 = "092"
	digit3 = "094"
	final  = []
	for num in range(0, 9999999):
		number1  = str(digit1) + '{0:07}'.format(num)
		number2  = str(digit2) + '{0:07}'.format(num)
		number3  = str(digit3) + '{0:07}'.format(num)
		newnum1  = (newline + str(number1))
		newnum2  = (newline + str(number2))
		newnum3  = (newline + str(number3))
		final.append(newnum1)
		final.append(newnum2)
		final.append(newnum3)
	return final
def file_save(final):
	with open("list.txt", "w") as file:
		for ndx, each in enumerate(final):
			file.write(final[ndx]+"\r\n")
def main():
	final = []
	with open(fileName, "r") as ly:
		for line in ly:
			newline = line.replace("\n", "")
			final.extend(phone_gen(newline))
	return final
if __name__ == '__main__':
	file_save(main())
