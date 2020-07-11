class ModuleBase:
    @property
    def full_name(self):
        return self._full_name

    @property
    def alarms(self):
        return self._alarms

    def load_module(self):
        self.initialize_alarms()

    def initialize_alarms(self):
        return
