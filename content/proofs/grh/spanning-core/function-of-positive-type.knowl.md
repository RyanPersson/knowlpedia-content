+++
id = "proofs/grh/spanning-core/function-of-positive-type"
title = "Function of positive type on a finite group"
kind = "definition"
summary = "A real function on a finite group whose values at a^{-1}b are inner products of vectors u_a, u_b."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.inner_sum_sum_eq_card_mul", "New.norm_sq_sum_tmul_eq_card_mul_sum"]
lean_files = ["src/New/Spanning/SecondMoment/PositiveType.lean"]
+++

Let \(G\) be a [[algebra-groups/finite-group|finite group]]. A function \(\Theta\colon G\to\mathbb{R}\) is **of positive type** if there are a complex [[linear-algebra/inner-product-space|inner product space]] \(H\) and vectors \(u_a\in H\) \((a\in G)\) with
\[
\langle u_a,u_b\rangle=\Theta(a^{-1}b)\qquad\text{for all }a,b\in G .
\]
The family \((u_a)\) is called a **realisation** of \(\Theta\). (Inner products are conjugate-linear in the first variable and linear in the second.)

## Properties

Let \(\Theta\) be of positive type with realisation \((u_a)_{a\in G}\) in \(H\).

1. **(Sum rule.)** If \((u_a)\), \((v_a)\) are two families in an inner product space and \(f\colon G\to\mathbb{C}\) satisfies \(\langle u_a,v_b\rangle=f(a^{-1}b)\) for all \(a,b\), then
\[
\Bigl\langle \sum_{a\in G}u_a,\ \sum_{b\in G}v_b\Bigr\rangle=\lvert G\rvert\sum_{s\in G}f(s).
\]
2. **(Mass of a stabiliser.)** Let \(G\) act on a finite set \(X\), let \(x\in X\), and let \((c_\xi)_{\xi\in X}\) be an orthonormal family in a complex inner product space \(L\). Then, in the [[algebra-modules/tensor-product|tensor product]] \(L\otimes H\) with the inner product \(\langle c\otimes u,c'\otimes u'\rangle=\langle c,c'\rangle\langle u,u'\rangle\),
\[
\Bigl\lVert\sum_{a\in G}c_{a x}\otimes u_a\Bigr\rVert^2=\lvert G\rvert\sum_{s\in G,\ s x=x}\Theta(s).
\]
The sum on the right is the **\(\Theta\)-mass of the [[algebra-groups/stabilizer|stabiliser]]** of \(x\).

## Proof

(1) For fixed \(a\), the map \(b\mapsto a^{-1}b\) is a bijection of \(G\), so \(\sum_b\langle u_a,v_b\rangle=\sum_s f(s)\); now sum over \(a\).

(2) Put \(f(s)=\Theta(s)\) if \(sx=x\) and \(f(s)=0\) otherwise. By orthonormality, \(\langle c_{ax}\otimes u_a,c_{bx}\otimes u_b\rangle\) equals \(\Theta(a^{-1}b)\) if \(ax=bx\), that is if \(a^{-1}b\) fixes \(x\), and \(0\) otherwise; so it equals \(f(a^{-1}b)\). Apply (1) with \(u_a\), \(v_a\) both replaced by \(c_{ax}\otimes u_a\).

## Remarks

In the Lean source the notion is not a named definition: it appears as the hypothesis \(\langle u_a,u_b\rangle=\Theta(a^{-1}b)\) of the lemmas, and (2) is stated for the action of \(G\) on \(k^n\) through a homomorphism \(G\to\mathrm{GL}_n(k)\).

## References

1. Lean: `New.inner_sum_sum_eq_card_mul`, `New.norm_sq_sum_tmul_eq_card_mul_sum` in `src/New/Spanning/SecondMoment/PositiveType.lean`.

## References

1. Lean: `New.inner_sum_sum_eq_card_mul`, `New.norm_sq_sum_tmul_eq_card_mul_sum` in `src/New/UpperBound/ElementaryDivisors/.lean`.
