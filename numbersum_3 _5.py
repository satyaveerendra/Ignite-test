def divisibles(below, *divisors):
    return (n for n in xrange(below) if 0 in (n % d for d in divisors))
print sum(divisibles(1000, 3, 5))
