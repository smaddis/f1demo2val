import fastf1 as f1

import pandas as pd

f1.Cache.enable_cache('./cache')  
monza = f1.get_session(2021, 'Monza', 'R') # Pick Monza 2021 race 

laps = monza.load_laps(True) # Load laps with telemetry
driver_data = laps.pick_driver('BOT').get_car_data().add_distance() # Get Bottas car data
driver_pos = laps.pick_driver('BOT').get_pos_data() # Get Bottas position data


driver_data_ip = driver_data.merge_channels(driver_pos) # Merge car data and position data 
dataFrame = pd.DataFrame(driver_data_ip)
dataFrame.to_csv("Bottas_Monza2021Race.csv") # Output to csv

