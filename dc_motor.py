import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import control

# ================== DC MOTOR PARAMETERS ==================
J = 0.01   # inertia
b = 0.1    # friction
K = 0.01   # motor constant
R = 1.0    # resistance
L = 0.5    # inductance

# Create the motor model (Plant)
plant = control.tf([K], [J*L, J*R + b*L, b*R + K**2])

# ================== PID CONTROLLER ==================
Kp = 100.0
Ki = 200.0
Kd = 10.0
pid = control.tf([Kd, Kp, Ki], [1, 0])   # PID transfer function

# Closed-loop system
sys_pid = control.feedback(plant * pid)

# ================== SIMULATION DATA ==================
t = np.linspace(0, 3, 600)                    # 3 seconds, 600 frames (smooth)
_, y_pid = control.step_response(sys_pid, T=t)  # Simulate once
reference = np.ones_like(t)                   # Desired speed = 1 rad/s

# ================== CREATE FIGURE ==================
fig, ax = plt.subplots(figsize=(11, 6))
ax.set_xlim(0, 3)
ax.set_ylim(-0.1, 1.4)
ax.set_xlabel('Time (seconds)', fontsize=12)
ax.set_ylabel('Angular Speed ω (rad/s)', fontsize=12)
ax.set_title('🔴 LIVE DC Motor Speed Control Simulation with PID Controller\n(Kp=100, Ki=200, Kd=10)', fontsize=14)
ax.grid(True, alpha=0.3)

# Plot lines
ref_line, = ax.plot([], [], 'k:', lw=2.5, label='Reference Speed (1 rad/s)')
actual_line, = ax.plot([], [], 'r-', lw=3.5, label='Actual Motor Speed')
error_line, = ax.plot([], [], 'b--', lw=1.5, label='Error')

# Live value display
time_text = ax.text(0.05, 1.25, '', fontsize=11, bbox=dict(facecolor='white', alpha=0.8))
speed_text = ax.text(0.05, 1.15, '', fontsize=11, bbox=dict(facecolor='white', alpha=0.8))
error_text = ax.text(0.05, 1.05, '', fontsize=11, bbox=dict(facecolor='white', alpha=0.8))

ax.legend(loc='lower right')

# ================== ANIMATION FUNCTION ==================
def animate(frame):
    # Update lines up to current time
    ref_line.set_data(t[:frame], reference[:frame])
    actual_line.set_data(t[:frame], y_pid[:frame])
    error_line.set_data(t[:frame], reference[:frame] - y_pid[:frame])
    
    # Live numbers
    curr_time = t[frame]
    curr_speed = y_pid[frame]
    curr_error = reference[frame] - curr_speed
    
    time_text.set_text(f'Time     : {curr_time:.2f} s')
    speed_text.set_text(f'Actual Speed : {curr_speed:.3f} rad/s')
    error_text.set_text(f'Error        : {curr_error:.3f} rad/s')
    
    return ref_line, actual_line, error_line, time_text, speed_text, error_text

# Create the animation
ani = FuncAnimation(fig, animate, frames=len(t), interval=25, 
                   blit=True, repeat=True, init_func=lambda: (ref_line, actual_line, error_line))

plt.tight_layout()
plt.show()

# Optional: Save as GIF (uncomment if you want)
# ani.save('dc_motor_pid_live.gif', writer='pillow', fps=30)