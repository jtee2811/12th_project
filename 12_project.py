# importing everything from the tkinter module
from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.font import Font
#importing the csv module
import csv

# initializing tkinter module as root 
root = Tk()
root.title('')

# code to place the gui in the middle of the screen
app_width = 310
app_height = 130

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

a = (screen_width / 2) - (app_width / 2)
b = (screen_height / 2) - (app_height / 2)
 
# initializing the co ordinates of our window
root.geometry(f'{app_width}x{app_height}+{int(a)}+{int(b)}')

# globalizing the variable'
global enter_customer_details
def enter_customer_details():
	# creating a new window in our program
	new_window = Toplevel()
	new_window.title('Enter Records')

	app_width4 = 250
	app_height4 = 250

	screen_width4 = root.winfo_screenwidth()
	screen_height4 = root.winfo_screenheight()

	g = (screen_width4 / 2) - (app_width4 / 2)
	h = (screen_height4 / 2) - (app_height4 / 2)
 
	new_window.geometry(f'{app_width4}x{app_height4}+{int(g)}+{int(h)}')

	def add_records():
		# using .get() to fetch the input from the entry box
		serial_no = serial_entry.get()
		customer_name = customer_name_entry.get()
		check_in_date = check_in_date_entry.get()
		phone_no = phone_number_entry.get()
		room_no = room_number_entry.get()
		check_out_date = check_out_date_entry.get()

		# checking if all the values were filled or not
		if (serial_no == '' or customer_name == '' or check_in_date == '' or phone_no == '' or room_no == '' or 
		check_out_date == '') :
			# shows an error the the user in a messagebox
			messagebox.showerror('Error', 'Please fill all details to enter records!')
			serial.set('')
			name2.set('')
			in_date.set('')
			number.set('')
			room_no2.set('')
			out_date.set('')

		elif (len(phone_no) != 10):
			messagebox.showerror('Error', 'The phone number length is faulty!')
			# .set() resets the values in the entry boxes
			serial.set('')
			name2.set('')
			in_date.set('')
			number.set('')
			room_no2.set('')
			out_date.set('')

		else:
			submission = messagebox.askquestion('Submit', 'You are about to enter the following data\n' + 'Mr./Ms. ' + 
			customer_name + '\n' + check_in_date + '\n' + '+91'+phone_no + '\n' + room_no + '\n' + check_out_date)

			if (submission == 'yes'):
				# opening a csv file to append records to it
				with open('hotel.csv', 'a', newline='') as csvfile:
					f = csv.writer(csvfile, delimiter=',')
					# writing a row in the csv file
					f.writerow([serial_no, customer_name, check_in_date, phone_no, room_no, check_out_date])

				serial.set('')
				name2.set('')
				in_date.set('')
				number.set('')
				room_no2.set('')
				out_date.set('')
				messagebox.showinfo('Info', 'Records were added!')

			else:
				messagebox.showinfo('Info', 'Records were not added!')
				serial.set('')
				name2.set('')
				in_date.set('')
				number.set('')
				room_no2.set('')
				out_date.set('')

	# creating a label widget
	main_label = Label(new_window, text='New Customer Details', font=('Joker', 10))
	# specifying the widget position in the gui
	main_label.grid(row=0,column=0)

	serial_no_label = Label(new_window, text='Customer no.')
	# sticky is used to place the text in the middle of the row and pady acts as y-axis placing from that place
	serial_no_label.grid(row=1, column=0, sticky='', pady=5)

	serial = StringVar()
	# to use .set() we need set the variable type as StringVar()
	serial_entry = Entry(new_window, textvariable=serial, width=15)
	serial_entry.grid(row=1, column=1, sticky='', pady=5)

	customer_name_label = Label(new_window, text='Customer Name')
	customer_name_label.grid(row=2, column=0, sticky='', pady=5)

	name2 = StringVar()
	customer_name_entry = Entry(new_window, textvariable=name2, width=15)
	customer_name_entry.grid(row=2, column=1, sticky='', pady=5)

	check_in_date_label = Label(new_window, text='Check-in Date')
	check_in_date_label.grid(row=3, column=0, sticky='', pady=5)

	in_date = StringVar()
	check_in_date_entry = Entry(new_window, textvariable=in_date, width=15)
	# pre-inserting a text in the entry
	check_in_date_entry.insert(0, 'dd/mm/yyyy')
	check_in_date_entry.grid(row=3, column=1, sticky='', pady=5)

	phone_number_label = Label(new_window, text='Phone Number')
	phone_number_label.grid(row=4, column=0, sticky='', pady=5)

	number = StringVar()
	phone_number_entry = Entry(new_window, textvariable=number, width=15)
	phone_number_entry.grid(row=4, column=1, sticky='', pady=5)

	room_number_label = Label(new_window, text='Room Alloted')
	room_number_label.grid(row=5, column=0, sticky='', pady=5)

	room_no2 = StringVar()
	room_number_entry = Entry(new_window, textvariable=room_no2, width=15)
	room_number_entry.grid(row=5, column=1, sticky='', pady=5)

	check_out_date_label = Label(new_window, text='Check-out Date')
	check_out_date_label.grid(row=6, column=0, sticky='', pady=5)

	out_date = StringVar()
	check_out_date_entry = Entry(new_window, textvariable=out_date, width=15)
	check_out_date_entry.insert(0, 'dd/mm/yyyy')
	check_out_date_entry.grid(row=6, column=1, sticky='', pady=5)

	# creating a button widget
	my_button = Button(new_window, text='Add Records', command=add_records)
	my_button.grid(row=7, column=0, sticky='', pady=5)

