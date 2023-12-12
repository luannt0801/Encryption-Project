# Initial Permutation Matrix
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Inverse Permutation Matrix
InvP = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

# Permutation made after each SBox substitution
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# Initial permutation on key
PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# Permutation applied after shifting key (i.e gets Ki+1)
PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

# Expand matrix to obtain 48bit matrix
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# SBOX represented as a three dimentional matrix
# --> SBOX[block][row][column]
SBOX = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
]

# Shift Matrix for each round of keys
SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

#Convert string to bitarray
def str_to_bitarray(msg):
    # Converts string to a bit array.
    mp = {'0' : "0000",  
          '1' : "0001", 
          '2' : "0010",  
          '3' : "0011", 
          '4' : "0100", 
          '5' : "0101",  
          '6' : "0110", 
          '7' : "0111",  
          '8' : "1000", 
          '9' : "1001",  
          'A' : "1010", 
          'B' : "1011",  
          'C' : "1100", 
          'D' : "1101",  
          'E' : "1110", 
          'F' : "1111" } 
    bin_str = "" 
    for char in msg:
        bin_str += mp[char]
    
    binary_list = [int(bit) for bit in bin_str]
    return binary_list

def binary_to_hex(binary_list):
    #convert bitarray to hexstring (in hoa)
    hex_string = ''.join([hex(int(''.join(map(str, binary_list[i:i+4])), 2))[2:].upper() for i in range(0, len(binary_list), 4)])
    return hex_string



class DES:
    def __init__(self):
        self.key_text = ""
        self.plain_text = ""
        self.all_keys = []
        self.len_plaintext = 0
      
    @staticmethod
    #performs left shift
    def left_shift(m_array, round_num):
        num_shift = SHIFT[round_num]
        return m_array[num_shift:] + m_array[:num_shift]

    @staticmethod
     #performs permutation 2
    def pc2(m_array):
        keyarray_48bit = []
        for i in range(0, len(PC_2)):
            keyarray_48bit.append(m_array[PC_2[i] - 1])
        return keyarray_48bit

    @staticmethod
    #single funtion to call initial permutation and inverse permutation  
    def perms_on_plaintext(m_array, is_inverse_permutation):
        perm_array = IP if is_inverse_permutation is False else InvP
        processed_array = []
        for i in range(0, len(perm_array)):
            processed_array.append(m_array[perm_array[i] - 1])
        return processed_array

    @staticmethod
    #XOR function
    def XOR(array_one, array_two):
        # xor function 
        return [i ^ j for i, j in zip(array_one, array_two)]

    @staticmethod
    #splits the text in blocks of 8 bits
    def split_long_text(stuff_to_split, split_at_every):
        return [stuff_to_split[i:i + split_at_every] for i in range(0, len(stuff_to_split), split_at_every)]

    def sbox_substition(self, m_array):
        # Apply sbox subsitution on the bits
        sixbitarrays = self.split_long_text(m_array, 6)

        substresult = []
        s = ""

        for j in range(0, len(sixbitarrays)):
            row = int(str(sixbitarrays[j][0]) + str(sixbitarrays[j][5]), 2)
            col = int(
                str(sixbitarrays[j][1]) + str(sixbitarrays[j][2]) + str(sixbitarrays[j][3]) + str(sixbitarrays[j][4]),
                2)
            sboxintvalue = SBOX[j][row][col]
            s = s + format(sboxintvalue, '04b')  # converts int to bin string (4) 
        for c in s:
            substresult.append(int(c))
        return substresult

    def createKeys(self,key):
        key_bitarray = str_to_bitarray(key)
        perm_key_bitarray = []
        for i in range(0, len(PC_1)):
            perm_key_bitarray.append(key_bitarray[PC_1[i]-1])

        key_left = perm_key_bitarray[:28]
        key_right = perm_key_bitarray[28:]

        for i in range(0, 16):
            key_left = self.left_shift(key_left, i)
            key_right = self.left_shift(key_right, i)
            self.all_keys.append(self.pc2(key_left + key_right))

    @staticmethod
    def permute(m_array):
        permuted_array = []
        for i in range(0, len(P)):
            permuted_array.append(m_array[P[i] - 1])
        return permuted_array

    def performRounds(self, m_array, is_encrypt):
        left_part = m_array[:32]
        right_part = m_array[32:]

        if is_encrypt:
            for i in range(0, 16):
                temp_array = right_part
                right_part = self.XOR(left_part, self.performRound(right_part, i))
                left_part = temp_array
            return right_part + left_part
        else:
            for i in range(16, 0, -1):
                temp_array = right_part
                right_part = self.XOR(left_part, self.performRound(right_part, i - 1))
                left_part = temp_array
            return right_part + left_part

    def performRound(self, right_part, round_num):
        # Performs a single round of the DES algorithm
        expanded_array = []
        for i in range(0, len(E)):
            expanded_array.append(right_part[E[i] - 1])

        temp_array = self.XOR(expanded_array, self.all_keys[round_num])
        sboxresult = self.sbox_substition(temp_array)
        return self.permute(sboxresult)

    def encrypt(self, key, pln_text):
        self.key_text = key
        self.plain_text = pln_text
        self.createKeys(key) # Hiếu , Linh
        s = ""
        self.len_plaintext = len(pln_text)
        str_bitarray = str_to_bitarray(pln_text) # chuoi bit
        while len(str_bitarray)%64 != 0:
            str_bitarray.append(0)
        bitarray = self.split_long_text(str_bitarray,64)
        for i in range(0,len(bitarray)):
            s = s + self.encrypt_main(bitarray[i])
        return s     
        
    def encrypt_main(self, bit_arr):
        temp_array = self.perms_on_plaintext(bit_arr, False) # Luân
        round_performed_array = self.performRounds(temp_array, True) # Minh , TRung, Quang , Sơn, Đăng, Hiền
        ciphertext = self.perms_on_plaintext(round_performed_array, True) #Luân
        return binary_to_hex(ciphertext)

    def decrypt(self, encrypted_text, key_text):
        self.key_text = key_text
        self.createKeys(key_text)
        s = ""
        bit_array = str_to_bitarray(encrypted_text)
        while len(bit_array)%64 != 0:
            bit_array.append(0)
        bitarray = self.split_long_text(bit_array,64)
        for i in range(0,len(bitarray)):
            s = s + self.decrypt_main(bitarray[i])
        return s     
    
    def decrypt_main(self,bit_arr):
        inversed_array = self.perms_on_plaintext(bit_arr, False)
        temp_array = self.performRounds(inversed_array, False)
        straight_array = self.perms_on_plaintext(temp_array, True)
        return binary_to_hex(straight_array)

