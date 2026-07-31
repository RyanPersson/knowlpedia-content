+++
id = "operator-algebras/nondegenerate-cstar-representation"
title = "Nondegenerate representation of a C*-algebra"
kind = "definition"
summary = "A representation whose image acts on a dense subspace of the whole representation Hilbert space."
aliases = ["non-degenerate C*-representation", "essential representation"]
domains = ["operator-algebras", "representation-theory"]
section_mode = "progressive"
+++

Let \(\pi:A\to\mathcal B(H)\) be a
[[operator-algebras/cstar-representation|representation of a \(C^*\)-algebra]].
It is **nondegenerate** if
\[
\overline{\operatorname{span}\{\pi(a)\xi:a\in A,\ \xi\in H\}}=H.
\]
Equivalently, no nonzero vector is annihilated by every operator \(\pi(a)\).
This is the representation-space instance of a
[[operator-algebras/nondegenerate-star-homomorphism|nondegenerate
\(*\)-homomorphism]]. It does not mean that \(\pi\) is injective: faithfulness
controls the kernel in \(A\), whereas nondegeneracy says that the represented
algebra has no zero orthogonal summand in \(H\).

## Approximate-identity criteria

If \((e_i)\) is an
[[operator-algebras/approximate-identity|approximate identity]] of \(A\), then
\(\pi\) is nondegenerate exactly when
\[
\pi(e_i)\xi\longrightarrow\xi\qquad(\xi\in H).
\]
Thus \(\pi(e_i)\) converges strongly to \(I_H\), independently of the chosen
approximate identity. If \(A\) is unital, the condition reduces to
\(\pi(1_A)=I_H\). These equivalences are proved in
[Pedersen, the chapter on representations].

## Essential subspace

For an arbitrary representation, the essential subspace
\[
H_{\mathrm{ess}}=\overline{\operatorname{span}\pi(A)H}
\]
reduces \(\pi\). The restriction to \(H_{\mathrm{ess}}\) is nondegenerate,
while the restriction to \(H_{\mathrm{ess}}^\perp\) is zero. Hence every
representation decomposes canonically as a [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate representation]] plus
a zero representation.

## Extension to multipliers

A nondegenerate representation extends uniquely to a unital representation of
the [[operator-algebras/multiplier-algebra|multiplier algebra]] \(M(A)\), with
convergence in the [[operator-algebras/strict-topology|strict topology]]
carried to convergence in the
[[operator-algebras/strong-operator-topology|strong operator topology]]. This
extension property is a principal reason that nondegenerate representations
are the standard convention for nonunital \(C^*\)-algebras.

## References

1. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 3 on representations, approximate identities, and nondegeneracy.
2. Dana P. Williams, *Crossed Products of C*-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: Appendix A on nondegenerate homomorphisms and multiplier extensions.
