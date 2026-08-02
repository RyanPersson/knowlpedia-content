+++
id = "operator-algebras/support-projection-of-functional"
title = "Support projection of a normal positive functional"
kind = "definition"
summary = "The least projection on which a normal positive functional is concentrated."
aliases = ["carrier projection of a functional"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]
and let \(\varphi\) be a positive
[[operator-algebras/normal-functional|normal functional]] on \(M\). The
**support projection** \(s(\varphi)\) is the least
[[operator-algebras/projection-cstar-algebra|projection]] \(p\in M\) such that
\(\varphi(p)=\varphi(1)\). Equivalently,
\[
s(\varphi)=1-\sup\{q\in M:q\text{ is a projection and }\varphi(q)=0\}.
\]
Any projection with the first property is said to support \(\varphi\);
leastness makes \(s(\varphi)\) unique and identifies the smallest corner on
which the functional is concentrated.
It satisfies \(\varphi(x)=\varphi(s(\varphi)x s(\varphi))\) for every
\(x\in M\). This definition includes \(s(0)=0\); for nonzero \(\varphi\), its
restriction to the corner \(s(\varphi)Ms(\varphi)\) is faithful.

## Equivalent tests

For a projection \(p\in M\), the following conditions are equivalent:
\(\varphi(p)=\varphi(1)\), \(\varphi(1-p)=0\), and
\(\varphi(x)=\varphi(pxp)\) for every \(x\in M\). Normality is what permits the
supremum of all \(\varphi\)-null projections to remain null. Consequently,
\(\varphi\) is faithful exactly when \(s(\varphi)=1\). These support
properties are part of the standard theory of normal positive forms.

## Concrete models

For \(M=B(H)\) and
\(\varphi(x)=\operatorname{Tr}(\rho x)\), where \(\rho\) is positive and
trace class, \(s(\varphi)\) is the
[[linear-algebra/orthogonal-projection|orthogonal projection]] onto
\(\overline{\operatorname{ran}\rho}\). In particular, the support of the
vector functional \(x\mapsto\langle x\xi,\xi\rangle\) is the rank-one
projection onto \(\mathbb C\xi\). In a commutative model \(M=L^\infty(X,\mu)\),
the support is multiplication by the essential support of the density
representing \(\varphi\).

## Distinctions

The support projection need not be central. The
[[operator-algebras/central-support|central support]] of \(\varphi\) is the
least central projection dominating \(s(\varphi)\), and can be strictly
larger. Support also differs from the support of an individual element:
\(s(\varphi)\) records which corner of \(M\) the functional detects.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: the chapter on normal positive functionals, supports, and polar decomposition.
