from multiprocessing import Process
import time
import keyboard

def my_loop():
    while True:
        print("a")
        time.sleep(0.3)


if __name__ == '__main__': # This is necessary for Windows (and maybe Mac OS X) to work properly with multiprocessing module   
    process = Process(target=my_loop)
    process.start()
    while process.is_alive():
        if keyboard.is_pressed('q'):
            process.terminate()
            break
        print("b")
        time.sleep(0.3)


