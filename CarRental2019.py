
# -- PyQt5 pip install PyQt5

# -- Tkinter pip install tkinter

# -- Kivy   pip install kivy


from tkinter import *

import sqlite3


# create tkinter window

root = Tk()

root.title('Car Rental 2019')

root.geometry("500x500")



car_rental_connect = sqlite3.connect('UpdatedData.db')

car_rental_cur = car_rental_connect.cursor()

def AddCustWindow():
	newWindow = Toplevel(root)
	newWindow.title('Add New Customer')
	newWindow.geometry("400x400")

	CustID = Entry(newWindow, width=30)
	CustID.grid(row=0, column=1, padx=20)

	Name = Entry(newWindow, width=30)
	Name.grid(row=1, column=1)

	Phone = Entry(newWindow, width=30)
	Phone.grid(row=2, column=1)

	CustID_label = Label(newWindow, text='CustID: ')
	CustID_label.grid(row=0, column=0)

	Name_label = Label(newWindow, text='Name: ')
	Name_label.grid(row=1, column=0)

	Phone_label = Label(newWindow, text='Phone: ')
	Phone_label.grid(row=2, column=0)

	def submitCust():
		submit_conn = sqlite3.connect('UpdatedData.db')

		submit_cur = submit_conn.cursor()

		submit_cur.execute("INSERT INTO CUSTOMER (CustID, Name, Phone) VALUES (:CustID, :Name, :Phone) ",
						{
							'CustID': CustID.get(),
							'Name': Name.get(),
							'Phone': Phone.get()
						})

		# commit changes

		submit_conn.commit()
		# close the db connection
		submit_conn.close()

	submit_btn = Button(newWindow, text='Add Customer ', command=submitCust)
	submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=140)


def AddCarWindow():
	newWindow = Toplevel(root)
	newWindow.title('Add New Car')
	newWindow.geometry("400x400")

	VehicleID = Entry(newWindow, width=30)
	VehicleID.grid(row=0, column=1, padx=20)

	Description = Entry(newWindow, width=30)
	Description.grid(row=1, column=1)

	Year = Entry(newWindow, width=30)
	Year.grid(row=2, column=1)

	Type = Entry(newWindow, width=30)
	Type.grid(row=3, column=1)

	Category = Entry(newWindow, width=30)
	Category.grid(row=4, column=1)

	VehicleID_label = Label(newWindow, text='VehicleID: ')
	VehicleID_label.grid(row=0, column=0)

	Description_label = Label(newWindow, text='Description: ')
	Description_label.grid(row=1, column=0)

	Year_label = Label(newWindow, text='Year: ')
	Year_label.grid(row=2, column=0)

	Type_label = Label(newWindow, text='Type: ')
	Type_label.grid(row=3, column=0)

	Category_label = Label(newWindow, text='Category: ')
	Category_label.grid(row=4, column=0)

	def submitCar():
		submit_conn = sqlite3.connect('UpdatedData.db')

		submit_cur = submit_conn.cursor()

		submit_cur.execute("INSERT INTO VEHICLE (VehicleID, Description, Year, Type, Category) "
						   "VALUES (:VehicleID, :Description, :Year, :Type, :Category) ",
						{
							'VehicleID': VehicleID.get(),
							'Description': Description.get(),
							'Year': Year.get(),
							'Type': Type.get(),
							'Category': Category.get()
						})

		# commit changes

		submit_conn.commit()
		# close the db connection
		submit_conn.close()

	submit_btn = Button(newWindow, text='Add Car ', command=submitCar)
	submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

