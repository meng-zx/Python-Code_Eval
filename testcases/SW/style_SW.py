import pylint.lint

def check_code_style(file_path):
    pylint_output = pylint.lint.Run([file_path])
    score = pylint_output.linter.stats['global_note']
    return score

if __name__ == "__main__":
    file_path = "SW.py"  # Modify the file name
    style_score = check_code_style(file_path)
    # print("Style score:", style_score)
