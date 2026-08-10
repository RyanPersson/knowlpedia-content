+++
id = "lie-groups/compact-exceptional-lie-group-f4"
title = "Compact exceptional Lie group F4"
kind = "knowl"
summary = "The compact connected simple 52-dimensional Lie group of rank 4 that is the automorphism group of the real Albert algebra."
aliases = ["compact-exceptional-lie-group-f4", "compact F4", "compact Lie group F4", "Aut(H3(O))"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

The **compact exceptional Lie group \(F_4\)** is the compact connected simple [[lie-groups/compact-lie-group|Lie group]] of rank \(4\) and real dimension \(52\) whose [[lie-groups/root-system|root system]] has Dynkin type \(F_4\). It is both [[lie-groups/simply-connected-lie-group|simply connected]] and centerless. Its real [[lie-groups/lie-algebra|Lie algebra]] is the [[lie-groups/compact-real-form|compact real form]] of [[lie-groups/exceptional-lie-algebra-f4|\(\mathfrak f_4\)]].

Its distinguished \(26\)-dimensional real representation is the action on the trace-zero part of the exceptional [[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan algebra]].

## Automorphisms of the Albert algebra

Let
\[
H_3(\mathbb O)=\{x\in M_3(\mathbb O):x=x^*\}
\]
with Jordan product \(x\circ y=(xy+yx)/2\). Although octonionic matrix multiplication is not associative, this symmetrized product makes \(H_3(\mathbb O)\) a \(27\)-dimensional real [[nonassociative-algebra/jordan-algebra|Jordan algebra]]. There is a natural isomorphism
\[
F_4\cong\operatorname{Aut}(H_3(\mathbb O)).
\]
The group fixes the identity matrix, so its \(27\)-dimensional action decomposes as the trivial line plus the irreducible \(26\)-dimensional trace-zero module.

This realization specifies the **compact** group because \(\mathbb O\) is the real division-octonion algebra and \(H_3(\mathbb O)\) is Euclidean. Using split octonions gives a noncompact real form instead. Complexifying the Lie algebra gives \(\mathfrak f_4\), not a compact group.

## Stabilizers and the Standard Model gauge group

In the exceptional-Jordan-algebra construction, \(F_4\) acts on [[nonassociative-algebra/jordan-subalgebra|Jordan subalgebras]] of \(H_3(\mathbb O)\). For nested subalgebras
\[
X\cong H_2(\mathbb C)\subset B\cong H_3(\mathbb C),
\]
one obtains
\[
\operatorname{Stab}_{F_4}(X)\cap\operatorname{Stab}_{F_4}(B)^0
\cong S(U(2)\times U(3)).
\]
The identity-component superscript is essential: the full stabilizer of \(B\) has an additional disconnected component induced by complex conjugation.

## References

1. John Frank Adams, *Lectures on Exceptional Lie Groups*, University of Chicago Press, 1996, Chapters 5--6. [Publisher record](https://press.uchicago.edu/ucp/books/book/chicago/L/bo3683975.html).
2. Kevin McCrimmon, *A Taste of Jordan Algebras*, Springer, 2004, Chapter 6. [Publisher record](https://doi.org/10.1007/b97489).
3. John C. Baez, "The Octonions," *Bulletin of the American Mathematical Society* 39 (2002), 145--205. [DOI](https://doi.org/10.1090/S0273-0979-01-00934-X).
4. John C. Baez and Paul Schwahn, *The Standard Model Gauge Group from the Exceptional Jordan Algebra*, 2026. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
