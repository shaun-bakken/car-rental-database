# Step-By-Step Instructions

1. Create your Python file in the same directory as your `.db` file with your database already created.

2. When installing Python, tkinter is usually included in the download. If not, then perform `pip install tk` in the command line.

3. Make sure to import tkinter and sqlite3 in your Python file.

4. To connect the database to your tkinter window, make sure the name of the database file matches the name of the database file in your directory.

5. Finally, to access and open the database GUI, simply type in the command line "python `<Name of Python file>`" or `CarRental2019.py` in this example.

## Using the GUI

Each button in the window `CarRental2019` will open a new window when pressed. Once you are done with that new window, be sure to close that window out before pressing another one of the buttons in `CarRental2019`. When finished, close out the `CarRental2019` window to terminate.

**Note:** After opening a window from the main window, be sure to only press the new window's buttons **only once per instance** to prevent errors. For example, to prevent overlapping print statements in the "Search for cars" button, close out the "Add New Rental" window after clicking "Search for cars" one time if you want to search for cars again.

![GUI Image](https://github.com/shaun-bakken/car-rental-database/assets/30188203/d4456456-849e-4978-b8fa-81c680780ab0)
