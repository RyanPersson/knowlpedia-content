+++
id = "operator-algebras/spectral-mapping-theorem"
title = "Spectral mapping theorem"
kind = "theorem"
summary = "Functional calculus carries the spectrum of an element to the image of that spectrum under the function."
aliases = ["spectrum of f(a)", "spectral mapping"]
domains = ["operator-algebras", "functional-analysis"]
prerequisites = ["functional-analysis/banach-algebra", "functional-analysis/banach-algebra-spectrum", "functional-analysis/holomorphic-functional-calculus-banach-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a complex unital [[functional-analysis/banach-algebra|Banach algebra]], let \(a\in A\), and let \(f\) be holomorphic on a neighborhood of the [[functional-analysis/banach-algebra-spectrum|spectrum]] \(\sigma_A(a)\). For \(f(a)\) defined by the [[functional-analysis/holomorphic-functional-calculus-banach-algebra|holomorphic functional calculus]], the **spectral mapping theorem** states
\[
\sigma_A(f(a))=f(\sigma_A(a)).
\]
If \(A\) is a unital \(C^*\)-algebra, \(a\) is normal, and \(f\) is continuous on \(\sigma_A(a)\), the same identity holds for the [[operator-algebras/continuous-functional-calculus|continuous functional calculus]]. Thus functional calculus transports spectral values exactly; it neither adds nor loses them.

## Proof mechanism

For the holomorphic calculus, if \(\mu\notin f(\sigma_A(a))\), then
\[
g(z)=\frac{1}{f(z)-\mu}
\]
is holomorphic near \(\sigma_A(a)\), and the composition rule gives
\((f(a)-\mu 1_A)g(a)=1_A\). This proves one inclusion. For the reverse inclusion, factor \(f(z)-f(\lambda)\) by \(z-\lambda\) near a chosen \(\lambda\in\sigma_A(a)\); invertibility of \(f(a)-f(\lambda)1_A\) would force invertibility of \(a-\lambda1_A\).

## Consequences

Polynomial spectral mapping is the special case
\(\sigma_A(p(a))=p(\sigma_A(a))\). The theorem also detects invertibility:
\(f(a)\) is invertible exactly when \(0\notin f(\sigma_A(a))\). For a normal
element of a \(C^*\)-algebra, it combines with the norm formula to yield
\[
\lVert f(a)\rVert=\max_{\lambda\in\sigma_A(a)}|f(\lambda)|.
\]

## Conventions and scope

**Warning.** The allowed functions depend on the calculus. Holomorphic
spectral mapping applies to an arbitrary Banach-algebra element, whereas the
continuous version requires a normal element in a \(C^*\)-algebra. For a
nonunital algebra, spectra and functional calculus are taken in the
[[operator-algebras/unitization|unitization]]; an additional condition such
as \(f(0)=0\) is needed to ensure that \(f(a)\) lies in the original algebra.

## References

1. Gerard J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §1.3 on holomorphic functional calculus and spectral mapping, and Theorem 2.1.10 on continuous functional calculus.
2. F. F. Bonsall and J. Duncan, *Complete Normed Algebras*, Springer, 1973. [DOI record](https://doi.org/10.1007/978-3-642-65669-9). Relevant: the chapters on spectra and analytic functional calculus in Banach algebras.