global show_customer_details
def show_customer_details():
	new_window = Toplevel()
	new_window.title('Show Records')

	app_width3 = 300
	app_height3 = 350

	screen_width3 = root.winfo_screenwidth()
	screen_height3 = root.winfo_screenheight()

	c = (screen_width3 / 2) - (app_width3 / 2)
	d = (screen_height3 / 2) - (app_height3 / 2)
 
	new_window.geometry(f'{app_width3}x{app_height3}+{int(c)}+{int(d)}')

	global L
	with open('hotel.csv', 'r', newline = '') as csvfile2:
		# reading the contents of the csv file
		reader2 = csv.reader(csvfile2)
		L = list(reader2)

	serial_nos = []
	for i in list(range(0,len(L))):
		serial_nos.append(L[i][1])

	def records():
		# curselection() returns a tuple containing the line numbers of the selection/s
		index = listbox.curselection()[0]
		# .config() can modify an objects attributes after it's initialisation
		customer_record_no_label2.config(text=L[index][0])
		customer_name_label2.config(text= 'Mr./Ms. ' + L[index][1])
		check_in_date_label2.config(text=L[index][2])
		phone_number_label2.config(text=L[index][3])
		room_number_label2.config(text=L[index][4])
		check_out_date_label2.config(text=L[index][5])

	# creating a frame to place the listbox in it
	my_frame = Frame(new_window)
	# adding a scrollbar to the listbox int the created frame
	my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

	var = StringVar(value=serial_nos)
	# creating a listbox and connecting the scrollbar to it
	listbox = Listbox(my_frame, listvariable=var, yscrollcommand=my_scrollbar.set)

	# configuring the scrollbar so that we can scroll it vertically
	my_scrollbar.config(command=listbox.yview)
	my_scrollbar.pack(side=RIGHT, fill=Y)
	# packing the the contents of the frame and listbox to the screen
	my_frame.pack()
	listbox.pack()

	# creating another frame
	my_frame2 = Frame(new_window)
	my_frame2.pack()

	customer_record_no_label = Label(my_frame2, text='Record No.')
	customer_record_no_label.grid(row=0, column=0)

	customer_name_label = Label(my_frame2, text='Customer Name')
	customer_name_label.grid(row=1, column=0)

	check_in_date_label = Label(my_frame2, text='Check-in date')
	check_in_date_label.grid(row=2, column=0)

	phone_number_label = Label(my_frame2, text='Phone number')
	phone_number_label.grid(row=3, column=0)

	room_number_label = Label(my_frame2, text='Room Alloted')
	room_number_label.grid(row=4, column=0)

	check_out_date_label = Label(my_frame2, text='Check-out date')
	check_out_date_label.grid(row=5, column=0)

	customer_record_no_label2 = Label(my_frame2, text='')
	customer_record_no_label2.grid(row=0, column=1)

	customer_name_label2 = Label(my_frame2, text='')
	customer_name_label2.grid(row=1, column=1)

	check_in_date_label2 = Label(my_frame2, text='')
	check_in_date_label2.grid(row=2, column=1)

	phone_number_label2 = Label(my_frame2, text='')
	phone_number_label2.grid(row=3, column=1)

	room_number_label2 = Label(my_frame2, text='')
	room_number_label2.grid(row=4, column=1)

	check_out_date_label2 = Label(my_frame2, text='')
	check_out_date_label2.grid(row=5, column=1)

	my_button = Button(my_frame2, text='show records', command=records)
	my_button.grid(row=6, column=0)


