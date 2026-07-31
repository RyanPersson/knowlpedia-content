+++
id = "operator-algebras/quasicentral-approximate-identity"
title = "Quasicentral approximate identity"
kind = "definition"
summary = "A quasicentral approximate identity for an ideal also asymptotically commutes with every element of the ambient C*-algebra."
aliases = ["quasi-central approximate unit", "quasicentral approximate unit"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(I\) be a [[operator-algebras/closed-two-sided-ideal|closed two-sided ideal]] in a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\). A
**quasicentral approximate identity for \(I\) in \(A\)** is a positive
contractive [[operator-algebras/approximate-identity|approximate identity]]
\((e_\lambda)\) for \(I\) such that
\[
\lVert e_\lambda a-ae_\lambda\rVert\longrightarrow0
\qquad(a\in A).
\]
Thus the net must approximate the identity on \(I\) from both sides and must
asymptotically commute, in norm, with the entire ambient algebra. The phrase
“in \(A\)” matters: the same approximate identity can be quasicentral
relative to one containing algebra and not another.

## Existence theorem

Every closed [[algebra-rings/two-sided-ideal|two-sided ideal]] \(I\triangleleft A\) has a quasicentral
approximate identity in \(A\). Starting from an ordinary approximate identity
for \(I\), one uses
[[convex-analysis/convex-combination|convex combinations]] to make finitely
many commutators small while preserving the approximation properties;
directing the construction by finite subsets and error tolerances yields the
required net
[Arveson, §1.7].

The theorem guarantees a net, not necessarily a sequence. Countability
hypotheses can allow sequential forms, but the definition itself should not
replace the indexing net by [[shared-foundations/natural-numbers|natural numbers]].

## Examples and a near-miss

If \(A\) is commutative, every approximate identity for every ideal is
automatically quasicentral. If \(A\) is unital and \(I=A\), the constant net
\(e_\lambda=1_A\) is quasicentral.

In contrast, let \(P_n\) project \(\ell^2(\mathbb N)\) onto the first \(n\)
standard basis vectors. The sequence \((P_n)\) is an approximate identity for
\(K(\ell^2)\), but it is not quasicentral in \(B(\ell^2)\): for the unilateral
shift \(S\), one has \(\lVert P_nS-SP_n\rVert=1\). This does not contradict
the existence theorem, which may require a different net.

## Extension-theoretic role

Quasicentral approximate identities let computations in an ideal approach
central behavior relative to an extension algebra. They are used to separate
ideal and quotient contributions, construct asymptotic splittings, and
control commutators in extension theory. Quasicentrality does not mean that
any \(e_\lambda\) is central, nor does it imply norm convergence of
\((e_\lambda)\) to an element of \(A\)
[Blackadar, §II.4].

## References

1. William Arveson, *An Invitation to \(C^*\)-Algebras*, Graduate Texts in Mathematics 39, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4612-6371-5). Relevant: §1.7 on quasicentral approximate units.
2. Bruce Blackadar, *Operator Algebras: Theory of \(C^*\)-Algebras and von Neumann Algebras*, Springer, 2006. [DOI record](https://doi.org/10.1007/3-540-28517-2). Relevant: §II.4 on approximate units and quasicentrality.
