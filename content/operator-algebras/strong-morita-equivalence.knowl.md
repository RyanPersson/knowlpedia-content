+++
id = "operator-algebras/strong-morita-equivalence"
title = "Strong Morita equivalence of C*-algebras"
kind = "definition"
summary = "An equivalence of C*-algebras witnessed by a full imprimitivity bimodule."
aliases = ["C*-Morita equivalence", "Rieffel Morita equivalence"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Two [[operator-algebras/cstar-algebra|\(C^*\)-algebras]] \(A\) and \(B\) are **strongly Morita equivalent** when there exists an [[operator-algebras/imprimitivity-bimodule|\(A\)-\(B\) imprimitivity bimodule]] \(X\). Concretely, \(X\) is a full right Hilbert \(B\)-module with a nondegenerate \(*\)-homomorphism
\[
A\longrightarrow\mathcal L_B(X)
\]
whose image is exactly \(\mathcal K_B(X)\), the \(C^*\)-algebra of compact adjointable operators on \(X\). Equivalently, \(X\) carries compatible full \(A\)- and \(B\)-valued inner products satisfying
\[
{}_A\langle x,y\rangle z=x\langle y,z\rangle_B.
\]
The existence of such an \(X\), not a chosen algebra isomorphism, is the defining equivalence.

## Equivalence relation and representations

Strong Morita equivalence is reflexive, symmetric, and transitive. The conjugate bimodule reverses an equivalence, while the [[operator-algebras/internal-tensor-product-correspondences|interior tensor product]] composes two of them. [[operator-algebras/rieffel-induction|Rieffel induction]] through \(X\) gives an equivalence between the nondegenerate representation categories of \(A\) and \(B\) [Rieffel, induced representations](https://doi.org/10.1016/0001-8708%2874%2990068-1).

Ideals, primitive spectra, and many structural properties correspond under this equivalence. In particular, type I and continuous-trace behavior are Morita invariant.

## Examples and non-examples

For any Hilbert space \(H\), the module \(H\) is a \(\mathcal K(H)\)-\(\mathbb C\) imprimitivity bimodule, so \(\mathcal K(H)\) is strongly Morita equivalent to \(\mathbb C\). More generally, \(M_n(A)\) is strongly Morita equivalent to \(A\).

Morita equivalence is weaker than \(*\)-isomorphism: \(\mathcal K(H)\) and \(\mathbb C\) are not isomorphic when \(H\) is infinite-dimensional. A general \(C^*\)-correspondence is a near miss; without fullness and the identification of the left action with compact operators, it need not implement an equivalence.

## References

1. M. A. Rieffel, “Induced Representations of \(C^*\)-Algebras,” *Advances in Mathematics* 13 (1974), 176–257. [DOI record](https://doi.org/10.1016/0001-8708%2874%2990068-1). Relevant: imprimitivity bimodules, induction, and equivalence of representation theories.
2. I. Raeburn and D. P. Williams, *Morita Equivalence and Continuous-Trace \(C^*\)-Algebras*, Mathematical Surveys and Monographs 60, American Mathematical Society, 1998. [DOI record](https://doi.org/10.1090/surv/060). Relevant: Chapter 3 on imprimitivity bimodules and strong Morita equivalence.
