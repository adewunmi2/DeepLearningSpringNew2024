# I imported the needed imports
import pandas as pd
import numpy as np
import tensorflow as tf
import keras
from keras import layers

# STEP 1: recall the saved classification model  
# which is carpurchaseprice.keras
# the ann_classification_exercise2Updated.ipynb
# needed designing the userapp

# STEP 2: 
# proceed to load the model, 
# and then test it 
# loading the model from file, see that you also have the folder correctly
model = keras.saving.load_model("DeepLearningSpringNew2024/New_Exercise2_Project/carpurchaseprice.keras")


print("Userapp")

# tester_row = {
    # 'gender': 0, 
    # 'age': 45,
    # 'BasePay': 250000, 
    # 'OvertimePay': 100000, 
    # 'OtherPay': 160000, 
    # 'TotalPay': 400000,
    # 'TotalPayBenefits': 600000,
    # 'credit_card_debt': 90000, 
    # 'net_worth': 600000, 
    # 'car_purchase_amount': 250000, 
#}

# Import the tkinter module
import tkinter 
 
# Creating the GUI window.
window = tkinter.Tk()
window.title("Deep learning GUI - Ultimate version 1.034bc")
window.geometry("400x800")
window.option_add("*font", "lucida 10 bold")

# make a text label for the first Entry
def show(): 
	label2.config( text = clicked.get() ) 

# Dropdown menu options 
options = [ 
	" ",
	"0", 
	"1", 
] 

label1 = tkinter.Label(window, text="Gender")
label1.pack(pady=4)

# datatype of menu text 
clicked = tkinter.StringVar() 

# Create Dropdown menu 
drop = tkinter.OptionMenu( window , clicked , *options ) 
drop.pack(pady=2) 

# make a text label for the second Entry
label2 = tkinter.Label(window, text="Age")
label2.pack(pady=4)

# Creating our text widget.
entry_age = tkinter.Entry(window)
entry_age.pack(pady=0)

# make a text label for the third Entry
label3 = tkinter.Label(window, text="Base Payment")
label3.pack(pady=4)

# Creating our text widget.
entry_basepay = tkinter.Entry(window)
entry_basepay.pack(pady=0)

# make a text label for the forth Entry
label4 = tkinter.Label(window, text="Overtime Payemnt")
label4.pack(pady=4)

# Creating our text widget.
entry_overtime = tkinter.Entry(window)
entry_overtime.pack(pady=0)

# make a text label for the fifth Entry
label5 = tkinter.Label(window, text="Other Payment")
label5.pack(pady=4)

# Creating our text widget.
entry_otherpay = tkinter.Entry(window)
entry_otherpay.pack(pady=0)

# make a text label for the sixth Entry
label6 = tkinter.Label(window, text="Total Payment")
label6.pack(pady=4)

# Creating our text widget.
entry_totalpay = tkinter.Entry(window)
entry_totalpay.pack(pady=0)

# make a text label for the seventh Entry
label7 = tkinter.Label(window, text="Total Benefits paid")
label7.pack(pady=4)

# Creating our text widget.
entry_totalbenefitpay= tkinter.Entry(window)
entry_totalbenefitpay.pack(pady=0)

# make a text label for the eight Entry
label8 = tkinter.Label(window, text="Credit Bank Card Debt")
label8.pack(pady=4)

# Creating our text widget.
entry_creditcarddebt = tkinter.Entry(window)
entry_creditcarddebt.pack(pady=0)

# make a text label for the ninth Entry
label9 = tkinter.Label(window, text="Net Worth")
label9.pack(pady=4)

# Creating our text widget.
entry_networth = tkinter.Entry(window)
entry_networth.pack(pady=0)

# make a text label for the tenth Entry
label10 = tkinter.Label(window, text="Car Purchase Amount")
label10.pack(pady=4)

# Creating our text widget.
entry_carpurchaseamount = tkinter.Entry(window)
entry_carpurchaseamount.pack(pady=0)

# there's high need to
# Create the function to set the text 
# with the help of button

# I then connected each Entry's text-value
# into their correct attribute in the tester row
# I did convert each text into int
def set_text_by_button():
    tester_row = {
        'gender': int(clicked.get()), 
        'age': int(entry_age.get()), 
        'basepay': int(entry_basepay.get()),
        'overtimepay': int(entry_overtime.get()), 
        'otherpay': int(entry_otherpay.get()), 
        'totalpay': int(entry_totalpay.get()), 
        'totalbenefit': int(entry_totalbenefitpay.get()),
        'creditcard': int(entry_creditcarddebt.get()),
        'networth': int(entry_networth.get()), 
        'carpurchase': int(entry_carpurchaseamount.get())
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