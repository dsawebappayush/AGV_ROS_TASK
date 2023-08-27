import rosbag
import yaml
import numpy as np

bag_path = '/home/pc/dummy/src/packs/bagfiles/2023-08-27-10-33-19.bag'
output_yaml_path = '/home/pc/dummy/src/packs/bagfiles/output_data_noise.yaml'

data_to_save = []

mean = 0.0  # Mean of the Gaussian distribution
std_dev_linear = 0.1  # Standard deviation for linear velocity noise
std_dev_angular = 0.05  # Standard deviation for angular velocity noise

data_to_save = []

with rosbag.Bag(bag_path, 'r') as bag:
    for topic, msg, t in bag.read_messages(topics=['/cmd_vel']):
        # Extract linear and angular velocities
        linear_x = msg.linear.x
        angular_z = msg.angular.z
        
        # Add Gaussian noise to velocities
        noisy_linear_x = linear_x + np.random.normal(mean, std_dev_linear)
        noisy_angular_z = angular_z + np.random.normal(mean, std_dev_angular)
        
        data_entry = {
            'timestamp': t.to_sec(),
            'noisy_linear_velocity': noisy_linear_x,
            'noisy_angular_velocity': noisy_angular_z
        }
        data_to_save.append(data_entry)
