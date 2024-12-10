TEMPLATE_COT= '''

    Given an example input and output dataset, learn how the transformation performed from the provided input dataset to the output dataset. 

    input dataset: {input_list} 

    output dataset: {output_list}

    Pay attention to the size difference between the input and output dataset.

    You should think step by step how the transformation was performed.

    you should generate python code to reproduce the transformation.
    
    In the python code only print out the transformed dataset, no other information.

    you are also given a test set {test_list} where you should include the test set in your python code

    '''

TEMPLATE_C= '''

    Given an example input and output dataset, learn how the transformation performed from the provided input dataset to the output dataset. 
        
    Pay attention to the size difference between the input and output dataset.
    
    Generate python function with no explanations needed. 
        
    input dataset: {input_list} 
    output dataset: {output_list}
    
    you are also given a test set {test_list} where you should include the test set in your python code as the function input
    Do not include input database in your code output
    
    '''
TEMPLATE_6= '''

    Given an example input and output dataset, learn how the transformation performed from the provided input dataset to the output dataset. 
        
    Pay attention to the size difference between the input and output dataset.
    
    Generate python function with no explanations needed. 
        
    input dataset: {input_list} 
    output dataset: {output_list}
    
    you are also given a test set {test_list} where you should include the test set in your python code as the function input
    Do not include input database in your code output

    Note: The element from first row of input dataset will be the first element in each row of the output, follows by product
    
    '''
TEMPLATE_26= '''

    Given an example input and output dataset, learn how the transformation performed from the provided input dataset to the output dataset. 
        
    Pay attention to the size difference between the input and output dataset.
    
    Generate python function with no explanations needed. 
        
    input dataset: {input_list} 
    output dataset: {output_list}
    
    you are also given a test set {test_list} where you should include the test set in your python code as the function input
    Do not include input database in your code output

    Note: change from 1 element a sublist to 4 element per sublist
    
    '''
TEMPLATE_29= '''

    Given an example input and output dataset, learn how the transformation performed from the provided input dataset to the output dataset. 
        
    Pay attention to the size difference between the input and output dataset.
    
    Generate python function with no explanations needed. 
        
    input dataset: {input_list} 
    output dataset: {output_list}
    
    you are also given a test set {test_list} where you should include the test set in your python code as the function input
    Do not include input database in your code output

    Note: combine 2 two from the input to 1 row for the output, but only keep the first word in the first row and all the numerical values
    
    '''
TEMPLATE_LANGUAGE = '''

    Given an example input and output dataset, learn how the transformation performed from the provided input dataset to the output dataset. 
        
    Pay attention to the size difference between the input and output dataset.
    
    Generate python function with no explanations needed. 
        
    input dataset: {input_list} 
    output dataset: {output_list}
    
    you are also given a test set {test_list} where you should include the test set in your python code as the function input
    Do not include input database in your code output

    Note: You should use information you have with this problem such as countries respective ISO language code eg ["Arabic = ar"].
    
    '''
TEMPLATE_KG= '''

    Given an example input and output dataset, learn how the transformation performed from the provided input dataset to the output dataset. 
    Common operations in data cleaning and data wrangling include: identifying and removing duplicate data, handling missing values, 
    filtering outliers, standardizing data formats, data type conversion, data aggregation, joining datasets, data validation, 
    and data enrichment by adding information from external sources. Note you should not use the datetime package.
        
    Pay attention to the size difference between the input and output dataset.
    
    Generate python function with no explanations needed. 
        
    input dataset: {input_list} 
    output dataset: {output_list}
    
    you are also given a test set {test_list} where you should include the test set in your python code as the function input
    Do not include input database in your code output
    '''
TEMPLATE_KG2= '''
    Given an example input and output dataset, learn the transformation applied to convert the provided input dataset into the output dataset.

    Data transformations can include various cleaning and wrangling operations, such as identifying and removing duplicate data, 
    handling missing values, filtering outliers, standardizing data formats, performing data type conversion, data aggregation, 
    joining datasets, validating data integrity, or enriching the dataset by adding information from external sources. 
    However, avoid using any datetime-specific packages for this task.

    When analyzing the transformation, take note of potential changes in the dataset's structure, size, or format between input and output.

    Based on these transformations, generate a Python function that will take a new test set as input and apply the same transformation. 
    Include test_list as the function parameter and ensure the code only outputs the function definition. Do not include the original input_list or output_list directly in the code.
    
    input dataset: {input_list}
    output dataset: {output_list}
    test set: {test_list}
    '''
