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
                    'Score': score,
                    'Difficulty': details['difficulty']
                })
    return pd.DataFrame(rows)

def create_separate_heatmaps_by_difficulty(df, directory):
    # Create directory if it does not exist
    os.makedirs(directory, exist_ok=True)

    # Separate data by difficulty and create a heatmap for each metric
    metrics = df['Metric'].unique()
    for metric in metrics:
        plt.figure(figsize=(12, 10))

        for i, difficulty in enumerate(['hard', 'medium'], 1):
            plt.subplot(1, 2, i)
            difficulty_data = df[(df['Difficulty'] == difficulty) & (df['Metric'] == metric)]
            if difficulty_data.empty:
                plt.text(0.5, 0.5, f'No {difficulty} problems', horizontalalignment='center', verticalalignment='center')
                plt.title(f'{metric} - {difficulty.capitalize()} Problems')
                continue
            pivot_table = difficulty_data.pivot(index="Problem", columns="Model", values="Score")
            sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap="coolwarm", cbar_kws={'label': 'Score'})
            plt.title(f'{metric} - {difficulty.capitalize()} Problems')

        plt.tight_layout()
        # Save each combined heatmap for each metric
        plt.savefig(f"{directory}/heatmap_{metric}_by_difficulty.png")
        plt.close()

# Main execution block
if __name__ == "__main__":
    # Load data
    data = load_data_from_json('output_integrated_data.json')  # Update this path as necessary
    df = prepare_data_for_visualization(data)
    create_separate_heatmaps_by_difficulty(df, 'separate_heatmap/')
