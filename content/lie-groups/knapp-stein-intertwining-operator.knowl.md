+++
id = "lie-groups/knapp-stein-intertwining-operator"
title = "Knapp–Stein intertwining operator"
kind = "definition"
summary = "A Knapp–Stein operator is the meromorphically continued and normalized standard integral intertwining two Weyl-related principal-series representations."
aliases = ["standard intertwining operator", "normalized intertwiner"]
domains = ["lie-groups", "harmonic-analysis"]
prerequisites = ["lie-groups/real-reductive-lie-group", "lie-groups/normalized-parabolic-induction", "lie-groups/intertwining-operator-unitary-representations"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive group]],
\(P=MAN\) a parabolic subgroup, and \(I_P(\sigma,\lambda)\) a representation
formed by [[lie-groups/normalized-parabolic-induction|normalized parabolic induction]]. For a Weyl-group
element \(w\) carrying the inducing data to \((w\sigma,w\lambda)\), a
**Knapp–Stein intertwining operator**
\[
R(w,\sigma,\lambda)\colon I_P(\sigma,\lambda)
   \longrightarrow I_{wPw^{-1}}(w\sigma,w\lambda)
\]
is the meromorphic continuation in \(\lambda\) of the standard integral over
the appropriate unipotent subgroup, multiplied by scalar normalizing factors.
It is a [[lie-groups/intertwining-operator-unitary-representations|representation intertwiner]] wherever regular, and the normalization is chosen to satisfy
Weyl-group composition and unitarity identities.

## Integral and continuation

In a chamber where the unipotent integral converges absolutely, the operator is
defined directly on smooth induced functions. Analytic continuation then
extends it meromorphically to the full complex parameter space. Poles, zeros,
and noninvertibility detect reducibility phenomena in
[[lie-groups/principal-series-representation|principal series]].

## Normalization and consequences

After normalization, one obtains identities of the form
\[
R(w_1w_2,\lambda)=R(w_1,w_2\lambda)R(w_2,\lambda)
\]
when lengths and parameters permit the corresponding factorization, together
with \(R(w,\lambda)^*=R(w^{-1},-\overline{\lambda})\). On the unitary axis the
regular normalized operators are unitary. Their eigenspaces can control
reducible constituents, while positivity of an associated Hermitian form
produces
[[lie-groups/complementary-series-representation|complementary series]].

## Conventions and scope

**Warning.** “Standard intertwining operator” may denote the unnormalized
integral, its meromorphic continuation, or a normalized Knapp–Stein operator.
Normalizing scalars depend on [[harmonic-analysis/haar-measure|Haar measures]]
and on root and \(c\)-function conventions. The source and target may also be
identified in a compact picture, hiding the conjugated parabolic in the
displayed formula.

## References

1. Anthony W. Knapp and Elias M. Stein, “Intertwining Operators for Semisimple Groups,” *Annals of Mathematics* 93 (1971), 489–578. [DOI record](https://doi.org/10.2307/1970887). Relevant: construction, meromorphic continuation, normalization, and functional equations.
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton Mathematical Series 36, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter VII on principal-series intertwining operators.
