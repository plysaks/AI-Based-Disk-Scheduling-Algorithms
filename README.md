# AI-Based Disk Scheduling Project - Code Only

## Overview
This project implements AI-based disk scheduling algorithms, comparing traditional methods like FCFS, SSTF, and SCAN with machine learning approaches to optimize seek time and disk efficiency.Disk scheduling is a critical component in operating systems, responsible for managing the sequence in which disk I/O requests are processed. This project explores AI-based disk scheduling techniques and compares them with traditional approaches to enhance efficiency and performance. Conventional methods such as First-Come-First-Serve (FCFS), Shortest Seek Time First (SSTF), and SCAN are implemented alongside machine learning models, including Reinforcement Learning (RL) and Neural Networks. The goal is to minimize seek time and optimize disk movement based on real-time predictions.


## Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/plysaks/AI-Based-Disk-Scheduling-Algorithms.git]
   ```
2. Install required dependencies:
   ```bash
   pip install numpy pandas matplotlib seaborn tensorflow
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Technologies Used
- **Python** for implementation
- **NumPy, Pandas** for data handling
- **Matplotlib, Seaborn** for visualization
- **Tkinter** for GUI development
- **TensorFlow/Keras** for AI-based scheduling

## Code Implementation
### Traditional Disk Scheduling Algorithms
- **First-Come-First-Serve (FCFS)**: Processes requests in the order they arrive.
- **Shortest Seek Time First (SSTF)**: Prioritizes requests with the shortest seek time.
- **SCAN Algorithm**: Moves in one direction, servicing requests, then reverses.

### AI-Based Disk Scheduling
- **Reinforcement Learning (RL)**: Uses a neural network to optimize disk movement decisions.
- **Model Training**: Trains on historical disk access patterns.
- **Prediction**: The AI model predicts the optimal request sequence.

### GUI & Visualization
- Users can input request sequences and run different scheduling algorithms.
- Real-time graphical visualization of disk head movement.

## Execution
Run the `main.py` file, which launches the GUI and executes the disk scheduling algorithms.

## Future Enhancements
- Train AI models with real-world data for better accuracy.
- Implement additional scheduling techniques like C-SCAN and LOOK.
- Optimize AI-based decision-making with deep reinforcement learning.



