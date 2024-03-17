
#
# shift
# def encrypt_chunk(chunk, key):
#     key = int(key)
#     all_letters_Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRST"
#     all_letters_Lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmn"
#     if chunk in all_letters_Upper:
#         position1 = all_letters_Upper.find(chunk)
#         result1 = all_letters_Upper[position1 + key]
#         return result1
#     if chunk in all_letters_Lower:
#         position2 = all_letters_Lower.find(chunk)
#         result2 = all_letters_Lower[position2 + key]
#         return result2
#     else:
#         return chunk

# def decrypt_chunk(chunk, key):
#     key = int(key)
#     all_letters_Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     all_letters_Lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
#     if chunk in all_letters_Upper:
#         position1 = all_letters_Upper.find(chunk)
#         result1 = all_letters_Upper[position1 + 26 - key]
#         return result1
#     if chunk in all_letters_Lower:
#         position2 = all_letters_Lower.find(chunk)
#         result2 = all_letters_Lower[position2 + 26 - key]
#         return result2
#     else:
#         return chunk

# def encrypt(plain_text, key):
#     chunk_size = 1
#     cipher_text = "" # accumulator pattern: start with no encrypted test
#     for i in range(0, len(plain_text), chunk_size): # look one chunk at a time
#         chunk = plain_text[i:i + chunk_size] # all chunks the same size
#         a = encrypt_chunk(chunk, key) # most work done in function
#         cipher_text += a
#     return cipher_text

# z = encrypt("Fdhvdu flskhu", 3)
# print(z)

# --------------------
# Vigenère
# def encrypt_chunk(chunk, key):
#     all_letters_Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRST"
#     all_letters_Lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmn"
#     lenth = len(key)
#     key = key.lower()
#     result = ""
#     for i in range(0, len(key)):
#         if chunk[i] in all_letters_Upper:
#             position1 = all_letters_Upper.find(chunk[i])
#             result += all_letters_Upper[position1 + all_letters_Lower.find(key[i])]
#         if chunk[i] in all_letters_Lower:
#             position2 = all_letters_Lower.find(chunk[i])
#             result += all_letters_Lower[position2 + all_letters_Lower.find(key[i])]
#         else:
#             return chunk[i]
#     return result
#
# def encrypt(plain_text, key):
#     chunk_size = len(key)
#     cipher_text = ""
#     for i in range(0, len(plain_text), chunk_size):
#         chunk = plain_text[i:i + chunk_size]
#         a = encrypt_chunk(chunk, key)
#         cipher_text += a
#     return cipher_text
#
# z = encrypt("wo zhen de hen wu yu", "hi")
# print(z)