import os, platform
os.system('git pull')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from HACK_TARGET import menu
    menu()
elif bit == '32bit':
    from HACK_TARGET import menu
    menu()