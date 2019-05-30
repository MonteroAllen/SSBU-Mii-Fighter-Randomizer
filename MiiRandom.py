#Python 3
#Made by SterbenScix12 on Github
import PySimpleGUI as sg
import random

# Randomizer
def button1():
        BUpSpecial = ["1: Soaring Axe Kick", "2: Helicopter Kick", "3: Thrust Uppercut"]
        BNeutralSpecial = ["1: Shot Put", "2: Flashing Mach Punch", "3: Exploding Side Kick"]
        BSideSpecial = ["1: Onslaught", "2: Burning Dropkick", "3: Suplex"]
        BDownSpecial = ["1: Head-On Assault", "2: Feint jump", "3: Counter Throw"]

        sg.Popup('Mii Brawler', random.choice(BNeutralSpecial), random.choice(BSideSpecial), random.choice(BUpSpecial),
                 random.choice(BDownSpecial))

def button2():
    SUpSpecial = ["1: Stone Scabbard", "2: Skyward Slash Dash ", "3: Hero's Spin"]
    SNeutralSpecial = ["1: Gale Strike", "2: Shuriken of Light", "3: Blurring Blade"]
    SSideSpecial = ["1: Airborne Assault", "2: Gale Stab", "3: Chakram"]
    SDownSpecial = ["1: Blade Counter", "2: Reversal Slash", "3: Power Thrust"]

    sg.Popup('Mii Sword', random.choice(SNeutralSpecial), random.choice(SSideSpecial), random.choice(SUpSpecial),
          random.choice(SDownSpecial))

def button3():

    GUpSpecial = ["1: Lunar Launch", "2: Canon Jump Kick", "3: Arm Rocket"]
    GNeutralSpecial = ["1: Charge Blast", "2: Laser Blaze", "3: Grenade Launch"]
    GSideSpecial = ["1: Flame Pillar", "2: Stealth Burst", "3: Gunner Missle"]
    GDownSpecial = ["1: Echo Reflector", "2: Bomb Drop", "3: Absorbing Vortex"]

    sg.Popup('Mii Gunner.', random.choice(GNeutralSpecial), random.choice(GSideSpecial), random.choice(GUpSpecial),
          random.choice(GDownSpecial))

def button4():
    Randomfighter = [button1, button2, button3,]
    random.choice(Randomfighter)()

#NSUD

# Button Layout
layout = [
              [sg.Button('Mii Bralwer'), sg.Button('Mii Sword'), sg.Button('Mii Gunner'), sg.Button('Random')]
             ]
# Shows Window
window = sg.Window('Mii Fighter Randomizer', layout)

# Event loop
while True:
    event, value = window.Read()
    # Take appropriate action based on button
    if event == 'Mii Bralwer':
        button1()
    elif event == 'Mii Sword':
        button2()
    elif event == 'Mii Gunner':
        button3()
    elif event == 'Random':
        button4()