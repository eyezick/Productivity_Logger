#! /usr/bin/env python3

import time, os, sys, random
interval = 5
from text_feedback import *

if not os.path.exists('SelfAcct_Logs'):
    os.makedirs('SelfAcct_Logs')

setprofile = random.choice(profiles)

filename = '-'.join(list(str(x) for x in list(time.localtime())[:-4])) + '-' + str(interval) +'.txt' # log file name includes all numbers from Year through Minute the script was launched
logfile = open(os.path.join(os.getcwd(), 'SelfAcct_Logs', filename), 'a')                            # and further includes at end the chosen time interval

def alarm():
    print('\n' + setprofile[0])
    time.sleep(2.5)
    print('\n' + setprofile[1])
    time.sleep(2)
    print('\nProductivity Mode [ON]')
    def timer():
        time.sleep(interval*60)
        try:
            while True:
                print('\nTime to log!! Ctrl + C to stop alarm. ','\a', '\a', '\n')
                time.sleep(2) # time interval between each alarm
        except KeyboardInterrupt:
            rating = input('\n'+ setprofile[2] + '\n')


            if not rating.isdigit():
                clarify = input('That wasn\'t an integer, repeat to \'Quit\' or enter integer to proceed\n')
                if clarify.isdigit():
                    if int(clarify) >= 50:
                        print(setprofile[3])
                        time.sleep(2)
                        print('\nProductivity Mode [ON]')
                    else:
                        print(setprofile[4])
                        time.sleep(2)
                        print('\nProductivity Mode [ON]')
                    logfile.write(clarify + '\n')
                    timer()
                else:
                    print('\n' + setprofile[-1] + '\n')
                    sys.exit()
            else:
                if int(rating) >= 50:
                    print(setprofile[3])
                    time.sleep(2)
                    print('\nProductivity Mode [ON]')
                else:
                    print(setprofile[4])
                    time.sleep(2)
                    print('\nProductivity Mode [ON]')
                logfile.write(rating + '\n')
                timer()
    timer()

alarm()