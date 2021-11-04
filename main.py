# This function determines how many pairs of socks with matching colors there are
# int n represents the number of socks in the pile
# int ar[n] represents the colors of each sock within the array ar

def sockMerchant(n, ar):
    # int total_pairs will store the final number of pairs with matching colors
    total_pairs = 0
    
    # Loop through the elements of set ar 
    # Using set to remove duplicates and remain with only the unique colors
    for i in set(ar):
        # For each sock color and its total number got from .count method, perform a floor division by 2
        # Then, add the result to total_pairs
        total_pairs += ar.count(i) // 2        
    
    # Return the final result with all the matching colors
    return total_pairs


