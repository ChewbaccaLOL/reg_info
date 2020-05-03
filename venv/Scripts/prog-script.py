#!C:\Users\volko\PycharmProjects\reg_info\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'MainApp==0.1','console_scripts','prog'
__requires__ = 'MainApp==0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('MainApp==0.1', 'console_scripts', 'prog')()
    )
