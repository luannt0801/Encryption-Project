def main():
    nonce = list(range(8))
    k = list(range(32))
    plaintext = "This is Salsa20."
    m = [ord(char) for char in plaintext]
    c, key = salsa20_encrypt(k, nonce, m)
    ciphertext = ''.join([chr(x) for x in c])
    decrypted = ''.join([chr(c[i] ^ key[i]) for i in range(len(m))])
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("After decryption:", decrypted)


def rotate(a, r):
    return ((a << r) & (2 ** 32 - 1)) | (a >> (32 - r))

def quarter_round(y0, y1, y2, y3):
    y1 ^= rotate(y0 + y3, 7)
    y2 ^= rotate(y1 + y0, 9)
    y3 ^= rotate(y2 + y1, 13)
    y0 ^= rotate(y3 + y2, 18)
    return y0, y1, y2, y3

def row_round(y):
    y[0], y[1], y[2], y[3] = quarter_round(y[0], y[1], y[2], y[3])
    y[5], y[6], y[7], y[4] = quarter_round(y[5], y[6], y[7], y[4])
    y[10], y[11], y[8], y[9] = quarter_round(y[10], y[11], y[8], y[9])
    y[15], y[12], y[13], y[14] = quarter_round(y[15], y[12], y[13], y[14])

def column_round(y):
    y[0], y[4], y[8], y[12] = quarter_round(y[0], y[4], y[8], y[12])
    y[5], y[9], y[13], y[1] = quarter_round(y[5], y[9], y[13], y[1])
    y[10], y[14], y[2], y[6] = quarter_round(y[10], y[14], y[2], y[6])
    y[15], y[3], y[7], y[11] = quarter_round(y[15], y[3], y[7], y[11])

def double_round(x):
    column_round(x)
    row_round(x)

def little_endian(b0, b1, b2, b3):
    return b0 + b1 * 256 + b2 * 256 ** 2 + b3 * 256 ** 3

def little_endian_reverse(z):
    b0 = z & 255
    b1 = (z >> 8) & 255
    b2 = (z >> 16) & 255
    b3 = (z >> 24) & 255
    return [b0, b1, b2, b3]

def salsa20(x):
    y = []
    result = []
    for i in range(16):
        x0, x1, x2, x3 = x[4 * i : 4 * i + 4]
        y.append(little_endian(x0, x1, x2, x3))
    z = y.copy()
    for _ in range(10):
        double_round(z)
    for i in range(16):
        result += little_endian_reverse(z[i] + y[i])
    return result

def salsa20_exp(k, n):
    o0, o1, o2, o3 = [101, 120, 112, 97], [110, 100, 32, 51], [50, 45, 98, 121], [116, 101, 32, 107]
    t0, t1, t2, t3 = [101, 120, 112, 97], [110, 100, 32, 49], [54, 45, 98, 121], [116, 101, 32, 107]
    if len(k) == 16:
        return salsa20(t0 + k + t1 + n + t2 + k + t3)
    elif len(k) == 32:
        return salsa20(o0 + k[:16] + o1 + n + o2 + k[16:] + o3)

def i_to_8byte(b):
    bi = []
    for i in range(8):
        bx = (b >> (8 * i)) & 255
        bi.append(bx)
    return bi

def salsa20_encrypt(k, v, m):
    c = []
    key = []
    for i in range(len(m) // 64 + 1):
        key += salsa20_exp(k, v + i_to_8byte(i))
    for j in range(len(m)):
        c.append(m[j] ^ key[j])
    return c, key


if __name__ == '__main__':
    main()
