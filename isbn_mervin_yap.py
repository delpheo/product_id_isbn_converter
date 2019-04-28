# 
# This file is created to convert product IDs to ISBN-10 numbers. The program runs in Python 3
# environment. Created by Mervin Yap, 28th April 2019.
#

#!/usr/bin/env python3



barcode = input("Please key in product ID. \n")			#asks for input for the product ID; this can be in the form of typed ID, or directly from a barcode scanner



def product_id_validator(product_id):
	if len(product_id) != 12:							#checks if the product ID is even valid before running; product IDs should have 12 digits
		print("Invalid product ID")
	else:
		return isbn_conversion(product_id)



def isbn_conversion(product_id_input):
	product_9digit = str(product_id_input)[3:]			#removes first 3 digits from product ID


	def error_key(product_string):						#computes the error key based on ISBN method


		def error_key_check(weighted_sum):				#checks if the error digit is a value of 10; returns x when true, returns 0 when mod 11 is 0
			key1 = 11 - (weighted_sum % 11)
			if key1 == 10:
				return "x"
			elif key1 == 11:
				return "0"
			else:
				return str(key1)


		total_sum = 0									#calculate the weighted sum of the 9 digits
		counter, multiplier = 0, 10
		while counter < len(product_string):
			total_sum += int(product_string[counter]) * multiplier
			multiplier -= 1
			counter += 1
		return error_key_check(total_sum)				#this should return the error key based on mod 11


	isbn_number = product_9digit + error_key(product_9digit)			#combines the initial 9 digits and the computed error key
	print("\nISBN-10:\n" + isbn_number[0] + "-" + isbn_number[1:3] + "-" + isbn_number[3:9] + "-" + isbn_number[9])		#prints the results




product_id_validator(barcode)