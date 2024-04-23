import json
import pandas as pd


def load_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def integrate_and_export_data(metrics_data, problem_names, problem_details, output_path):
    integrated_data = {}

    for metric, models in metrics_data.items():
        for model, scores in models.items():
            for score, problem in zip(scores, problem_names):
                if problem not in integrated_data:
                    integrated_data[problem] = {
                        'tags': problem_details[problem]['tags'],
                        'difficulty': problem_details[problem]['difficulty'],
                        'metrics': {}
                    }
                if metric not in integrated_data[problem]['metrics']:
                    integrated_data[problem]['metrics'][metric] = {}
                integrated_data[problem]['metrics'][metric][model] = score

    with open(output_path, 'w') as outfile:
        json.dump(integrated_data, outfile, indent=4)

    print(f"Integrated data saved to {output_path}")


metrics_data_path = 'metrics_data.json'
problem_names_path = 'problem_names_array.json'
problem_details_path = 'problem_details.json'

metrics_data = load_json_data(metrics_data_path)
problem_names = load_json_data(problem_names_path)
problem_details = load_json_data(problem_details_path)

output_json_path = 'output_integrated_data.json'
integrate_and_export_data(metrics_data, problem_names, problem_details, output_json_path)
