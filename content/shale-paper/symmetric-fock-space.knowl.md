+++
id = "shale-paper/symmetric-fock-space"
title = "Symmetric Fock Space S(H)"
kind = "knowl"
summary = "The Hilbert direct sum of the symmetric tensor powers of a complex Hilbert space, with its vacuum vector."
aliases = ["symmetric-fock-space", "Symmetric Fock Space S(H)"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/symmetric-fock-space.md"
+++

Let $H$ be a complex Hilbert space. Its **symmetric (bosonic) Fock space** is the Hilbert direct sum
$$
S(H)=\widehat{\bigoplus}_{n=0}^\infty \operatorname{Sym}^n(H),
$$
where $\operatorname{Sym}^n(H)$ is the completed symmetric $n$-fold tensor power. The unit vector $e_0\in\operatorname{Sym}^0(H)\cong\mathbb C$ is the **vacuum vector**.

## Remarks

**Key properties (paper use):**
- Carries creation/annihilation operators and the Fock–Cook field operators.
- The canonical action of $U(H)$ second-quantizes to a unitary action on $S(H)$.

## Examples

- If $H=\mathbb C$, then $S(H)\cong \ell^2(\mathbb N_0)$.
