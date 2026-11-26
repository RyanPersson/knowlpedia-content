+++
id = "proofs/grh/spanning-core/character-sum-bound-by-stabilisers"
title = "Character sums against a function of positive type"
kind = "lemma"
summary = "A twisted sum of a function of positive type over a finite group is bounded by the masses of two stabilisers."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.re_sum_addChar_dotProduct_mul_le", "New.orthonormal_addChar_div_sqrt", "New.inner_addChar_invTranspose_smul_single", "New.expect_addChar_dotProduct"]
lean_files = ["src/New/Spanning/SecondMoment/PositiveType.lean"]
proof_status = "full"
+++

**Lemma.** Let \(G\) be a [[algebra-groups/finite-group|finite group]] and \(\Theta\colon G\to\mathbb{R}\) a [[proofs/grh/spanning-core/function-of-positive-type|function of positive type]]. Let \(k\) be a [[?c:finite field|finite field]] with \(q\) elements, \(n\) a finite index set, \(\pi\colon G\to\mathrm{GL}_n(k)\) a [[algebra-groups/group-homomorphism|group homomorphism]], and \(\pi'(s)=(\pi(s)^{\mathsf T})^{-1}\) its inverse transpose. Let \(\psi\colon k\to\mathbb{C}^\times\) be a nontrivial [[?c:additive character of a finite field|additive character]] of \(k\), and write \(x\cdot z=\sum_{i\in n}x_iz_i\) for \(x,z\in k^n\). Let \(x,z\in k^n\) and \(Y\in\mathbb{R}\) satisfy
\[
\sum_{s\in G,\ \pi'(s)x=x}\Theta(s)\le Y,\qquad \sum_{s\in G,\ \pi(s)z=z}\Theta(s)\le Y .
\]
Then
\[
\operatorname{Re}\sum_{s\in G}\psi\bigl(x\cdot\pi(s)z\bigr)\,\Theta(s)\ \le\ q^{\lvert n\rvert/2}\,Y .
\]

## Proof

Put \(r=q^{\lvert n\rvert/2}\), and let \((u_a)_{a\in G}\) be a realisation of \(\Theta\) in an inner product space \(H\). Let \(L\) be the space of complex functions on \(k^n\) with \(\langle f,g\rangle=\sum_{\zeta}\overline{f(\zeta)}g(\zeta)\). For \(v\in k^n\) let \(e_v\in L\) be the indicator function of \(\{v\}\) and \(c_v(\zeta)=\psi(-v\cdot\zeta)/r\).

*Both families are orthonormal.* This is clear for \((e_v)\). For \((c_v)\): \(\langle c_v,c_{v'}\rangle=r^{-2}\sum_\zeta\psi\bigl((v-v')\cdot\zeta\bigr)\), and since \(k\) is a field and \(\psi\) is nontrivial, the sum of \(\psi(w\cdot\zeta)\) over \(\zeta\in k^n\) is \(q^{\lvert n\rvert}\) for \(w=0\) and \(0\) otherwise (orthogonality of characters).

*The mixed products.* For \(a,b\in G\),
\[
\langle c_{\pi'(a)x},e_{\pi(b)z}\rangle=\overline{\psi\bigl(-\pi'(a)x\cdot\pi(b)z\bigr)}/r=\psi\bigl(x\cdot\pi(a^{-1}b)z\bigr)/r ,
\]
because \((\pi(a)^{\mathsf T})^{-1}x\cdot w=x\cdot\pi(a)^{-1}w\) and \(\overline{\psi(-t)}=\psi(t)\).

In \(L\otimes H\) set \(X_1=\sum_a c_{\pi'(a)x}\otimes u_a\) and \(X_0=\sum_a e_{\pi(a)z}\otimes u_a\). By the sum rule of [[proofs/grh/spanning-core/function-of-positive-type|functions of positive type]], with \(w(s)=\psi(x\cdot\pi(s)z)\Theta(s)/r\),
\[
\langle X_1,X_0\rangle=\lvert G\rvert\sum_{s}w(s),
\]
and by the stabiliser rule there (for the actions of \(G\) on \(k^n\) through \(\pi'\) and through \(\pi\)) and the hypotheses,
\[
\lVert X_1\rVert^2=\lvert G\rvert\sum_{\pi'(s)x=x}\Theta(s)\le\lvert G\rvert Y,\qquad \lVert X_0\rVert^2=\lvert G\rvert\sum_{\pi(s)z=z}\Theta(s)\le\lvert G\rvert Y .
\]
By the [[linear-algebra/cauchy-schwarz-inequality|Cauchy–Schwarz inequality]] and \(2\alpha\beta\le\alpha^2+\beta^2\), \(2\operatorname{Re}\langle X_1,X_0\rangle\le\lVert X_1\rVert^2+\lVert X_0\rVert^2\le2\lvert G\rvert Y\). Hence
\[
\operatorname{Re}\sum_s\psi\bigl(x\cdot\pi(s)z\bigr)\Theta(s)=\frac{r}{\lvert G\rvert}\operatorname{Re}\langle X_1,X_0\rangle\le rY .\qquad\blacksquare
\]

## Remarks

The Lean statement assumes \(\psi\) primitive in Mathlib's sense; for a finite field this is the same as nontrivial.

## References

1. Lean: `New.re_sum_addChar_dotProduct_mul_le` in `src/New/Spanning/SecondMoment/PositiveType.lean`.

## References

1. Lean: `New.re_sum_addChar_dotProduct_mul_le`, `New.orthonormal_addChar_div_sqrt`, `New.inner_addChar_invTranspose_smul_single`, `New.expect_addChar_dotProduct` in `src/New/UpperBound/ElementaryDivisors/.lean`.
