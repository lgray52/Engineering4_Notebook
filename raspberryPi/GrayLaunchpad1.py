from time import sleep
counter = 10

if counter > 0:
    print(counter)
    counter -= 1
    sleep(1)

if counter == 0:
    print("LIFTOFF")