global search_customer_details
def search_customer_details():
	new_window = Toplevel()
	new_window.title('Search Records')

	app_width5 = 260
	app_height5 = 180

	screen_width5 = root.winfo_screenwidth()
	screen_height5 = root.winfo_screenheight()

	m = (screen_width5 / 2) - (app_width5 / 2)
	n = (screen_height5 / 2) - (app_height5 / 2)
 
	new_window.geometry(f'{app_width5}x{app_height5}+{int(m)}+{int(n)}')

	def search_record():
		record_no = tkinter.simpledialog.askstring('Enter record no.', 'Enter the record no. whose details you want to search')
		
		# initialising a counter
		found = 0
		with open('hotel.csv', 'r', newline='') as csvfile3:
			reader3 = csv.reader(csvfile3)

			for row in reader3:
				if record_no == row[0]:
					found = 1
					messagebox.showinfo('Info', 'Record found!')

					serial_no_label4 = Label(new_window, text=row[0])
					serial_no_label4.grid(row=1, column=1, sticky='')

					customer_name_label4 = Label(new_window, text=row[1])
					customer_name_label4.grid(row=2, column=1, sticky='')

					check_in_date_label4 = Label(new_window, text=row[2])
					check_in_date_label4.grid(row=3, column=1, sticky='')

					phone_number_label4 = Label(new_window, text=row[3])
					phone_number_label4.grid(row=4, column=1, sticky='')

					room_number_label4 = Label(new_window, text=row[4])
					room_number_label4.grid(row=5, column=1, sticky='')

					check_out_date_label4 = Label(new_window, text=row[5])
					check_out_date_label4.grid(row=6, column=1, sticky='')

		if found == 0:
			messagebox.showerror('Error', 'No such record no. was found')


	main_label2 = Label(new_window, text='Search By Customer Record No.')
	main_label2.grid(row=0, column=0)

	serial_no_label3 = Label(new_window, text='Record No.')
	serial_no_label3.grid(row=1, column=0, sticky='')

	customer_name_label3 = Label(new_window, text='Customer Name')
	customer_name_label3.grid(row=2, column=0, sticky='')

	check_in_date_label3 = Label(new_window, text='Check-in date')
	check_in_date_label3.grid(row=3, column=0, sticky='')

	phone_number_label3 = Label(new_window, text='Phone number')
	phone_number_label3.grid(row=4, column=0, sticky='')

	room_number_label3 = Label(new_window, text='Room Alloted')
	room_number_label3.grid(row=5, column=0, sticky='')

	check_out_date_label3 = Label(new_window, text='Check-out date')
	check_out_date_label3.grid(row=6, column=0, sticky='')

	serial_no_label4 = Label(new_window, text='')
	serial_no_label4.grid(row=1, column=1, sticky='')

	customer_name_label4 = Label(new_window, text='')
	customer_name_label4.grid(row=2, column=1, sticky='')

	check_in_date_label4 = Label(new_window, text='')
	check_in_date_label4.grid(row=3, column=1, sticky='')

	phone_number_label4 = Label(new_window, text='')
	phone_number_label4.grid(row=4, column=1, sticky='')

	room_number_label4 = Label(new_window, text='')
	room_number_label4.grid(row=5, column=1, sticky='')

	check_out_date_label4 = Label(new_window, text='')
	check_out_date_label4.grid(row=6, column=1, sticky='')

	my_button = Button(new_window, text='Search Record', command=search_record)
	my_button.grid(row=7, column=0, sticky='')

