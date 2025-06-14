### NOTE: The prompts are optimized for each language models for best output, therefore they may have a slight variation. 

llama3_8b = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>
Assume you are an expert in understanding JAVA code. 
<|eot_id|><|start_header_id|>user<|end_header_id|>

Question: As a Java Expert, please provide a detailed summary of the following Java code, with the following sections: 
1. Inputs and outputs of the method
2. Business purpose 
3. Detailed functional summary of the method.

```
{}
```
Answer:

<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""


llama3_70b = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>
Assume you are an expert in understanding JAVA code. 
<|eot_id|><|start_header_id|>user<|end_header_id|>

Question: As a Java Expert, please provide a detailed summary of the following Java code, with the following sections: 
1. Inputs and outputs of the method
2. Business purpose 
3. Detailed functional summary of the method.

```
{}
```
Answer:

<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""


mistral_7b = """<s> [INST] Assume you are an expert in understanding JAVA code. [/INST] </s>

[INST] As a Java Expert, please provide a detailed summary of the following Java code, with the following sections: 
1. Inputs and outputs of the method
2. Business purpose 
3. Detailed functional summary of the method.

```
{}
```
[/INST]"""


ibm_granite_20b = """Question: As a Java Expert, please provide a detailed summary of the following Java code, with the following sections: 
1. Inputs and outputs of the method
2. Business purpose 
3. Detailed functional summary of the method.

```
{}
```
Answer:"""

ibm_granite_34b = """Question: As a Java Expert, please provide a detailed summary of the following Java code, with the following sections: 
1. Inputs and outputs of the method
2. Business purpose 
3. Detailed functional summary of the method

```
{}
```
Answer:"""


codellama_7b = """[INST]Assume you are an expert in understanding JAVA code.

As a Java Expert, please provide a detailed summary of the following Java code, with the following sections: 
1. Inputs and outputs of the method
2. Business purpose 
3. Detailed functional summary of the method.

```
{}
```
[/INST]"""

codellama_34b = """[INST]Assume you are an expert in understanding JAVA code. 

As a Java Expert, please provide a detailed summary of the following Java code, with the following sections: 
1. Inputs and outputs of the method
2. Business purpose
3. Detailed functional summary of the method.

```
{}
```
[/INST]"""


