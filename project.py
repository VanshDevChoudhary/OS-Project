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

        tk.Button(self.frame, text="Add Process", command=lambda: self.add_node('P')).grid(row=0, column=2)
        tk.Button(self.frame, text="Add Resource", command=lambda: self.add_node('R')).grid(row=0, column=3)
        
        self.plot_graph()
    
    def add_node(self, node_type):
        node = self.node_entry.get()
        if node:
            self.graph.add_node(node, type=node_type)
            self.plot_graph()
    
    def plot_graph(self):
        plt.clf()
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=1500)
        fig = plt.gcf()
        fig.set_size_inches(5, 3)
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ResourceAllocationSimulator(root)
    root.mainloop()
