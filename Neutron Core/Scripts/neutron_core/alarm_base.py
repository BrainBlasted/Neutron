import alarms

global handle


# Base class used to set up alarm classes in other modules
class AlarmBase:
    def __init__(self, interval):
        global handle
        handle = alarms.add_alarm(self, interval, self.alarm_callback)

    def alarm_callback(self, handle):
        pass

    def reset_handle(self, interval):
        global handle
        handle = alarms.add_alarm(self, interval, self.alarm_callback)