'''
des = DES()
key = "BBCC1938472AEEFF"
plain_text = "C0B7A8D05F3A829C"
print("Plain Text is: " + plain_text)
ciphertext = des.encrypt("BBCC1938472AEEFF","C0B7A8D05F3A829C")
print("Encrypted Text is: " + ciphertext)
dec_text = des.decrypt(ciphertext, key)
print("Decrypted Text is: " + dec_text)

'''
def tripleDes (key,plainText):# Đức
    print("Plain text is " + plainText)
    des = DES()
    des2 = DES()
    des3 = DES()
    if len(plainText) % 2 != 0:
        print("Input is not valid hexadecimal string. Permitted characters are: [a-fA-F0-9 \n\r\t\-] and the string must have even length.")
    key = des.split_long_text(key,16)
    # encryption
    ciphertext1 = des.encrypt(key[0], plainText)
    #print("Encrypted Text1 is: " +ciphertext1)
    ciphertext2 = des2.decrypt(ciphertext1,key[1])
    #print("Decrypted Text1 is: " +ciphertext2)
    ciphertext3 = des3.encrypt(key[2], ciphertext2)
    print("Encrypted Text is: " +ciphertext3)

    # decryption
    dec_text1 = des3.decrypt(ciphertext3, key[2])
    #print("Decrypted Text1 is: " + dec_text1)
    dec_text2 = des2.encrypt(key[1],dec_text1)
    #print("Encrypted Text2 is: " + dec_text2)
    dec_text3  = des.decrypt(dec_text2, key[0])
    print("Decrypted Text is: " + dec_text3[0:des.len_plaintext])
    
key1 = "AABB09182736CCDD" # 8 byte
key2 = "BBCC1938472AEEFF"
key3 = "CCDD28495B3EAAFF"
key = key1 + key2 + key3 # 24 byte = 192 bit
#plain_text = "123456ABCD132536"
plain_text = "123456ABCD132536123456ABCD1325" #15 byte
tripleDes(key, plain_text)

#expected : 0C86BD298CE7B5A3EFA357ABE376CEEA