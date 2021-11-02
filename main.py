# This function determines how many pairs of socks with matching colors there are
# int n represents the number of socks in the pile
# int ar[n] represents the colors of each sock within the array ar

def sockMerchant(n, ar):
    # This dictionary will store the number of stocks with the same color
    socks_per_number = {}
    # int total_pairs will store the final number of pairs with matching colors
    total_pairs = 0
    # Loop through the elements of array ar
    for sock_color in range(len(ar)):
        # Check if the sock color is not in number_of_socks yet
        # If not, add it to the dictionary as the key and its value to 1
        # Otherwise, increment the value of the sock color with 1
        if ar[sock_color] not in socks_per_number:
            socks_per_number[ar[sock_color]] = 1
        else:
            socks_per_number[ar[sock_color]] += 1
    # Loop through the key, value pairs in the dictionary number of socks
    for sock in socks_per_number:
        # For each sock color and the total number, perform a floor division by 2
        # Then, add the result to total_pairs
        total_pairs += socks_per_number[sock] // 2
    # Return the final result with all the matching colors
    return total_pairs


