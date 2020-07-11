import clock
import services
import sims4
from neutron_core import utils, relationships
from neutron_core.alarm_base import AlarmBase
from neutron_core.module_base import ModuleBase
from relationships.relationship_track import RelationshipTrack

alarm = None
processed_friendships = set()


class FriendshipAlarm(AlarmBase):
    def alarm_callback(self, handle):
        utils.show_notification("Running relationship alarms...")
        self.progress_world_friendships()
        now = services.time_service().sim_now
        interval = clock.time_until_hour_of_day(now, 0)
        self.reset_handle(interval)

    def progress_world_friendships(self):
        global processed_friendships
        for sim_info in services.sim_info_manager().get_all():
            if sim_info.is_npc:
                self.progress_current_friendships(sim_info)

        # Clear for next pass
        processed_friendships.clear()
        utils.show_notification("Ran relationship alarms...")

    def progress_current_friendships(self, sim_info):
        global processed_friendships
        rels = relationships.get_relationships(sim_info)
        if rels is not None:
            for relationship in rels:
                # TODO: For each relationship, check shared traits,
                # shared skills, and shared "status" (fame, wealth).
                # In addition, check incompatible traits, if sims
                # in the relationship have "bad" traits, etc.
                #
                # Once that is checked, weigh all factors and come up
                # with whether a relationship will gain or lose points.
                target_sim_info = relationship[1]
                if not (target_sim_info.sim_id in processed_friendships):
                    self.progress_friendship(sim_info, target_sim_info)

        processed_friendships.add(sim_info.sim_id)

    def progress_friendship(self, sim_info, target_sim_info):
        relationship_service = services.relationship_service()
        # TODO: Actually run processing here
        relationship_service.add_relationship_score(sim_info.sim_id, target_sim_info.sim_id, 25,
                                                    track=RelationshipTrack.FRIENDSHIP_TRACK)


class NeutronFriendshipsModule(ModuleBase):
    def __init__(self):
        self._full_name = 'Neutron Friendships'

    def initialize_alarms(self):
        global alarm
        now = services.time_service().sim_now
        interval = clock.time_until_hour_of_day(now, 0)
        alarm = FriendshipAlarm(interval)
