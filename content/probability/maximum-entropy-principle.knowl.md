+++
id = "probability/maximum-entropy-principle"
title = "Maximum entropy principle"
kind = "knowl"
summary = "A rule for selecting a probability distribution by maximizing entropy subject to known constraints."
aliases = ["maximum-entropy-principle", "Maximum entropy principle"]
domains = ["probability"]
legacy_source_path = "probability/maximum-entropy-principle.md"
+++

A **maximum entropy principle** selects, when a maximizer exists, a probability distribution $P^\star$ from a nonempty feasible class $\mathcal C$ such that
$$
P^\star \in \operatorname*{arg\,max}_{P\in\mathcal C} H(P),
$$

where $H$ is [[probability/shannon-entropy|Shannon entropy]] for discrete laws and often [[probability/differential-entropy|differential entropy]] for absolutely continuous laws. The class $\mathcal C$ is usually specified by support or moment constraints such as $\mathbb E_P[g_i(X)]=c_i$.

The guiding idea is to choose a distribution that adds as little structure as the entropy model permits beyond the stated constraints. This depends on the chosen entropy and, in the continuous case, on the underlying coordinates or reference measure. Relative-entropy minimization against a specified reference distribution is the corresponding reference-dependent formulation.

## Examples

- On a finite set of $n$ outcomes, the uniform distribution maximizes Shannon entropy.
- Among probability distributions on $\mathbb R$ with a fixed mean and a fixed positive variance, the normal distribution with those parameters maximizes differential entropy.
