import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# =====================================
# Đọc dữ liệu
# =====================================

df = pd.read_csv(
    "DuLieu/weather.csv",
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

# Chuyển đổi ngày tháng
df["Date"] = pd.to_datetime(df["Date"])

# =====================================
# Tạo nhiệt độ ngày tiếp theo
# =====================================

df["TempTomorrow"] = df["TempMean"].shift(-1)

# Xóa dòng cuối bị NaN
df = df.dropna()

# =====================================
# Dữ liệu đầu vào
# =====================================

X = df[
    [
        "TempMean",
        "TempMax",
        "TempMin",
        "Rainfall"
    ]
]

# =====================================
# Dữ liệu đầu ra
# =====================================

y = df["TempTomorrow"]

# =====================================
# Chia dữ liệu
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================
# Huấn luyện mô hình
# =====================================

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

# =====================================
# Dự đoán
# =====================================

last_day = X.iloc[[-1]]

prediction = model.predict(last_day)

# =====================================
# Hiển thị kết quả
# =====================================

print("=" * 50)
print("DỰ ĐOÁN NHIỆT ĐỘ NGÀY MAI")
print("=" * 50)

print(
    f"Nhiệt độ trung bình dự đoán: "
    f"{prediction[0]:.2f} °C"
)

score = model.score(X_test, y_test)

print(
    f"Độ chính xác R²: "
    f"{score:.4f}"
)