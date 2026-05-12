from csvtomelog import (MelogConverter)
import pandas as pd

# Sample data
data = {'timestamp': [1, 2, 3], 'joint_id': [2, 2, 2], 'angle': [45, 90, 0], 'motor_status': [0, 8, 0], 'sensor_feedback': [7, 7, 4]}
df = pd.DataFrame(data)
mapping = {1: 'timestamp', 2: 'joint_id', 3: 'angle', 4: 'motor_status', 6: 'sensor_feedback'}
converter = MelogConverter(domain="ROBOTICS")

for index, row in df.iterrows():
    linear, phonetic = converter.convert_row(row, mapping, roles={2: '^', 6: '_'})