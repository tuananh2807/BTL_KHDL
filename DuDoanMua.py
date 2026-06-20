import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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
# Tạo nhãn mưa ngày mai
# =====================================

df["RainTomorrow"] = (
    df["Rainfall"]
    .shift(-1)
    .apply(lambda x: 1 if x > 0 else 0)
)

# Xóa dữ liệu rỗng
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

y = df["RainTomorrow"]

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
# Huấn luyện Random Forest
# =====================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# =====================================
# Đánh giá mô hình
# =====================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)

# =====================================
# Dự đoán ngày mai
# =====================================

last_day = X.iloc[[-1]]

prediction = model.predict(
    last_day
)

# =====================================
# Hiển thị kết quả
# =====================================

print("=" * 50)
print("DỰ ĐOÁN MƯA NGÀY MAI")
print("=" * 50)

if prediction[0] == 1:
    print("Kết quả: Có mưa")
else:
    print("Kết quả: Không mưa")

print(
    f"Độ chính xác: {accuracy:.4f}"
)