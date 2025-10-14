Clone and build the packages: 

colcon build --packages-select simple_threshold_monitor --symlink-install
source install/setup.bash

Run: 

ros2 launch simple_threshold_monitor launch.py
