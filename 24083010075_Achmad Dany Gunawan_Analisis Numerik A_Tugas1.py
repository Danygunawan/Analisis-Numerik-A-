# nama: Achmad Dany Gunawan
# NPM: 24083010075

# tugas:
# hitung volume produksi yang menghasilkan kentungan maksimum 
#    (pendapatan dari penjualan dikurangi produksi)
#----------------------------------------------------------------#

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm

# range harga jual
x = np.linspace(3000, 10000, 500)

# rescale parameters
a = 6
loc = 3.5 * 1000
scale = 1.5 * 1000

# probability density (permintaan)
y = skewnorm.pdf(x, a=a, loc=loc, scale=scale) * 1000
np.random.seed(75)
y = y + np.random.normal(0, 0.005, size=x.shape)
y = y * 1000

# produksi (supply)
produksi_y = np.linspace(0, 1000, len(x))  # jumlah produksi
produksi_z = np.linspace(3000, 2000, len(x)) + np.random.normal(0, 0.1, size=x.shape) * 100

# revenue = harga jual * jumlah
revenue = x * y

# cost = harga produksi * jumlah
cost = produksi_z * produksi_y

# profit
profit = revenue - cost

# cari maksimum
idx_max = np.argmax(profit)
q_optimal = produksi_y[idx_max]
profit_max = profit[idx_max]
harga_jual_opt = x[idx_max]
harga_produksi_opt = produksi_z[idx_max]

print("Volume produksi optimal:", q_optimal)
print("Harga jual optimal:", harga_jual_opt)
print("Harga produksi optimal:", harga_produksi_opt)
print("Keuntungan maksimum:", profit_max)

# Plot profit curve
plt.figure(figsize=(8,5))
plt.plot(produksi_y, profit, label="Profit", color="green")
plt.axvline(q_optimal, color="red", linestyle="--", label="Optimal Production")
plt.title("Profit vs Volume Produksi")
plt.xlabel("Volume Produksi (jumlah barang)")
plt.ylabel("Profit")
plt.legend()
plt.grid(True)
plt.show()
