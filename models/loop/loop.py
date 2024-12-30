import json
import openai
import io
import contextlib
import prompt 
from collections import defaultdict
import time

#"craigslist_data_wrangler","crime_data_wrangler", "potters_wheel_divide", "potters_wheel_fold" ,
name_list = ["craigslist_data_wrangler","crime_data_wrangler", "potters_wheel_divide", "potters_wheel_fold" ,
            "potters_wheel_fold_2", "potters_wheel_merge_split", "potters_wheel_split_fold", "potters_wheel_unfold", 
            "potters_wheel_unfold2", "proactive_wrangling_fold", "proactive_wrangling_complex", "reshape_table_structure_data_wrangler"]
missing_list = [9, 14, 16, 20, 21, 23, 25, 31, 32, 35, 38, 39, 42, 50]

# prompts
TEMPLATE_WITH_FUNC_LOOP = prompt.TEMPLATE_WITH_FUNC_LOOP
LOOP_FINAL = prompt.LOOP_FINAL
RETRY = prompt.RETRY
BASE_PROMPT = prompt.BASE_PROMPT
TEMPLATE_WITH_FUNC_CALL = prompt.TEMPLATE_WITH_FUNC_CALL
ERROR_IDENTIFIER = prompt.ERROR_IDENTIFIER
RETRY_WITH_ERROR = prompt.RETRY_WITH_ERROR

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

def get_ouput(content, chat_history=None, error = False):
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
    

    if not error:
    # Append the current user's message to the history
        chat_history.append({"role": "user", "content": content})
        # Send the entire conversation history to the model
        response = client.chat.completions.create(
            messages=chat_history, stream=False, **settings
        )
    else:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": content}], stream=False, **settings
        )
    
    # Process the model's response
    if response.choices:
        client_response = response.choices[0].message.content
        if error:
            return client_response
        chat_history.append({"role": "assistant", "content": client_response})
        return client_response, chat_history
    else:
        return None, chat_history


def gpt_output(specific_error):
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
                prompt = TEMPLATE_WITH_FUNC_CALL.format(
                        input_list = input_data[0],
                        output_list = input_data[1],
                )
                answer, chat_history = get_ouput(prompt)
                if '```python' in answer:
                    code = answer.split('```python')[1]
                    code = code.split('```')[0]
                    code_result = run_code(code)
                    if isinstance(code_result, str):
                        try:
                            generated_output = eval(code_result)
                        except:
                            generated_output = code_result
                    else:
                        generated_output = code_result
                else:
                     code = 'Invalid'
                     generated_output = []
                num_try = 0
                tmp_dic[num_try] = [code, generated_output]
                if specific_error:
                    while generated_output != input_data[1] and num_try < 3:
                        num_try += 1

                        # identify the error
                        
                        print('generating errors')
                        error_prompt = ERROR_IDENTIFIER.format(
                            correct_output = input_data[1],
                            generated_output = generated_output
                        )
                        start_time = time.time()
                        errors = get_ouput(error_prompt, error = True)
                        mid_time = time.time()
                        print('error time', mid_time - start_time)
                        tmp_dic['errors'].append(errors)

                        # retry with error identified
                        print('retrying with error')
                        retry_with_error_prompt = RETRY_WITH_ERROR.format(
                            code_history = code,
                            error = errors,
                            generated_output = generated_output
                        )
                        answer, chat_history = get_ouput(retry_with_error_prompt,chat_history)
                        end_time = time.time()
                        print('retry time', end_time - mid_time)
                        if '```python' in answer:
                            code = answer.split('```python')[1]
                            code = code.split('```')[0]
                            code_result = run_code(code)
                            if isinstance(code_result, str):
                                try:
                                    generated_output = eval(code_result)
                                except:
                                    generated_output = code_result
                            else:
                                generated_output = code_result
                        else:
                            code = 'Invalid'
                            generated_output = []
                        print('retry', num_try)
                        tmp_dic[num_try] = [code, generated_output]
                else:
                    while generated_output != input_data[1] and num_try < 3:
                        num_try += 1
                        retry_prompt = RETRY.format(
                            code_history = code,
                            test_list = input_data[1],
                            generated_output = generated_output
                        )
                        answer, chat_history = get_ouput(retry_prompt,chat_history)
                        if '```python' in answer:
                            code = answer.split('```python')[1]
                            code = code.split('```')[0]
                            code_result = run_code(code)
                            if isinstance(code_result, str):
                                try:
                                    generated_output = eval(code_result)
                                except:
                                    generated_output = code_result
                            else:
                                generated_output = code_result
                        else:
                            code = 'Invalid'
                            generated_output = []
                        print('retry', num_try)
                        tmp_dic[num_try] = [code, generated_output]
                # pass the test input to the code
                final_prompt = LOOP_FINAL.format(
                        code_history = code,
                        test_list = test_data[0]
                    )
                answer, chat_history = get_ouput(final_prompt,chat_history)
                code = answer.split('```python')[1]
                code = code.split('```')[0]
                code_result = run_code(code)
                if isinstance(code_result, str):
                    try:
                        generated_output = eval(code_result)
                    except:
                        generated_output = 'DOUBLE CHECK' + ', '.join(map(str, code_result))
                else:
                    generated_output = 'DOUBLE CHECK' + ', '.join(map(str, code_result))
                tmp_dic['final'] = [code, generated_output]
                tmp_dic['full_chat_history'] = chat_history

                ouput_file = './loop_error/foofah_kg_'+str(j)+'_'+ str(i)+'.json'

                # Write the dictionary to the Python file
                with open(ouput_file, 'w') as file:
                    json.dump(tmp_dic, file)
                
        return 

if __name__ == "__main__":
    gpt_output(specific_error = True)