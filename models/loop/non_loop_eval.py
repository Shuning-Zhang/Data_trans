import json
import os
from collections import defaultdict
import pandas as pd

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
    directory_path = 'non_loop_simple'
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
    with open('non_loop_simple.json', 'w') as f:
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
    df.to_excel('non_loop_simple.xlsx')
    return acc_dict



if __name__ == '__main__':
    acc_dict = eval()
    print('----------------------')
    combine_by_dataset(acc_dict)
