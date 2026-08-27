+++
id = "differential-geometry/octonionic-projective-line"
title = "Octonionic projective line"
kind = "definition"
summary = "The eight-sphere obtained as the projective quotient of the unit sphere in the octonionic plane."
aliases = ["Cayley projective line", "OP^1", "octonionic line space"]
domains = ["differential-geometry", "nonassociative-algebra", "octonionic-analysis"]
section_mode = "progressive"
+++

For unit vectors \(\xi,\eta\in S^{15}\subset\mathbb O^2\), define
\[
\xi\sim\eta\quad\Longleftrightarrow\quad
\xi\xi^*=\eta\eta^*.
\]
The **octonionic projective line** is the smooth quotient
\[
\mathbb OP^1=S^{15}/{\sim}.
\]
It is diffeomorphic to \(S^8\), equivalently to the
[[topology/one-point-compactification|one-point compactification]]
\(\mathbb O\cup\{\infty\}\).

## Octonionic Hopf fibration

The quotient map
\[
S^{15}\longrightarrow\mathbb OP^1\cong S^8
\]
has fibers diffeomorphic to \(S^7\) and is the octonionic Hopf fibration. It
is not a principal \(S^7\)-bundle: the unit octonions form a Moufang loop, not
an associative [[fiber-bundles/lie-group|Lie group]].

## Lines in the octonionic plane

Each point of \(\mathbb OP^1\) determines an eight-dimensional real linear
subspace of \(\mathbb O^2\), called an octonionic line. Their translates are
the [[complex-analysis/octonionic-affine-line|affine octonionic lines]] used to
test [[complex-analysis/octonionic-plurisubharmonic-function|octonionic
plurisubharmonicity]].

## Spin symmetry

The [[lie-groups/spin9-spin-representation|spin representation of
\(\operatorname{Spin}(9)\)]] on \(\mathbb O^2\) makes the Hopf fibration
equivariant and acts transitively on \(\mathbb OP^1\).

## References

1. Semyon Alesker, “Plurisubharmonic functions on the octonionic plane and \(\operatorname{Spin}(9)\)-invariant valuations on convex sets,” *Journal of Geometric Analysis* 18 (2008), 651–686. [arXiv record](https://arxiv.org/abs/0707.4385). Relevant: §1.3.
2. John C. Baez, “The Octonions,” *Bulletin of the American Mathematical Society* 39 (2002), 145–205. [DOI record](https://doi.org/10.1090/S0273-0979-01-00934-X). Relevant: §4.2.
