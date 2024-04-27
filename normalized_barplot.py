import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import json

# Load the data
with open('output_integrated_data.json', 'r') as file:
    data = json.load(file)

# Prepare data for visualization
records = []
for problem, metrics_info in data.items():
    for metric, model_scores in metrics_info['metrics'].items():
        for model, score in model_scores.items():
            records.append({
                'Metric': metric,
                'Model': model,
                'Score': score,
                'Problem': problem
            })

# Create a DataFrame
df = pd.DataFrame(records)
df['Normalized Score'] = df.groupby(['Metric'])['Score'].transform(
    lambda x: x / np.sqrt((x ** 2).sum()))

# Create a clustered bar plot
plt.figure(figsize=(15, 10))
bar_plot = sns.barplot(data=df, x='Metric', y='Normalized Score', hue='Model',errorbar=None)

# Set plot labels and title
plt.title('Normalized Performance Comparison Across Models and Metrics')
plt.xlabel('Metric')
plt.ylabel('Normalized Score')
plt.legend(title='Model')

# Rotate x-axis labels for better readability
bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45)

# Save the figure
output_dir = 'visualization'  # Replace with your directory
plt.savefig(f"{output_dir}/normalized_performance_comparison.png")

# Show the plot
plt.show()
