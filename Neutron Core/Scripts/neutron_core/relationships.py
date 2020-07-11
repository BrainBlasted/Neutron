import services
from relationships.relationship_track import RelationshipTrack


def get_relationships(sim_info):
    valid_relationships = []
    for relationship in sim_info.relationship_tracker:
        target_sim_info = relationship.get_other_sim_info(sim_info.sim_id)
        if target_sim_info is not None:
            valid_relationships.append((sim_info, target_sim_info))

    return valid_relationships


def get_romantic_relationships(sim_info):
    valid_relationships = []
    for relationship in get_relationships(sim_info):
        target_sim_info = relationship.get_other_sim_info(sim_info.sim_id)
        # Any romantic relationship with a score other than zero is valid
        if target_sim_info is not None and sim_info.relationship_tracker.get_relationship_score(
                target_sim_info.sim_id,
                track=RelationshipTrack.ROMANCE_TRACK
        ) != 0:
            valid_relationships.append((sim_info, target_sim_info))

    return valid_relationships
