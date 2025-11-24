import numpy as np

def count_values_in_bins(data, bin_edges):
    ### Replace with your own code (begin) ###
    B=len(bin_edges)-1
    counts=np.zeros(B,dtype=int)
    for i in range(B):
        left=bin_edges[i]
        right=bin_edges[i+1]
        if i==B-1:
         mask = (data >= left) & (data <= right)
        else:
            mask = (data >= left) & (data < right)
        counts[i] = np.sum(mask)

    return counts
    ### Replace with your own code (end)   ###

