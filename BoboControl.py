# !/usr/bin/python
import threading, queue
import BoboGo as bg
# import maestro

# MOTORS = 1
# TURN = 2
# BODY = 0
# HEADTILT = 4
# HEADTURN = 3

# bobo = maestro.Controller()

# gamepad = InputDevice('/dev/input/event3')

# bobo = maestro.Controller()
# body = 6000
# headTurn = 6000
# headTilt = 6000
# motors = 6000
# turn = 6000
# amount = 1200

# turn = 6000
# bobo.setTarget(TURN, turn)
# motors = 6000
# bobo.setTarget(MOTORS, motors)
# bobo.setTarget(BODY, 6000)
# bobo.setTarget(HEADTILT, 6000)
# bobo.setTarget(HEADTURN, 6000)
# for event in gamepad.read_loop():
#     if event.type == ecodes.EV_KEY:
#         keyevent = categorize(event)
#         if keyevent.keystate == KeyEvent.key_down:
#             if keyevent.keycode[0] == 'BTN_A':
#                 print("X")
#                 motors -= amount
#                 if (motors < 1510):
#                     motors = 1510
#                 print(motors)
#                 bobo.setTarget(MOTORS, motors)
#             elif keyevent.keycode[1] == 'BTN_Y':
#                 print("Square")
#                 turn -= amount
#                 if (turn < 2110):
#                     turn = 2110
#                 print(turn)
#                 bobo.setTarget(TURN, turn)

#             elif keyevent.keycode[0] == 'BTN_B':
#                 print("Circle")
#                 turn += amount
#                 if (turn > 7400):
#                     turn = 7400
#                 print(turn)
#                 bobo.setTarget(TURN, turn)
#             elif keyevent.keycode[1] == 'BTN_X':
#                 print("Triangle")
#                 motors += amount
#                 if (motors > 7900):
#                     motors = 7900
#                 print(motors)
#                 bobo.setTarget(MOTORS, motors)
#             else:
#                 turn = 6000
#                 bobo.setTarget(TURN, turn)
#                 motors = 6000
#                 bobo.setTarget(MOTORS, motors)


class BoboControl:
    def __init__(self, device):
        self.device = device
        self.change_mode = [False]
        self.mode_lock = threading.Lock()
        self.event_queue = queue.Queue()
        self.event_handler = BoboEventHandler(self.device, self.event_queue, self.change_mode, self.mode_lock)
        self.event_handler.start()

        self.turn_mult = 

    def run_tick(self):
        event = self.event_queue.get()
        
        #Reset Bobo
        if event[0] == "Select":
            bg.stop()
        elif event[0] == "Start":
            bg.stopMoving()

        elif event[0] = "RX":
            bg.lookLeft(7 * (event[1]-128))
        elif event[0] = "RY":
            bg.lookUp(7 * (event[1]-128))

        elif event[0] = "LT":
            bg.goLeft(0, 3*event[1])
        elif event[0] = "RT":
            bg.goLeft(0, -3*event[1])

        elif event[0] == "LY":
            bg.goForward(7 * (event[1]-128))


    def check_mode(self):
        with self.mode_lock:
            return self.change_mode[0]

    def mode_changed(self):
        with self.mode_lock:
            self.change_mode[0] = False

class BoboEventHandler(threading.Thread):
    def __init__(self, device, event_queue, change_mode, mode_lock):
        threading.Thread.__init__(self, daemon=True)
        self.change_mode = change_mode
        self.mode_lock = mode_lock


        self.device = device
        self.device_state = {
            "LY":0,
            "LX":0,
            "LT":0,

            "RY":0,
            "RX":0,
            "RT":0,

            "HAT_X":0,
            "HAT_Y":0,

            "Cross":0,
            "Circle":0,
            "Triangle":0,
            "Square":0,

            "LB":0,
            "RB":0,

            "Select":0,
            "Start":0,
            "Home":0,
        }
        self.axes = ["LY", "LX", "LT", "RY", "RX", "RT"]
        self.axes_thresh = 5

        self.hats = ["HAT_X","HAT_Y"]
        self.buttons = ["Cross", "Circle", "Triangle", "Square", "LB", "RB", "Select", "Start", "Home"]
        self.event_queue = event_queue

    def run(self):
        while True:
            event = self.device.get_event()
            if event[0] in self.axes:
                if abs(self.device_state[event[0]] - event[1]) > self.axes_thresh:
                    self.event_queue.put(event)

            elif event[0] in self.hats:
                if self.device_state[event[0]] != event[1] and event[1] == 0:
                    self.event_queue.put(event)
            
            elif event[0] in self.buttons:
                if self.device_state[event[0]] != event[1] and event[1] == 0:
                    self.event_queue.put(event)
                    if event[0] == "Home":
                        # print("Change Mode")
                        with self.mode_lock:
                            self.change_mode[0] = True


            self.device_state[event[0]]= event[1] 