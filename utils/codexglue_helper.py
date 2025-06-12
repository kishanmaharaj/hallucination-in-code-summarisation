from args import args
import json

descrpition_codexglue="""
After preprocessing dataset, you can obtain three .jsonl files, i.e. train.jsonl, valid.jsonl, test.jsonl
For each file, each line in the uncompressed file represents one function. 
One row is illustrated below:

repo: the owner/repo
path: the full path to the original file
func_name: the function or method name
original_string: the raw string before tokenization or parsing
language: the programming language
code/function: the part of the original_string that is code
code_tokens/function_tokens: tokenized version of code
docstring: the top-level comment or docstring, if it exists in the original string
docstring_tokens: tokenized version of docstring


### Data Statistic
| Programming Language | Training |  Dev   |  Test  |
| :------------------- | :------: | :----: | :----: |
| Python               | 251,820  | 13,914 | 14,918 |
| PHP                  | 241,241  | 12,982 | 14,014 |
| Go                   | 167,288  | 7,325  | 8,122  |
| Java                 | 164,923  | 5,183  | 10,955 |
| JavaScript           |  58,025  | 3,885  | 3,291  |
| Ruby                 |  24,927  | 1,400  | 1,261  |

"""

def preprocess_codexglue(required_entries, describe=False, java_data_path=args.java_data_path.format(args.splits)):
    """
    Helper function for inference
    ----------
    Parameters
    ----------
    java_data_path: string
    path to codexglue Java data
    
    required_entities: list
    list of entities to be returned 
    
    ----------
    Returns 
    ----------
    returned_entries: dict
    a dict containing the entries in required_entries
    """
    with open(java_data_path, "r") as file:
        java_data = [json.loads(line) for line in file]

    if describe:
        print(descrpition_codexglue)
        print(f"Keys: {list(java_data[0].keys())}")

    returned_entries = {}
    for entry in required_entries:
        return_entry = []
        
        for i in range(len(java_data)):
            return_entry.append(java_data[i][entry])

        returned_entries[entry] = return_entry

    return returned_entries
 
    