+++
id = "operator-algebras/nuclear-cstar-algebra"
title = "Nuclear C*-algebra"
kind = "definition"
summary = "A C*-algebra whose algebraic tensor product with every C*-algebra has a unique C*-tensor norm."
aliases = ["C*-nuclearity", "nuclearity of a C*-algebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

A [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\) is **nuclear** if,
for every \(C^*\)-algebra \(B\), the algebraic tensor product \(A\odot B\)
has a unique [[operator-algebras/cstar-tensor-norm|\(C^*\)-tensor norm]].
Equivalently, for every \(B\), the canonical quotient from the
[[operator-algebras/maximal-cstar-tensor-product|maximal tensor product]]
\(A\otimes_{\max}B\) onto the
[[operator-algebras/minimal-cstar-tensor-product|minimal tensor product]]
\(A\otimes_{\min}B\) is an isomorphism. No unitality or separability
assumption is part of the definition. Nuclearity says that \(A\) cannot
detect the distinction between universal and spatial completions, not that
\(A\) is finite-dimensional or commutative.

## Completely positive characterization

The Choi–Effros–Kirchberg approximation theorem says that \(A\) is nuclear
exactly when it has the
[[operator-algebras/completely-positive-approximation-property|completely
positive approximation property]]. Concretely, the identity on \(A\) can be
approximated in point-norm by factorizations
\[
A\xrightarrow{\ \phi_\lambda\ }M_{n(\lambda)}(\mathbb C)
\xrightarrow{\ \psi_\lambda\ }A
\]
through [[operator-algebras/matrix-cstar-algebra|matrix algebras]], where both
maps are [[operator-algebras/completely-positive-contraction|completely positive contractions]]
[Brown–Ozawa, Theorem 2.3.8]. This converts a
global tensor-norm condition into finite-dimensional local approximations.

## Examples and permanence

Every [[operator-algebras/commutative-cstar-algebra|commutative
\(C^*\)-algebra]], every matrix algebra, the
[[operator-algebras/compact-operator-cstar-algebra|compact-operator
\(C^*\)-algebra]], and every AF algebra are nuclear. Nuclearity passes to
ideals, quotients, inductive limits, and extensions, but not to arbitrary
\(C^*\)-subalgebras.

For a discrete group \(\Gamma\), the
[[operator-algebras/nuclearity-reduced-group-cstar-algebra-discrete-amenability|
Lance theorem]] states that \(C_r^*(\Gamma)\) is nuclear exactly when
\(\Gamma\) is amenable. Hence the reduced \(C^*\)-algebra of the free group on
two generators, a [[algebra-groups/free-group|free group]], is a standard
non-example.

## Structural significance

Nuclearity is an operator-algebraic regularity property. It permits tensor
products to be written without choosing between minimal and maximal norms and
is a standing hypothesis in much of the structure and classification theory
of \(C^*\)-algebras. It is stronger than
[[operator-algebras/exact-cstar-algebra|exactness]] and stronger than ordinary
Banach-space approximation properties.

The original tensor-norm theory and its completely positive formulation were
developed through several equivalent characterizations; the approximation
form is especially useful because it behaves well under limits and
constructions
[Choi–Effros, pp. 61–79].

## Conventions and scope

**Warning.** Nuclearity here is a property of a \(C^*\)-algebra and its
\(C^*\)-tensor products. It should not be conflated with nuclearity of locally
convex spaces or nuclear operators between [[linear-algebra/banach-space|Banach spaces]]. “Amenable
\(C^*\)-algebra” is sometimes used for an equivalent Banach-algebraic
property, but “amenable group” is a separate notion connected to nuclearity
only through specific theorems.

## References

1. E. Christopher Lance, “On nuclear C*-algebras,” *Journal of Functional Analysis* 12 (1973), 157–176. [DOI record](https://doi.org/10.1016/0022-1236%2873%2990021-9). Relevant: tensor-norm characterizations and group C*-algebras.
2. Man-Duen Choi and Edward G. Effros, “Nuclear C*-Algebras and the Approximation Property,” *American Journal of Mathematics* 100 (1978), 61–79. [DOI record](https://doi.org/10.2307/2373876). Relevant: completely positive approximation methods.
3. Nathanial P. Brown and Narutaka Ozawa, *C*-Algebras and Finite-Dimensional Approximations*, Graduate Studies in Mathematics 88, American Mathematical Society, 2008. [DOI record](https://doi.org/10.1090/gsm/088). Relevant: §2.3, especially Theorem 2.3.8, on tensor products, CPAP, and nuclearity.
