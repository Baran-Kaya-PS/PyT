def count_bits(n : int) -> int:
    count = 0
    n_str = str(n)[::-1]
    n_size = len(n_str)
    for i in range(n_size):
        int_val = int(n_str[i])
        if int_val == 1:
            count += 2**i
        print(int_val)
    return count

print(count_bits(1011))