import json
import os
from collections import defaultdict
import pandas as pd

name_list = [
    "craigslist_data_wrangler", "crime_data_wrangler", "potters_wheel_divide", "potters_wheel_fold",
    "potters_wheel_fold_2", "potters_wheel_merge_split", "potters_wheel_split_fold", "potters_wheel_unfold",
    "potters_wheel_unfold2", "proactive_wrangling_fold", "proactive_wrangling_complex", "reshape_table_structure_data_wrangler"
]
missing_list = [9, 14, 16, 20, 21, 23, 25, 31, 32, 35, 38, 39, 42, 50]


def read_in_data(file_name):
    """Reads test data from the specified JSON file."""
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File not found: {file_name}")

    with open(file_name, 'rb') as f:
        test_data = json.load(f)

    # Check if required keys exist
    required_keys = ['InputTable', 'OutputTable', 'TestingTable', 'TestAnswer']
    for key in required_keys:
        if key not in test_data:
            raise KeyError(f"Missing key '{key}' in {file_name}")

    input_data = [test_data['InputTable'], test_data['OutputTable']]
    output_data = [test_data['TestingTable'], test_data['TestAnswer']]

    return input_data, output_data


def eval():
    """Evaluates the output data in 'non_loop_simple' directory and calculates accuracy."""
    directory_path = './non_loop_simple_2'
    acc = defaultdict(list)

    for filename in os.listdir(directory_path):
        if filename == '.DS_Store':
            continue

        try:
            file_number = filename.split('foofah_kg_')[1][:-5]
        except IndexError:
            print(f"Unexpected filename format: {filename}")
            continue

        file_path = os.path.join(directory_path, filename)
        correct_output_path = f'../../data/foofah/foofah/exp0_{file_number}.txt'

        # Skip if the correct output file doesn't exist
        if not os.path.exists(correct_output_path):
            print(f"Correct output file not found: {correct_output_path}")
            continue

        try:
            input_data, test_data = read_in_data(correct_output_path)
            with open(file_path, 'r') as f:
                output = json.load(f)
        except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
            print(f"Error processing {filename}: {e}")
            continue

        final_result = output.get('final', [None, []])[1]
        ans = test_data[1]

        # Ensure final_result and ans are lists of lists
        if not isinstance(final_result, list) or not all(isinstance(row, list) for row in final_result):
            print(f"Invalid format in final_result for file: {filename}")
            continue

        if not isinstance(ans, list) or not all(isinstance(row, list) for row in ans):
            print(f"Invalid format in ans for file: {filename}")
            continue

        acc_temp = 0
        for k in range(min(len(final_result), len(ans))):
            for m in range(min(len(final_result[k]), len(ans[k]))):
                if final_result[k][m] == ans[k][m]:
                    acc_temp += 1

        total_values = sum(len(inner_list) for inner_list in ans) or 1  # Avoid division by zero
        test_case_acc = acc_temp / total_values

        acc[file_number] = [len(output) - 2, test_case_acc]

    acc = sorted(acc.items())
    print(acc)

    # Save accuracy to file
    with open('non_loop_simple.json', 'w') as f:
        json.dump(acc, f)

    return acc


def combine_by_dataset(eval_result):
    """Combines evaluation results by dataset and exports to an Excel file."""
    acc_dict = defaultdict(lambda: [0, 0])

    for key, value in eval_result:
        dataset = key[:-2]
        acc_dict[dataset][0] += value[0] / 5
        acc_dict[dataset][1] += value[1] / 5

    df = pd.DataFrame(acc_dict).transpose()
    df.columns = ['# of tries', 'Metric 2']
    df.to_excel('non_loop_simple.xlsx')
    print("Results saved to 'non_loop_simple.xlsx'")
    return acc_dict


if __name__ == '__main__':
    acc_dict = eval()
    print('----------------------')
    combine_by_dataset(acc_dict)
