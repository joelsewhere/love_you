import os
import  numpy as np
from subprocess import Popen
from src.error_handling import push_log

def check():
    try:  
        result = np.random.choice([False,True], p=[.95, .05])
        return result
    except:
        push_log(error=True)
    
def exec_applescript(script):
    p = Popen(['osascript', '-e', script])

def love_you_mom():
    phone_number = os.environ.get("PHONE_NUMBER")
    apple_id = os.environ.get("APPLE_ID")
    script = f'''
            tell application "Messages"
                set theBuddy to buddy "{phone_number}" of service "E:{apple_id}"
                send "Love you, Mom 🧡" to theBuddy
            end tell
            '''
    exec_applescript(script)