global update_customer_details
def update_customer_details():
	new_window = Toplevel()
	new_window.title('Update Records')

	app_width7 = 250
	app_height7 = 250

	screen_width7 = root.winfo_screenwidth()
	screen_height7 = root.winfo_screenheight()

	q = (screen_width7 / 2) - (app_width7 / 2)
	w = (screen_height7 / 2) - (app_height7 / 2)
 
	new_window.geometry(f'{app_width7}x{app_height7}+{int(q)}+{int(w)}')

	def update_records():
		index = None
		updated_data = []
		with open('hotel.csv', 'r', encoding="utf-8") as csvfile4:
			reader4 = csv.reader(csvfile4)
			count = 0
			for row in reader4:
				if len(row) > 0:
					if question == row[0]:
						index = count
						hotel_data = []

						value = serial_entry2.get()
						value2 = customer_name_entry2.get()
						value3 = check_in_date_entry2.get()
						value4 = phone_number_entry2.get()
						value5 = room_number_entry2.get()
						value6 = check_out_date_entry2.get()

						if (value == '' or value2 =='' or value3 == '' or value4 == '' or value5 == '' or value6 == ''):
							messagebox.showerror('Error', 'Please fill all details to update records!')
							serial2.set('')
							name3.set('')
							in_date2.set('')
							number2.set('')
							room_no3.set('')
							out_date2.set('')

						elif (len(value4) != 10):
							messagebox.showerror('Error', 'The phone number length is faulty!')
							serial2.set('')
							name3.set('')
							in_date2.set('')
							number2.set('')
							room_no3.set('')
							out_date2.set('')

						else:
							# updating the contents of only the row selected by the user
							hotel_data.append(value)
							hotel_data.append(value2)
							hotel_data.append(value3)
							hotel_data.append(value4)
							hotel_data.append(value5)
							hotel_data.append(value6)

							updated_data.append(hotel_data)

					else:
						# appending the the other rows to a temporary list without any changes
						updated_data.append(row)
					count += 1

		if index is not None:
			if (value == '' or value2 =='' or value3 == '' or value4 == '' or value5 == '' or value6 == ''):
				serial2.set('')
				name3.set('')
				in_date2.set('')
				number2.set('')
				room_no3.set('')
				out_date2.set('')

			elif (len(value4) != 10):
				serial2.set('')
				name3.set('')
				in_date2.set('')
				number2.set('')
				room_no3.set('')
				out_date2.set('')

			else:
				submit = messagebox.askquestion('Submit', 'You are about to update the following data\n' + value + '\n' + 
				'Mr./Ms. ' + value2 + '\n' + value3 + '\n' + '+91' + value4 + '\n' + value5 + '\n' + value6)
				if (submit == 'yes'):
					with open('hotel.csv', 'w', newline='') as csvfile5:
						writer2 = csv.writer(csvfile5)
						# writing the updated data to the file
						writer2.writerows(updated_data)
						messagebox.showinfo('Info', 'Records updated successfully!')
						serial2.set('')
						name3.set('')
						in_date2.set('')
						number2.set('')
						room_no3.set('')
						out_date2.set('')

				else:
					messagebox.showinfo('Info', 'Records not updated!')
					serial2.set('')
					name3.set('')
					in_date2.set('')
					number2.set('')
					room_no3.set('')
					out_date2.set('')

		else:
			messagebox.showinfo('Info', 'Records could not be updated because\n' + 'the searched record no. was not found!')
			serial2.set('')
			name3.set('')
			in_date2.set('')
			number2.set('')
			room_no3.set('')
			out_date2.set('')

	question = tkinter.simpledialog.askstring('Enter record no.', 'Please enter the record no. whose records you wish to update')
	with open('hotel.csv', 'r', encoding="utf-8") as csvfile6:
		reader5 = csv.reader(csvfile6)
		for row in reader5:
			if len(row) > 0:
				if (question == row[0]):
					messagebox.showinfo('Info', 'Record found!')


	main_label3 = Label(new_window, text='Update Customer Details')
	main_label3.grid(row=0, column=0, pady=5)

	serial_no_label5 = Label(new_window, text='New Rec No.')
	serial_no_label5.grid(row=1, column=0, pady=5, sticky='')

	serial2 = StringVar()
	serial_entry2 = Entry(new_window, width=15, textvariable=serial2)
	serial_entry2.grid(row=1, column=1, pady=5, sticky='')

	customer_name_label5 = Label(new_window, text='New Customer Name')
	customer_name_label5.grid(row=2, column=0, pady=5, sticky='')

	name3 = StringVar()
	customer_name_entry2 = Entry(new_window, width=15, textvariable=name3)
	customer_name_entry2.grid(row=2, column=1, pady=5, sticky='')

	check_in_date_label5 = Label(new_window, text='New Check-in Date')
	check_in_date_label5.grid(row=3, column=0, pady=5, sticky='')

	in_date2 = StringVar()
	check_in_date_entry2 = Entry(new_window, width=15, textvariable=in_date2)
	check_in_date_entry2.insert(0, 'dd/mm/yyyy')
	check_in_date_entry2.grid(row=3, column=1, pady=5, sticky='')

	phone_number_label5 = Label(new_window, text='New Phone No.')
	phone_number_label5.grid(row=4, column=0, pady=5, sticky='')

	number2 = StringVar()
	phone_number_entry2 = Entry(new_window, width=15, textvariable=number2)
	phone_number_entry2.grid(row=4, column=1, pady=5, sticky='')

	room_number_label5 = Label(new_window, text='New Room Alloted')
	room_number_label5.grid(row=5, column=0, pady=5, sticky='')

	room_no3 = StringVar()
	room_number_entry2 = Entry(new_window, width=15, textvariable=room_no3)
	room_number_entry2.grid(row=5, column=1, pady=5, sticky='')

	check_out_date_label5 = Label(new_window, text='New Check-out Date')
	check_out_date_label5.grid(row=6, column=0, pady=5, sticky='')

	out_date2 = StringVar()
	check_out_date_entry2 = Entry(new_window, width=15, textvariable=out_date2)
	check_out_date_entry2.insert(0, 'dd/mm/yyyy')
	check_out_date_entry2.grid(row=6, column=1, pady=5, sticky='')

	run_button = Button(new_window, text='Update Records', command=update_records)
	run_button.grid(row=7, column=0, pady=5, sticky='')

