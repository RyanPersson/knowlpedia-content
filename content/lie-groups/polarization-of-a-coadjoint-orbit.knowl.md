+++
id = "lie-groups/polarization-of-a-coadjoint-orbit"
title = "Polarization at a coadjoint functional"
kind = "definition"
summary = "A maximal-dimensional Lie subalgebra on which the alternating form defined by a coadjoint functional vanishes."
aliases = ["subordinate subalgebra of maximal dimension", "real polarization", "complex polarization"]
domains = ["lie-groups", "representation-theory", "differential-geometry"]
section_mode = "progressive"
+++

Let \(\mathfrak g\) be a finite-dimensional real [[lie-groups/lie-algebra|Lie algebra]] and \(\ell\in\mathfrak g^*\). Set
\[
B_\ell(X,Y)=\ell([X,Y]),\qquad
\mathfrak g_\ell=\{X:B_\ell(X,\mathfrak g)=0\}.
\]
A **real polarization at \(\ell\)** is a [[lie-groups/lie-subalgebra|Lie subalgebra]] \(\mathfrak p\subseteq\mathfrak g\) such that \(\ell([\mathfrak p,\mathfrak p])=0\) and
\[
\dim\mathfrak p=\tfrac12(\dim\mathfrak g+\dim\mathfrak g_\ell).
\]
Thus \(\mathfrak p\) is a maximal-dimensional isotropic subspace for \(B_\ell\) that is also closed under the [[fiber-bundles/lie-bracket|Lie bracket]]. A **complex polarization** is defined analogously as a complex Lie subalgebra of \(\mathfrak g_{\mathbb C}\), subordinate to the complex-linear extension of \(\ell\), with the corresponding complex dimension.

## Relation to the coadjoint orbit

The radical \(\mathfrak g_\ell\) is the stabilizer Lie algebra of \(\ell\), while \(B_\ell\) descends to the nondegenerate [[differential-geometry/kirillov-kostant-souriau-form|Kirillov form]] on \(\mathfrak g/\mathfrak g_\ell\), the [[differential-geometry/tangent-space|tangent space]] to the [[differential-geometry/coadjoint-orbit|coadjoint orbit]]. The dimension formula therefore says that \(\mathfrak p/\mathfrak g_\ell\) is Lagrangian in that [[differential-geometry/symplectic-quotient|symplectic quotient]]. The bracket-closure condition is additional: a merely [[differential-geometry/isotropic-subspace|maximal isotropic subspace]] need not integrate to a subgroup and is not a polarization.

## From a polarization to a representation

Suppose \(G\) is connected and simply connected nilpotent with Lie algebra \(\mathfrak g\), and let \(P=\exp(\mathfrak p)\). Subordination makes
\[
\chi_\ell(\exp X)=e^{i\ell(X)}
\]
a [[harmonic-analysis/unitary-character|unitary character]] of \(P\). The
[[harmonic-analysis/unitary-induced-representation|unitarily induced
representation]] \(\operatorname{Ind}_P^G\chi_\ell\) is irreducible, is
independent up to unitary equivalence of the chosen polarization, and depends
only on the coadjoint orbit of \(\ell\). These conclusions are
special to the nilpotent orbit-method setting; the bare definition alone
does not guarantee them for a general [[fiber-bundles/lie-group|Lie group]].

## Heisenberg example

For the three-dimensional Heisenberg algebra with basis \(X,Y,Z\) and \([X,Y]=Z\), choose \(\ell(Z)=\lambda\neq0\). Then \(\mathfrak g_\ell=\mathbb RZ\), and \(\mathfrak p=\operatorname{span}\{Y,Z\}\) is a polarization: it is abelian and has dimension \(2=(3+1)/2\). The line \(\mathbb RY\) is subordinate but not a polarization because it is too small. Choosing \(\operatorname{span}\{X,Z\}\) instead leads to an equivalent [[algebra-representation-theory/irreducible-representation|irreducible representation]].

## Conventions and scope

Some sources call any maximal subordinate subalgebra a polarization. For [[lie-groups/nilpotent-lie-algebra|nilpotent Lie algebras]] this is normally paired with the dimension condition in the core. For [[algebra-groups/solvable-group|solvable groups]], additional conditions such as the Pukánszky condition can be required. A complex polarization may also be required to be positive or invariant under a stabilizer; those are strengthened notions and are not included here.

## References

1. A. A. Kirillov, *Lectures on the Orbit Method*, Graduate Studies in Mathematics 64, American Mathematical Society, 2004. [AMS record](https://bookstore.ams.org/GSM/64). Relevant: Chapters 2–3 on polarizations, the Heisenberg group, and nilpotent groups.
2. Lawrence J. Corwin and Frederick P. Greenleaf, *Representations of Nilpotent Lie Groups and Their Applications, Part I: Basic Theory and Examples*, Cambridge Studies in Advanced Mathematics 18, Cambridge University Press, 1990. [Publisher front matter](https://assets.cambridge.org/97805216/04956/frontmatter/9780521604956_frontmatter.pdf). Relevant: Chapter 2 on coadjoint orbits, polarizations, and induced representations.
