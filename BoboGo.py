import maestro
import time
MOTORS = 1
TURN = 2
BODY = 0
HEADTILT = 4
HEADTURN = 3
zeroed = 6000
Tamount = 900
Famount = 800
up = 6000
left = 6000

bobo = maestro.Controller()
def start():
    bobo.setTarget(4, 6000)
    time.sleep(0.3)
    bobo.setTarget(4, 1510)

def torqueRight(torque, amount):
    if not torque:
        bobo.setTarget(TURN, 8000)
        time.sleep(0.01)
    bobo.setTarget(TURN, zeroed + int(amount))
    return True

def torqueLeft(torque,amount):
    if not torque:
        bobo.setTarget(TURN, 8000)
        time.sleep(0.01)
    bobo.setTarget(TURN, zeroed - int(amount))
    return True

    
def goLeft(delay=0, amount=0):
    bobo.setTarget(TURN, zeroed - int(amount))
    time.sleep(delay)

def goRight(delay=0, amount=0):
    bobo.setTarget(TURN, zeroed + int(amount))
    time.sleep(delay)

def goForward(delay=0, amount=Famount):
    bobo.setTarget(MOTORS, zeroed - amount)
    time.sleep(delay)

def goBackward(delay=0, amount=Famount):
    bobo.setTarget(MOTORS, zeroed + amount)
    time.sleep(delay)

def lookUp(amount):
    global up
    up += amount
    bobo.setTarget(HEADTILT, up)

def lookDown(amount):
    global up
    up -= amount
    bobo.setTarget(HEADTILT, up)

def lookRight(amount):
    global left
    left -= amount
    bobo.setTarget(HEADTURN, left)

def lookLeft(amount):
    global left
    left += amount
    bobo.setTarget(HEADTURN, left)

def stop():
    for i in range(5):
        bobo.setTarget(i, 6000)

def stopMoving():
    for i in range(2):
        bobo.setTarget(i, 6000)


def getServoValues():
    return up, left
