def check_if_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_primes_list_to(upper_number):
    primes_list = []
    for j in range(upper_number):
        is_prime = check_if_prime(j)
        if is_prime:
            primes_list.append(j)
    return primes_list

primes_list = get_primes_list_to(100)
print(primes_list)