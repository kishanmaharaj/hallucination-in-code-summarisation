### NOTE: The prompts are optimized for each language models for best output, therefore they may have a slight variation. 

llama3_8b = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>
Assume that you are an expert in understanding Java and performing named entity recognition related to Java code.
<|eot_id|><|start_header_id|>user<|end_header_id|>

You have to label the entities by considering the following labels:

Code entities: CLASS, VARIABLE, FUNCTION, LIBRARY, VALUE, DATA TYPE, and HTML or XML TAG
Natural language entities: APPLICATION, UI ELEMENT, LANGUAGE, DATA STRUCTURE, ALGORITHM, FILE TYPE, FILE NAME, VERSION, DEVICE, OS, WEBSITE, and USER NAME.

For every entity in the input mention the entity_type in the given format only. 
Strictly follow this template and only print the output without any other word.

You can follow the example below:

Input: 
Inputs and Outputs of the Method
Inputs: The method does not take any external input via parameters or user input. It uses a hardcoded integer n with a value of 3. 
Outputs: The method outputs to the console whether the number n is a prime number or not. 
Business Purpose: The purpose of this method is to determine if a given integer n is a prime number and print the result to the console. This could be useful in applications that need to verify the primality of numbers, such as cryptographic algorithms or educational tools.

Output: 
[{'entity_name': 'integer', 'entity_type': 'DATA TYPE'},  {'entity_name': 'n', 'entity_type': 'VARIABLE'},  {'entity_name': '3', 'entity_type': 'VALUE'},  {'entity_name': 'console', 'entity_type': 'APPLICATION'},  {'entity_name': 'cryptographic algorithms', 'entity_type': 'ALGORITHM'},  {'entity_name': 'educational tools', 'entity_type': 'APPLICATION'}]

Now consider the summary describing a code below:

{generated_summary}

<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

llama3_70b = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>
Assume that you are an expert in understanding Java and performing named entity recognition related to Java code.
<|eot_id|><|start_header_id|>user<|end_header_id|>

You have to label the entities by considering the following labels:

Code entities: CLASS, VARIABLE, FUNCTION, LIBRARY, VALUE, DATA TYPE, and HTML or XML TAG
Natural language entities: APPLICATION, UI ELEMENT, LANGUAGE, DATA STRUCTURE, ALGORITHM, FILE TYPE, FILE NAME, VERSION, DEVICE, OS, WEBSITE, and USER NAME.

For every entity in the input mention the entity_type in the given format only. 
Strictly follow this template and only print the output without any other word.

You can follow the example below:

Input: 
Inputs and Outputs of the Method
Inputs: The method does not take any external input via parameters or user input. It uses a hardcoded integer n with a value of 3. 
Outputs: The method outputs to the console whether the number n is a prime number or not.
Business Purpose: The purpose of this method is to determine if a given integer n is a prime number and print the result to the console. This could be useful in applications that need to verify the primality of numbers, such as cryptographic algorithms or educational tools.

Output: 
[{'entity_name': 'integer', 'entity_type': 'DATA TYPE'},  {'entity_name': 'n', 'entity_type': 'VARIABLE'},  {'entity_name': '3', 'entity_type': 'VALUE'},  {'entity_name': 'console', 'entity_type': 'APPLICATION'},  {'entity_name': 'cryptographic algorithms', 'entity_type': 'ALGORITHM'},  {'entity_name': 'educational tools', 'entity_type': 'APPLICATION'}]

Now consider the summary describing a code below:

{generated_summary}

<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

mistral_7b = """<s>[INST]Assume that you are an expert in understanding Java and performing named entity recognition related to Java code.[/INST]</s>

[INST]
You have to label the entities by considering the following labels:

Code entities: CLASS, VARIABLE, FUNCTION, LIBRARY, VALUE, DATA TYPE, and HTML or XML TAG
Natural language entities: APPLICATION, UI ELEMENT, LANGUAGE, DATA STRUCTURE, ALGORITHM, FILE TYPE, FILE NAME, VERSION, DEVICE, OS, WEBSITE, and USER NAME.

For every entity in the input mention the entity_type in the given format only. 
Strictly follow this template and only print the output without any other word.
[/INST]

[INST]
You can follow the example below:

Input: 
Inputs and Outputs of the Method
Inputs: The method does not take any external input via parameters or user input. It uses a hardcoded integer n with a value of 3. 
Outputs: The method outputs to the console whether the number n is a prime number or not. 
Business Purpose: The purpose of this method is to determine if a given integer n is a prime number and print the result to the console. This could be useful in applications that need to verify the primality of numbers, such as cryptographic algorithms or educational tools.

Output:
[{'entity_name': 'integer', 'entity_type': 'DATA TYPE'},  {'entity_name': 'n', 'entity_type': 'VARIABLE'},  {'entity_name': '3', 'entity_type': 'VALUE'},  {'entity_name': 'console', 'entity_type': 'APPLICATION'},  {'entity_name': 'cryptographic algorithms', 'entity_type': 'ALGORITHM'},  {'entity_name': 'educational tools', 'entity_type': 'APPLICATION'}]


Now consider the summary describing a code below:

{generated_summary}
[/INST]"""



