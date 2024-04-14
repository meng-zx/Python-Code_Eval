#!/bin/bash

import os
import re
import matplotlib.pyplot as plt
import numpy as np

fig_directory = '/mnt/d/cornell/24sp/info5900/Python-Code_Eval/fig'
if not os.path.exists(fig_directory):
    os.makedirs(fig_directory)
def parse_report(file_path):
    with open(file_path, 'r') as file:
        report_content = file.read()

    tests_pattern = r"Total tests run: (\d+).*Passed tests: (\d+).*Failed tests: (\d+).*Pass percentage: ([0-9.]+)%"
    time_pattern = r"Average running time over \d+ runs: ([0-9.]+) seconds"
    memory_pattern = r"Average memory usage over \d+ runs: ([0-9.]+) MiB"
    maintainability_pattern = r"(\w+)\.py - ([ABCD]) \((\d+\.\d+)\)"
    style_pattern = r"Your code has been rated at ([0-9.]+)/10"

    tests_match = re.search(tests_pattern, report_content, re.DOTALL)
    time_match = re.search(time_pattern, report_content)
    memory_match = re.search(memory_pattern, report_content)
    maintainability_match = re.search(maintainability_pattern, report_content)
    style_match = re.search(style_pattern, report_content)

    pass_percentage = float(tests_match.group(4)) if tests_match else 0.0
    average_time = float(time_match.group(1)) if time_match else 0.0
    average_memory = float(memory_match.group(1)) if memory_match else 0.0
    average_complexity_score = float(maintainability_match.group(3)) if maintainability_match else 0.0
    style_rating = float(style_match.group(1)) if style_match else 0.0

    metrics = {
        'Accuracy': pass_percentage,
        'Time': average_time,
        'Memory': average_memory,
        'Maintainability': average_complexity_score,
        'Style': style_rating
    }

    return metrics

# dir for each model
model_paths = {
    'GPT4': '/mnt/d/cornell/24sp/info5900/Python-Code_Eval/reports/GPT4',
    'Watsons': '/mnt/d/cornell/24sp/info5900/Python-Code_Eval/reports/watsonx',
    'Claude': '/mnt/d/cornell/24sp/info5900/Python-Code_Eval/reports/Claude',
    'CodeWhisperer': '/mnt/d/cornell/24sp/info5900/Python-Code_Eval/reports/CodeWhisperer',
}

test_names = [filename[:-4] for filename in sorted(os.listdir(next(iter(model_paths.values())))) if
              filename.endswith('.txt')]

metrics_data = {metric: {model: [] for model in model_paths} for metric in
                ['Accuracy', 'Time', 'Memory', 'Maintainability', 'Style']}

for model, path in model_paths.items():
    for filename in sorted(os.listdir(path)):
        if filename.endswith('.txt'):
            file_path = os.path.join(path, filename)
            metrics = parse_report(file_path)
            for metric, value in metrics.items():
                if value is not None:
                    metrics_data[metric][model].append(value)
                else:
                    print(f"Warning: Missing data for {metric} in {file_path}")


num_tests = len(test_names)
x = np.arange(num_tests)
width = 0.2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.ion()
for metric in metrics_data:
    fig, ax = plt.subplots()
    for i, (model, values) in enumerate(metrics_data[metric].items()):
        # None -> 0
        values_with_zeros = [0 if v is None else v for v in values]
        ax.bar(x + i * width, values_with_zeros, width, label=model)

    ax.set_ylabel(metric)
    ax.set_title(f'{metric} by test and model')
    ax.set_xticks(x + width * (len(model_paths) - 1) / 2)
    ax.set_xticklabels(test_names, rotation=45, ha='right')
    ax.legend()
    fig.savefig(os.path.join(fig_directory, f"{metric}.png"))
    plt.show()

# for metric in metrics_data:
#     fig, ax = plt.subplots()
#     for i, (model, values) in enumerate(metrics_data[metric].items()):
#         if any(v is None for v in values):
#             print(f"Cannot plot {metric} for {model} because it contains None values")
#             continue