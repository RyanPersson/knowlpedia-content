+++
id = "lie-groups/langlands-classification-real-reductive-groups"
title = "Langlands classification for real reductive groups"
kind = "theorem"
summary = "Every irreducible admissible representation of a real reductive group is the unique quotient of a standard module."
aliases = ["Langlands quotient theorem", "nonunitary dual classification"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive Lie group]] and fix compatible standard parabolic subgroups and positive
chambers. The **Langlands classification** states that
every irreducible [[lie-groups/admissible-representation-real-reductive-group|admissible representation]] of \(G\), equivalently every irreducible
admissible \((\mathfrak g,K)\)-module, is the unique irreducible
[[lie-groups/langlands-quotient|Langlands quotient]]
\[
J(P,\sigma,\nu)
\]
of a [[lie-groups/standard-module-real-reductive-group|standard module]]
\(I(P,\sigma,\nu)\). Here \(P=MAN\), \(\sigma\) is irreducible tempered data
on \(M\), and \(\operatorname{Re}\nu\) lies in the chosen open positive
chamber. The inducing data are unique up to the prescribed conjugacies and
Weyl-group equivalences.

## Content of the classification

The theorem has three parts: a standard module has a unique irreducible
quotient; every irreducible admissible representation occurs as such a
quotient; and ordered inducing data determine that quotient uniquely up to
the standard equivalences. Langlands proves the quotient and uniqueness in
§3 and exhaustion in §4
[Langlands, §3, Lemmas 3.13–3.14, and §4, Lemma 4.2](https://publications.ias.edu/sites/default/files/classification-algebraic-groups_rpl_7.pdf).

The result classifies the admissible dual, not just the
[[harmonic-analysis/unitary-dual|unitary dual]]. A Langlands quotient may
fail to be unitarizable.

## Example

For \(G=\mathrm{SL}(2,\mathbb R)\), normalized
[[lie-groups/principal-series-representation|principal series]] induced from
the upper-triangular minimal parabolic are standard modules when the real
part of the parameter lies in the positive chamber. At reducibility points,
the induced module can have several composition factors, but the theorem
selects exactly one irreducible quotient. Other factors are not additional
Langlands quotients for the same ordered parameter.

## Conventions and scope

Changing from normalized to unnormalized induction shifts the parameter by
\(\rho_P\). Reversing the positive chamber can turn the unique-quotient
formulation into a unique-subrepresentation formulation. Some sources use
relative discrete-series data on a Levi subgroup rather than the equivalent
tempered formulation. These are convention changes in the parametrization,
not different classifications
[Knapp, Chapter XIV](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html).

The theorem does not by itself decide which quotients are unitary, nor does it
describe their full composition series.

## References

1. Robert P. Langlands, *On the Classification of Irreducible Representations of Real Algebraic Groups*, Institute for Advanced Study preprint, 1973; reprinted in *Representation Theory and Harmonic Analysis on Semisimple Lie Groups*, Mathematical Surveys and Monographs 31, American Mathematical Society, 1989. [IAS record and author PDF](https://publications.ias.edu/classification-rpl). Relevant: §3, Lemmas 3.13–3.14, and §4, Lemma 4.2.
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton Mathematical Series 36, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter XIV on standard modules and the Langlands classification.
