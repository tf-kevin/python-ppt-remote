# This is a script to remote control PowerPoint presentations on macOS from your smartphone. 
# Usage:
#  * Run pptremoteserver.py on a server accessible from the internet
#  * Run pptremoteagent.py on the computer where you have PowerPoint running
#  * Open the pptremoteserver's IP address with your smartphone's browser and control the slideshow
#
# Notes:
#  * By default pptremoteagent.py polls localhost:8080. To have it poll a different address, run:
#       pptremoteagent.py -s <serverip>:<serverport>
#  * You will need to install the following Python 3 modules:
#       On server: flask
#       On agent: keyboard, requests

import time, requests, sys, getopt, keyboard

REQUESTS_CONNECT_TIMEOUT    = 5
REQUESTS_READ_TIMEOUT       = 5

COMMANDS = ['next', 'back', 'stop']

def getcommand (p_server):
    try:
        r = requests.get('http://' + p_server + '/command/', timeout=(REQUESTS_CONNECT_TIMEOUT, REQUESTS_READ_TIMEOUT))
    except:
        print('WARNING: unable to access command server')
        return(None)
        
    if r.status_code != requests.codes.ok:
        return (None)
        
    rjson = r.json()
    
    if not rjson is None:
        rcmd = rjson['command']
        if rcmd in COMMANDS:
            return(rcmd)
    
    return(None)


def main(argv):
    #initialize variables for command line arguments
    arg_server = '127.0.0.1:8080'

    #get command line arguments
    try:
        opts, args = getopt.getopt(argv, 's:')
    except getopt.GetoptError:
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-s':
            arg_server = arg

    print ('INFO: Polling server %s' % arg_server)        
            
    while (True):
        time.sleep(1)
        
        cmd = getcommand (arg_server)
            if not cmd is None:
                if   cmd == 'next':
                    keyboard.send('space')
                elif cmd == 'back':
                    keyboard.send('backspace')
                elif cmd == 'stop':
                    keyboard.send('escape')
                    
       
if __name__ == '__main__':
    main(sys.argv[1:])            
