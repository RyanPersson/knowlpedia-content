+++
id = "noncommutative-geometry/hochschild-chain-complex"
title = "Hochschild chain complex"
kind = "definition"
summary = "The tensor chain complex of an associative algebra with coefficients in a bimodule and boundary given by adjacent multiplications."
aliases = ["Hochschild chains", "Hochschild boundary b"]
domains = ["noncommutative-geometry", "algebra-homological"]
prerequisites = ["algebra-rings/commutative-ring", "algebra-modules/bimodule", "algebra-homological/chain-complex"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(k\) be a [[algebra-rings/commutative-ring|commutative ring]], \(A\) a unital associative \(k\)-algebra, and \(M\) an [[algebra-modules/bimodule|\(A\)-bimodule]]. The **Hochschild chain complex** has
\[
C_n(A,M)=M\otimes_k A^{\otimes_k n}\qquad(n\geq0)
\]
and boundary \(b:C_n\to C_{n-1}\) given by
\[
\begin{aligned}
b(m\otimes a_1\otimes\cdots\otimes a_n)
={}&ma_1\otimes a_2\otimes\cdots\otimes a_n\\
&+\sum_{i=1}^{n-1}(-1)^i m\otimes\cdots\otimes a_i a_{i+1}\otimes\cdots\otimes a_n\\
&+(-1)^n a_n m\otimes a_1\otimes\cdots\otimes a_{n-1}.
\end{aligned}
\]
The identity \(b^2=0\) makes this an [[algebra-homological/chain-complex|chain complex]], whose homology is Hochschild homology.

## Homology and low degrees

Its homology is Hochschild homology \(HH_n(A,M)\). In degree zero,
\[
HH_0(A,M)=M/\langle ma-am:a\in A,\ m\in M\rangle.
\]
For \(M=A\), one writes \(C_n(A)=A^{\otimes(n+1)}\) and \(HH_n(A)=HH_n(A,A)\). The final term in \(b\) is what closes the linear chain cyclically by using the left \(A\)-action on \(M\).

## Normalization and cyclic theory

For a unital algebra, quotienting by chains having some \(a_i=1\) produces the normalized Hochschild complex, which has the same homology. The Hochschild boundary is also one of the two operators in Connes's cyclic bicomplex; the additional operator \(B\) supplies the cyclic direction.

## Conventions and scope

**Warning.** This is the homological complex: its boundary lowers degree. Hochschild cochains instead use \(\operatorname{Hom}_k(A^{\otimes n},M)\) and a coboundary raising degree. Nonunital, topological, bornological, and completed tensor-product versions require additional choices not included in this definition.

## References

1. J.-L. Loday, *Cyclic Homology*, 2nd ed., Springer, 1998. [Publisher record](https://doi.org/10.1007/978-3-662-11389-9). Relevant: §1.1, the Hochschild complex and boundary.
2. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-maintained text](https://www.alainconnes.org/docs/book94bigpdf.pdf). Relevant: chapter III, Hochschild and cyclic complexes.