global delete_customer_details
def delete_customer_details():
	del_no = tkinter.simpledialog.askstring('Enter record no.', 'Please enter the record no. whose records you wish to delete')
	hotel_found = False
	updated_data2 = []
	with open('hotel.csv', 'r', encoding="utf-8") as csvfile7:
		reader6 = csv.reader(csvfile7)
		count2 = 0
		for row in reader6:
			if len(row) > 0:
				if del_no != row[0]:
					# appending every record except the one to be deleted to the temporary list
					updated_data2.append(row)
					count2 += 1

				else:
					hotel_found = True

	if hotel_found is True:
		with open('hotel.csv', 'w', newline='', encoding="utf-8") as csvfile8:
			writer3 = csv.writer(csvfile8)
			writer3.writerows(updated_data2)
		messagebox.showinfo('Info', 'Record deleted successfully!')

	else:
		messagebox.showinfo('Info', 'No such record found!')

global customer_bill
def customer_bill():
	new_window = Toplevel()
	new_window.title('Bill')

	app_width8 = 265
	app_height8 = 584

	screen_width8 = root.winfo_screenwidth()
	screen_height8 = root.winfo_screenheight()

	e = (screen_width8 / 2) - (app_width8 / 2)
	u = (screen_height8 / 2) - (app_height8 / 2)
 
	new_window.geometry(f'{app_width8}x{app_height8}+{int(e)}+{int(u)}')

	global font
	# initializing a separate font type for headers
	font = Font(family='Helvetica', size=15, weight='bold', slant='roman')

	def print_bill():
		new_window = Toplevel()
		new_window.title('Bill')

		app_width6 = 800
		app_height6 = 500

		screen_width6 = root.winfo_screenwidth()
		screen_height6 = root.winfo_screenheight()

		ab = (screen_width6 / 2) - (app_width6 / 2)
		cd = (screen_height6 / 2) - (app_height6 / 2)
 
		new_window.geometry(f'{app_width6}x{app_height6}+{int(ab)}+{int(cd)}')

		total_bill = 0

		header_label2 = Label(new_window, text='Bill', font=font)
		header_label2.grid(row=0, column=0, sticky='w')

		hotel_name2 = Label(new_window, text='hotel Amnesia')
		hotel_name2.grid(row=1, column=0, sticky='w')

		hotel_add2 = Label(new_window, text='A-2 block,Paschim Vihar,New Delhi-110063')
		hotel_add2.grid(row=2, column=0, sticky='w')

		hotel_phone2 = Label(new_window, text='+911234567890')
		hotel_phone2.grid(row=3, column=0, sticky='w')

		hotel_mail2 = Label(new_window, text='hotelamnesia@gmail.com')
		hotel_mail2.grid(row=5, column=0, sticky='w')

		blank_label4 = Label(new_window, text='')
		blank_label4.grid(row=6, column=0)

		name_label = Label(new_window, text='Name')
		name_label.grid(row=7, column=0, sticky='')

		room_label = Label(new_window, text='Room no.')
		room_label.grid(row=7, column=1, sticky='')

		check_in_label = Label(new_window, text='Check-in')
		check_in_label.grid(row=7, column=2, sticky='', padx=10)

		check_out_label = Label(new_window, text='Check-out')
		check_out_label.grid(row=7, column=3, sticky='', padx=10)

		nights_spent_label = Label(new_window, text='Nights spent')
		nights_spent_label.grid(row=7, column=4, sticky='', padx=10)

		cost_per_night_label = Label(new_window, text='Cost/night')
		cost_per_night_label.grid(row=7, column=5, sticky='', padx=10)

		additional_services_label = Label(new_window, text='Additional\n'+'services')
		additional_services_label.grid(row=7, column=6, sticky='', padx=10)

		total_label = Label(new_window, text='Line total')
		total_label.grid(row=7, column=7, sticky='', padx=10)

		blank_label5 = Label(new_window, text='')
		blank_label5.grid(row=8, column=0)

		name_label2 = Label(new_window, text=f'Mr./Ms. {name}')
		name_label2.grid(row=9, column=0, sticky='')

		room_label2 = Label(new_window, text=room_no4)
		room_label2.grid(row=9, column=1, sticky='')

		check_in_label2 = Label(new_window, text=check_in)
		check_in_label2.grid(row=9, column=2, sticky='', padx=10)

		check_out_label2 = Label(new_window, text=check_out)
		check_out_label2.grid(row=9, column=3, sticky='', padx=10)

		nights_spent_label2 = Label(new_window, text=nights_spent_entry.get())
		nights_spent_label2.grid(row=9, column=4, sticky='', padx=10)

		nights_spent2 = (int(nights_spent_entry.get()))*1000
		cost_per_night_label2 = Label(new_window, text=nights_spent2)
		cost_per_night_label2.grid(row=9, column=5, sticky='', padx=10)
		total_bill += nights_spent2

		blank_label6 = Label(new_window, text='-')
		blank_label6.grid(row=9, column=6, sticky='', padx=10)

		line_total_label = Label(new_window, text=nights_spent2)
		line_total_label.grid(row=9, column=7, sticky='', padx=10)

		breakfast_label = Label(new_window, text='Breakfast')
		breakfast_label.grid(row=10, column=6, sticky='', padx=10)

		if checkbox.get() == 0:
			breakfast_label2 = Label(new_window, text='-')
			breakfast_label2.grid(row=10, column=7, sticky='', padx=10)

		else:
			breakfast_label2 = Label(new_window, text='300')
			breakfast_label2.grid(row=10, column=7, sticky='', padx=10)
			total_bill += 300

		lunch_label = Label(new_window, text='Lunch')
		lunch_label.grid(row=11, column=6, sticky='', padx=10)

		if checkbox2.get() == 0:
			lunch_label2 = Label(new_window, text='-')
			lunch_label2.grid(row=11, column=7, sticky='', padx=10)

		else:
			lunch_label2 = Label(new_window, text='300')
			lunch_label2.grid(row=11, column=7, sticky='', padx=10)
			total_bill += 300

		dinner_label = Label(new_window, text='Dinner')
		dinner_label.grid(row=12, column=6, sticky='', padx=10)

		if checkbox3.get() == 0:
			dinner_label2 = Label(new_window, text='-')
			dinner_label2.grid(row=12, column=7, sticky='', padx=10)

		else:
			dinner_label2 = Label(new_window, text='300')
			dinner_label2.grid(row=12, column=7, sticky='', padx=10)
			total_bill += 300

		pool_label = Label(new_window, text='Pool')
		pool_label.grid(row=13, column=6, sticky='', padx=10)

		if checkbox4.get() == 0:
			pool_label2 = Label(new_window, text='-')
			pool_label2.grid(row=13, column=7, sticky='', padx=10)

		else:
			pool_label2 = Label(new_window, text='500')
			pool_label2.grid(row=13, column=7, sticky='', padx=10)
			total_bill += 500

		bar_label = Label(new_window, text='Bar')
		bar_label.grid(row=14, column=6, sticky='', padx=10)

		if checkbox5.get() == 0:
			bar_label2 = Label(new_window, text='-')
			bar_label2.grid(row=14, column=7, sticky='', padx=10)

		else:
			bar_label2 = Label(new_window, text='1000')
			bar_label2.grid(row=14, column=7, sticky='', padx=10)
			total_bill += 1000

		laundry_label = Label(new_window, text='Laundry')
		laundry_label.grid(row=15, column=6, sticky='', padx=10)

		if checkbox6.get() == 0:
			laundry_label2 = Label(new_window, text='-')
			laundry_label2.grid(row=15, column=7, sticky='', padx=10)

		else:
			laundry_label2 = Label(new_window, text='300')
			laundry_label2.grid(row=15, column=7, sticky='', padx=10)
			total_bill += 300

		blank_label7 = Label(new_window, text='')
		blank_label7.grid(row=16, column=0)

		blank_label8 = Label(new_window, text='')
		blank_label8.grid(row=17, column=0)

		blank_label9 = Label(new_window, text='')
		blank_label9.grid(row=18, column=0)

		if checkbox8.get() == 1:
			total_bill = total_bill - (total_bill*5)/100

		else:
			total_bill = total_bill

		if checkbox9.get() == 1:
			total_bill = total_bill - (total_bill*7)/100

		else:
			total_bill = total_bill

		subtotal_label = Label(new_window, text='Subtotal')
		subtotal_label.grid(row=19, column=6, sticky='', padx=10)

		subtotal_label2 = Label(new_window, text=total_bill)
		subtotal_label2.grid(row=19, column=7, sticky='', padx=10)

		tax = (total_bill*15)/100
		tax_label = Label(new_window, text='Tax')
		tax_label.grid(row=20, column=6, sticky='', padx=10)

		tax_label2 = Label(new_window, text=tax)
		tax_label2.grid(row=20, column=7, sticky='', padx=10)

		total_bill2 = tax + total_bill
		total_label2 = Label(new_window, text='Total')
		total_label2.grid(row=21, column=6, sticky='',padx=10)

		total_label3 = Label(new_window, text=total_bill2)
		total_label3.grid(row=21, column=7, sticky='', padx=10)
		
		# resetting the values of the checkboxes 
		checkbox.set(0)
		checkbox2.set(0)
		checkbox3.set(0)
		checkbox4.set(0)
		checkbox5.set(0)
		checkbox6.set(0)
		checkbox7.set(0)
		checkbox7.set(0)
		checkbox8.set(0)
		nights_spent.set('')


	record_no2 = tkinter.simpledialog.askstring('Enter record no.', 'Enter the record no. whose bill you want to print')

	found3 = 0
	with open('hotel.csv', 'r', newline='') as csvfile13:
		reader9 = csv.reader(csvfile13)

		for row2 in reader9:
			if record_no2 == row2[0]:
				found3 = 1
				messagebox.showinfo('Info', 'Record found!')

				name = row2[1]
				check_in = row2[2]
				phone_no2 = row2[3]
				room_no4 = row2[4]
				check_out = row2[5]

				header_label = Label(new_window, text='Bill Form', font=font)
				# setting the label position to left of the specified column
				header_label.grid(row=0, column=0, sticky='w')

				hotel_name = Label(new_window, text='hotel Amnesia')
				hotel_name.grid(row=1, column=0, sticky='w')

				hotel_add = Label(new_window, text='A-2 block,Paschim Vihar,New Delhi-110063')
				hotel_add.grid(row=2, column=0, sticky='w')

				hotel_phone = Label(new_window, text='+911234567890')
				hotel_phone.grid(row=3, column=0, sticky='w')

				hotel_mail = Label(new_window, text='hotelamnesia@gmail.com')
				hotel_mail.grid(row=4, column=0, sticky='w')

				blank_label = Label(new_window, text='')
				blank_label.grid(row=5, column=0)

				bill_to_label = Label(new_window, text='Bill to:', font=font)
				bill_to_label.grid(row=6, column=0, sticky='w')

				customer_name_label6 = Label(new_window, text=f'Cutomer name - Mr./Ms. {row2[1]}')
				customer_name_label6.grid(row=7, column=0, sticky='w')

				customer_phone_no = Label(new_window, text=f'Phone number - {row2[3]}')
				customer_phone_no.grid(row=8, column=0, sticky='w')

				text_label = Label(new_window, text='No. of nights spent')
				text_label.grid(row=9, column=0, sticky='w')

				nights_spent = StringVar()	
				nights_spent_entry = Entry(new_window, width=3, textvariable=nights_spent)
				nights_spent_entry.grid(row=9, column=0, sticky='')

				blank_label2 = Label(new_window, text='')
				blank_label2.grid(row=10, column=0)

				extra_services_label = Label(new_window, text='Additional Services', font=font)
				extra_services_label.grid(row=11, column=0, sticky='w')

				# IntVar() is used here to set the on/off value of the checkbox in form of an integer(0/1) 
				checkbox = IntVar()	
				# creating a checkbox widget
				breakfast_checkbox = Checkbutton(new_window, text='Breakfast', variable=checkbox)
				breakfast_checkbox.grid(row=12, column=0, sticky='w')

				checkbox2 = IntVar()
				lunch_checkbox = Checkbutton(new_window, text='Lunch', variable=checkbox2)
				lunch_checkbox.grid(row=13, column=0, sticky='w')

				checkbox3 = IntVar()
				dinner_checkbox = Checkbutton(new_window, text='Dinner', variable=checkbox3)
				dinner_checkbox.grid(row=14, column=0, sticky='w')

				checkbox4 = IntVar()
				pool_checkbox = Checkbutton(new_window, text='Pool', variable=checkbox4)
				pool_checkbox.grid(row=15, column=0, sticky='w')

				checkbox5 = IntVar()
				bar_checkbox = Checkbutton(new_window, text='Bar', variable=checkbox5)
				bar_checkbox.grid(row=16, column=0, sticky='w')

				checkbox6 = IntVar()
				laundry_checkbox = Checkbutton(new_window, text='Laundry', variable=checkbox6)
				laundry_checkbox.grid(row=17, column=0, sticky='w')

				blank_label3 = Label(new_window, text='')
				blank_label3.grid(row=18, column=0)

				pay_type_label = Label(new_window, text='Mode of payment', font=font)
				pay_type_label.grid(row=19, column=0, sticky='w')

				checkbox7 = IntVar()
				cash_checkbox = Checkbutton(new_window, text='Cash', variable=checkbox7)
				cash_checkbox.grid(row=20, column=0, sticky='w')

				checkbox8 = IntVar()
				card_checkbox = Checkbutton(new_window, text='Card(5%off)', variable=checkbox8)
				card_checkbox.grid(row=21, column=0, sticky='w')

				checkbox9 = IntVar()
				paytm_checkbox = Checkbutton(new_window, text='Paytm(7%off)', variable=checkbox9)
				paytm_checkbox.grid(row=22, column=0, sticky='w')

				Bill_button = Button(new_window, text='Print Bill', command=print_bill)
				Bill_button.grid(row=23, column=0, sticky='')


	if found3 == 0:
		messagebox.showerror('Info', 'No such record was found!')


