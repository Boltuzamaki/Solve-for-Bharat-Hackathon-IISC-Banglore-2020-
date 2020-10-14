import keyboard  # using module keyboard
while True:  # making a loop
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        break  # finishing the loop
    else:
        continue # if user pressed a key other than the given key the loop will break
