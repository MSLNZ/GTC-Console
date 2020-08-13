import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "gtc",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("gtc.py", base=base)])
        
# # These excludes were found by trial and error by excluding stuff library.zip 
# excludes = [
    # "pywin","pywin.debugger","pywin.debugger.dbgcon","pywin.dialogs","pywin.dialogs.list",
    # "Tkconstants","Tkinter","tcl",
    # "email", "_ssl",
# #    "doctest",
    # "unitest",
# #    "pdb",
# #    "difflib",
    # 'BaseHTTPServer', 'SocketServer',
# #    'StringIO',
    # '_LWPCookieJar', '_MozillaCookieJar',
# #    '_threading_local', 
# #    'atexit', 
# #    'bisect', 
# #    'calendar', "socket", 'base64',  # used by `openpyxl`
    # 'cookielib','os2emxpath', 
# #    'pickle', 'posixpath',
# #   'urllib', 'urllib2', 'urlparse', 'uu', # used by `openpyxl`
# #    'weakref', 
    # 'webbrowser', 'win32pdh'
# #    'zipfile', 'nturl2path',    # used by openpyxl
# #    '_ctypes', 
    # '_hashlib', 'bz2',
    # 'ssl',
# #    'struct', # used by xlrd and xlwt, openpyxl
# #    'subprocess', 
    # 'symbol', 'symtable', 
# #    'threading', 
    # 'tty','formatter','ftplib','getpass','gettext',
    # 'gzip',
# #    'hashlib', 
    # 'httplib',
    # 'logging/__init__', 'macurl2path', 'mimetools',
# #    'mimetypes', 
    # 'new', 
# #    'pprint',
# #    'py_compile',
    # 'quopri', 'rfc822', 'shlex', 
# #    'shutil',
    # ]
# includes = [
    # '__future__', 'csv', 'decimal', 'zipfile', 'glob',
    # 'jdcal', 'json', 'et_xmlfile'   # for openpyxy (needed to install with .py source)
# #    'pyvisa'    # for Murray
    
# ]
# packages = [ 'xml' ]
# ignores = [
    # 'IronPythonConsole',
    # 'System',
    # 'System.Windows.Forms.Clipboard',
    # 'clr',
    # 'modes.editingmodes',
    # 'startup',
    # ] +\
    # ['sitecustomize', 'usercustomize'] +\
    # ['email.base64mime', 'email.utils']

# dll_excludes = ['w9xpopen.exe']

# setup(
    # # data_files=data_files, 
    # console=[
        # {
            # "script": "gtc.py",                             ### Main Python script    
            # # "icon_resources": [(0, "../icon/gtc.ico")]      ### Icon to embed into the PE file.
        # }
        # ],
    # options= {
        # "py2exe": {
                # "excludes" : excludes
            # ,	"includes" : includes
            # ,	"ignores"  : ignores
            # ,	"dll_excludes" : dll_excludes
            # ,	"packages" : packages
            # ,	"unbuffered": True
            # ,   "ascii"     : False
            # ,   "bundle_files" : 1
        # }
    # },
    # zipfile=None,
# )