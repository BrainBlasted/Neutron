import importlib
import inspect
import zone
from .module_base import ModuleBase
from .utils import injector, show_notification

has_run_setup = False
module_count = 0


def show_initial_notification(core):
    text = 'Neutron Core has been loaded successfully.'
    text += '\n{} modules loaded.'.format(len(core.modules))
    for module in core.modules:
        text += '\n\u2022 {}'.format(module.full_name)
    show_notification(text)


# Hooks into the game process after the initial loading screen
# to set up game alarms.
@injector(zone.Zone, 'on_loading_screen_animation_finished')
def inject_initial_setup(original, self, *args, **kwargs):
    global has_run_setup
    result = original(self, *args, **kwargs)

    if not has_run_setup:
        # try:
        core = NeutronCore()
        core.run_initial_setup()
        show_initial_notification(core)
        has_run_setup = True
        # except:
        #     pass
    return result


class NeutronCore:
    def __init__(self):
        self._module_names = [
            'neutron_friendships'
        ]
        self._modules = []

    @property
    def modules(self):
        return self._modules

    def run_initial_setup(self):
        for name in self._module_names:
            try:
                py_module = importlib.import_module('{}.module'.format(name))
                for x in dir(py_module):
                    obj = getattr(py_module, x)

                    if inspect.isclass(obj) and issubclass(obj, ModuleBase) and obj is not ModuleBase:
                        module = obj()
                        self._modules += [module]
            except ImportError:
                pass

        for module in self._modules:
            module.initialize_alarms()
