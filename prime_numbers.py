def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def print_primes(limit):
    """Print all prime numbers up to the given limit"""
    print(f"Prime numbers up to {limit}:")
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num, end=" ")
    print()  # New line at the end

def print_first_n_primes(n):
    """Print the first n prime numbers"""
    print(f"First {n} prime numbers:")
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1
    print()  # New line at the end

# Example usage
if __name__ == "__main__":
    # Print primes up to 50
    print_primes(50)
    
    print()  # Empty line for separation
    
    # Print first 10 prime numbers
    print_first_n_primes(10)