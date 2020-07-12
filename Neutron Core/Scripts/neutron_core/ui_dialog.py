import services
import traceback
import os
from .utils import ParametrizedLocalizedString
from sims4.localization import LocalizationHelperTuning, _create_localized_string
from ui.ui_dialog import ButtonType, UiDialog, UiDialogResponse


class UiDialogChoices(UiDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._choice_responses = list()

    def _get_responses_gen(self):
        # yield old values:
        super_results = list(super()._get_responses_gen())
        for result in super_results:
            yield result
        # yield our choices:
        for response in self._choice_responses:
            yield response


# Creates, initializes and displays the choice dialog
def display_choices(choices, choice_callback, text: ParametrizedLocalizedString = None, title: ParametrizedLocalizedString = None, cancel: ParametrizedLocalizedString = None):
    try:
        client = services.client_manager().get_first_client()

        # Instantiates the dialog with the supplied title and text
        dlg = UiDialogChoices.TunableFactory().default(client.active_sim, text=text.localized_string, title=title.localized_string)

        # Creates a localized string for each choice contained within the dialog
        labels = [lambda choice=choice: _create_localized_string(choice) for choice in choices]
        for idx, choice in enumerate(choices):
            dlg._choice_responses.append(UiDialogResponse(dialog_response_id=idx, text=labels[idx], ui_request=UiDialogResponse.UiDialogUiRequest.NO_REQUEST))

        # Standard EA cancel choice
        dlg._choice_responses.append(UiDialogResponse(dialog_response_id=ButtonType.DIALOG_RESPONSE_CANCEL, text=cancel.localized_string, ui_request=UiDialogResponse.UiDialogUiRequest.NO_REQUEST))
    except Exception as e:
        raise e

    # Handles the callback response of the dialog
    def choice_response_callback(dialog):
        try:
            choice_callback(dialog.response)
        except Exception as e:
            raise e

    # Sets the dialog as the active one and displays it
    dlg.add_listener(choice_response_callback)
    dlg_service = services.ui_dialog_service()
    dlg_service._active_dialogs[dlg.dialog_id] = dlg
    dlg.show_dialog()
