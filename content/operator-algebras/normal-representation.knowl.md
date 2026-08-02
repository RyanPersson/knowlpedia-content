+++
id = "operator-algebras/normal-representation"
title = "Normal representation"
kind = "definition"
summary = "A representation of a von Neumann algebra on a Hilbert space that is ultraweakly continuous."
aliases = ["ultraweakly continuous representation"]
domains = ["operator-algebras", "algebra-representation-theory"]
section_mode = "progressive"
+++

Let \(M\) be a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] and \(H\) a
[[linear-algebra/hilbert-space|Hilbert space]]. A **normal representation** of
\(M\) on \(H\) is a
[[operator-algebras/cstar-representation|\(C^*\)-algebra representation]]
\[
\pi:M\longrightarrow\mathcal B(H)
\]
that is a
[[operator-algebras/normal-star-homomorphism|normal \(*\)-homomorphism]].
Equivalently, \(\pi\) is continuous from the ultraweak topology of \(M\) to
the [[operator-algebras/ultraweak-topology|ultraweak operator topology]] of
\(\mathcal B(H)\). Normality is separate
from faithfulness and unitality. Under the convention that representations
are nondegenerate, one additionally requires
\(\overline{\pi(M)H}=H\), which for unital \(M\) is equivalent to
\(\pi(1)=I_H\).

## Coefficient-functional criterion

The representation is normal exactly when every coefficient functional
\[
x\longmapsto\langle\pi(x)\xi,\eta\rangle,\qquad \xi,\eta\in H,
\]
belongs to the [[operator-algebras/predual|predual]] \(M_*\). Equivalently,
for every bounded increasing net \((x_i)\) of positive elements,
\(\pi(\sup_i x_i)=\sup_i\pi(x_i)\). These criteria connect the concrete
operator representation with the canonical weak-star structure of \(M\).

## Examples and a non-example

The defining inclusion of a concrete von Neumann algebra
\(M\subseteq\mathcal B(H)\) is normal, as is any spatial amplification
\(x\mapsto x\otimes I_K\). Direct sums of normal representations are normal.
The representation of \(\ell^\infty(\mathbb N)\) on \(\mathbb C\) given by a
free-ultrafilter character is not normal: it fails to preserve the supremum
of the increasing sequence of finite-coordinate projections.

## Decomposition and scope

A degenerate normal representation splits as its nondegenerate restriction
on \(\overline{\pi(M)H}\) plus the zero representation on the orthogonal
complement. Normal representations are therefore often defined to be unital
without losing the nonzero essential part, but the convention should be
stated.

**Warning.** A representation of the underlying \(C^*\)-algebra need not be
normal. Norm continuity is automatic for every representation and does not
ensure compatibility with monotone or ultraweak limits.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: the chapters on normal representations, preduals, and ultraweak continuity.
2. Shôichirô Sakai, *C*-Algebras and *W*-Algebras, Springer, 1971; Classics in Mathematics reprint, 1998. [DOI record](https://doi.org/10.1007/978-3-642-61993-9). Relevant: representations of abstract \(W^*\)-algebras and normality.
