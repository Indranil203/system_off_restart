#System Shutdown And Restart
import os

def Systemoffrestart():
    print("Enter r for restart:")
    print("Enter s for shutdown:")
    print("Enter any key for exit:")

    option=input("Enter your option:")

    if(option=='r'):
        os.system('shutdown /r')
    elif(option=='s'):
        os.system('shutdown /s')
    else:
        print('you exit')
        exit()

Systemoffrestart()