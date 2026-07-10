+++
id = "knowlification/galois-extensions-and-bundles-transcript"
title = "Galois Extensions and Bundles — knowlified transcript"
kind = "document"
summary = "A full conversation transcript with expandable definitions for its mathematical terminology."
aliases = ["Galois Extensions and Bundles transcript", "knowlified Galois conversation"]
domains = ["knowlification"]
+++

# Galois Extensions and Bundles

## User

Let's see, doesn't an argument of Grothendieck's give that a [[algebra-fields-galois/galois-extension|Galois extension]] of [[algebra-rings/field|fields]] is equivalent data to a [[algebraic-geometry-foundations/g-torsor-on-a-site|principal Gal(K/F)-bundle]]?

## Assistant

Yes, with one important qualification: it is a [[algebraic-geometry-foundations/g-torsor-on-a-site|principal bundle]] **in the [[algebraic-geometry-foundations/etale-topology|étale topology]]**, not usually in the [[algebra-commutative/zariski-topology|ordinary topology]].

Let \(K/F\) be a [[algebra-fields-galois/galois-extension|finite Galois extension]] and let

\[
G=\operatorname{Gal}(K/F)=\operatorname{Aut}_F(K).
\]

Then the corresponding [[algebraic-geometry-foundations/g-torsor-on-a-site|principal \(G\)-bundle]] is

\[
\operatorname{Spec} K \longrightarrow \operatorname{Spec} F.
\]

Here:

\[
P=\operatorname{Spec}K,\qquad M=\operatorname{Spec}F,\qquad G=\operatorname{Gal}(K/F).
\]

The [[algebra-groups/group|group]] \(G\) [[algebra-groups/group-action|acts]] on \(K\) by \(F\)-algebra [[algebra-fields-galois/field-automorphism|automorphisms]], hence [[algebra-category-theory/contravariant-functor|contravariantly]] [[algebra-groups/group-action|acts]] on \(\operatorname{Spec}K\) over \(\operatorname{Spec}F\). This makes

\[
\operatorname{Spec}K \to \operatorname{Spec}F
\]

a [[algebraic-geometry-foundations/g-torsor-on-a-site|\(G\)-torsor]], i.e. a [[algebraic-geometry-foundations/g-torsor-on-a-site|principal \(G\)-bundle]], in the [[algebraic-geometry-foundations/small-etale-site|étale site]].

The key algebraic condition is the [[algebraic-geometry-foundations/galois-tensor-product-identity|Galois identity]]

\[
K\otimes_F K \cong \prod_{\sigma\in G} K,
\]

given by

\[
a\otimes b \mapsto \big(a\,\sigma(b)\big)_{\sigma\in G}.
\]

Geometrically, this says

\[
\operatorname{Spec}K \times_{\operatorname{Spec}F} \operatorname{Spec}K
\cong
\operatorname{Spec}K \times G.
\]

That is the [[algebraic-geometry-foundations/torsor-condition|torsor condition]]: over \(\operatorname{Spec}K\), the bundle [[fiber-bundles/local-trivialization|trivializes]] into one copy of the [[fiber-bundles/fiber-of-a-map|fiber]] for each \(g\in G\).

So the slogan is:

\[
\boxed{\text{finite Galois extension } K/F
\quad\leftrightsquigarrow\quad
\text{connected finite étale } G\text{-torsor over } \operatorname{Spec}F.}
\]

But more precisely:

\[
K/F \text{ finite Galois with group }G
\]

determines a [[algebraic-geometry-foundations/g-torsor-on-a-site|principal \(G\)-bundle]]

\[
\operatorname{Spec}K\to\operatorname{Spec}F
\]

in the [[algebraic-geometry-foundations/etale-topology|étale topology]].

Conversely, a [[algebraic-geometry-foundations/connected-scheme|connected]] [[algebraic-geometry-foundations/finite-etale-morphism|finite étale]] [[algebraic-geometry-foundations/g-torsor-on-a-site|\(G\)-torsor]] over \(\operatorname{Spec}F\) gives a finite Galois \(F\)-algebra. If the [[algebraic-geometry-foundations/connected-scheme|total space]] is [[algebraic-geometry-foundations/connected-scheme|connected]], that [[algebra-modules/algebra-over-ring|algebra]] is a [[algebra-fields-galois/field-extension|field extension]] \(K/F\).

## User

What is the [[algebraic-geometry-foundations/etale-topology|etale topology]]? Also how do I type the accented e in macOS?

## Assistant

