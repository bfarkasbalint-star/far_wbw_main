A package két node-ból áll. A `/random_publisher`1 Hz frekvenciával véletlenszámot generál (0–100 tartományban) és elküldi egy topicra `/random_value`. A `/threshold_subscriber` feliratkozik a `/random_value` topicra, és ellenőrzi, hogy az érték meghaladja-e a küszöbértéket (pl. 50). Ha igen → „Threshold exceeded”, ha nem → „OK”.

# `ros2_py_template` package
ROS 2 python package.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)
## Packages and build

It is assumed that the workspace is `~/ros2_ws/`.

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
 git clone https://github.com/bfarkasbalint-star/far_wbw_mai
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

### Node-topic kapcsolat

```mermaid
graph LR
    A[random_publisher] -->|/random_value| B[threshold_subscriber]
