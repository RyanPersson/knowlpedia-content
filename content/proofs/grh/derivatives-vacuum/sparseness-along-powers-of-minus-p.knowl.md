+++
id = "proofs/grh/derivatives-vacuum/sparseness-along-powers-of-minus-p"
title = "Sparseness of the b-places along the powers of -p"
kind = "lemma"
summary = "For a prime p at most k that does not split in K and 0 < i < j < l0, the places sigma, (-p)^i sigma, (-p)^j sigma are not all b-places; and for p = d a place and its partner have different classes modulo q0."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.notMem_bPlaces_of_two_partners", "New.Data.ne_d_of_placeClass_eq"]
lean_files = ["src/New/Derivatives/Sharpness/NearPairs.lean"]
proof_status = "full"
+++

Let \(D\) be [[?lean:New.Data|admissible data]] over parameters \(P\). The infinite places of \(E\) form the group \(\Phi=(\mathbb{Z}/q_1)^\times\); for an integer \(\nu\) write \([\nu]\in\Phi\) for [[?lean:New.Data.placeOfInt|the place named by \(\nu\)]]: the class of \(\nu\) if \(\nu\) is prime to \(q_1\), and the identity place otherwise. Let \(\Phi_b\subset\Phi\) be the [[?lean:New.Data.bPlaces|\(b\)-places]], \(k\) the rank parameter and \(l_0\) [[?lean:New.l₀|the least power of \(3\) above \(27s\)]].

**Lemma.**

1. Let \(p\le k\) be a prime with \(\chi_K(p)\ne1\), \(\sigma\in\Phi\), and \(0<i<j<l_0\). Then \(\sigma\), \([-p]^i\sigma\), \([-p]^j\sigma\) are not all in \(\Phi_b\).
2. If \([-p^e]\sigma\) and \(\sigma\) have the same class modulo \(q_0\), then \(p\ne d\).

## Proof

1. Primes dividing \(q_1\) split in \(K\), so \(p\nmid q_1\) and \(-p\) is prime to \(q_0\). The ratios \([-p]^n\sigma/\sigma\) have class \((-1)^np^n\) modulo the part of \(q_1\) prime to \(p\). The data require the \(b\)-places to be [[?lean:New.Parameters.IsSparse|sparse]]: for primes \(\ell\le kt\) and \(0<i<j<l_0\), no \(\sigma,\pm\ell^i\sigma,\pm\ell^j\sigma\) all lie in \(\Phi_b\), modulo the part of \(q_1\) prime to \(\ell\) ([[?lean:New.Data.sparse|the sparseness condition of the data]]). Apply it with \(\ell=p\le k\le kt\).

2. For \(p=d\) the hypothesis says \(-d^e\equiv1\bmod q_0\), which is excluded by the congruence condition on \(d\) (Lean `New.Parameters.d_pow_ne_neg_one`).

## References

1. Lean: `New.Data.notMem_bPlaces_of_two_partners`, `New.Data.ne_d_of_placeClass_eq` in `src/New/Derivatives/Sharpness/NearPairs.lean`.
