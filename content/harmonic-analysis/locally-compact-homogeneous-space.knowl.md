+++
id = "harmonic-analysis/locally-compact-homogeneous-space"
title = "Locally compact homogeneous space"
kind = "definition"
summary = "A quotient G/H of a locally compact group by a closed subgroup, equipped with its transitive continuous G-action."
aliases = ["topological homogeneous space", "locally compact quotient homogeneous space", "homogeneous G-space G/H"]
domains = ["harmonic-analysis", "topology", "lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact Hausdorff
group]] and \(H\leq G\) a closed subgroup. The **locally compact homogeneous
space** \(G/H\) is the set of left cosets \(gH\), equipped with the
[[topology/quotient-topology|quotient topology]] and the
[[topology/continuous-group-action|continuous action]]
\[
x\cdot(gH)=(xg)H.
\]
It is a locally compact Hausdorff space, and the action is transitive. More
generally, a locally compact homogeneous \(G\)-space means a \(G\)-space
equivariantly homeomorphic to some \(G/H\) with \(H\) closed. This
topological notion does not require \(G\) to be a Lie group or \(G/H\) to be
a manifold.

## Quotient topology

The canonical projection \(q:G\to G/H\) is continuous, surjective, and open:
for every open \(U\subseteq G\),
\[
q^{-1}(q(U))=UH=\bigcup_{h\in H}Uh
\]
is open. Closedness of \(H\) is exactly what makes the quotient Hausdorff.
Local compactness descends through the open quotient map, so compact
neighborhoods in \(G\) yield relatively compact neighborhoods in \(G/H\).

## Stabilizers and recognition

If \(G\) acts continuously and transitively on a Hausdorff space \(X\), the
stabilizer \(G_x\) is closed and the orbit map induces a continuous
\(G\)-equivariant bijection
\[
G/G_x\longrightarrow X,\qquad gG_x\longmapsto g\cdot x.
\]
It is a homeomorphism when the orbit map \(G\to X\) is a quotient map—for
example, when it is open. Transitivity alone should not silently be used to
claim this topological conclusion without an applicable quotient-map
hypothesis.

## Measures on the quotient

A quotient \(G/H\) carries a natural
[[harmonic-analysis/quasi-invariant-measure|quasi-invariant measure class]]
under standard locally compact hypotheses. It carries a nonzero invariant
Radon measure precisely when the modular functions satisfy
\[
\Delta_G|_H=\Delta_H.
\]
The [[harmonic-analysis/weil-integration-formula|Weil integration formula]]
describes integration on \(G\) in terms of integration along \(H\) and over
\(G/H\), including the correction needed when an invariant quotient measure
does not exist.

## Lie-group specialization

When \(G\) is a Lie group, every closed subgroup \(H\) is a Lie subgroup and
\(G/H\) has a canonical smooth structure. It is then the
[[lie-groups/homogeneous-space|smooth homogeneous space]] associated with the
transitive Lie-group action. The locally compact definition is broader: it
also includes quotients of totally disconnected, profinite, discrete, and
\(p\)-adic groups.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §2.6 on homogeneous spaces, rho-functions, and quasi-invariant measures.
2. Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis*, Volume I, 2nd ed., Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4419-8638-2). Relevant: quotient spaces of locally compact groups and invariant integration.
