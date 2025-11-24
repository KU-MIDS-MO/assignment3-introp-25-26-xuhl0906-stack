import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    ### Replace with your own code (begin) ###
    cleaned=np.array(scores,dtype=float)
    cleaned[cleaned<min_score]=min_score
    cleaned[cleaned>max_score]=max_score
    scaled = (cleaned - min_score) / (max_score - min_score)
    return scaled    
    ### Replace with your own code (end)   ###
