+++
id = "lie-groups/borel-de-siebenthal-theory"
title = "Borel–de Siebenthal theory"
kind = "theorem"
summary = "The root-theoretic classification of connected maximal-rank subgroups of compact Lie groups."
aliases = ["Borel-de Siebenthal theory", "Borel–de Siebenthal classification"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

**Borel–de Siebenthal theory** classifies the closed connected subgroups of
maximal rank in a compact [[lie-groups/connected-lie-group|connected Lie group]] by reducing the problem to
closed subsystems of its [[lie-groups/root-system|root system]]. In particular, if \(G\) is compact,
connected, and simple, the maximal proper connected subgroups \(H\subset G\)
that contain a [[lie-groups/maximal-torus-theorem|maximal torus]] can be read
from the extended [[lie-groups/dynkin-diagram|Dynkin diagram]], with finite [[lie-groups/central-quotient-of-a-lie-group|central quotients]] restored at
the group level.

## Extended-Dynkin-diagram procedure

Choose [[lie-groups/simple-root|simple roots]] \(\alpha_1,\ldots,\alpha_r\), and let
\[
\theta=\sum_{i=1}^r m_i\alpha_i
\]
be the highest root. Adjoin the node \(\alpha_0=-\theta\) to obtain the
extended Dynkin diagram. The maximal closed subsystems, and hence the
semisimple parts of the desired subgroups, arise in two ways. When \(m_i=1\),
deleting \(\alpha_i\) from the ordinary diagram gives a subsystem of rank
\(r-1\), accompanied by a one-dimensional central torus. When \(m_i\) is a
prime greater than one, replacing \(\alpha_i\) by \(-\theta\), equivalently
deleting \(\alpha_i\) from the extended diagram, gives a proper semisimple
subsystem of full rank. These coefficient conditions are what ensure
maximality among proper closed connected maximal-rank subgroups.

This procedure is related to, but not identical with, deleting a node from an
ordinary Dynkin diagram to obtain a [[lie-groups/levi-subalgebra|Levi subalgebra]]. Borel–de Siebenthal theory
uses the **extended** diagram and concerns compact-group subgroups of maximal
rank; Levi subalgebras arise from parabolic subalgebras of a complex reductive
algebraic or [[lie-groups/lie-algebra|Lie algebra]].

## Group-level cautions

Root systems determine Lie algebras but not the global isogeny form of a Lie
group. Consequently a subgroup identified infinitesimally as
\(\mathfrak h_1\oplus\mathfrak h_2\) may be globally a finite central quotient
of \(H_1\times H_2\). Moreover, “[[lie-groups/maximal-connected-closed-subgroup|maximal connected subgroup]]” does not imply
maximal among all closed subgroups: a disconnected normalizer may be larger.
Both distinctions are essential in applications involving stabilizer identity
components.

## Example in \(F_4\)

For the compact exceptional group \(F_4\), the theory yields maximal-rank
connected subgroups including \(\operatorname{Spin}(9)\) and a subgroup with
global form \((SU(3)\times SU(3))/\mathbb Z_3\). In the exceptional Jordan
algebra, these appear as [[lie-groups/identity-component-of-a-lie-group|identity components]] of stabilizers of distinguished
[[nonassociative-algebra/jordan-subalgebra|Jordan subalgebras]].

## References

1. Armand Borel and Jean de Siebenthal, “Les sous-groupes fermés de rang
   maximum des groupes de Lie clos,” *Commentarii Mathematici Helvetici* 23
   (1949), 200–221. [Digitized journal
   record](https://doi.org/10.5169/seals-19760).
2. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the
   Exceptional Jordan Algebra,” 2026, §§3–4.
   [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
