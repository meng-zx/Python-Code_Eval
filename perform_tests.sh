#!/bin/bash

report_dir="reports"
model_names=("example") # put all model names here
problem_names=("TwoSum") # put all problem names here


for model_name in "${model_names[@]}"; do
    for i in "${!problem_names[@]}"; do
        problem_name="${problem_names[i]}"
        problem_id=$((i))
        testcase_folder="testcases/$problem_name"

        if [ ! -d "$testcase_folder" ]; then
            break
        fi
        cd "$testcase_folder"

        report_file="../../$report_dir/$model_name/$model_name-$problem_name.txt"
        source_file="../../$model_name/$problem_name.py"

        if [ ! -f "$source_file" ]; then
            cd ../..
            break
        fi

        rm -f "$report_file"
        cp "$source_file" .


        touch "$report_file"
        printf "$model_name $problem_id $problem_name \n" >> "$report_file"

        printf "\n" >> "$report_file"
        printf "Test: QA \n" >> "$report_file"
        python3 "qa_$problem_name.py" &>> "$report_file"

        printf "\n" >> "$report_file"
        printf "Test: Time \n" >> "$report_file"
        python3 "time_$problem_name.py" &>> "$report_file"

        printf "\n" >> "$report_file"
        printf "Test: Memory \n" >> "$report_file"
        python3 "memory_$problem_name.py" &>> "$report_file"


        printf "\n" >> "$report_file"
        printf "Test: Maintainability \n" >> "$report_file"
        chmod +x "maintainability_$problem_name.sh"
        "./maintainability_$problem_name.sh" &>> "$report_file"

        printf "\n" >> "$report_file"
        printf "Test: Style \n" >> "$report_file"
        python3 "style_$problem_name.py" &>> "$report_file"

        rm -f "$problem_name.py"
        cd ../..
        printf "Finished Evaluating Code for Problem: ${problem_name}, Model: ${model_name}! \n"

    done
done