codellama_7b = """[INST] Q: Perform named entity recognition related to the Java Code in the given summary. The output needs to be a list of dictionaries.
You can only use the following labels:
CLASS, VARIABLE, FUNCTION, LIBRARY, VALUE, DATA TYPE, and HTML or XML TAG, APPLICATION, UI ELEMENT, LANGUAGE, DATA STRUCTURE, ALGORITHM, FILE TYPE, FILE NAME, VERSION, DEVICE, OS, WEBSITE, and USER NAME.

Summary:
Input: 
Inputs and Outputs of the Method
Inputs: The method does not take any external input via parameters or user input. It uses a hardcoded integer n with a value of 3. 
Outputs: The method outputs to the console whether the number n is a prime number or not. 
Business Purpose: The purpose of this method is to determine if a given integer n is a prime number and print the result to the console. This could be useful in applications that need to verify the primality of numbers, such as cryptographic algorithms or educational tools.

A: 
```
[{'entity_name': 'integer', 'entity_type': 'DATA TYPE'},  {'entity_name': 'n', 'entity_type': 'VARIABLE'},  {'entity_name': '3', 'entity_type': 'VALUE'},  {'entity_name': 'console', 'entity_type': 'APPLICATION'},  {'entity_name': 'cryptographic algorithms', 'entity_type': 'ALGORITHM'},  {'entity_name': 'educational tools', 'entity_type': 'APPLICATION'}]
```

Q: Perform named entity recognition related to the Java Code in the given summary. The output needs to be a list of dictionaries.
You can only use the following labels:
Code entities: CLASS, VARIABLE, FUNCTION, LIBRARY, VALUE, DATA TYPE, and HTML or XML TAG
Natural language entities: APPLICATION, UI ELEMENT, LANGUAGE, DATA STRUCTURE, ALGORITHM, FILE TYPE, FILE NAME, VERSION, DEVICE, OS, WEBSITE, and USER NAME.

Summary:
{generated_summary}

A:
[/INST]"""


codellama_34b =  """[INST] Q: Perform named entity recognition related to the Java Code in the given summary. The output needs to be a list of dictionaries.
You can only use the following labels:
CLASS, VARIABLE, FUNCTION, LIBRARY, VALUE, DATA TYPE, and HTML or XML TAG, APPLICATION, UI ELEMENT, LANGUAGE, DATA STRUCTURE, ALGORITHM, FILE TYPE, FILE NAME, VERSION, DEVICE, OS, WEBSITE, and USER NAME

Summary:
Input: 
Inputs and Outputs of the Method
Inputs: The method does not take any external input via parameters or user input. It uses a hardcoded integer n with a value of 3. 
Outputs: The method outputs to the console whether the number n is a prime number or not. 
Business Purpose: The purpose of this method is to determine if a given integer n is a prime number and print the result to the console. This could be useful in applications that need to verify the primality of numbers, such as cryptographic algorithms or educational tools.

A: 
```
[{'entity_name': 'integer', 'entity_type': 'DATA TYPE'},  {'entity_name': 'n', 'entity_type': 'VARIABLE'},  {'entity_name': '3', 'entity_type': 'VALUE'},  {'entity_name': 'console', 'entity_type': 'APPLICATION'},  {'entity_name': 'cryptographic algorithms', 'entity_type': 'ALGORITHM'},  {'entity_name': 'educational tools', 'entity_type': 'APPLICATION'}]
```

Q: Perform named entity recognition related to the Java Code in the given summary. The output needs to be a list of dictionaries.
You can only use the following labels:
Code entities: CLASS, VARIABLE, FUNCTION, LIBRARY, VALUE, DATA TYPE, and HTML or XML TAG
Natural language entities: APPLICATION, UI ELEMENT, LANGUAGE, DATA STRUCTURE, ALGORITHM, FILE TYPE, FILE NAME, VERSION, DEVICE, OS, WEBSITE, and USER NAME.

Summary:
{generated_summary}

A:
[/INST]"""


