+++
id = "langlands/drinfeld-lemma"
title = "Drinfeld's lemma"
kind = "theorem"
summary = "Partial Frobenius structures on a product over a finite field produce an action of a product of Weil or fundamental groups."
aliases = ["Drinfeld lemma", "Drinfeld's lemma on partial Frobenius", "Drinfeld lemma for products"]
domains = ["langlands", "algebraic-geometry-foundations", "algebra-fields-galois"]
section_mode = "progressive"
+++

Let \(X\) be a connected [[algebraic-geometry-foundations/scheme|scheme]] over
a [[algebra-fields-galois/finite-field|finite field]] \(\mathbb F_q\), let \(I\)
be a finite set, and consider \(X^I\).  **Drinfeld's lemma** says, in one of
its sheaf-theoretic forms, that a finite étale or
[[algebraic-geometry-foundations/lisse-ell-adic-sheaf|lisse sheaf]] on \(X^I\)
equipped with compatible isomorphisms for the
[[langlands/partial-frobenius-on-shtukas|partial Frobenius morphisms]] carries
the monodromy action expected from a product of copies of the fundamental or
Weil group of \(X\), one copy for each element of \(I\).

In particular, the commuting partial Frobenius operators recover independent
Frobenius elements in the different legs; using only the diagonal Frobenius
would see just one copy.

## Hypotheses and versions

Precise statements differ with the coefficient category.  The original
finite-étale form is a statement about fundamental groups.  The lisse
\(\ell\)-adic form used for shtukas imposes a finiteness condition on geometric
monodromy, or works through an appropriate Weil-group formulation.  Modern
versions for stacks and diamonds require corresponding smallness and
continuity hypotheses.

## Role in excursion operators

The cohomology of a multiple-leg [[langlands/g-shtuka|\(G\)-shtuka]] has
partial Frobenius actions.
Drinfeld's lemma upgrades them to an action of a product of global Galois
groups. Together with [[langlands/coalescence-of-shtuka-legs|coalescence of
legs]], this makes it possible to insert a
tuple \((\gamma_i)_{i\in I}\) into an
[[langlands/excursion-operator|excursion operator]].

## References

1. Vladimir Drinfeld, “On a conjecture of Kashiwara,” *Mathematical Research
   Letters* 8 (2001), 713–728.
2. Vincent Lafforgue, “Chtoucas pour les groupes réductifs et paramétrisation
   de Langlands globale,” *Journal of the American Mathematical Society* 31
   (2018), 719–891, §8. [arXiv](https://arxiv.org/abs/1209.5352).
