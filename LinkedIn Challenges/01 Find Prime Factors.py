
def generate_primes(n: int) -> list:
    """Generates list of primes up to and including n using a sieve of erasthosthenes"""
    candidates = range(2,n+1)
    primes = []
    i = 0
    while len(candidates) > 0:
        p = candidates[0]
        primes.append(p)
        candidates = list(filter(lambda x: x%p != 0, candidates))
        i += 1
    return primes
    # now, starting at 2, we eliminate all the multiples of the numbers

def find_prime_factors(n: int) -> list:
# Going to find divisors of n and then keep dividing down until I can't any more
# We have a list of primes, p_i, up to sqrt(n) because at most n is (p_i)^2
   
    primes = generate_primes(n)
    prime_factors = []
    while n > 1:
        for p in primes:
            if n % p == 0: # if p divides into n
                n = n/p # fork and divide by p
                prime_factors.append(p)
                break
            else:
                pass
    return prime_factors

print(find_prime_factors(630))