ibm_granite_20b = """Question: As a Java Expert, perform named entity recognition related to the Java Code in the given summary. The output needs to be a list of dictionaries.
You can only use the following labels:
Code entities: CLASS, VARIABLE, FUNCTION, LIBRARY, VALUE, DATA TYPE, and HTML or XML TAG

Natural Language entities: APPLICATION, UI ELEMENT, LANGUAGE, DATA STRUCTURE, ALGORITHM, FILE TYPE, FILE NAME, VERSION, DEVICE, OS, WEBSITE, and USER NAME.

Summary:
Input: 
Inputs and Outputs of the Method
Inputs: The method does not take any external input via parameters or user input. It uses a hardcoded integer n with a value of 3. 
Outputs: The method outputs to the console whether the number n is a prime number or not. 
Business Purpose: The purpose of this method is to determine if a given integer n is a prime number and print the result to the console. This could be useful in applications that need to verify the primality of numbers, such as cryptographic algorithms or educational tools.

Answer: 
```
[{'entity_name': 'integer', 'entity_type': 'DATA TYPE'},  {'entity_name': 'n', 'entity_type': 'VARIABLE'},  {'entity_name': '3', 'entity_type': 'VALUE'},  {'entity_name': 'console', 'entity_type': 'APPLICATION'},  {'entity_name': 'cryptographic algorithms', 'entity_type': 'ALGORITHM'},  {'entity_name': 'educational tools', 'entity_type': 'APPLICATION'}]
```

Question: As a Java Expert, perform named entity recognition related to the Java Code in the given summary. The output needs to be a list of dictionaries.
You can only use the following labels:
Code entities: CLASS, VARIABLE, FUNCTION, LIBRARY, VALUE, DATA TYPE, and HTML or XML TAG
Natural language entities: APPLICATION, UI ELEMENT, LANGUAGE, DATA STRUCTURE, ALGORITHM, FILE TYPE, FILE NAME, VERSION, DEVICE, OS, WEBSITE, and USER NAME.

Summary:
{generated_summary}

Answer:"""

ibm_granite_34b = """Question: As a Java Expert, perform named entity recognition related to the Java Code in the given summary. The output needs to be a list of dictionaries wrapped with ```.
You can only use the following labels:
Code entities: CLASS, VARIABLE, FUNCTION, LIBRARY, VALUE, DATA TYPE, and HTML or XML TAG
Natural Language entities: APPLICATION, UI ELEMENT, LANGUAGE, DATA STRUCTURE, ALGORITHM, FILE TYPE, FILE NAME, VERSION, DEVICE, OS, WEBSITE, and USER NAME.

Summary:
Input: 
Inputs and Outputs of the Method
Inputs: The method does not take any external input via parameters or user input. It uses a hardcoded integer n with a value of 3. 
Outputs: The method outputs to the console whether the number n is a prime number or not. 
Business Purpose: The purpose of this method is to determine if a given integer n is a prime number and print the result to the console. This could be useful in applications that need to verify the primality of numbers, such as cryptographic algorithms or educational tools.

Answer: 
```
[{'entity_name': 'integer', 'entity_type': 'DATA TYPE'},  {'entity_name': 'n', 'entity_type': 'VARIABLE'},  {'entity_name': '3', 'entity_type': 'VALUE'},  {'entity_name': 'console', 'entity_type': 'APPLICATION'},  {'entity_name': 'cryptographic algorithms', 'entity_type': 'ALGORITHM'},  {'entity_name': 'educational tools', 'entity_type': 'APPLICATION'}]
```

Question: As a Java Expert, perform named entity recognition related to the Java Code in the given summary. The output needs to be a list of dictionaries wrapped with ```.
You can only use the following labels:
Code entities: CLASS, VARIABLE, FUNCTION, LIBRARY, VALUE, DATA TYPE, and HTML or XML TAG
Natural language entities: APPLICATION, UI ELEMENT, LANGUAGE, DATA STRUCTURE, ALGORITHM, FILE TYPE, FILE NAME, VERSION, DEVICE, OS, WEBSITE, and USER NAME.

Summary:
{generated_summary}

Answer:"""
