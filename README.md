# rosbag_reader

generate rosbag files:

http://wiki.ros.org/rosbag/Tutorials/Recording%20and%20playing%20back%20data

Husky:

http://wiki.ros.org/Robots/Husky

```cd catkin_ws/src```

```git clone https://github.com/husky/husky.git```

start simulation:


```
cd catkin_ws
catkin_make
source devel/setup.bash
```

launch only the robot in an empty gazebo world

```roslaunch husky_gazebo husky_empty_world.launch```

launch robot in environment clearpath_playpen:

```roslaunch husky_gazebo husky_playpen.launch```

open a second terminal and run the following commands:

```
cd catkin_ws/src
mkdir bagfiles
cd catkin_ws/src/bagfiles
rosbag record -a
```

1. recording data (creating a bag file):


Terminal1:
```roscore```

Terminal2:
```rosrun turtlesim turtlesim_node```

Terminal3:
```rosrun turtlesim turtle_teleop_key```


Terminal4:
```
cd catkin_ws/src
mkdir bagfiles
cd catkin_ws/src/bagfiles
rosbag record -a
```

optional:

Terminal5:

```rostopic list -v```

```
Published topics:
 * /turtle1/color_sensor [turtlesim/Color] 1 publisher
 * /turtle1/cmd_vel [geometry_msgs/Twist] 1 publisher
 * /rosout [rosgraph_msgs/Log] 2 publishers
 * /rosout_agg [rosgraph_msgs/Log] 1 publisher
 * /turtle1/pose [turtlesim/Pose] 1 publisher

Subscribed topics:
 * /turtle1/cmd_vel [geometry_msgs/Twist] 1 subscriber
 * /rosout [rosgraph_msgs/Log] 1 subscriber
```

2. Recording a subset of the data

```rosbag record -O subset /turtle1/cmd_vel /turtle1/pose```


```
path:        subset.bag
version:     2.0
duration:    12.6s
start:       Dec 10 2014 20:20:49.45 (1418271649.45)
end:         Dec 10 2014 20:21:02.07 (1418271662.07)
size:        68.3 KB
messages:    813
compression: none [1/1 chunks]
types:       geometry_msgs/Twist [9f195f881246fdfa2798d1d3eebca84a]
             turtlesim/Pose      [863b248d5016ca62ea2e895ae5265cf9]
topics:      /turtle1/cmd_vel    23 msgs    : geometry_msgs/Twist
             /turtle1/pose      790 msgs    : turtlesim/Pose
```


3. Examining and playing the bag file

```rosbag info <your bagfile>```

```rosbag play <your bagfile>```

subset of data:

```rosbag info <your subset.bag>```

```rosbag play <your subset.bag>```




