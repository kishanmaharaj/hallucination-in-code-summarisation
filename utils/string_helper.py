import re


def find_substring_occurrences(main_str, sub_str, label=""):
    """
    Find the starting and ending index of all occurrences of a substring in a string at the word level,
    accounting for special characters.
    
    Parameters:
    main_str (str): The main string to search within.
    sub_str (str): The substring to search for.
    label (str): label of the substring (entity_type)
    
    Returns:
    occurrences (list): A list of lists where each list contains the starting, ending index of an occurrence along with the label of the entity
    """
    
    occurrences = []
    # Create a regular expression pattern to match the substring as a whole word
    pattern = re.compile(r'\b' + re.escape(sub_str) + r'\b')
    
    # Find all matches using the regular expression
    for match in pattern.finditer(main_str):
        start = match.start()
        end = match.end()
        occurrences.append([start, end, label])
    
    return occurrences



def get_relevant_sents(longer_sent, current_mapped_ent):
    """
    Find the sentences containing the 'current_mapped_ent' at the word level, accounting for special characters.
    
    Parameters:
    longer_sent (list of str): List consisting of sentences more than 4 chars.
    current_mapped_ent (str): Name of the entity.
    
    Returns:
    relevant_sents (list of str): A list of strings containing the sentences with 'current_mapped_ent' occurrences.
    """
    
    # Create a regular expression pattern to match the current_mapped_ent as a whole word
    pattern = re.compile(r'\b' + re.escape(current_mapped_ent) + r'\b')
    
    # Filter sentences that contain the entity as a whole word
    relevant_sents = [x.strip() for x in longer_sent if pattern.search(x)]

    return relevant_sents
    