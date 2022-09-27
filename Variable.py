# Created by: John Hanekom
# Date: September 26th, 2022
# 
# This program sets a variable named "counter" to 0 and adds 1 when you press A but subtracts 1 when you press B. When you press A+B it will show the number.

counter = 0
def on_button_pressed_a():
    global counter
    counter += 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)
def on_button_pressed_b():
    global counter
    counter = -= 1
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_ab():
    basic.show_number(counter):

