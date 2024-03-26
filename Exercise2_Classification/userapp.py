# imports neccessary Libraries
import pandas as pd
import numpy as np
import tensorflow as tf
import keras
from keras import layers

# STEP 1: save the model in the Jupyter -notebook (for example
# mobilephoneprices.keras)
# we'll use the lecture4 / ann_classification_example1.ipynb

# STEP 2: load the model, and test it briefly
# loading the model from file, see that you also have the folder correctly
#model = keras.saving.load_model("lecture5/mobilephoneprice.keras")
model = keras.saving.load_model("Exercise2_Classification\mobilephoneprice.keras")

print("Testing")

# # test the model with existing code from ann_classification_example1
# # let's try with some new imaginary data
# # modify this as needed regarding your own dataset
# tester_row = {
#     'battery_power': 1000, 
#     'dual_sim': 0 ,
#     'fc': 4, 
#     'int_memory': 4, 
#     'n_cores': 1, 
#     'pc': 4,
#     'px_height': 900,
#     'px_width': 1200, 
#     'ram': 2096, 
#     'sc_h': 7, 
#     'sc_w': 4, 
#     'talk_time': 12
# }

# # convert to pandas-format
# tester_row = pd.DataFrame([tester_row])
# result = model.predict(tester_row)[0]
# result_index = np.argmax(result)

# categories = ['1: Cheap', '2: Avg-', '3: Avg+', '4: Expensive']

# # print the actual name with this index
# result_text = categories[result_index]

# # print the result
# print(f"Predicted price range: {result_text}")

# STEP 3: create a window application with tkinter
# - how to make buttons, textboxes etc.
# - how to make the button to do something if it's clicked
# - how to connect textboxes into our Keras model

# we're going to use and modify this example:
# https://www.geeksforgeeks.org/how-to-set-text-of-tkinter-text-widget-with-a-button/

# Import the tkinter module
import tkinter 
#from tkinter import *
 
# Creating the GUI window.
window = tkinter.Tk()
window.title("Deep learning GUI - Ultimate version 1.034bc")
window.geometry("400x800")
window.option_add("*font", "lucida 10 bold")

# make a text label for the first Entry
label1 = tkinter.Label(window, text="Battery power (mAh)")
label1.pack(pady=3)

# Creating our text widget.
entry_battery = tkinter.Entry(window)
entry_battery.pack(pady=0)

def show(): 
	label2.config( text = clicked.get() ) 

# Dropdown menu options 
options = [ 
	" ",
	"0", 
	"1", 
] 

label2 = tkinter.Label(window, text="Dual SIM (0/1)")
label2.pack(pady=2)

# Creating our text widget.
#entry_dualsim = tkinter.Entry(window)
#entry_dualsim.pack(pady=0)

# datatype of menu text 
clicked = tkinter.StringVar() 

# Create Dropdown menu 
drop = tkinter.OptionMenu( window , clicked , *options ) 
drop.pack(pady=2) 

# make a text label for the third Entry
label3 = tkinter.Label(window, text="Front cam (mpx)")
label3.pack(pady=2)

# Creating our text widget.
entry_frontcam = tkinter.Entry(window)
entry_frontcam.pack(pady=0)

# make a text label for the fourth Entry
label4 = tkinter.Label(window, text="Internal memory / storage (Gb)")
label4.pack(pady=2)

# Creating our text widget.
entry_intmemory = tkinter.Entry(window)
entry_intmemory.pack(pady=0)

# make a text label for the fifth Entry
label5 = tkinter.Label(window, text="Amount of cores")
label5.pack(pady=2)

# Creating our text widget.
entry_cores = tkinter.Entry(window)
entry_cores.pack(pady=0)

# make a text label for the sixth Entry
label6 = tkinter.Label(window, text="Primary camera (mpx)")
label6.pack(pady=2)

# Creating our text widget.
entry_primarycam= tkinter.Entry(window)
entry_primarycam.pack(pady=0)

# make a text label for the seveth Entry
label7 = tkinter.Label(window, text="Height (px)")
label7.pack(pady=2)

# Creating our text widget.
entry_pixelh = tkinter.Entry(window)
entry_pixelh.pack(pady=0)

# make a text label for the eight Entry
label8 = tkinter.Label(window, text="Width (px)")
label8.pack(pady=2)

# Creating our text widget.
entry_pixelw = tkinter.Entry(window)
entry_pixelw.pack(pady=0)

# make a text label for the ninth Entry
label9 = tkinter.Label(window, text="RAM (Mb)")
label9.pack(pady=2)

# Creating our text widget.
entry_ram = tkinter.Entry(window)
entry_ram.pack(pady=0)

# make a text label for the tenth Entry
label10 = tkinter.Label(window, text="Screen height (cm)")
label10.pack(pady=2)

# Creating our text widget.
entry_screenh = tkinter.Entry(window)
entry_screenh.pack(pady=0)

# make a text label for the eleventh Entry
label11 = tkinter.Label(window, text="Screen width (cm)")
label11.pack(pady=2)

# Creating our text widget.
entry_screenw = tkinter.Entry(window)
entry_screenw.pack(pady=0)

# make a text label for the twelfth Entry
label12 = tkinter.Label(window, text="Talk time (hours)")
label12.pack(pady=2)

# Creating our text widget.
entry_talktime = tkinter.Entry(window)
entry_talktime.pack(pady=0)

# Creating the function to set the text 
# with the help of button

# connect each Entry's text-value
# into the correct attribute in the tester row
# remember to also convert each text into int
def set_text_by_button():
    tester_row = {
        'battery_power': int(entry_battery.get()), 
        'dual_sim': int(clicked.get()),
        'fc': int(entry_frontcam.get()), 
        'int_memory': int(entry_intmemory.get()), 
        'n_cores': int(entry_cores.get()), 
        'pc': int(entry_primarycam.get()),
        'px_height': int(entry_pixelh.get()),
        'px_width': int(entry_pixelw.get()), 
        'ram': int(entry_ram.get()), 
        'sc_h': int(entry_screenh.get()), 
        'sc_w': int(entry_screenw.get()), 
        'talk_time': int(entry_talktime.get())
    }

    # convert to pandas-format
    tester_row = pd.DataFrame([tester_row])
    result = model.predict(tester_row)[0]
    result_index = np.argmax(result)

    categories = ['1: Cheap', '2: Avg-', '3: Avg+', '4: Expensive']

    # print the actual name with this index
    result_text = categories[result_index]

    # print the result
    result_string.set(f"Predicted price range: {result_text}")
 

# Setting up the button, set_text_by_button() 
# is passed as a command
set_up_button = tkinter.Button(window, height=1, width=10, text="Set", 
                    command=set_text_by_button)

set_up_button.pack(pady=10)
 
# the result text we will change with the function
# this is connected to the label below
result_string = tkinter.StringVar()
result_string.set("Waiting for user input...")

# make a text label for the first Entry
label_result = tkinter.Label(window, textvariable=result_string, fg="red")
label_result.pack(pady=4)




# launch the window application
window.mainloop()
