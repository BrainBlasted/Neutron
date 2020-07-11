import random
import services
from functools import wraps
from sims4.localization import LocalizationHelperTuning
from ui.ui_dialog_notification import UiDialogNotification


def injector(target_object, target_function_name):
    def inject(target_function, new_function):
        @wraps(target_function)
        def _inject(*args, **kwargs):
            return new_function(target_function, *args, **kwargs)

        return _inject

    def _inject_to(new_function):
        target_function = getattr(target_object, target_function_name)
        setattr(target_object, target_function_name, inject(target_function, new_function))
        return new_function

    return _inject_to


def run_once(f):
    def wrapper(*args, **kwargs):
        wrapper.has_run = True
        return f(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


def show_notification(text, title=None):
    client = services.client_manager().get_first_client()
    if title is None:
        title = 'Neutron Core'

    localized_title = lambda **_: LocalizationHelperTuning.get_raw_text(title)
    localized_text = lambda **_: LocalizationHelperTuning.get_raw_text(text)

    notification = UiDialogNotification.TunableFactory().default(
        client.active_sim,
        text=localized_text,
        title=localized_title
    )
    notification.show_dialog()


def probability_check(probability_percentage):
    return (random.random() * 100) >= probability_percentage
