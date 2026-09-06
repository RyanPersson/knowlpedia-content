+++
id = "algebra-representation-theory/character-orthonormality"
title = "Orthonormality of irreducible characters"
kind = "knowl"
summary = "With respect to the standard inner product on class functions, irreducible characters are orthonormal (and over ℂ they form an orthonormal basis)."
aliases = ["character-orthonormality", "Orthonormality of irreducible characters"]
domains = ["algebra-representation-theory"]
prerequisites = ["algebra-groups/class-function", "linear-algebra/inner-product", "algebra-groups/conjugacy-class"]
dependency_review_count = 1
legacy_source_path = "algebra-representation-theory/character-orthonormality.md"
+++

Let \(G\) be a finite group, and let \(\mathrm{Cl}(G;\mathbb C)\) denote the \(\mathbb C\)-vector space of complex-valued [[algebra-groups/class-function|class functions]] on \(G\).

Define the standard [[linear-algebra/inner-product|inner product]] by
\[
\langle f,g\rangle \;:=\; \frac{1}{|G|}\sum_{x\in G} f(x)\,\overline{g(x)}.
\]

**Orthonormality theorem.** If \(\chi\) and \(\psi\) are irreducible complex characters of \(G\), then
\[
\langle\chi,\psi\rangle=\delta_{\chi,\psi}.
\]

Equivalently, summing over [[algebra-groups/conjugacy-class|conjugacy classes]] \(C\),
\[
\langle f,g\rangle=\sum_C\frac{|C|}{|G|}f(C)\overline{g(C)}.
\]

## Consequences
1. **Multiplicity formula.**
   If \(V\) is a complex representation with character \(\chi_V\) and \(\chi_i\) is irreducible, then the multiplicity \(m_i\) of the corresponding irreducible representation in \(V\) is
   \[
   m_i \;=\; \langle \chi_V,\chi_i\rangle \in \mathbb Z_{\ge 0}.
   \]
   This uses [[algebra-representation-theory/maschkes-theorem|Maschke's theorem]] / [[algebra-representation-theory/completely-reducible-representation|complete reducibility]] over \(\mathbb C\).

2. **Orthonormal basis of class functions (over \(\mathbb C\)).**
   The irreducible characters form an orthonormal basis of \(\mathrm{Cl}(G;\mathbb C)\). In particular, every class function \(f\) has a unique expansion
   \[
   f \;=\; \sum_i \langle f,\chi_i\rangle\, \chi_i.
   \]
   The spanning/basis part is tied to [[algebra-representation-theory/number-irreducibles-conjugacy-classes|the number of irreducibles equals the number of conjugacy classes]].

3. **Character tables.**
   Writing the character table with rows \(\chi_i\) and columns indexed by conjugacy classes, orthonormality implies the rows are orthonormal with respect to the weights \(|C|/|G|\). (There is also a “column orthogonality” relation, equivalent to the same set of facts.)

## Examples

Let \(G=C_n=\langle a\rangle\) with \(|G|=n\), and fix \(\zeta=e^{2\pi i/n}\). The irreducible characters are 1-dimensional:
\[
\chi_k(a^m)=\zeta^{km}\qquad (k=0,1,\dots,n-1).
\]
Then
\[
\langle \chi_k,\chi_\ell\rangle
=\frac1n\sum_{m=0}^{n-1}\zeta^{km}\overline{\zeta^{\ell m}}
=\frac1n\sum_{m=0}^{n-1}\zeta^{(k-\ell)m}
=\begin{cases}
1,&k=\ell,\\
0,&k\ne \ell,
\end{cases}
\]
since the sum is a geometric series.
