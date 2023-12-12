number_of_bits = 64

# bảng ip-1 hoán vị
final_perm = [40, 8, 48, 16, 56, 24, 64, 32,  
              39, 7, 47, 15, 55, 23, 63, 31,  
              38, 6, 46, 14, 54, 22, 62, 30,  
              37, 5, 45, 13, 53, 21, 61, 29,  
              36, 4, 44, 12, 52, 20, 60, 28,  
              35, 3, 43, 11, 51, 19, 59, 27,  
              34, 2, 42, 10, 50, 18, 58, 26,  
              33, 1, 41, 9, 49, 17, 57, 25]

# thực hiện hoán vị cho plain text
def initial_permutation(plain_text,initial_perm, no_bits): 
    permutation="" 
    for i in range(0,no_bits): 
        permutation=permutation + plain_text[initial_perm[i]-1] 
    return permutation

if __name__ == "__main__":
    # output R16 & L16 là:
    # 0000 1010 0100 1100 1101 1001 1001 01010100 0011 0100 0010 0011 0010 0011 0100
    R16L16='0000101001001100110110011001010101000011010000100011001000110100'
    print('Input:                     ', R16L16)

    R16L16 = initial_permutation(R16L16, final_perm, number_of_bits)

    print('After initial permutation: ', R16L16)
    # print('Cipher_text:                1000010111101000000100110101010000001111000010101011010000000101')
