+++
id = "proofs/grh/upper-divisibility/classes-of-primes"
title = "Small non-split primes, primes congruent to plus or minus one modulo m, and exceptional primes"
kind = "definition"
summary = "The classes of primes distinguished in the local proof of divisibility, with the loss, transfer exponent and collision exponent attached to a prime."
aliases = ["exceptional prime", "small non-split prime", "loss at a prime", "transfer exponent", "collision exponent"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsSmallNonsplit", "New.Data.IsPlusMinusOneModLifts", "New.Data.loss", "New.Data.ceilLogLifts", "New.Data.transferExponent", "New.Data.collisionExponent", "New.Data.o₀", "New.Data.IsExceptional"]
lean_files = ["src/New/UpperBound/Size/ShortColumns.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] for the parameters \((q_0,d)\), with scales \(x_1\), \(b\), \(a=xb\), number of lifts \(m\), ranks \(n_j=k+j(t+1)\), and \(f\) infinite places of \(E\). Let \(\chi_K\) be the [[?lean:New.chiK|quadratic character]] of \(K=\mathbb{Q}(\sqrt{-d})\). Let \(p\) be a natural number; the formulas are used for primes. (For \(p\le1\) the source's conventions apply: a quotient by \(0\) is \(0\), and the rounded-up logarithm to a base \(p\le1\) is \(0\).)

- \(p\) is **small non-split** if \(p<x_1\) and \(\chi_K(p)\ne 1\).
- \(p\) is **\(\pm1\) modulo the number of lifts** if \(m\mid p-1\) (with \(p-1\) read as \(0\) for \(p=0\)) or \(m\mid p+1\).
- The **loss** at \(p\) is \(\operatorname{loss}(p)=f(\log b)^2\cdot\dfrac{a}{p}\cdot\varepsilon_p\), where \(\varepsilon_p=m\) if \(p\) is \(\pm1\) modulo \(m\) and \(\varepsilon_p=1\) otherwise.
- \(\mathfrak r=\mathfrak r(p)\) is the least natural number with \(m\le p^{\mathfrak r}\) (for \(p>1\)), the base-\(p\) logarithm of \(m\) rounded up.
- The **transfer exponent** is \(\nu_p=\mathfrak r\,f\,(n_m+\mathfrak r)\).
- The **collision exponent** is \(j_p=\lceil 2mfa/p\rceil\).
- \(o_0(p)\) is the [[?c:Order of a group element|order]] in \((\mathbb{Z}/q_0)^\times\) of the reduction modulo \(q_0\) of the [[?lean:New.Data.placeOfInt|place named by \(-p\)]]; for \(p\) prime to \(q_1\) it is the order of \(-p\) in \((\mathbb{Z}/q_0)^\times\).
- \(p\) is **exceptional** if \(\chi_K(p)=-1\), \(p\) is not \(\pm1\) modulo \(m\), and \(o_0(p)\) is odd and at most \(\mathfrak r(p)\).

## Remarks

For an exceptional prime and \(e=o_0(p)\), the place named by \(-p^{e}\) is congruent to \(1\) modulo \(q_0\), that is, an [[?lean:New.Data.aPlaces|a-place]], and \(e\) is odd with \(p^{e-1}<m\). These are the primes at which two a-places can be partners of each other for a small exponent; see [[proofs/grh/upper-divisibility/collisions|collisions]].

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Size/ShortColumns.lean`.
