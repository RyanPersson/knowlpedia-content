+++
id = "linear-algebra/right-inverse"
title = "Right inverse of a linear map"
kind = "definition"
summary = "A linear map R with TR equal to the identity on the target of T."
aliases = ["right-inverse"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/linear-map", "shared-foundations/composition", "shared-foundations/surjective-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **right inverse** of a [[linear-algebra/linear-map|linear map]] \(T:V\to W\) is a linear map \(R:W\to V\) such that
\[
TR=I_W.
\]
It supplies a solution \(v=Rw\) to \(Tv=w\) for every \(w\in W\), so \(T\) is surjective. A right inverse need not be unique: adding a linear map \(K:W\to V\) satisfying \(TK=0\) preserves the identity.

## Compatibility and regularity

If a differential operator is inverted only on a subspace of compatible sources, that subspace is the target \(W\) in the right-inverse statement. Existence of an algebraic right inverse does not assert boundedness, smooth parameter dependence or support preservation; each is an additional property of the chosen inverse.

## Example

For \(T(x,y)=x\), the map \(R(t)=(t,0)\) is a right inverse. Here \(RT\) is a projection, not the identity on \(\mathbb R^2\).

## References

- [Sheldon Axler, Linear Algebra Done Right, 4th ed., Chapters 2–3, 6 and 9](https://linear.axler.net/LADR4e.pdf).
