# DC Motor Speed Controller using PID

Experiment Graph <img width="1435" height="738" alt="image" src="https://github.com/user-attachments/assets/ff9d6637-8b74-4bba-9557-8f695abda3db" />
 


A complete simulation project that demonstrates **speed control of a DC motor** using a **PID (Proportional-Integral-Derivative) controller**.

Built from scratch with both **Python** and **MATLAB** implementations, including step response comparisons, live animation, and detailed explanations.

---

## ✨ Features

- Accurate mathematical model of an armature-controlled DC motor
- PID controller implementation (P, PI, and full PID comparison)
- Professional step response graphs
- **Live animated simulation** showing real-time motor behavior
- Clean, well-commented code in both Python and MATLAB
- Transfer function approach using Control Systems concepts
- Ready for learning, college projects, or portfolio

---

## 🎯 Project Overview

DC motors are widely used in robotics, electric vehicles, drones, and industrial automation. However, their speed varies with load, temperature, and voltage fluctuations.

This project implements a **closed-loop PID controller** to make the motor track a desired reference speed accurately, with fast response, minimal overshoot, and **zero steady-state error**.

You will learn:
- How to derive and use **transfer functions**
- Difference between open-loop and closed-loop control
- How PID tuning affects system performance
- Simulation techniques using Python (`control` library) and MATLAB

---


## 🛠️ Technologies Used

- **Python** 3.10+
- **MATLAB** (with Control System Toolbox)
- `control` library (Python Control Systems Library)
- `matplotlib` + `numpy`
- Transfer Function modeling

---

## 📦 Installation & Setup

### Option 1: Using Python (Recommended for beginners)

1. Clone or download the project folder.

2. Open PowerShell / Command Prompt in the project folder.

3. **Create a virtual environment** (strongly recommended):

```powershell
# Using Python 3.10 (or whichever version you prefer)
python -m venv venv

# Activate the environment
venv\Scripts\activate

Install required packages:

PowerShellpip install control matplotlib numpy

Verify installation:

PowerShellpython test_control.py
Option 2: Using MATLAB

Open MATLAB
Set the project folder as current directory
Run dc_motor.m


🚀 How to Run
1. Basic Simulation (Comparison Graph)
PowerShellpython dc_motor.py
This generates a clean comparison plot showing:

Open-loop response
P controller
PI controller
Full PID controller

2. Live Animation (Most Fun!)
PowerShellpython dc_motor_pid_live.py
Watch the motor speed rise in real-time with live error display!
3. MATLAB Version
Simply run the dc_motor.m script in MATLAB.

📊 Results & What You Will See

Open Loop: Slow response with large steady-state error
P Controller: Faster but still has steady-state error
PI Controller: Eliminates steady-state error
PID Controller: Fast rise time, low overshoot, zero steady-state error

The tuned gains used are:

( K_p = 100 )
( K_i = 200 )
( K_d = 10 )



🧠 Learning Outcomes
After working with this project, you will understand:

What a transfer function is and how to create one
Difference between open-loop and closed-loop systems
Role of each term in a PID controller (P, I, D)
How to simulate dynamic systems in Python and MATLAB
Basic PID tuning concepts


🎮 Experiment & Learn
Try these changes in the code:

Reduce Kp to 50 → slower response
Set Ki = 0 → see steady-state error appear
Increase Kd → observe reduced overshoot
Change reference speed or motor parameters

This is the best way to deeply understand control systems!

📝 Report / Documentation
A ready-to-use report structure is included in the conversation history. It contains:

Mathematical modeling
PID design explanation
Results discussion
Code appendix


🔮 Future Improvements (Ideas)

Discrete-time PID for microcontroller (Arduino/ESP32)
Anti-windup implementation
Load disturbance rejection simulation
Real-time hardware interface
Interactive dashboard with sliders (using Plotly/Streamlit)



