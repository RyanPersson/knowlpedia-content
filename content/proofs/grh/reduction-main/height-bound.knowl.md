+++
id = "proofs/grh/reduction-main/height-bound"
title = "Height bound for a family of complex numbers indexed by the finite places"
kind = "definition"
summary = "A family y with one complex number for each finite place of C has height at most c if a common multiplier H makes archimedean and l-adic bounds add up to at most c."
aliases = ["height at most c", "HeightLe"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.HeightLe"]
lean_files = ["src/New/Reduction/Lattices/Heights.lean"]
+++

Let \(y=(y_\iota)_\iota\) be a family of complex numbers indexed by all [[proofs/grh/reduction-main/prime-padic-iso|finite places \(\iota\mid\ell\) of \(\mathbb C\)]] (pairs of a prime \(\ell\) and an isomorphism \(\iota:\mathbb C\cong\overline{\mathbb Q}_\ell\)), and let \(c\in\mathbb R\). The family \(y\) **has height at most \(c\)**, written \(\operatorname{ht}(y)\le c\), if there exist

- a complex number \(H\ne0\) (the *multiplier*),
- a real number \(\alpha\), and
- real numbers \(h_\ell\ge 0\), one for each natural number \(\ell\),

such that

1. \(\lvert\sigma(H)\rvert\le e^{\alpha}\) for every [[algebra-fields-galois/field-automorphism|field automorphism]] \(\sigma\) of \(\mathbb C\);
2. \(\lvert H\,y_\iota\rvert_\iota\le\ell^{\,h_\ell}\) for every finite place \(\iota\mid\ell\);
3. \(\alpha+\sum_{\ell\in T}h_\ell\log\ell\le c\) for every finite set \(T\) of primes.

## Remarks

- The multiplier \(H\), and so the bound at infinity, does not depend on \(\iota\), while \(y_\iota\) may. This is what allows a different twist at each prime in [[proofs/grh/reduction-main/covolume-add-index-nonneg|the lower bound for a twisted lattice]].
- "\(\operatorname{ht}(y)\le c\)" is a relation; no number \(\operatorname{ht}(y)\) is defined. The bound \(c\) may be negative.
- Condition (1) forces \(H\) to be algebraic over \(\mathbb Q\) (a transcendental number has conjugates of arbitrarily large absolute value under \(\operatorname{Aut}(\mathbb C)\)); the proof of the [[proofs/grh/reduction-main/height-product-formula|product formula for heights]] uses the analogous fact at the prime \(2\).
- The relation is *not* a bound for the Weil height. Example: for the constant family \(y_\iota=2\) take \(H=\tfrac12\), \(\alpha=-\log2\), \(h_\ell=0\); then \(\operatorname{ht}(y)\le-\log2\), whereas the logarithmic Weil height of \(2\) is \(\log2\). For a rational constant \(z\ne0\) the least admissible \(c\) is \(-\log\lvert z\rvert\): it is attained with \(H=1/z\), and \(c\ge-\log\lvert z\rvert\) by part (2) of the [[proofs/grh/reduction-main/height-product-formula|product formula for heights]].

## References

1. Lean: `New.HeightLe` in `src/New/Reduction/Lattices/Heights.lean`.
2. Related work named in the Lean file head: É. Gaudron, *Pentes des fibrés vectoriels adéliques sur un corps global*, 2006; E. Bombieri, W. Gubler, *Heights in Diophantine Geometry*, Cambridge University Press, 2006, Chapter 1.
