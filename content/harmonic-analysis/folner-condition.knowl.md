+++
id = "harmonic-analysis/folner-condition"
title = "Følner condition"
kind = "definition"
summary = "A small-boundary condition requiring finite-measure sets that are nearly invariant under translation by prescribed compact subsets."
aliases = ["Folner condition", "Følner net"]
domains = ["harmonic-analysis", "algebra-groups"]
section_mode = "progressive"
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/haar-measure"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] with left [[harmonic-analysis/haar-measure|Haar measure]] \(\mu\). A net \((F_i)\) of measurable, relatively compact subsets with \(0<\mu(F_i)<\infty\) is a **left Følner net** if, for every compact subset \(C\subseteq G\),
\[
\sup_{g\in C}\frac{\mu(gF_i\mathbin{\triangle}F_i)}
{\mu(F_i)}\longrightarrow0.
\]
The group satisfies the **Følner condition** if it admits such a net. For a discrete group with counting measure, this says that finite nonempty subsets have boundary negligible relative to their size. A Følner sequence is a Følner net indexed by the positive integers.

## Relation to amenability

The Følner condition gives almost invariant probability densities by normalizing the indicators \(1_{F_i}\), and hence produces a [[harmonic-analysis/invariant-mean|left-invariant mean]] through a weak-star cluster point. Conversely, standard Følner criteria recover nearly invariant sets from amenability under the usual locally compact hypotheses. This connects geometric boundary smallness with [[harmonic-analysis/amenable-locally-compact-group|amenability]].

## Examples and non-examples

For \(\mathbb Z^d\), the boxes \(F_n=\{-n,\ldots,n\}^d\) form a Følner sequence because translating by a fixed finite set changes only a boundary layer of order \(n^{d-1}\), while \(\lvert F_n\rvert\) has order \(n^d\). Expansion prevents the [[algebra-groups/free-group|free group]] on two generators from having a Følner net; in particular, its balls have boundary comparable in size to their volume.

## Conventions and scope

Some formulations use \(\mu(CF_i\mathbin{\triangle}F_i)\), others demand uniformity over \(g\in C\), and still others use the equivalent Leptin growth condition. Nets are the natural general form; the existence of a sequence can require countability assumptions. Right Følner conditions must account for the modular function when [[lie-groups/right-translation|right translation]] does not preserve left Haar measure.

## References

1. Alan L. T. Paterson, *Amenability*, Mathematical Surveys and Monographs 29, American Mathematical Society, 1988. [AMS DOI record](https://doi.org/10.1090/surv/029). Relevant: Følner conditions and their relationship with invariant means.
2. Erling Følner, “On groups with full Banach mean value,” *Mathematica Scandinavica* 3 (1955), 243–254. [DOI record](https://doi.org/10.7146/math.scand.a-10442). Relevant: the original discrete-group condition.