The **[[algebraic-geometry-foundations/etale-topology|étale topology]]** is a [[algebraic-geometry-foundations/grothendieck-topology|Grothendieck topology]] on [[algebraic-geometry-foundations/scheme|schemes]]. It is not usually a topology on the [[topology/topological-space|point-set]] \(|X|\). It is a rule for which [[algebra-category-theory/morphism|morphisms]] into \(X\) count as “[[topology/open-cover|open covers]].”

For a [[algebraic-geometry-foundations/scheme|scheme]] \(X\), define the **[[algebraic-geometry-foundations/small-etale-site|small étale site]]** \(X_{\mathrm{\acute{e}t}}\) as follows.

[[algebra-category-theory/object|Objects]]:

\[
U \to X
\]

where \(U\) is a [[algebraic-geometry-foundations/scheme|scheme]] and \(U \to X\) is an [[algebraic-geometry-foundations/etale-morphism|étale morphism]].

[[algebra-category-theory/morphism|Morphisms]]:

\[
(V\to X)\to (U\to X)
\]

are [[algebraic-geometry-foundations/morphism-of-schemes|\(X\)-morphisms]] \(V\to U\).

[[algebraic-geometry-foundations/covering-family|Covering families]]:

\[
\{U_i \to U\}_{i\in I}
\]

such that each \(U_i\to U\) is étale and

\[
\bigcup_i \operatorname{im}(U_i\to U)=U.
\]

So the slogan is:

\[
\boxed{\text{étale topology}=\text{topology where étale maps are allowed as local charts/covers}.}
\]

An [[algebraic-geometry-foundations/etale-morphism|étale morphism]] is a [[algebraic-geometry-foundations/morphism-of-schemes|morphism of schemes]] that is:

\[
\text{locally of finite presentation}+\text{flat}+\text{unramified}.
\]

It is the algebraic-geometry analogue of a [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphism]].

For [[algebra-rings/field|fields]], this becomes very concrete:

\[
\operatorname{Spec}K\to \operatorname{Spec}F
\]

is [[algebraic-geometry-foundations/finite-etale-morphism|finite étale]] iff \(K/F\) is finite separable. Therefore a [[algebra-fields-galois/galois-extension|finite Galois extension]] \(K/F\) gives an étale cover

\[
\operatorname{Spec}K\to\operatorname{Spec}F.
\]

This is why the [[algebraic-geometry-foundations/g-torsor-on-a-site|principal bundle]] statement is made in the [[algebraic-geometry-foundations/etale-topology|étale topology]]. In the ordinary [[algebra-commutative/zariski-topology|Zariski topology]], \(\operatorname{Spec}F\) has only one point, so there are no nontrivial [[topology/open-cover|local covers]] that can trivialize \(\operatorname{Spec}K\to\operatorname{Spec}F\). The [[algebraic-geometry-foundations/etale-topology|étale topology]] adds algebraic covers like [[algebra-fields-galois/separable-extension|finite separable extensions]].

For typing **é** on macOS:

\[
\text{Option} + e,\ \text{then } e
\]

So:

1. Press `Option` + `e`
2. Release
3. Press `e`

For uppercase:

\[
\text{Option}+e,\ \text{then Shift}+e
\]

giving **É**.

In LaTeX:

```latex
\'{e}tale
```

or directly:

```latex
étale
```

## User

Sorry what is X and how is it related to K and F?

## Assistant

In the general definition, \(X\) is just an arbitrary [[algebraic-geometry-foundations/scheme|scheme]].

For your [[algebra-fields-galois/galois-extension|Galois-extension]] example, take

\[
X=\operatorname{Spec}F.
\]

Then the étale cover/[[algebraic-geometry-foundations/g-torsor-on-a-site|principal bundle]] is

\[
\operatorname{Spec}K \longrightarrow \operatorname{Spec}F.
\]

So in this example:

\[
\boxed{
X=\operatorname{Spec}F,\qquad
P=\operatorname{Spec}K,\qquad
G=\operatorname{Gal}(K/F).
}
\]

The map

\[
\operatorname{Spec}K \to \operatorname{Spec}F
\]

comes from the [[algebra-rings/ring-homomorphism|field inclusion]]

\[
F \hookrightarrow K
\]

by [[algebra-category-theory/contravariant-functor|contravariance]] of \(\operatorname{Spec}\). In algebraic geometry, [[algebra-rings/ring-homomorphism|ring maps]] reverse direction:

\[
F \hookrightarrow K
\]

induces

\[
\operatorname{Spec}K \to \operatorname{Spec}F.
\]

