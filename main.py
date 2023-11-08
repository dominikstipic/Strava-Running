import src.strava_data as strava
import pandas as pd

data = strava.process()
df = pd.DataFrame(data)

DF = df[['name', 'distance', 'moving_time', 'elapsed_time','total_elevation_gain', 
'type', 'sport_type', 'start_date_local','map', 'trainer', 'start_latlng', 'end_latlng',
'average_speed', 'max_speed', 'elev_high', 'elev_low']]

DF = DF.sort_values("start_date_local")
DF["start_date_local"] = DF["start_date_local"].apply(lambda x:x.strftime("%d-%m-%Y %H:%M"))
DF.to_excel("data.xlsx")
