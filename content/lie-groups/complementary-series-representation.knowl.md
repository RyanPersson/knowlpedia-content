+++
id = "lie-groups/complementary-series-representation"
title = "Complementary series representation"
kind = "definition"
summary = "A complementary series consists of unitary non-tempered members obtained by unitarizing principal-series representations away from the unitary parameter axis."
aliases = ["complementary series", "non-tempered unitary principal series"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["lie-groups/principal-series-representation", "lie-groups/real-reductive-lie-group", "lie-groups/irreducible-unitary-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(I(\lambda)\) be a normalized
[[lie-groups/principal-series-representation|principal-series family]] of a
[[lie-groups/real-reductive-lie-group|real reductive group]], induced from fixed
unitary data and a complex character \(e^\lambda\) of the split factor. A
**complementary-series representation** is an irreducible
member or irreducible constituent for a parameter with
\(\operatorname{Re}\lambda\neq 0\) that nevertheless admits a positive-definite,
invariant Hermitian form and hence a unitary Hilbert globalization. It is
non-tempered and usually lies in an open parameter region adjacent to the
unitary principal series. The term refers to such induced families, not to
every non-tempered [[lie-groups/irreducible-unitary-representation|irreducible unitary representation]].

## Construction by intertwiners

For a Weyl reflection carrying \(\lambda\) to \(-\lambda\), a suitably
normalized [[lie-groups/knapp-stein-intertwining-operator|Knapp–Stein intertwining operator]] can define a \(G\)-invariant Hermitian form on
\(I(\lambda)\). Complementary series occur precisely on those real parameter
regions where this form is positive definite; degeneracy often marks
reducibility or an endpoint.

## Rank-one example

The spherical principal series of \(\mathrm{SL}(2,\mathbb R)\) has a real
interval, on either side of the unitary axis and before the first reducibility
point, on which the intertwining form is positive. Its irreducible
globalizations form the spherical complementary series. At the central
imaginary parameter one instead has unitary principal series; beyond the
positivity interval the same [[algebra-representation-theory/induced-representation|induced representations]] are not unitarizable.

## Conventions and scope

**Warning.** Numerical endpoints depend on whether the parameter is scaled by a
root, a coroot, or the half-sum \(\rho\). Endpoint representations may be
listed as limits of complementary series but are normally not members of the
open complementary family. The trivial representation can occur at an
endpoint, so “complementary series” is not simply another name for all
non-tempered unitary representations.

## References

1. Anthony W. Knapp and Elias M. Stein, “The Existence of Complementary Series,” in *Problems in Analysis: A Symposium in Honor of Salomon Bochner*, Princeton University Press, 1970, 249–259. [DOI record](https://doi.org/10.1515/9781400869312-017). Relevant: §3, especially the invariant Hermitian form on p. 253 and the rank-one positivity result on p. 257.
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton Mathematical Series 36, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapters VII and XVI on principal-series intertwiners, complementary series, and unitarity.
