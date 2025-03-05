import numpy as np
import matplotlib.pyplot as plt

F = 5.e2          # No. of cycles per second, F = 500 Hz
T = 2.e-3         # Time period, T = 2 ms
Fs = 50.e3        # No. of samples per second, Fs = 50 kHz
Ts = 1./Fs        # Sampling interval, Ts = 20 us
N = int(T/Ts)     # No. of samples for 2 ms, N = 100

t = np.linspace(0, T, N)
signal = np.sin(2*np.pi*F*t)

plt.plot(t, signal)

plt.xlabel('Time (s)')

plt.ylabel('Voltage (V)')

plt.show()