#!/usr/bin/env python

import rospy
import yaml
from std_msgs.msg import Float32
rospy.init_node('yaml_publisher_node')
pub = rospy.Publisher('/noise_vel', Float32, queue_size=10)
rate = rospy.Rate(10)  # Publish rate in Hz
yaml_file_path = '/home/pc/dummy/src/packs/bagfiles/output_data_noise.yaml'
with open(yaml_file_path, 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)
while not rospy.is_shutdown():
    for data_entry in yaml_data:
        linear_velocity = data_entry['noisy_linear_velocity']
        angular_velocity = data_entry['noisy_angular_velocity']
        
        # Publish linear and angular velocities as separate Float32 messages
        pub.publish(linear_velocity)
        rospy.sleep(0.1)  # Adjust sleep duration as needed
        pub.publish(angular_velocity)
        rospy.sleep(0.1)  # Adjust sleep duration as needed
        
        rate.sleep()
