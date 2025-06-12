# https://huggingface.co/docs/transformers/en/main_classes/text_generation

from args import args
import os


def inference(tokenizer, model, prompt, top_p=args.top_p, max_new_tokens=args.max_new_tokens, temperature=args.temperature):
    """
    Helper function for inference
    ----------
    Parameters
    ----------
    tokenizer: tokenizer object
    Tokenizer of the LM

    model: model object from huggingface
    Model from Huggingface

    prompt: string
    prompt for the generative model
    ----------
    Returns the generated text
    """
    
    model_inputs = tokenizer([prompt], return_tensors="pt").to(args.device)
    
    
    # For removal of input string from the output string
    input_ids_cutoff = model_inputs.input_ids.size(dim=1) 
    
    generated_ids = model.generate(**model_inputs,
                                   max_new_tokens=max_new_tokens,
                                   top_p = top_p,
                                   temperature = temperature,
                                   do_sample=True, 
                                   pad_token_id=tokenizer.eos_token_id)
    
    completion = tokenizer.decode(
    generated_ids[0][input_ids_cutoff:],
    skip_special_tokens=True)
    
    return completion


def update_file_name(filename, data_folder='./saved_data/gpt_evaluations/action_verification_entity_level/'):
    """
    Updates the file name based on the current contents of the given directory -> Avoids overwriting
    ----------
    Parameters
    ----------
    filename: string
    Specified file name
    
    data_folder: string
    Specified data directory 
    ----------
    Returns the generated text
    """
    
    folder_content = list(os.listdir(data_folder))
    run = 1
    extension = ".csv"

    while filename.split(extension)[0][:-1]+str("_run_")+str(run)+extension in  folder_content:
        run = run+1
            
    return filename.split(extension)[0][:-1]+str("_run_")+str(run)+extension


def reload_lib(module):
    """
    Reloads a library
    ----------
    Parameters
    ----------
    module: library class
    the library to be reloaded
    ----------
    Returns None
    """
    import importlib
    importlib.reload(module)

