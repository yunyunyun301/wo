import requests
import json
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 26.05942,
    "longitude": 119.198,
    "start_date": "2025-01-01",
    "end_date": "2025-01-31",
    "hourly": [
        "temperature_2m",
        "relative_humidity_2m",
        "apparent_temperature",
        "precipitation",
        "weather_code",
        "cloudcover",
        "wind_speed_10m",
        "wind_direction_10m",
        "shortwave_radiation_instant",
        "is_day",
    ],
    "daily": [
        "temperature_2m_mean",
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "sunshine_duration",
    ],
    "timezone": "auto",
}
response = requests.get(url, params=params)
if response.status_code == 200:
    with open ("weather_data.json", "w") as f:
        json.dump(response.json(), f, indent=4)#用json.dump()函数将响应数据写入文件，并使用indent参数进行格式化，indent=4表示每个层级缩进4个空格，使得输出的JSON数据更易读。