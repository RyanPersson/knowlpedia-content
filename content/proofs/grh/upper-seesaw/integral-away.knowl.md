+++
id = "proofs/grh/upper-seesaw/integral-away"
title = "Complex numbers integral away from n"
kind = "definition"
summary = "The subring of complex numbers whose image under every homomorphism to the l-adic complex numbers is integral, for all primes l not dividing n."
aliases = ["integral away from n", "integralAway"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.integralAway", "New.Seesaw.div_mem_integralAway"]
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleCombinations.lean"]
+++

Let \(n\) be a natural number. A complex number \(z\) is **integral away from \(n\)** if for every
prime \(l\) coprime to \(n\) and every [[?c:Ring homomorphism|ring homomorphism]]
\(\iota\colon \mathbb{C}\to\mathbb{C}_l\) into the
[[?c:Field of p-adic complex numbers|field of \(l\)-adic complex numbers]] one has
\(\lVert \iota(z)\rVert_l \le 1\). The set of these numbers is denoted
\[
\mathcal{O}^{(n)} \;=\; \{\, z\in\mathbb{C} \;:\; \lVert\iota(z)\rVert_l\le 1 \text{ for all primes } l\nmid n \text{ and all } \iota\colon\mathbb{C}\to\mathbb{C}_l \,\}.
\]

## Properties

**\(\mathcal{O}^{(n)}\) is a [[algebra-rings/subring|subring]] of \(\mathbb{C}\).** It contains
\(0\) and \(1\) and is closed under negation. It is closed under products because
\(\lVert\iota(xy)\rVert=\lVert\iota x\rVert\,\lVert\iota y\rVert\le 1\), and under sums because the
norm of \(\mathbb{C}_l\) is [[?c:Non-archimedean absolute value|ultrametric]]:
\(\lVert\iota(x+y)\rVert\le\max(\lVert\iota x\rVert,\lVert\iota y\rVert)\le 1\).

**Roots of unity.** Every [[?c:Root of unity|root of unity]] lies in \(\mathcal{O}^{(n)}\): its image under \(\iota\) is
a root of unity of \(\mathbb{C}_l\), which has norm \(1\).

**Quotients of integers.** Let \(c,d,q,k\) be natural numbers with \(c \mid d\,q^{k}\). Then
\(d/c\in\mathcal{O}^{(q)}\) (with the convention \(d/0=0\)). Indeed, write \(d q^{k}=c\,m\) and let
\(l\nmid q\) be a prime. Since \(q\) is an \(l\)-adic unit, \(\lVert d\rVert_l=\lVert c\rVert_l\lVert m\rVert_l\).
If \(c\ne0\) this gives \(\lVert d/c\rVert_l=\lVert m\rVert_l\le1\); if \(c=0\) the quotient is \(0\).
A ring homomorphism \(\mathbb{C}\to\mathbb{C}_l\) fixes the rational number \(d/c\).

## Remarks

The condition quantifies over all ring homomorphisms \(\mathbb{C}\to\mathbb{C}_l\), not over one
chosen isomorphism; so membership is invariant under the
[[algebra-fields-galois/field-automorphism|field automorphisms]] of \(\mathbb{C}\).

## References

1. Lean: `New.Seesaw.integralAway`, `New.Seesaw.div_mem_integralAway` in `src/New/UpperBound/Seesaw/AdmissibleCombinations.lean`.
