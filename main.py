def on_button_pressed_a():
    ht16k33.Turn_ON()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    ht16k33.Turn_OFF()
input.on_button_pressed(Button.B, on_button_pressed_b)

ht16k33.init_()
ht16k33.show_hex_number(36554)
ht16k33.write_digit_num(9, 3, True)