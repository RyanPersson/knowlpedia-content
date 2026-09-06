+++
id = "differential-geometry/coisotropic-subspace"
title = "Coisotropic subspace"
kind = "definition"
summary = "A subspace of a symplectic vector space that contains its symplectic orthogonal complement."
aliases = ["coisotropic linear subspace", "co-isotropic subspace"]
domains = ["differential-geometry", "linear-algebra"]
prerequisites = ["differential-geometry/symplectic-vector-space", "convex-analysis/linear-subspace", "differential-geometry/symplectic-orthogonal-complement"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((V,\omega)\) be a [[differential-geometry/symplectic-vector-space|symplectic vector space]] and \(W\subseteq V\) a [[convex-analysis/linear-subspace|linear subspace]]. The subspace \(W\) is **coisotropic** if
\[
W^\omega\subseteq W,
\]
where \(W^\omega\) is its [[differential-geometry/symplectic-orthogonal-complement|symplectic orthogonal complement]]. The subspace \(W^\omega\) is then the **characteristic subspace** of \(W\). The restriction \(\omega|_W\) has kernel exactly \(W^\omega\), so it descends to a nondegenerate alternating form on the quotient \(W/W^\omega\). Hence \(W/W^\omega\) is naturally a symplectic vector space; this quotient is the linear model for [[differential-geometry/coisotropic-reduction|coisotropic reduction]].

## Equivalent conditions

The following conditions are equivalent: \(W\) is coisotropic; \(W^\omega\subseteq W\); the symplectic orthogonal \(W^\omega\) is isotropic; and \(\ker(\omega|_W)\) has dimension equal to \(\operatorname{codim}W\). In particular, a coisotropic subspace of a \(2n\)-dimensional symplectic vector space has dimension at least \(n\).

## Examples and boundary cases

The whole space \(V\) is coisotropic because \(V^\omega=\{0\}\). Every [[convex-analysis/hyperplane|hyperplane]] in a finite-dimensional symplectic vector space is coisotropic. A [[differential-geometry/lagrangian-subspace|Lagrangian subspace]] is both isotropic and coisotropic, since \(W=W^\omega\). By contrast, a proper [[differential-geometry/symplectic-subspace|symplectic subspace]] is not coisotropic: nondegeneracy gives \(W\cap W^\omega=\{0\}\), so \(W^\omega\subseteq W\) would force \(W=V\).

## Reduction

For \(u,v\in W\), define \(\bar\omega([u],[v])=\omega(u,v)\) on \(W/W^\omega\). This is well defined because changing either representative by an element of \(W^\omega\) leaves the value unchanged. Its kernel is zero by construction. The same mechanism globalizes, under regularity hypotheses, to the reduction of a [[differential-geometry/coisotropic-submanifold|coisotropic submanifold]] by its [[differential-geometry/characteristic-foliation|characteristic foliation]].

## Conventions and scope

Some sources write “co-isotropic.” The definition here is purely linear and finite-dimensional. For a coisotropic submanifold \(C\) of a [[differential-geometry/symplectic-manifold|symplectic manifold]], the condition is imposed pointwise as \((T_pC)^\omega\subseteq T_pC\), and forming a smooth quotient requires additional global hypotheses.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §1.1, isotropic, coisotropic, and Lagrangian subspaces.
2. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: linear symplectic algebra and reduction.
