import json
import os
import matplotlib.pyplot as plt
import numpy as np

# Load the JSON data
with open("output_integrated_data.json", "r") as f:
    data = json.load(f)

# Create a folder for visualizations
os.makedirs("visualization", exist_ok=True)

# Function to save figures
def save_figure(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join("visualization", f"{name}.png"), dpi=300, bbox_inches="tight")

# Helper function to create a single graph for a metric
def create_metric_graph(metric_name):
    problems = list(data.keys())
    models = list(data["BFS"]["metrics"][metric_name].keys())
    num_problems = len(problems)
    num_models = len(models)

    scores = np.zeros((num_problems, num_models))
    for i, problem in enumerate(problems):
        problem_data = data[problem]
        for j, model in enumerate(models):
            scores[i, j] = problem_data["metrics"][metric_name].get(model, 0)

    fig, ax = plt.subplots(figsize=(12, 8))
    im = ax.imshow(scores, cmap="YlGn")

    ax.set_xticks(np.arange(num_models))
    ax.set_xticklabels(models, rotation=45, ha="right", fontsize=10)
    ax.set_yticks(np.arange(num_problems))
    ax.set_yticklabels(problems, fontsize=10)

    ax.set_title(f"{metric_name} Scores", fontsize=16)
    ax.set_xlabel("Model", fontsize=14)
    ax.set_ylabel("Problem", fontsize=14)

    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel(metric_name, rotation=-90, va="bottom", fontsize=12)

    # Show numerical values on the heatmap
    for i in range(num_problems):
        for j in range(num_models):
            text = ax.text(j, i, f"{scores[i, j]:.2f}",
                           ha="center", va="center", color="k", fontsize=8)

    save_figure(fig, f"{metric_name.lower()}_scores")

# Create graphs for each metric
for metric in ["Accuracy", "Time", "Memory", "Maintainability", "Style"]:
    create_metric_graph(metric)

print("Visualizations have been created in the 'visualization' folder")