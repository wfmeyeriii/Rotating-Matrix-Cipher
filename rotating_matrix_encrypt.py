import numpy as np

M = np.zeros((5,5),str)
H = np.zeros((5,5),str)
A = np.zeros((5,5),str)

letters = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

key = input("Enter the key. No spaces, no numbers; only letters: ")

for char in key:
    if not char.isalpha():
        exit("Invalid key. Try again.")

i = 0
j = 0
for char in key:
    if char == "j":
        char = "i"
    if char in letters:
        M[i,j] = char
        letters.remove(char)
        # print(letters)
        if j == 4:
            i += 1
            j = -1
        j += 1
# print(M)
for letter in letters:
    M[i, j] = letter
    # print(letters)
    if j == 4:
        i += 1
        j = -1
    j += 1

# print(M)

plaintext = input("Enter the plaintext: ")

ciphertext = ""


(a,b) = (0,0)

for i in range(5):
    for j in range(5):
        H[i,j] = M[j,(-i+4)%5]
        A[(i+1)%5,j%5] = H[i,j]
# print(f"{A = }")

for char in plaintext:
    # print(f"{char = }\n{A = }")
    if char == "j":
        char = "i"
    x = np.where(A == char)
    (a,b) = (int(x[0][0]),int(x[1][0]))
    letter = M[a,b]
    ciphertext += letter
    # print(f"{ciphertext = }\n")

    y = np.where(A == letter)
    (n,m) = (int(y[0][0]),int(y[1][0]))
    for i in range(5):
        for j in range(5):
            H[i,j] = A[j,(-i+4)%5]
    for i in range(5):
        for j in range(5):
            A[(i+n+m+1)%5,(j-n+m)%5] = H[i,j]

print(f"The ciphertext for \"{plaintext}\" is:\n\t{ciphertext}")
