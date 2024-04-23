#!/bin/bash

import os
import re
import matplotlib.pyplot as plt
import numpy as np
import json

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
    'GPT4': 'reports/GPT4',
    'Watsons': 'reports/watsonx',
    'Claude': 'reports/Claude',
    'CodeWhisperer': 'reports/CodeWhisperer',
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



# json_file_path = 'metrics_data.json'
#
#
# with open(json_file_path, 'w') as file:
#     json.dump(metrics_data, file)
#
# problem_names = ["BFS", "Graph2D", "GraphUnion", "LIS", "MedianSortedArray", "RecArea", "RPN", "SW", "SwimInWater", "TrappingRainWater"]
# pname_file_path = 'problem_names_array.json'
# with open(pname_file_path, 'w') as file:
#     json.dump(problem_names, file)

# problem_details={}
# problem_details["TrappingRainWater"]={"difficulty": "hard",
#                                       "tags" : []
#                                       }
# problem_details["RPN"]={"difficulty": "medium",
#                                       "tags" : ['stack']
#                                       }
# problem_details["MedianSortedArray"]={"difficulty": "hard",
#                                       "tags" : ['binary search']
#                                       }
# problem_details["LIS"]={"difficulty": "medium",
#                                       "tags" : ['dp']
#                                       }
# problem_details["SwimInWater"]={"difficulty": "hard",
#                                       "tags" : ['priority queue', 'graph']
#                                       }
# problem_details["Graph2D"]={"difficulty": "hard",
#                                       "tags" : ['dp', 'graph']
#                                       }
# problem_details["GraphUnion"]={"difficulty": "medium",
#                                       "tags" : ['union', 'graph']
#                                       }
#
# problem_details["BFS"]={"difficulty": "hard",
#                                       "tags" : ['bfs', 'trie']
#                                       }
# problem_details["SW"]={"difficulty": "hard",
#                                       "tags" : ['sliding windows']
#                                       }
# problem_details["RecArea"]={"difficulty": "medium",
#                                       "tags" : ['rectangle area']
#                                       }
#
#
# detail_file_path = 'problem_details.json'


with open(detail_file_path, 'w') as file:
    json.dump(problem_details, file)


num_tests = len(test_names)
x = np.arange(num_tests)
total_width = 0.8
width = total_width / len(metrics_data)
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.ion()
for metric in metrics_data:
    fig, ax = plt.subplots()
    rects = []
    for i, (model, values) in enumerate(metrics_data[metric].items()):
        rect = ax.bar(x + i * width - total_width / 2, values, width, label=model)
        rects.append(rect)

    ax.set_ylabel(metric)
    ax.set_title(f'{metric}')
    ax.set_xticks(x + width * (len(model_paths) - 1) / 2)
    ax.set_xticklabels(test_names, rotation=45, ha='right')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    fig.set_size_inches(12, 8)
    fig.savefig(os.path.join(fig_directory, f"{metric}.png"))
    plt.show()

for metric in metrics_data:
    fig, ax = plt.subplots()
    for i, (model, values) in enumerate(metrics_data[metric].items()):
        if any(v is None for v in values):
            print(f"Cannot plot {metric} for {model} because it contains None values")
            continue