def AddRentalWindow():
	newWindow = Toplevel(root)
	newWindow.title('Add New Rental')
	newWindow.geometry("500x500")

	Type = Entry(newWindow, width=30)
	Type.grid(row=0, column=1, padx=20)

	Category = Entry(newWindow, width=30)
	Category.grid(row=1, column=1)

	Type.insert(0, "1")
	Category.insert(0, "1")

	Type_label = Label(newWindow, text='Type: ')
	Type_label.grid(row=0, column=0)

	Category_label = Label(newWindow, text='Category: ')
	Category_label.grid(row=1, column=0)

	def submitSearch():
		iq_conn = sqlite3.connect('UpdatedData.db')

		iq_cur = iq_conn.cursor()

		iq_cur.execute("SELECT VehicleID, Type, Category, Description, Year "
					   "FROM VEHICLE "
					   "WHERE VEHICLE.VehicleID NOT IN "
					   "(SELECT DISTINCT R.VehicleID "
					   "FROM RENTAL as R, VEHICLE as V "
					   "WHERE V.VehicleID = R.VehicleID AND R.Returned = 0 AND V.Type = :Type AND V.Category = :Category) "
					   "AND VEHICLE.Type = :Type AND VEHICLE.Category = :Category ",
					   {
						   	'Type': Type.get(),
						    'Category': Category.get()
					   })


		output_records = iq_cur.fetchall()

		print_record = ''

		for output_record in output_records:
			print_record += str(output_record[0])+ " " + str(output_record[1])+ " " +str(output_record[2])+ \
							" " + str(output_record[3])+ " " + str(output_record[4])+"\n"

		iq_label = Label(newWindow, text = print_record)

		iq_label.grid(row = 9, column = 0, columnspan = 4)

		#commit changes

		iq_conn.commit()

		#close the db connection
		iq_conn.close()

	search_btn = Button(newWindow, text='Search for cars ', command=submitSearch)
	search_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

	CustID = Entry(newWindow, width=30)
	CustID.grid(row=10, column=1, padx=20)

	VehicleID = Entry(newWindow, width=30)
	VehicleID.grid(row=11, column=1, padx=20)

	StartDate = Entry(newWindow, width=30)
	StartDate.grid(row=12, column=1)

	OrderDate = Entry(newWindow, width=30)
	OrderDate.grid(row=13, column=1)

	RentalType = Entry(newWindow, width=30)
	RentalType.grid(row=14, column=1)

	Qty = Entry(newWindow, width=30)
	Qty.grid(row=15, column=1)

	ReturnDate = Entry(newWindow, width=30)
	ReturnDate.grid(row=16, column=1)

	TotalAmount = Entry(newWindow, width=30)
	TotalAmount.grid(row=17, column=1)

	CustID.insert(0, "eg. 101")
	VehicleID.insert(0, "eg. JM3KE4DY4F0441471")
	StartDate.insert(0, "eg. 4/25/2022")
	OrderDate.insert(0, "eg. 4/25/2022")
	RentalType.insert(0, "eg. 1 or 7")
	Qty.insert(0, "eg. 1-4")
	ReturnDate.insert(0, "Add (Qty*RentalType) to StartDate")
	TotalAmount.insert(0, "eg. Base Price * Qty")


	CustID_label = Label(newWindow, text='CustID: ')
	CustID_label.grid(row=10, column=0)

	VehicleID_label = Label(newWindow, text='VehicleID: ')
	VehicleID_label.grid(row=11, column=0)

	StartDate_label = Label(newWindow, text='StartDate: ')
	StartDate_label.grid(row=12, column=0)

	OrderDate_label = Label(newWindow, text='OrderDate: ')
	OrderDate_label.grid(row=13, column=0)

	RentalType_label = Label(newWindow, text='RentalType: ')
	RentalType_label.grid(row=14, column=0)

	Qty_label = Label(newWindow, text='Quantity: ')
	Qty_label.grid(row=15, column=0)

	ReturnDate_label = Label(newWindow, text='ReturnDate: ')
	ReturnDate_label.grid(row=16, column=0)

	TotalAmount_label = Label(newWindow, text='TotalAmount: ')
	TotalAmount_label.grid(row=17, column=0)

	def submitRental():
		submit_conn = sqlite3.connect('UpdatedData.db')

		submit_cur = submit_conn.cursor()


		submit_cur.execute("INSERT INTO RENTAL "
						   "VALUES (:CustID, :VehicleID, :StartDate, :OrderDate, :RentalType, :Qty, :ReturnDate, :TotalAmount, NULL, 0) ",
						{
							'CustID': CustID.get(),
							'VehicleID': VehicleID.get(),
							'StartDate': StartDate.get(),
							'OrderDate': OrderDate.get(),
							'RentalType': RentalType.get(),
							'Qty': Qty.get(),
							'ReturnDate': ReturnDate.get(),
							'TotalAmount': TotalAmount.get()
						})

		# commit changes

		submit_conn.commit()
		# close the db connection
		submit_conn.close()

	submit_btn = Button(newWindow, text='Submit Rental ', command=submitRental)
	submit_btn.grid(row=18, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

def ReturnRentalWindow(): #REQUIREMENT 4 TO DO
    newWindow = Toplevel(root)
    newWindow.title('Return Rental')
    newWindow.geometry("400x400")

    ReturnDate = Entry(newWindow, width=30)
    ReturnDate.grid(row=0, column=1, padx=20)

    Name = Entry(newWindow, width=30)
    Name.grid(row=1, column=1)

    VehicleID = Entry(newWindow, width=30)
    VehicleID.grid(row=2, column=1)

    Description = Entry(newWindow, width=30)
    Description.grid(row=3, column=1, padx=20)

    Year = Entry(newWindow, width=30)
    Year.grid(row=4, column=1)

    Type = Entry(newWindow, width=30)
    Type.grid(row=5, column=1)

    Category = Entry(newWindow, width=30)
    Category.grid(row=6, column=1)

    CustomerID = Entry(newWindow, width=30)
    CustomerID.grid(row=7, column=1, padx=20)

    ReturnDate_label = Label(newWindow, text='Return Date: ')
    ReturnDate_label.grid(row=0, column=0)

    Name_label = Label(newWindow, text='Name: ')
    Name_label.grid(row=1, column=0)

    VehicleID_label = Label(newWindow, text='VehicleID: ')
    VehicleID_label.grid(row=2, column=0)

    Description_label = Label(newWindow, text='Description: ')
    Description_label.grid(row=3, column=0)

    Year_label = Label(newWindow, text='Year: ')
    Year_label.grid(row=4, column=0)

    Type_label = Label(newWindow, text='Type: ')
    Type_label.grid(row=5, column=0)

    Category_label = Label(newWindow, text='Category: ')
    Category_label.grid(row=6, column=0)

    CustomerID_label = Label(newWindow, text='Category: ')
    CustomerID_label.grid(row=7, column=0)

    def submitSearch():
        iq_conn = sqlite3.connect('UpdatedData.db')

        iq_cur = iq_conn.cursor()

        record_id = ReturnDate.get()

        iq_cur.execute(" SELECT TotalAmount "
                       " FROM RENTAL "
                       " WHERE CustID IN (SELECT CustID "
                       " FROM CUSTOMER "
                       " WHERE Name = :Name) "
                       " AND VehicleID IN (SELECT V.VehicleID "
                       " FROM VEHICLE AS V "
                       " WHERE V.VehicleID = :VehicleID "
                       " AND V.Description = :Description "
                       " AND V.Year = :Year "
                       " AND V.Type = :Type "
                       " AND V.Category = :Category) "
                       " AND ReturnDate = :ReturnDate ",
                       {
                               'ReturnDate': ReturnDate.get(),
                            'Name': Name.get(),
                            'VehicleID': VehicleID.get(),
                            'Description': Description.get(),
                            'Year': Year.get(),
                            'Type': Type.get(),
                            'Category': Category.get()
                       })

        output_records = iq_cur.fetchall()

        print_record = ''

        for output_record in output_records:
            print_record += str(output_record[0])+ " " +"\n"

        iq_label = Label(newWindow, text = print_record)

        iq_label.grid(row = 8, column = 0, columnspan = 2)

        #commit changes

        iq_conn.commit()
        #close the db connection
        iq_conn.close()

    submit_btn = Button(newWindow, text='Show Balance ', command=submitSearch)
    submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

    def submitRental():
        submit_conn = sqlite3.connect('UpdatedData.db')

        submit_cur = submit_conn.cursor()

        submit_cur.execute(" UPDATE RENTAL "
                           " SET Returned = 1 "
                           " WHERE CustID IN (SELECT CustID "
                           " FROM CUSTOMER "
                           " WHERE Name = :Name) "
                           " AND VehicleID IN (SELECT V.VehicleID "
                           " FROM VEHICLE AS V "
                           " WHERE V.VehicleID = :VehicleID "
                           " AND V.Description = :Description "
                           " AND V.Year = :Year "
                           " AND V.Type = :Type "
                           " AND V.Category = :Category) "
                           " AND ReturnDate = :ReturnDate ",
                        {
                            'ReturnDate': ReturnDate.get(),
                            'Name': Name.get(),
                            'VehicleID': VehicleID.get(),
                            'Description': Description.get(),
                            'Year': Year.get(),
                            'Type': Type.get(),
                            'Category': Category.get(),
                            'CustomerID': CustomerID.get(),
                        })

        # commit changes

        submit_conn.commit()
        # close the db connection
        submit_conn.close()

    submit_btn = Button(newWindow, text=' Update Database ', command=submitRental)
    submit_btn.grid(row=20, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

def ViewCustomerInfo():
	newWindow = Toplevel(root)
	newWindow.title('View Customer Info')
	newWindow.geometry("500x300")

	Cust_ID_label = Label(newWindow, text='Customer ID: ')
	Cust_ID_label.grid(row=0, column=0)

	CustName_label = Label(newWindow, text='Customer Name: ')
	CustName_label.grid(row=1, column=0)

	CustID = Entry(newWindow, width=30)
	CustID.grid(row=0, column=1, padx=20)

	CustName = Entry(newWindow, width=30)
	CustName.grid(row=1, column=1)

	def submitSearch():
		# Connecting to database and creating cursor
		iq_conn = sqlite3.connect('UpdatedData.db')
		iq_cur = iq_conn.cursor()
		iq_cur.execute( "SELECT "
						"CustID, "
						"Name, "
						"CASE WHEN PaymentDate IS NOT NULL THEN 0 ELSE TotalAmount END "
						"FROM vRentalInfo "
						"WHERE CustID = :CustomerID OR Name = :CustomerName "
						"ORDER BY TotalAmount ASC;",
						{
							'CustomerName': CustName.get(),
							'CustomerID': CustID.get()
						})

		# Capturing data, iterating over tuple to print each attribute
		output_records = iq_cur.fetchall()
		print_record = ''
		for output_record in output_records:
			print_record += "Customer ID: " + str(output_record[0]) + ", " + "Customer Name: " + str(output_record[1]) + ", " + "Remaining Balance: " + "$" + str(output_record[2]) + ".00" + "\n"

		# Creating label for retrieved data and displaying to window
		iq_label = Label(newWindow, text = print_record)
		iq_label.grid(row=4, column=0, columnspan=2)

		# Defining function that clears the query results so another can be retrieved
		def clear():
			iq_label.destroy()

		# Creating a clear button to get rid of old results, attaching to clear command
		clear_btn = Button(newWindow, text='Clear Results', command=clear)
		clear_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

		#commit changes
		iq_conn.commit()
		#close the db connection
		iq_conn.close()

	# Creating the search button and connecting to submitSearch function
	submit_btn = Button(newWindow, text='Search', command=submitSearch)
	submit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

def VehiclePriceWindow():
	newWindow = Toplevel(root)
	newWindow.title('View Vehicle Info')
	newWindow.geometry("500x300")

	Vehicle_ID_label = Label(newWindow, text='VIN: ')
	Vehicle_ID_label.grid(row=0, column=0)

	Description_label = Label(newWindow, text='Description: ')
	Description_label.grid(row=1, column=0)

	VehicleID = Entry(newWindow, width=30)
	VehicleID.grid(row=0, column=1, padx=20)

	Description = Entry(newWindow, width=30)
	Description.grid(row=1, column=1)

	def submitSearch():
		# Connecting to database and creating cursor
		iq_conn = sqlite3.connect('UpdatedData.db')
		iq_cur = iq_conn.cursor()
		iq_cur.execute( "SELECT DISTINCT "
						"VehicleID, "
						"Description, "
						"TotalAmount/(RentalType*Qty) "
						"FROM vRentalInfo "
						"WHERE VehicleID = :VIN OR Description = :Desc "
						"ORDER BY TotalAmount ASC;",
						{
							'VIN': VehicleID.get(),
							'Desc': Description.get()
						})

		# Capturing data, iterating over tuple to print each attribute
		output_records = iq_cur.fetchall()
		print_record = ''
		for output_record in output_records:
			print_record += "VIN: " + str(output_record[0]) + ", " + "Description: " + str(output_record[1]) + ", " + "Average Daily Price: $" + str(output_record[2]) + ".00" + "\n"

		# Creating label for retrieved data and displaying to window
		iq_label = Label(newWindow, text = print_record)
		iq_label.grid(row=4, column=0, columnspan=2)

		# Defining function that clears the query results so another can be retrieved
		def clear():
			iq_label.destroy()

		# Creating a clear button to get rid of old results, attaching to clear command
		clear_btn = Button(newWindow, text='Clear Results', command=clear)
		clear_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

		#commit changes
		iq_conn.commit()
		#close the db connection
		iq_conn.close()

	# Creating the search button and connecting to submitSearch function
	submit_btn = Button(newWindow, text='Search', command=submitSearch)
	submit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

AddCust_btn = Button(root, text ='Add Customer ', command = AddCustWindow)
AddCust_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

AddCar_btn = Button(root, text ='Add Car ', command = AddCarWindow)
AddCar_btn.grid(row = 8, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

AddRental_btn = Button(root, text ='Add Rental ', command = AddRentalWindow)
AddRental_btn.grid(row = 9, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

ReturnRental_btn = Button(root, text ='Return Rental ', command = ReturnRentalWindow)
ReturnRental_btn.grid(row = 10, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

CustomerBalance_btn = Button(root, text ='Customer Balance ', command = ViewCustomerInfo)
CustomerBalance_btn.grid(row = 11, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

VehiclePrice_btn = Button(root, text ='Vehicle Price ', command = VehiclePriceWindow)
VehiclePrice_btn.grid(row = 12, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

# input_qry_btn = Button(root, text = 'Output Names', command = input_query)
# input_qry_btn.grid(row = 8, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)



#executes tinker components
root.mainloop()
