+++
id = "proofs/grh/upper-divisibility/collision-sum-bound"
title = "The collision sum is within the loss at non-exceptional primes"
kind = "lemma"
summary = "Collisions have odd exponents divisible by the order of -p modulo q_0; at a small non-split prime that is not exceptional, m times the collision sum is at most the loss."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.mul_collisionSum_le_loss", "New.Data.collisionSum_le", "New.Data.IsCollision.ne_and_odd_and_dvd", "New.Data.placeOfInt_mul_mem_aPlaces_iff", "New.Data.le_loss"]
lean_files = ["src/New/UpperBound/Divisibility/JetExponent.lean"]
proof_status = "full"
+++

Let \(D\) be [[?lean:New.Data|admissible data]] and \(p\) a prime. Notation as in [[proofs/grh/upper-divisibility/collisions|collisions]] and [[proofs/grh/upper-divisibility/classes-of-primes|classes of primes]].

**Lemma.**

1. If \((\tau,e)\) is a collision at \(p\) outside a set \(S\), then \(p\ne d\), \(e\) is odd, and \(o_0(p)\mid e\).
2. If every collision outside \(S\) has \(e\ge o\), then \(\operatorname{coll}_p(S)\le 2fa/p^{o}\).
3. If \(p\) is small non-split (\(p<x_1\), \(\chi_K(p)\ne1\)) and not exceptional, then \(m\cdot\operatorname{coll}_p(\emptyset)\le\operatorname{loss}(p)\).

Moreover \(\operatorname{loss}(p)\ge f(\log b)^2a/p\) for every \(p\).

## Proof

(1) For odd \(e\), \(u(-p^{e})=u(-p)^{e}\), and for an a-place \(\tau\) (class \(1\) modulo \(q_0\)) the place \(u(-p)^{e}\tau\) is an a-place exactly when the class of \(u(-p)\) modulo \(q_0\) has \(e\)-th power \(1\), that is when \(o_0(p)\mid e\). If \(p=d\), a collision would give two a-places \(\tau\) and \(u(-d^{e})\tau\), hence \(-d^{e}\equiv1\pmod{q_0}\); this is excluded, because \(d\equiv q_0/2-1\pmod{q_0}\) makes no power of \(d\) congruent to \(-1\) modulo \(q_0\) ([[?lean:New.Data.ne_d_of_placeClass_eq|`ne_d_of_placeClass_eq`]], proved in another file from `d_pow_ne_neg_one`). So \(p\ne d\). Then \(e\in I_p\) means \(\chi_K(p)=-1\) and \(e\) odd, and the first sentence applies.

(2) At each of the \(f\) places the collisions have exponents \(e=o+i\), \(i\ge0\), and since \(p\ge2\) their terms are at most \(a/(p^{o}2^{i})\), with sum at most \(2a/p^{o}\).

(3) If \(p\equiv\pm1\bmod m\): exponents in \(I_p\) are at least \(1\), so by (2) \(m\operatorname{coll}_p(\emptyset)\le 2mfa/p\le m f(\log b)^2a/p=\operatorname{loss}(p)\), using \((\log b)^2\ge2\). Otherwise: by (1) a collision has \(p\ne d\), so \(\chi_K(p)=-1\) (as \(\chi_K(p)\ne1\)), and \(e\) is odd and a multiple of \(o_0(p)\); hence \(o_0(p)\) is odd and \(o_0(p)\le e\). As \(p\) is not exceptional and not \(\pm1\) modulo \(m\), an odd \(o_0(p)\) exceeds \(\mathfrak r=\mathfrak r(p)\). So every collision has \(e\ge\mathfrak r+1\), and by (2) and \(m\le p^{\mathfrak r}\),
\[
m\operatorname{coll}_p(\emptyset)\le\frac{2mfa}{p^{\mathfrak r+1}}\le\frac{2fa}{p}\le f(\log b)^2\frac ap=\operatorname{loss}(p).
\]
The last assertion holds because the extra factor in the loss is \(m\ge1\) or \(1\). \(\blacksquare\)

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Divisibility/JetExponent.lean`.
