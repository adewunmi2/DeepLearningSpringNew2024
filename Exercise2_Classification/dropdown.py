import pandas as pd
import numpy as np
import tensorflow as tf
import keras
from keras import layers

# Import module 
#from tkinter import *
import tkinter

# Create object 
window = tkinter.Tk() 

# Adjust size 
window.geometry( "200x200" ) 

# Change the label text 
def show(): 
	label1.config( text = clicked.get() ) 

# Dropdown menu options 
options = [ 
	" ",
	"0", 
	"1" 
] 

# Create Label 
label1 = tkinter.Label( window , text = "Dual SIM (0/1)" ) 
label1.pack() 

# Creating our text widget.
entry_dualsim = tkinter.Entry(window)
entry_dualsim.pack(pady=0)

# datatype of menu text 
clicked = tkinter.StringVar() 

# initial menu text 
#clicked.set( "Monday" ) 

# Create Dropdown menu 
drop = tkinter.OptionMenu( window , clicked , *options ) 
drop.pack() 

# Create button, it will change label text 
#button = Button( root , text = "click Me" , command = show ).pack() 

# Create Label 
#label = Label( root , text = "Dual SIM (0/1)" ) 
#label.pack() 

def set_text_by_button():
	test_row = {
		'dual_sim': int(entry_dualsim.get())
    }

# Execute tkinter 
window.mainloop() 
