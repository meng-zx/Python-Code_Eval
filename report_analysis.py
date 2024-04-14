#!/bin/bash

import os
import re
import matplotlib.pyplot as plt
import numpy as np

def parse_report(file_path):
    with open(file_path, 'r') as file:
        report_content = file.read()
    # Define regex patterns for each metric
    tests_pattern = r"Total tests run: (\d+).*Passed tests: (\d+).*Failed tests: (\d+).*Pass percentage: ([0-9.]+)%"
    time_pattern = r"Average running time over \d+ runs: ([0-9.]+) seconds"
    memory_pattern = r"Average memory usage over \d+ runs: ([0-9.]+) MiB"
    maintainability_pattern = r"Average complexity: ([ABCD](?: \(\d+\.\d+\))?)"
    style_pattern = r"Your code has been rated at ([0-9.]+)/10"

    # Extract metrics using regex
    tests_match = re.search(tests_pattern, report_content, re.DOTALL)
    time_match = re.search(time_pattern, report_content)
    memory_match = re.search(memory_pattern, report_content)
    maintainability_match = re.search(maintainability_pattern, report_content)
    style_match = re.search(style_pattern, report_content)

    # Parse the metrics
    total_tests = int(tests_match.group(1)) if tests_match else None
    passed_tests = int(tests_match.group(2)) if tests_match else None
    failed_tests = int(tests_match.group(3)) if tests_match else None
    pass_percentage = float(tests_match.group(4)) if tests_match else None
    average_time = float(time_match.group(1)) if time_match else None
    average_memory = float(memory_match.group(1)) if memory_match else None
    average_complexity = maintainability_match.group(1) if maintainability_match else None
    style_rating = float(style_match.group(1)) if style_match else None

    # Create a dictionary with the metrics
    metrics = {
        'Accuracy': pass_percentage,
        'Time': average_time,
        'Memory': average_memory,
        'Maintainability': average_complexity,
        'Style': style_rating
    }

    return metrics

# dir for each model
model_paths = {
    'GPT4': 'D:/cornell/24sp/info5900/Python-Code_Eval/reports/GPT4',
    'Watsons': 'D:/cornell/24sp/info5900/Python-Code_Eval/reports/watsonx',
    'Claude': 'D:/cornell/24sp/info5900/Python-Code_Eval/reports/Claude',
    'CodeWhisperer': 'D:/cornell/24sp/info5900/Python-Code_Eval/reports/CodeWhisperer',
}

metrics_data = {metric: {model: [] for model in model_paths} for metric in ['Accuracy', 'Time', 'Memory', 'Maintainability', 'Style']}
test_names = []


for model, path in model_paths.items():
    for filename in sorted(os.listdir(path)):
        if filename.endswith('.txt'):
            file_path = os.path.join(path, filename)
            metrics = parse_report(file_path)
            test_names.append(filename[:-4])
            for metric, value in metrics.items():
                metrics_data[metric][model].append(value)

num_tests = len(test_names)
x = np.arange(num_tests)
width = 0.2 

for metric in metrics_data:
    fig, ax = plt.subplots()
    for i, (model, _) in enumerate(model_paths.items()):
        ax.bar(x + i*width, metrics_data[metric][model], width, label=model)
    
    ax.set_ylabel(metric)
    ax.set_title(f'{metric} by test and model')
    ax.set_xticks(x)
    ax.set_xticklabels(test_names, rotation=45, ha='right')
    ax.legend()
    plt.show()