from flask import Flask, render_template
import pandas as pd
import os

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier

# ===================================
# KHAI BÁO FLASK
# ===================================

app = Flask(
    __name__,
    template_folder="GiaoDien",
    static_folder="TaiNguyen"
)

# ===================================
# ĐỌC FILE CSV
# ===================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(
    BASE_DIR,
    "DuLieu",
    "weather.csv"
)

# CSV Open-Meteo có 3 dòng metadata đầu
df = pd.read_csv(
    csv_path,
    skiprows=3
)

# Đổi tên cột
df.columns = [
    "Date",
    "Rainfall",
    "TempMax",
    "TempMin",
    "TempMean"
]

# Chuyển kiểu dữ liệu
df["Date"] = pd.to_datetime(df["Date"])

# ===================================
# DỰ ĐOÁN NHIỆT ĐỘ
# ===================================

df["Ngay"] = range(len(df))

X = df[["Ngay"]]
y = df["TempMean"]

model_temp = LinearRegression()

model_temp.fit(X, y)

du_doan_nhiet_do = round(
    model_temp.predict(
        pd.DataFrame(
            {"Ngay": [len(df)]}
        )
    )[0],
    2
)

# ===================================
# DỰ ĐOÁN MƯA
# ===================================

df["CoMua"] = (
    df["Rainfall"] > 0
).astype(int)

X_rain = df[
    [
        "TempMean",
        "TempMax",
        "TempMin"
    ]
]

y_rain = df["CoMua"]

model_rain = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model_rain.fit(
    X_rain,
    y_rain
)

ket_qua_mua = model_rain.predict(
    X_rain.iloc[-1:]
)[0]

du_doan_mua = (
    "Có mưa"
    if ket_qua_mua == 1
    else "Không mưa"
)

# ===================================
# THỐNG KÊ
# ===================================

nhiet_do_tb = round(
    df["TempMean"].mean(),
    2
)

nhiet_do_cao_nhat = round(
    df["TempMax"].max(),
    2
)

nhiet_do_thap_nhat = round(
    df["TempMin"].min(),
    2
)

tong_luong_mua = round(
    df["Rainfall"].sum(),
    2
)

# ===================================
# ROUTE
# ===================================

@app.route("/")
def trang_chu():

    return render_template(
        "index.html",
        nhiet_do=du_doan_nhiet_do,
        mua=du_doan_mua
    )

@app.route("/phan-tich")
def phan_tich():

    return render_template(
        "phan_tich.html",
        nhiet_do_tb=nhiet_do_tb,
        nhiet_do_cao_nhat=nhiet_do_cao_nhat,
        nhiet_do_thap_nhat=nhiet_do_thap_nhat,
        tong_luong_mua=tong_luong_mua
    )

@app.route("/du-doan-nhiet-do")
def du_doan_nhiet_do_page():

    return render_template(
        "du_doan_nhiet_do.html",
        nhiet_do=du_doan_nhiet_do
    )

@app.route("/du-doan-mua")
def du_doan_mua_page():

    return render_template(
        "du_doan_mua.html",
        mua=du_doan_mua
    )

# ===================================
# CHẠY CHƯƠNG TRÌNH
# ===================================

if __name__ == "__main__":

    print("\n===== KIỂM TRA DỮ LIỆU =====")

    print(df.head())

    print("\nCột dữ liệu:")

    print(df.columns)

    print("\nTổng số bản ghi:")

    print(len(df))

    app.run(
        debug=True
    )