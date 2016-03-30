
import eular3


def main():
    upperlimit = 2000000
    prime_sum = 0

    for i in range(upperlimit):
        if eular3.is_prime(i):
            prime_sum += i

    print('The sum of all primes up to {} = {}'.format(upperlimit, prime_sum))

if __name__ == "__main__":
    main()
