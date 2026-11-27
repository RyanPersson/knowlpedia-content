+++
id = "proofs/grh/upper-seesaw/admissible-combination"
title = "Admissible combination"
kind = "definition"
summary = "A finite linear combination of a family of vectors whose coefficients have a bounded denominator away from n and, on demand, bounded size at all conjugates."
aliases = ["admissible coefficients", "admissible combination of translates"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.IsAdmissibleCoeffs", "New.Seesaw.IsAdmissibleCombination"]
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleCombinations.lean"]
+++

Let \(Z\) be a complex vector space, \((v_x)_{x\in\alpha}\) a family of vectors of \(Z\) indexed by
a set \(\alpha\), and \(A\subseteq\alpha\) a subset. Let \(n,d\) be natural numbers, \(p\) a
proposition (a condition that may or may not hold) and \(B\) a real number.

A finitely supported function \(r\colon\alpha\to\mathbb{C}\) is a family of **admissible
coefficients** for \((A,n,d,p,B)\) if

1. (**support**) \(r(x)\neq 0\) implies \(x\in A\);
2. (**denominator**) for every \(x\), the number \(d\cdot r(x)\) is
   [[proofs/grh/upper-seesaw/integral-away|integral away from \(n\)]];
3. (**size**) if \(p\) holds, then for every
   [[algebra-fields-galois/field-automorphism|field automorphism]] \(\sigma\) of \(\mathbb{C}\),
   \(\sum_{x}\lvert\sigma(r(x))\rvert\le B\).

A vector \(z\in Z\) is an **admissible combination** of the \(v_x\), \(x\in A\), with denominator
\(d\) away from \(n\) and size \(B\) under \(p\), if
\[
z=\sum_{x} r(x)\,v_x
\]
for some family \(r\) of admissible coefficients for \((A,n,d,p,B)\).

## Remarks

The proposition \(p\) switches the size condition on and off. In the seesaw application, for a tame character with chosen modulus \(Q\): \(n=q=\prod_{w\in Q}\mathrm{N}w\); \(p\) is "\(Q=\emptyset\)"; and the denominator is \(d=\mathcal{C}^{2m}\), a power of the norm of \(\pi_M\), for the [[proofs/grh/upper-seesaw/seesaw-datum|seesaw datum]] before rescaling, and \(d=1\) for the coefficients of the chain datum after the rescaling in the proof of the [[proofs/grh/upper-seesaw/seesaw-identity|seesaw identity]]. So the coefficients are integral away from \(q\) always, and bounded in size only when the modulus is empty.

The coefficients are not required to be unique, and the \(v_x\) need not be linearly independent.

## References

1. Lean: `New.Seesaw.IsAdmissibleCoeffs`, `New.Seesaw.IsAdmissibleCombination` in `src/New/UpperBound/Seesaw/AdmissibleCombinations.lean`.
