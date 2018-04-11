import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

# Gazebo
# ----------------------------------------

# Example envs
register(
    id='GazeboBox-v0',
    entry_point='gym_gazebo_boilerplate.envs.box:GazeboBox',
    # More arguments here
)