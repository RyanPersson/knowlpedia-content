+++
id = "operator-algebras/toeplitz-representation-cstar-correspondence"
title = "Toeplitz representation of a C*-correspondence"
kind = "definition"
summary = "A compatible pair representing a C*-correspondence and its coefficient algebra inside another C*-algebra."
aliases = ["covariant representation of a correspondence", "Toeplitz pair"]
domains = ["operator-algebras", "algebra-representation-theory"]
section_mode = "progressive"
+++

Let \(X\) be a [[operator-algebras/cstar-correspondence|\(C^*\)-correspondence]]
over \(A\), with left action \(\varphi_X\). A **Toeplitz representation** of
\(X\) in a \(C^*\)-algebra \(B\) is a
[[linear-algebra/linear-map|linear map]] \(t:X\to B\) and a
[[operator-algebras/star-homomorphism|\(*\)-homomorphism]] \(\pi:A\to B\)
such that, for \(a\in A\) and \(\xi,\eta\in X\),
\[
t(\xi a)=t(\xi)\pi(a),\qquad
t(\varphi_X(a)\xi)=\pi(a)t(\xi),\qquad
t(\xi)^*t(\eta)=\pi(\langle\xi,\eta\rangle_A).
\]
The represented \(C^*\)-algebra is \(C^*(\pi(A),t(X))\). No injectivity,
nondegeneracy, or Cuntz–Pimsner covariance is part of the definition unless
stated separately.

## The induced compact-operator representation

Every Toeplitz representation determines a
\(*\)-homomorphism
\[
t^{(1)}:\mathcal K_A(X)\longrightarrow B,\qquad
t^{(1)}(\theta_{\xi,\eta})=t(\xi)t(\eta)^*,
\]
on the [[operator-algebras/compact-operator-hilbert-module|compact
Hilbert-module operators]]. The inner-product relation makes this formula
multiplicative and independent of a chosen rank-one decomposition. This
induced map is the object compared with \(\pi\) in the Cuntz–Pimsner
covariance relation [Katsura, opening definitions](https://doi.org/10.1016/j.jfa.2004.03.010).

## Fock representation

On the Fock module \(\mathcal F(X)\), each \(\xi\in X\) defines a creation
operator \(T_\xi(\eta)=\xi\otimes\eta\), while \(A\) acts diagonally on tensor
powers. The pair \((T,\varphi_\infty)\) is a Toeplitz representation and gives
the standard concrete model. Its relation
\(T_\xi^*T_\eta=\varphi_\infty(\langle\xi,\eta\rangle_A)\) is the operator
form of the last defining axiom.

## Conventions and nearby notions

Some authors call this simply a “representation” of \(X\), reserving
“covariant representation” for a pair satisfying an additional quotient
relation. Others use “Toeplitz-covariant representation” for the definition
above. The phrase “covariant representation” alone is therefore ambiguous.
The three displayed relations encode the module actions and inner product;
they should not be replaced by the weaker requirement that \(t\) is merely a
bounded linear map.

## References

1. Takeshi Katsura, “On C*-algebras associated with C*-correspondences,” *Journal of Functional Analysis* 217 (2004), 366–401. [DOI record](https://doi.org/10.1016/j.jfa.2004.03.010). Relevant: the opening definitions of representations, induced compact-operator maps, and covariance.
2. Michael V. Pimsner, “A Class of C*-Algebras Generalizing Both Cuntz–Krieger Algebras and Crossed Products by Z,” in *Free Probability Theory*, Fields Institute Communications 12, American Mathematical Society, 1997, 189–212. [Bibliographic record](https://cir.nii.ac.jp/crid/1570572699254124800). Relevant: Toeplitz representations and the universal Toeplitz construction.
