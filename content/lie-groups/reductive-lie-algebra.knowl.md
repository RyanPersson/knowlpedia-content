+++
id = "lie-groups/reductive-lie-algebra"
title = "Reductive Lie algebra"
kind = "knowl"
summary = "A Lie algebra that decomposes as a direct sum of its center and a semisimple ideal."
aliases = ["reductive-lie-algebra", "Reductive Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/reductive-lie-algebra.md"
+++

A finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak{g}\) over a field of characteristic zero is **reductive** if
\[
\mathfrak{g} = Z(\mathfrak{g}) \oplus [\mathfrak{g}, \mathfrak{g}]
\]
with \(Z(\mathfrak g)\) its center and \([\mathfrak g,\mathfrak g]\) a semisimple ideal.

## Equivalent characterizations
Under the hypotheses above, the following are equivalent:

1. \(\mathfrak{g}\) is reductive.
2. The [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]] is completely reducible.
3. \(\mathfrak{g}\) is a direct sum of simple and abelian Lie algebras.

## Examples
- Semisimple Lie algebras (center is trivial).
- Abelian Lie algebras (derived algebra is trivial).
- \(\mathfrak{gl}_n\): center is scalar matrices, derived algebra is \(\mathfrak{sl}_n\).
- \(\mathfrak{u}(n)=Z(\mathfrak u(n))\oplus\mathfrak{su}(n)\), where \(Z(\mathfrak u(n))=i\mathbb R I_n\).

## Non-example
The Lie algebra of upper triangular matrices is not reductive (it is solvable but not semisimple).
