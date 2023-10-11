import pandas as pd

import src.scoring as scoring

def score_timeseries(data):
    date_score = {"date": [], "score": []}
    for d in data:
        date = d["start_date"]
        score = scoring.activity_effort_score(d, scoring.WEIGHTS)
        date_score["date"].append(date)
        date_score["score"].append(score)
    df = pd.DataFrame.from_dict(date_score)
    return df