TEMPLATE_KG_LONG = ''' 
    Given an example input and output dataset, learn the transformations applied to convert the input dataset into the output dataset. These transformations may involve various data cleaning and wrangling tasks that standardize and prepare the data for analysis. Here are some common transformations to consider, along with examples where appropriate:

    Removing Duplicate Data: Detect and remove repeated entries based on specific columns or across the entire dataset.
    Example: If the input dataset contains multiple rows for the same ID, the output dataset may include only the first instance.

    Handling Missing Values: Fill or remove missing data based on the output dataset. You may need to impute values with the mean, median, or mode, or drop rows/columns entirely if missing data is excessive.
    Example: If the input dataset has rows with missing ages, the output dataset might replace them with the average age.

    Filtering Outliers: Remove or modify extreme values that are beyond an acceptable range.
    Example: If a numerical column has values that are three standard deviations away from the mean, they might be removed or capped at a specific threshold.

    Standardizing Data Formats: Ensure consistency in text formats, date formats, and number formats.
    Example: Converting all names to title case (e.g., "john doe" to "John Doe") or ensuring all dates follow the "YYYY-MM-DD" format.

    Data Type Conversion: Change column data types as required by the output dataset, such as converting strings to numbers or dates to strings.
    Example: If a column contains numeric values stored as strings in the input dataset, the output dataset might have them converted to integers or floats.

    Data Aggregation: Combine data at a higher level, like summing, averaging, or grouping by a specific attribute.
    Example: If the input dataset contains daily sales, the output dataset might aggregate these values to show monthly or weekly totals.

    Joining Datasets: Merge data from additional sources if the output dataset contains extra columns not present in the input dataset.
    Example: Joining a product details dataset with the input dataset based on a product ID to include product names in the output.

    Take note of changes in size, format, or structure between the input and output datasets. Also, ensure that any transformations are consistent with observed changes across multiple examples if provided.

    Based on these transformations, generate a Python function that will take a new test set as input and apply the same transformation. 
    Include test_list as the function parameter and ensure the code only outputs the function definition. Do not include the original input_list or output_list directly in the code.
    
    input dataset: {input_list}
    output dataset: {output_list}
    test set: {test_list}
    '''
TEMPLATE_WITH_FUNC = '''
    Given an example input and output dataset, learn the transformations applied to convert the input dataset into the output dataset. 
    These transformations may involve various data cleaning and wrangling tasks that standardize and prepare the data for analysis. 
    Here are some common transformations to consider, along with examples where appropriate, some sample reference functions are provided but you are not limited or have to use the provided functions:

    # Combine the first two rows into one by concatenation
    def combine_first_two_rows(data):
        """
        Combines the first two rows in a 2D list by concatenating them.
        Returns a new 2D list with the combined row.
        """
        if len(data) < 2:
            raise ValueError("Not enough rows to combine.")
        new_row = data[0] + data[1]
        new_data = [new_row] + data[2:]
        return new_data

    # Flip the first row and the leftmost column
    def flip_first_row_and_leftmost_col(data):
        """
        Flips the first row and the leftmost column in a 2D list.
        Returns a new 2D list with the flipped values.
        """
        if not data or not data[0]:
            return data
        num_rows = len(data)
        num_cols = len(data[0])

        # Extract first row and leftmost column
        first_row = data[0]
        leftmost_col = [data[i][0] for i in range(num_rows)]

        # Swap the values
        new_data = [[data[i][j] for j in range(num_cols)] for i in range(num_rows)]
        new_data[0] = leftmost_col
        for i in range(num_rows):
            new_data[i][0] = first_row[i] if i < len(first_row) else None  # Handle any length mismatch

        return new_data

    # Transpose the 2D list
    def transpose(data):
        """
        Transposes a 2D list, flipping rows and columns.
        """
        return [list(row) for row in zip(*data)]

    # Rotate the 2D list 90 degrees clockwise
    def rotate_90_clockwise(data):
        """
        Rotates the 2D list 90 degrees clockwise.
        """
        return [list(row) for row in zip(*data[::-1])]

    # Swap the first two columns
    def swap_first_two_columns(data):
        """
        Swaps the first two columns in a 2D list.
        """
        if len(data[0]) < 2:
            raise ValueError("Not enough columns to swap.")
        return [[row[1], row[0]] + row[2:] for row in data]

    # Add the first two rows element-wise
    def add_first_two_rows(data):
        """
        Adds the first two rows element-wise in a 2D list.
        Returns a new row and a modified 2D list.
        """
        if len(data) < 2:
            raise ValueError("Not enough rows to add.")
        new_row = [data[0][i] + data[1][i] for i in range(len(data[0]))]
        new_data = [new_row] + data[2:]
        return new_data

    # Remove duplicate elements in each row of the 2D list
    def remove_duplicates(data):
        """
        Removes duplicate elements in each row of a 2D list.
        Returns a new 2D list with duplicates removed, preserving the original order.
        """
        return [list(dict.fromkeys(row)) for row in data]


    Based on these transformations, generate a Python function that will take a new test set as input and apply the same transformation. 
    Include test_list as the function parameter and ensure the code only outputs the function definition. Do not include the original input_list or output_list directly in the code.
    
    input dataset: {input_list}
    output dataset: {output_list}
    test set: {test_list}
    '''

