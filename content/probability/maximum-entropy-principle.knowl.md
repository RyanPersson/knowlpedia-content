+++
id = "probability/maximum-entropy-principle"
title = "Maximum entropy principle"
kind = "knowl"
summary = "A rule for selecting a probability distribution by maximizing entropy subject to known constraints."
aliases = ["maximum-entropy-principle", "Maximum entropy principle"]
domains = ["probability"]
prerequisites = []
dependency_review_count = 1
legacy_source_path = "probability/maximum-entropy-principle.md"
+++

A **maximum entropy principle** selects, when a maximizer exists, a probability distribution \(P^\star\) from a nonempty feasible class \(\mathcal C\) such that
\[
P^\star \in \operatorname*{arg\,max}_{P\in\mathcal C} H(P),
\]

where \(H\) is the chosen entropy functional and \(\mathcal C\) is the feasible class of distributions.

The guiding idea is to choose a distribution that adds as little structure as the entropy model permits beyond the stated constraints. This depends on the chosen entropy and, in the continuous case, on the underlying coordinates or reference measure. Relative-entropy minimization against a specified reference distribution is the corresponding reference-dependent formulation.

## Examples

For discrete laws, \(H\) is commonly [[probability/shannon-entropy|Shannon entropy]]; for absolutely continuous laws it is often [[probability/differential-entropy|differential entropy]]. A typical feasible class is specified by support or moment constraints, for example \(\mathbb E_P[g_i(X)]=c_i\).
- On a finite set of \(n\) outcomes, the uniform distribution maximizes Shannon entropy.
- Among probability distributions on \(\mathbb R\) with a fixed mean and a fixed positive variance, the normal distribution with those parameters maximizes differential entropy.
