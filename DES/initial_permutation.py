number_of_bits = 64

# Hexadecimal to binary conversion 
def hexa_to_bin(msg): 
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
  bin = "" 
  for i in range(len(msg)): 
    bin = bin + mp[msg[i]] 
  return bin
    
# Binary to hexadecimal conversion 
def bin_to_hexa(msg): 
  mp = {"0000" : '0',  
        "0001" : '1', 
        "0010" : '2',  
        "0011" : '3', 
        "0100" : '4', 
        "0101" : '5',  
        "0110" : '6', 
        "0111" : '7',  
        "1000" : '8', 
        "1001" : '9',  
        "1010" : 'A', 
        "1011" : 'B',  
        "1100" : 'C', 
        "1101" : 'D',  
        "1110" : 'E', 
        "1111" : 'F' } 
  hex="" 
  for i in range(0,len(msg),4): 
    ch="" 
    ch=ch+msg[i] 
    ch=ch+msg[i+1]  
    ch=ch+msg[i+2]  
    ch=ch+msg[i+3]  
    hex=hex+mp[ch] 
  return hex

# check đủ input đầu vào là 16 kí tự hay không
def pad(msg):
    if(len(msg)%16!=0):
        print("Padding required")
        for i in range(abs(16-(len(msg)%16))):
            msg=msg+'0'
    # else:
    #     print("No padding required")
    return(msg)

# bảng ip hoán vị
initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,  
                60, 52, 44, 36, 28, 20, 12, 4,  
                62, 54, 46, 38, 30, 22, 14, 6,  
                64, 56, 48, 40, 32, 24, 16, 8,  
                57, 49, 41, 33, 25, 17, 9, 1,  
                59, 51, 43, 35, 27, 19, 11, 3,  
                61, 53, 45, 37, 29, 21, 13, 5,  
                63, 55, 47, 39, 31, 23, 15, 7]  

# thực hiện hoán vị cho plain text
def initial_permutation(plain_text,initial_perm, no_bits): 
    permutation="" 
    for i in range(0,no_bits): 
        permutation=permutation + plain_text[initial_perm[i]-1] 
    return permutation

if __name__ == "__main__":
    print("input plain text:")
    plain_text=input()

    plain_text=pad(plain_text)
    print("after padding: ", plain_text)

    plain_text = hexa_to_bin(plain_text)
    print("hexa to bin:", plain_text)

    plain_text = initial_permutation(plain_text, initial_perm, number_of_bits)
    print('After initial permutation: ', plain_text)

    plain_text = bin_to_hexa(plain_text)
    print('bin to hexa', plain_text)