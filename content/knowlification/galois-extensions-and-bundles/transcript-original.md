# Galois Extensions and Bundles

## User

Let's see, doesn't an argument of Grothendieck's give that a Galois extension of fields is equivalent data to a principal Gal(K/F)-bundle?

## Assistant

Yes, with one important qualification: it is a principal bundle **in the étale topology**, not usually in the ordinary topology.

Let \(K/F\) be a finite Galois extension and let

\[
G=\operatorname{Gal}(K/F)=\operatorname{Aut}_F(K).
\]

Then the corresponding principal \(G\)-bundle is

\[
\operatorname{Spec} K \longrightarrow \operatorname{Spec} F.
\]

Here:

\[
P=\operatorname{Spec}K,\qquad M=\operatorname{Spec}F,\qquad G=\operatorname{Gal}(K/F).
\]

The group \(G\) acts on \(K\) by \(F\)-algebra automorphisms, hence contravariantly acts on \(\operatorname{Spec}K\) over \(\operatorname{Spec}F\). This makes

\[
\operatorname{Spec}K \to \operatorname{Spec}F
\]

a \(G\)-torsor, i.e. a principal \(G\)-bundle, in the étale site.

The key algebraic condition is the Galois identity

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

That is the torsor condition: over \(\operatorname{Spec}K\), the bundle trivializes into one copy of the fiber for each \(g\in G\).

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

determines a principal \(G\)-bundle

\[
\operatorname{Spec}K\to\operatorname{Spec}F
\]

in the étale topology.

Conversely, a connected finite étale \(G\)-torsor over \(\operatorname{Spec}F\) gives a finite Galois \(F\)-algebra. If the total space is connected, that algebra is a field extension \(K/F\).

## User

What is the etale topology? Also how do I type the accented e in macOS?

## Assistant

The **étale topology** is a Grothendieck topology on schemes. It is not usually a topology on the point-set \(|X|\). It is a rule for which morphisms into \(X\) count as “open covers.”

For a scheme \(X\), define the **small étale site** \(X_{\mathrm{\acute{e}t}}\) as follows.

Objects:

\[
U \to X
\]

where \(U\) is a scheme and \(U \to X\) is an étale morphism.

Morphisms:

\[
(V\to X)\to (U\to X)
\]

are \(X\)-morphisms \(V\to U\).

Covering families:

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

An étale morphism is a morphism of schemes that is:

\[
\text{locally of finite presentation}+\text{flat}+\text{unramified}.
\]

It is the algebraic-geometry analogue of a local diffeomorphism.

For fields, this becomes very concrete:

\[
\operatorname{Spec}K\to \operatorname{Spec}F
\]

is finite étale iff \(K/F\) is finite separable. Therefore a finite Galois extension \(K/F\) gives an étale cover

\[
\operatorname{Spec}K\to\operatorname{Spec}F.
\]

This is why the principal bundle statement is made in the étale topology. In the ordinary Zariski topology, \(\operatorname{Spec}F\) has only one point, so there are no nontrivial local covers that can trivialize \(\operatorname{Spec}K\to\operatorname{Spec}F\). The étale topology adds algebraic covers like finite separable extensions.

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

In the general definition, \(X\) is just an arbitrary scheme.

For your Galois-extension example, take

\[
X=\operatorname{Spec}F.
\]

Then the étale cover/principal bundle is

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

comes from the field inclusion

\[
F \hookrightarrow K
\]

by contravariance of \(\operatorname{Spec}\). In algebraic geometry, ring maps reverse direction:

\[
F \hookrightarrow K
\]

induces

\[
\operatorname{Spec}K \to \operatorname{Spec}F.
\]

The reason I introduced a general \(X\) was to define the étale topology on any scheme. For a general scheme \(X\), objects of \(X_{\acute{e}t}\) are étale maps

\[
U\to X.
\]

In the Galois case, the base scheme is specifically

\[
X=\operatorname{Spec}F,
\]

and one distinguished étale object over it is

\[
\operatorname{Spec}K\to\operatorname{Spec}F.
\]

If \(K/F\) is finite separable, this map is finite étale. If \(K/F\) is finite Galois with group \(G\), it is a principal \(G\)-bundle in the étale topology.

## User

axiomatically define scheme and give examples.

## Assistant

