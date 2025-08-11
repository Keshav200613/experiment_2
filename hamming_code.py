
def calculate_parity_bits_length(data_bits_length):
    r = 0
    while (2 ** r) < (data_bits_length + r + 1):
        r += 1
    return r

def insert_parity_bits(data_bits, r):
    j = 0
    k = 0
    m = len(data_bits)
    res = ''
    total_length = m + r
    for i in range(1, total_length + 1):
        if i == 2 ** j:
            res = res + '0'
            j += 1
        else:
            res = res + data_bits[k]
            k += 1
    return res

def calculate_parity_bits(arr, r):
    n = len(arr)
    arr = list(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[j - 1])
        arr[(2 ** i) - 1] = str(val)
    return ''.join(arr)

def detect_and_correct(hamming_code):
    n = len(hamming_code)
    r = 0
    while (2 ** r) < (n + 1):
        r += 1
    error_pos = 0
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(hamming_code[j - 1])
        if val != 0:
            error_pos += 2 ** i
    if error_pos == 0:
        print("No error detected in received Hamming code.")
        return hamming_code
    else:
        print(f"Error detected at position: {error_pos}")
        hamming_code = list(hamming_code)
        hamming_code[error_pos - 1] = '1' if hamming_code[error_pos - 1] == '0' else '0'
        print(f"Corrected Hamming code: {''.join(hamming_code)}")
        return ''.join(hamming_code)

def main():
    print("--- Hamming Code Generation and Correction ---")
    data_bits = input("Enter the data bits (e.g., 1011): ")
    m = len(data_bits)
    r = calculate_parity_bits_length(m)
    print(f"Number of parity bits required: {r}")
    arr_with_parity = insert_parity_bits(data_bits, r)
    hamming_code = calculate_parity_bits(arr_with_parity, r)
    print(f"Generated Hamming code: {hamming_code}")

    simulate = input("Do you want to simulate a single-bit error? (y/n): ")
    if simulate.lower() == 'y':
        pos = int(input(f"Enter the position to flip (1 to {len(hamming_code)}): "))
        hamming_code_with_error = list(hamming_code)
        hamming_code_with_error[pos - 1] = '1' if hamming_code_with_error[pos - 1] == '0' else '0'
        hamming_code_with_error = ''.join(hamming_code_with_error)
        print(f"Hamming code with error at position {pos}: {hamming_code_with_error}")
        detect_and_correct(hamming_code_with_error)
    else:
        print("No error simulated.")
        detect_and_correct(hamming_code)

if __name__ == "__main__":
    main()