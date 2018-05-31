#python3
#primes_list.py

def check_if_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        return True

def get_list_of_primes_to(upper_number):
    primes_list = []
    for j in range(upper_number):
        is_prime = check_if_prime(j)
        if is_prime:
            primes_list.append(j)
    return primes_list

upper_number = int(input('Enter upper number >> '))
primes_list = get_list_of_primes_to(upper_number)
print('The primes to %s are ' % upper_number + str(primes_list) )


