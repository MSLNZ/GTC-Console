import code
import sys
import os       
from optparse import OptionParser
import traceback

import math
import cmath

from GTC import *

#-----------------------------------------------------------------------------------------------
# Pyinstaller changes the site.py module, here we restore help, quit and copyright 
#
import builtins
if not hasattr(builtins,'help'):
    import _sitebuiltins

    if os.sep == '\\':
        eof = 'Ctrl-Z plus Return'
    else:
        eof = 'Ctrl-D (i.e. EOF)'

    builtins.quit = _sitebuiltins.Quitter('quit', eof)
    builtins.exit = _sitebuiltins.Quitter('exit', eof)
        
    builtins.help = _sitebuiltins._Helper()

    builtins.copyright = _sitebuiltins._Printer("copyright", sys.copyright)

#-----------------------------------------------------------------------------------------------
# Add submodules to the sys.modules register so they can be imported
#
submodules = (
    'function',
    'reporting',
    'linear_algebra',
    'type_b',
    'type_a',
)
for name in submodules:
    exec( "sys.modules['{!s}'] = {!s}".format(name,name) )
    

#-----------------------------------------------------------------------------------------------
# Add any library directories to the Python path, 
# allowing user-defined modules to be imported
#
try:
    for d in os.environ['GTC_LIB'].split(';'):
        sys.path.append(d)
except KeyError:
    pass

# Add the CWD too?
# sys.path.append('.')

# #-------------------------------------------------------
# from GTC import core 
# def help(module=core):
    # builtins.help(module)

#-----------------------------------------------------------------
def my_excepthook(tp,va,tb):
    """
    This function re-defines error reporting

    `tp` is the exception type
    `va` is the exception parameter
    `tb` is the traceback object, which encapsulates
        the call stack at the point
        where the exception originally occurred
    
    """
    # The API module names need to be augmented
    # with all other modules in GTC, as an error
    # may arise anywhere. `code` is the Python
    # module that provides the interpreter. `gtc`
    # is the module in which scripts are executed
    # so neither of these are accessible.

    modules = submodules + (
        'context',
        'lib',
        'LU',
        'uncertain_array',
        'persistence',
        'named_tuples',
        'node',
        'vector'
        # , 'cholesky','svd'
    )
    # These `outer_modules` provide the top level calling
    # context, which we need to remove.
    outer_modules = ('code','gtc')
    
    # Need to step through the traceback chain
    # until something in the GTC libraries is
    # found. The source for these is unavailable
    # to users, so we do not report beyond that.
    
    # `depth` will be set to avoid inaccessible
    # GTC modules
    outer = 0
    depth = 0
    t = tb
    while True: 
        name = os.path.splitext(
            os.path.basename(t.tb_frame.f_code.co_filename)
        )[0]
        
        if name in outer_modules: outer += 1
        if name in modules: break
        
        depth += 1
            
        if t.tb_next is not None:   
            t = t.tb_next
        else:
            break

    tb_text = traceback.format_exception(tp,va,tb,depth)

    # The first line is just the intro: `Traceback (most recent call last):`
    print(tb_text[0], file=sys.stderr) 
    
    # Now skip any reference to the outer modules and also
    # skip any reference to GTC modules
    for l in tb_text[1+outer:]: 
        print(l, file=sys.stderr)

# This will catch exceptions raised 
# during script files execution
sys.excepthook = my_excepthook

#-----------------------------------------------------------------------------------------------
class Console(code.InteractiveConsole):
    
    """
    A subclass of code.InteractiveConsole is needed
    to control the way that exceptions are handled
    when the calculator is in interactive mode.
    """
    
    def __init__(self,locals=None):
        code.InteractiveConsole.__init__(self,locals=locals)

    def _preamble(self):
        """
        Execute lines of code before running the interpreter
        
        """
        # A Python 2.7 legacy: remove  
        # assert False == self.push("from __future__ import division")
        
        # If something was left over, this discards it.
        self.resetbuffer()
        
    def start(self,banner=None):
        self._preamble()
        if banner is None:
            self.interact()
        else:
            self.interact(banner)

    def showtraceback(self):
        # This is called for uncaught exceptions
        my_excepthook( *sys.exc_info() )
            
#-------------------------------------------------------
gtc_version = "%%prog v{!s}".format(version)
parser = OptionParser(
    usage="%prog [-i|--interact] [-p|--plain] [script1 script2 ...]",
    version=gtc_version
)
parser.add_option(
    "-i",
    "--interact",
    action="store_true",
    dest="interact",
    help="enter interactive mode after executing any scripts"
)
parser.add_option(
    "-p",
    "--plain",
    action="store_true",
    dest="plain",
    help="no banner output at the start of interactive mode"
)
parser.set_defaults(interact=False)

(options, args) = parser.parse_args()

try:
    script_paths = os.environ['GTC_SCRIPTS'].split(';')
except KeyError:
    script_paths = []

#-------------------------------------------------------
# Execute any positional arguments as scripts
#
for n in args:
    try:
        exec( open( n ).read() )
    except IOError:
        for p in script_paths:
            f = os.path.join(p,n)
            if os.path.isfile(f):
                exec( open( f ).read() )
                break    
        else:   # no break, loop exhausted
            raise    
            
#-------------------------------------------------------
# Remain in the interpreter if requested or if no files
# are provided on the command line
#
if options.interact or len(args) == 0:  
    if len(args) != 0:
        # There are options AND input files
        Console(locals=globals()).start("") 
    elif options.plain:
        # Create the console 
        Console(locals=globals()).start("")    
    else:
        banner="""
                === GUM Tree Calculator Console ({!s}) ===
                
For help, type "help(topic)". To close the window, type "quit()" or CTRL-Z. 
""".format(version)
        # Create the console 
        Console(locals=globals()).start(banner)
        

    