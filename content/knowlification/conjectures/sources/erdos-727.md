For a nonnegative integer \(m\), its factorial is \(m!=1\cdot2\cdots m\), with \(0!=1\). For integers \(a,b\), the relation \(a\mid b\) means that \(b=ac\) for some integer \(c\).

Fix an integer \(k\ge 2\), and define the divisibility predicate
\[
P_k(n) :\Longleftrightarrow ((n+k)!)^2\mid (2n)!.
\]

## Conjecture

For every fixed \(k\ge2\), there are infinitely many positive integers \(n\) for which \(P_k(n)\) holds. Equivalently, for every bound \(N\), there is an \(n\ge N\) such that
\[
((n+k)!)^2\mid(2n)!.
\]

The first open case is \(k=2\): are there infinitely many \(n\) such that \(((n+2)!)^2\) divides \((2n)!\)? Prime by prime, the condition is equivalent to
\[
2v_q((n+k)!)\le v_q((2n)!)
\]
for every prime \(q\), where \(v_q(m)\) is the exponent of \(q\) in the prime factorization of \(m\). This reformulation makes visible the competing contributions of primes lying in different parts of the interval from \(1\) to \(2n\).

## Known boundary

The analogous case \(k=1\) is known. A weaker statement, with divisor \((n+k)!(n+1)!\) instead of \(((n+k)!)^2\), is also known for every fixed \(k\). The square in the original problem is therefore the essential extra demand.

## Formal source

This page follows `FormalConjectures/ErdosProblems/727.lean`, which states infinitude using the set of natural numbers satisfying the divisibility condition.
