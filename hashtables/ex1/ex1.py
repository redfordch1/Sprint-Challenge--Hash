
def get_indices_of_item_weights(weights, length, limit):
    nums = dict()        # empty dictionary
    for i, weight in enumerate(weights):       # loops through and numbers the elements in the list
        diff = limit - weight      # difference of limit and weight
        j = nums.get(diff)      # checking to see if that difference is stored in the dictionary  
        if j is not None:     # if its not stored in the dictionary
            return tuple(sorted([i, j], reverse= True))      # this returns if the difference was found in the dictionary, and returns the indexes of the original list and the dictionary  
        nums[weight] = i     # assigning the weight to the index positions in the dictionary
    return None
