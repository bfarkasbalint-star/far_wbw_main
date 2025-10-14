Clone and build the packages: 

colcon build --packages-select simple_threshold_monitor --symlink-install
source install/setup.bash

Run: 

ros2 launch simple_threshold_monitor launch.py

# `ros2_py_template` package
ROS 2 python package.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)
## Packages and build

It is assumed that the workspace is `~/ros2_ws/`.

### Clone the packages
``` r
git clone https://github.com/bfarkasbalint-star/far_wbw_main
```
``` r
 cd ~/ros2_ws/far_wbw_main
```

### Build ROS 2 packages

``` r
colcon build --packages-select simple_threshold_monitor --symlink-install
```

``` bash
source install/setup.bash
```

``` r
ros2 launch simple_threshold_monitor launch.py
```