global reset_password
def reset_password():
	old_password = tkinter.simpledialog.askstring('Enter password', 'Please enter your old password', show='*')
	
	with open('password.csv', 'r', encoding="utf-8") as csvfile12:
		reader8 = csv.reader(csvfile12)
		list3 = list(reader8)

	if (list3[0][0] == old_password):
		# we can show any type of special character or symbol instead of the entered text with show 
		new_password = tkinter.simpledialog.askstring('Enter password', 'Please enter your new password', show='*')
		confirm_password3 = tkinter.simpledialog.askstring('Enter password', 'Please confirm your new password', show='*')
		if (new_password != confirm_password3):
			messagebox.showerror('Error', "Both new passwords don't match!")

		else:
			with open('password.csv', 'w', encoding="utf-8") as csvfile9:
				writer4 = csv.writer(csvfile9)
				writer4.writerow([new_password, confirm_password3])
				messagebox.showinfo('Info', 'Password successfully changed!')

	else:
		messagebox.showerror('Error', "The old password isn't correct!")


def enter_program():
	password = entry_box.get()
	confirm_password2 = tkinter.simpledialog.askstring('Enter password', 'Please enter your password one more time', show='*')
	if (password != confirm_password2):
		messagebox.showerror('Error', "Both passwords don't match!")
		root.quit()

	found2 = 0
	with open('password.csv', 'r', encoding="utf-8") as csvfile10:
		reader7 = csv.reader(csvfile10)
		list2 = list(reader7)

		if (list2 == []):
			found2 = 0

		elif (list2[0] == [] or list2[0][0] == ''):
			found2 = 0

		else:
			found2 = 1

	if found2 == 1:
		if (password == list2[0][0]):
			new_window = Toplevel()
			new_window.title('Main Window')
			
			app_width2 = 250
			app_height2 = 290

			screen_width2 = root.winfo_screenwidth()
			screen_height2 = root.winfo_screenheight()

			x = (screen_width2 / 2) - (app_width2 / 2)
			y = (screen_height2 / 2) - (app_height2 / 2)

			new_window.geometry(f'{app_width2}x{app_height2}+{int(x)}+{int(y)}')

			my_button3 = Button(new_window, text='Enter Customer Details', command=enter_customer_details, width=23, font=3)
			my_button3.pack(pady=2)

			my_button4 = Button(new_window, text='Show Customer Details', command=show_customer_details, width=23, font=3)
			my_button4.pack(pady=2)

			my_button5 = Button(new_window, text='Search Customer Details', command=search_customer_details, width=23, font=3)
			my_button5.pack(pady=2)

			my_button6 = Button(new_window, text='Update Customer Details', command=update_customer_details, width=23, font=3)
			my_button6.pack(pady=2)

			my_button7 = Button(new_window, text='Delete Customer Details', command=delete_customer_details, width=23, font=3)
			my_button7.pack(pady=2)

			my_button10 = Button(new_window, text='Bill', command=customer_bill, width=23, font=3)
			my_button10.pack(pady=2)

			my_button8 = Button(new_window, text='Reset Password', command=reset_password, width=23, font=3)
			my_button8.pack(pady=2)

			my_button9 = Button(new_window, text='Close Window', command=new_window.destroy, width=23, font=3)
			my_button9.pack(pady=2)

			# deletes the contents of the entry box from index value 0 till the end
			entry_box.delete(0,'end')

		else:
			messagebox.showerror('Error', 'The password you entered was not correct. Please try again')
			entry_box.delete(0,'end')

	else:
		with open('password.csv', 'w', encoding="utf-8") as csvfile11:
			writer5 = csv.writer(csvfile11)
			writer5.writerow([password, confirm_password2])
			messagebox.showinfo('Info', 'Password has been set!')
			# automatically exits from the root window
			root.quit()


global my_label
my_label = Label(root, text='Please enter your password')
my_label.pack()

entry_box = Entry(root, show='*', width=20)
entry_box.pack(padx=10, pady=10)

my_button = Button(root, text='Submit Password', command=enter_program)
my_button.pack(pady=10)

my_button2 = Button(root, text='Exit', command=root.quit)
my_button2.pack()

# this will keep running the program till the user exits the program
root.mainloop()