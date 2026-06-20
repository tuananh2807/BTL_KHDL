import pandas as pd

# ==========================
# Đọc dữ liệu
# ==========================

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

# Tạo cột năm và tháng
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

# ==================================================
# 1. Nhiệt độ trung bình theo tháng
# ==================================================

print("=" * 60)
print("NHIỆT ĐỘ TRUNG BÌNH THEO THÁNG")
print("=" * 60)

temp_month = df.groupby("Month")["TempMean"].mean()

for month, temp in temp_month.items():
    print(f"Tháng {month}: {temp:.2f}°C")

# ==================================================
# 2. Tháng nóng nhất trong từng năm
# ==================================================

print("\n")
print("=" * 60)
print("THÁNG NÓNG NHẤT TRONG TỪNG NĂM")
print("=" * 60)

temp_year_month = df.groupby(["Year", "Month"])["TempMean"].mean()

for year in sorted(df["Year"].unique()):

    hottest_month = temp_year_month[year].idxmax()
    hottest_temp = temp_year_month[year].max()

    print(
        f"Năm {year}: "
        f"Tháng {hottest_month} "
        f"({hottest_temp:.2f}°C)"
    )

# ==================================================
# 3. Tháng lạnh nhất trong từng năm
# ==================================================

print("\n")
print("=" * 60)
print("THÁNG LẠNH NHẤT TRONG TỪNG NĂM")
print("=" * 60)

for year in sorted(df["Year"].unique()):

    coldest_month = temp_year_month[year].idxmin()
    coldest_temp = temp_year_month[year].min()

    print(
        f"Năm {year}: "
        f"Tháng {coldest_month} "
        f"({coldest_temp:.2f}°C)"
    )

# ==================================================
# 4. Tháng mưa nhiều nhất trong từng năm
# ==================================================

print("\n")
print("=" * 60)
print("THÁNG MƯA NHIỀU NHẤT TRONG TỪNG NĂM")
print("=" * 60)

rain_year_month = df.groupby(["Year", "Month"])["Rainfall"].sum()

for year in sorted(df["Year"].unique()):

    rainiest_month = rain_year_month[year].idxmax()
    rainiest_value = rain_year_month[year].max()

    print(
        f"Năm {year}: "
        f"Tháng {rainiest_month} "
        f"({rainiest_value:.2f} mm)"
    )

# ==================================================
# 5. Tháng mưa ít nhất trong từng năm
# ==================================================

print("\n")
print("=" * 60)
print("THÁNG MƯA ÍT NHẤT TRONG TỪNG NĂM")
print("=" * 60)

for year in sorted(df["Year"].unique()):

    driest_month = rain_year_month[year].idxmin()
    driest_value = rain_year_month[year].min()

    print(
        f"Năm {year}: "
        f"Tháng {driest_month} "
        f"({driest_value:.2f} mm)"
    )

print("\n")
print("=" * 60)
print("PHÂN TÍCH DỮ LIỆU HOÀN THÀNH")
print("=" * 60)