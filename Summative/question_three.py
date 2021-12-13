import timeit
""" 
    Helper function to create a 2D matrix 
    based on the key and length of the text
"""
def create_matrix(text, key):
    matrix = []
    columns = key
    rows = len(text)

    for i in range(columns):
        submatrix = [''] * rows
        matrix.append(submatrix)

    return matrix

""" 
    Function to encrypt a text based on a key
"""
def encrypt(text, key):
    encrypted = ''
    matrix = create_matrix(text, key)

    # If key is 2
    if key == 2:
        # Store the text in the 2D matrix
        for i in range(len(text)):
            if i % 2 == 0:
                matrix[0][i] = text[i]
            else:
                matrix[1][i] = text[i]
        
        # Concatenate the strings from the 2D matrix 
        # Starting from the 1st submatrix, then the 2nd submatrix
        for i in range(len(text)):
            encrypted += matrix[0][i]
        for i in range(len(text)):
            encrypted += matrix[1][i]

    # If key is 3
    elif key == 3:
        # Using a counter to keep track of the index in the matrix
        # Storing the letters in matrix depending on the index number
        counter = 0
        for i in range(len(text)):
            if counter == 0:
                matrix[0][i] = text[i]
                counter += 1
            elif counter == 1:
                matrix[1][i] = text[i]
                counter += 1
            elif counter == 2:
                matrix[2][i] = text[i]
                counter = 0
        
        # Concatenating the letters in matrix per submatrix
        # Starting from the 1st, 2nd and 3rd matrix
        for i in range(len(text)):
            encrypted += matrix[0][i]
        for i in range(len(text)):
            encrypted += matrix[1][i]        
        for i in range(len(text)):
            encrypted += matrix[2][i]

    return encrypted


""" 
    Function to decrypt a text based on a key
"""
def decrypt(text, key):
    decrypted = ''
    matrix = create_matrix(text, key)

    # If key is 2
    if key == 2:
        # Using a counter to kee track of the len of text
        n = 0
        for i in range(len(text)):
            # Only store the letter if the index is % 2
            if i % 2 == 0 and n <= len(text)//2:
                matrix[0][i] = text[n]
                n += 1
        
        for i in range(len(text)):
            if i % 2 != 0:
                matrix[1][i] = text[n]
                n += 1

        # Concatenate the letter by submatrix in order
        for i in range(len(text)):
            decrypted += matrix[0][i]
            decrypted += matrix[1][i]

    # If key is 3
    # Same principle as encryption 
    # Based on the counter, index the letter to each submatrix
    elif key == 3:
        counter = 0
        n = 0
        for i in range(len(text)):
            if counter == 0:
                matrix[0][i] = text[n]
                counter += 1
                n += 1

            elif counter == 1:
                counter += 1
               
            elif counter == 2:
                counter = 0
        
        counter = 0
        for i in range(len(text)):
            if counter == 0:
                counter += 1

            elif counter == 1:
                matrix[1][i] = text[n]
                counter += 1
                n += 1
               
            elif counter == 2:
                counter = 0

        counter = 0
        for i in range(len(text)):
            if counter == 0:
                counter += 1

            elif counter == 1:
                counter += 1
                
            elif counter == 2:
                matrix[2][i] = text[n]
                counter = 0
                n += 1      
        
        # Concatenating the letters in matrix per submatrix
        # Starting from the 1st, 2nd and 3rd matrix
        for i in range(len(text)):
            decrypted += matrix[0][i]
            decrypted += matrix[1][i]
            decrypted += matrix[2][i]

    return decrypted


print(encrypt('Plain Text', 2))
print(decrypt(encrypt('Plain Text', 2), 2))

print(encrypt('Plain Text', 3))
print(decrypt(encrypt('Plain Text', 3), 3))

print(encrypt('Hello World', 2))
print(decrypt(encrypt('Hello World', 2), 2))

print(encrypt('Hello World', 3))
print(decrypt(encrypt('Hello World', 3), 3))


# Uncomment to print the running time of the algorithms
# text = 'Plain text'
# key2 = 2
# key3 = 3

# enc2 = 'PanTxli et'
# enc3 = 'PiTtlnea x'

# def encryption_time():
#     t1_timer = timeit.Timer("text, key2, encrypt(text, key2)", setup="from __main__ import encrypt, text, key2")
#     t2_timer = timeit.Timer("text, key3, encrypt(text, key3)", setup="from __main__ import encrypt, text, key3")
#     t1 = t1_timer.timeit(number=1000)
#     t2 = t2_timer.timeit(number=1000)

#     print(t1, t2)


# def decryption_time():
#     t1_timer = timeit.Timer("enc2, key2, decrypt(enc2, key2)", setup="from __main__ import decrypt, enc2, key2")
#     t2_timer = timeit.Timer("enc3, key3, decrypt(enc3, key3)", setup="from __main__ import decrypt, enc3, key3")
#     t1 = t1_timer.timeit(number=1000)
#     t2 = t2_timer.timeit(number=1000)

#     print(t1, t2)

