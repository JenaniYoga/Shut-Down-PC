import os

print('1.Shutdown')
print('2.Restart')
print('3.Exit')

command=input('Enter Your Command')

if'1' in command:
    os.system('shutdown/s')
if'2' in command:
    os.system('shutdown/r')
if'3' in command:
    exit()
