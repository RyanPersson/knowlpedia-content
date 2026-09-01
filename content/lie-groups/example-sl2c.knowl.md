+++
id = "lie-groups/example-sl2c"
title = "Complex Lie algebra sl2(C)"
kind = "knowl"
summary = "The three-dimensional simple complex Lie algebra of trace-zero 2 by 2 matrices, of rank 1 and Dynkin type A1."
aliases = ["example-sl2c", "sl2(C)", "sl(2,C)", "complex Lie algebra sl2", "complex special linear Lie algebra sl2"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/simple-lie-algebra", "lie-groups/root-system", "lie-groups/dynkin-diagram", "lie-groups/adjoint-representation-of-a-lie-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "lie-groups/example-sl2c.md"
section_mode = "progressive"
+++

The **complex Lie algebra** \(\mathfrak{sl}_2(\mathbb C)\) is
\[
\mathfrak{sl}_2(\mathbb C)
=\{X\in M_2(\mathbb C):\operatorname{tr}X=0\},
\qquad [X,Y]=XY-YX.
\]
It is a three-dimensional [[lie-groups/simple-lie-algebra|simple Lie algebra]] of rank \(1\), with [[lie-groups/root-system|root system]] and [[lie-groups/dynkin-diagram|Dynkin type]] \(A_1\). Its defining representation is the two-dimensional module \(\mathbb C^2\), and its [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]] has dimension \(3\).

## Standard basis and roots

The matrices
\[
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
F=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix}
\]
satisfy
\[
[H,E]=2E,\qquad [H,F]=-2F,\qquad [E,F]=H.
\]
Thus \(\mathfrak h=\mathbb C H\) is a [[lie-groups/cartan-subalgebra|Cartan subalgebra]], and
\[
\mathfrak{sl}_2(\mathbb C)=\mathbb C F\oplus\mathbb C H\oplus\mathbb C E
\]
is its [[lie-groups/root-space-decomposition|root-space decomposition]]. The two roots take values \(-2\) and \(2\) on \(H\); rescaling this coordinate does not change the abstract root system \(A_1\).

## Finite-dimensional representations

For every integer \(m\geq 0\), the symmetric power
\[
\operatorname{Sym}^m(\mathbb C^2)
\]
is the irreducible highest-weight module of [[lie-groups/highest-weight|highest weight]] \(m\) and dimension \(m+1\). Every finite-dimensional irreducible \(\mathfrak{sl}_2(\mathbb C)\)-module is obtained this way. In particular, \(\operatorname{Sym}^2(\mathbb C^2)\) is the three-dimensional adjoint module.

The \(E,F,H\) relations occur inside every complex [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]]: the [[lie-groups/root-space|root spaces]] for a root \(\alpha\) and \(-\alpha\), together with the coroot, generate an \(\mathfrak{sl}_2\)-subalgebra. This is why rank-one calculations control root strings and much of [[lie-groups/highest-weight-representation|highest-weight representation]] theory.

## Groups and real forms

The connected [[lie-groups/simply-connected-lie-group|simply connected]] [[lie-groups/complex-lie-group|complex Lie group]] with this Lie algebra is \(SL(2,\mathbb C)\); its adjoint quotient is \(PSL(2,\mathbb C)=SL(2,\mathbb C)/\{\pm I\}\). These complex groups should not be confused with real forms having the same complexification. The [[lie-groups/compact-real-form|compact real form]] is \(\mathfrak{su}(2)\), while the split real form is \(\mathfrak{sl}_2(\mathbb R)\). As a real Lie algebra, \(\mathfrak{sl}_2(\mathbb C)\) has real dimension \(6\) and is isomorphic to \(\mathfrak{so}(1,3)\).

## Role in the E7 three-generation construction

In the three-generation construction, three distinguished \(\mathfrak{sl}_2\)-subalgebras occur inside a generation-symmetry \(\mathfrak{sl}_3\). The centralizer of each one in [[lie-groups/exceptional-lie-algebra-e7|\(\mathfrak e_7\)]] is a copy of [[lie-groups/complex-lie-algebra-so12|\(\mathfrak{so}_{12}(\mathbb C)\)]]. The relevant branching is
\[
\mathfrak e_7
\cong (\mathbf 3,\mathbf 1)
\oplus(\mathbf 1,\mathbf{66})
\oplus(\mathbf 2,\mathbf{32}),
\]
where \(\mathbf 3\) and \(\mathbf{66}\) are the adjoint modules of
\(\mathfrak{sl}_2\) and \(\mathfrak{so}_{12}\), respectively, and
\(\mathbf{32}\) is a [[lie-groups/half-spin-representation|half-spin module]].

## References

1. James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972, Sections 7 and 11. [Publisher record](https://doi.org/10.1007/978-1-4612-6398-2).
2. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991, Sections 11.1--11.2. [Publisher record](https://doi.org/10.1007/978-1-4612-0979-9).
3. John C. Baez, *Three Generations in E7*, 2026. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
