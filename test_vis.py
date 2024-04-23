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

# Visualization: Average score across all metrics for each model
avg_scores = {model: 0 for model in data["BFS"]["metrics"]["Accuracy"].keys()}
total_problems = len(data)
for problem_data in data.values():
    for model, score in problem_data["metrics"]["Accuracy"].items():
        avg_scores[model] += score / total_problems

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(avg_scores.keys(), avg_scores.values())
ax.set_title("Average Score Across All Metrics", fontsize=16)
ax.set_xlabel("Model", fontsize=14)
ax.set_ylabel("Average Score", fontsize=14)
save_figure(fig, "average_score")

# Visualization: Problem difficulty distribution
difficulties = [data[problem]["difficulty"] for problem in data]
difficulty_counts = {difficulty: difficulties.count(difficulty) for difficulty in set(difficulties)}

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(difficulty_counts.keys(), difficulty_counts.values())
ax.set_title("Problem Difficulty Distribution", fontsize=16)
ax.set_xlabel("Difficulty Level", fontsize=14)
ax.set_ylabel("Number of Problems", fontsize=14)
save_figure(fig, "difficulty_distribution")

# Visualization: Heatmap for average score of each metric, problem, and model
metrics = ["Accuracy", "Time", "Memory", "Maintainability", "Style"]
models = list(data["BFS"]["metrics"]["Accuracy"].keys())
problems = list(data.keys())

scores = np.zeros((len(problems), len(metrics), len(models)))

for i, problem in enumerate(problems):
    for j, metric in enumerate(metrics):
        for k, model in enumerate(models):
            scores[i, j, k] = data[problem]["metrics"][metric].get(model, 0)

fig, ax = plt.subplots(figsize=(12, 8))
im = ax.imshow(np.mean(scores, axis=2), cmap="YlGn")

ax.set_xticks(np.arange(len(metrics)))
ax.set_xticklabels(metrics, rotation=45, ha="right", fontsize=10)
ax.set_yticks(np.arange(len(problems)))
ax.set_yticklabels(problems, fontsize=10)

ax.set_title("Average Score per Metric and Problem", fontsize=16)
ax.set_xlabel("Metric", fontsize=14)
ax.set_ylabel("Problem", fontsize=14)

cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("Average Score", rotation=-90, va="bottom", fontsize=12)

save_figure(fig, "heatmap_average_scores")

print("Visualizations have been created in the 'visualization' folder.")