The reason I introduced a general \(X\) was to define the [[algebraic-geometry-foundations/etale-topology|étale topology]] on any [[algebraic-geometry-foundations/scheme|scheme]]. For a general [[algebraic-geometry-foundations/scheme|scheme]] \(X\), [[algebra-category-theory/object|objects]] of \(X_{\acute{e}t}\) are [[algebraic-geometry-foundations/etale-morphism|étale maps]]

\[
U\to X.
\]

In the Galois case, the base [[algebraic-geometry-foundations/scheme|scheme]] is specifically

\[
X=\operatorname{Spec}F,
\]

and one distinguished étale [[algebra-category-theory/object|object]] over it is

\[
\operatorname{Spec}K\to\operatorname{Spec}F.
\]

If \(K/F\) is finite separable, this map is [[algebraic-geometry-foundations/finite-etale-morphism|finite étale]]. If \(K/F\) is finite Galois with [[algebra-groups/group|group]] \(G\), it is a [[algebraic-geometry-foundations/g-torsor-on-a-site|principal \(G\)-bundle]] in the [[algebraic-geometry-foundations/etale-topology|étale topology]].

## User

axiomatically define [[algebraic-geometry-foundations/scheme|scheme]] and give examples.

## Assistant

A **[[algebraic-geometry-foundations/scheme|scheme]]** is a space locally modeled on [[algebra-rings/commutative-ring|commutative rings]].

Fix \(\mathbf{CRing}\) = [[algebra-category-theory/category|category]] of [[algebra-rings/commutative-ring|commutative unital rings]].

## 1. [[algebraic-geometry-foundations/locally-ringed-space|Locally ringed space]]

A **[[algebraic-geometry-foundations/locally-ringed-space|locally ringed space]]** is a pair

\[
(X,\mathcal O_X)
\]

where:

**[[topology/topological-space|Topological space]]:** \(X\) is a [[topology/topological-space|topological space]].

**[[algebraic-geometry-foundations/structure-sheaf|Structure sheaf]]:** \(\mathcal O_X\) is a [[algebraic-geometry-foundations/sheaf|sheaf]] of [[algebra-rings/commutative-ring|commutative unital rings]] on \(X\).

**[[algebra-commutative/local-ring|Local]] [[algebraic-geometry-foundations/stalk|stalks]]:** For every \(x\in X\), the [[algebraic-geometry-foundations/stalk|stalk]]

\[
\mathcal O_{X,x}
\]

is a [[algebra-commutative/local-ring|local ring]], i.e. it has a unique [[algebra-rings/maximal-ideal|maximal ideal]].

The [[algebraic-geometry-foundations/sheaf|sheaf]] \(\mathcal O_X\) is the “[[algebraic-geometry-foundations/structure-sheaf|ring of functions]]” on \(X\), though its elements may be algebraic rather than ordinary [[shared-foundations/function|functions]].

## 2. [[algebraic-geometry-foundations/affine-scheme|Affine scheme]]

Given \(A\in \mathbf{CRing}\), define

\[
\operatorname{Spec} A
\]

as follows.

**Points:**

\[
|\operatorname{Spec} A|
=
\{\mathfrak p\subseteq A : \mathfrak p \text{ is a prime ideal}\}.
\]

**[[topology/closed-set|Closed sets]]:** For each [[algebra-rings/ideal|ideal]] \(I\subseteq A\),

\[
V(I)=\{\mathfrak p\in \operatorname{Spec}A : I\subseteq \mathfrak p\}.
\]

These define the [[algebra-commutative/zariski-topology|Zariski topology]].

**[[topology/open-set|Basic open sets]]:** For \(f\in A\),

\[
D(f)=\{\mathfrak p\in \operatorname{Spec}A : f\notin \mathfrak p\}.
\]

**[[algebraic-geometry-foundations/structure-sheaf|Structure sheaf]]:** Define

\[
\mathcal O_{\operatorname{Spec}A}(D(f))=A_f,
\]

where \(A_f\) is the [[algebra-commutative/localization-ring|localization]] of \(A\) obtained by inverting \(f\). These assignments glue to a [[algebraic-geometry-foundations/sheaf|sheaf]] \(\mathcal O_{\operatorname{Spec}A}\).

**[[algebraic-geometry-foundations/stalk|Stalks]]:** At \(\mathfrak p\in \operatorname{Spec}A\),

\[
\mathcal O_{\operatorname{Spec}A,\mathfrak p}\cong A_{\mathfrak p}.
\]

Since \(A_{\mathfrak p}\) is [[algebra-commutative/local-ring|local]], \(\operatorname{Spec}A\) is a [[algebraic-geometry-foundations/locally-ringed-space|locally ringed space]].

