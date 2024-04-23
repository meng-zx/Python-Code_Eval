import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def load_data_from_json(file_path):
    # Load JSON data from a file
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def prepare_data_for_visualization(data):
    # Convert JSON data to a DataFrame for easier manipulation
    rows = []
    for problem, details in data.items():
        for metric, models_scores in details['metrics'].items():
            for model, score in models_scores.items():
                rows.append({
                    'Problem': problem,
                    'Metric': metric,
                    'Model': model,
                    'Score': score
                })
    return pd.DataFrame(rows)


def create_heatmaps(df):
    # Create a directory for plots if it does not exist
    plot_dir = "heatmaps"
    os.makedirs(plot_dir, exist_ok=True)

    # Generate a heatmap for each metric
    metrics = df['Metric'].unique()
    for metric in metrics:
        plt.figure(figsize=(10, 8))
        metric_data = df[df['Metric'] == metric]
        pivot_table = metric_data.pivot(index="Problem", columns="Model", values="Score")
        sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap="coolwarm", cbar_kws={'label': 'Score'})
        plt.title(f"Heatmap of {metric} Scores Across Models and Problems")
        plt.ylabel('Problem')
        plt.xlabel('Model')
        plt.tight_layout()
        # Save each heatmap to the directory
        plt.savefig(f"{plot_dir}/heatmap_{metric}.png")
        plt.close()


# Main execution block
if __name__ == "__main__":
    # Load data
    data = load_data_from_json('output_integrated_data.json')  # Specify the correct JSON file path
    df = prepare_data_for_visualization(data)
    create_heatmaps(df)
