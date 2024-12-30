import json
import os
from collections import defaultdict
import pandas as pd
import shutil

name_list = [ "craigslist_data_wrangler","crime_data_wrangler", "potters_wheel_divide", "potters_wheel_fold" ,
            "potters_wheel_fold_2", "potters_wheel_merge_split", "potters_wheel_split_fold", "potters_wheel_unfold", 
            "potters_wheel_unfold2", "proactive_wrangling_fold", "proactive_wrangling_complex", "reshape_table_structure_data_wrangler"]
missing_list = [9, 14, 16, 20, 21, 23, 25, 31, 32, 35, 38, 39, 42, 50]


def read_in_data(file_name):
        test_data = None
        input_data = [''] * 2
        output_data = [''] * 2
        with open(file_name, 'rb') as f:
            test_data = json.load(f)
            
        input_data[0] = test_data['InputTable']
        input_data[1] = test_data['OutputTable']
        output_data[0] = test_data['TestingTable']
        output_data[1] = test_data['TestAnswer']


        return input_data, output_data

def eval():
    directory_path = '../../output/loop_output_without_baseP'
    acc = defaultdict(list)
    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        if filename == '.DS_Store':
            continue
        file_number = filename.split('foofah_kg_')[1][:-5]
        file_path = os.path.join(directory_path, filename)  # Get full path
        correct_output_path = '../../data/foofah/foofah/exp0_' + file_number + '.txt'
        input_data, test_data = read_in_data(correct_output_path)
        with open(file_path, 'r') as f:
            output = json.load(f)
        final_result = output['final'][1]
        # compare final_result with output_data
        acc_temp = 0
                        # print(j,i)
        ans = test_data[1]

        for k in range(min(len(final_result),len(ans))):
            for m in range(min(len(final_result[k]),len(ans[k]))):
                if final_result[k][m] == ans[k][m]:
                    acc_temp += 1
        total_values = sum(len(inner_list) for inner_list in ans)
        test_case_acc = acc_temp/total_values
                
        acc[file_number] = [len(output)-2, test_case_acc]

    acc = sorted(acc.items())
    print(acc)
    # save acc to file
    with open('loop_eval_nobase.json', 'w') as f:
        json.dump(acc, f)

    return acc

def combine_by_dataset(eval_result):
    acc_dict = defaultdict(lambda: [0, 0])

    for key, value in eval_result:
        dataset = key[:-2]
        acc_dict[dataset][0] += value[0]/5
        acc_dict[dataset][1] += value[1]/5
    df = pd.DataFrame(acc_dict)
    df = df.transpose()
    df.to_excel('simple.xlsx')
    return acc_dict

def sub_eval():
    directory_path = './loop_error'
    acc = defaultdict(list)
    # both output and middle mismatch
    final_result_mis_match = []
    # only final mismatch
    final_mismatch_middle_match = []
    middle_mismatch_first = []
    middle_mismatch = []
    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        if filename == '.DS_Store':
            continue
        file_number = filename.split('foofah_kg_')[1][:-5]
        file_path = os.path.join(directory_path, filename)  # Get full path
        correct_output_path = '../../data/foofah/foofah/exp0_' + file_number + '.txt'
        input_data, test_data = read_in_data(correct_output_path)
        with open(file_path, 'r') as f:
            output = json.load(f)
        final_result = output['final'][1]
        ans = test_data[1]
        if final_result != ans:
            print(file_number)
            if output[str(max(0,len(output)-4))][1] == input_data[1]:
                final_mismatch_middle_match.append(file_number)
            else:
                final_result_mis_match.append(file_number)
                copy_file_path = './mismatched_files/loop_with_error_analysis'
                shutil.copy(file_path, os.path.join(copy_file_path, filename))
        if output['0'][1] != input_data[1]:
            middle_mismatch_first.append(file_number)
            print(file_number)
            if output[str(max(0,len(output)-4))][1] != input_data[1]:
                middle_mismatch.append(file_number)
    # Ensure final_diff is converted to a list
    final_diff = list(set(middle_mismatch_first) - set(middle_mismatch))

    # Create a dictionary for JSON output
    acc_dict = {
        'final_diff': final_diff,
        'final_result_mis_match': final_result_mis_match,
        'final_mismatch_middle_match': final_mismatch_middle_match,
        'middle_mismatch_first': middle_mismatch_first,
        'middle_mismatch': middle_mismatch
    }

    # Save dictionary to JSON
    with open('results_with_sub_file.json', 'w') as f:
        json.dump(acc_dict, f, indent=4)

    # Prepare data for DataFrame
    # Flatten the dictionary for consistent tabular structure
    df_data = []
    for key, value in acc_dict.items():
        if isinstance(value, list):
            for item in value:
                df_data.append({'key': key, 'value': item})
        else:
            df_data.append({'key': key, 'value': value})

    # Create DataFrame
    df = pd.DataFrame(df_data)

    # Save to Excel
    df.to_excel('simple_subset.xlsx', index=False)


if __name__ == '__main__':
    acc_dict = sub_eval()
    # print('----------------------')
    # combine_by_dataset(acc_dict)
