import numpy as np
import time
import os

A, B = 0, 0  # Rotation angles
while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    z = np.zeros((1760))  # Z-buffer
    b = [' '] * 1760  # Frame buffer
    
    for j in np.arange(0, 6.28, 0.07):
        for i in np.arange(0, 6.28, 0.02):
            c, d, e, f, g = np.sin(i), np.cos(j), np.sin(A), np.sin(j), np.cos(A)
            h, D = d + 2, 1 / (c * h * e + f * g + 5)
            l, m, n, t = np.cos(i), np.cos(B), np.sin(B), c * h * g - f * e
            x, y = int(40 + 30 * D * (l * h * m - t * n)), int(12 + 15 * D * (l * h * n + t * m))
            o = x + 80 * y
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 22 > y > 0 and 80 > x > 0 and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]
    
    print("\033[H", end="")  # Move cursor to the top
    for k in range(1760):
        print(b[k], end="\n" if k % 80 == 79 else "")
    
    A += 0.04
    B += 0.02
    time.sleep(0.03)
