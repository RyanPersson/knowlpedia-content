+++
id = "operator-algebras/c0-x-algebra"
title = "C_0(X)-algebra"
kind = "definition"
summary = "A C*-algebra equipped with a central nondegenerate action of C_0(X)."
aliases = ["C0(X)-algebra", "C*-algebra over a space", "central C_0(X)-algebra"]
domains = ["operator-algebras", "topology"]
section_mode = "progressive"
+++

Let \(X\) be a [[topology/locally-compact-space|locally compact Hausdorff space]]. A **\(C_0(X)\)-algebra** is a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\) together with a [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate \(*\)-homomorphism]]
\[
\Phi\colon C_0(X)\longrightarrow ZM(A),
\]
where \(ZM(A)\) is the center of the [[operator-algebras/multiplier-algebra|multiplier algebra]]. Thus \(\Phi(f)a=a\Phi(f)\) and the closed linear span of \(C_0(X)A\) is \(A\). One usually writes \(fa\) for \(\Phi(f)a\).
The pair \((A,\Phi)\), rather than \(A\) alone, is the \(C_0(X)\)-algebra.

## Geometric meaning

The central action says where an element of \(A\) is supported over \(X\). Multiplying by \(f\in C_0(X)\) localizes that element to the region where \(f\) is nonzero. Nondegeneracy ensures that this localization sees all of \(A\), including when \(A\) is nonunital.

The structure map is part of the data: the same underlying \(C^*\)-algebra can carry inequivalent \(C_0(X)\)-algebra structures.

## Fibers

For \(x\in X\), let
\[
I_x=\overline{\Phi(\{f\in C_0(X):f(x)=0\})A}.
\]
This is a [[operator-algebras/closed-two-sided-ideal|closed two-sided ideal]], and the quotient
\[
A_x=A/I_x
\]
is the [[operator-algebras/fiber-c0-x-algebra|fiber of \(A\) at \(x\)]]. Each \(a\in A\) determines a section \(x\mapsto a(x)\), where \(a(x)=a+I_x\).

## Morphisms and examples

The basic example is \(A=C_0(X,B)\), with \(\Phi(f)g(x)=f(x)g(x)\); every fiber is \(B\). More generally, the [[operator-algebras/section-algebra-cstar-bundle|section algebra]] of an upper-semicontinuous \(C^*\)-bundle is a \(C_0(X)\)-algebra.

A homomorphism between \(C_0(X)\)-algebras is \(C_0(X)\)-linear when it respects the given actions. An ordinary \(*\)-homomorphism need not do so.

## References

1. May Nilsen, “C*-Bundles and \(C_0(X)\)-Algebras,” *Indiana University Mathematics Journal* 45 (1996), 463–477. [DOI record](https://doi.org/10.1512/iumj.1996.45.1086). Relevant: the definition and bundle realization of \(C_0(X)\)-algebras.
2. Dana P. Williams, *Crossed Products of C*-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: Appendix C on \(C_0(X)\)-algebras.
