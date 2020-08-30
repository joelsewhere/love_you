from src.app import *
from src.error_handling import  *

if __name__ == "__main__":
    if check():
        try:
            love_you_mom()
            push_log()
        except:
            push_log(error=True)

          