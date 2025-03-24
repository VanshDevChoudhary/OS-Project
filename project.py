import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ResourceAllocationSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Resource Allocation Graph Simulator")
        
        self.graph = nx.DiGraph()
        
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        
        tk.Label(self.frame, text="Process/Resource Name:").grid(row=0, column=0)
        self.node_entry = tk.Entry(self.frame)
        self.node_entry.grid(row=0, column=1)
