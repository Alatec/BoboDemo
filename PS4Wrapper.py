import evdev
import glob
import subprocess
import queue
import threading
import time



class PS4Controller():
    def __init__(self, path):
        self.device = evdev.InputDevice(path)
        self.DS4_colors = [
            glob.glob("/sys/class/leds/[0-9]*red/brightness")[0],
            glob.glob("/sys/class/leds/[0-9]*green/brightness")[0],
            glob.glob("/sys/class/leds/[0-9]*blue/brightness")[0],
        ]

        self.set_color(255,0,0)
        time.sleep(0.5)
        self.set_color(0,255,0)
        time.sleep(0.5)
        self.set_color(0,0,255)

        self.event_queue = queue.Queue(maxsize=100)

        self.event_handler = PS4EventHandler(self.event_queue, self.device)

        self.event_handler.start()



    def set_color(self, r,g,b):
        rgb = [r,g,b]
        for c, color in enumerate(self.DS4_colors):
            p1 = subprocess.Popen(['echo', str(rgb[c])], stdout=subprocess.PIPE)
            p2 = subprocess.Popen(['tee', str(color)], stdin=p1.stdout, stdout=subprocess.PIPE)
            p2.communicate()

    def get_event(self):
        return self.event_queue.get()

class PS4EventHandler(threading.Thread):
    def __init__(self, event_queue, device, deadzone=10):
        threading.Thread.__init__(self, daemon=True)
        self.event_queue = event_queue
        self.device = device
        self.deadzone = deadzone


    def run(self):
        for event in self.device.read_loop():
        # print(event.type)
        #Handle Analog Inputs
            if event.type == evdev.ecodes.EV_ABS:
                axis = event.code

                #LY
                if axis == 0:
                    if event.value < 128 - self.deadzone or event.value > 128 + self.deadzone:
                        self.event_queue.put(('LY', event.value)) 
                    else:
                        self.event_queue.put(('LY', 128)) 

                #LX
                elif axis == 1:
                    if event.value < 128 - self.deadzone or event.value > 128 + self.deadzone:
                        self.event_queue.put(('LX', event.value)) 
                    else:
                        self.event_queue.put(('LX', 128)) 


                #LT
                elif axis == 2:
                    if event.value > 10:
                        self.event_queue.put(('LT', event.value)) 
                    else:
                        self.event_queue.put(('LT', 0)) 
                        

                #RX
                elif axis == 3:
                    if event.value < 128 - self.deadzone or event.value > 128 + self.deadzone:
                        self.event_queue.put(('RX', event.value)) 
                    else:
                        self.event_queue.put(('RX', 128)) 

                
                #RY
                elif axis == 4:
                    if event.value < 128 - self.deadzone or event.value > 128 + self.deadzone:
                        self.event_queue.put(('RY', event.value)) 
                    else:
                        self.event_queue.put(('RY', 128)) 


                #RT
                elif axis == 5:
                        if event.value > 10:
                        self.event_queue.put(('RT', event.value)) 
                    else:
                        self.event_queue.put(('RT', 0)) ) 

                #HAT_X
                elif axis == 16:
                        self.event_queue.put(('HAT_X', event.value)) 

                #HAT_Y
                elif axis == 17:
                        self.event_queue.put(('HAT_Y', event.value)) 

                else:
                    print(repr(event))

            elif event.type == evdev.ecodes.EV_KEY:
                event = evdev.categorize(event)
                code = event.scancode

                #Cross
                if code == 304:
                    self.event_queue.put(('Cross', event.keystate)) 

                #Circle
                elif code == 305:
                    self.event_queue.put(('Circle', event.keystate)) 
                
                #Triangle
                elif code == 307:
                    self.event_queue.put(('Triangle', event.keystate)) 

                #Square
                elif code == 308:
                    self.event_queue.put(('Square', event.keystate)) 

                
                #LB
                elif code == 310:
                    self.event_queue.put(('LB', event.keystate)) 

                #RB
                elif code == 311:
                    self.event_queue.put(('RB', event.keystate)) 

                #Select
                elif code == 314:
                    self.event_queue.put(('Select', event.keystate)) 
                
                #Start
                elif code == 315:
                    self.event_queue.put(('Start', event.keystate)) 

                #Home
                elif code == 316:
                    self.event_queue.put(('Home', event.keystate)) 
                

if __name__ == "__main__":
    device = evdev.InputDevice('/dev/input/event19')
    deadzone = 10
    print(device.capabilities(verbose=True))
    for event in device.read_loop():
        # print(event.type)
        #Handle Analog Inputs
        if event.type == evdev.ecodes.EV_ABS:
            axis = event.code

            #LY
            if axis == 0:
                if event.value < 128 - deadzone or event.value > 128 + deadzone:
                    print(repr(event)) 

            #LX
            elif axis == 1:
                if event.value < 128 - deadzone or event.value > 128 + deadzone:
                    print(repr(event)) 

            #LT
            elif axis == 2:
                # if event.value < 128 - deadzone or event.value > 128 + deadzone:
                    print(repr(event)) 

            #RX
            elif axis == 3:
                if event.value < 128 - deadzone or event.value > 128 + deadzone:
                    print(repr(event)) 
            
            #RY
            elif axis == 4:
                if event.value < 128 - deadzone or event.value > 128 + deadzone:
                    print(repr(event)) 

            #RT
            elif axis == 5:
                # if event.value < 128 - deadzone or event.value > 128 + deadzone:
                    print(repr(event)) 

            #HAT_X
            elif axis == 16:
                # if event.value < 128 - deadzone or event.value > 128 + deadzone:
                    print(repr(event)) 

            #HAT_Y
            elif axis == 17:
                # if event.value < 128 - deadzone or event.value > 128 + deadzone:
                    print(repr(event)) 

            else:
                print(repr(event))

        elif event.type == evdev.ecodes.EV_KEY:
            event = evdev.categorize(event)
            code = event.scancode

      

            
