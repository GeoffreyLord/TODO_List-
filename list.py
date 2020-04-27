#Python 3
#Created By: Geoffrey G. Lord Feb 3 2020
#Daily list MK.2
#LIG
#Last Update: April 27 2020
import time
import sys
import datetime
#Variables____________________________
listEdit = "V"



#Functions___________________________

def loadbar():
	toolbar_width = 40
	sys.stdout.write("[%s]" % (" " * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1))
	for i in range(toolbar_width):
		time.sleep(0.025)
		sys.stdout.write("-")
		sys.stdout.flush()
	sys.stdout.write("\n")
	return

def print_funct_r():
	now = datetime.datetime.today()
	day_list = open("list.txt", 'r')
	print('\n' * 60)
	print("___________________________")
	print("       Todays List")
	print(now)
	print("___________________________")
	print(day_list.read())
	day_list.close()
	return


#Main___________________________________
print('\n' *60)
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" Productivity List System Mk.02")
print("\n")
editOption = input("Would you like to edit your To-Do list? (Y/N) " +  ("\n" *5)) 

if editOption == "Y" or editOption == "y":
	print("\n" *70)
	print("How would you like to edit your list?")
	editOption = input("add, mark, or clear. (A/M/C) "  +  ("\n" *5))
	if  editOption == "A" or editOption == "a":
		editOption = "Y"
		print("\n" * 70)
		while editOption == "Y" or editOption == "y":
			list_file = open("list.txt", "a")
			new_entry = input("Please enter a new item: \n")
			list_file.write("|-|  " + new_entry + "\n")
			editOption = input("Do you have any more items to add? (y/n): ")
	
	elif editOption == "M" or editOption == "m":
		print("\n" *70)
		editOption = "Y"
		while editOption == "Y" or editOption == "y":
			num = 0
			mark_line = ['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12', 'n13', 'n14', 'n15', 'n16', 'n17', 'n18', 'n19', 'n20', 'n21']
			for line in open("list.txt"):
				print(num, line)
				mark_line[num] = line
				num = num + 1
			user_mark = input("Which line would you like to mark? ")
			user_mark = int(user_mark)
			mark_line[user_mark] = "--|DONE|" + mark_line[user_mark]
			list_file = open("list.txt" , "w")
			for x in range(0 ,num):
				print_line = mark_line[x]
				print_line = str(print_line)
				list_file.write(print_line)
				list_file.close
			editOption = input("Do you have any more items to mark? (y/n): ")
			user_mark = "null"
	elif editOption == "C" or editOption == "c":
		list_file = open("list.txt" , "w")
		list_file.write("")
		list_file.close()
	else:
		print("ERROR")
	print("\n" * 70)




#*********************************************



elif editOption == "N" or editOption == "n":
	print("\n"*70)
	print("Opening List")
	loadbar()
	print("                 100%            Action Complete")
	time.sleep(.25)
	print_funct_r()









