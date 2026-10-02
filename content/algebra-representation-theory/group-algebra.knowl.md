+++
id = "algebra-representation-theory/group-algebra"
title = "Group algebra"
kind = "knowl"
summary = "The finite-support group ring R[G], called the group algebra when R is a field."
aliases = ["group-algebra", "Group algebra", "group ring", "integral group ring"]
domains = ["algebra-representation-theory"]
legacy_source_path = "algebra-representation-theory/group-algebra.md"
section_mode = "progressive"
prerequisites = ["algebra-groups/group", "algebra-rings/commutative-ring", "algebra-modules/free-module"]
dependency_heuristic = "transcript-connections-semantic-v1"
dependency_review_count = 2
+++

Let \(G\) be a [[algebra-groups/group|group]] and \(R\) a [[algebra-rings/commutative-ring|commutative ring]] with identity. The **group ring** \(R[G]\) is the [[algebra-modules/free-module|free \(R\)-module]] with basis \(\{\delta_g:g\in G\}\) and multiplication determined by
\[
\delta_g\cdot \delta_h = \delta_{gh}\quad (g,h\in G),
\]
extended \(R\)-bilinearly. Thus every element has a unique expression
\[
x=\sum_{g\in G} a_g\,\delta_g\qquad (a_g\in R),
\]
with only finitely many nonzero coefficients, and multiplication is
\[
\left(\sum_{g} a_g\delta_g\right)\left(\sum_{h} b_h\delta_h\right)=\sum_{g,h} a_g b_h\,\delta_{gh}.
\]
The identity is \(\delta_e\), where \(e\) is the identity of \(G\). When \(R=k\) is a field, \(k[G]\) is called the **group algebra** (also written \(kG\)). Neither construction requires \(G\) to be finite.

## Representations as modules

Over a field \(k\), a (finite-dimensional) [[algebra-representation-theory/group-representation|group representation]] \(\rho:G\to \mathrm{GL}(V)\) on a \(k\)-vector space \(V\) extends uniquely to a unital \(k\)-algebra homomorphism
\[
\widetilde{\rho}:k[G]\to \mathrm{End}_k(V),\qquad
\widetilde{\rho}\!\left(\sum_g a_g\delta_g\right)=\sum_g a_g\,\rho(g).
\]
Equivalently, giving a representation of \(G\) is the same as giving a unital left \(k[G]\)-module structure on \(V\) extending its scalar action. In this correspondence:
- [[algebra-representation-theory/subrepresentation|subrepresentations]] are exactly \(k[G]\)-submodules,
- [[algebra-representation-theory/irreducible-representation|irreducible representations]] are exactly [[algebra-modules/simple-module|simple modules]] over \(k[G]\),
- for finite \(G\), [[algebra-representation-theory/maschkes-theorem|Maschke’s theorem]] describes when \(k[G]\) is semisimple and its representations are completely reducible.

## Integral orders

For finite \(G\), \(\mathbb Z[G]\) is a [[algebra-rings/order-in-algebra|\(\mathbb Z\)-order]] in \(\mathbb Q[G]\): its basis has \(|G|\) elements, it spans \(\mathbb Q[G]\), and its multiplication has integer structure constants. For infinite \(G\), it is not a finite-rank order in this sense.

## Examples

### Example 1: Cyclic groups \(C_n\)
Let \(G=C_n=\langle t\mid t^n=e\rangle\). Then
\[
k[C_n]\cong k[t]/(t^n-1),
\]
via \(\delta_{t^m}\mapsto t^m\). This realizes \(k[C_n]\) as a commutative \(k\)-algebra.

### Example 2: The order-2 group \(C_2=\{e,s\}\)
Here \(k[C_2]=k\delta_e\oplus k\delta_s\) with \(\delta_s^2=\delta_e\). So
\[
k[C_2]\cong k[s]/(s^2-1).
\]
If \(\mathrm{char}(k)\neq 2\), the elements
\[
e_\pm=\tfrac12(\delta_e\pm \delta_s)
\]
satisfy \(e_\pm^2=e_\pm\) and \(e_+e_-=0\), giving a decomposition \(k[C_2]\cong k\times k\). (This is a concrete instance of semisimplicity in characteristic not dividing \(|G|\).)

### Example 3: \(S_3\) and class sums
For \(G=S_3\), \(k[S_3]\) is \(6\)-dimensional with basis \(\{\delta_\sigma:\sigma\in S_3\}\).
The center \(Z(k[S_3])\) is spanned by sums over [[algebra-groups/conjugacy-class|conjugacy classes]]:
\[
z_1=\delta_e,\qquad
z_2=\sum_{\text{transpositions }\tau}\delta_\tau,\qquad
z_3=\sum_{\text{3-cycles }\gamma}\delta_\gamma.
\]
Over an [[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed field]], these class sums act as scalars in any finite-dimensional irreducible representation (compare [[algebra-representation-theory/schurs-lemma|Schur’s lemma]]).
