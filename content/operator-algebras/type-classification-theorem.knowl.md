+++
id = "operator-algebras/type-classification-theorem"
title = "Type decomposition of von Neumann algebras"
kind = "theorem"
summary = "Every von Neumann algebra decomposes uniquely into central summands of types I, II, and III."
aliases = ["Murray–von Neumann type classification", "I-II-III decomposition"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

For every [[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\),
there are unique pairwise orthogonal central projections
\(z_{\mathrm I},z_{\mathrm {II}},z_{\mathrm {III}}\in M\) such that
\[
z_{\mathrm I}+z_{\mathrm {II}}+z_{\mathrm {III}}=1
\]
and the central summands \(z_{\mathrm I}M\), \(z_{\mathrm {II}}M\), and
\(z_{\mathrm {III}}M\) are respectively a
[[operator-algebras/type-i-von-neumann-algebra|type I]],
[[operator-algebras/type-ii-von-neumann-algebra|type II]], and
[[operator-algebras/type-iii-von-neumann-algebra|type III von Neumann
algebra]]. Zero summands are allowed. Hence
\(M\cong z_{\mathrm I}M\oplus z_{\mathrm {II}}M\oplus
z_{\mathrm {III}}M\), canonically up to the uniquely determined central
projections.

## Construction and uniqueness

The type I projection is the central support of all
[[operator-algebras/abelian-projection|abelian projections]]. After
removing that summand, projection comparison separates the remaining algebra
into the central part supported by
[[operator-algebras/finite-projection|finite projections]] and the part containing
no nonzero finite projection. These are the type II and type III summands.
Because each defining class is stable under central summands and central
orthogonal sums, the three largest central supports are forced, which proves
uniqueness. A detailed proof appears in
[Kadison–Ringrose, Theorem 6.5.2].

## Finer decomposition

The theorem is only the first layer of the classification. The type I part
decomposes into homogeneous pieces of type \(\mathrm I_\kappa\). The type II
part separates into finite type \(\mathrm {II}_1\) and properly infinite type
\(\mathrm {II}_\infty\) central summands.
[[operator-algebras/type-iii-factor|Type III factors]] admit the finer
Connes classes \(\mathrm {III}_0\), \(\mathrm {III}_\lambda\), and
\(\mathrm {III}_1\), obtained from modular theory rather than projection
finiteness alone.

## Consequences and scope

Any property of von Neumann algebras that respects central direct sums can be
studied separately on the three summands. For a factor, central projections
are only \(0\) and \(1\), so exactly one of the three types occurs.

**Warning.** This is not a decomposition into norm-closed ideals of an
arbitrary \(C^*\)-algebra. It uses central projections inside a von Neumann
algebra and the projection theory made available by weak-operator closure.

## References

1. R. V. Kadison and J. R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. II, American Mathematical Society, 1997. [DOI record](https://doi.org/10.1090/gsm/016). Relevant: Theorem 6.5.2 and the surrounding type-decomposition theory.
2. M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on the type classification of von Neumann algebras.
