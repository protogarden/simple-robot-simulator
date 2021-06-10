# simple-robot-simulator

A simple robot simulator for testing various algorithms. 

There are lots of decent robot simulators available such as webots and gazebo. Those can be tedious to setup. The aim of simple robot simulator is to not provide the most accurate physics representation of a robot, but rather just a quick way to test various robotics algorithms and ideas. If your algorithm doesn't work in this simulator then it won't work in the more advanced ones. 

The simulator aims to provide basic interface where you can control the robot from your python script and get data back from various sensors (Currently basic odometry, lidar data and a camera)

This is still a work in progress, but feature requests are welcome

- Free Software: MIT License

## Installation

Simulator Binaries Available: https://github.com/protogarden/simple-robot-simulator/releases

Clone this repo for python core and code examples:

```shell
git clone https://github.com/protogarden/simple-robot-simulator.git
```

## Example Usage

Basic simulator connection example:

```python
import time
from core.robot_controller import RobotController

rb = RobotController('localhost', 5005)

while True:
    rb.send_cmd_vel(1.5,0)
    time.sleep(1)
```

## Code Examples

| Filename | Description | Dependencies |
|----------|-------------|--------------|
| ex_remote_control.py | Remote control the robot with arrow keys | pygame |
| ex_odometry.py | Example to retrieve robot odometry data | pygame |
| ex_lidar.py | Example to retrieve robot lidar data  | pygame |
| ex_camera.py | Example to retrieve robot camera images | pygame |
| ex_opencv.py | Example to retrieve robot camera images for opencv processing | opencv |


## Roadmap

These items are on the todo, but no timelines available:

:x: Custom Scenes

:x: Slightly more/better physics on robot

:x: More visualizations in simulator

:x: Various code examples of popular algorithms

## Credits

Python/Unity Communication Code used from the following two projects

Tawn Kramer - <https://github.com/tawnkramer/gym-donkeycar>

Tawn Kramer - <https://github.com/tawnkramer/sdsandbox>
