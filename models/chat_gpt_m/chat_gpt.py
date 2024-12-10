
import os
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks import get_openai_callback
from chatgpt_model import GPT_Model
from openai import AzureOpenAI



# api key:
#3.5
# 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
#4.0
# sk-GardnCuVxSwbqswZ1a55F262A4D74431Af05AbD6D5C72dA2
# model name
# gpt-4-0409

client = AzureOpenAI(
    api_key='17b5615f064c4a899a308979d2f195e7',
    api_version="2024-02-15-preview",
    azure_endpoint="https://wed-aiq-aoai-swc.openai.azure.com/",
)

# prose data test
def prose_test(GPT_Model_35, template_c):
    folder_path = "../data/foofah/Transformation.Text/"
    result = []
    visited_file = []
    for sub_file in os.listdir(folder_path):
        if sub_file != '.DS_Store':
            print(sub_file)
            visited_file.append(sub_file)
            file_path = os.path.join(folder_path, sub_file)
            input_data, output_data = GPT_Model_35.read_in_data(file_path)
            tutorial = GPT_Model_35.get_prose_output(input_data, template_c)
            result.append([sub_file, tutorial])
            GPT_Model_35.ans.append([sub_file, tutorial])
    return result, visited_file

# foofah data test
def foofah_test(GPT_Model_35, template_c):
    result = GPT_Model_35.gpt_output(template_c)
    return result



def main():
    # define template
    template_c= '''

    Given an example input and output dataset, learn how the transformation performed from the provided input dataset to the output dataset. 
        
    Pay attention to the size difference between the input and output dataset.
    
    Generate python function with no explanations needed. 
        
    input dataset: {input_list} 
    output dataset: {output_list}
    
     '''
    
    template_cot= '''

    Given an example input and output dataset, learn how the transformation performed from the provided input dataset to the output dataset. 
        
    input dataset: {input_list} 
    output dataset: {output_list}

    Pay attention to the size difference between the input and output dataset.

    You should think step by step how the transformation was performed.

    you should generate python code to reproduce the transformation.

    you are also given a test set {test_list} where you should include the test set in your python code
    
    '''
    
    #define model 

    # GPT_Model_35 = GPT_Model('sk-proj-QAY6J5d8kbS4GGwbjQVcT3BlbkFJiOSQh2u8tHd3k7JcEBHV',3.5)
    GPT_Model4 = GPT_Model('sk-v2jfjIB3eI39LpLh4d060e314f534d4f85C74169E7164c76')

    # call tests on datasets
    # result = prose_test(GPT_Model,template_c)
    result = foofah_test(GPT_Model4,template_c)
    print(result)

    # convert result into csv
    output= []
    for x in result:
        o = x[1].split('\n\ninput_data')
        d = {'data': x[0],'output': o[0]}

        output.append(d)
    df = pd.DataFrame(output)
    df.to_csv('rerun_gpt4_multitimes.csv', index=False)

if __name__ == '__main__':
    main()
