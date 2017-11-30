# # import curses and GPIO
# import curses
# import RPi.GPIO as GPIO
#
# in4 = 15
# in3 = 13
# in2 = 11
# in1 = 7
#
# in5 = 29
# in6 = 31
# in7 = 33
# in8 = 35
#
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(in1, GPIO.OUT)
# GPIO.setup(in2, GPIO.OUT)
# GPIO.setup(in3, GPIO.OUT)
# GPIO.setup(in4, GPIO.OUT)
# GPIO.setup(in5, GPIO.OUT)
# GPIO.setup(in6, GPIO.OUT)
# GPIO.setup(in7, GPIO.OUT)
# GPIO.setup(in8, GPIO.OUT)
#
#
# screen = curses.initscr()
# curses.noecho()
# curses.cbreak()
# screen.keypad(True)
#
#
# def w1stop():
#     GPIO.output(in1, False)
#     GPIO.output(in2, False)
#
# def w1f():
#     GPIO.output(in1, True)
#     GPIO.output(in2, False)
#
#
# def w1b():
#     GPIO.output(in1, False)
#     GPIO.output(in2, True)
#
#
# def w2stop():
#     GPIO.output(in3, False)
#     GPIO.output(in4, False)
#
# def w2f():
#     GPIO.output(in3, True)
#     GPIO.output(in4, False)
#
#
# def w2b():
#     GPIO.output(in3, False)
#     GPIO.output(in4, True)
#
#
# def w3stop():
#     GPIO.output(in5, False)
#     GPIO.output(in6, False)
#
# def w3f():
#     GPIO.output(in5, True)
#     GPIO.output(in6, False)
#
#
# def w3b():
#     GPIO.output(in5, False)
#     GPIO.output(in6, True)
#
#
# def w4stop():
#     GPIO.output(in7, False)
#     GPIO.output(in8, False)
#
# def w4f():
#     GPIO.output(in7, True)
#     GPIO.output(in8, False)
#
#
# def w4b():
#     GPIO.output(in7, False)
#     GPIO.output(in8, True)
#
#
# try:
#     while True:
#         char = screen.getch()
#         if char == ord('p'):
#             break
#         elif char == ord('q'):
#             w1f()
#         elif char == ord('a'):
#             w1stop()
#         elif char == ord('z'):
#             w1b()
#         elif char == ord('w'):
#             w2f()
#         elif char == ord('s'):
#             w2stop()
#         elif char == ord('x'):
#             w2b()
#
#         elif char == ord('7'):
#             w3f()
#         elif char == ord('4'):
#             w3stop()
#         elif char == ord('1'):
#             w3b()
#         elif char == ord('9'):
#             w4f()
#         elif char == ord('6'):
#             w4stop()
#         elif char == ord('3'):
#             w4b()
#
# finally:
#     # Close down curses properly, inc turn echo back on!
#     curses.nocbreak();
#     screen.keypad(0);
#     curses.echo()
#     curses.endwin()
#     GPIO.cleanup()
#