An **[[algebraic-geometry-foundations/affine-scheme|affine scheme]]** is a [[algebraic-geometry-foundations/locally-ringed-space|locally ringed space]] [[algebra-category-theory/isomorphism-category|isomorphic]] to

\[
(\operatorname{Spec}A,\mathcal O_{\operatorname{Spec}A})
\]

for some \(A\in\mathbf{CRing}\).

## 3. [[algebraic-geometry-foundations/scheme|Scheme]]

A **[[algebraic-geometry-foundations/scheme|scheme]]** is a [[algebraic-geometry-foundations/locally-ringed-space|locally ringed space]]

\[
(X,\mathcal O_X)
\]

such that:

**[[algebraic-geometry-foundations/affine-scheme|Affine]] [[algebra-commutative/local-ring|local]] cover:**

\[
X=\bigcup_{i\in I} U_i
\]

for [[topology/open-set|open subsets]] \(U_i\subseteq X\), and for each \(i\), there exists a [[algebra-rings/commutative-ring|commutative unital ring]] \(A_i\) such that

\[
(U_i,\mathcal O_X|_{U_i})\cong \operatorname{Spec}A_i
\]

as [[algebraic-geometry-foundations/locally-ringed-space|locally ringed spaces]].

So:

\[
\boxed{
\text{scheme}=\text{locally ringed space locally isomorphic to }\operatorname{Spec}A.
}
\]

## Examples

### 1. One-point [[algebraic-geometry-foundations/scheme|scheme]] from a [[algebra-rings/field|field]]

If \(F\) is a [[algebra-rings/field|field]], then

\[
\operatorname{Spec}F=\{(0)\}.
\]

It has one point, and its [[algebraic-geometry-foundations/structure-sheaf|structure sheaf]] has [[algebraic-geometry-foundations/stalk|stalk]]

\[
\mathcal O_{\operatorname{Spec}F,(0)}=F.
\]

This is the [[algebraic-geometry-foundations/scheme|scheme]] appearing in the [[algebra-fields-galois/galois-extension|Galois-extension]] example:

\[
\operatorname{Spec}K\to\operatorname{Spec}F.
\]

### 2. The [[algebraic-geometry-foundations/affine-line|affine line]] over a [[algebra-rings/field|field]]

For a [[algebra-rings/field|field]] \(k\),

\[
\mathbb A^1_k := \operatorname{Spec} k[x].
\]

Its points are [[algebra-rings/prime-ideal|prime ideals]] of \(k[x]\). For example, if \(k\) is [[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed]], the [[algebraic-geometry-foundations/closed-point|closed points]] are

\[
(x-a)
\]

for \(a\in k\), plus the [[algebraic-geometry-foundations/generic-point|generic point]] \((0)\).

### 3. [[algebraic-geometry-foundations/affine-n-space|Affine \(n\)-space]]

\[
\mathbb A^n_k := \operatorname{Spec} k[x_1,\dots,x_n].
\]

This is the [[algebraic-geometry-foundations/scheme|scheme]] version of \(n\)-dimensional [[algebraic-geometry-foundations/affine-scheme|affine]] space over \(k\).

### 4. The [[algebraic-geometry-foundations/scheme|integer scheme]]

\[
\operatorname{Spec}\mathbb Z.
\]

Its points are

\[
(0),\ (2),\ (3),\ (5),\ (7),\dots
\]

where \((p)\) ranges over [[algebra-rings/prime-ideal|prime ideals]] generated by rational primes \(p\).

The point \((0)\) is the [[algebraic-geometry-foundations/generic-point|generic point]]. The points \((p)\) are closed.

### 5. [[algebraic-geometry-foundations/projective-space|Projective space]]

[[algebraic-geometry-foundations/projective-space|Projective \(n\)-space]] over \(k\) is

\[
\mathbb P^n_k.
\]

It is not usually [[algebraic-geometry-foundations/affine-scheme|affine]], but it is a [[algebraic-geometry-foundations/scheme|scheme]] because it has an [[topology/open-cover|affine open cover]]

\[
\mathbb P^n_k=\bigcup_{i=0}^n U_i,
\]

with

\[
U_i\cong \mathbb A^n_k.
\]

So [[algebraic-geometry-foundations/scheme|schemes]] include both [[algebraic-geometry-foundations/affine-scheme|affine]] [[algebra-category-theory/object|objects]] like \(\operatorname{Spec}A\) and [[algebra-category-theory/object|objects]] glued from [[algebraic-geometry-foundations/affine-scheme|affine]] pieces, like \(\mathbb P^n_k\).
