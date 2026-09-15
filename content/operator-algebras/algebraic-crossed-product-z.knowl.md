+++
id = "operator-algebras/algebraic-crossed-product-z"
title = "Algebraic crossed product by an automorphism"
kind = "construction"
summary = "Finite formal sums with multiplication twisted by powers of an automorphism."
aliases = []
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/involutive-algebra", "operator-algebras/star-automorphism"]
+++

For a unital \(*\)-algebra \(A\) and [[operator-algebras/star-automorphism|\(*\)-automorphism]] \(\alpha\), the **algebraic crossed product** \(A\rtimes_{\alpha,\mathrm{alg}}\mathbb Z\) consists of finite formal sums \(\sum_n a_nu^n\), with
\[
(au^m)(bu^n)=a\alpha^m(b)u^{m+n},\qquad
(au^m)^*=\alpha^{-m}(a^*)u^{-m}.
\]
Addition and scalar multiplication are coefficientwise. The formal unitary \(u\) obeys \(uau^*=\alpha(a)\).

## Noncommutativity

The commutator is \(ua-au=(\alpha(a)-a)u\). Thus a commutative function algebra and the abelian group \(\mathbb Z\) can produce a noncommutative algebra through a nontrivial action.

## Completions

The algebraic object has no specified complete operator norm. Its operator-algebra completions include [[operator-algebras/full-crossed-product|\(C^*\)-crossed products]] and, for normal actions, [[operator-algebras/von-neumann-crossed-product|von Neumann crossed products]]. The formulas are the discrete \(\mathbb Z\) case of the [[operator-algebras/crossed-product-convolution-star-algebra|crossed-product convolution algebra]].
