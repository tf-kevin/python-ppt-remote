# python-ppt-remote
This is a script to remote control PowerPoint presentations on macOS from your smartphone. 

Usage:
 * Run pptremoteserver.py on a server accessible from the internet
 * Run pptremoteagent.py on the computer where you have PowerPoint running
 * Open the pptremoteserver's IP address with your smartphone's browser and control the slideshow

Notes:
  * By default pptremoteagent.py polls localhost:8080. To have it poll a different address, run:
      `pptremoteagent.py -s <serverip>:<serverport>`
 * You will need to install the following Python 3 modules:
      On server: flask
      On agent: keyboard, requests
 * This is a slightly simplified version from the original repo for macOS. 
