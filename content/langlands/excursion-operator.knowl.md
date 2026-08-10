+++
id = "langlands/excursion-operator"
title = "Excursion operator"
kind = "knowl"
summary = "An operator on cuspidal automorphic forms built by creating shtuka legs, moving them by Galois elements, and annihilating them."
aliases = ["excursion operators", "Lafforgue excursion operator"]
domains = ["langlands", "number-theory", "representation-theory"]
section_mode = "progressive"
+++

Let \(F\) be a global function field and \(G\) a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]].
An **excursion operator** is indexed by

\[
\left(I,f,(\gamma_i)_{i\in I}\right),
\]

where \(I\) is a finite set,
\(f\in\mathcal O(\widehat G\backslash\widehat G^I/\widehat G)\) is invariant
under diagonal left and [[lie-groups/right-translation|right translation]], and
\(\gamma_i\in\operatorname{Gal}(\overline F/F)\). It defines an endomorphism

\[
S_{I,f,(\gamma_i)}
\]

of the finite-level space of cuspidal [[langlands/automorphic-form|automorphic forms]].

## Creation, excursion, annihilation

Choose a finite-dimensional representation \(W\) of \(\widehat G^I\), a
diagonal-\(\widehat G\)-invariant vector \(x\in W\), and an invariant
covector \(\xi\in W^*\) such that

\[
f((g_i))=\langle\xi,(g_i)x\rangle.
\]

The operator is the composite:

1. **create** \(I\) coincident shtuka legs using \(x:\mathbf 1\to W\);
2. act on the legs by the independent Galois elements \((\gamma_i)\), using
   partial Frobenius and Drinfeld's lemma;
3. **annihilate** the legs using \(\xi:W\to\mathbf 1\).

Coalescence of legs supplies the comparison maps. The resulting operator
depends only on \(I,f,(\gamma_i)\), not on the chosen realization
\((W,x,\xi)\).

## Why many legs are necessary

Characters of single dual-group elements do not distinguish all
semisimple homomorphisms into a general reductive group. Simultaneous
invariant functions on \(\widehat G^I\) for all finite \(I\) retain the
pseudocharacter data needed to reconstruct a semisimple
\(\widehat G\)-valued Galois parameter.

## Relations

Excursion operators are continuous in the Galois variables, compatible
with maps of finite sets, multiplicative in invariant functions, and
commute with one another and with unramified Hecke operators. They generate
the [[langlands/excursion-algebra|excursion algebra]].

## References

1. Vincent Lafforgue, “Chtoucas pour les groupes réductifs et
   paramétrisation de Langlands globale,” §§0.1 and 5–10.
   [arXiv](https://arxiv.org/abs/1209.5352).
2. Vincent Lafforgue, “Shtukas for reductive groups and Langlands
   correspondence for function fields,” 2018.
   [arXiv](https://arxiv.org/abs/1803.03791).
