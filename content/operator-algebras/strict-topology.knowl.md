+++
id = "operator-algebras/strict-topology"
title = "Strict topology on a multiplier algebra"
kind = "definition"
summary = "The strict topology records norm convergence after multiplication on either side by every algebra element."
aliases = ["strict convergence", "multiplier strict topology", "strictly convergent multiplier net"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] and
\(M(A)\) its [[operator-algebras/multiplier-algebra|multiplier algebra]]. The
**strict topology** on \(M(A)\) is the locally convex topology generated, for
each \(a\in A\), by the seminorms
\[
p_a(m)=\lVert ma\rVert,\qquad q_a(m)=\lVert am\rVert.
\]
Thus a net \((m_i)\) converges **strictly** to \(m\) exactly when
\[
\lVert(m_i-m)a\rVert\to0
\quad\text{and}\quad
\lVert a(m_i-m)\rVert\to0
\]
for every \(a\in A\). The topology uses the distinguished
[[operator-algebras/essential-ideal|essential ideal]]
\(A\subseteq M(A)\); it is generally weaker than the multiplier norm topology.

## Approximate identities and strict density

If \((e_\lambda)\) is an
[[operator-algebras/approximate-identity|approximate identity]] of \(A\),
then
\[
e_\lambda\longrightarrow1_{M(A)}
\]
strictly. More generally, \(me_\lambda\to m\) and \(e_\lambda m\to m\)
strictly for every \(m\in M(A)\). Consequently the canonical copy of \(A\) is
strictly dense in \(M(A)\), even though it is norm closed there. This is the
basic mechanism by which the multiplier unit is approximated from the
nonunital algebra.

If \(A\) is unital, choosing \(a=1_A\) among the defining seminorms shows that
the strict topology equals the norm topology on \(M(A)=A\). The distinction
therefore matters primarily for nonunital algebras.

## Extension of nondegenerate maps

A [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate
\(*\)-homomorphism]] \(\phi:A\to M(B)\) has a unique unital extension
\[
\overline{\phi}:M(A)\longrightarrow M(B)
\]
that is strictly continuous and agrees with \(\phi\) on \(A\). It can be
recovered from any approximate identity by strict limits. This extension
theorem is one reason strict, rather than norm, continuity is built into the
morphism theory of multiplier algebras.

## Concrete model and comparison

For a [[linear-algebra/hilbert-space|Hilbert space]] \(H\),
\[
M(\mathcal K(H))=\mathcal B(H).
\]
On norm-bounded subsets of \(\mathcal B(H)\), the strict topology determined
by \(\mathcal K(H)\) agrees with the strong-star operator topology: both
\(T_i\xi\to T\xi\) and \(T_i^*\xi\to T^*\xi\) for every \(\xi\in H\).
This gives a useful concrete model, but strict topology is defined through
two-sided norm multiplication by elements of \(A\), not by selecting a
Hilbert-space representation.

**Warning.** Strict convergence does not ordinarily imply norm convergence.
For an infinite-dimensional \(H\), finite-rank projections increasing
strongly to \(I_H\) converge strictly to \(I_H\) in
\(M(\mathcal K(H))\), while their norm distance from \(I_H\) remains one.

## References

1. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §3.12 on multiplier algebras, strict topology, and approximate identities.
2. E. Christopher Lance, *Hilbert C*-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [DOI record](https://doi.org/10.1017/CBO9780511526206). Relevant: Chapter 2 on multipliers, strict convergence, and extensions of nondegenerate homomorphisms.
