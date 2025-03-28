# AI-Based Disk Scheduling Project - Code Only

## Overview
Disk scheduling plays a crucial role in operating systems, managing the order in which disk I/O requests are processed. Traditional scheduling methods such as First-Come-First-Serve (FCFS), Shortest Seek Time First (SSTF), and SCAN follow predefined rules to handle requests. However, AI-based approaches, including Reinforcement Learning (RL) and Neural Networks, can dynamically optimize disk movement, reducing seek time and improving efficiency. This project implements and compares these scheduling techniques.

## Installation
### Prerequisites
Ensure you have Python installed on your system. Then, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/plysaks/AI-Based-Disk-Scheduling-Algorithms.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AI-Based-Disk-Scheduling-Algorithms
   ```
3. Install the required dependencies:
   ```bash
   pip install numpy pandas matplotlib seaborn tensorflow
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Technologies Used
- **Python** - Primary language for implementation.
- **NumPy, Pandas** - Data handling and numerical operations.
- **Matplotlib, Seaborn** - Visualization and graphical representation.
- **Tkinter** - GUI development for user interaction.
- **TensorFlow/Keras** - AI-based scheduling model development.

## Code Implementation
### Traditional Disk Scheduling Algorithms
- **First-Come-First-Serve (FCFS)**: Requests are processed in the order they arrive, without prioritization.
- **Shortest Seek Time First (SSTF)**: Prioritizes requests closest to the current disk head position to minimize movement.
- **SCAN Algorithm**: Moves in one direction, servicing requests sequentially, then reverses upon reaching the end.

### AI-Based Disk Scheduling
- **Reinforcement Learning (RL)**: Utilizes a neural network model to dynamically optimize disk movement.
- **Model Training**: The AI model is trained using historical disk access patterns to enhance scheduling efficiency.
- **Prediction Mechanism**: The trained model predicts optimal request sequences, reducing seek time.

### GUI & Visualization
- Allows users to input request sequences and execute various scheduling algorithms.
- Provides a real-time graphical representation of disk head movement.
- Displays seek time and performance comparisons between traditional and AI-based methods.

## Execution
Once dependencies are installed, execute the following command to launch the GUI and run scheduling algorithms:
   ```bash
   python main.py
   ```

## Future Enhancements
- **Training with real-world disk access data** for more accurate predictions.
- **Incorporating additional scheduling techniques** like C-SCAN and LOOK.
- **Enhancing AI models** with deep reinforcement learning to further optimize disk movement.

## Contribution & Collaboration
We welcome contributions! If you’d like to enhance the project, fork the repository, make changes, and submit a pull request.



