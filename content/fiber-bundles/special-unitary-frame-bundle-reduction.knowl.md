+++
id = "fiber-bundles/special-unitary-frame-bundle-reduction"
title = "Special unitary frame bundle"
kind = "knowl"
summary = "A unit determinant trivialization selects a principal SU(n)-subbundle of the unitary frame bundle."
aliases = ["special-unitary-frame-bundle-reduction", "Special unitary frame bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/special-unitary-frame-bundle-reduction.md"
+++

Let $E\to M$ be a complex rank-$n$ vector bundle over a [[fiber-bundles/smooth-manifold|smooth manifold]], equipped with a [[fiber-bundles/hermitian-metric|Hermitian metric]]. Choose a unit-norm nowhere-vanishing section
$$
\Omega\in\Gamma(\det E),\qquad \det E:=\Lambda^nE.
$$
The **special unitary frame bundle** determined by $\Omega$ is
$$
\operatorname{SU}(E,\Omega)
=\{(e_1,\ldots,e_n)\in\operatorname{U}(E):
e_1\wedge\cdots\wedge e_n=\Omega_x,\ e_i\in E_x\}.
$$
It is a principal $\operatorname{SU}(n)$-subbundle of the unitary frame bundle $\operatorname{U}(E)$, hence an $\operatorname{SU}(n)$-reduction of its structure group.

Such a reduction exists exactly when the determinant line bundle $\det E$ is trivial. A trivializing section can always be rescaled to have unit norm.

## Equivalent data

Giving an $\operatorname{SU}(n)$-reduction of $\operatorname{U}(E)$ is equivalent to giving a unit-norm trivializing section $\Omega$ of $\det E$. The Hermitian metric on $E$ induces the metric used on $\det E$; see [[fiber-bundles/exterior-power-bundle|exterior power bundle]].

## Examples
1. **Trivial bundle.** For $E=M\times\mathbb C^n$ with its standard metric and $\Omega=\mathbf e_1\wedge\cdots\wedge\mathbf e_n$, one has $\operatorname{SU}(E,\Omega)\cong M\times\operatorname{SU}(n)$.

2. **Rank one.** If $n=1$, then $\operatorname{SU}(1)=\{1\}$. A chosen unit-norm trivialization of the Hermitian line bundle $E$ gives a special unitary frame bundle canonically identified with $M$.
