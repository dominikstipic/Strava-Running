import src.strava_data as strava
import pandas as pd

data = strava.process()
df = pd.DataFrame(data)

DF = df[['name', 'distance', 'moving_time', 'elapsed_time','total_elevation_gain', 
'type', 'sport_type', 'start_date_local','map', 'start_latlng', 'end_latlng',
'average_speed', 'max_speed', 'elev_high', 'elev_low']]

DF = DF.sort_values("start_date_local", ascending=False)
DF["start_date_local"] = DF["start_date_local"].apply(lambda x:x.strftime("%d-%m-%Y %H:%M"))
DF["start_lat"] = DF["start_latlng"].map(lambda x : x[0] if len(x) > 0 else None)
DF["start_lng"] = DF["start_latlng"].map(lambda x : x[1] if len(x) > 0 else None)
DF["end_lat"] = DF["end_latlng"].map(lambda x : x[0] if len(x) > 0 else None)
DF["end_lng"] = DF["end_latlng"].map(lambda x : x[1] if len(x) > 0 else None)
del DF["start_latlng"]
del DF["end_latlng"]

DF.to_excel("data.xlsx", index=False)
