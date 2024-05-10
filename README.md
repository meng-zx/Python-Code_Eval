# Generated Code Evaluation Tool
TODO: write introduction of this repo

## 0.Clone the Repository From GitHub
In WSL, 
```
git clone git@github.com:meng-zx/Python-Code-Generation-Evaluation.git
```
[How to Configure SSH Keys for GitHub](https://jdblischak.github.io/2014-09-18-chicago/novice/git/05-sshkeys.html)

## 1. Set Up Python Virtual Environment
The script for setting up the virtual environment of this project is written.
For easy setup, just run 
```
chmod +x setup_env.sh
./setup_env.sh
```
This only needs to run once.

## 2. Activate Python Virtual Environment
Activate Python Virtual Environment by
```
source env/bin/activate
```

## 3. Install Packages
```
chmod +x install_packages.sh
./install_packages.sh
```


## 4. Run the Tests
Run the test by
```
./perform_tests.sh
```
If it's the first run, give permission by 
```
chmod +x perform_tests.sh
```

## 3. Add New Tests
Please strictly follow the file structure and naming rules, per the `testcases/TwoSum`, for the scripts to work properly. 

For example, if you want to test how Claude works with `TrappingRainWater`, the file structure should be:
```
testcases/
└── TrappingRainWater
    ├── TrappingRainWater_test.py
    ├── maintainability_TrappingRainWater.sh
    ├── memory_TrappingRainWater.py
    ├── qa_TrappingRainWater.py
    ├── style_TrappingRainWater.py
    ├── test_TrappingRainWater.sh
    └── time_TrappingRainWater.py
```
The safest way is copy all the files from the `testcases/TwoSum` and modify all the file names and corresponding variables in the scripts. The generated code is in `Claude/TrappingRainWater.py`, test cases are in `testcases/TrappingRainWater/TrappingRainWater_test.py`. Don't forget to create a folder for `Claude` under `reports/` if there doesn't exists one.

For using same model to generate codes for different problems, put the new problem solution file under the model folder, e.g.
```
Claude/
└── TrappingRainWater.py
└── ReversePolishNotation.py
```

## 4. Raw data

Raw data is stored in `output_integrated_da.json`.

## 5. Visualization

The visualization is stored in folders `visualization/`, `seperate_heatmap/`, and `seperate_heatmap_green/`.
