import requests
import pandas as pd

url = (
    "https://archive-api.open-meteo.com/v1/archive?"
    "latitude=21.5942"
    "&longitude=105.8482"
    "&start_date=2021-06-20"
    "&end_date=2026-06-20"
    "&daily=temperature_2m_mean,"
    "temperature_2m_max,"
    "temperature_2m_min,"
    "precipitation_sum"
    "&timezone=Asia%2FBangkok"
)

response = requests.get(url)
data = response.json()

df = pd.DataFrame({
    "Date": data["daily"]["time"],
    "TempMean": data["daily"]["temperature_2m_mean"],
    "TempMax": data["daily"]["temperature_2m_max"],
    "TempMin": data["daily"]["temperature_2m_min"],
    "Rainfall": data["daily"]["precipitation_sum"]
})

df.to_csv("DuLieu/weather.csv", index=False)

print("Đã tải thành công!")
print(df.head())
print(f"\nSố dòng dữ liệu: {len(df)}")