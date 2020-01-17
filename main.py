from BoboDemeanor import BoboDemeanor
from BoboControl import BoboControl

from PS4Wrapper import PS4Controller
import threading, queue

if __name__ == "__main__":
    human_control = True
    mode_changed = False

    human_color = (209,66,245)
    ai_color    = (66,245,96)

    mode_lock = threading.Lock()

    ps4 = PS4Controller("/dev/input/event19")
    ps4.set_color(*human_color)

    bc = BoboControl(ps4)

    face_queue = queue.Queue(10)
    bd = BoboDemeanor(face_queue)
    bd.start()

    face_queue.put("happy")
    
    while True:
        if human_control == True:
            if mode_changed:
                ps4.set_color(*human_color)
                mode_changed = False

            bc.run_tick()

            if bc.check_mode():
                human_control = False
                mode_changed = True
                bc.mode_changed()

        else:
            if mode_changed:
                ps4.set_color(*ai_color)
                mode_changed = False

            # bt.run_tick()

            if bc.check_mode():
                human_control = True
                mode_changed = True
                bc.mode_changed()
            
