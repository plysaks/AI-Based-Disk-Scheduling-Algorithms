import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import random
import time
from collections import deque
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Traditional Disk Scheduling Algorithms
class DiskScheduling:
    def __init__(self, requests, head, size=200):
        self.requests = requests
        self.head = head
        self.size = size
    
    def fcfs(self):
        seek_sequence = [self.head] + self.requests
        seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence)-1))
        return seek_sequence, seek_time
    
    def sstf(self):
        requests = self.requests.copy()
        seek_sequence = [self.head]
        head = self.head
        while requests:
            closest = min(requests, key=lambda x: abs(x - head))
            seek_sequence.append(closest)
            requests.remove(closest)
            head = closest
        seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence)-1))
        return seek_sequence, seek_time
    
    def scan(self):
        left = sorted([r for r in self.requests if r < self.head])
        right = sorted([r for r in self.requests if r >= self.head])
        seek_sequence = [self.head] + right + [self.size] + left[::-1]
        seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence)-1))
        return seek_sequence, seek_time

# AI-based Disk Scheduling (Reinforcement Learning Approach)
class AIDiskScheduler:
    def __init__(self, size=200):
        self.size = size
        self.model = self.build_model()
    
    def build_model(self):
        model = keras.Sequential([
            layers.Dense(32, activation='relu', input_shape=(2,)),
            layers.Dense(32, activation='relu'),
            layers.Dense(1, activation='linear')
        ])
        model.compile(optimizer='adam', loss='mse')
        return model
    
    def train_model(self, data):
        X, y = zip(*data)
        X = np.array(X)
        y = np.array(y)
        self.model.fit(X, y, epochs=50, verbose=0)
    
    def predict(self, head, requests):
        inputs = np.array([[head, r] for r in requests])
        predictions = self.model.predict(inputs)
        return requests[np.argmin(predictions)]

# GUI for Visualization
class DiskSchedulingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Disk Scheduling Visualization")
        
        self.label = tk.Label(root, text="Enter Requests (comma-separated):")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.button = tk.Button(root, text="Run Algorithms", command=self.run)
        self.button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
    
    def run(self):
        requests = list(map(int, self.entry.get().split(',')))
        head = random.randint(0, 199)
        scheduler = DiskScheduling(requests, head)
        
        fcfs_seq, fcfs_time = scheduler.fcfs()
        sstf_seq, sstf_time = scheduler.sstf()
        scan_seq, scan_time = scheduler.scan()
        
        results = f"FCFS: {fcfs_time} | SSTF: {sstf_time} | SCAN: {scan_time}"
        self.result_label.config(text=results)
        
        self.plot_results(fcfs_seq, sstf_seq, scan_seq)
    
    def plot_results(self, *sequences):
        plt.figure(figsize=(10, 5))
        for seq, label in zip(sequences, ['FCFS', 'SSTF', 'SCAN']):
            plt.plot(seq, range(len(seq)), marker='o', label=label)
        plt.gca().invert_yaxis()
        plt.legend()
        plt.show()

# Main Execution
def main():
    root = tk.Tk()
    app = DiskSchedulingGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()