A **scheme** is a space locally modeled on commutative rings.

Fix \(\mathbf{CRing}\) = category of commutative unital rings.

## 1. Locally ringed space

A **locally ringed space** is a pair

\[
(X,\mathcal O_X)
\]

where:

**Topological space:** \(X\) is a topological space.

**Structure sheaf:** \(\mathcal O_X\) is a sheaf of commutative unital rings on \(X\).

**Local stalks:** For every \(x\in X\), the stalk

\[
\mathcal O_{X,x}
\]

is a local ring, i.e. it has a unique maximal ideal.

The sheaf \(\mathcal O_X\) is the “ring of functions” on \(X\), though its elements may be algebraic rather than ordinary functions.

## 2. Affine scheme

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

**Closed sets:** For each ideal \(I\subseteq A\),

\[
V(I)=\{\mathfrak p\in \operatorname{Spec}A : I\subseteq \mathfrak p\}.
\]

These define the Zariski topology.

**Basic open sets:** For \(f\in A\),

\[
D(f)=\{\mathfrak p\in \operatorname{Spec}A : f\notin \mathfrak p\}.
\]

**Structure sheaf:** Define

\[
\mathcal O_{\operatorname{Spec}A}(D(f))=A_f,
\]

where \(A_f\) is the localization of \(A\) obtained by inverting \(f\). These assignments glue to a sheaf \(\mathcal O_{\operatorname{Spec}A}\).

**Stalks:** At \(\mathfrak p\in \operatorname{Spec}A\),

\[
\mathcal O_{\operatorname{Spec}A,\mathfrak p}\cong A_{\mathfrak p}.
\]

Since \(A_{\mathfrak p}\) is local, \(\operatorname{Spec}A\) is a locally ringed space.

An **affine scheme** is a locally ringed space isomorphic to

\[
(\operatorname{Spec}A,\mathcal O_{\operatorname{Spec}A})
\]

for some \(A\in\mathbf{CRing}\).

## 3. Scheme

A **scheme** is a locally ringed space

\[
(X,\mathcal O_X)
\]

such that:

**Affine local cover:**

\[
X=\bigcup_{i\in I} U_i
\]

for open subsets \(U_i\subseteq X\), and for each \(i\), there exists a commutative unital ring \(A_i\) such that

\[
(U_i,\mathcal O_X|_{U_i})\cong \operatorname{Spec}A_i
\]

as locally ringed spaces.

So:

\[
\boxed{
\text{scheme}=\text{locally ringed space locally isomorphic to }\operatorname{Spec}A.
}
\]

## Examples

### 1. One-point scheme from a field

If \(F\) is a field, then

\[
\operatorname{Spec}F=\{(0)\}.
\]

It has one point, and its structure sheaf has stalk

\[
\mathcal O_{\operatorname{Spec}F,(0)}=F.
\]

This is the scheme appearing in the Galois-extension example:

\[
\operatorname{Spec}K\to\operatorname{Spec}F.
\]

### 2. The affine line over a field

For a field \(k\),

\[
\mathbb A^1_k := \operatorname{Spec} k[x].
\]

Its points are prime ideals of \(k[x]\). For example, if \(k\) is algebraically closed, the closed points are

\[
(x-a)
\]

for \(a\in k\), plus the generic point \((0)\).

### 3. Affine \(n\)-space

\[
\mathbb A^n_k := \operatorname{Spec} k[x_1,\dots,x_n].
\]

This is the scheme version of \(n\)-dimensional affine space over \(k\).

### 4. The integer scheme

\[
\operatorname{Spec}\mathbb Z.
\]

Its points are

\[
(0),\ (2),\ (3),\ (5),\ (7),\dots
\]

where \((p)\) ranges over prime ideals generated by rational primes \(p\).

The point \((0)\) is the generic point. The points \((p)\) are closed.

### 5. Projective space

Projective \(n\)-space over \(k\) is

\[
\mathbb P^n_k.
\]

It is not usually affine, but it is a scheme because it has an affine open cover

\[
\mathbb P^n_k=\bigcup_{i=0}^n U_i,
\]

with

\[
U_i\cong \mathbb A^n_k.
\]

So schemes include both affine objects like \(\operatorname{Spec}A\) and objects glued from affine pieces, like \(\mathbb P^n_k\).
