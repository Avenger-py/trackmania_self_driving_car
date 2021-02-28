from pynput.keyboard import Key, Listener
from pynput import keyboard
import datetime
#import logging
#log_dir = r"E:/Shantanu/Project-self_driving_car/"
#logging.basicConfig(filename=(log_dir + "{}".format(datetime.datetime.now()) + "keyLog.txt"), level=logging.DEBUG,
#                    format='%(asctime)s: %(message)s')

keystrokes = []
keystrokesWtime = []


def on_press(key):
    keystrokesWtime.append(str(datetime.datetime.now().time()) + str(key))
    #keystrokes.append(str(key))


def on_release(key):
    keystrokesWtime.append(str(datetime.datetime.now().time()) + str('{} released'.format(key)))
    #keystrokes.append(str('{} released'.format(key)))
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print(keystrokesWtime)
keystrokes = [i[15:] for i in keystrokesWtime]
print(keystrokes)


marker_w = keystrokes.index("'w'")
marker_a = keystrokes.index("'a'")
marker_s = keystrokes.index("'s'")
marker_d = keystrokes.index("'d'")

for j in range(len(keystrokes)):
    if keystrokes[j] == "'w' released":
        keystrokes[j] = ""
        if keystrokes[j-1] != "'w'":
            for i in range(marker_w, j):
                if keystrokes[i] != "'w'" and keystrokes[i] != "":
                    keystrokes[i] = keystrokes[i] + "'w'"
    try:
        marker_w = keystrokes.index("'w'")
        marker_a = keystrokes.index("'a'")
        marker_s = keystrokes.index("'s'")
        marker_d = keystrokes.index("'d'")
    except ValueError:
        pass

    if keystrokes[j] == "'d' released":
        keystrokes[j] = ""
        if keystrokes[j - 1] != "'d'":
            for i in range(marker_d, j):
                if keystrokes[i] != "'d'" and keystrokes[i] != "":
                    keystrokes[i] = keystrokes[i] + "'d'"
    try:
        marker_w = keystrokes.index("'w'")
        marker_a = keystrokes.index("'a'")
        marker_s = keystrokes.index("'s'")
        marker_d = keystrokes.index("'d'")
    except ValueError:
        pass

    if keystrokes[j] == "'a' released":
        keystrokes[j] = ""
        if keystrokes[j-1] != "'a'":
            for i in range(marker_a, j):
                if keystrokes[i] != "'a'" and keystrokes[i] != "":
                    keystrokes[i] = keystrokes[i] + "'a'"
    try:
        marker_w = keystrokes.index("'w'")
        marker_a = keystrokes.index("'a'")
        marker_s = keystrokes.index("'s'")
        marker_d = keystrokes.index("'d'")
    except ValueError:
        pass

    if keystrokes[j] == "'s' released":
        keystrokes[j] = ""
        if keystrokes[j-1] != "'s'":
            for i in range(marker_s, j):
                if keystrokes[i] != "'s'" and keystrokes[i] !="":
                    keystrokes[i] = keystrokes[i] + "'s'"
    try:
        marker_w = keystrokes.index("'w'")
        marker_a = keystrokes.index("'a'")
        marker_s = keystrokes.index("'s'")
        marker_d = keystrokes.index("'d'")
    except ValueError:
        pass

print(keystrokes)
keystrokes = [i[:15] + j for i, j in zip(keystrokesWtime, keystrokes)]
print(keystrokes)



x = datetime.datetime.now()
with open(x.strftime("%d%b%H%M")+"keylog.txt", "w") as output:
    output.write(str(keystrokes))
