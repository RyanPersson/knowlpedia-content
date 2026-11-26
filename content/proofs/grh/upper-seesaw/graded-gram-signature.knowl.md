+++
id = "proofs/grh/upper-seesaw/graded-gram-signature"
title = "Signature of the graded Gram matrix"
kind = "lemma"
summary = "For N > 0 the graded Gram form with a string of length s is congruent over the complex numbers to a diagonal of signs with exactly floor((s+1)/2) minus signs."
aliases = ["string frame", "string signs"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.stringSign", "New.Seesaw.stringFrame", "New.Seesaw.gram_stringFrame_eq_signMatrix", "New.Seesaw.conjTranspose_stringFrame_one_mul_self", "New.Seesaw.exists_conjTranspose_mul_gradedGram_mul_eq_signMatrix"]
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleCombinations.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\iota\) be a finite set indexing a basis \((x_i)_{i\in X}\), \(z_0,\dots,z_{s-1}\)
through a bijection, let \(N\ge1\) be an integer, and let \(J\) be the
[[?lean:New.gradedGram|graded Gram matrix]] with parameter \(N\), viewed as a complex matrix:
\(\langle x_i,x_j\rangle=\delta_{ij}\), \(\langle z_b,z_{b'}\rangle=1\) if \(b+b'=s-1\) and
\(b\ne b'\), \(\langle z_c,z_c\rangle=-N\) if \(2c=s-1\), all other pairings \(0\). Let
\(\varepsilon\colon\iota\to\{\pm1\}\) be signs of which exactly \(\lfloor(s+1)/2\rfloor\) are
\(-1\). Then there is a complex matrix \(y\) with
\[
y^{*}J\,y=\operatorname{diag}(\varepsilon),
\]
and \(y\) can be taken [[?c:Unitary matrix|unitary]] if \(N=1\).

## Proof

Define the **string signs** \(\sigma_b=-1\) for \(b<\lfloor(s+1)/2\rfloor\) and \(\sigma_b=+1\)
otherwise, and the **string frame**
\[
f_b=\frac{\sigma_b z_b+z_{s-1-b}}{\sqrt2}\quad(b\ne s-1-b),\qquad f_c=\frac{z_c}{\sqrt N}\quad(2c=s-1).
\]
For \(b\neq s-1-b\) exactly one of \(b,\,s-1-b\) is below \(\lfloor(s+1)/2\rfloor\), so
\(\sigma_b\sigma_{s-1-b}=-1\); the middle index has \(\sigma_c=-1\). Hence:

* \(\langle f_b,f_b\rangle=\tfrac12(2\sigma_b)=\sigma_b\) for \(b\ne s-1-b\);
* \(\langle f_b,f_{s-1-b}\rangle=\tfrac12(\sigma_b\sigma_{s-1-b}+1)=0\);
* \(\langle f_c,f_c\rangle=-N/N=-1=\sigma_c\);
* \(f_b\perp f_{b'}\) when \(b'\notin\{b,s-1-b\}\), since the planes \(\langle z_b,z_{s-1-b}\rangle\)
  are mutually orthogonal.

So the Gram matrix of \((x_i)\cup(f_b)\) is diagonal with entries \(+1\) on \(X\) and \(\sigma_b\)
on the string; it has \(\lfloor(s+1)/2\rfloor\) entries \(-1\). Since \(\varepsilon\) has the same
number of minus signs, a bijection of the index sets carries one sign vector to the other; \(y\) is
the matrix of the frame \((x_i),(f_b)\) with columns permuted accordingly.

If \(N=1\) the vectors \(f_b\) are orthonormal for the standard hermitian product on the span of
the \(z_b\) (they are \((\pm z_b+z_{s-1-b})/\sqrt2\) and \(z_c\)), so \(y\) is unitary.
\(\blacksquare\)

## References

1. Lean: `New.Seesaw.gram_stringFrame_eq_signMatrix`, `New.Seesaw.exists_conjTranspose_mul_gradedGram_mul_eq_signMatrix` in `src/New/UpperBound/Seesaw/AdmissibleCombinations.lean`.
