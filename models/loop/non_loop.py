import json
import openai
import io
import contextlib
import prompt 
from collections import defaultdict
import ast

#"craigslist_data_wrangler","crime_data_wrangler", "potters_wheel_divide", "potters_wheel_fold" , 'potters_wheel_fold_2
name_list = ["craigslist_data_wrangler","crime_data_wrangler", "potters_wheel_divide", "potters_wheel_fold" ,
            "potters_wheel_fold_2","potters_wheel_merge_split", "potters_wheel_split_fold", "potters_wheel_unfold", 
            "potters_wheel_unfold2", "proactive_wrangling_fold", "proactive_wrangling_complex", "reshape_table_structure_data_wrangler"]
missing_list = [9, 14, 16, 20, 21, 23, 25, 31, 32, 35, 38, 39, 42, 50]
SIMPLE = prompt.TEMPLATE_C
BASE_PROMPT = prompt.TEMPLATE_WITH_FUNC

def run_code(code):
    output = io.StringIO()

    # Use contextlib.redirect_stdout to redirect print statements to the StringIO object
    try:
        with contextlib.redirect_stdout(output):
            exec(code)

        # Get the output as a string
        captured_output = output.getvalue()
    except:
        captured_output = []
    return captured_output

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

client = openai.Client(
    api_key='sk-uUJWDlppyATaEVatYfmv7GgOs02eT2I7Dge57wxj07oMfR6n',
    base_url = "https://xiaoai.plus/v1")

def get_ouput(content, chat_history=None):
    settings = {
            "model": "gpt-4o",
            "temperature": 0,
            "seed": 1,
        }
    ##### base prompt pass in here
    if chat_history is None:
        # chat_history = [{"role": "system", "content": BASE_PROMPT}]
        chat_history = []
    #####
    
    # Append the current user's message to the history
    chat_history.append({"role": "user", "content": content})
    
    # Send the entire conversation history to the model
    response = client.chat.completions.create(
        messages=chat_history, stream=False, **settings
    )
    
    # Process the model's response
    if response.choices:
        client_response = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": client_response})
        return client_response, chat_history
    else:
        return None, chat_history


def gpt_output():
        # loop thrpugh all the files
        for j in name_list:
            if j in missing_list:
                continue
            for i in range(1,6):
                # create a dictionary to store the code
                tmp_dic = defaultdict(list)
                path = '../../data/foofah/foofah/exp0_'+str(j) + '_'+ str(i)+ '.txt'
                input_data, test_data = read_in_data(path)
                print('on file', j,i)
                prompt = SIMPLE.format(
                        input_list = input_data[0],
                        output_list = input_data[1],
                        test_list = test_data[0]
                )
                answer, chat_history = get_ouput(prompt)
                if '```python' in answer:
                    code = answer.split('```python')[1]
                    code = code.split('```')[0]
                    code_result = run_code(code)
                    if isinstance(code_result, str):
                        generated_output = ast.literal_eval(code_result)
                    else:
                        generated_output = code_result
                else:
                     code = 'Invalid'
                     generated_output = []

                tmp_dic['final'] = [code, generated_output]
                tmp_dic['full_chat_history'] = chat_history

                ouput_file = './non_loop_simple/foofah_kg_'+str(j)+'_'+ str(i)+'.json'

                # Write the dictionary to the Python file
                with open(ouput_file, 'w') as file:
                    json.dump(tmp_dic, file)
                
        return 

if __name__ == "__main__":
    gpt_output()