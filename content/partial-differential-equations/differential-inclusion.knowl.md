+++
id = "partial-differential-equations/differential-inclusion"
title = "Differential inclusion"
kind = "definition"
summary = "A derivative is required to belong to a prescribed set instead of equaling a single prescribed value."
aliases = []
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["real-analysis/total-derivative-frechet-derivative", "shared-foundations/subset", "topology/open-set", "linear-algebra/matrix"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For \(u:\Omega\subset\mathbb R^n\to\mathbb R^m\), a **first-order differential inclusion** has the form
\[
Du(x)\in K(x,u(x)),
\]
where \(Du\) is the [[real-analysis/total-derivative-frechet-derivative|derivative]] and \(K(x,z)\) is a specified [[shared-foundations/subset|subset]] of the space of \(m\)-by-\(n\) [[linear-algebra/matrix|matrices]]. The domain \(\Omega\) is [[topology/open-set|open]]. The required regularity of \(u\) and whether inclusion holds everywhere or almost everywhere are part of the problem.

## Linear equations plus a pointwise constraint

In fluid dynamics one often uses the same terminology for a linear differential system on enlarged variables together with a nonlinear pointwise constraint. For Euler, \(\partial_t v+\operatorname{div}S+\nabla q=0\), \(\operatorname{div}v=0\), and \(S=v\otimes v-|v|^2I/n\) give such a formulation.

## References

- [De Lellis and Székelyhidi, The Euler equations as a differential inclusion (2009)](https://annals.math.princeton.edu/wp-content/uploads/annals-v170-n3-p09-p.pdf).
