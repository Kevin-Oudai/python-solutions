import time

currentseconds = int(time.time())
offset = eval(input("Enter the time zone offset to GMT: "))
offset = offset * 60 * 60
currentseconds = currentseconds - offset
seconds = currentseconds % 60
currentseconds = currentseconds // 60
minutes = currentseconds % 60
currentseconds = currentseconds // 60
hours = currentseconds % 24
print("{}:{}:{}".format(hours, minutes, seconds))
