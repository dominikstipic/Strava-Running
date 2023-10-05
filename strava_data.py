import requests

def request_access_token(refresh_token):
    auth_url = "https://www.strava.com/oauth/token"
    payload = {
        'client_id': "114681",
        'client_secret': "1ed90905e8141438f4335fc329922499e350e6c9",
        'refresh_token': refresh_token,
        'grant_type': "refresh_token"
    }
    res = requests.post(auth_url, data=payload, verify=True)
    access_token = res.json()['access_token']
    return access_token

def fetch_data(access_token):
    activities_url = "https://www.strava.com/api/v3/athlete/activities"
    header = {"Authorization": "Bearer " + access_token}
    param = {'per_page': 200, 'page': 1}
    my_dataset = requests.get(activities_url, headers=header, params=param).json()
    return my_dataset

def process():
    refresh_token = "6daa102959f3408428794d19e99ca360cb24c44a"
    access_token = request_access_token(refresh_token)
    data = fetch_data(access_token)
    return data

if __name__ == "__main__":
    data = process()
    print(data)