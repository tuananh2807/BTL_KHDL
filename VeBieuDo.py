import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv("DuLieu/weather.csv")

# Chuyển kiểu ngày
df["Date"] = pd.to_datetime(df["Date"])

# Tạo cột năm và tháng
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

# ==========================================
# 1. Nhiệt độ trung bình theo tháng
# ==========================================

temp_month = df.groupby("Month")["TempMean"].mean()

plt.figure(figsize=(10,5))
plt.plot(temp_month.index, temp_month.values, marker="o")
plt.title("Nhiệt độ trung bình theo tháng")
plt.xlabel("Tháng")
plt.ylabel("Nhiệt độ (°C)")
plt.grid(True)

plt.savefig("TaiNguyen/nhiet_do_trung_binh_thang.png")
plt.close()

# ==========================================
# 2. Tháng nóng nhất từng năm
# ==========================================

hot_months = []
years = []

temp_year_month = df.groupby(["Year","Month"])["TempMean"].mean()

for year in sorted(df["Year"].unique()):

    hottest_month = temp_year_month[year].idxmax()

    years.append(year)
    hot_months.append(hottest_month)

plt.figure(figsize=(10,5))
plt.bar(years, hot_months)

plt.title("Tháng nóng nhất từng năm")
plt.xlabel("Năm")
plt.ylabel("Tháng")

plt.savefig("TaiNguyen/thang_nong_nhat.png")
plt.close()

# ==========================================
# 3. Tháng lạnh nhất từng năm
# ==========================================

cold_months = []

for year in sorted(df["Year"].unique()):

    coldest_month = temp_year_month[year].idxmin()

    cold_months.append(coldest_month)

plt.figure(figsize=(10,5))
plt.bar(years, cold_months)

plt.title("Tháng lạnh nhất từng năm")
plt.xlabel("Năm")
plt.ylabel("Tháng")

plt.savefig("TaiNguyen/thang_lanh_nhat.png")
plt.close()

# ==========================================
# 4. Tháng mưa nhiều nhất từng năm
# ==========================================

rain_year_month = df.groupby(["Year","Month"])["Rainfall"].sum()

rainiest_months = []

for year in sorted(df["Year"].unique()):

    rainiest_month = rain_year_month[year].idxmax()

    rainiest_months.append(rainiest_month)

plt.figure(figsize=(10,5))
plt.bar(years, rainiest_months)

plt.title("Tháng mưa nhiều nhất từng năm")
plt.xlabel("Năm")
plt.ylabel("Tháng")

plt.savefig("TaiNguyen/thang_mua_nhieu_nhat.png")
plt.close()

# ==========================================
# 5. Tháng mưa ít nhất từng năm
# ==========================================

driest_months = []

for year in sorted(df["Year"].unique()):

    driest_month = rain_year_month[year].idxmin()

    driest_months.append(driest_month)

plt.figure(figsize=(10,5))
plt.bar(years, driest_months)

plt.title("Tháng mưa ít nhất từng năm")
plt.xlabel("Năm")
plt.ylabel("Tháng")

plt.savefig("TaiNguyen/thang_mua_it_nhat.png")
plt.close()

print("Đã tạo 5 biểu đồ trong thư mục TaiNguyen")