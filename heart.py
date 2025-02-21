import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# กำหนดช่วงช่องของ t
t = np.linspace(0, 2*np.pi, 300)
# สมการหัวใจ
x = 16 * np.sin(t) ** 3
y = 13 * np.cos (t) - 5 * np.cos (2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
# สร้างกราฟ
fig, ax = plt.subplots()
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_xticks ([])
ax.set_yticks ([])
ax.set_aspect('equal')
ax.set_title("Heartbeat Animation")
#สร้างเส้นเคลื่อนไหว
line1, = ax.plot([], [], 'r', lw=2) # สร้างเส้นสีแดง
line2, = ax.plot([], [], 'r', lw=2) # สร้างเส้นสีแดง
# ฟังก์ชันอัพเดตเฟรม
def update (i) :
    #เส้นที่เริ่มจากซ้ายไปขวา
    line1.set_data(x[:i], y[ :i])
    #เส้นที่เริ่มจากขวาไปซ้าย
    line2.set_data(x[-i:], y[-i:])
    return line1, line2
#สร้างอนิเมชั่น
ani =  animation.FuncAnimation(fig, update, frames=len(t), interval=10, blit=True)
plt.show() 