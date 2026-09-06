+++
id = "differential-geometry/lagrangian-grassmannian"
title = "Lagrangian Grassmannian"
kind = "definition"
summary = "The smooth parameter space of all Lagrangian subspaces of a finite-dimensional symplectic vector space."
aliases = ["Grassmannian of Lagrangian subspaces", "space of Lagrangian subspaces", "Λ(n)"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/symplectic-vector-space", "differential-geometry/lagrangian-subspace", "differential-geometry/embedded-submanifold", "differential-geometry/grassmannian"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((V,\omega)\) be a real [[differential-geometry/symplectic-vector-space|symplectic vector space]] of dimension \(2n\). The **Lagrangian Grassmannian**
\[
\Lambda(V)=\{L\in\operatorname{Gr}_n(V):L=L^\omega\}
\]
is the set of all [[differential-geometry/lagrangian-subspace|Lagrangian subspaces]] of \(V\), with the [[differential-geometry/embedded-submanifold|smooth submanifold]] structure inherited from the [[differential-geometry/grassmannian|\(n\)-plane Grassmannian]]. Here \(L^\omega=\{v\in V:\omega(v,L)=0\}\), so membership requires both isotropy and the maximal possible isotropic dimension. After choosing a compatible complex structure and a unitary identification \(V\cong\mathbb C^n\), the unitary group acts transitively, and the stabilizer of \(\mathbb R^n\) is \(O(n)\); hence \(\Lambda(V)\cong U(n)/O(n)\).

## Local model and dimension

Fix complementary Lagrangian subspaces \(V=L\oplus L'\). Every Lagrangian plane transverse to \(L'\) is the graph of a [[linear-algebra/linear-map|linear map]] \(A:L\to L'\). Identifying \(L'\cong L^*\) using \(\omega\), the graph is Lagrangian exactly when the associated bilinear form is symmetric. Thus this chart is modeled on \(\operatorname{Sym}^2(L^*)\), and
\[
\dim_{\mathbb R}\Lambda(V)=\frac{n(n+1)}2.
\]

## Topology and the Maslov class

The homogeneous-space description shows that \(\Lambda(V)\) is compact and connected. Its [[topology/fundamental-group|fundamental group]] is infinite cyclic. A preferred generator of \(H^1(\Lambda(V);\mathbb Z)\) is the [[differential-geometry/maslov-class-lagrangian-grassmannian|universal Maslov class]]; pulling it back along a loop or a [[differential-geometry/lagrangian-gauss-map|Lagrangian Gauss map]] produces the corresponding Maslov invariant. Arnol'd relates this class to the cycle of planes meeting a fixed Lagrangian nontrivially.

## Examples

For \(n=1\), every line in \(\mathbb R^2\) is Lagrangian, so \(\Lambda(1)=\mathbb RP^1\cong S^1\). For \(n>1\), the Lagrangian Grassmannian is a proper submanifold of \(\operatorname{Gr}_n(\mathbb R^{2n})\): an \(n\)-plane on which \(\omega\) does not vanish is not a point of \(\Lambda(V)\).

## Conventions and scope

The notation \(\Lambda(n)\) means the Lagrangian Grassmannian of the standard symplectic \(\mathbb R^{2n}\). The identification with \(U(n)/O(n)\) depends on auxiliary compatible linear data, although its diffeomorphism type does not. The complex Lagrangian Grassmannian of a complex symplectic vector space is a different homogeneous variety and should not be conflated with this real manifold.

## References

1. V. I. Arnol'd, “On a characteristic class entering into conditions of quantization,” *Functional Analysis and Its Applications* 1 (1967), 1–14. [DOI record](https://doi.org/10.1007/BF01079201). Relevant: the Lagrangian Grassmannian, Maslov cycle, and characteristic class.
2. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: §2.1, linear symplectic geometry and Lagrangian subspaces.
