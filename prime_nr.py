def primes():

    print("""
    A prime number is a natural number with exactly 2 factors
    wich means that it can only be diveded by 1 and itself,
    and it's not evenly divisible by any other whole number.
    
    Here you can search for how many prime numbers there are 
    within a span and which numbers within that span that
    are prime. Search between a defined starting number
    and a defined ending number by your choice.
    """)

    i = int(input("Enter the start number: "))
    end_nr = int(input("Enter the end number: "))
    counter = 0

    while(i < end_nr):
        if i == 0 : i += 2 
        elif i == 1 : i += 1
        j = 2
        while(j <= (i/j)):
            if not(i%j): break
            j += 1
        if (j > i / j):
            counter += 1
            print(i, "is prime. ")
        i += 1
    print(f"\nTotal number of primes {counter}\n")

primes()