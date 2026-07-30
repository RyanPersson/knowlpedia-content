+++
id = "formal-groups/formal-group-logarithm"
title = "Formal group logarithm"
kind = "theorem"
summary = "Over a Q-algebra, a commutative formal group law has a unique strict isomorphism to the additive law."
aliases = ["logarithm of a formal group law", "formal logarithm", "log_F"]
domains = ["formal-groups"]
section_mode = "progressive"
+++

Let \(R\) be a \(\mathbb Q\)-algebra and let \(F\) be a commutative
\(n\)-dimensional [[formal-groups/formal-group-law|formal group law]] over
\(R\). There is a unique tuple
\[
\log_F(X)=X+\text{terms of total degree at least \(2\)}
\]
such that
\[
\log_F(F(X,Y))=\log_F(X)+\log_F(Y).
\]
The **formal group logarithm** is therefore a strict
[[formal-groups/formal-group-law-morphism|isomorphism]] from \(F\) to the
\(n\)-dimensional additive formal group law.

## Construction from invariant differentials

In one dimension, set
\[
\omega_F(X)
=
\left(\frac{\partial F}{\partial Y}(X,0)\right)^{-1}dX.
\]
This is the invariant differential of \(F\), and its coefficientwise formal
integral normalized by \(\log_F(0)=0\) is the logarithm:
\[
\log_F(X)=\int_0^X\omega_F.
\]
Division by positive integers explains the \(\mathbb Q\)-algebra hypothesis.
In several commuting dimensions, the matrix of invariant one-forms is
formally closed and integrates to the logarithm coordinatewise.

## Inverse exponential

The linear term of \(\log_F\) is the identity, so the
[[algebra-rings/formal-inverse-function-theorem|formal inverse function
theorem]] gives an inverse
\[
\exp_F=\log_F^{-1}.
\]
It satisfies
\(\exp_F(U+V)=F(\exp_F(U),\exp_F(V))\).

## Scope

The theorem requires commutativity. A noncommutative formal group in
characteristic zero is instead put into
[[lie-groups/baker-campbell-hausdorff-formula|BCH coordinates]], where its
tangent Lie bracket remains visible. Over rings not containing
\(\mathbb Q\), logarithm coefficients may have forbidden denominators, and
height and other integral phenomena survive.

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Chapters 1–2, logarithms in characteristic zero.
2. Serge Lang, *Algebra*, revised third edition, Springer, 2002. Relevant: formal power series and commutative formal groups over characteristic-zero rings.
