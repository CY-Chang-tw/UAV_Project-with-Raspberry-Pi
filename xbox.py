import pygame as pg

pg.init()
pg.joystick.init()

joystick = pg.joystick.Joystick(0)

joystick.init()

while True:
    for event in pg.event.get():
        if event.type == pg.JOYAXISMOTION:
            if event.axis == 2 or event.axis == 3:
                print('右搖桿')
                x = joystick.get_axis(2)
                y = joystick.get_axis(3)
                print("axis " + str(2) +": " + str(x))
                print("axis " + str(3) +": " + str(y))
            elif event.axis == 4:
                print('RT')
                axis = joystick.get_axis(4)
                print("axis " + str(4) +": " + str(axis))
            elif event.axis == 5:
                print('LT')
                axis = joystick.get_axis(5)
                print("axis " + str(5) +": " + str(axis))

         #   axes = joystick.get_numaxes()
          #  for i in range(axes):
           #     axis = joystick.get_axis(i)
            #    print("axis " + str(i) +": " + str(axis))

pg.joystick.quit()
