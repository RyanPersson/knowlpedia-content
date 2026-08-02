+++
id = "harmonic-analysis/conjugate-and-contragredient-unitary-representations"
title = "Conjugate and contragredient unitary representations"
kind = "definition"
summary = "The conjugate action on the conjugate Hilbert space and the corresponding dual action on continuous linear functionals."
aliases = ["conjugate representation", "dual unitary representation"]
domains = ["harmonic-analysis", "lie-groups"]
section_mode = "progressive"
+++

Let \((\pi,\mathcal H)\) be a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of a group \(G\). Its **conjugate representation** acts on the conjugate [[linear-algebra/hilbert-space|Hilbert space]] \(\overline{\mathcal H}\) by
\[
\overline{\pi}(g)\overline{\xi}=\overline{\pi(g)\xi}.
\]
Its **contragredient representation** acts on the continuous linear dual \(\mathcal H'\) by
\[
\pi^\vee(g)\lambda=\lambda\circ\pi(g)^{-1}.
\]
Both actions are strongly continuous and unitary for their natural Hilbert structures. They are canonically unitarily equivalent through the Riesz map \(\overline{\xi}\mapsto\langle\,\cdot\,,\xi\rangle\), with the [[linear-algebra/inner-product|inner product]] taken linear in the first variable.

## Coefficients

For \(\xi,\eta\in\mathcal H\), the [[harmonic-analysis/coefficient-function|matrix coefficients]] of the conjugate representation satisfy
\[
c^{\overline{\pi}}_{\overline{\xi},\overline{\eta}}(g)
=\overline{c^\pi_{\xi,\eta}(g)}.
\]
Under the Riesz identification, the contragredient action sends the functional represented by \(\eta\) to the functional represented by \(\pi(g)\eta\). This calculation is the reason the inverse occurs in the dual-action formula.

## Relationship to equivalence

The representation \(\pi\) is **self-conjugate** when it is unitarily equivalent to \(\overline{\pi}\). This condition does not by itself decide whether a compatible real or quaternionic structure exists; those finer alternatives require an antiunitary intertwiner and a condition on its square. Conjugation also reverses scalar phases, which is important even when \(\pi\) and \(\overline{\pi}\) act on Hilbert spaces of the same dimension.

## Conventions and scope

For a general Banach-space representation, the dual action naturally lives on the Banach dual and need not share the Hilbert-space properties used above. In finite-dimensional algebra, “contragredient” is often written using inverse transpose matrices. The Riesz identification is conjugate-linear on \(\mathcal H\) but becomes linear when its source is \(\overline{\mathcal H}\).

## References

1. G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §3.1 on unitary representations and their conjugates.
