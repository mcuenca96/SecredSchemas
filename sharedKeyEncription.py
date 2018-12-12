import sys
import gmpy
import random



def getPrimes(moduleDigits):

    prime_list = []
    x = 1

    # Agafem el ultim primer amb un menor numero de digits
    while len(str(x)) < moduleDigits:
        x = gmpy.next_prime(x)

    x = gmpy.next_prime(x)

    while len(str(x)) < moduleDigits + 1:

        prime_list.append(str(x)[:])
        x = gmpy.next_prime(x)


    return int(''.join(random.sample(prime_list,1)))


def genFunction(module, p, secret):

    return random.sample(range(0, module - 1), p - 1)




if __name__ =="__main__":

    p = int(raw_input("Number of participants: "))
    secret = int(raw_input("Secret: "))
    moduleDigits = int(raw_input("Number of digits of the module: "))
    # string_input = raw_input("Set of public keys: ")
    # input_list = string_input.split()
    # public_keys = [int(a) for a in input_list]


    module = getPrimes(moduleDigits)
    print genFunction(module, p, secret)
