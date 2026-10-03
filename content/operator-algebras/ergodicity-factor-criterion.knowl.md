+++
id = "operator-algebras/ergodicity-factor-criterion"
title = "Ergodicity and factoriality of a free crossed product"
kind = "theorem"
summary = "For an essentially free probability-preserving action, the crossed product is a factor exactly when the action is ergodic."
aliases = []
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/group-measure-space-construction", "ergodic-theory/essentially-free-action", "ergodic-theory/ergodic-action", "operator-algebras/von-neumann-factor", "operator-algebras/maximal-abelian-subalgebra", "operator-algebras/fixed-point-algebra"]
+++

Let a countable discrete group \(G\) act [[ergodic-theory/essentially-free-action|essentially freely]] by probability-preserving transformations on a standard probability space. For \(M=L^\infty(X,\mu)\rtimes G\),
\[
Z(M)=L^\infty(X,\mu)^G.
\]
Consequently, \(M\) is a [[operator-algebras/von-neumann-factor|factor]] if and only if the action is [[ergodic-theory/ergodic-action|ergodic]]. If also \(X\) is atomless, the factor is of type \(\mathrm{II}_1\).

## Reason

Essential freeness makes the included \(A=L^\infty(X)\) [[operator-algebras/maximal-abelian-subalgebra|maximal abelian]]. A central element must therefore lie in \(A\). It commutes with the implementing unitaries exactly when it is fixed by every \(\alpha_g\). This gives the center formula; the fixed-function criterion gives the ergodicity equivalence.

## Freeness is a hypothesis

For an \(n\)-cycle viewed as a \(\mathbb Z\)-action, \(u^n\) is central in the regular crossed product and is not scalar. Thus the action is ergodic but the crossed product is not a factor. Omitting essential freeness would make the stated equivalence false.

## References

1. Sorin Popa, [*Ergodic theory of group actions*](https://www.math.ucla.edu/~popa/Books/OElectures.pdf). Theorem 4.1.1.