RETRY = '''
    Given the previously generated code, its output, and the test list, 
    modify only the code in the code history—do not alter the input data—to ensure the generated output matches the correct output.
    Code history: {code_history}
    Test list: {test_list}
    Generated output: {generated_output}
'''
    

BASE_PROMPT = '''
    You are a data scientist swpecializing in program by example, focusing on data wrangling and transformation tasks.
    Given an example input and output dataset, learn the transformations applied to convert the input dataset into the output dataset. 
    These transformations may involve various data cleaning and wrangling tasks that standardize and prepare the data for analysis. 
    Here are some common transformations to consider, along with examples where appropriate, some sample reference functions are provided but you are not limited or have to use the provided functions:

    # Combine the first two rows into one by concatenation
    def combine_first_two_rows(data):
        """
        Combines the first two rows in a 2D list by concatenating them.
        Returns a new 2D list with the combined row.
        """
        if len(data) < 2:
            raise ValueError("Not enough rows to combine.")
        new_row = data[0] + data[1]
        new_data = [new_row] + data[2:]
        return new_data

    # Flip the first row and the leftmost column
    def flip_first_row_and_leftmost_col(data):
        """
        Flips the first row and the leftmost column in a 2D list.
        Returns a new 2D list with the flipped values.
        """
        if not data or not data[0]:
            return data
        num_rows = len(data)
        num_cols = len(data[0])

        # Extract first row and leftmost column
        first_row = data[0]
        leftmost_col = [data[i][0] for i in range(num_rows)]

        # Swap the values
        new_data = [[data[i][j] for j in range(num_cols)] for i in range(num_rows)]
        new_data[0] = leftmost_col
        for i in range(num_rows):
            new_data[i][0] = first_row[i] if i < len(first_row) else None  # Handle any length mismatch

        return new_data

    # Transpose the 2D list
    def transpose(data):
        """
        Transposes a 2D list, flipping rows and columns.
        """
        return [list(row) for row in zip(*data)]

    # Rotate the 2D list 90 degrees clockwise
    def rotate_90_clockwise(data):
        """
        Rotates the 2D list 90 degrees clockwise.
        """
        return [list(row) for row in zip(*data[::-1])]

    # Swap the first two columns
    def swap_first_two_columns(data):
        """
        Swaps the first two columns in a 2D list.
        """
        if len(data[0]) < 2:
            raise ValueError("Not enough columns to swap.")
        return [[row[1], row[0]] + row[2:] for row in data]

    # Add the first two rows element-wise
    def add_first_two_rows(data):
        """
        Adds the first two rows element-wise in a 2D list.
        Returns a new row and a modified 2D list.
        """
        if len(data) < 2:
            raise ValueError("Not enough rows to add.")
        new_row = [data[0][i] + data[1][i] for i in range(len(data[0]))]
        new_data = [new_row] + data[2:]
        return new_data

    # Remove duplicate elements in each row of the 2D list
    def remove_duplicates(data):
        """
        Removes duplicate elements in each row of a 2D list.
        Returns a new 2D list with duplicates removed, preserving the original order.
        """
        return [list(dict.fromkeys(row)) for row in data]
    '''
TEMPLATE_WITH_FUNC_LOOP = '''

    Based on your information, generate a Python function that will take input dataset as input and apply the same transformation. 
    Include input data as the function parameter and ensure the code only outputs the function definition.
    Make sure you include the input list in your python code as the function input.
    Make sure to print the output of the function 'print(output_list)' in the end of the code.
    
    input list: {input_list}
    output list: {output_list}
    '''
LOOP_FINAL = '''
    Given the code and the test list replace the function's input with the test list, without doing any modification to the code.
    Please make sure to print the output of the function.

    code: {code_history}
    test list: {test_list}
    '''
TEMPLATE_WITH_FUNC_CALL = '''

    Based on your information, generate a Python function that will take input dataset as input and apply the same transformation. 
    Include input data as the function parameter and ensure the code only outputs the function definition.
    You should try to include as much the example functions in your system prompt be part of your code.
    Make sure you include the input list in your python code as the function input.
    Make sure to print the output of the function 'print(output_list)' in the end of the code.
    
    input list: {input_list}
    output list: {output_list}
    '''