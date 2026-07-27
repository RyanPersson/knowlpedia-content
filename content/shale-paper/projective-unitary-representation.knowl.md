+++
id = "shale-paper/projective-unitary-representation"
title = "Projective Unitary Representation"
kind = "knowl"
summary = "A homomorphism into a projective unitary group, equivalently unitary operators whose multiplication law holds up to phase."
aliases = ["projective-unitary-representation", "Projective Unitary Representation"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/projective-unitary-representation.md"
+++

A **projective unitary representation** of a group \(G\) on a complex Hilbert space \(H\) is a homomorphism
\[
\overline U:G\longrightarrow PU(H)=U(H)/U(1).
\]
Equivalently, after choosing a unitary representative \(U_g\) of each projective class, there is a function \(\omega:G\times G\to U(1)\) such that
\[
U_gU_h=\omega(g,h)U_{gh}.
\]
Associativity forces the cocycle identity
\[
\omega(g,h)\omega(gh,k)=\omega(h,k)\omega(g,hk).
\]
Changing the representatives \(U_g\) changes \(\omega\) by a coboundary but leaves \(\overline U\) unchanged.

## Remarks

Shale's implementers \(Y(T)\) are unique only up to phase, so their unitary rays define a projective representation. A projective representation lifts to an ordinary unitary representation precisely when its multiplier class is trivial; it may instead lift after passing to a central extension of \(G\).

## Examples

- Spin representations give projective unitary representations of rotation groups and ordinary representations of their double covers.
