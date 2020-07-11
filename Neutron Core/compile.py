from Utilities import compile_module
from settings import *

root = os.path.dirname(os.path.realpath('__file__'))
compile_module(creator_name, root, mods_folder, mod_name='neutron_core', use_creator_name=False)
