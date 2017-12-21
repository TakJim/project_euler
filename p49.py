#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
#increases by 3330, is unusual in two ways: (i) each of the three terms 
#are prime, and, (ii) each of the 4-digit numbers are permutations of 
#one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit 
#primes, exhibiting this property, but there is one other 4-digit 
#increasing sequence.

#What 12-digit number do you form by concatenating the three terms in 
#this sequence?

### generate the list of primes within 4-digit
primes = [2]
for num in range(2,10000):
    for prime in primes:
        if num % prime == 0:
            break
    else:
        primes.append(num)
#print(primes)

### make the list of primes which are permutations of one another.
for prime in primes:
    if prime < 1000:
        continue
    sequence = []
    perm = list( str( prime ) )
    perm.sort()
    for prime2 in primes[ primes.index(prime) :]:
        if prime < 1000:
            continue
        permx = list( str( prime2 ) )
        permx.sort()
        if permx == perm:
            sequence.append(prime2) 
            primes[primes.index(prime2)]=0 #あやしい

### find arithmetric sequence meet the given criteria
    if len(sequence) >= 3:
        for a in sequence:
            for b in sequence[sequence.index(a)+1:]:
                if b + b - a in sequence and a!=b:
                    print(a, b, 2*b-a,"D=",b-a)

