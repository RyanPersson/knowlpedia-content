+++
id = "algebra-representation-theory/schurs-lemma"
title = "Schur's Lemma"
kind = "knowl"
summary = "A nonzero intertwiner between irreducible representations is an isomorphism; equivariant endomorphisms form a division ring and, under standard hypotheses, are scalars."
aliases = ["schurs-lemma", "Schur's Lemma"]
domains = ["algebra-representation-theory"]
prerequisites = ["algebra-representation-theory/group-representation", "algebra-representation-theory/irreducible-representation"]
dependency_review_count = 1
legacy_source_path = "algebra-representation-theory/schurs-lemma.md"
+++

Let \(G\) be a group and let \(k\) be a field. A (finite-dimensional) \(k\)-[[algebra-representation-theory/group-representation|representation]] of \(G\) is a \(k\)-vector space \(V\) with a homomorphism \(\rho_V: G \to \mathrm{GL}(V)\). A \(G\)-**intertwiner** (or \(G\)-map) \(f:V\to W\) between two representations is a \(k\)-linear map satisfying
\[
f(\rho_V(g)v) \;=\; \rho_W(g)f(v)\quad \text{for all } g\in G,\ v\in V.
\]

**Schur's lemma.** If \(V,W\) are [[algebra-representation-theory/irreducible-representation|irreducible representations]] of \(G\) over \(k\), then:

1. Every nonzero \(G\)-intertwiner \(f:V\to W\) is an isomorphism.
2. Consequently, \(\operatorname{End}_G(V)\) is a division ring.
3. If \(k\) is algebraically closed and \(V\) is finite-dimensional, then \(\operatorname{End}_G(V)=k\cdot\operatorname{id}_V\).

In particular, if \(V\not\cong W\), then \(\operatorname{Hom}_G(V,W)=0\).

## Module interpretation

An intertwiner is equivalently a [[algebra-modules/module-homomorphism|module homomorphism]] of \(kG\)-modules, where \(kG\) is the [[algebra-representation-theory/group-algebra|group algebra]].

## Remarks

This result is frequently paired with character theory and the corollary that central elements act by scalars on irreducibles (see [[algebra-representation-theory/schur-corollary|Schur's corollary]]).

## Examples

### Example 1: Cyclic group \(C_n\) over \(\mathbb{C}\)
All irreducible \(\mathbb{C}\)-representations of \(C_n\) are 1-dimensional. If \(\chi,\psi\) are distinct 1-dimensional characters, then any \(C_n\)-equivariant map \(f:\mathbb{C}_\chi\to \mathbb{C}_\psi\) must be zero, because equivariance forces
\[
f(\chi(g)v)=\psi(g)f(v)
\]
for all \(g\), and choosing \(g\) with \(\chi(g)\neq \psi(g)\) implies \(f(v)=0\). If \(\chi=\psi\), then \(\mathrm{End}_{C_n}(\mathbb{C}_\chi)=\mathbb{C}\).

### Example 2: The standard 2D irreducible of \(S_3\)
Let \(V\) be the standard 2-dimensional [[algebra-representation-theory/irreducible-representation|irreducible representation]] of \(S_3\) (e.g. the reflection representation on the plane of an equilateral triangle). Schur’s lemma over \(\mathbb{C}\) says any \(S_3\)-equivariant \(T:V\to V\) must be of the form \(T=\lambda I\).
So the commutant \(\{T\in \mathrm{End}(V): T\rho(g)=\rho(g)T \ \forall g\}\) is exactly \(\mathbb{C}\cdot I\).

### Example 3: A real irreducible where \(\mathrm{End}_G(V)\neq \mathbb{R}\)
Let \(G=C_3=\langle r\rangle\) act on \(V=\mathbb{R}^2\) by rotation by \(120^\circ\). This is an irreducible real representation. The real matrices commuting with a \(120^\circ\) rotation are precisely the real linear combinations of \(I\) and that rotation (equivalently, they identify with \(\mathbb{C}\) acting on \(\mathbb{R}^2\cong \mathbb{C}\)). Thus
\[
\mathrm{End}_{C_3}(V)\cong \mathbb{C},
\]
illustrating the “division ring” conclusion over non-algebraically-closed fields.
