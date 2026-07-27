+++
id = "operator-algebras/star-automorphism"
title = "*-automorphism"
kind = "definition"
summary = "A bijective star-homomorphism from a C-star algebra to itself."
aliases = ["C*-automorphism", "automorphism of a C*-algebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A
**\(*\)-automorphism** of \(A\) is a
[[operator-algebras/star-isomorphism|\(*\)-isomorphism]]
\(\alpha:A\to A\); equivalently, it is a bijective complex-linear map that
preserves multiplication and involution. Its inverse is again a
\(*\)-automorphism. Under composition, all such maps form the automorphism
group \(\operatorname{Aut}(A)\). If \(A\) is unital, every
\(*\)-automorphism preserves \(1_A\) automatically. No topology on
\(\operatorname{Aut}(A)\), continuity in an external parameter, or choice of
an implementing operator is included in the definition.

## Inner and outer automorphisms

For a [[operator-algebras/unitary-element|unitary]] \(u\) in a unital
\(C^*\)-algebra, conjugation
\[
\operatorname{Ad}_u(a)=uau^*
\]
is a \(*\)-automorphism. Such automorphisms are inner; automorphisms not of this
form are outer. For a nonunital algebra, inner automorphisms are naturally
implemented by unitaries in the
[[operator-algebras/multiplier-algebra|multiplier algebra]]. The quotient by
inner automorphisms records genuinely external symmetries
[Pedersen, §1.2 and Chapter 8](https://doi.org/10.1016/C2016-0-03431-9).

## Preserved structure

Every \(*\)-automorphism is isometric and preserves spectra, positivity,
ideals, approximate identities, and functional calculus. It therefore acts on
the state space by pullback and transports representations by composition.
For commutative \(A=C_0(X)\), \(*\)-automorphisms correspond contravariantly to
homeomorphisms of \(X\), giving the basic geometric model
[Murphy, §§2.1 and 2.2](https://doi.org/10.1016/C2009-0-22289-6).

## Dynamical conventions and near-misses

A \(C^*\)-dynamical system requires an action \(g\mapsto\alpha_g\) by
\(*\)-automorphisms together with a stated continuity condition; individual
automorphisms are automatically norm-continuous as maps \(A\to A\), but this
does not make the parameter map continuous. A conjugate-linear multiplicative
involution, an anti-automorphism that reverses products, or a merely isometric
linear bijection is not a \(*\)-automorphism unless it also satisfies every
algebraic requirement in the core.

## References

1. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §1.2 and Chapter 8 on automorphisms, inner implementation, and automorphism groups.
2. Gerard J. Murphy, *C*-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §§2.1–2.2 on \(*\)-isomorphisms, commutative \(C^*\)-algebras, and preserved structure.
