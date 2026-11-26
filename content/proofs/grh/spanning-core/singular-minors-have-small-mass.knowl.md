+++
id = "proofs/grh/spanning-core/singular-minors-have-small-mass"
title = "Singular minors have small mass"
kind = "theorem"
summary = "For a function of positive type on a finite group acting on a vector space over a finite field, the set where a matrix coefficient minor is singular has small mass if stabilisers of nonzero vectors do."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.card_mul_sum_det_eq_zero_le", "New.card_le_card_filter_vecMul_eq_zero"]
lean_files = ["src/New/Spanning/SecondMoment/PositiveType.lean"]
proof_status = "full"
+++

**Theorem (singular minors).** Let \(G\) be a [[algebra-groups/finite-group|finite group]] and \(\Theta\colon G\to\mathbb{R}\) a [[proofs/grh/spanning-core/function-of-positive-type|function of positive type]] with \(\Theta(s)\ge0\) for all \(s\). Let \(k\) be a [[?c:finite field|finite field]] with \(q\) elements, \(n\) and \(m\) finite index sets, \(\pi\colon G\to\mathrm{GL}_n(k)\) a [[algebra-groups/group-homomorphism|homomorphism]] and \(\pi'(s)=(\pi(s)^{\mathsf T})^{-1}\). Let \(A_0,A_1\) be \(n\times m\) [[linear-algebra/matrix|matrices]] over \(k\) and \(Y\ge0\) a real number such that for every nonzero \(v\in k^m\)
\[
\sum_{s\in G,\ \pi(s)A_0v=A_0v}\Theta(s)\le Y\qquad\text{and}\qquad\sum_{s\in G,\ \pi'(s)A_1v=A_1v}\Theta(s)\le Y .
\]
Then
\[
q\cdot\sum_{s\in G,\ \det(A_1^{\mathsf T}\pi(s)A_0)=0}\Theta(s)\ \le\ 2\sum_{s\in G}\Theta(s)+q^{\lvert m\rvert}\,q^{\lvert n\rvert/2}\,Y .
\]

## Proof

Write \(Z(s)=A_1^{\mathsf T}\pi(s)A_0\), an \(m\times m\) matrix, \(\Theta(G)=\sum_s\Theta(s)\ge0\) and \(r=q^{\lvert n\rvert/2}\). Fix a nontrivial additive character \(\psi\) of \(k\) (one exists).

*Step 1: the left kernel of a singular matrix has at least \(q\) elements.* If \(\det Z=0\) there is \(y\neq0\) with \(y^{\mathsf T}Z=0\), and the \(q\) multiples \(ty\), \(t\in k\), are distinct and lie in the left kernel. Since \(\Theta\ge0\),
\[
q\sum_{\det Z(s)=0}\Theta(s)\le\sum_{s}\#\{y\in k^m: y^{\mathsf T}Z(s)=0\}\,\Theta(s)=\sum_{y\in k^m}\ \sum_{s:\ y^{\mathsf T}Z(s)=0}\Theta(s).
\]

*Step 2: counting with the character.* For \(y,v\in k^m\) put \(S(y,v)=\sum_s\psi\bigl(y^{\mathsf T}Z(s)v\bigr)\Theta(s)\). By orthogonality of characters the mean over \(v\in k^m\) of \(\psi(w\cdot v)\) is \(1\) if \(w=0\) and \(0\) otherwise; with \(w=y^{\mathsf T}Z(s)\),
\[
\frac1{q^{\lvert m\rvert}}\sum_{v\in k^m}\operatorname{Re}S(y,v)=\sum_{s:\ y^{\mathsf T}Z(s)=0}\Theta(s).
\]

*Step 3: bounds for \(S(y,v)\).* If \(y=0\) or \(v=0\) the character is \(1\) and \(\operatorname{Re}S(y,v)=\Theta(G)\). If \(y\neq0\) and \(v\neq0\), then \(y^{\mathsf T}Z(s)v=(A_1y)\cdot\pi(s)(A_0v)\), and the [[proofs/grh/spanning-core/character-sum-bound-by-stabilisers|character sum bound]] with \(x=A_1y\), \(z=A_0v\) and the two hypotheses gives \(\operatorname{Re}S(y,v)\le rY\). As \(\Theta(G)\ge0\) and \(rY\ge0\), in all cases
\[
\operatorname{Re}S(y,v)\le[y=0]\,\Theta(G)+[v=0]\,\Theta(G)+rY .
\]

*Step 4.* Summing over \(y\) the mean over \(v\): the first term contributes \(\Theta(G)\) (one \(y\)), the second \(q^{\lvert m\rvert}\cdot\Theta(G)/q^{\lvert m\rvert}=\Theta(G)\), the third \(q^{\lvert m\rvert}rY\). With Steps 1 and 2 this is the claim. \(\blacksquare\)

## Remarks

This is used in [[?lean:New.Filling.HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sq_le|the bound for the second moment]] (file `New/Spanning/Unfolding/MomentBounds`), with \(\Theta(s)=\lVert P^*sP\rVert^2\), which is of positive type by the [[proofs/grh/spanning-core/cauchy-schwarz-for-translates|translate identity]].

## References

1. Lean: `New.card_mul_sum_det_eq_zero_le` in `src/New/Spanning/SecondMoment/PositiveType.lean`.

## References

1. Lean: `New.card_mul_sum_det_eq_zero_le`, `New.card_le_card_filter_vecMul_eq_zero` in `src/New/UpperBound/ElementaryDivisors/.lean`.
