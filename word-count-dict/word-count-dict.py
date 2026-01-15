import numpy as np
def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    if len(sentences) == 0:
        return {}
    
    word_map = {}
    for sentence in sentences:
        for word in sentence:
            if word not in word_map.keys():
                word_map[word] = 1
            else:
                word_map[word] += 1
    return word_map