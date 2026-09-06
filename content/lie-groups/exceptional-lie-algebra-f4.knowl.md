+++
id = "lie-groups/exceptional-lie-algebra-f4"
title = "Exceptional Lie algebra f4"
kind = "knowl"
summary = "The 52-dimensional simple complex Lie algebra of rank 4 and exceptional Dynkin type F4."
aliases = ["exceptional-lie-algebra-f4", "f4", "complex Lie algebra f4", "exceptional Lie algebra F4"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/simple-lie-algebra", "lie-groups/root-system", "algebra-representation-theory/irreducible-representation"]
dependency_review_count = 1
section_mode = "progressive"
+++

The **exceptional complex Lie algebra** \(\mathfrak f_4\) is the unique [[lie-groups/simple-lie-algebra|simple complex Lie algebra]] whose [[lie-groups/root-system|root system]] has Dynkin type \(F_4\). It has complex dimension \(52\), rank \(4\), and \(48\) roots, occurring in two root lengths.

Its smallest nontrivial [[algebra-representation-theory/irreducible-representation|irreducible representation]] is the \(26\)-dimensional fundamental module \(\mathbf{26}\); its adjoint representation is \(\mathbf{52}\).

## Exceptional Jordan-algebra realization

Let \(J_{\mathbb C}=H_3(\mathbb O)\otimes_{\mathbb R}\mathbb C\) be the complex [[nonassociative-algebra/exceptional-jordan-algebra|Albert algebra]]. Then
\[
\mathfrak f_4\cong\operatorname{Der}(J_{\mathbb C}),
\]
the [[lie-groups/lie-algebra|Lie algebra]] of derivations of its Jordan product. The decomposition
\[
J_{\mathbb C}=\mathbb C I\oplus J_{\mathbb C,0}
\]
separates the fixed identity line from the trace-zero subspace; \(J_{\mathbb C,0}\) is the irreducible \(\mathbf{26}\).

## Groups and real forms

Type \(F_4\) has trivial fundamental group and trivial diagram automorphism group, so its [[lie-groups/simply-connected-lie-group|simply connected]] and adjoint complex groups coincide and have trivial center. The real automorphism group of the Euclidean Albert algebra is the [[lie-groups/compact-exceptional-lie-group-f4|compact exceptional group \(F_4\)]]. Its Lie algebra complexifies to \(\mathfrak f_4\). The split real form instead acts on the split Albert algebra.

## Paper context

The exceptional-Jordan-algebra construction works with compact \(F_4=\operatorname{Aut}(H_3(\mathbb O))\). For suitable nested [[nonassociative-algebra/jordan-subalgebra|Jordan subalgebras]] \(X\cong H_2(\mathbb C)\subset B\cong H_3(\mathbb C)\), it gives
\[
\operatorname{Stab}(X)\cap\operatorname{Stab}(B)^0
\cong S(U(2)\times U(3)),
\]
the [[mathematical-physics/standard-model-gauge-group|Standard Model gauge group]]. This is a group statement in the [[lie-groups/compact-real-form|compact real form]]; passing to \(\mathfrak f_4\) complexifies its infinitesimal symmetry algebra but discards global stabilizer information.

## References

1. Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4--6*, Springer, 2002, Plate VIII. [Publisher record](https://doi.org/10.1007/978-3-540-89394-3).
2. John Frank Adams, *Lectures on Exceptional Lie Groups*, University of Chicago Press, 1996, Chapters 5--6. [Publisher record](https://press.uchicago.edu/ucp/books/book/chicago/L/bo3683975.html).
3. Kevin McCrimmon, *A Taste of Jordan Algebras*, Springer, 2004, Chapter 6. [Publisher record](https://doi.org/10.1007/b97489).
4. John C. Baez and Paul Schwahn, *The Standard Model Gauge Group from the Exceptional Jordan Algebra*, 2026. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
