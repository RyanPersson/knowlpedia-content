+++
id = "posts/riemannian-metrics-and-manifolds"
title = "Riemannian Metrics and Manifolds"
kind = "document"
summary = "Dependency-first lecture notes on smooth manifolds, fiber bundles, Lie groups, and Riemannian geometry."
aliases = ["Manifold lecture notes", "Riemannian Metrics and Manifolds lecture notes"]
domains = ["differential-geometry", "fiber-bundles", "lie-groups"]
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

These lecture notes are adapted from the supplied LaTeX manuscript. Existing Knowlpedia concepts open inline; terms awaiting dedicated knowls remain bold.

## Preface

The notes use finite-dimensional real manifolds.
A manifold is [[topology/hausdorff-space|Hausdorff]] and [[fiber-bundles/convention-manifolds-are-smooth-hausdorff-and-second-countable|second countable]] unless a statement gives different assumptions.
The word smooth means $C^\infty$.
All [[linear-algebra/vector-space|vector spaces]] are real and finite-dimensional unless a statement gives a different [[algebra-rings/field|field]] or dimension.

Several major theorems from analysis and [[topology/topology|topology]] occur as input.
The notes state each input with its assumptions.
Appendix A gives a dependency list.
The text proves many structural results.
It does not reproduce full proofs of the [[shared-foundations/inverse-function|inverse function]] theorem, the existence theorem for ordinary differential equations, the paracompactness theorem, or the [[lie-groups/closed-subgroup-theorem|closed subgroup theorem]].

### How to use the notes

Read Chapters 1--3 before Chapter 4 if the prerequisite concepts are new.
A reader with a course in analysis and [[topology/topology|topology]] can start at Chapter 4.
Chapters 9--12 give the bundle and [[fiber-bundles/lie-group|Lie group]] material.
Chapters 13--19 give Riemannian geometry.

Each chapter starts with required concepts.
Each definition fixes notation.
Each theorem states its assumptions.
Exercises test the dependency chain.
Appendix C gives selected solutions.

## Axiomatic base and dependency map

### Axiomatic base

The text uses classical first-order logic and a standard [[shared-foundations/set|set]] theory such as ZFC.
The [[shared-foundations/axiom-of-choice|Axiom of Choice]] is available.
The text uses $\mathbb{R}$ as a complete ordered [[algebra-rings/field|field]].
It uses finite-dimensional linear algebra over $\mathbb{R}$.

The construction of $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, and $\mathbb{R}$ from [[shared-foundations/set|set]] theory is not part of the notes.
Their algebraic and order properties are part of the base.
The [[real-analysis/completeness-axiom|completeness axiom]] for $\mathbb{R}$ states that each nonempty [[shared-foundations/set|set]] that has an [[shared-foundations/upper-bound|upper bound]] has a least [[shared-foundations/upper-bound|upper bound]].

### Main dependency chain

| Layer | Required output |
| --- | --- |
| [[shared-foundations/set|Sets]] and maps | Products, quotients, [[shared-foundations/function|functions]], and [[shared-foundations/equivalence-relation|equivalence relations]]. |
| Algebra | [[algebra-groups/group|Groups]], actions, [[linear-algebra/vector-space|vector spaces]], dual spaces, and [[linear-algebra/inner-product|inner products]]. |
| Euclidean calculus | [[real-analysis/derivative|Derivatives]], [[fiber-bundles/smooth-map|smooth maps]], [[linear-algebra/rank|rank]], and local normal forms. |
| [[topology/topology|Topology]] | Continuity, compactness, [[topology/quotient-topology|quotient topology]], and manifold hypotheses. |
| [[fiber-bundles/smooth-manifold|Smooth manifolds]] | Charts, atlases, [[fiber-bundles/smooth-map|smooth maps]], and [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partitions of unity]]. |
| Tangent geometry | [[differential-geometry/tangent-space|Tangent spaces]], differentials, [[fiber-bundles/vector-field|vector fields]], and tensors. |
| Bundles | [[fiber-bundles/tangent-bundle|Tangent bundles]], [[fiber-bundles/vector-bundle|vector bundles]], principal bundles, and [[fiber-bundles/associated-bundle|associated bundles]]. |
| Lie theory | [[fiber-bundles/lie-group|Lie groups]], [[lie-groups/lie-algebra|Lie algebras]], actions, and [[lie-groups/homogeneous-space|homogeneous spaces]]. |
| Riemannian geometry | [[topology/metric|Metrics]], [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]], geodesics, and [[fiber-bundles/curvature|curvature]]. |

The following arrows record major uses:
\[
\begin{aligned}
\text{complete ordered field} &\longrightarrow \text{Euclidean analysis},\\
\text{Euclidean analysis + topology} &\longrightarrow \text{smooth manifolds},\\
\text{smooth manifolds + linear algebra} &\longrightarrow \text{tangent and tensor bundles},\\
\text{group theory + smooth manifolds} &\longrightarrow \text{Lie groups},\\
\text{Lie groups + bundles} &\longrightarrow \text{principal and associated bundles},\\
\text{partition of unity + tangent bundle} &\longrightarrow \text{Riemannian metrics},\\
\text{Riemannian metric + connection theory} &\longrightarrow \text{Levi-Civita connection},\\
\text{Levi-Civita connection + ODE theory} &\longrightarrow \text{geodesics and curvature}.
\end{aligned}
\]

### The manifold--Lie group relations

The notes develop the following [[shared-foundations/relation|relations]].

1. A [[fiber-bundles/lie-group|Lie group]] is a [[fiber-bundles/smooth-manifold|smooth manifold]] with smooth [[algebra-groups/group|group]] operations.
1. A [[lie-groups/lie-algebra|Lie algebra]] is the [[differential-geometry/tangent-space|tangent space]] of a [[fiber-bundles/lie-group|Lie group]] at its identity, with an additional bracket.
1. A [[fiber-bundles/lie-group|Lie group]] action describes smooth symmetry of a manifold.
1. A [[algebra-groups/transitive-action|transitive action]] writes a homogeneous manifold as a quotient $G/H$.
1. A principal $G$-bundle has a free and transitive $G$-action on each fiber.
1. The frame bundle of an $n$-manifold is a principal $\operatorname{GL}(n,\mathbb{R})$-bundle.
1. A [[differential-geometry/riemannian-manifold|Riemannian metric]] reduces the frame bundle from $\operatorname{GL}(n,\mathbb{R})$ to $\mathrm O(n)$.
1. A [[fiber-bundles/principal-connection|principal connection]] gives covariant [[real-analysis/derivative|derivatives]] on [[fiber-bundles/associated-vector-bundle|associated vector bundles]].
1. Every [[fiber-bundles/lie-group|Lie group]] has left-invariant [[differential-geometry/riemannian-manifold|Riemannian metrics]].
1. The [[topology/isometry|isometry]] [[algebra-groups/group|group]] of a connected [[differential-geometry/riemannian-manifold|Riemannian manifold]] is a [[fiber-bundles/lie-group|Lie group]].


# Part: Foundations
## Sets, maps, and algebraic structures

**Required concepts.** Classical logic and the usual number systems.
**Result of this chapter.** The reader can use products, quotients, [[algebra-groups/group|groups]], [[algebra-groups/group-action|group actions]], [[linear-algebra/vector-space|vector spaces]], dual spaces, and [[linear-algebra/inner-product|inner products]].

### Sets and subsets

A [[shared-foundations/set|set]] is an object in the set-theoretic base.
The notation $x\in A$ means that $x$ is an element of $A$.
The notation $A\subseteq B$ means that each element of $A$ is an element of $B$.

The [[shared-foundations/empty-set|empty set]] is $\varnothing$.
The [[shared-foundations/union|union]] and [[shared-foundations/intersection|intersection]] of [[shared-foundations/set|sets]] $A$ and $B$ are
\[
A\cup B=\left\{x:x\in A\text{ or }x\in B\right\},
\qquad
A\cap B=\left\{x:x\in A\text{ and }x\in B\right\}.
\]
If $A\subseteq X$, then the [[shared-foundations/complement|complement]] of $A$ in $X$ is $X\setminus A$.
The [[shared-foundations/cartesian-product|Cartesian product]] of $A$ and $B$ is
\[
A\times B=\left\{(a,b):a\in A,\ b\in B\right\}.
\]
For [[shared-foundations/set|sets]] $A_1,\ldots,A_k$, the product $\prod_{i=1}^{k}A_i$ is the [[shared-foundations/set|set]] of ordered $k$-tuples.
A product over an arbitrary index [[shared-foundations/set|set]] $I$ is the [[shared-foundations/set|set]] of all [[shared-foundations/function|functions]]
\[
x:I\to\bigcup_{i\in I}A_i
\]
such that $x(i)\in A_i$ for each $i\in I$.

### Maps

**Definition.**
A [[shared-foundations/function|map]] $f:A\to B$ assigns one element $f(a)\in B$ to each $a\in A$.
The [[shared-foundations/set|set]] $A$ is the [[shared-foundations/domain|domain]].
The [[shared-foundations/set|set]] $B$ is the [[shared-foundations/codomain|codomain]].

For $S\subseteq A$, the [[shared-foundations/image|image]] is
\[
f(S)=\left\{f(s):s\in S\right\}.
\]
For $T\subseteq B$, the inverse [[shared-foundations/image|image]] is
\[
f^{-1}(T)=\left\{a\in A:f(a)\in T\right\}.
\]
The inverse-image notation does not require an inverse map.

A map is [[shared-foundations/injective-function|injective]] if $f(a_1)=f(a_2)$ implies $a_1=a_2$.
A map is [[shared-foundations/surjective-function|surjective]] if $f(A)=B$.
A map is [[shared-foundations/bijective-function|bijective]] if it is [[shared-foundations/injective-function|injective]] and [[shared-foundations/surjective-function|surjective]].

If $f:A\to B$ and $g:B\to C$, then the composite is
\[
g\circ f:A\to C,
\qquad
(g\circ f)(a)=g(f(a)).
\]
The identity map on $A$ is $\operatorname{id}_A(a)=a$.

**Proposition.**
A map $f:A\to B$ has an inverse map $f^{-1}:B\to A$ if and only if $f$ is [[shared-foundations/bijective-function|bijective]].

*Proof.*
Suppose that $f^{-1}$ exists.
The identity $f^{-1}\circ f=\operatorname{id}_A$ gives injectivity.
The identity $f\circ f^{-1}=\operatorname{id}_B$ gives surjectivity.

Suppose that $f$ is [[shared-foundations/bijective-function|bijective]].
Each $b\in B$ has a unique $a\in A$ such that $f(a)=b$.
Define $f^{-1}(b)=a$.
The two inverse identities follow from this definition.
 \(\square\)

### Relations and quotients

**Definition.**
A [[shared-foundations/relation|relation]] on a [[shared-foundations/set|set]] $A$ is a [[shared-foundations/subset|subset]] of $A\times A$.
The notation $a\sim b$ means that $(a,b)$ belongs to the [[shared-foundations/relation|relation]].

**Definition.**
An [[shared-foundations/equivalence-relation|equivalence relation]] is a [[shared-foundations/relation|relation]] that has these properties:

1. Reflexivity: $a\sim a$.
1. Symmetry: $a\sim b$ implies $b\sim a$.
1. Transitivity: $a\sim b$ and $b\sim c$ imply $a\sim c$.

The [[shared-foundations/equivalence-class|equivalence class]] of $a$ is
\[
[a]=\left\{b\in A:b\sim a\right\}.
\]
The [[shared-foundations/quotient-set|quotient set]] is
\[
A/{\sim}=\left\{[a]:a\in A\right\}.
\]
The quotient map is
\[
q:A\to A/{\sim},
\qquad
q(a)=[a].
\]

**Proposition (Universal property of a quotient set).**
Let $q:A\to A/{\sim}$ be a quotient map.
Let $f:A\to B$ be constant on each [[shared-foundations/equivalence-class|equivalence class]].
Then there is a unique map
\[
\overline f:A/{\sim}\to B
\]
such that $f=\overline f\circ q$.

*Proof.*
Define $\overline f([a])=f(a)$.
The class condition makes this definition independent of the representative.
The identity $f=\overline f\circ q$ follows from the definition.
Surjectivity of $q$ gives uniqueness.
 \(\square\)

This universal property occurs in [[topology/quotient-topology|quotient topology]], quotient [[linear-algebra/vector-space|vector spaces]], [[algebra-groups/quotient-group|quotient groups]], and [[lie-groups/homogeneous-space|homogeneous spaces]].

### Categories and commutative diagrams

A small amount of [[algebra-category-theory/category|category]] language reduces repetition.

**Definition.**
A [[algebra-category-theory/category|category]] has [[algebra-category-theory/object|objects]], [[algebra-category-theory/morphism|morphisms]] between [[algebra-category-theory/object|objects]], associative [[shared-foundations/composition|composition]], and an [[algebra-category-theory/identity-morphism|identity morphism]] for each [[algebra-category-theory/object|object]].

The [[algebra-category-theory/category|category]] $\mathbf{Set}$ has [[shared-foundations/set|sets]] as [[algebra-category-theory/object|objects]] and maps as [[algebra-category-theory/morphism|morphisms]].
The [[algebra-category-theory/category|category]] $\mathbf{Vect}_{\mathbb{R}}$ has real [[linear-algebra/vector-space|vector spaces]] as [[algebra-category-theory/object|objects]] and [[linear-algebra/linear-map|linear maps]] as [[algebra-category-theory/morphism|morphisms]].
Later, the [[algebra-category-theory/category|category]] $\mathbf{Man}$ has [[fiber-bundles/smooth-manifold|smooth manifolds]] as [[algebra-category-theory/object|objects]] and [[fiber-bundles/smooth-map|smooth maps]] as [[algebra-category-theory/morphism|morphisms]].

A diagram commutes when all directed composites with the same start and end are equal.
For example, the equation $f=\overline f\circ q$ means that
\[
\begin{array}{ccc}
A&\xrightarrow{f}&B\\
\downarrow q&&\nearrow\overline f\\
A/{\sim}&&
\end{array}
\]
commutes.

### Groups and actions

**Definition.**
A [[algebra-groups/group|group]] is a [[shared-foundations/set|set]] $G$ with a map
\[
m:G\times G\to G,
\qquad
m(g,h)=gh,
\]
and an element $e\in G$.
The following axioms hold:

1. $(gh)k=g(hk)$ for all $g,h,k\in G$.
1. $eg=ge=g$ for all $g\in G$.
1. For each $g\in G$, there is $g^{-1}\in G$ such that $gg^{-1}=g^{-1}g=e$.

A [[algebra-groups/group|group]] is abelian if $gh=hg$ for all $g,h\in G$.
A [[shared-foundations/subset|subset]] $H\subseteq G$ is a [[algebra-groups/subgroup|subgroup]] if $e\in H$, if $h_1h_2\in H$, and if $h^{-1}\in H$ for all $h,h_1,h_2\in H$.

A map $\varphi:G\to K$ is a [[algebra-groups/group-homomorphism|group homomorphism]] if
\[
\varphi(gh)=\varphi(g)\varphi(h).
\]
Its kernel and [[shared-foundations/image|image]] are
\[
\operatorname{ker}\varphi=\left\{g\in G:\varphi(g)=e_K\right\},
\qquad
\operatorname{im}\varphi=\left\{\varphi(g):g\in G\right\}.
\]

A [[algebra-groups/subgroup|subgroup]] $N\subseteq G$ is normal if $gNg^{-1}=N$ for each $g\in G$.
If $N$ is normal, then the [[shared-foundations/quotient-set|quotient set]] $G/N$ has a [[algebra-groups/group|group]] structure.
The product is
\[
(gN)(hN)=(gh)N.
\]
Normality makes this product independent of the representatives.

**Definition.**
A [[algebra-groups/group-action|left action]] of a [[algebra-groups/group|group]] $G$ on a [[shared-foundations/set|set]] $X$ is a map
\[
G\times X\to X,
\qquad
(g,x)\mapsto g\cdot x,
\]
that satisfies
\[
e\cdot x=x,
\qquad
(gh)\cdot x=g\cdot(h\cdot x).
\]

The [[algebra-groups/orbit|orbit]] of $x$ is
\[
G\cdot x=\left\{g\cdot x:g\in G\right\}.
\]
The [[algebra-groups/stabilizer|stabilizer]] of $x$ is
\[
G_x=\left\{g\in G:g\cdot x=x\right\}.
\]
The action is transitive if it has one [[algebra-groups/orbit|orbit]].
The action is free if $G_x=\left\{e\right\}$ for all $x$.

**Example.**
The [[algebra-groups/group|group]] $\operatorname{GL}(n,\mathbb{R})$ acts on $\mathbb{R}^n$ by [[linear-algebra/matrix|matrix]] multiplication.
The action is not transitive because $0$ is a [[real-analysis/fixed-point|fixed point]].
The action is transitive on $\mathbb{R}^n\setminus\left\{0\right\}$.
An invertible [[linear-algebra/linear-map|linear map]] can send any nonzero vector to any other nonzero vector.

**Warning.**
A [[algebra-groups/transitive-action|transitive action]] does not make $X$ a [[algebra-groups/group|group]].
A quotient $G/H$ is a [[algebra-groups/group|group]] only when $H$ is normal.
A [[lie-groups/homogeneous-space|homogeneous space]] $G/H$ can exist when $H$ is not normal.

### Fields and vector spaces

A [[algebra-rings/field|field]] is a [[algebra-rings/commutative-ring|commutative ring]] in which each nonzero element has a multiplicative inverse.
The main [[algebra-rings/field|fields]] in these notes are $\mathbb{R}$ and $\mathbb{C}$.

**Definition.**
A [[linear-algebra/vector-space|vector space]] over a [[algebra-rings/field|field]] $F$ is an [[algebra-groups/abelian-group|abelian group]] $(V,+)$ with scalar multiplication $F\times V\to V$.
The scalar multiplication satisfies the distributive and associative axioms and the identity axiom $1v=v$.

A finite list $(v_1,\ldots,v_k)$ is linearly independent if
\[
a_1v_1+\cdots+a_kv_k=0
\]
implies $a_1=\cdots=a_k=0$.
The [[convex-analysis/subspace-generated-by-a-set-span|span]] is
\[
\operatorname{span}(v_1,\ldots,v_k)
=
\left\{a_1v_1+\cdots+a_kv_k:a_i\in F\right\}.
\]
A basis is a linearly independent spanning list.
The number of vectors in a basis is the dimension.

A map $L:V\to W$ is linear if
\[
L(av+bw)=aL(v)+bL(w).
\]
The kernel and [[shared-foundations/image|image]] are subspaces.
The [[linear-algebra/rank|rank]] is $\operatorname{rank} L=\dim(\operatorname{im} L)$.
The nullity is $\dim(\operatorname{ker} L)$.

**Theorem (Rank--nullity theorem).**
Let $L:V\to W$ be linear.
Suppose that $V$ is finite-dimensional.
Then
\[
\dim V=\operatorname{rank} L+\dim(\operatorname{ker} L).
\]

*Proof.*
Choose a basis $(v_1,\ldots,v_k)$ of $\operatorname{ker} L$.
Extend this list to a basis
\[
(v_1,\ldots,v_k,v_{k+1},\ldots,v_n)
\]
of $V$.
Then
\[
(L(v_{k+1}),\ldots,L(v_n))
\]
is a basis of $\operatorname{im} L$.
Thus $\operatorname{rank} L=n-k$.
 \(\square\)

The dual space is
\[
V^*=\operatorname{Hom}(V,F).
\]
For a basis $(e_1,\ldots,e_n)$, the dual basis $(e^1,\ldots,e^n)$ satisfies $e^i(e_j)=\delta^i_j$.
If $L:V\to W$ is linear, then its dual map is
\[
L^*:W^*\to V^*,
\qquad
L^*(\lambda)=\lambda\circ L.
\]
The direction reverses.

### Inner products and orthogonality

**Definition.**
An [[linear-algebra/inner-product|inner product]] on a real [[linear-algebra/vector-space|vector space]] $V$ is a map
\[
\left\langle \cdot,\cdot\right\rangle:V\times V\to\mathbb{R}
\]
with these properties:

1. It is linear in each variable.
1. $\left\langle v,w\right\rangle=\left\langle w,v\right\rangle$.
1. $\left\langle v,v\right\rangle>0$ for each $v\neq0$.

The [[linear-algebra/norm|norm]] is $\left\lVert v\right\rVert=\sqrt{\left\langle v,v\right\rangle}$.
Vectors $v$ and $w$ are orthogonal if $\left\langle v,w\right\rangle=0$.

**Theorem (Cauchy--Schwarz inequality).**
For all $v,w\in V$,
\[
\left|\left\langle v,w\right\rangle\right|\leq\left\lVert v\right\rVert\left\lVert w\right\rVert.
\]
Equality holds if and only if $v$ and $w$ are linearly dependent.

*Proof.*
The result is immediate when $w=0$.
Suppose that $w\neq0$.
For $t\in\mathbb{R}$,
\[
0\leq\left\lVert v-tw\right\rVert^2
=
\left\lVert v\right\rVert^2-2t\left\langle v,w\right\rangle+t^2\left\lVert w\right\rVert^2.
\]
[[shared-foundations/set|Set]] $t=\left\langle v,w\right\rangle/\left\lVert w\right\rVert^2$.
The inequality follows.
Equality holds exactly when $v-tw=0$.
 \(\square\)

An ordered basis is orthonormal if $\left\langle e_i,e_j\right\rangle=\delta_{ij}$.
The Gram--Schmidt process changes any basis into an [[linear-algebra/orthonormal-basis|orthonormal basis]].
An [[linear-algebra/inner-product|inner product]] gives a linear [[algebra-category-theory/isomorphism-category|isomorphism]]
\[
\flat:V\to V^*,
\qquad
v^\flat(w)=\left\langle v,w\right\rangle.
\]
Its inverse is denoted by $\sharp:V^*\to V$.
[[differential-geometry/riemannian-manifold|Riemannian metrics]] apply these maps at each [[differential-geometry/tangent-space|tangent space]].

### Direct sums and tensor products

The direct sum of [[linear-algebra/vector-space|vector spaces]] $V$ and $W$ is $V\oplus W=V\times W$ with componentwise operations.

**Definition.**
A [[algebra-modules/tensor-product|tensor product]] of $V$ and $W$ is a [[linear-algebra/vector-space|vector space]] $V\otimes W$ with a [[algebra-modules/bilinear-map|bilinear map]]
\[
\otimes:V\times W\to V\otimes W
\]
that has this universal property:
for each [[algebra-modules/bilinear-map|bilinear map]] $b:V\times W\to U$, there is a unique [[linear-algebra/linear-map|linear map]]
\[
\widetilde b:V\otimes W\to U
\]
such that $b=\widetilde b\circ\otimes$.

For finite-dimensional spaces, a basis $(e_i)$ of $V$ and a basis $(f_j)$ of $W$ give a basis $(e_i\otimes f_j)$ of $V\otimes W$.
Thus
\[
\dim(V\otimes W)=\dim V\dim W.
\]
The universal property is more important than a coordinate construction.
It determines the tensor product up to unique [[algebra-category-theory/isomorphism-category|isomorphism]].

### Exercises

**Exercise.**
Let $f:A\to B$ and $g:B\to C$.
Prove that $g\circ f$ is [[shared-foundations/injective-function|injective]] only if $f$ is [[shared-foundations/injective-function|injective]].
Prove that $g\circ f$ is [[shared-foundations/surjective-function|surjective]] only if $g$ is [[shared-foundations/surjective-function|surjective]].

**Exercise.**
Let a [[algebra-groups/group|group]] $G$ act on a [[shared-foundations/set|set]] $X$.
Prove that the [[shared-foundations/relation|relation]]
\[
x\sim y
\quad\Longleftrightarrow\quad
y=g\cdot x\text{ for some }g\in G
\]
is an [[shared-foundations/equivalence-relation|equivalence relation]].
Its quotient is the [[lie-groups/orbit-space|orbit space]] $X/G$.

**Exercise.**
Let $H\subseteq G$ be a [[algebra-groups/subgroup|subgroup]].
Let $G$ act on the [[shared-foundations/set|set]] of left [[algebra-groups/coset|cosets]] $G/H$ by
\[
g\cdot(kH)=(gk)H.
\]
Prove that the action is transitive.
Prove that the [[algebra-groups/stabilizer|stabilizer]] of $eH$ is $H$.

**Exercise.**
Let $V$ be finite-dimensional.
Define $\iota:V\to V^{**}$ by $\iota(v)(\lambda)=\lambda(v)$.
Prove that $\iota$ is a linear [[algebra-category-theory/isomorphism-category|isomorphism]].

**Exercise.**
Let $L:V\to W$ be linear.
Prove that $\operatorname{ker} L^*$ is the annihilator of $\operatorname{im} L$.
Deduce that $\operatorname{rank} L^*=\operatorname{rank} L$.

 ## Euclidean calculus

**Required concepts.** Finite-dimensional real [[linear-algebra/vector-space|vector spaces]], [[linear-algebra/norm|norms]], [[linear-algebra/linear-map|linear maps]], and completeness of $\mathbb{R}$.
**Result of this chapter.** The reader can define [[fiber-bundles/smooth-map|smooth maps]] on Euclidean open [[shared-foundations/set|sets]] and can use the inverse, implicit, constant-rank, and ODE theorems.

### Euclidean space

The [[linear-algebra/vector-space|vector space]] $\mathbb{R}^n$ has the standard [[linear-algebra/inner-product|inner product]]
\[
\left\langle x,y\right\rangle=\sum_{i=1}^{n}x^iy^i.
\]
Its [[linear-algebra/norm|norm]] is $\left\lVert x\right\rVert=\sqrt{\left\langle x,x\right\rangle}$. The [[topology/open-ball|open ball]] with center $a$ and radius $r>0$ is
\[
B_r(a)=\left\{x\in\mathbb{R}^n:\left\lVert x-a\right\rVert<r\right\}.
\]

**Definition.**
A [[shared-foundations/subset|subset]] $U\subseteq\mathbb{R}^n$ is [[topology/open-set|open]] if each $a\in U$ has $r>0$ such that $B_r(a)\subseteq U$.

A [[shared-foundations/sequence|sequence]] $(x_k)$ converges to $x$ if $\left\lVert x_k-x\right\rVert\to 0$. A map $f:U\to\mathbb{R}^m$ is continuous at $a$ if $f(x_k)\to f(a)$ for each [[shared-foundations/sequence|sequence]] $x_k\to a$ in $U$.

All [[linear-algebra/norm|norms]] on a finite-dimensional [[linear-algebra/vector-space|vector space]] give the same open [[shared-foundations/set|sets]]. Thus differentiability does not depend on the selected [[linear-algebra/norm|norm]].

### The Fréchet derivative

**Definition.**
Let $U\subseteq\mathbb{R}^n$ be open. Let $f:U\to\mathbb{R}^m$. The map $f$ is [[real-analysis/differentiable-map|differentiable at $a\in U$]] if there is a [[linear-algebra/linear-map|linear map]] $Df(a):\mathbb{R}^n\to\mathbb{R}^m$ such that
\[
\lim_{h\to 0}
\frac{\left\lVert f(a+h)-f(a)-Df(a)h\right\rVert}{\left\lVert h\right\rVert}=0.
\]
The map $Df(a)$ is the [[real-analysis/derivative|derivative]] of $f$ at $a$.

The definition says that the affine map
\[
h\mapsto f(a)+Df(a)h
\]
approximates $f(a+h)$ with an error of order $o(\left\lVert h\right\rVert)$.

**Proposition.**
The [[real-analysis/derivative|derivative]] is unique.

*Proof.*
Suppose that [[linear-algebra/linear-map|linear maps]] $A$ and $B$ satisfy the [[real-analysis/derivative|derivative]] condition. Fix $v\in\mathbb{R}^n$. [[shared-foundations/set|Set]] $h=tv$ with $t\neq 0$. Then
\[
\left\lVert (A-B)v\right\rVert
\leq
\frac{\left\lVert f(a+tv)-f(a)-Atv\right\rVert}{\left|t\right|}
+
\frac{\left\lVert f(a+tv)-f(a)-Btv\right\rVert}{\left|t\right|}.
\]
Both terms tend to zero as $t\to 0$. Thus $(A-B)v=0$. This holds for each $v$.
 \(\square\)

**Proposition.**
Differentiability at $a$ implies continuity at $a$.

*Proof.*
Write
\[
f(a+h)-f(a)=Df(a)h+r(h),
\qquad
\frac{\left\lVert r(h)\right\rVert}{\left\lVert h\right\rVert}\to 0.
\]
A [[linear-algebra/linear-map|linear map]] on a finite-dimensional normed space is bounded. Thus $\left\lVert Df(a)h\right\rVert\leq C\left\lVert h\right\rVert$ for some $C$. Both terms tend to zero with $h$.
 \(\square\)

### Partial derivatives and Jacobian matrices

Let $e_i$ be the $i$th standard basis vector. The [[real-analysis/partial-derivative|partial derivative]] of $f$ with respect to $x^i$ is
\[
\frac{\partial f}{\partial x^i}(a)
=
\lim_{t\to 0}\frac{f(a+te_i)-f(a)}{t},
\]
when the limit exists. If $f=(f^1,\ldots,f^m)$ is differentiable, then the [[linear-algebra/matrix|matrix]] of $Df(a)$ is the [[real-analysis/jacobian-matrix|Jacobian matrix]]
\[
J_f(a)=
\left(\frac{\partial f^{\alpha}}{\partial x^i}(a)\right)_{
1\leq \alpha\leq m,\ 1\leq i\leq n}.
\]

Existence of all [[real-analysis/partial-derivative|partial derivatives]] does not imply differentiability. Continuous [[real-analysis/partial-derivative|partial derivatives]] on a [[topology/neighborhood|neighborhood]] do imply differentiability.

**Theorem.**
Let $f:U\to\mathbb{R}^m$. Suppose that all first [[real-analysis/partial-derivative|partial derivatives]] exist and are continuous on $U$. Then $f$ is differentiable on $U$.

The proof uses the one-variable [[real-analysis/mean-value-theorem|mean value theorem]] on coordinate line segments.

### Chain rule

**Theorem (Chain rule).**
Let $U\subseteq\mathbb{R}^n$ and $V\subseteq\mathbb{R}^m$ be open. Let $f:U\to V$ be differentiable at $a$. Let $g:V\to\mathbb{R}^k$ be differentiable at $f(a)$. Then $g\circ f$ is differentiable at $a$, and
\[
D(g\circ f)(a)=Dg(f(a))\circ Df(a).
\]

*Proof.*
Write
\[
f(a+h)=f(a)+Ah+r(h),
\qquad
\frac{\left\lVert r(h)\right\rVert}{\left\lVert h\right\rVert}\to 0,
\]
where $A=Df(a)$. Write
\[
g(f(a)+u)=g(f(a))+Bu+s(u),
\qquad
\frac{\left\lVert s(u)\right\rVert}{\left\lVert u\right\rVert}\to 0,
\]
where $B=Dg(f(a))$. [[shared-foundations/set|Set]] $u=Ah+r(h)$. Then
\[
(g\circ f)(a+h)-(g\circ f)(a)-BAh
=Br(h)+s(Ah+r(h)).
\]
The first term is $o(\left\lVert h\right\rVert)$. The second term is also $o(\left\lVert h\right\rVert)$ because $\left\lVert Ah+r(h)\right\rVert=O(\left\lVert h\right\rVert)$. Thus the [[real-analysis/derivative|derivative]] is $BA$.
 \(\square\)

### Higher derivatives and smooth maps

A map $f:U\to\mathbb{R}^m$ is of class $C^1$ if $Df:U\to\operatorname{Hom}(\mathbb{R}^n,\mathbb{R}^m)$ is continuous. Inductively, $f$ is of class $C^k$ if its [[real-analysis/derivative|derivatives]] through order $k$ exist and are continuous. A map is [[fiber-bundles/smooth-map|smooth]] if it is of class $C^k$ for every $k\geq 1$.

For a scalar map $f:U\to\mathbb{R}$, the second [[real-analysis/derivative|derivative]] at $a$ is a [[algebra-modules/bilinear-map|bilinear map]]
\[
D^2f(a):\mathbb{R}^n\times\mathbb{R}^n\to\mathbb{R}.
\]
Its [[linear-algebra/matrix|matrix]] is the Hessian
\[
\operatorname{Hess}_a(f)
=
\left(\frac{\partial^2f}{\partial x^i\partial x^j}(a)\right).
\]
If $f$ is $C^2$, then [[real-analysis/mixed-partial-derivative|mixed partial derivatives]] commute.

### Inverse function theorem

**Theorem (Inverse function theorem).**
Let $U\subseteq\mathbb{R}^n$ be open. Let $f:U\to\mathbb{R}^n$ be $C^1$. Let $a\in U$. Suppose that $Df(a)$ is invertible. Then there are open [[topology/neighborhood|neighborhoods]] $U_0$ of $a$ and $V_0$ of $f(a)$ such that
\[
\left.f\right|_{U_0}:U_0\to V_0
\]
is a $C^1$ [[fiber-bundles/diffeomorphism|diffeomorphism]]. If $f$ is smooth, then its local inverse is smooth. For $y=f(x)$,
\[
D(f^{-1})(y)=Df(x)^{-1}.
\]

The theorem is a major analytic input. A proof uses a [[shared-foundations/contraction-mapping|contraction mapping]] argument after a linear normalization.

**Corollary.**
A [[fiber-bundles/smooth-map|smooth map]] with invertible [[real-analysis/derivative|derivative]] at each point is a [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphism]].

### Implicit function theorem

Write points of $\mathbb{R}^{n+k}$ as $(x,y)$ with $x\in\mathbb{R}^n$ and $y\in\mathbb{R}^k$.

**Theorem (Implicit function theorem).**
Let $F:U\to\mathbb{R}^k$ be $C^1$, where $U\subseteq\mathbb{R}^{n+k}$ is open. Suppose that $F(a,b)=0$. Suppose that the [[real-analysis/partial-derivative|partial derivative]]
\[
D_yF(a,b):\mathbb{R}^k\to\mathbb{R}^k
\]
is invertible. Then there are [[topology/neighborhood|neighborhoods]] $A$ of $a$ and $B$ of $b$, and a unique $C^1$ map $g:A\to B$, such that
\[
F(x,y)=0
\quad\Longleftrightarrow\quad
y=g(x)
\]
for $(x,y)\in A\times B$. If $F$ is smooth, then $g$ is smooth.

Differentiate the identity $F(x,g(x))=0$. The [[real-analysis/chain-rule|chain rule]] gives
\[
Dg(x)=-D_yF(x,g(x))^{-1}D_xF(x,g(x)).
\]

### Constant-rank theorem

**Theorem (Constant-rank theorem).**
Let $f:U\subseteq\mathbb{R}^n\to\mathbb{R}^m$ be smooth. Suppose that $\operatorname{rank} Df(x)=r$ on a [[topology/neighborhood|neighborhood]] of $a$. Then there are local coordinate [[fiber-bundles/diffeomorphism|diffeomorphisms]] $\phi$ near $a$ and $\psi$ near $f(a)$ such that
\[
(\psi\circ f\circ\phi^{-1})(x^1,\ldots,x^n)
=
(x^1,\ldots,x^r,0,\ldots,0).
\]

The theorem contains the [[shared-foundations/inverse-function|inverse function]] theorem as the case $r=n=m$. It contains the local form of a submersion as the case $r=m$. It contains the local form of an immersion as the case $r=n$.

### Curves and ordinary differential equations

A [[topology/curve|curve]] in $\mathbb{R}^n$ is a map $\gamma:I\to\mathbb{R}^n$, where $I\subseteq\mathbb{R}$ is an [[real-analysis/interval|interval]]. Its velocity is $\dot\gamma(t)=D\gamma(t)(1)$.

A time-dependent ordinary differential equation has the form
\[
\dot x(t)=F(t,x(t)),
\qquad
x(t_0)=x_0.
\]

**Theorem (Local existence and uniqueness).**
Let $F:I\times U\to\mathbb{R}^n$ be continuous. Suppose that $F$ is locally Lipschitz in the $x$ variable. Then each initial value $(t_0,x_0)$ has a unique local solution. If $F$ is smooth, then the solution depends smoothly on the initial data on its [[shared-foundations/domain|domain]] of definition.

This theorem gives local flows of [[fiber-bundles/vector-field|vector fields]]. It also gives geodesics from the geodesic equation.

### Bump functions on Euclidean space

Define
\[
\eta(t)=
\begin{cases}
\exp(-1/t),&t>0,\\
0,&t\leq 0.
\end{cases}
\]
Then $\eta$ is smooth on $\mathbb{R}$. All [[real-analysis/derivative|derivatives]] at $0$ are zero.

For $0<r<R$, define
\[
\chi(x)=
\frac{\eta(R^2-\left\lVert x\right\rVert^2)}{
\eta(R^2-\left\lVert x\right\rVert^2)+\eta(\left\lVert x\right\rVert^2-r^2)}.
\]
Then $\chi$ is smooth. It equals $1$ on the [[topology/closed-ball|closed ball]] $\overline B_r(0)$. Its support is contained in $\overline B_R(0)$. Such maps are [[differential-geometry/bump-function|bump functions]].

[[differential-geometry/bump-function|Bump functions]] are local input for [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partitions of unity]] on manifolds.

### Exercises

**Exercise.**
Prove that a [[linear-algebra/linear-map|linear map]] $L:\mathbb{R}^n\to\mathbb{R}^m$ is differentiable and $DL(a)=L$ at each $a$.

**Exercise.**
Let $f(x)=\left\lVert x\right\rVert^{2}$. Compute $Df(x)$ and $D^2f(x)$.

**Exercise.**
Let $f:\mathbb{R}^2\to\mathbb{R}$ be
\[
f(x,y)=
\begin{cases}
\dfrac{x^3}{x^2+y^2},&(x,y)\neq(0,0),\\
0,&(x,y)=(0,0).
\end{cases}
\]
Determine whether all [[real-analysis/directional-derivative|directional derivatives]] at the origin exist. Determine whether $f$ is differentiable at the origin.

**Exercise.**
Let $F(x,y)=x^2+y^2-1$. Use the [[real-analysis/implicit-function-theorem|implicit function theorem]] near $(0,1)$ to write the unit circle as a graph. Compute the [[real-analysis/derivative|derivative]] of the graph map at $0$.

**Exercise.**
Let $A$ be an $n\times n$ real [[linear-algebra/matrix|matrix]]. Solve $\dot x=Ax$ by the [[linear-algebra/matrix|matrix]] exponential
\[
e^{tA}=\sum_{k=0}^{\infty}\frac{t^kA^k}{k!}.
\]
Prove the [[algebra-groups/group|group]] law $e^{(s+t)A}=e^{sA}e^{tA}$.

 ## [[topology/topological-space|Topological spaces]]

**Required concepts.** [[shared-foundations/set|Sets]], maps, products, quotients, and Euclidean open [[shared-foundations/set|sets]].
**Result of this chapter.** The reader can state the topological hypotheses in the definition of a manifold and can use subspace, product, and [[topology/quotient-topology|quotient topologies]].

### Topologies

**Definition.**
A [[topology/topology|topology]] on a [[shared-foundations/set|set]] $X$ is a [[shared-foundations/set|set]] $\mathcal T$ of [[shared-foundations/subset|subsets]] of $X$ with these properties:

1. $\varnothing\in\mathcal T$ and $X\in\mathcal T$.
1. An arbitrary [[shared-foundations/union|union]] of members of $\mathcal T$ is in $\mathcal T$.
1. A finite [[shared-foundations/intersection|intersection]] of members of $\mathcal T$ is in $\mathcal T$.

The pair $(X,\mathcal T)$ is a [[topology/topological-space|topological space]].
The members of $\mathcal T$ are open [[shared-foundations/set|sets]].

A [[shared-foundations/set|set]] is closed if its [[shared-foundations/complement|complement]] is open.
The interior $\operatorname{Int}(A)$ is the largest open [[shared-foundations/subset|subset]] of $A$.
The closure $\overline A$ is the smallest closed [[shared-foundations/set|set]] that contains $A$.
The [[topology/boundary|boundary]] is
\[
\partial A=\overline A\setminus\operatorname{Int}(A).
\]
A [[topology/neighborhood|neighborhood]] of $x$ is a [[shared-foundations/set|set]] that contains an open [[shared-foundations/set|set]] that contains $x$.

**Definition.**
A collection $\mathcal B$ of open [[shared-foundations/set|sets]] is a [[topology/basis-of-topology|basis]] for the [[topology/topology|topology]] if each open [[shared-foundations/set|set]] is a [[shared-foundations/union|union]] of members of $\mathcal B$.

The [[topology/open-ball|open balls]] form a basis for the Euclidean [[topology/topology|topology]] on $\mathbb{R}^n$.

### Continuous maps

**Definition.**
A map $f:X\to Y$ is [[topology/continuous-map|continuous]] if $f^{-1}(V)$ is open in $X$ for each open [[shared-foundations/set|set]] $V\subseteq Y$.

The identity map is continuous.
A composite of [[topology/continuous-map|continuous maps]] is continuous.

**Definition.**
A [[topology/homeomorphism|homeomorphism]] is a [[shared-foundations/bijective-function|bijective]] [[topology/continuous-map|continuous map]] with a continuous inverse.

Homeomorphic spaces have the same topological properties.
A [[fiber-bundles/smooth-manifold|smooth manifold]] starts with a [[topology/topological-space|topological space]].
Charts give local [[topology/homeomorphism|homeomorphisms]] to Euclidean open [[shared-foundations/set|sets]].

### Subspace, product, and quotient topologies

Let $A\subseteq X$.
The [[topology/subspace-topology|subspace topology]] on $A$ is
\[
\left\{A\cap U:U\text{ is open in }X\right\}.
\]
The inclusion $A\hookrightarrow X$ is continuous.

The [[topology/product-topology|product topology]] on $X\times Y$ has basis
\[
\left\{U\times V:U\subseteq X\text{ open},\ V\subseteq Y\text{ open}\right\}.
\]
The projection maps
\[
\operatorname{pr}_X:X\times Y\to X,
\qquad
\operatorname{pr}_Y:X\times Y\to Y
\]
are continuous.

**Proposition (Universal property of a product).**
A map $f:Z\to X\times Y$ is continuous if and only if $\operatorname{pr}_X\circ f$ and $\operatorname{pr}_Y\circ f$ are continuous.

*Proof.*
The forward direction follows from [[shared-foundations/composition|composition]].
For the reverse direction, the inverse [[shared-foundations/image|image]] of a basis [[shared-foundations/set|set]] is
\[
f^{-1}(U\times V)
=
(\operatorname{pr}_X\circ f)^{-1}(U)\cap(\operatorname{pr}_Y\circ f)^{-1}(V).
\]
This [[shared-foundations/set|set]] is open.
 \(\square\)

Let $q:X\to Q$ be a [[shared-foundations/surjective-function|surjective]] map.
The [[topology/quotient-topology|quotient topology]] on $Q$ is defined by
\[
V\subseteq Q\text{ is open}
\quad\Longleftrightarrow\quad
q^{-1}(V)\text{ is open in }X.
\]
Then $q$ is a quotient map.

**Proposition (Universal property of a quotient topology).**
Let $q:X\to Q$ be a quotient map.
A map $g:Q\to Y$ is continuous if and only if $g\circ q:X\to Y$ is continuous.

*Proof.*
One direction follows from [[shared-foundations/composition|composition]].
Suppose that $g\circ q$ is continuous.
For each open $V\subseteq Y$,
\[
q^{-1}(g^{-1}(V))=(g\circ q)^{-1}(V)
\]
is open.
The definition of the [[topology/quotient-topology|quotient topology]] gives that $g^{-1}(V)$ is open.
 \(\square\)

Quotients require care.
A quotient of a [[topology/hausdorff-space|Hausdorff space]] need not be [[topology/hausdorff-space|Hausdorff]].
A quotient of a manifold need not be a manifold.

### Separation and countability

**Definition.**
A space $X$ is [[topology/hausdorff-space|Hausdorff]] if distinct points have disjoint open [[topology/neighborhood|neighborhoods]].

In a [[topology/hausdorff-space|Hausdorff space]], limits of [[shared-foundations/sequence|sequences]] are unique.
Compact [[shared-foundations/subset|subsets]] of a [[topology/hausdorff-space|Hausdorff space]] are closed.

**Definition.**
A space $X$ is [[fiber-bundles/convention-manifolds-are-smooth-hausdorff-and-second-countable|second countable]] if its [[topology/topology|topology]] has a countable basis.

Second countability gives control over the size of an atlas.
It also implies [[topology/separable-space|separability]].
Each second-countable space has a countable dense [[shared-foundations/subset|subset]].

A space is locally Euclidean of dimension $n$ if each point has a [[topology/neighborhood|neighborhood]] homeomorphic to an open [[shared-foundations/subset|subset]] of $\mathbb{R}^n$.

**Definition.**
A [[topology/topological-manifold|topological $n$-manifold]] is a [[topology/hausdorff-space|Hausdorff]], second-countable, locally [[linear-algebra/euclidean-space|Euclidean space]] of dimension $n$.

Some authors omit one of the first two hypotheses.
These notes include both hypotheses.

### Compactness

**Definition.**
A space $X$ is [[topology/compact-set|compact]] if each [[topology/open-cover|open cover]] of $X$ has a finite subcover.

A [[shared-foundations/subset|subset]] is compact if it is compact in the [[topology/subspace-topology|subspace topology]].

**Theorem (Heine--Borel).**
A [[shared-foundations/subset|subset]] of $\mathbb{R}^n$ is compact if and only if it is closed and bounded.

This theorem depends on completeness of $\mathbb{R}$.

**Proposition.**
The continuous [[shared-foundations/image|image]] of a compact space is compact.

*Proof.*
Let $f:X\to Y$ be continuous.
Let $\{V_\alpha\}$ [[topology/cover|cover]] $f(X)$.
Then $\{f^{-1}(V_\alpha)\}$ [[topology/cover|covers]] $X$.
A finite subfamily [[topology/cover|covers]] $X$.
The corresponding [[shared-foundations/set|sets]] $V_\alpha$ [[topology/cover|cover]] $f(X)$.
 \(\square\)

**Proposition.**
A continuous bijection from a compact space to a [[topology/hausdorff-space|Hausdorff space]] is a [[topology/homeomorphism|homeomorphism]].

*Proof.*
Let $f:X\to Y$ be such a map.
Each closed [[shared-foundations/subset|subset]] $C\subseteq X$ is compact.
Its [[shared-foundations/image|image]] $f(C)$ is compact and therefore closed in $Y$.
Thus $f$ is a closed map.
The inverse map is continuous.
 \(\square\)

### Connectedness

**Definition.**
A space is [[topology/connected-set|connected]] if it is not the [[shared-foundations/union|union]] of two disjoint nonempty open [[shared-foundations/set|sets]].
It is [[topology/path-connected-set|path connected]] if each pair of points is joined by a continuous [[topology/path|path]].

[[topology/path|Path]] connectedness implies connectedness.
The converse can fail.
A locally path-connected connected space is [[topology/path-connected-set|path connected]].
Manifolds are locally [[topology/path-connected-set|path connected]].
Thus each connected manifold is [[topology/path-connected-set|path connected]].

The [[topology/connected-component|connected components]] of a manifold are open.
Second countability implies that a manifold has at most countably many [[topology/connected-component|connected components]].

### Local compactness and proper maps

A space is [[topology/locally-compact-space|locally compact]] if each point has a [[topology/neighborhood|neighborhood]] with compact closure.
A [[topology/topological-manifold|topological manifold]] is [[topology/locally-compact-space|locally compact]].

**Definition.**
A [[topology/continuous-map|continuous map]] $f:X\to Y$ is **proper** if $f^{-1}(K)$ is compact for each [[topology/compact-set|compact set]] $K\subseteq Y$.

For [[topology/locally-compact-space|locally compact]] [[topology/hausdorff-space|Hausdorff spaces]], a proper map is closed.
Proper [[algebra-groups/group-action|group actions]] give well-behaved quotient spaces.

### Paracompactness and local finiteness

**Definition.**
A collection $\{A_i\}_{i\in I}$ is **locally finite** if each point has a [[topology/neighborhood|neighborhood]] that meets only finitely many $A_i$.

Local finiteness makes pointwise sums of supported [[shared-foundations/function|functions]] meaningful.
Near each point, only finitely many terms are nonzero.

**Definition.**
A space is [[fiber-bundles/paracompact-topological-space|paracompact]] if each [[topology/open-cover|open cover]] has a locally finite open refinement.

**Theorem.**
Each [[topology/hausdorff-space|Hausdorff]] second-countable locally [[linear-algebra/euclidean-space|Euclidean space]] is [[fiber-bundles/paracompact-topological-space|paracompact]].

This theorem is a topological input.
It gives [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partitions of unity]] after the [[fiber-bundles/smooth-atlas|smooth structure]] supplies [[differential-geometry/bump-function|bump functions]].

### Partitions of unity as a topological pattern

Let $\{U_i\}_{i\in I}$ be an [[topology/open-cover|open cover]] of $X$.
A family of [[shared-foundations/function|functions]] $\{\rho_i:X\to[0,1]\}_{i\in I}$ is a [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]] subordinate to the [[topology/cover|cover]] if:

1. The supports $\operatorname{supp}\rho_i$ form a locally finite family.
1. $\operatorname{supp}\rho_i\subseteq U_i$ after a suitable indexing or refinement.
1. $\sum_i\rho_i(x)=1$ for all $x\in X$.

The word smooth has no meaning on a [[topology/topological-space|topological space]] without a [[fiber-bundles/smooth-atlas|smooth structure]].
Chapter 4 gives smooth [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partitions of unity]] on [[fiber-bundles/smooth-manifold|smooth manifolds]].

### Exercises

**Exercise.**
Prove that arbitrary [[shared-foundations/union|unions]] of open [[shared-foundations/set|sets]] and finite [[shared-foundations/intersection|intersections]] of open [[shared-foundations/set|sets]] are open in the [[topology/subspace-topology|subspace topology]].

**Exercise.**
Let $q:\mathbb{R}\to\mathbb{R}/\mathbb{Z}$ identify points whose difference is an integer.
Prove that $\mathbb{R}/\mathbb{Z}$ is homeomorphic to the unit circle.

**Exercise.**
Let $X$ be [[topology/hausdorff-space|Hausdorff]].
Prove that the diagonal
\[
\Delta_X=\left\{(x,x):x\in X\right\}
\]
is closed in $X\times X$.
Prove the converse.

**Exercise.**
Prove that a compact discrete space is finite.

**Exercise.**
Let $X$ be connected.
Prove that a [[topology/continuous-map|continuous map]] $f:X\to\left\{0,1\right\}$ is constant when $\left\{0,1\right\}$ has the discrete [[topology/topology|topology]].

# Part: Smooth Manifolds
## Smooth manifolds and smooth maps

**Required concepts.** [[topology/topological-manifold|Topological manifolds]] and [[fiber-bundles/smooth-map|smooth maps]] between Euclidean open [[shared-foundations/set|sets]].
**Result of this chapter.** The reader can define a [[fiber-bundles/smooth-atlas|smooth structure]], test a map in charts, construct standard examples, and use smooth [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partitions of unity]].

### Charts and atlases

Let $M$ be a topological $n$-manifold.

**Definition.**
A [[fiber-bundles/smooth-chart-coordinate-chart|chart]] on $M$ is a pair $(U,\varphi)$ where $U\subseteq M$ is open and
\[
\varphi:U\to\varphi(U)\subseteq\mathbb{R}^n
\]
is a [[topology/homeomorphism|homeomorphism]] onto an open [[shared-foundations/set|set]]. The [[shared-foundations/function|functions]] $x^i=\operatorname{pr}_i\circ\varphi$ are local coordinates.

Let $(U,\varphi)$ and $(V,\psi)$ be charts. Their coordinate-change map is
\[
\psi\circ\varphi^{-1}:
\varphi(U\cap V)\to\psi(U\cap V).
\]

**Definition.**
Two charts are [[fiber-bundles/smooth-atlas|smoothly compatible]] if $U\cap V=\varnothing$ or their coordinate-change map is a smooth [[fiber-bundles/diffeomorphism|diffeomorphism]].

**Definition.**
A [[fiber-bundles/smooth-atlas|smooth atlas]] is a [[shared-foundations/set|set]] of pairwise compatible charts whose [[shared-foundations/domain|domains]] [[topology/cover|cover]] $M$.

An atlas $\mathcal A$ is contained in a unique maximal compatible atlas. This maximal atlas contains each chart that is compatible with every chart in $\mathcal A$.

**Definition.**
A [[fiber-bundles/smooth-atlas|smooth structure]] on $M$ is a maximal [[fiber-bundles/smooth-atlas|smooth atlas]]. A [[fiber-bundles/smooth-manifold|smooth manifold]] is a [[topology/topological-manifold|topological manifold]] with a [[fiber-bundles/smooth-atlas|smooth structure]].

The maximal atlas is part of the structure. A small atlas can specify it.

**Proposition.**
Compatibility with an atlas is enough. Let $\mathcal A$ be a [[fiber-bundles/smooth-atlas|smooth atlas]]. Let $(W,\theta)$ be a chart that is compatible with each chart in $\mathcal A$. Then $(W,\theta)$ is compatible with every chart in the maximal atlas generated by $\mathcal A$.

*Proof.*
Let $(V,\psi)$ belong to the maximal atlas. Fix a point in $W\cap V$. Choose $(U,\varphi)\in\mathcal A$ whose [[shared-foundations/domain|domain]] contains this point. On the relevant overlap,
\[
\psi\circ\theta^{-1}
=
(\psi\circ\varphi^{-1})\circ(\varphi\circ\theta^{-1}).
\]
Both factors are smooth. The same argument applies to the inverse.
 \(\square\)

### Smooth maps

**Definition.**
Let $M$ and $N$ be [[fiber-bundles/smooth-manifold|smooth manifolds]]. A map $F:M\to N$ is [[fiber-bundles/smooth-map|smooth at $p\in M$]] if there are charts $(U,\varphi)$ at $p$ and $(V,\psi)$ at $F(p)$ such that $F(U)\subseteq V$ and
\[
\psi\circ F\circ\varphi^{-1}
\]
is smooth near $\varphi(p)$. The map is smooth if it is smooth at each point.

**Proposition (Chart independence).**
If one chart pair gives a smooth coordinate representation of $F$ at $p$, then every chart pair with suitable [[shared-foundations/domain|domains]] gives a smooth coordinate representation at $p$.

*Proof.*
Let $(U,\varphi)$ and $(V,\psi)$ give a smooth representation. Let $(\widetilde U,\widetilde\varphi)$ and $(\widetilde V,\widetilde\psi)$ be other charts. On a smaller [[topology/neighborhood|neighborhood]],
\[
\widetilde\psi\circ F\circ\widetilde\varphi^{-1}
=
(\widetilde\psi\circ\psi^{-1})
\circ
(\psi\circ F\circ\varphi^{-1})
\circ
(\varphi\circ\widetilde\varphi^{-1}).
\]
Each coordinate-change map is smooth. The [[real-analysis/chain-rule|chain rule]] gives the result.
 \(\square\)

**Definition.**
A [[fiber-bundles/diffeomorphism|diffeomorphism]] is a [[shared-foundations/bijective-function|bijective]] [[fiber-bundles/smooth-map|smooth map]] with a smooth inverse.

A [[fiber-bundles/smooth-map|smooth map]] need not have a smooth inverse. A [[shared-foundations/bijective-function|bijective]] [[fiber-bundles/smooth-map|smooth map]] need not be a [[fiber-bundles/diffeomorphism|diffeomorphism]] without additional assumptions.

The [[shared-foundations/set|set]] of smooth real-valued [[shared-foundations/function|functions]] on $M$ is denoted by $C^{\infty}(M)$. It is a commutative algebra under pointwise operations.

**Proposition.**
The composite of [[fiber-bundles/smooth-map|smooth maps]] is smooth.

*Proof.*
Use charts and apply the Euclidean [[real-analysis/chain-rule|chain rule]].
 \(\square\)

### Standard examples

#### Euclidean open sets

Each open [[shared-foundations/set|set]] $U\subseteq\mathbb{R}^n$ is a smooth $n$-manifold. The one-chart atlas contains $(U,\operatorname{id}_U)$.

#### The sphere

The [[linear-algebra/unit-sphere|unit sphere]] is
\[
S^n=\left\{x\in\mathbb{R}^{n+1}:\left\lVert x\right\rVert=1\right\}.
\]
Let $N=(0,\ldots,0,1)$ and $S=(0,\ldots,0,-1)$. Stereographic projection from $N$ gives a chart
\[
\sigma_N:S^n\setminus\left\{N\right\}\to\mathbb{R}^n,
\qquad
\sigma_N(x',x^{n+1})=\frac{x'}{1-x^{n+1}}.
\]
Projection from $S$ gives a second chart. The transition map on $\mathbb{R}^n\setminus\left\{0\right\}$ is
\[
u\mapsto \frac{u}{\left\lVert u\right\rVert^{2}}.
\]
This map is smooth. The two charts define a [[fiber-bundles/smooth-atlas|smooth structure]] on $S^n$.

#### Products

If $M$ is an $m$-manifold and $N$ is an $n$-manifold, then $M\times N$ is an $(m+n)$-manifold. Product charts are
\[
(U\times V,\varphi\times\psi).
\]
The transition maps are products of transition maps.

#### The torus

The $n$-torus is
\[
T^n=\mathbb{R}^n/\mathbb{Z}^n.
\]
The [[algebra-groups/group|group]] $\mathbb{Z}^n$ acts by translations. Small Euclidean balls that do not meet their nontrivial integer translates descend to charts. These charts define a [[fiber-bundles/smooth-atlas|smooth structure]]. The quotient map $\mathbb{R}^n\to T^n$ is a [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphism]].

The product $(S^1)^n$ is diffeomorphic to $T^n$.

#### Real projective space

Real [[algebraic-geometry-foundations/projective-space|projective space]] $\mathbb{R} P^n$ is the [[shared-foundations/set|set]] of one-dimensional [[convex-analysis/linear-subspace|linear subspaces]] of $\mathbb{R}^{n+1}$. It is also the quotient
\[
S^n/(x\sim -x).
\]
For $0\leq i\leq n$, let $U_i$ be the [[shared-foundations/set|set]] of lines with a representative whose $i$th coordinate is nonzero. Normalize this coordinate to $1$. The remaining coordinates give a chart $U_i\to\mathbb{R}^n$. The transition maps are rational maps with nonzero denominators. They are smooth.

#### Matrices

The space $M_{m\times n}(\mathbb{R})$ is a [[linear-algebra/euclidean-space|Euclidean space]]. The [[lie-groups/general-linear-group|general linear group]]
\[
\operatorname{GL}(n,\mathbb{R})=\left\{A\in M_{n\times n}(\mathbb{R}):\det A\neq 0\right\}
\]
is open because the [[linear-algebra/determinant|determinant]] is continuous. Thus $\operatorname{GL}(n,\mathbb{R})$ is a [[fiber-bundles/smooth-manifold|smooth manifold]]. Chapter~10 adds the [[algebra-groups/group|group]] structure.

### Equivalent smooth structures

Two atlases define the same [[fiber-bundles/smooth-atlas|smooth structure]] if their [[shared-foundations/union|union]] is a [[fiber-bundles/smooth-atlas|smooth atlas]]. A [[topology/homeomorphism|homeomorphism]] $F:M\to N$ can transport a [[fiber-bundles/smooth-atlas|smooth structure]] from $N$ to $M$. The transported charts have the form $(F^{-1}(V),\psi\circ F)$.

A [[topology/topological-manifold|topological manifold]] can have more than one non-diffeomorphic [[fiber-bundles/smooth-atlas|smooth structure]]. This issue does not affect local definitions. It affects global classification.

### Smooth functions as structure data

A chart gives smooth coordinate [[shared-foundations/function|functions]] $x^1,\ldots,x^n$. Conversely, a map
\[
(x^1,\ldots,x^n):U\to\mathbb{R}^n
\]
forms a chart when it is a [[topology/homeomorphism|homeomorphism]] onto an open [[shared-foundations/set|set]] and has compatible coordinate changes.

The algebra $C^{\infty}(M)$ determines the [[fiber-bundles/smooth-manifold|smooth manifold]] up to [[fiber-bundles/diffeomorphism|diffeomorphism]] under standard finite-dimensional hypotheses. This fact motivates the derivation definition of [[fiber-bundles/tangent-space-at-a-point|tangent vectors]].

### Manifolds with boundary

Define the closed upper half-space
\[
\mathbb H^n=\left\{x\in\mathbb{R}^n:x^n\geq 0\right\}.
\]
A [[shared-foundations/subset|subset]] $U\subseteq\mathbb H^n$ is relatively open when $U=\mathbb H^n\cap V$ for an open [[shared-foundations/set|set]] $V\subseteq\mathbb{R}^n$.

**Definition.**
A [[differential-geometry/manifold-with-boundary|smooth manifold with boundary]] has charts to relatively open [[shared-foundations/subset|subsets]] of $\mathbb H^n$. Coordinate changes extend smoothly to open [[shared-foundations/subset|subsets]] of $\mathbb{R}^n$.

A point is a [[differential-geometry/boundary-and-interior-of-a-manifold|boundary point]] when one, and therefore every, chart sends it to $x^n=0$. The [[shared-foundations/set|set]] of [[differential-geometry/boundary-and-interior-of-a-manifold|boundary points]] is $\partial M$. The interior $M\setminus\partial M$ is a [[fiber-bundles/smooth-manifold|smooth manifold]] without [[topology/boundary|boundary]].

The invariance of [[topology/boundary|boundary]] type is a theorem. It uses invariance of [[shared-foundations/domain|domain]] or local homology.

### Smooth bump functions

**Proposition (Local bump function).**
Let $M$ be a [[fiber-bundles/smooth-manifold|smooth manifold]]. Let $p\in U$, where $U\subseteq M$ is open. Then there is $\rho\in C^{\infty}(M)$ such that
\[
0\leq\rho\leq 1,
\qquad
\rho=1\text{ near }p,
\qquad
\operatorname{supp}\rho\subseteq U.
\]

*Proof.*
Choose a chart $(V,\varphi)$ with $p\in V$ and $\overline V\subseteq U$. Choose Euclidean balls
\[
\varphi(p)\in B_r(\varphi(p))
\subseteq
\overline B_R(\varphi(p))
\subseteq
\varphi(V).
\]
Use the Euclidean [[differential-geometry/bump-function|bump function]] from Chapter~2. Compose it with $\varphi$ on $V$. Extend it by zero outside $V$. The support lies in a compact [[shared-foundations/subset|subset]] of $V$, so the extension is smooth across the edge of $V$.
 \(\square\)

### Smooth partitions of unity

**Theorem (Smooth partition of unity).**
Let $M$ be a [[fiber-bundles/smooth-manifold|smooth manifold]]. Let $\{U_\alpha\}_{\alpha\in A}$ be an [[topology/open-cover|open cover]]. Then there is a smooth [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]] $\{\rho_i\}_{i\in I}$ such that each $\operatorname{supp}\rho_i$ lies in some $U_\alpha$. The family of supports is locally finite.

*Proof.*[Construction outline]
Paracompactness gives a locally finite refinement by precompact coordinate [[topology/neighborhood|neighborhoods]] $V_i$ with $\overline V_i\subseteq U_{\alpha(i)}$. Choose a smaller [[topology/cover|cover]] $W_i$ with $\overline W_i\subseteq V_i$. A local [[differential-geometry/bump-function|bump function]] gives $\chi_i$ with $\chi_i=1$ on $\overline W_i$ and $\operatorname{supp}\chi_i\subseteq V_i$.

The sum $s=\sum_i\chi_i$ is smooth because the family is locally finite. At each point, one of the $\chi_i$ equals $1$. Thus $s>0$. Define
\[
\rho_i=\frac{\chi_i}{s}.
\]
Then $\sum_i\rho_i=1$, and each support lies in $V_i\subseteq U_{\alpha(i)}$.
 \(\square\)

**Remark.**
[[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|Partitions of unity]] convert local data into global data when the local data combine by convex sums. They give [[differential-geometry/riemannian-manifold|Riemannian metrics]], [[fiber-bundles/bundle-metric|bundle metrics]], [[fiber-bundles/section-of-a-fiber-bundle|global sections]] with local constraints, and integration formulas.

### Exercises

**Exercise.**
Prove that the stereographic transition map is its own inverse.

**Exercise.**
Prove that a map $f:M\to\mathbb{R}^k$ is smooth if and only if each component [[shared-foundations/function|function]] is smooth.

**Exercise.**
Let $M$ and $N$ be [[fiber-bundles/smooth-manifold|smooth manifolds]]. Prove that the projection $M\times N\to M$ is smooth. Prove that a map $F:P\to M\times N$ is smooth if and only if its two component maps are smooth.

**Exercise.**
Construct an atlas on $S^1$ from four graph charts. Compare it with the stereographic atlas.

**Exercise.**
Let $M$ be compact. Prove that each [[topology/open-cover|open cover]] of $M$ has a finite smooth [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]] subordinate to the [[topology/cover|cover]].

 ## [[differential-geometry/tangent-space|Tangent spaces]], cotangent spaces, and differentials

**Required concepts.** [[fiber-bundles/smooth-manifold|Smooth manifolds]], [[fiber-bundles/smooth-map|smooth functions]], [[real-analysis/derivative|derivatives]] in [[linear-algebra/euclidean-space|Euclidean space]], and dual [[linear-algebra/vector-space|vector spaces]].
**Result of this chapter.** The reader can construct tangent and cotangent spaces, compute differentials, and give [[fiber-bundles/smooth-atlas|smooth structures]] to the tangent and [[fiber-bundles/cotangent-bundle|cotangent bundles]].

### Derivations at a point

Let $M$ be a [[fiber-bundles/smooth-manifold|smooth manifold]] and let $p\in M$.

**Definition.**
A **derivation at $p$** is a [[linear-algebra/linear-map|linear map]]
\[
v:C^\infty(M)\to\mathbb{R}
\]
that satisfies the Leibniz rule
\[
v(fg)=f(p)v(g)+g(p)v(f).
\]
The [[differential-geometry/tangent-space|tangent space]] $T_pM$ is the [[linear-algebra/vector-space|vector space]] of derivations at $p$.

A derivation [[measure-theory/measure|measures]] first-order change at one point.

**Lemma.**
Each derivation $v\in T_pM$ satisfies $v(1)=0$ and $v(c)=0$ for each constant [[shared-foundations/function|function]] $c$.

*Proof.*
The Leibniz rule gives
\[
v(1)=v(1\cdot 1)=2v(1).
\]
Thus $v(1)=0$. Linearity gives $v(c)=cv(1)=0$.
 \(\square\)

**Lemma (Locality).**
Suppose that $f,g\in C^\infty(M)$ agree on a [[topology/neighborhood|neighborhood]] of $p$. Then $v(f)=v(g)$ for each $v\in T_pM$.

*Proof.*
[[shared-foundations/set|Set]] $h=f-g$. Then $h$ is zero near $p$. Choose a [[differential-geometry/bump-function|bump function]] $\rho$ that equals $1$ near $p$ and has support in a [[topology/neighborhood|neighborhood]] on which $h=0$. Then $h=(1-\rho)h$. The Leibniz rule gives
\[
v(h)=(1-\rho)(p)v(h)+h(p)v(1-\rho)=0.
\]
Thus $v(f)=v(g)$.
 \(\square\)

This lemma permits the use of local coordinate [[shared-foundations/function|functions]] in a derivation.

### Coordinate tangent vectors

Let $(U,x)$ be a chart at $p$, where
\[
x=(x^1,\ldots,x^n):U\to\mathbb{R}^n.
\]
Define
\[
\left.\frac{\partial}{\partial x^i}\right|_p f
=
\frac{\partial(f\circ x^{-1})}{\partial u^i}(x(p)).
\]
Locality makes this definition valid for global [[fiber-bundles/smooth-map|smooth functions]].

**Theorem.**
The vectors
\[
\left.\frac{\partial}{\partial x^1}\right|_p,
\ldots,
\left.\frac{\partial}{\partial x^n}\right|_p
\]
form a basis of $T_pM$.

*Proof.*
Use coordinates and [[shared-foundations/set|set]] $a=x(p)$. The Euclidean Hadamard lemma gives, near $a$,
\[
F(u)-F(a)
=
\sum_{i=1}^n(u^i-a^i)G_i(u),
\qquad
G_i(a)=\frac{\partial F}{\partial u^i}(a),
\]
for each smooth $F$. Apply this to $F=f\circ x^{-1}$. For $v\in T_pM$, the Leibniz rule gives
\[
v(f)=\sum_{i=1}^n v(x^i)\frac{\partial(f\circ x^{-1})}{\partial u^i}(a).
\]
Thus
\[
v=\sum_{i=1}^n v(x^i)\left.\frac{\partial}{\partial x^i}\right|_p.
\]
This proves spanning. Apply a linear [[shared-foundations/relation|relation]] to the coordinate [[shared-foundations/function|function]] $x^j$. The coefficient of $\partial/\partial x^j$ is zero. Thus the list is independent.
 \(\square\)

The [[differential-geometry/tangent-space|tangent space]] has dimension $n$. Under a coordinate change $y=y(x)$,
\[
\left.\frac{\partial}{\partial x^i}\right|_p
=
\sum_{\alpha=1}^n
\frac{\partial y^\alpha}{\partial x^i}(p)
\left.\frac{\partial}{\partial y^\alpha}\right|_p.
\]
The [[real-analysis/jacobian-matrix|Jacobian matrix]] controls the basis change.

### Tangent vectors from curves

Let $\gamma:(-\varepsilon,\varepsilon)\to M$ be a smooth [[topology/curve|curve]] with $\gamma(0)=p$. Define
\[
v_\gamma(f)=\left.\frac{d}{dt}\right|_{t=0}f(\gamma(t)).
\]
The [[real-analysis/chain-rule|chain rule]] shows that $v_\gamma$ is a derivation.

Two [[topology/curve|curves]] through $p$ have first-order contact when they give the same derivation. The [[shared-foundations/equivalence-class|equivalence class]] is a [[fiber-bundles/tangent-space-at-a-point|tangent vector]].

**Theorem.**
Every derivation at $p$ is the [[fiber-bundles/tangent-space-at-a-point|tangent vector]] of a smooth [[topology/curve|curve]] through $p$.

*Proof.*
Let $(U,x)$ be a chart at $p$. Write
\[
v=\sum_i v^i\left.\frac{\partial}{\partial x^i}\right|_p.
\]
For small $t$, define
\[
\gamma(t)=x^{-1}\bigl(x(p)+t(v^1,\ldots,v^n)\bigr).
\]
Then $v_\gamma=v$ by the Euclidean [[real-analysis/chain-rule|chain rule]].
 \(\square\)

The derivation model and the [[topology/curve|curve]] model are equivalent. The derivation model is intrinsic. The [[topology/curve|curve]] model gives a geometric representation.

### Differentials

**Definition.**
Let $F:M\to N$ be smooth. The [[fiber-bundles/differential-of-a-smooth-map|differential of $F$ at $p$]] is the [[linear-algebra/linear-map|linear map]]
\[
dF_p:T_pM\to T_{F(p)}N
\]
defined by
\[
(dF_pv)(h)=v(h\circ F),
\qquad
h\in C^\infty(N).
\]

For the [[topology/curve|curve]] model,
\[
dF_p[\gamma]=[F\circ\gamma].
\]

**Proposition (Chain rule on manifolds).**
For [[fiber-bundles/smooth-map|smooth maps]] $F:M\to N$ and $G:N\to P$,
\[
d(G\circ F)_p=dG_{F(p)}\circ dF_p.
\]

*Proof.*
For $v\in T_pM$ and $h\in C^\infty(P)$,
\[
(d(G\circ F)_pv)(h)
=v(h\circ G\circ F)
=(dF_pv)(h\circ G)
=(dG_{F(p)}dF_pv)(h).
\]
 \(\square\)

If $F$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]], then $dF_p$ is an [[algebra-category-theory/isomorphism-category|isomorphism]] and
\[
d(F^{-1})_{F(p)}=(dF_p)^{-1}.
\]

In coordinates $x$ on $M$ and $y$ on $N$,
\[
dF_p\left(\left.\frac{\partial}{\partial x^i}\right|_p\right)
=
\sum_\alpha
\frac{\partial(y^\alpha\circ F\circ x^{-1})}{\partial u^i}(x(p))
\left.\frac{\partial}{\partial y^\alpha}\right|_{F(p)}.
\]
Thus the [[linear-algebra/matrix|matrix]] of $dF_p$ is the [[real-analysis/jacobian-matrix|Jacobian matrix]] of the coordinate representation.

### Cotangent spaces

**Definition.**
The **cotangent space** at $p$ is the dual [[linear-algebra/vector-space|vector space]]
\[
T_p^*M=(T_pM)^*.
\]

The coordinate covectors $dx^1|_p,\ldots,dx^n|_p$ form the dual basis. They satisfy
\[
dx^i|_p\left(\left.\frac{\partial}{\partial x^j}\right|_p\right)=\delta^i_j.
\]

For $f\in C^\infty(M)$, its differential at $p$ is the covector
\[
df_p(v)=v(f).
\]
In coordinates,
\[
df_p=\sum_i\frac{\partial f}{\partial x^i}(p)\,dx^i|_p.
\]
Under a coordinate change,
\[
dy^\alpha=\sum_i\frac{\partial y^\alpha}{\partial x^i}\,dx^i.
\]
Tangent bases transform by the Jacobian. Cotangent bases transform by the transpose rule that preserves the pairing.

### Pullback of covectors

Let $F:M\to N$ be smooth. The dual of $dF_p$ is
\[
(dF_p)^*:T^*_{F(p)}N\to T_p^*M.
\]
It is defined by
\[
((dF_p)^*\alpha)(v)=\alpha(dF_pv).
\]
For $h\in C^\infty(N)$,
\[
F^*(dh)=d(h\circ F).
\]
The notation $F^*$ is the [[algebra-category-theory/pullback|pullback]]. [[algebra-category-theory/pullback|Pullback]] reverses the direction of the map.

### The tangent bundle

Define the disjoint [[shared-foundations/union|union]]
\[
TM=\coprod_{p\in M}T_pM.
\]
The projection is
\[
\pi:TM\to M,
\qquad
\pi(v)=p\quad\text{when }v\in T_pM.
\]

A chart $(U,x)$ on $M$ gives a map
\[
\widetilde x:\pi^{-1}(U)\to x(U)\times\mathbb{R}^n
\]
by
\[
\widetilde x\left(\sum_i v^i\left.\frac{\partial}{\partial x^i}\right|_p\right)
=
\bigl(x(p),(v^1,\ldots,v^n)\bigr).
\]
On an overlap, the coordinate change has the form
\[
(u,v)\longmapsto
\bigl(y\circ x^{-1}(u),D(y\circ x^{-1})(u)v\bigr).
\]
This map is smooth. These bundle charts define a [[fiber-bundles/smooth-atlas|smooth structure]] on $TM$. The dimension of $TM$ is $2n$.

The restriction
\[
\pi^{-1}(U)\cong U\times\mathbb{R}^n
\]
is a local product. The map is linear on each fiber. Chapter~9 abstracts this structure as a [[fiber-bundles/vector-bundle|vector bundle]].

### The cotangent bundle

Define
\[
T^*M=\coprod_{p\in M}T_p^*M.
\]
A coordinate covector
\[
\alpha=\sum_i\alpha_i\,dx^i|_p
\]
has bundle coordinates $(x(p),\alpha_1,\ldots,\alpha_n)$. On an overlap, covector components transform by
\[
\beta_\alpha=\sum_i\frac{\partial x^i}{\partial y^\alpha}\alpha_i.
\]
This gives a [[fiber-bundles/smooth-atlas|smooth structure]] on $T^*M$.

There is a [[differential-geometry/tautological-one-form-cotangent|canonical one-form]] $\theta$ on $T^*M$. At $\alpha_p\in T^*M$, define
\[
\theta_{\alpha_p}(V)=\alpha_p(d\pi_{\alpha_p}V).
\]
Its [[fiber-bundles/exterior-derivative|exterior derivative]] gives the canonical symplectic form. Chapter~8 defines [[fiber-bundles/exterior-derivative|exterior derivatives]] and [[fiber-bundles/differential-k-form|differential forms]].

### Rank and regularity

**Definition.**
The [[differential-geometry/rank-of-a-smooth-map|rank of a smooth map]] $F:M\to N$ at $p$ is $\operatorname{rank} dF_p$. A point is [[real-analysis/regular-point|regular]] if $dF_p$ has maximal [[linear-algebra/rank|rank]] relative to the required context. A point is [[differential-geometry/critical-point-of-a-smooth-map|critical]] otherwise.

For a real-valued [[shared-foundations/function|function]] $f:M\to\mathbb{R}$, a point is critical exactly when $df_p=0$.

### Exercises

**Exercise.**
Prove the locality lemma without a global [[differential-geometry/bump-function|bump function]] when $M$ is an open [[shared-foundations/subset|subset]] of $\mathbb{R}^n$.

**Exercise.**
Let $F:\mathbb{R}^2\to\mathbb{R}^2$ be
\[
F(r,\theta)=(r\cos\theta,r\sin\theta).
\]
Compute $dF_{(r,\theta)}$. Find its [[linear-algebra/rank|rank]].

**Exercise.**
Let $F:M\to N$ be constant. Prove that $dF_p=0$ for all $p$.

**Exercise.**
Prove that $T(M\times N)$ is diffeomorphic to $TM\times TN$ over $M\times N$.

**Exercise.**
Let $f:M\to\mathbb{R}$ and $F:N\to M$ be smooth. Prove that
\[
d(f\circ F)=F^*(df).
\]

 ## Local normal forms and submanifolds

**Required concepts.** Differentials, [[linear-algebra/rank|rank]], the Euclidean constant-rank theorem, and [[fiber-bundles/smooth-chart|smooth charts]].
**Result of this chapter.** The reader can distinguish immersions, submersions, and embeddings, and can construct manifolds as [[differential-geometry/regular-level-set|regular level sets]].

### Immersions, submersions, and local diffeomorphisms

Let $F:M^m\to N^n$ be smooth.

**Definition.**
The map $F$ is an [[fiber-bundles/smooth-immersion|immersion at $p$]] if $dF_p$ is [[shared-foundations/injective-function|injective]]. It is a [[fiber-bundles/smooth-submersion|submersion at $p$]] if $dF_p$ is [[shared-foundations/surjective-function|surjective]]. It is a [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphism at $p$]] if it restricts to a [[fiber-bundles/diffeomorphism|diffeomorphism]] from a [[topology/neighborhood|neighborhood]] of $p$ to an open [[shared-foundations/subset|subset]] of $N$.

An immersion requires $m\leq n$. A submersion requires $m\geq n$.

**Theorem (Manifold inverse function theorem).**
Let $F:M^n\to N^n$ be smooth. If $dF_p$ is an [[algebra-category-theory/isomorphism-category|isomorphism]], then $F$ is a [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphism]] at $p$.

*Proof.*
Choose charts at $p$ and $F(p)$. The coordinate representation has an invertible Euclidean [[real-analysis/derivative|derivative]]. Apply the Euclidean [[shared-foundations/inverse-function|inverse function]] theorem. Translate the local inverse back through the charts.
 \(\square\)

### Constant-rank theorem on manifolds

**Theorem (Constant-rank theorem).**
Let $F:M^m\to N^n$ be smooth. Suppose that $\operatorname{rank} dF=r$ on a [[topology/neighborhood|neighborhood]] of $p$. Then there are charts $x$ at $p$ and $y$ at $F(p)$ such that
\[
y\circ F\circ x^{-1}(u^1,\ldots,u^m)
=
(u^1,\ldots,u^r,0,\ldots,0).
\]

The theorem follows from the Euclidean constant-rank theorem in charts.

**Corollary (Immersion normal form).**
If $F$ is an immersion at $p$, then there are local coordinates in which
\[
F(u^1,\ldots,u^m)=(u^1,\ldots,u^m,0,\ldots,0).
\]

**Corollary (Submersion normal form).**
If $F$ is a submersion at $p$, then there are local coordinates in which
\[
F(u^1,\ldots,u^m)=(u^1,\ldots,u^n).
\]

The [[linear-algebra/rank|rank]] condition at one point persists near that point when the [[linear-algebra/rank|rank]] is maximal. A nonzero maximal minor remains nonzero on a [[topology/neighborhood|neighborhood]].

### Embedded submanifolds

**Definition.**
A [[shared-foundations/subset|subset]] $S\subseteq M^n$ is an [[differential-geometry/embedded-submanifold|embedded $k$-submanifold]] if each $p\in S$ has a chart $(U,x)$ of $M$ such that
\[
x(U\cap S)=x(U)\cap(\mathbb{R}^k\times\left\{0\right\}).
\]
Such a chart is a [[differential-geometry/submanifold-chart|slice chart]].

The [[topology/subspace-topology|subspace topology]] and the restricted slice coordinates make $S$ a smooth $k$-manifold. The inclusion
\[
\iota:S\hookrightarrow M
\]
is a [[fiber-bundles/smooth-immersion|smooth immersion]] and a topological embedding.

**Definition.**
A [[fiber-bundles/smooth-map|smooth map]] $F:M\to N$ is a [[fiber-bundles/smooth-embedding|smooth embedding]] if it is an immersion and a [[topology/homeomorphism|homeomorphism]] from $M$ to the subspace $F(M)\subseteq N$.

**Theorem.**
A [[fiber-bundles/smooth-map|smooth map]] is an embedding if and only if it is a [[fiber-bundles/diffeomorphism|diffeomorphism]] from its [[shared-foundations/domain|domain]] onto an [[differential-geometry/embedded-submanifold|embedded submanifold]] of its [[shared-foundations/codomain|codomain]].

*Proof.*[Proof outline]
The local immersion normal form shows that an embedding has a local slice [[shared-foundations/image|image]]. The [[topology/homeomorphism|homeomorphism]] condition gives the correct global [[topology/subspace-topology|subspace topology]]. Conversely, the inclusion of a slice is an immersion, and a [[fiber-bundles/diffeomorphism|diffeomorphism]] onto that slice preserves both properties.
 \(\square\)

**Warning.**
An [[shared-foundations/injective-function|injective]] immersion need not be an embedding. The [[shared-foundations/image|image]] can have the wrong [[topology/subspace-topology|subspace topology]].

**Example.**
Identify $T^2$ with $S^1\times S^1$. Let $\alpha\in\mathbb{R}\setminus\mathbb{Q}$. The map
\[
F:\mathbb{R}\to T^2,
\qquad
F(t)=(e^{\mathrm{i} t},e^{\mathrm{i}\alpha t})
\]
is an [[shared-foundations/injective-function|injective]] immersion. Its [[shared-foundations/image|image]] is dense. Thus it is not an embedding.

### Immersed submanifolds

An [[differential-geometry/immersed-submanifold|immersed submanifold]] is a manifold $S$ with an immersion $F:S\to M$. The map need not be [[shared-foundations/injective-function|injective]]. When it is [[shared-foundations/injective-function|injective]], its [[shared-foundations/image|image]] can still fail to have the [[topology/subspace-topology|subspace topology]].

[[differential-geometry/embedded-submanifold|Embedded submanifolds]] are [[shared-foundations/subset|subsets]] with an induced [[fiber-bundles/smooth-atlas|smooth structure]]. [[differential-geometry/immersed-submanifold|Immersed submanifolds]] include parametrized self-intersections and dense immersed [[shared-foundations/image|images]].

### Regular level sets

**Definition.**
Let $F:M^m\to N^n$ be smooth. A point $q\in N$ is a [[fiber-bundles/regular-value|regular value]] if $dF_p$ is [[shared-foundations/surjective-function|surjective]] for every $p\in F^{-1}(q)$. A value that is not regular is a [[real-analysis/critical-value|critical value]].

**Theorem (Regular value theorem).**
If $q$ is a [[fiber-bundles/regular-value|regular value]] of $F:M^m\to N^n$, then $F^{-1}(q)$ is an [[differential-geometry/embedded-submanifold|embedded submanifold]] of dimension $m-n$. Its [[differential-geometry/tangent-space|tangent space]] is
\[
T_pF^{-1}(q)=\operatorname{ker} dF_p.
\]

*Proof.*
At each $p\in F^{-1}(q)$, the submersion normal form gives coordinates in which
\[
F(u^1,\ldots,u^m)=(u^1,\ldots,u^n).
\]
After a translation in target coordinates, the level [[shared-foundations/set|set]] is
\[
u^1=\cdots=u^n=0.
\]
This is a coordinate slice of dimension $m-n$. The tangent slice is the kernel of the coordinate projection. Coordinate invariance gives the kernel formula.
 \(\square\)

**Example (Sphere).**
Define $F:\mathbb{R}^{n+1}\to\mathbb{R}$ by $F(x)=\left\lVert x\right\rVert^2$. Then
\[
dF_x(v)=2\left\langle x,v\right\rangle.
\]
For $x\in F^{-1}(1)$, this covector is nonzero. Thus $1$ is a [[fiber-bundles/regular-value|regular value]] and $S^n=F^{-1}(1)$ is an embedded $n$-manifold. Its [[differential-geometry/tangent-space|tangent space]] is
\[
T_xS^n=\left\{v\in\mathbb{R}^{n+1}:\left\langle x,v\right\rangle=0\right\}=x^\perp.
\]

**Example (Special linear group).**
The [[linear-algebra/determinant|determinant]] map
\[
\det:\operatorname{GL}(n,\mathbb{R})\to\mathbb{R}^\times
\]
has [[real-analysis/derivative|derivative]]
\[
d(\det)_A(H)=\det(A)\operatorname{tr}(A^{-1}H).
\]
This [[real-analysis/derivative|derivative]] is nonzero. Thus
\[
\operatorname{SL}(n,\mathbb{R})=\det^{-1}(1)
\]
is an [[differential-geometry/embedded-submanifold|embedded submanifold]] of [[convex-analysis/codimension|codimension]] one.

### Graphs

Let $f:M\to N$ be smooth. Its graph is
\[
\Gamma_f=\left\{(p,f(p)):p\in M\right\}\subseteq M\times N.
\]

**Proposition.**
The graph $\Gamma_f$ is an [[differential-geometry/embedded-submanifold|embedded submanifold]]. The map
\[
p\longmapsto(p,f(p))
\]
is an embedding.

*Proof.*
The map is an immersion because its differential is
\[
v\longmapsto(v,df_pv).
\]
The first projection restricts to a continuous inverse on the [[shared-foundations/image|image]]. Thus the map is an embedding.
 \(\square\)

### Transversality

**Definition.**
Let $F:M\to N$ be smooth. Let $S\subseteq N$ be an [[differential-geometry/embedded-submanifold|embedded submanifold]]. The map $F$ is [[differential-geometry/map-transverse-to-a-submanifold|transverse to $S$ at $p$]] when $F(p)\in S$ implies
\[
dF_p(T_pM)+T_{F(p)}S=T_{F(p)}N.
\]
Write $F\pitchfork S$ when this holds at every relevant point.

**Theorem (Transverse preimage theorem).**
If $F\pitchfork S$, then $F^{-1}(S)$ is an [[differential-geometry/embedded-submanifold|embedded submanifold]]. Its [[convex-analysis/codimension|codimension]] in $M$ equals the [[convex-analysis/codimension|codimension]] of $S$ in $N$. At $p\in F^{-1}(S)$,
\[
T_pF^{-1}(S)=\left\{v\in T_pM:dF_pv\in T_{F(p)}S\right\}.
\]

The [[fiber-bundles/regular-value|regular value]] theorem is the case $S=\left\{q\right\}$.

### Compact injective immersions

**Proposition.**
Let $M$ be compact and let $N$ be [[topology/hausdorff-space|Hausdorff]]. Each [[shared-foundations/injective-function|injective]] immersion $F:M\to N$ is an embedding.

*Proof.*
A continuous injection from a compact space to a [[topology/hausdorff-space|Hausdorff space]] is a [[topology/homeomorphism|homeomorphism]] onto its [[shared-foundations/image|image]]. Add the immersion hypothesis.
 \(\square\)

### Exercises

**Exercise.**
Prove that the inclusion $S^n\hookrightarrow\mathbb{R}^{n+1}$ is an embedding.

**Exercise.**
Let $f:\mathbb{R}^n\to\mathbb{R}$ be smooth. Suppose that $df_p\neq 0$ at each point of $f^{-1}(0)$. Prove that $f^{-1}(0)$ is a hypersurface.

**Exercise.**
Prove that
\[
\mathrm O(n)=\left\{A\in M_n(\mathbb{R}):A^{\mathsf T}A=I\right\}
\]
is an [[differential-geometry/embedded-submanifold|embedded submanifold]] of $M_n(\mathbb{R})$. Compute its [[differential-geometry/tangent-space|tangent space]] at the identity.

**Exercise.**
Let $F:M\to N$ be a submersion. Prove that $F$ is an open map.

**Exercise.**
Let $S_1,S_2\subseteq M$ be [[differential-geometry/embedded-submanifold|embedded submanifolds]]. Suppose that they are transverse. Prove that $S_1\cap S_2$ is an [[differential-geometry/embedded-submanifold|embedded submanifold]] and
\[
T_p(S_1\cap S_2)=T_pS_1\cap T_pS_2.
\]

 ## [[fiber-bundles/vector-field|Vector fields]], flows, and distributions

**Required concepts.** The [[fiber-bundles/tangent-bundle|tangent bundle]], [[fiber-bundles/section-of-a-fiber-bundle|smooth sections]], differentials, and ODE existence and uniqueness.
**Result of this chapter.** The reader can compute [[fiber-bundles/lie-bracket|Lie brackets]], construct local flows, and state the Frobenius integrability theorem.

### Vector fields

**Definition.**
A [[fiber-bundles/vector-field|vector field]] on $M$ is a [[fiber-bundles/smooth-map|smooth map]] $X:M\to TM$ such that
\[
\pi\circ X=\operatorname{id}_M.
\]
Thus $X(p)\in T_pM$ for each $p$.

The [[shared-foundations/set|set]] of smooth [[fiber-bundles/vector-field|vector fields]] is denoted by $\mathfrak X(M)$. In a chart $(U,x)$, a [[fiber-bundles/vector-field|vector field]] has the form
\[
X=\sum_{i=1}^n X^i\frac{\partial}{\partial x^i}.
\]
The field is smooth if and only if each component $X^i$ is smooth.

A [[fiber-bundles/vector-field|vector field]] acts on [[fiber-bundles/smooth-map|smooth functions]] by
\[
Xf(p)=X(p)f.
\]
This action is a derivation of the algebra $C^\infty(M)$:
\[
X(fg)=fXg+gXf.
\]

**Theorem.**
Each derivation
\[
D:C^\infty(M)\to C^\infty(M)
\]
is $D=X$ for a unique smooth [[fiber-bundles/vector-field|vector field]] $X$.

*Proof.*
For each $p$, define $X(p)f=Df(p)$. The Leibniz rule makes $X(p)$ a [[fiber-bundles/tangent-space-at-a-point|tangent vector]]. In coordinates,
\[
X^i=D(x^i).
\]
These [[shared-foundations/function|functions]] are smooth. Thus $X$ is smooth. Uniqueness follows from the action on [[shared-foundations/function|functions]].
 \(\square\)

### The Lie bracket

**Definition.**
For $X,Y\in\mathfrak X(M)$, define the [[fiber-bundles/lie-bracket|Lie bracket]] by
\[
[X,Y]f=X(Yf)-Y(Xf).
\]

The [[algebra-groups/commutator|commutator]] of two derivations is a derivation. Thus $[X,Y]$ is a [[fiber-bundles/vector-field|vector field]].

In local coordinates,
\[
[X,Y]
=
\sum_k\left(
\sum_i X^i\frac{\partial Y^k}{\partial x^i}
-
\sum_i Y^i\frac{\partial X^k}{\partial x^i}
\right)
\frac{\partial}{\partial x^k}.
\]
Coordinate [[fiber-bundles/vector-field|vector fields]] commute:
\[
\left[\frac{\partial}{\partial x^i},\frac{\partial}{\partial x^j}\right]=0.
\]

The bracket has these properties:
\[
\begin{aligned}
[X,Y]&=-[Y,X],\\
[aX+bY,Z]&=a[X,Z]+b[Y,Z],\\
[X,fY]&=f[X,Y]+(Xf)Y,\\
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]&=0.
\end{aligned}
\]
The last identity is the Jacobi identity.

Thus $\mathfrak X(M)$ is a [[lie-groups/lie-algebra|Lie algebra]] over $\mathbb{R}$. It is not a [[lie-groups/lie-algebra|Lie algebra]] over $C^\infty(M)$ because the bracket is not $C^\infty(M)$-linear.

### Related vector fields

Let $F:M\to N$ be smooth. [[fiber-bundles/vector-field|Vector fields]] $X\in\mathfrak X(M)$ and $Y\in\mathfrak X(N)$ are **$F$-related** if
\[
dF_p(X_p)=Y_{F(p)}
\]
for all $p$.

**Proposition (Naturality of the bracket).**
If $X_1$ is $F$-related to $Y_1$ and $X_2$ is $F$-related to $Y_2$, then $[X_1,X_2]$ is $F$-related to $[Y_1,Y_2]$.

*Proof.*
For $h\in C^\infty(N)$, the [[shared-foundations/relation|relation]] gives
\[
X_i(h\circ F)=(Y_ih)\circ F.
\]
Apply this identity twice and subtract.
 \(\square\)

If $F$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]], the pushforward field is
\[
F_*X=dF\circ X\circ F^{-1}.
\]
Then
\[
F_*[X,Y]=[F_*X,F_*Y].
\]

### Integral curves

**Definition.**
An **integral curve** of $X$ is a smooth [[topology/curve|curve]] $\gamma:I\to M$ such that
\[
\dot\gamma(t)=X_{\gamma(t)}.
\]

In coordinates, this equation is an ordinary differential equation:
\[
\dot x^i(t)=X^i(x(t)).
\]

**Theorem (Local integral curve).**
For each $p\in M$, there is a unique maximal integral [[topology/curve|curve]]
\[
\gamma_p:I_p\to M
\]
with $\gamma_p(0)=p$. The [[real-analysis/interval|interval]] $I_p$ is open and contains $0$.

The theorem follows from the Euclidean ODE theorem and uniqueness on chart overlaps.

### Flows

**Definition.**
A **local flow** of $X$ is a [[fiber-bundles/smooth-map|smooth map]]
\[
\Phi:D\to M,
\qquad
(t,p)\mapsto\Phi_t(p),
\]
where $D\subseteq\mathbb{R}\times M$ is open and contains $\left\{0\right\}\times M$, such that
\[
\Phi_0(p)=p,
\qquad
\frac{d}{dt}\Phi_t(p)=X_{\Phi_t(p)},
\]
and
\[
\Phi_{t+s}(p)=\Phi_t(\Phi_s(p))
\]
whenever both sides are defined.

The maximal integral [[topology/curve|curves]] define a unique maximal local flow. Each $\Phi_t$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]] between open [[shared-foundations/subset|subsets]], with inverse $\Phi_{-t}$.

A [[fiber-bundles/vector-field|vector field]] is **complete** if its flow is defined for all $(t,p)\in\mathbb{R}\times M$.

**Proposition.**
Each smooth [[fiber-bundles/vector-field|vector field]] on a compact manifold is complete.

*Proof.*[Proof outline]
A maximal integral [[topology/curve|curve]] can fail to extend only if it leaves each compact [[shared-foundations/subset|subset]] of a coordinate [[topology/neighborhood|neighborhood]]. On a compact manifold, finitely many coordinate [[topology/neighborhood|neighborhoods]] and uniform local existence times prevent this escape in finite time.
 \(\square\)

### The bracket from flows

Let $\Phi_t$ be the flow of $X$. Then
\[
[X,Y]
=
\left.\frac{d}{dt}\right|_{t=0}(\Phi_{-t})_*Y.
\]
The bracket [[measure-theory/measure|measures]] the first-order change of $Y$ under the flow of $X$.

The flows of $X$ and $Y$ commute locally if and only if $[X,Y]=0$.

### Distributions

**Definition.**
A **rank-$k$ smooth distribution** on $M$ assigns a $k$-dimensional subspace $D_p\subseteq T_pM$ to each $p$. Each point has a [[topology/neighborhood|neighborhood]] with smooth [[fiber-bundles/vector-field|vector fields]] $X_1,\ldots,X_k$ that form a basis of $D_q$ at every point $q$ in the [[topology/neighborhood|neighborhood]].

A connected [[differential-geometry/immersed-submanifold|immersed submanifold]] $S\subseteq M$ is an **integral manifold** of $D$ if
\[
T_pS=D_p
\]
for each $p\in S$.

A distribution is **involutive** if $[X,Y]$ takes values in $D$ whenever $X$ and $Y$ take values in $D$.

**Theorem (Frobenius theorem).**
A smooth constant-rank distribution is locally tangent to coordinate slices if and only if it is involutive. More precisely, for each $p$ there are local coordinates $(x^1,\ldots,x^n)$ such that
\[
D=\operatorname{span}\left(
\frac{\partial}{\partial x^1},\ldots,
\frac{\partial}{\partial x^k}
\right)
\]
if and only if $D$ is involutive.

The Frobenius theorem links the [[fiber-bundles/lie-bracket|Lie bracket]] with the existence of submanifolds.

### Parallelizable manifolds

**Definition.**
An $n$-manifold is **parallelizable** if it has [[fiber-bundles/vector-field|vector fields]] $E_1,\ldots,E_n$ that form a basis of $T_pM$ at every point.

Equivalently, the [[fiber-bundles/tangent-bundle|tangent bundle]] is isomorphic to the product $M\times\mathbb{R}^n$. Each coordinate [[shared-foundations/domain|domain]] is parallelizable. A global frame can fail to exist.

The sphere $S^2$ is not parallelizable. The hairy-ball theorem gives this result. Each [[fiber-bundles/lie-group|Lie group]] is parallelizable because [[lie-groups/left-translation|left translation]] moves a basis at the identity to every point.

### Exercises

**Exercise.**
Compute $[fX,gY]$ in terms of $f$, $g$, $X$, $Y$, and their [[real-analysis/derivative|derivatives]].

**Exercise.**
Let
\[
X=x\frac{\partial}{\partial y}-y\frac{\partial}{\partial x}
\]
on $\mathbb{R}^2$. Find its flow. Determine whether $X$ is complete.

**Exercise.**
Let
\[
X=x^2\frac{\partial}{\partial x}
\]
on $\mathbb{R}$. Find the maximal integral [[topology/curve|curve]] through $x_0$. Determine the points for which the [[topology/curve|curve]] has a finite endpoint.

**Exercise.**
Prove that a rank-one distribution is involutive.

**Exercise.**
Suppose that [[fiber-bundles/vector-field|vector fields]] $X_1,\ldots,X_k$ commute and are independent near $p$. Use their flows to construct local coordinates in which
\[
X_i=\frac{\partial}{\partial x^i}
\qquad
(1\leq i\leq k).
\]

 ## Tensor fields and [[fiber-bundles/differential-k-form|differential forms]]

**Required concepts.** Tangent and cotangent spaces, [[fiber-bundles/vector-field|vector fields]], [[algebra-category-theory/pullback|pullbacks]], and [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partitions of unity]].
**Result of this chapter.** The reader can compute tensor components, [[fiber-bundles/exterior-derivative|exterior derivatives]], [[algebra-category-theory/pullback|pullbacks]], [[fiber-bundles/lie-derivative|Lie derivatives]], and integrals of forms.

### Tensor spaces

Let $V$ be a finite-dimensional [[linear-algebra/vector-space|vector space]].

**Definition.**
A **tensor of type $(r,s)$** on $V$ is an element of
\[
V^{\otimes r}\otimes(V^*)^{\otimes s}.
\]
Equivalently, it is a multilinear map
\[
(V^*)^r\times V^s\to\mathbb{R}.
\]

A type $(1,0)$ tensor is a vector. A type $(0,1)$ tensor is a covector. A type $(1,1)$ tensor is an [[algebra-category-theory/endomorphism-category|endomorphism]]. A type $(0,2)$ tensor is a [[linear-algebra/bilinear-form|bilinear form]].

Let $(e_i)$ be a basis and let $(e^i)$ be its dual basis. A tensor has a unique expansion
\[
T=T^{i_1\cdots i_r}{}_{j_1\cdots j_s}
 e_{i_1}\otimes\cdots\otimes e_{i_r}
 \otimes e^{j_1}\otimes\cdots\otimes e^{j_s}.
\]
Repeated upper and lower indices are summed in this chapter and later chapters.

The tensor product combines types:
\[
(r,s)\otimes(r',s')=(r+r',s+s').
\]
A contraction pairs one vector factor with one covector factor. It lowers both $r$ and $s$ by one.

### Tensor fields

At each $p\in M$, define
\[
T^r_s(T_pM)=(T_pM)^{\otimes r}\otimes(T_p^*M)^{\otimes s}.
\]
The disjoint [[shared-foundations/union|union]] of these spaces is the tensor bundle $T^r_sM$.

**Definition.**
A **tensor field of type $(r,s)$** is a [[fiber-bundles/section-of-a-fiber-bundle|smooth section]] of $T^r_sM$.

In local coordinates,
\[
T=
T^{i_1\cdots i_r}{}_{j_1\cdots j_s}
\frac{\partial}{\partial x^{i_1}}\otimes\cdots\otimes
\frac{\partial}{\partial x^{i_r}}
\otimes dx^{j_1}\otimes\cdots\otimes dx^{j_s}.
\]
The field is smooth if and only if its component [[shared-foundations/function|functions]] are smooth.

A tensor field is $C^\infty(M)$-multilinear in its [[fiber-bundles/vector-field|vector-field]] and covector-field arguments. This property separates tensors from [[fiber-bundles/connection-on-a-vector-bundle|connections]] and [[fiber-bundles/lie-bracket|Lie brackets]].

### Symmetric and alternating tensors

A covariant $k$-tensor $T$ is **symmetric** if it is unchanged by each permutation of its arguments. It is **alternating** if
\[
T(v_{\sigma(1)},\ldots,v_{\sigma(k)})
=\operatorname{sgn}(\sigma)T(v_1,\ldots,v_k)
\]
for each permutation $\sigma$.

The space of alternating $k$-covectors is $\Lambda^kV^*$. Its dimension is $\binom nk$ when $\dim V=n$.

The alternating projection is
\[
\operatorname{Alt}(T)(v_1,\ldots,v_k)
=
\frac{1}{k!}\sum_{\sigma\in S_k}
\operatorname{sgn}(\sigma)T(v_{\sigma(1)},\ldots,v_{\sigma(k)}).
\]

### Differential forms

**Definition.**
A [[fiber-bundles/differential-k-form|differential $k$-form]] on $M$ is a [[fiber-bundles/section-of-a-fiber-bundle|smooth section]] of $\Lambda^kT^*M$. The space of $k$-forms is $\Omega^k(M)$.

A zero-form is a [[fiber-bundles/smooth-map|smooth function]]. In coordinates,
\[
\omega=\frac{1}{k!}\omega_{i_1\cdots i_k}
 dx^{i_1}\wedge\cdots\wedge dx^{i_k}.
\]

The wedge product of $\alpha\in\Omega^k(M)$ and $\beta\in\Omega^\ell(M)$ is
\[
\alpha\wedge\beta
=
\frac{(k+\ell)!}{k!\ell!}\operatorname{Alt}(\alpha\otimes\beta).
\]
It satisfies
\[
\alpha\wedge\beta=(-1)^{k\ell}\beta\wedge\alpha.
\]
For one-forms,
\[
(\alpha\wedge\beta)(v,w)
=\alpha(v)\beta(w)-\alpha(w)\beta(v).
\]

### Pullback of tensors and forms

Let $F:M\to N$ be smooth. A covariant tensor $T$ on $N$ has [[algebra-category-theory/pullback|pullback]]
\[
(F^*T)_p(v_1,\ldots,v_s)
=
T_{F(p)}(dF_pv_1,\ldots,dF_pv_s).
\]
This definition applies to [[fiber-bundles/differential-k-form|differential forms]].

[[algebra-category-theory/pullback|Pullback]] satisfies
\[
(G\circ F)^*=F^*\circ G^*,
\qquad
F^*(\alpha\wedge\beta)=F^*\alpha\wedge F^*\beta,
\qquad
F^*f=f\circ F.
\]

A general tensor with contravariant factors does not have a [[algebra-category-theory/pullback|pullback]] by an arbitrary [[fiber-bundles/smooth-map|smooth map]]. A [[fiber-bundles/diffeomorphism|diffeomorphism]] can transport all tensor types.

### Exterior derivative

**Theorem.**
There is a unique [[shared-foundations/sequence|sequence]] of [[linear-algebra/linear-map|linear maps]]
\[
d:\Omega^k(M)\to\Omega^{k+1}(M)
\]
with these properties:

1. For $f\in C^\infty(M)$, the one-form $df$ is the differential of $f$.
1. For $\alpha\in\Omega^k(M)$,
\[
d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^k\alpha\wedge d\beta.
\]
1. $d\circ d=0$.

In coordinates,
\[
\omega=
\sum_{i_1<\cdots<i_k}
\omega_{i_1\cdots i_k}
 dx^{i_1}\wedge\cdots\wedge dx^{i_k}
\]
gives
\[
d\omega=
\sum_{i_1<\cdots<i_k}\sum_j
\frac{\partial\omega_{i_1\cdots i_k}}{\partial x^j}
 dx^j\wedge dx^{i_1}\wedge\cdots\wedge dx^{i_k}.
\]
The identity $d^2=0$ follows from equality of [[real-analysis/mixed-partial-derivative|mixed partial derivatives]] and antisymmetry of the wedge product.

**Proposition (Naturality).**
For each [[fiber-bundles/smooth-map|smooth map]] $F:M\to N$,
\[
F^*(d\omega)=d(F^*\omega).
\]

*Proof.*[Proof outline]
The identity holds for [[shared-foundations/function|functions]] by the [[real-analysis/chain-rule|chain rule]]. The graded product rule extends it to coordinate forms. Locality gives the global statement.
 \(\square\)

A form is [[fiber-bundles/closed-differential-form|closed]] if $d\omega=0$. It is [[fiber-bundles/exact-differential-form|exact]] if $\omega=d\eta$. Each exact form is closed.

**Theorem (Poincaré lemma).**
Each closed $k$-form on a star-shaped open [[shared-foundations/subset|subset]] of $\mathbb{R}^n$ is exact when $k\geq 1$.

The quotient
\[
H^k_{\mathrm{dR}}(M)
=
\frac{\operatorname{ker}(d:\Omega^k\to\Omega^{k+1})}
{\operatorname{im}(d:\Omega^{k-1}\to\Omega^k)}
\]
is the $k$th [[fiber-bundles/de-rham-cohomology-group|de Rham cohomology group]].

### Interior product and Lie derivative

For $X\in\mathfrak X(M)$, define the [[fiber-bundles/interior-product|interior product]]
\[
\iota_X:\Omega^k(M)\to\Omega^{k-1}(M)
\]
by
\[
(\iota_X\omega)(X_2,\ldots,X_k)
=\omega(X,X_2,\ldots,X_k).
\]

Let $\Phi_t$ be the local flow of $X$.

**Definition.**
The [[fiber-bundles/lie-derivative|Lie derivative]] of a covariant tensor field $T$ along $X$ is
\[
\mathcal{L}_XT=\left.\frac{d}{dt}\right|_{t=0}\Phi_t^*T.
\]
The equivalent transport definition applies to all tensor types.

For [[shared-foundations/function|functions]], $\mathcal{L}_Xf=Xf$. For [[fiber-bundles/vector-field|vector fields]], $\mathcal{L}_XY=[X,Y]$.

**Theorem (Cartan formula).**
For each [[fiber-bundles/differential-k-form|differential form]] $\omega$,
\[
\mathcal{L}_X\omega=d(\iota_X\omega)+\iota_X(d\omega).
\]

This formula expresses infinitesimal flow change through the [[fiber-bundles/exterior-derivative|exterior derivative]].

### Orientation

An ordered basis of an $n$-dimensional [[linear-algebra/vector-space|vector space]] has one of two [[differential-geometry/orientation-of-a-smooth-manifold|orientations]]. Two ordered bases have the same [[differential-geometry/orientation-of-a-smooth-manifold|orientation]] when the change-of-basis [[linear-algebra/determinant|determinant]] is positive.

**Definition.**
An [[differential-geometry/orientation-of-a-smooth-manifold|orientation]] on an $n$-manifold is a smooth choice of [[differential-geometry/orientation-of-a-smooth-manifold|orientation]] on each $T_pM$. Equivalently, it is an atlas whose transition maps have positive [[real-analysis/jacobian-determinant|Jacobian determinant]].

**Theorem.**
An $n$-manifold is orientable if and only if it has a nowhere-zero $n$-form.

*Proof.*[Proof outline]
A nowhere-zero top form selects the bases on which it is positive. Conversely, choose positive local coordinate forms. Use a [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]] to combine them. Positivity prevents cancellation.
 \(\square\)

A connected [[differential-geometry/orientability-of-a-smooth-manifold|orientable manifold]] has exactly two [[differential-geometry/orientation-of-a-smooth-manifold|orientations]].

### Integration of forms

Let $M$ be an oriented $n$-manifold. Let $\omega\in\Omega^n(M)$ have compact support. Choose an oriented atlas and a [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]] $\{\rho_i\}$ subordinate to it. Define
\[
\int_M\omega
=
\sum_i\int_{x_i(U_i)}(x_i^{-1})^*(\rho_i\omega).
\]
The change-of-variables theorem shows that this number is independent of the atlas and partition.

If $F:M\to N$ is an orientation-preserving [[fiber-bundles/diffeomorphism|diffeomorphism]], then
\[
\int_MF^*\omega=\int_N\omega.
\]
An orientation-reversing [[fiber-bundles/diffeomorphism|diffeomorphism]] gives a minus sign.

### Stokes' theorem

Let $M$ be an oriented [[differential-geometry/manifold-with-boundary|manifold with boundary]]. Give $\partial M$ the outward-normal-first [[differential-geometry/orientation-of-a-smooth-manifold|orientation]].

**Theorem (Stokes).**
Let $M$ be an oriented $n$-manifold with [[topology/boundary|boundary]]. Let $\omega\in\Omega^{n-1}(M)$ have compact support. Then
\[
\int_Md\omega=\int_{\partial M}\omega.
\]

For $n=1$, this is the fundamental theorem of calculus. In Euclidean vector calculus, it contains the divergence theorem and the classical Stokes theorem.

### Exercises

**Exercise.**
Prove that $dx^i\wedge dx^i=0$. Compute
\[
(dx^1+dx^2)\wedge(dx^1-dx^2).
\]

**Exercise.**
Let
\[
\omega=x\,dy-y\,dx
\]
on $\mathbb{R}^2$. Compute $d\omega$. Compute the integral of $\omega$ around the unit circle with counterclockwise [[differential-geometry/orientation-of-a-smooth-manifold|orientation]].

**Exercise.**
Prove that $d(F^*f)=F^*(df)$ directly from the definition of the differential.

**Exercise.**
Use Cartan's formula to prove that $\mathcal{L}_X$ commutes with $d$.

**Exercise.**
Let $\omega$ be a nowhere-zero top form. Prove that $f\omega$ gives the same [[differential-geometry/orientation-of-a-smooth-manifold|orientation]] exactly when $f>0$.

# Part: Bundles and Lie Groups
## Fiber bundles and vector bundles

**Required concepts.** [[fiber-bundles/smooth-manifold|Smooth manifolds]], products, [[fiber-bundles/smooth-map|smooth maps]], [[fiber-bundles/tangent-bundle|tangent bundles]], and [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partitions of unity]].
**Result of this chapter.** The reader can use [[fiber-bundles/local-trivialization|local trivializations]], [[fiber-bundles/transition-function|transition functions]], sections, [[algebra-category-theory/pullback|pullbacks]], and [[fiber-bundles/vector-bundle|vector-bundle]] operations.

### Fiber bundles

**Definition.**
A [[fiber-bundles/smooth-fiber-bundle|smooth fiber bundle]] with [[fiber-bundles/typical-fiber|typical fiber]] $F$ consists of [[fiber-bundles/smooth-manifold|smooth manifolds]] $E$ and $B$, a [[shared-foundations/surjective-function|surjective]] [[fiber-bundles/smooth-map|smooth map]]
\[
\pi:E\to B,
\]
and an [[topology/open-cover|open cover]] $\{U_\alpha\}$ of $B$. For each $\alpha$, there is a [[fiber-bundles/diffeomorphism|diffeomorphism]]
\[
\Phi_\alpha:\pi^{-1}(U_\alpha)\to U_\alpha\times F
\]
that satisfies
\[
\operatorname{pr}_1\circ\Phi_\alpha=\pi.
\]
The manifold $E$ is the total space. The manifold $B$ is the base. The [[shared-foundations/set|set]] $E_b=\pi^{-1}(b)$ is the fiber over $b$.

The map $\Phi_\alpha$ is a [[fiber-bundles/local-trivialization|local trivialization]]. It identifies each fiber over $U_\alpha$ with $F$.

On $U_\alpha\cap U_\beta$, the transition map has the form
\[
\Phi_\alpha\circ\Phi_\beta^{-1}(b,f)
=(b,g_{\alpha\beta}(b)(f)),
\]
where $g_{\alpha\beta}(b)$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]] of $F$. The transition maps satisfy
\[
g_{\alpha\alpha}=\operatorname{id},
\qquad
g_{\alpha\beta}=g_{\beta\alpha}^{-1},
\qquad
g_{\alpha\beta}g_{\beta\gamma}=g_{\alpha\gamma}.
\]
The last identity is the cocycle identity.

A bundle is [[fiber-bundles/local-trivialization|trivial]] if it is isomorphic to $B\times F\to B$.

**Example.**
The projection $M\times F\to M$ is a trivial bundle. The [[fiber-bundles/tangent-bundle|tangent bundle]] $TM\to M$ is locally trivial with fiber $\mathbb{R}^n$.

### Sections and bundle maps

**Definition.**
A [[fiber-bundles/section-of-a-fiber-bundle|section]] of $\pi:E\to B$ is a [[fiber-bundles/smooth-map|smooth map]] $s:B\to E$ such that
\[
\pi\circ s=\operatorname{id}_B.
\]

A section selects one point in each fiber. A local section is defined on an open [[shared-foundations/subset|subset]] of the base.

**Definition.**
A [[fiber-bundles/bundle-map|bundle map]] from $E\to B$ to $E'\to B'$ is a pair $(F,f)$ of [[fiber-bundles/smooth-map|smooth maps]] such that
\[
\pi'\circ F=f\circ\pi.
\]
The map $F$ sends the fiber over $b$ to the fiber over $f(b)$.

A [[fiber-bundles/bundle-isomorphism|bundle isomorphism]] is a [[fiber-bundles/bundle-map|bundle map]] with [[fiber-bundles/diffeomorphism|diffeomorphisms]] on total and base spaces. A [[fiber-bundles/bundle-map|bundle map]] over the identity has $f=\operatorname{id}_B$.

### Vector bundles

**Definition.**
A [[fiber-bundles/vector-bundle|smooth vector bundle of rank $k$]] is a [[fiber-bundles/smooth-fiber-bundle|smooth fiber bundle]] $\pi:E\to B$ with [[fiber-bundles/typical-fiber|typical fiber]] $\mathbb{R}^k$. Each fiber $E_b$ is a [[linear-algebra/vector-space|vector space]]. Each [[fiber-bundles/local-trivialization|local trivialization]] restricts to a linear [[algebra-category-theory/isomorphism-category|isomorphism]]
\[
E_b\to\left\{b\right\}\times\mathbb{R}^k.
\]

The [[fiber-bundles/transition-function|transition functions]] of a [[fiber-bundles/vector-bundle|vector bundle]] take values in $\operatorname{GL}(k,\mathbb{R})$:
\[
\Phi_\alpha\circ\Phi_\beta^{-1}(b,v)
=(b,g_{\alpha\beta}(b)v).
\]
The map $g_{\alpha\beta}:U_\alpha\cap U_\beta\to\operatorname{GL}(k,\mathbb{R})$ is smooth.

A [[fiber-bundles/vector-bundle|vector-bundle]] map is fiberwise linear. The zero vectors define the [[fiber-bundles/zero-section|zero section]].

The [[shared-foundations/set|set]] of [[fiber-bundles/section-of-a-fiber-bundle|smooth sections]] is denoted by $\Gamma(E)$. It is a [[algebra-modules/module|module]] over $C^\infty(B)$:
\[
(fs)(b)=f(b)s(b).
\]

### Local frames

**Definition.**
A [[fiber-bundles/local-frame-of-a-vector-bundle|local frame]] of a rank-$k$ [[fiber-bundles/vector-bundle|vector bundle]] on $U$ is a list of sections $e_1,\ldots,e_k\in\Gamma(\left.E\right|_{U})$ such that $(e_1(b),\ldots,e_k(b))$ is a basis of $E_b$ for each $b\in U$.

A [[fiber-bundles/local-trivialization|local trivialization]] gives a local frame. A local frame gives a [[fiber-bundles/local-trivialization|local trivialization]] by
\[
(b,(v^1,\ldots,v^k))
\mapsto
v^ae_a(b).
\]

**Proposition.**
A rank-$k$ [[fiber-bundles/vector-bundle|vector bundle]] is trivial if and only if it has a global frame of $k$ sections.

*Proof.*
A trivialization pulls back the standard basis of $\mathbb{R}^k$ to a global frame. Conversely, a global frame defines the displayed fiberwise [[linear-algebra/linear-map|linear map]] $B\times\mathbb{R}^k\to E$. It is a [[fiber-bundles/bundle-isomorphism|bundle isomorphism]].
 \(\square\)

Thus a manifold is parallelizable if and only if its [[fiber-bundles/tangent-bundle|tangent bundle]] is trivial.

### Transition-function construction

Let $\{U_\alpha\}$ [[topology/cover|cover]] $B$. Suppose that [[fiber-bundles/smooth-map|smooth maps]]
\[
g_{\alpha\beta}:U_\alpha\cap U_\beta\to\operatorname{GL}(k,\mathbb{R})
\]
satisfy the cocycle identities. Form the disjoint [[shared-foundations/union|union]]
\[
\coprod_\alpha U_\alpha\times\mathbb{R}^k.
\]
Impose the [[shared-foundations/relation|relation]]
\[
(b,v)_\beta\sim(b,g_{\alpha\beta}(b)v)_\alpha.
\]
The quotient has a [[fiber-bundles/vector-bundle|vector-bundle]] structure. Thus [[fiber-bundles/transition-function|transition functions]] can define a bundle.

Changing [[fiber-bundles/local-trivialization|local trivializations]] changes $g_{\alpha\beta}$ by
\[
g'_{\alpha\beta}
=h_\alpha g_{\alpha\beta}h_\beta^{-1},
\]
where $h_\alpha:U_\alpha\to\operatorname{GL}(k,\mathbb{R})$. This is a change of local frame.

### The pullback bundle

Let $\pi:E\to B$ be a [[fiber-bundles/vector-bundle|vector bundle]] and let $f:X\to B$ be smooth. Define
\[
f^*E=
\left\{(x,e)\in X\times E:f(x)=\pi(e)\right\}.
\]
The projection is $(x,e)\mapsto x$. Its fiber over $x$ is naturally $E_{f(x)}$.

**Definition.**
The bundle $f^*E\to X$ is the [[fiber-bundles/pullback-bundle|pullback bundle]].

A section $s$ of $E$ pulls back to the section
\[
f^*s(x)=(x,s(f(x))).
\]

The [[fiber-bundles/pullback-bundle|pullback bundle]] has this universal property. If $F:E'\to E$ is a [[fiber-bundles/bundle-map|bundle map]] over $f:X\to B$, then there is a unique [[fiber-bundles/bundle-map|bundle map]] $E'\to f^*E$ over $\operatorname{id}_X$ whose composite with the natural map $f^*E\to E$ is $F$.

### Vector-bundle operations

Let $E$ and $F$ be [[fiber-bundles/vector-bundle|vector bundles]] over the same base $B$.

The direct sum has fibers
\[
(E\oplus F)_b=E_b\oplus F_b.
\]
The tensor product has fibers
\[
(E\otimes F)_b=E_b\otimes F_b.
\]
The dual bundle has fibers
\[
(E^*)_b=(E_b)^*.
\]
The homomorphism bundle has fibers
\[
\operatorname{Hom}(E,F)_b=\operatorname{Hom}(E_b,F_b).
\]
Exterior and symmetric powers have fibers $\Lambda^kE_b$ and $\operatorname{Sym}^kE_b$.

The tangent tensor bundles satisfy
\[
T^r_sM=(TM)^{\otimes r}\otimes(T^*M)^{\otimes s}.
\]
[[fiber-bundles/differential-k-form|Differential forms]] are sections of $\Lambda^kT^*M$.

### Subbundles and quotient bundles

**Definition.**
A [[fiber-bundles/vector-subbundle|vector subbundle]] $F\subseteq E$ has a vector subspace $F_b\subseteq E_b$ in each fiber and has local frames that extend to local frames of $E$.

The [[linear-algebra/rank|rank]] must be locally constant. A pointwise family of subspaces with nonconstant dimension is not a [[fiber-bundles/vector-subbundle|vector subbundle]].

If $F\subseteq E$ is a subbundle, then the quotient fibers $E_b/F_b$ form a [[fiber-bundles/quotient-vector-bundle|quotient vector bundle]] $E/F$.

A constant-rank [[fiber-bundles/bundle-map|bundle map]] $A:E\to F$ has kernel and [[shared-foundations/image|image]] subbundles. A variable-rank map need not have a kernel or [[fiber-bundles/kernel-and-image-bundles-of-a-constant-rank-morphism|image bundle]] of constant [[linear-algebra/rank|rank]].

### Bundle metrics

**Definition.**
A [[fiber-bundles/bundle-metric|bundle metric]] on a real [[fiber-bundles/vector-bundle|vector bundle]] $E\to B$ is a smooth choice of [[linear-algebra/inner-product|inner product]] $h_b$ on each fiber $E_b$.

**Theorem.**
Each real [[fiber-bundles/vector-bundle|vector bundle]] over a [[fiber-bundles/smooth-manifold|smooth manifold]] has a [[fiber-bundles/bundle-metric|bundle metric]].

*Proof.*
Choose [[fiber-bundles/local-trivialization|local trivializations]]. Give each local product bundle the standard Euclidean [[linear-algebra/inner-product|inner product]]. Let $\{\rho_\alpha\}$ be a [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]] subordinate to the trivializing [[topology/cover|cover]]. Define
\[
h_b(v,w)=\sum_\alpha\rho_\alpha(b)h^{(\alpha)}_b(v,w).
\]
The sum is locally finite. It is smooth and symmetric. For $v\neq 0$, each term is nonnegative and at least one term with positive coefficient is positive. Thus $h_b(v,v)>0$.
 \(\square\)

A [[fiber-bundles/bundle-metric|bundle metric]] gives an [[linear-algebra/orthogonal-complement|orthogonal complement]] $F^\perp$ to each [[fiber-bundles/vector-subbundle|vector subbundle]] $F\subseteq E$. Then
\[
E=F\oplus F^\perp.
\]

### The Möbius line bundle

Start with $[0,1]\times\mathbb{R}$. Identify
\[
(0,v)\sim(1,-v).
\]
The quotient is a [[fiber-bundles/line-bundle|line bundle]] over $S^1=[0,1]/(0\sim1)$. It is the **Möbius line bundle**.

This bundle is not trivial. A nonzero [[fiber-bundles/section-of-a-fiber-bundle|global section]] would have a continuous scalar representative $s:[0,1]\to\mathbb{R}\setminus\left\{0\right\}$ with $s(1)=-s(0)$. The [[real-analysis/intermediate-value-theorem|intermediate value theorem]] forces a zero.

The direct sum of two Möbius [[fiber-bundles/line-bundle|line bundles]] is trivial. The transition [[linear-algebra/matrix|matrix]] is $-I_2$, which can be connected to $I_2$ in $\operatorname{GL}^+(2,\mathbb{R})$.

### Exact sequences and splittings

A [[shared-foundations/sequence|sequence]] of [[fiber-bundles/vector-bundle|vector bundles]]
\[
0\to E'\xrightarrow{i}E\xrightarrow{q}E”\to0
\]
is [[fiber-bundles/exact-differential-form|exact]] if it is exact on each fiber. A [[fiber-bundles/bundle-metric|bundle metric]] on $E$ gives a splitting. The [[linear-algebra/orthogonal-complement|orthogonal complement]] of $i(E')$ maps isomorphically to $E”$.

Thus each [[algebra-modules/short-exact-sequence|short exact sequence]] of smooth real [[fiber-bundles/vector-bundle|vector bundles]] over a manifold splits. The splitting is not canonical.

### Exercises

**Exercise.**
Prove that the [[fiber-bundles/tangent-bundle|tangent bundle]] [[fiber-bundles/transition-function|transition functions]] are the Jacobian matrices of chart transitions.

**Exercise.**
Let $L\to B$ be a [[fiber-bundles/line-bundle|real line bundle]]. Prove that $L$ is trivial if and only if it has a [[fiber-bundles/nowhere-vanishing-section|nowhere-zero section]].

**Exercise.**
Prove that $f^*(E\oplus F)$ is isomorphic to $f^*E\oplus f^*F$.

**Exercise.**
Let $S\subseteq M$ be an [[differential-geometry/embedded-submanifold|embedded submanifold]]. Prove that $TS$ is a [[fiber-bundles/vector-subbundle|vector subbundle]] of $\left.TM\right|_{S}$.

**Exercise.**
Use a [[fiber-bundles/bundle-metric|bundle metric]] to prove that every [[fiber-bundles/vector-subbundle|vector subbundle]] has a complementary subbundle.

 ## [[fiber-bundles/lie-group|Lie groups]] and [[lie-groups/lie-algebra|Lie algebras]]

**Required concepts.** [[algebra-groups/group|Groups]], [[fiber-bundles/smooth-manifold|smooth manifolds]], differentials, [[fiber-bundles/vector-field|vector fields]], flows, and [[differential-geometry/embedded-submanifold|embedded submanifolds]].
**Result of this chapter.** The reader can pass between a [[fiber-bundles/lie-group|Lie group]] and its tangent [[lie-groups/lie-algebra|Lie algebra]], use the [[fiber-bundles/exponential-map|exponential map]], and identify standard [[linear-algebra/matrix|matrix]] [[fiber-bundles/lie-group|Lie groups]].

### Lie groups

**Definition.**
A [[fiber-bundles/lie-group|Lie group]] is a [[fiber-bundles/smooth-manifold|smooth manifold]] $G$ with a [[algebra-groups/group|group]] structure such that multiplication
\[
m:G\times G\to G,
\qquad
m(g,h)=gh,
\]
and inversion
\[
i:G\to G,
\qquad
i(g)=g^{-1},
\]
are smooth.

A [[fiber-bundles/lie-group|Lie group]] is a [[algebra-groups/group|group]] [[algebra-category-theory/object|object]] in the [[differential-geometry/category-of-smooth-manifolds|category of smooth manifolds]].

For $g\in G$, define left and [[lie-groups/right-translation|right translations]]
\[
L_g(h)=gh,
\qquad
R_g(h)=hg.
\]
They are [[fiber-bundles/diffeomorphism|diffeomorphisms]]. Their inverses are $L_{g^{-1}}$ and $R_{g^{-1}}$.

**Example.**
The additive [[algebra-groups/group|group]] $\mathbb{R}^n$ is a [[fiber-bundles/lie-group|Lie group]]. The torus $T^n=\mathbb{R}^n/\mathbb{Z}^n$ is a compact [[lie-groups/abelian-lie-group|abelian Lie group]].

**Example.**
The [[algebra-groups/group|group]] $\operatorname{GL}(n,\mathbb{R})$ is an open submanifold of $M_n(\mathbb{R})$. [[linear-algebra/matrix|Matrix]] multiplication is [[real-analysis/polynomial|polynomial]]. Inversion is smooth because
\[
A^{-1}=\frac{1}{\det A}\operatorname{adj}(A).
\]
Thus $\operatorname{GL}(n,\mathbb{R})$ is a [[fiber-bundles/lie-group|Lie group]] of dimension $n^2$.

**Example.**
The [[algebra-groups/group|groups]] $\operatorname{SL}(n,\mathbb{R})$, $\mathrm O(n)$, $\operatorname{SO}(n)$, $\mathrm U(n)$, and $\mathrm{SU}(n)$ are [[fiber-bundles/lie-group|Lie groups]]. They are [[differential-geometry/embedded-submanifold|embedded submanifolds]] of [[linear-algebra/matrix|matrix]] spaces.

A zero-dimensional [[fiber-bundles/lie-group|Lie group]] is discrete. Under the second-countability convention, its underlying [[shared-foundations/set|set]] is countable.

### Left-invariant vector fields

**Definition.**
A [[fiber-bundles/vector-field|vector field]] $X$ on $G$ is [[lie-groups/left-invariant-vector-field|left invariant]] if
\[
(L_g)_*X=X
\]
for each $g\in G$. Equivalently,
\[
d(L_g)_hX_h=X_{gh}.
\]

Let $e$ be the identity. Each $v\in T_eG$ gives a left-invariant field
\[
X^v_g=d(L_g)_e(v).
\]
Each left-invariant field has this form. Thus evaluation at $e$ is a [[linear-algebra/vector-space|vector-space]] [[algebra-category-theory/isomorphism-category|isomorphism]]
\[
\left\{\text{left-invariant vector fields}\right\}\cong T_eG.
\]

The bracket of left-invariant fields is left invariant because the bracket is natural under [[fiber-bundles/diffeomorphism|diffeomorphisms]].

**Definition.**
The [[lie-groups/lie-algebra|Lie algebra of $G$]] is the [[linear-algebra/vector-space|vector space]]
\[
\mathfrak g=T_eG
\]
with bracket
\[
[u,v]=[X^u,X^v]_e.
\]

This bracket is bilinear, antisymmetric, and satisfies the Jacobi identity.

**Proposition.**
Each [[fiber-bundles/lie-group|Lie group]] is parallelizable.

*Proof.*
Choose a basis $(e_1,\ldots,e_n)$ of $T_eG$. Extend each basis vector by [[lie-groups/left-translation|left translation]]. The resulting left-invariant fields form a basis at every point.
 \(\square\)

Thus parallelizability is a necessary condition for a manifold to have a [[fiber-bundles/lie-group|Lie group]] structure. It is not sufficient.

### Matrix Lie algebras

For $G=\operatorname{GL}(n,\mathbb{R})$,
\[
\mathfrak{gl}(n,\mathbb{R})=M_n(\mathbb{R}).
\]
The bracket is the [[linear-algebra/matrix|matrix]] [[algebra-groups/commutator|commutator]]
\[
[X,Y]=XY-YX.
\]

For standard [[linear-algebra/matrix|matrix]] [[algebra-groups/group|groups]],
\[
\begin{aligned}
\mathfrak{sl}(n,\mathbb{R})&=\left\{X:\operatorname{tr} X=0\right\},\\
\mathfrak o(n)&=\left\{X:X^{\mathsf T}+X=0\right\},\\
\mathfrak{so}(n)&=\mathfrak o(n),\\
\mathfrak u(n)&=\left\{X:X^*+X=0\right\},\\
\mathfrak{su}(n)&=\left\{X:X^*+X=0,\ \operatorname{tr} X=0\right\}.
\end{aligned}
\]

For example, differentiate $A(t)^{\mathsf T}A(t)=I$ at $t=0$ and $A(0)=I$. This gives $X^{\mathsf T}+X=0$.

### One-parameter subgroups and the exponential map

**Definition.**
A [[lie-groups/one-parameter-subgroup|one-parameter subgroup]] is a smooth homomorphism
\[
\gamma:(\mathbb{R},+)\to G.
\]

It satisfies
\[
\gamma(t+s)=\gamma(t)\gamma(s).
\]
Its velocity is the left-invariant field determined by $\dot\gamma(0)$.

**Theorem.**
For each $X\in\mathfrak g$, there is a unique [[lie-groups/one-parameter-subgroup|one-parameter subgroup]] $\gamma_X$ such that
\[
\dot\gamma_X(0)=X.
\]

*Proof.*
Let $X^L$ be the left-invariant field determined by $X$. Its maximal integral [[topology/curve|curve]] through $e$ satisfies the local [[algebra-groups/group|group]] law by uniqueness. [[lie-groups/left-translation|Left translation]] extends the [[topology/curve|curve]] for all time. Thus $X^L$ is complete. The resulting [[topology/curve|curve]] is a homomorphism. Uniqueness follows from ODE uniqueness.
 \(\square\)

**Definition.**
The [[fiber-bundles/exponential-map|Lie exponential map]] is
\[
\exp_G:\mathfrak g\to G,
\qquad
\exp_G(X)=\gamma_X(1).
\]

It satisfies
\[
\gamma_X(t)=\exp_G(tX),
\qquad
\exp_G((s+t)X)=\exp_G(sX)\exp_G(tX).
\]

For a [[linear-algebra/matrix|matrix]] [[fiber-bundles/lie-group|Lie group]], $\exp_G$ is the [[linear-algebra/matrix|matrix]] exponential
\[
\exp X=\sum_{k=0}^{\infty}\frac{X^k}{k!}.
\]

**Proposition.**
The differential of $\exp_G$ at $0$ is the identity on $\mathfrak g$. Thus $\exp_G$ is a [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphism]] near $0$.

*Proof.*
For $X\in\mathfrak g$,
\[
d(\exp_G)_0(X)
=
\left.\frac{d}{dt}\right|_{t=0}\exp_G(tX)
=X.
\]
Apply the [[shared-foundations/inverse-function|inverse function]] theorem.
 \(\square\)

The [[fiber-bundles/exponential-map|exponential map]] need not be [[shared-foundations/surjective-function|surjective]]. It is [[shared-foundations/surjective-function|surjective]] for compact connected [[lie-groups/abelian-lie-group|abelian Lie groups]]. It is not [[shared-foundations/surjective-function|surjective]] for $\operatorname{SL}(2,\mathbb{R})$.

### Lie group homomorphisms

**Definition.**
A [[lie-groups/lie-group-homomorphism|Lie group homomorphism]] is a smooth [[algebra-groups/group-homomorphism|group homomorphism]] $\Phi:G\to H$.

Its [[real-analysis/derivative|derivative]] at the identity is
\[
d\Phi_e:\mathfrak g\to\mathfrak h.
\]

**Theorem.**
The [[real-analysis/derivative|derivative]] $d\Phi_e$ is a [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]]:
\[
d\Phi_e[X,Y]=[d\Phi_eX,d\Phi_eY].
\]
It also satisfies
\[
\Phi(\exp_GX)=\exp_H(d\Phi_eX).
\]

*Proof.*
Left-invariant fields determined by $X$ and $d\Phi_eX$ are $\Phi$-related. Naturality of the bracket gives the first identity. The [[shared-foundations/image|image]] under $\Phi$ of the [[lie-groups/one-parameter-subgroup|one-parameter subgroup]] generated by $X$ and the [[lie-groups/one-parameter-subgroup|one-parameter subgroup]] generated by $d\Phi_eX$ have the same initial velocity. Uniqueness gives the second identity.
 \(\square\)

A continuous homomorphism between finite-dimensional [[fiber-bundles/lie-group|Lie groups]] is smooth.

### Adjoint representations

For $g\in G$, conjugation is
\[
C_g(h)=ghg^{-1}.
\]
Its differential at $e$ is
\[
\operatorname{Ad}_g=d(C_g)_e:\mathfrak g\to\mathfrak g.
\]
The map
\[
\operatorname{Ad}:G\to\operatorname{GL}(\mathfrak g)
\]
is a [[lie-groups/lie-group-homomorphism|Lie group homomorphism]].

Differentiate $\operatorname{Ad}$ at $e$. This gives
\[
\operatorname{ad}:\mathfrak g\to\mathfrak{gl}(\mathfrak g).
\]

**Theorem.**
For $X,Y\in\mathfrak g$,
\[
\operatorname{ad}_XY=[X,Y].
\]
Also,
\[
\operatorname{Ad}_{\exp X}=\exp(\operatorname{ad}_X).
\]

For a [[linear-algebra/matrix|matrix]] [[algebra-groups/group|group]],
\[
\operatorname{Ad}_gX=gXg^{-1}.
\]

### The Maurer--Cartan form

Define the left Maurer--Cartan form
\[
\theta\in\Omega^1(G;\mathfrak g)
\]
by
\[
\theta_g=d(L_{g^{-1}})_g:T_gG\to T_eG=\mathfrak g.
\]
It converts [[fiber-bundles/tangent-space-at-a-point|tangent vectors]] to their left-translated identity components.

The form is left invariant:
\[
L_g^*\theta=\theta.
\]
It reproduces left-invariant fields:
\[
\theta(X^v)=v.
\]

**Theorem (Maurer--Cartan equation).**
\[
d\theta+\frac12[\theta,\theta]=0.
\]

Here the bracket combines the wedge product of forms with the [[fiber-bundles/lie-bracket|Lie bracket]] of $\mathfrak g$. On [[fiber-bundles/vector-field|vector fields]] $X,Y$,
\[
[\theta,\theta](X,Y)=2[\theta(X),\theta(Y)].
\]
The Maurer--Cartan equation encodes the [[fiber-bundles/lie-bracket|Lie bracket]] in differential-form language.

### Lie subgroups

**Definition.**
A [[lie-groups/lie-subgroup|Lie subgroup]] $H\subseteq G$ is a [[algebra-groups/subgroup|subgroup]] that is also an [[differential-geometry/immersed-submanifold|immersed submanifold]]. Its inclusion is an [[shared-foundations/injective-function|injective]] immersion and a [[lie-groups/lie-group-homomorphism|Lie group homomorphism]].

**Theorem (Closed subgroup theorem).**
Each closed [[algebra-groups/subgroup|subgroup]] of a finite-dimensional [[fiber-bundles/lie-group|Lie group]] is an embedded [[lie-groups/lie-subgroup|Lie subgroup]].

This theorem is a major input. It makes quotients $G/H$ into manifolds when $H$ is closed.

The [[lie-groups/lie-algebra|Lie algebra]] $\mathfrak h$ of a [[lie-groups/lie-subgroup|Lie subgroup]] is a [[lie-groups/lie-subalgebra|Lie subalgebra]] of $\mathfrak g$. For a closed [[algebra-groups/subgroup|subgroup]],
\[
\mathfrak h
=
\left\{X\in\mathfrak g:\exp(tX)\in H\text{ for all }t\in\mathbb{R}\right\}.
\]

### Lie's fundamental existence statements

The following results connect [[fiber-bundles/lie-group|Lie groups]] and [[lie-groups/lie-algebra|Lie algebras]].

**Theorem (Integration of homomorphisms).**
Let $G$ be connected and simply connected. Each [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]]
\[
\varphi:\mathfrak g\to\mathfrak h
\]
integrates to a unique [[lie-groups/lie-group-homomorphism|Lie group homomorphism]] $\Phi:G\to H$ with $d\Phi_e=\varphi$.

**Theorem (Lie's third theorem).**
Each finite-dimensional real [[lie-groups/lie-algebra|Lie algebra]] is isomorphic to the [[lie-groups/lie-algebra|Lie algebra]] of a connected [[lie-groups/simply-connected-lie-group|simply connected Lie group]]. This [[algebra-groups/group|group]] is unique up to [[fiber-bundles/lie-group|Lie group]] [[algebra-category-theory/isomorphism-category|isomorphism]].

A [[lie-groups/lie-algebra|Lie algebra]] controls local [[algebra-groups/group|group]] structure. Global [[topology/topology|topology]] can distinguish [[fiber-bundles/lie-group|Lie groups]] with the same [[lie-groups/lie-algebra|Lie algebra]]. For example, $\mathbb{R}$ and $S^1$ have isomorphic one-dimensional [[lie-groups/abelian-lie-algebra|abelian Lie algebras]].

### Exercises

**Exercise.**
Prove that the inversion map on a [[fiber-bundles/lie-group|Lie group]] has differential
\[
di_e=-\operatorname{id}_{\mathfrak g}.
\]

**Exercise.**
Compute the [[lie-groups/lie-algebra|Lie algebra]] of the [[algebra-groups/group|group]] of upper triangular matrices with positive diagonal entries.

**Exercise.**
Prove that the center $Z(G)$ is a closed [[lie-groups/lie-subgroup|Lie subgroup]]. Show that its [[lie-groups/lie-algebra|Lie algebra]] is contained in the center of $\mathfrak g$.

**Exercise.**
For a [[linear-algebra/matrix|matrix]] [[fiber-bundles/lie-group|Lie group]], prove
\[
\left.\frac{d}{dt}\right|_{t=0}e^{tX}Ye^{-tX}=[X,Y].
\]

**Exercise.**
Show that a [[lie-groups/connected-lie-group|connected Lie group]] is abelian if and only if its [[lie-groups/lie-algebra|Lie algebra]] bracket is zero.

 ## [[fiber-bundles/lie-group|Lie group]] actions and [[lie-groups/homogeneous-space|homogeneous spaces]]

**Required concepts.** [[fiber-bundles/lie-group|Lie groups]], [[algebra-groups/group-action|group actions]], [[fiber-bundles/smooth-map|smooth maps]], submersions, [[differential-geometry/embedded-submanifold|embedded submanifolds]], and proper maps.
**Result of this chapter.** The reader can analyze [[algebra-groups/orbit|orbits]] and [[algebra-groups/stabilizer|stabilizers]], form quotients by free [[lie-groups/proper-action-lie|proper actions]], and write homogeneous manifolds as $G/H$.

### Smooth actions

**Definition.**
A smooth left action of a [[fiber-bundles/lie-group|Lie group]] $G$ on a manifold $M$ is a [[fiber-bundles/smooth-map|smooth map]]
\[
\Phi:G\times M\to M,
\qquad
(g,p)\mapsto g\cdot p,
\]
that satisfies
\[
e\cdot p=p,
\qquad
(gh)\cdot p=g\cdot(h\cdot p).
\]

For each $g$, the map $\Phi_g(p)=g\cdot p$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]]. Its inverse is $\Phi_{g^{-1}}$.

The action is [[lie-groups/effective-action|effective]] if the only element that fixes every point is $e$. It is [[algebra-groups/free-action|free]] if each [[algebra-groups/stabilizer|stabilizer]] is trivial. It is [[algebra-groups/transitive-action|transitive]] if it has one [[algebra-groups/orbit|orbit]].

**Example.**
The [[algebra-groups/group|group]] $\operatorname{GL}(n,\mathbb{R})$ acts on $\mathbb{R}^n$ by $A\cdot v=Av$. The [[algebra-groups/group|group]] $\mathrm O(n)$ acts on $S^{n-1}$. The latter action is transitive.

### Orbit maps and stabilizers

Fix $p\in M$. The [[fiber-bundles/orbit-map|orbit map]] is
\[
\sigma_p:G\to M,
\qquad
\sigma_p(g)=g\cdot p.
\]
The [[algebra-groups/stabilizer|stabilizer]] is
\[
G_p=\left\{g\in G:g\cdot p=p\right\}.
\]

**Proposition.**
The [[algebra-groups/stabilizer|stabilizer]] $G_p$ is a closed [[lie-groups/lie-subgroup|Lie subgroup]] of $G$.

*Proof.*
It is a [[algebra-groups/subgroup|subgroup]]. It is the inverse [[shared-foundations/image|image]] $\sigma_p^{-1}(\left\{p\right\})$. A point is closed in the [[topology/hausdorff-space|Hausdorff]] manifold $M$. Thus $G_p$ is closed. Apply the [[lie-groups/closed-subgroup-theorem|closed subgroup theorem]].
 \(\square\)

Let $\mathfrak g_p$ be the [[lie-groups/lie-algebra|Lie algebra]] of $G_p$.

### Fundamental vector fields

For $X\in\mathfrak g$, define
\[
X_M(p)=\frac{d}{dt}\bigg|_{0}\exp(tX)\cdot p.
\]
This is the [[differential-geometry/infinitesimal-generator-lie-action|fundamental vector field]] generated by $X$.

With this convention for a left action,
\[
[X_M,Y_M]=-[X,Y]_M.
\]
The minus sign occurs because the action of $G$ on itself by left multiplication gives [[lie-groups/right-invariant-vector-field|right-invariant vector fields]].

The differential of the [[fiber-bundles/orbit-map|orbit map]] is
\[
d(\sigma_p)_e(X)=X_M(p).
\]
Therefore,
\[
\operatorname{ker} d(\sigma_p)_e=\mathfrak g_p.
\]
The [[shared-foundations/image|image]] is the [[differential-geometry/tangent-space|tangent space]] to the [[algebra-groups/orbit|orbit]].

### Orbits as immersed submanifolds

**Theorem (Orbit theorem for Lie group actions).**
Each [[algebra-groups/orbit|orbit]] $G\cdot p$ has a unique [[fiber-bundles/smooth-atlas|smooth structure]] for which the map
\[
G/G_p\to G\cdot p,
\qquad
gG_p\mapsto g\cdot p,
\]
is a [[fiber-bundles/diffeomorphism|diffeomorphism]] onto an [[differential-geometry/immersed-submanifold|immersed submanifold]] of $M$. Its dimension is
\[
\dim(G\cdot p)=\dim G-\dim G_p.
\]
At $p$,
\[
T_p(G\cdot p)=\left\{X_M(p):X\in\mathfrak g\right\}.
\]

The [[linear-algebra/rank|rank]] of the [[fiber-bundles/orbit-map|orbit map]] is constant along $G$ because translations and action maps relate its differentials.

An [[algebra-groups/orbit|orbit]] need not be embedded. Irrational flow on a torus gives dense immersed [[algebra-groups/orbit|orbits]].

### Proper actions

**Definition.**
A smooth action is **proper** if the map
\[
G\times M\to M\times M,
\qquad
(g,p)\mapsto(g\cdot p,p)
\]
is proper.

For a [[lie-groups/proper-action-lie|proper action]], [[algebra-groups/stabilizer|stabilizers]] are compact and [[algebra-groups/orbit|orbits]] are closed [[differential-geometry/embedded-submanifold|embedded submanifolds]]. The [[lie-groups/orbit-space|orbit space]] $M/G$ is [[topology/hausdorff-space|Hausdorff]].

An action by a [[lie-groups/compact-lie-group|compact Lie group]] is proper.

**Theorem (Free proper quotient theorem).**
Let $G$ act smoothly, freely, and properly on $M$. Then the [[lie-groups/orbit-space|orbit space]] $M/G$ has a unique [[fiber-bundles/smooth-atlas|smooth structure]] such that the quotient map
\[
q:M\to M/G
\]
is a submersion. Its dimension is
\[
\dim(M/G)=\dim M-\dim G.
\]
Local [[fiber-bundles/section-of-a-fiber-bundle|smooth sections]] exist. The map $q$ is a principal $G$-bundle for the given action.

This theorem gives a main method to construct manifolds from symmetries.

### Homogeneous spaces

**Definition.**
A [[lie-groups/homogeneous-space|homogeneous space]] is a manifold with a transitive smooth [[fiber-bundles/lie-group|Lie group]] action.

Fix $p\in M$. The [[algebra-groups/stabilizer|stabilizer]] $H=G_p$ is closed. The [[algebra-groups/orbit|orbit]] theorem gives
\[
M\cong G/H.
\]
Thus each [[lie-groups/homogeneous-space|homogeneous space]] has a quotient presentation.

Conversely, let $H\subseteq G$ be a closed [[algebra-groups/subgroup|subgroup]]. The [[shared-foundations/set|set]] of left [[algebra-groups/coset|cosets]] $G/H$ has a [[fiber-bundles/smooth-atlas|smooth structure]]. The quotient map
\[
q:G\to G/H
\]
is a submersion. Left multiplication gives a transitive smooth action of $G$ on $G/H$. The [[algebra-groups/stabilizer|stabilizer]] of $eH$ is $H$.

The [[differential-geometry/tangent-space|tangent space]] at the base point satisfies
\[
T_{eH}(G/H)\cong\mathfrak g/\mathfrak h.
\]
The [[algebra-category-theory/isomorphism-category|isomorphism]] is induced by $dq_e$.

### When a quotient is a group

The quotient $G/H$ is a [[fiber-bundles/lie-group|Lie group]] exactly when $H$ is a closed [[algebra-groups/normal-subgroup|normal subgroup]]. In that case, the quotient multiplication is smooth and
\[
\operatorname{Lie}(G/H)\cong\mathfrak g/\mathfrak h.
\]

When $H$ is not normal, $G/H$ is a manifold with a transitive $G$-action but not a [[algebra-groups/quotient-group|quotient group]].

### Standard homogeneous spaces

**Example (Sphere).**
The [[algebra-groups/group|group]] $\operatorname{SO}(n+1)$ acts transitively on $S^n$. The [[algebra-groups/stabilizer|stabilizer]] of the north pole is isomorphic to $\operatorname{SO}(n)$. Thus
\[
S^n\cong\operatorname{SO}(n+1)/\operatorname{SO}(n).
\]

**Example (Projective space).**
The [[algebra-groups/group|group]] $\mathrm O(n+1)$ acts transitively on $\mathbb{R} P^n$. The [[algebra-groups/stabilizer|stabilizer]] of a line is isomorphic to $\mathrm O(1)\times\mathrm O(n)$. Thus
\[
\mathbb{R} P^n\cong\mathrm O(n+1)/(\mathrm O(1)\times\mathrm O(n)).
\]

**Example (Grassmannian).**
The [[differential-geometry/grassmannian|Grassmannian]] of $k$-planes in $\mathbb{R}^n$ is
\[
\operatorname{Gr}_k(\mathbb{R}^n)
\cong
\mathrm O(n)/(\mathrm O(k)\times\mathrm O(n-k)).
\]
Its dimension is $k(n-k)$.

**Example (Hyperbolic space).**
The identity component $\operatorname{SO}^{+}(n,1)$ acts transitively on hyperbolic $n$-space. A point [[algebra-groups/stabilizer|stabilizer]] is $\operatorname{SO}(n)$. Thus
\[
\mathbb H^n\cong\operatorname{SO}^{+}(n,1)/\operatorname{SO}(n).
\]

### Invariant geometric data

A tensor field $T$ on a $G$-manifold is $G$-invariant if
\[
\Phi_g^{*}T=T
\]
for all $g\in G$.

On a [[lie-groups/homogeneous-space|homogeneous space]] $G/H$, an invariant tensor is determined by its value at $eH$. That value must be invariant under the isotropy action of $H$ on
\[
T_{eH}(G/H)\cong\mathfrak g/\mathfrak h.
\]

For example, $G$-invariant [[differential-geometry/riemannian-manifold|Riemannian metrics]] on $G/H$ correspond to $H$-invariant [[linear-algebra/inner-product|inner products]] on $\mathfrak g/\mathfrak h$. Chapter~18 develops this statement.

### Actions and equivariant maps

Let $G$ act on $M$ and $N$.

**Definition.**
A map $F:M\to N$ is [[fiber-bundles/equivariant-map|$G$-equivariant]] if
\[
F(g\cdot p)=g\cdot F(p).
\]

An [[fiber-bundles/equivariant-map|equivariant map]] sends [[algebra-groups/orbit|orbits]] to [[algebra-groups/orbit|orbits]]. Its differential intertwines [[differential-geometry/infinitesimal-generator-lie-action|fundamental vector fields]]:
\[
dF_p(X_M(p))=X_N(F(p)).
\]

[[fiber-bundles/equivariant-map|Equivariant maps]] induce maps on [[lie-groups/orbit-space|orbit spaces]] when the quotient spaces exist.

### A relation table

| Structure | [[shared-foundations/relation|Relation]] to manifolds |
| --- | --- |
| [[fiber-bundles/lie-group|Lie group]] | A manifold with smooth multiplication and inversion. |
| [[lie-groups/lie-algebra|Lie algebra]] | The [[differential-geometry/tangent-space|tangent space]] at the identity with the bracket from invariant fields. |
| Smooth action | A homomorphism from $G$ to manifold [[fiber-bundles/diffeomorphism|diffeomorphisms]], with smooth evaluation. |
| [[algebra-groups/orbit|Orbit]] | An immersed homogeneous submanifold. |
| [[lie-groups/homogeneous-space|Homogeneous space]] | A manifold of the form $G/H$ for a closed [[algebra-groups/stabilizer|stabilizer]] $H$. |
| Free proper quotient | A manifold $M/G$ and a principal-bundle projection $M\to M/G$. |
| Normal quotient | A [[fiber-bundles/lie-group|Lie group]] $G/H$ when $H$ is closed and normal. |

### Exercises

**Exercise.**
Compute the [[algebra-groups/stabilizer|stabilizer]] of $e_1\in S^{n-1}$ under the $\operatorname{SO}(n)$ action. Derive the quotient presentation of the sphere.

**Exercise.**
Let $G$ act on itself by conjugation. Prove that the [[algebra-groups/stabilizer|stabilizer]] of $g$ is its [[algebra-groups/centralizer|centralizer]]. Identify the [[differential-geometry/tangent-space|tangent space]] to the [[algebra-groups/conjugacy-class|conjugacy class]] at $g$.

**Exercise.**
Prove that a [[algebra-groups/free-action|free action]] of a [[lie-groups/compact-lie-group|compact Lie group]] is proper.

**Exercise.**
Let $H\subseteq G$ be closed. Prove that the right action of $H$ on $G$ is free and proper. Its quotient is $G/H$.

**Exercise.**
Let $G$ act transitively on $M$. Prove that a $G$-invariant [[fiber-bundles/smooth-map|smooth function]] on $M$ is constant.

 ## Principal bundles, [[fiber-bundles/associated-bundle|associated bundles]], and [[fiber-bundles/connection-on-a-vector-bundle|connections]]

**Required concepts.** Fiber bundles, [[fiber-bundles/lie-group|Lie groups]], smooth right actions, quotient manifolds, and [[fiber-bundles/differential-k-form|differential forms]].
**Result of this chapter.** The reader can construct frame bundles, [[fiber-bundles/associated-vector-bundle|associated vector bundles]], structure-group reductions, and [[fiber-bundles/principal-connection|principal connections]].

### Principal bundles

**Definition.**
A [[fiber-bundles/principal-g-bundle|principal $G$-bundle]] consists of a manifold $P$, a manifold $B$, a [[shared-foundations/surjective-function|surjective]] [[fiber-bundles/smooth-map|smooth map]]
\[
\pi:P\to B,
\]
and a smooth right action
\[
P\times G\to P,
\qquad
(p,g)\mapsto pg.
\]
The action preserves each fiber. It is free and transitive on each fiber. Each point of $B$ has an open [[topology/neighborhood|neighborhood]] $U$ with a $G$-equivariant [[fiber-bundles/diffeomorphism|diffeomorphism]]
\[
\Phi:\pi^{-1}(U)\to U\times G,
\]
where $(x,h)g=(x,hg)$.

The base is the [[lie-groups/orbit-space|orbit space]] $P/G$. Each fiber is a $G$-torsor. It is like $G$, but it has no selected identity element.

A principal-bundle map $F:P\to P'$ over $f:B\to B'$ satisfies
\[
F(pg)=F(p)g.
\]

### Local sections and transition functions

A local section $s:U\to P$ gives a trivialization. Each $p\in\pi^{-1}(U)$ has a unique expression
\[
p=s(\pi(p))g.
\]
[[shared-foundations/set|Set]] $\Phi(p)=(\pi(p),g)$.

Conversely, a trivialization gives the section $s(x)=\Phi^{-1}(x,e)$.

Let $s_\alpha$ and $s_\beta$ be local sections. On an overlap, there is a unique [[fiber-bundles/smooth-map|smooth map]]
\[
g_{\alpha\beta}:U_\alpha\cap U_\beta\to G
\]
such that
\[
s_\beta(x)=s_\alpha(x)g_{\alpha\beta}(x).
\]
The maps satisfy
\[
g_{\alpha\alpha}=e,
\qquad
g_{\beta\alpha}=g_{\alpha\beta}^{-1},
\qquad
g_{\alpha\beta}g_{\beta\gamma}=g_{\alpha\gamma}.
\]

Thus principal bundles are described by $G$-valued cocycles.

### Associated bundles

Let $\rho:G\to\operatorname{GL}(V)$ be a finite-dimensional representation. Define a right action on $P\times V$ by
\[
(p,v)g=(pg,\rho(g^{-1})v).
\]

**Definition.**
The [[fiber-bundles/associated-vector-bundle|associated vector bundle]] is
\[
P\times_\rho V=(P\times V)/G.
\]
Its projection is $[p,v]\mapsto\pi(p)$.

A local section of $P$ gives a [[fiber-bundles/local-trivialization|local trivialization]] of the [[fiber-bundles/associated-bundle|associated bundle]]. The [[fiber-bundles/transition-function|transition functions]] are $\rho(g_{\alpha\beta})$.

More generally, a smooth left $G$-action on a manifold $F$ gives the associated fiber bundle $P\times_G F$.

**Proposition.**
Sections of $P\times_\rho V$ correspond to [[fiber-bundles/smooth-map|smooth maps]] $f:P\to V$ that satisfy
\[
f(pg)=\rho(g^{-1})f(p).
\]

*Proof.*
Given an [[fiber-bundles/equivariant-map|equivariant map]] $f$, define $s(x)=[p,f(p)]$ for any $p\in P_x$. Equivariance makes the class independent of $p$. Conversely, a section $s$ has a unique representative $s(\pi(p))=[p,f(p)]$. Change $p$ to $pg$ to obtain the equivariance law.
 \(\square\)

### The frame bundle

Let $E\to M$ be a rank-$k$ [[fiber-bundles/vector-bundle|vector bundle]].

**Definition.**
The [[fiber-bundles/frame-bundle-fr-of-a-manifold-m|frame bundle]] $\operatorname{Fr}(E)$ has fiber
\[
\operatorname{Fr}(E)_p=\left\{u:\mathbb{R}^k\to E_p\text{ linear isomorphism}\right\}.
\]

The [[algebra-groups/group|group]] $\operatorname{GL}(k,\mathbb{R})$ acts on the right by
\[
uA=u\circ A.
\]
This action is free and transitive on each fiber. Local frames give [[fiber-bundles/local-trivialization|local trivializations]]. Thus $\operatorname{Fr}(E)$ is a principal $\operatorname{GL}(k,\mathbb{R})$-bundle.

For $E=TM$, write $\operatorname{Fr}(M)=\operatorname{Fr}(TM)$. Its points are ordered bases of [[differential-geometry/tangent-space|tangent spaces]].

**Theorem.**
The original [[fiber-bundles/vector-bundle|vector bundle]] is recovered as an [[fiber-bundles/associated-bundle|associated bundle]]:
\[
E\cong\operatorname{Fr}(E)\times_{\operatorname{GL}(k,\mathbb{R})}\mathbb{R}^k.
\]
The [[algebra-category-theory/isomorphism-category|isomorphism]] is
\[
[u,v]\mapsto u(v).
\]

*Proof.*
The [[shared-foundations/relation|relation]] identifies $(uA,A^{-1}v)$ with $(u,v)$. Both pairs map to $u(v)$. The map is fiberwise linear and [[shared-foundations/bijective-function|bijective]]. Local frames show that it and its inverse are smooth.
 \(\square\)

This theorem gives an equivalence between rank-$k$ [[fiber-bundles/vector-bundle|vector bundles]] and principal $\operatorname{GL}(k,\mathbb{R})$-bundles with the standard representation.

### Reductions of structure group

Let $H\subseteq G$ be a closed [[lie-groups/lie-subgroup|Lie subgroup]].

**Definition.**
An [[fiber-bundles/reduction-of-structure-group|$H$-reduction]] of a principal $G$-bundle $P\to M$ is a principal $H$-subbundle $Q\subseteq P$ such that
\[
Q\times_HG\cong P.
\]

The reduction selects frames that satisfy an additional condition.

**Theorem.**
$H$-reductions of $P$ correspond to [[fiber-bundles/section-of-a-fiber-bundle|smooth sections]] of the [[fiber-bundles/associated-bundle|associated bundle]]
\[
P/H=P\times_G(G/H).
\]

*Proof.*[Construction]
An $H$-subbundle $Q$ selects the [[algebra-groups/coset|coset]] $qH$ in each fiber of $P/H$. Conversely, a section selects one $H$-orbit in each $G$-fiber. The [[shared-foundations/union|union]] of these [[algebra-groups/orbit|orbits]] is a principal $H$-subbundle.
 \(\square\)

An [[differential-geometry/orientation-of-a-smooth-manifold|orientation]] on an $n$-manifold is a reduction of $\operatorname{Fr}(M)$ from $\operatorname{GL}(n,\mathbb{R})$ to $\operatorname{GL}^{+}(n,\mathbb{R})$. A [[differential-geometry/riemannian-manifold|Riemannian metric]] is a reduction to $\mathrm O(n)$. Chapter~13 proves the second statement.

### Gauge transformations

A [[fiber-bundles/gauge-transformation|gauge transformation]] is a principal-bundle [[algebra-category-theory/automorphism-category|automorphism]] $\Phi:P\to P$ over $\operatorname{id}_M$.

Each [[fiber-bundles/gauge-transformation|gauge transformation]] has the form
\[
\Phi(p)=p\,u(p),
\]
where $u:P\to G$ satisfies
\[
u(pg)=g^{-1}u(p)g.
\]
The [[fiber-bundles/gauge-transformation|gauge transformations]] form the [[fiber-bundles/gauge-group|gauge group]] of $P$.

For an [[algebra-groups/abelian-group|abelian group]], the equivariance condition reduces to $u(pg)=u(p)$. Thus $u$ descends to a map $M\to G$.

### Vertical and horizontal spaces

The vertical space at $p\in P$ is
\[
V_pP=\operatorname{ker} d\pi_p.
\]
For $\xi\in\mathfrak g$, define the fundamental vector
\[
\xi_P(p)=\frac{d}{dt}\bigg|_{0}p\exp(t\xi).
\]
The map
\[
\mathfrak g\to V_pP,
\qquad
\xi\mapsto\xi_P(p)
\]
is a linear [[algebra-category-theory/isomorphism-category|isomorphism]].

**Definition.**
A [[fiber-bundles/principal-connection|principal connection]] is a smooth distribution $H\subseteq TP$ such that
\[
T_pP=H_pP\oplus V_pP
\]
and
\[
dR_g(H_pP)=H_{pg}P.
\]
The subspace $H_pP$ is the horizontal space.

A [[fiber-bundles/tangent-space-at-a-point|tangent vector]] splits uniquely into horizontal and vertical parts.

### Connection one-forms

A [[fiber-bundles/principal-connection|principal connection]] is equivalent to a Lie-algebra-valued one-form
\[
\omega\in\Omega^1(P;\mathfrak g)
\]
with these properties:
\[
\begin{aligned}
\omega(\xi_P)&=\xi,\\
R_g^{*}\omega&=\operatorname{Ad}_{g^{-1}}\omega.
\end{aligned}
\]
The [[fiber-bundles/horizontal-distribution|horizontal distribution]] is $H=\operatorname{ker}\omega$.

The first property returns the vertical generator. The second property gives right equivariance.

**Theorem.**
Each principal bundle over a [[fiber-bundles/smooth-manifold|smooth manifold]] has a [[fiber-bundles/principal-connection|principal connection]].

*Proof.*[Construction outline]
Choose [[fiber-bundles/local-trivialization|local trivializations]] and the product [[fiber-bundles/horizontal-distribution|horizontal distributions]]. Use a [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]] to combine the corresponding local [[fiber-bundles/connection-on-a-vector-bundle|connection]] forms. The space of [[fiber-bundles/connection-on-a-vector-bundle|connections]] is affine. [[convex-analysis/convex-combination|Convex combinations]] with base [[shared-foundations/function|functions]] preserve the two connection-form axioms.
 \(\square\)

### Local connection forms

Let $s_\alpha:U_\alpha\to P$ be a local section. Define
\[
A_\alpha=s_\alpha^{*}\omega
\in\Omega^1(U_\alpha;\mathfrak g).
\]
This is a local gauge potential.

If $s_\beta=s_\alpha g_{\alpha\beta}$, then
\[
A_\beta
=
\operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha
+g_{\alpha\beta}^{-1}dg_{\alpha\beta}.
\]
The second term is the [[algebra-category-theory/pullback|pullback]] of the left Maurer--Cartan form.

### Curvature of a principal connection

**Definition.**
The [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature form]] is
\[
\Omega=d\omega+\frac12[\omega,\omega]
\in\Omega^2(P;\mathfrak g).
\]

The [[fiber-bundles/curvature|curvature]] is horizontal and equivariant:
\[
\iota_{\xi_P}\Omega=0,
\qquad
R_g^{*}\Omega=\operatorname{Ad}_{g^{-1}}\Omega.
\]
In a local section,
\[
F_\alpha=s_\alpha^{*}\Omega
=dA_\alpha+\frac12[A_\alpha,A_\alpha].
\]

The [[fiber-bundles/bianchi-identity|Bianchi identity]] is
\[
d\Omega+[\omega,\Omega]=0.
\]

A [[fiber-bundles/connection-on-a-vector-bundle|connection]] is [[fiber-bundles/flat-principal-connection|flat]] if $\Omega=0$. Flatness is the infinitesimal condition for local horizontal sections.

### Connections on associated bundles

Let $E=P\times_\rho V$. A [[fiber-bundles/principal-connection|principal connection]] on $P$ gives a covariant [[real-analysis/derivative|derivative]] on $E$.

In a local frame from $s_\alpha$, a section is a map $v_\alpha:U_\alpha\to V$. The covariant [[real-analysis/derivative|derivative]] is
\[
\nabla v_\alpha
=dv_\alpha+\rho_{*}(A_\alpha)v_\alpha.
\]
The [[fiber-bundles/gauge-transformation|gauge transformation]] law for $A_\alpha$ makes these local expressions agree on overlaps.

The [[fiber-bundles/curvature|curvature]] of the associated [[fiber-bundles/connection-on-a-vector-bundle|connection]] is
\[
R^{\nabla}=\rho_{*}(F_\alpha)
\]
in a local frame.

Conversely, a linear [[fiber-bundles/connection-on-a-vector-bundle|connection]] on a rank-$k$ [[fiber-bundles/vector-bundle|vector bundle]] gives a [[fiber-bundles/principal-connection|principal connection]] on its frame bundle.

### The solder form and tangent connections

The frame bundle $\operatorname{Fr}(M)$ has a canonical $\mathbb{R}^n$-valued one-form
\[
\vartheta_u(V)=u^{-1}(d\pi_uV).
\]
This is the [[fiber-bundles/solder-form-on-the-frame-bundle|solder form]]. It satisfies
\[
R_A^{*}\vartheta=A^{-1}\vartheta.
\]
It connects the abstract model space $\mathbb{R}^n$ with [[fiber-bundles/tangent-space-at-a-point|tangent vectors]] on $M$.

Let $\omega$ be a [[fiber-bundles/connection-on-a-vector-bundle|connection]] form on $\operatorname{Fr}(M)$. Its [[fiber-bundles/torsion-2-form|torsion]] form is
\[
\Theta=d\vartheta+\omega\wedge\vartheta.
\]
The corresponding [[fiber-bundles/connection-on-a-vector-bundle|affine connection]] on $TM$ is torsion-free exactly when $\Theta=0$.

A [[differential-geometry/riemannian-manifold|Riemannian metric]] gives the orthonormal frame bundle, which is a principal $\mathrm O(n)$-bundle. The [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] is the unique principal $\mathrm O(n)$-connection with zero [[fiber-bundles/torsion-2-form|torsion]].

### Exercises

**Exercise.**
Prove that a principal bundle is trivial if and only if it has a [[fiber-bundles/section-of-a-fiber-bundle|global section]].

**Exercise.**
For the principal bundle $G\to G/H$, identify the right $H$-action and write a [[fiber-bundles/local-trivialization|local trivialization]] from a local section of the quotient map.

**Exercise.**
Prove the [[fiber-bundles/equivariant-map|equivariant-map]] description of sections of an [[fiber-bundles/associated-bundle|associated bundle]].

**Exercise.**
Show that the vertical map $\mathfrak g\to V_pP$ is an [[algebra-category-theory/isomorphism-category|isomorphism]].

**Exercise.**
Let $P=M\times G$ be trivial. Show that each [[fiber-bundles/principal-connection|principal connection]] has the form
\[
\omega_{(x,g)}
=
\operatorname{Ad}_{g^{-1}}A_x+\theta_g,
\]
where $A\in\Omega^1(M;\mathfrak g)$ and $\theta$ is the left Maurer--Cartan form.

# Part: Riemannian Geometry
## Riemannian metrics

**Required concepts.** Smooth covariant tensors, [[linear-algebra/inner-product|inner products]], [[fiber-bundles/vector-bundle|vector bundles]], [[algebra-category-theory/pullback|pullbacks]], and [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partitions of unity]].
**Result of this chapter.** The reader can construct [[differential-geometry/riemannian-manifold|Riemannian metrics]], compute [[topology/metric|metric]] duals and volume forms, and interpret a [[topology/metric|metric]] as an $\mathrm O(n)$-reduction of the frame bundle.

### Definition

**Definition.**
A [[differential-geometry/riemannian-manifold|Riemannian metric]] on a [[fiber-bundles/smooth-manifold|smooth manifold]] $M$ is a smooth covariant two-tensor $g$ such that
\[
g_p:T_pM\times T_pM\to\mathbb{R}
\]
is an [[linear-algebra/inner-product|inner product]] for each $p\in M$.

The pair $(M,g)$ is a [[differential-geometry/riemannian-manifold|Riemannian manifold]].

In local coordinates,
\[
g=g_{ij}\,dx^i\otimes dx^j.
\]
The [[linear-algebra/matrix|matrix]] $(g_{ij}(p))$ is symmetric and positive definite. The component [[shared-foundations/function|functions]] are smooth.

The term [[differential-geometry/riemannian-manifold|metric tensor]] refers to $g$. Chapter~15 constructs a distance [[topology/metric|metric]] from $g$.

A pseudo-Riemannian [[topology/metric|metric]] replaces positive definiteness by nondegeneracy with fixed signature. These notes use positive-definite [[topology/metric|metrics]].

### Existence

**Theorem.**
Each [[fiber-bundles/smooth-manifold|smooth manifold]] has a [[differential-geometry/riemannian-manifold|Riemannian metric]].

*Proof.*
Choose a coordinate [[topology/cover|cover]] $\{U_\alpha\}$. Pull the Euclidean [[linear-algebra/inner-product|inner product]] back through each coordinate map. This gives a local [[topology/metric|metric]] $g^{(\alpha)}$ on $U_\alpha$. Choose a [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]] $\{\rho_\alpha\}$ subordinate to the [[topology/cover|cover]]. Define
\[
g=\sum_\alpha\rho_\alpha g^{(\alpha)}.
\]
The sum is locally finite and smooth. It is symmetric. For $v\neq0$, each term $g^{(\alpha)}(v,v)$ is positive when defined, and at least one coefficient is positive. Thus $g(v,v)>0$.
 \(\square\)

[[differential-geometry/riemannian-manifold|Riemannian metrics]] are not unique. Their [[shared-foundations/set|set]] is a convex cone in $\Gamma(\operatorname{Sym}^2T^{*}M)$.

### Standard constructions

#### Euclidean metric

On $\mathbb{R}^n$,
\[
g_0=\sum_{i=1}^{n}dx^i\otimes dx^i.
\]
Its [[linear-algebra/matrix|matrix]] is the identity.

#### Induced metric

Let $(N,h)$ be Riemannian. Let $F:M\to N$ be an immersion. Define
\[
g=F^{*}h.
\]
Then
\[
g_p(v,w)=h_{F(p)}(dF_pv,dF_pw).
\]
Injectivity of $dF_p$ gives positive definiteness. The map
\[
F:(M,g)\to(N,h)
\]
is an isometric immersion.

An [[differential-geometry/embedded-submanifold|embedded submanifold]] receives the induced [[topology/metric|metric]] from its inclusion.

**Example.**
The standard round [[topology/metric|metric]] on $S^n$ is the [[topology/metric|metric]] induced by $S^n\subseteq\mathbb{R}^{n+1}$.

#### Product metric

For [[differential-geometry/riemannian-manifold|Riemannian manifolds]] $(M,g)$ and $(N,h)$, define
\[
g\oplus h=\operatorname{pr}_M^{*}g+\operatorname{pr}_N^{*}h
\]
on $M\times N$.

#### Conformal change

Let $f\in C^{\infty}(M)$. Then
\[
\widetilde g=e^{2f}g
\]
is a [[differential-geometry/riemannian-manifold|Riemannian metric]]. It has the same angles as $g$. Lengths scale by $e^f$ pointwise.

#### Hyperbolic upper half-space

On
\[
\mathbb H^n
=
\left\{(x^1,\ldots,x^{n-1},y):y>0\right\},
\]
define
\[
g_{\mathbb H}
=
\frac{1}{y^2}
\left(
\sum_{i=1}^{n-1}(dx^i)^2+dy^2
\right).
\]
This [[topology/metric|metric]] has constant sectional [[fiber-bundles/curvature|curvature]] $-1$.

### Metric duality

The [[topology/metric|metric]] gives [[fiber-bundles/bundle-isomorphism|bundle isomorphisms]]
\[
\flat:TM\to T^{*}M,
\qquad
X^{\flat}=g(X,\cdot),
\]
and
\[
\sharp:T^{*}M\to TM.
\]
They are called the **musical isomorphisms**.

In coordinates,
\[
X^{\flat}=g_{ij}X^jdx^i.
\]
Let $(g^{ij})$ be the inverse [[linear-algebra/matrix|matrix]] of $(g_{ij})$. Then
\[
\alpha^{\sharp}=g^{ij}\alpha_j\frac{\partial}{\partial x^i}.
\]

The [[topology/metric|metric]] induces [[linear-algebra/inner-product|inner products]] on cotangent spaces:
\[
\left\langle \alpha,\beta\right\rangle_{g^{-1}}=g^{ij}\alpha_i\beta_j.
\]
It also induces [[linear-algebra/inner-product|inner products]] on tensor and exterior-power bundles.

### Norm, angle, and orthogonality

For $v\in T_pM$, define
\[
\left\lVert v\right\rVert_g=\sqrt{g_p(v,v)}.
\]
For nonzero vectors $v,w$, define the angle $\theta\in[0,\pi]$ by
\[
\cos\theta
=
\frac{g(v,w)}{\left\lVert v\right\rVert_g\left\lVert w\right\rVert_g}.
\]
The vectors are orthogonal when $g(v,w)=0$.

A local frame $(E_1,\ldots,E_n)$ is orthonormal when
\[
g(E_i,E_j)=\delta_{ij}.
\]
Local orthonormal frames exist by smooth Gram--Schmidt orthonormalization.

### The gradient

**Definition.**
For $f\in C^{\infty}(M)$, the [[real-analysis/gradient|gradient]] is
\[
\operatorname{grad} f=(df)^{\sharp}.
\]

It is characterized by
\[
g(\operatorname{grad} f,X)=Xf
\]
for each [[fiber-bundles/vector-field|vector field]] $X$.

In coordinates,
\[
\operatorname{grad} f
=
g^{ij}\frac{\partial f}{\partial x^j}
\frac{\partial}{\partial x^i}.
\]
A point is critical for $f$ if and only if $\operatorname{grad} f=0$ at that point.

### Length and energy

Let $\gamma:[a,b]\to M$ be piecewise smooth. Its length is
\[
L_g(\gamma)=\int_a^b\left\lVert \dot\gamma(t)\right\rVert_g\,dt.
\]
Its energy is
\[
E_g(\gamma)=\frac12\int_a^b\left\lVert \dot\gamma(t)\right\rVert_g^2\,dt.
\]

Length is invariant under orientation-preserving reparametrization. Energy depends on the parametrization. For fixed [[real-analysis/interval|interval]] length,
\[
L_g(\gamma)^2\leq 2(b-a)E_g(\gamma).
\]
Equality holds exactly when speed is constant.

### Volume

Suppose that $M$ is oriented. In a positive coordinate chart, define
\[
\operatorname{vol}_g
=
\sqrt{\det(g_{ij})}\,dx^1\wedge\cdots\wedge dx^n.
\]
The transformation rule for $g_{ij}$ and the positive Jacobian rule show that these local forms agree. Thus $\operatorname{vol}_g$ is a global positive top form.

For a compactly supported [[shared-foundations/function|function]] $f$, define
\[
\int_M f\,d\operatorname{vol}_g=\int_M f\operatorname{vol}_g.
\]

On a nonorientable manifold, the [[topology/metric|metric]] defines a volume density. Integration of densities does not require [[differential-geometry/orientation-of-a-smooth-manifold|orientation]].

Under a conformal change $\widetilde g=e^{2f}g$,
\[
\operatorname{vol}_{\widetilde g}=e^{nf}\operatorname{vol}_g.
\]

### Metrics and frame-bundle reductions

Let $\operatorname{Fr}(M)$ be the principal $\operatorname{GL}(n,\mathbb{R})$-bundle of frames.

**Definition.**
The [[fiber-bundles/orthonormal-frame-bundle-o-of-a-riemannian-manifold|orthonormal frame bundle]] is
\[
\mathrm O(M,g)
=
\left\{
 u:\mathbb{R}^n\to T_pM:
 g_p(u(v),u(w))=\left\langle v,w\right\rangle_{\mathbb{R}^n}
\right\}.
\]

The [[algebra-groups/group|group]] $\mathrm O(n)$ acts freely and transitively on each orthonormal frame fiber.

**Theorem.**
A [[differential-geometry/riemannian-manifold|Riemannian metric]] on $M$ is equivalent to a reduction of $\operatorname{Fr}(M)$ from $\operatorname{GL}(n,\mathbb{R})$ to $\mathrm O(n)$.

*Proof.*
A [[topology/metric|metric]] gives the orthonormal frame bundle. Smooth local orthonormal frames show that this is a principal $\mathrm O(n)$-subbundle.

Conversely, let $Q\subseteq\operatorname{Fr}(M)$ be a principal $\mathrm O(n)$-subbundle. For $u\in Q_p$, define
\[
g_p(u(v),u(w))=\left\langle v,w\right\rangle_{\mathbb{R}^n}.
\]
If $u$ is replaced by $uA$ with $A\in\mathrm O(n)$, the value does not change. Local sections of $Q$ show smoothness. The form is positive definite.
 \(\square\)

This equivalence is one of the main [[shared-foundations/relation|relations]] between Riemannian geometry and [[fiber-bundles/lie-group|Lie groups]].

### Isometries and Killing fields

**Definition.**
An [[topology/isometry|isometry]] $F:(M,g)\to(N,h)$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]] such that
\[
F^{*}h=g.
\]

An [[topology/isometry|isometry]] preserves lengths, angles, volume, geodesics, and [[fiber-bundles/curvature|curvature]].

**Definition.**
A [[fiber-bundles/vector-field|vector field]] $X$ is a **Killing field** if
\[
\mathcal{L}_Xg=0.
\]

The local flow of a Killing field consists of local [[topology/isometry|isometries]]. Conversely, the infinitesimal generator of a one-parameter [[algebra-groups/group|group]] of [[topology/isometry|isometries]] is a Killing field.

In coordinates, the Killing equation is
\[
(\mathcal{L}_Xg)_{ij}
=
X^k\partial_kg_{ij}
+g_{kj}\partial_iX^k
+g_{ik}\partial_jX^k
=0.
\]
The covariant form of this equation appears after the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]].

### Exercises

**Exercise.**
Compute the round [[topology/metric|metric]] on $S^2$ in spherical coordinates.

**Exercise.**
Let $F:M\to N$ be smooth. Prove that $F^{*}h$ is a [[differential-geometry/riemannian-manifold|Riemannian metric]] if and only if $F$ is an immersion.

**Exercise.**
Prove that the [[shared-foundations/set|set]] of [[differential-geometry/riemannian-manifold|Riemannian metrics]] on a fixed manifold is convex.

**Exercise.**
Under $\widetilde g=e^{2f}g$, prove that
\[
\operatorname{grad}_{\widetilde g}u=e^{-2f}\operatorname{grad}_gu.
\]

**Exercise.**
Prove that an [[topology/isometry|isometry]] sends orthonormal frames to orthonormal frames and induces a principal $\mathrm O(n)$-bundle [[algebra-category-theory/isomorphism-category|isomorphism]].

 ## [[fiber-bundles/connection-on-a-vector-bundle|Connections]] and the Levi-Civita theorem

**Required concepts.** [[fiber-bundles/vector-bundle|Vector bundles]], [[fiber-bundles/vector-field|vector fields]], tensor fields, [[fiber-bundles/principal-connection|principal connections]], and [[differential-geometry/riemannian-manifold|Riemannian metrics]].
**Result of this chapter.** The reader can compute covariant [[real-analysis/derivative|derivatives]], parallel transport, [[fiber-bundles/torsion-2-form|torsion]], and the unique [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]].

### Connections on vector bundles

Let $E\to M$ be a smooth [[fiber-bundles/vector-bundle|vector bundle]].

**Definition.**
A [[fiber-bundles/connection-on-a-vector-bundle|connection]] on $E$ is a map
\[
\nabla:\mathfrak X(M)\times\Gamma(E)\to\Gamma(E),
\qquad
(X,s)\mapsto\nabla_Xs,
\]
with these properties:

1. It is $\mathbb{R}$-linear in $X$ and $s$.
1. $\nabla_{fX}s=f\nabla_Xs$.
1. $\nabla_X(fs)=X(f)s+f\nabla_Xs$.

The first variable is tensorial. The second variable has a [[real-analysis/derivative|derivative]] term.

Equivalently, a [[fiber-bundles/connection-on-a-vector-bundle|connection]] is an $\mathbb{R}$-linear map
\[
\nabla:\Gamma(E)\to\Omega^1(M;E)
\]
that satisfies
\[
\nabla(fs)=df\otimes s+f\nabla s.
\]

### Local connection coefficients

Let $(e_a)$ be a local frame of $E$. Define one-forms $\omega^b{}_a$ by
\[
\nabla e_a=\omega^b{}_a\otimes e_b.
\]
For $s=s^ae_a$,
\[
\nabla s=(ds^b+\omega^b{}_as^a)\otimes e_b.
\]

In local coordinates on $M$, write
\[
\nabla_{\partial_i}e_a=\Gamma^b{}_{ia}e_b.
\]
Then
\[
\nabla_Xs
=X^i\left(
\partial_i s^b+\Gamma^b{}_{ia}s^a
\right)e_b.
\]

Under a frame change $e'=eA$, the [[fiber-bundles/connection-on-a-vector-bundle|connection]] [[linear-algebra/matrix|matrix]] transforms by
\[
\omega'=A^{-1}\omega A+A^{-1}dA.
\]
This is the same law as a [[fiber-bundles/principal-connection|principal connection]] in a local gauge.

### Existence and affine structure

**Theorem.**
Each smooth [[fiber-bundles/vector-bundle|vector bundle]] over a [[fiber-bundles/smooth-manifold|smooth manifold]] has a [[fiber-bundles/connection-on-a-vector-bundle|connection]].

*Proof.*
Choose trivializing [[topology/neighborhood|neighborhoods]] and use the ordinary [[real-analysis/derivative|derivative]] in each local frame. Let $\{\rho_\alpha\}$ be a subordinate [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]]. Define
\[
\nabla_Xs=\sum_\alpha\rho_\alpha\nabla^{(\alpha)}_Xs.
\]
The [[fiber-bundles/connection-on-a-vector-bundle|connection]] axioms follow because $\sum_\alpha\rho_\alpha=1$.
 \(\square\)

If $\nabla$ and $\widetilde\nabla$ are [[fiber-bundles/connection-on-a-vector-bundle|connections]], then
\[
A(X,s)=\widetilde\nabla_Xs-\nabla_Xs
\]
is $C^{\infty}(M)$-linear in both variables. Thus
\[
A\in\Omega^1(M;\operatorname{End} E).
\]
Conversely, $\nabla+A$ is a [[fiber-bundles/connection-on-a-vector-bundle|connection]]. Therefore the [[shared-foundations/set|set]] of [[fiber-bundles/connection-on-a-vector-bundle|connections]] is an [[algebraic-geometry-foundations/affine-n-space|affine space]] modeled on $\Omega^1(M;\operatorname{End} E)$.

### Induced connections

A [[fiber-bundles/connection-on-a-vector-bundle|connection]] on $E$ gives a [[fiber-bundles/connection-on-a-vector-bundle|connection]] on $E^{*}$ by
\[
X(\alpha(s))=(\nabla_X\alpha)(s)+\alpha(\nabla_Xs).
\]
It gives [[fiber-bundles/connection-on-a-vector-bundle|connections]] on tensor products by the product rule. It gives [[fiber-bundles/connection-on-a-vector-bundle|connections]] on all tensor bundles when $E=TM$.

For a covariant tensor $T$,
\[
(\nabla_XT)(Y_1,\ldots,Y_k)
=
X(T(Y_1,\ldots,Y_k))
-
\sum_{a=1}^{k}
T(Y_1,\ldots,\nabla_XY_a,\ldots,Y_k).
\]

The [[fiber-bundles/connection-on-a-vector-bundle|connection]] commutes with contraction.

### Covariant derivatives along curves

Let $\gamma:I\to M$ be smooth. A [[fiber-bundles/vector-field|vector field]] along $\gamma$ is a [[fiber-bundles/smooth-map|smooth map]] $V:I\to TM$ with $V(t)\in T_{\gamma(t)}M$.

A [[fiber-bundles/connection-on-a-vector-bundle|connection]] gives
\[
\frac{DV}{dt}=\nabla_{\dot\gamma}V.
\]
In coordinates,
\[
\frac{DV^k}{dt}
=
\frac{dV^k}{dt}
+\Gamma^k{}_{ij}(\gamma(t))\dot\gamma^iV^j.
\]

**Definition.**
A [[fiber-bundles/vector-field|vector field]] $V$ along $\gamma$ is **parallel** if
\[
\frac{DV}{dt}=0.
\]

**Theorem (Parallel transport).**
For $t_0\in I$ and $v\in T_{\gamma(t_0)}M$, there is a unique parallel field $V$ along $\gamma$ with $V(t_0)=v$. The endpoint map
\[
P_{t_0,t_1}:T_{\gamma(t_0)}M\to T_{\gamma(t_1)}M
\]
is a linear [[algebra-category-theory/isomorphism-category|isomorphism]].

This is a linear ODE. Reversing the [[topology/curve|curve]] gives the inverse map.

### Affine connections, torsion, and metric compatibility

A [[fiber-bundles/connection-on-a-vector-bundle|connection]] on $TM$ is also called an [[fiber-bundles/connection-on-a-vector-bundle|affine connection]].

**Definition.**
The [[fiber-bundles/torsion-2-form|torsion]] of an [[fiber-bundles/connection-on-a-vector-bundle|affine connection]] is
\[
T(X,Y)=\nabla_XY-\nabla_YX-[X,Y].
\]

**Proposition.**
The [[fiber-bundles/torsion-2-form|torsion]] is $C^{\infty}(M)$-linear in $X$ and $Y$. Thus it is a tensor field of type $(1,2)$.

*Proof.*
Use the [[fiber-bundles/connection-on-a-vector-bundle|connection]] rules and
\[
[fX,Y]=f[X,Y]-Y(f)X.
\]
The [[real-analysis/derivative|derivative]] terms cancel. The second variable is similar.
 \(\square\)

In coordinates,
\[
T^k{}_{ij}=\Gamma^k{}_{ij}-\Gamma^k{}_{ji}.
\]
Thus a [[fiber-bundles/connection-on-a-vector-bundle|connection]] is torsion-free exactly when its Christoffel symbols are symmetric in the lower indices in every coordinate chart.

**Definition.**
A [[fiber-bundles/connection-on-a-vector-bundle|connection]] $\nabla$ is [[fiber-bundles/levicivita-connection-connection|compatible with $g$]] if
\[
\nabla g=0.
\]
Equivalently,
\[
Xg(Y,Z)=g(\nabla_XY,Z)+g(Y,\nabla_XZ).
\]

If $\nabla g=0$, then parallel transport preserves [[linear-algebra/inner-product|inner products]].

*Proof.*
For parallel fields $V$ and $W$ along a [[topology/curve|curve]],
\[
\frac{d}{dt}g(V,W)
=(\nabla_{\dot\gamma}g)(V,W)
+g(DV/dt,W)+g(V,DW/dt)=0.
\]
 \(\square\)

### Levi-Civita theorem

**Theorem (Levi-Civita).**
Each [[differential-geometry/riemannian-manifold|Riemannian manifold]] $(M,g)$ has a unique [[fiber-bundles/connection-on-a-vector-bundle|affine connection]] $\nabla$ that is torsion-free and compatible with $g$.

*Proof.*
Assume first that such a [[fiber-bundles/connection-on-a-vector-bundle|connection]] exists. [[topology/metric|Metric]] compatibility gives
\[
\begin{aligned}
Xg(Y,Z)&=g(\nabla_XY,Z)+g(Y,\nabla_XZ),\\
Yg(Z,X)&=g(\nabla_YZ,X)+g(Z,\nabla_YX),\\
Zg(X,Y)&=g(\nabla_ZX,Y)+g(X,\nabla_ZY).
\end{aligned}
\]
Add the first two equations and subtract the third. Replace $\nabla_XY-\nabla_YX$ by $[X,Y]$. Symmetry of $g$ gives the Koszul formula
\[
\begin{aligned}
2g(\nabla_XY,Z)
={}&Xg(Y,Z)+Yg(Z,X)-Zg(X,Y)\\
&+g([X,Y],Z)-g([Y,Z],X)+g([Z,X],Y).
\end{aligned}
\]
The right side determines $\nabla_XY$ because $g$ is nondegenerate. This proves uniqueness.

For existence, use the Koszul formula to define $\nabla_XY$ by its [[linear-algebra/inner-product|inner product]] with each $Z$. The right side is $C^{\infty}(M)$-linear in $Z$, so it defines a [[fiber-bundles/vector-field|vector field]]. Direct substitution verifies $\mathbb{R}$-linearity, $C^{\infty}(M)$-linearity in $X$, the Leibniz rule in $Y$, zero [[fiber-bundles/torsion-2-form|torsion]], and [[topology/metric|metric]] compatibility.
 \(\square\)

The resulting [[fiber-bundles/connection-on-a-vector-bundle|connection]] is the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]].

### Christoffel symbols

In coordinates, [[shared-foundations/set|set]]
\[
\nabla_{\partial_i}\partial_j
=\Gamma^k{}_{ij}\partial_k.
\]
The coordinate [[fiber-bundles/vector-field|vector fields]] commute. The Koszul formula gives
\[
\Gamma^k{}_{ij}
=
\frac12g^{k\ell}
\left(
\partial_i g_{j\ell}
+\partial_j g_{i\ell}
-\partial_\ell g_{ij}
\right).
\]

Christoffel symbols are not tensor components. A coordinate change adds terms with second [[real-analysis/derivative|derivatives]] of the coordinate map. Their non-tensorial law permits them to vanish at one point in suitable coordinates.

### Hessian, divergence, and Laplacian

For $f\in C^{\infty}(M)$, define the Hessian
\[
\operatorname{Hess}f=\nabla df.
\]
Equivalently,
\[
\operatorname{Hess}f(X,Y)
=X(Yf)-(\nabla_XY)f.
\]

**Proposition.**
The Hessian is symmetric.

*Proof.*
Subtract the two orders:
\[
\operatorname{Hess}f(X,Y)-\operatorname{Hess}f(Y,X)
=[X,Y]f-(\nabla_XY-\nabla_YX)f=0.
\]
Use zero [[fiber-bundles/torsion-2-form|torsion]].
 \(\square\)

The divergence of a [[fiber-bundles/vector-field|vector field]] is
\[
\operatorname{div} X=\operatorname{tr}(Y\mapsto\nabla_YX).
\]
In a local orthonormal frame $(E_i)$,
\[
\operatorname{div} X=\sum_i g(\nabla_{E_i}X,E_i).
\]

The Laplace--Beltrami operator is
\[
\Delta f=\operatorname{div}(\operatorname{grad} f)=\operatorname{tr}_g(\operatorname{Hess}f).
\]
Sign conventions vary. These notes use the displayed sign.

In coordinates,
\[
\Delta f
=
\frac{1}{\sqrt{\det g}}
\partial_i\left(
\sqrt{\det g}\,g^{ij}\partial_jf
\right).
\]

### Killing equation

For the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]],
\[
(\mathcal{L}_Xg)(Y,Z)
=g(\nabla_YX,Z)+g(Y,\nabla_ZX).
\]
Thus $X$ is Killing exactly when the [[algebra-category-theory/endomorphism-category|endomorphism]] $Y\mapsto\nabla_YX$ is skew-adjoint.

### Principal-bundle form

The [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] gives a principal $\mathrm O(n)$-connection on the orthonormal frame bundle $\mathrm O(M,g)$. In an orthonormal frame, its [[fiber-bundles/connection-on-a-vector-bundle|connection]] [[linear-algebra/matrix|matrix]] satisfies
\[
\omega_{ij}+\omega_{ji}=0.
\]
[[topology/metric|Metric]] compatibility gives this skew-symmetry.

Let $(\theta^i)$ be the tautological coframe. Torsion-free compatibility gives Cartan's first structure equation
\[
d\theta^i+\omega^i{}_j\wedge\theta^j=0.
\]

Thus the Levi-Civita theorem has an equivalent principal-bundle statement: there is a unique torsion-free principal $\mathrm O(n)$-connection on the orthonormal frame bundle.

### Exercises

**Exercise.**
Prove that the difference of two [[fiber-bundles/connection-on-a-vector-bundle|connections]] is a tensor in $\Omega^1(M;\operatorname{End} E)$.

**Exercise.**
Compute the Christoffel symbols of the Euclidean [[topology/metric|metric]] in polar coordinates.

**Exercise.**
Let $\widetilde g=e^{2f}g$. Show that the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connections]] satisfy
\[
\widetilde\nabla_XY
=
\nabla_XY+X(f)Y+Y(f)X-g(X,Y)\operatorname{grad} f.
\]

**Exercise.**
Prove that parallel transport for the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] is an [[topology/isometry|isometry]] between [[differential-geometry/tangent-space|tangent spaces]].

**Exercise.**
Derive the coordinate formula for the Laplace--Beltrami operator.

 ## Geodesics, [[fiber-bundles/exponential-map|exponential maps]], and distance

**Required concepts.** [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]], covariant [[real-analysis/derivative|derivatives]] along [[topology/curve|curves]], ODE theory, [[topology/curve|curve]] length, and compactness.
**Result of this chapter.** The reader can construct geodesics and normal coordinates, define Riemannian distance, and apply the Hopf--Rinow theorem.

### Geodesics

**Definition.**
A smooth [[topology/curve|curve]] $\gamma:I\to M$ is a **geodesic** if
\[
\frac{D\dot\gamma}{dt}=0.
\]

A geodesic has parallel velocity. Thus its speed is constant:
\[
\frac{d}{dt}g(\dot\gamma,\dot\gamma)
=
2g\left(\frac{D\dot\gamma}{dt},\dot\gamma\right)
=0.
\]

In local coordinates, the geodesic equation is
\[
\ddot\gamma^k+\Gamma^k{}_{ij}(\gamma)\dot\gamma^i\dot\gamma^j=0.
\]
This is a second-order nonlinear ODE.

**Theorem (Initial-value theorem).**
For each $p\in M$ and $v\in T_pM$, there is a unique maximal geodesic $\gamma_v:I_v\to M$ such that
\[
\gamma_v(0)=p,
\qquad
\dot\gamma_v(0)=v.
\]
The solution depends smoothly on $(p,v,t)$ on its [[shared-foundations/domain|domain]].

The theorem follows by writing the geodesic equation as a first-order ODE on $TM$.

### Affine parameters

If $\gamma$ is a geodesic and $a\neq0$, then
\[
\widetilde\gamma(t)=\gamma(at+b)
\]
is a geodesic. Such changes are **affine reparametrizations**.

A general reparametrization of a geodesic need not be a geodesic. It can preserve the [[shared-foundations/image|image]] but change the affine parameter.

### The exponential map

**Definition.**
The **Riemannian exponential map** at $p$ is
\[
\exp_p:D_p\subseteq T_pM\to M,
\qquad
\exp_p(v)=\gamma_v(1),
\]
where $D_p$ contains the vectors for which $1\in I_v$.

The scaling property of the geodesic equation gives
\[
\exp_p(tv)=\gamma_v(t)
\]
whenever both sides are defined.

**Proposition.**
The differential at the origin is
\[
d(\exp_p)_0=\operatorname{id}_{T_pM}.
\]

*Proof.*
For $v\in T_pM$,
\[
d(\exp_p)_0(v)
=
\frac{d}{dt}\bigg|_0\exp_p(tv)
=
\dot\gamma_v(0)
=
v.
\]
 \(\square\)

The [[shared-foundations/inverse-function|inverse function]] theorem gives a [[topology/neighborhood|neighborhood]] $U$ of $0\in T_pM$ such that $\exp_p$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]] from $U$ to an open [[topology/neighborhood|neighborhood]] of $p$.

**Definition.**
A **normal neighborhood** of $p$ is an open [[shared-foundations/set|set]] that is the [[shared-foundations/image|image]] under $\exp_p$ of a star-shaped [[topology/neighborhood|neighborhood]] of $0$ on which $\exp_p$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]].

### Normal coordinates

Choose a basis of $T_pM$. Use the inverse of $\exp_p$ to define coordinates on a normal neighborhood. These are **normal coordinates** at $p$.

If the basis is orthonormal, then
\[
g_{ij}(p)=\delta_{ij}.
\]

Radial lines in $T_pM$ map to geodesics through $p$. The geodesic equation for all radial lines gives
\[
\Gamma^k{}_{ij}(p)=0.
\]

For the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]], this also gives
\[
\partial_kg_{ij}(p)=0.
\]

Normal coordinates remove first-order [[topology/metric|metric]] variation at one point. [[fiber-bundles/curvature|Curvature]] controls the second-order variation.

### Gauss lemma

**Theorem (Gauss lemma).**
Let $v,w\in T_pM$. Suppose that $\exp_p$ is defined near $v$. Then
\[
g_{\exp_p(v)}
\left(
d(\exp_p)_v(v),
d(\exp_p)_v(w)
\right)
=
g_p(v,w).
\]

*Proof.*[Proof outline]
Consider the variation
\[
F(s,t)=\exp_p(t(v+sw)).
\]
For fixed $s$, the $t$-curve is a geodesic. Let $T=\partial_tF$ and $S=\partial_sF$. Torsion-free compatibility gives
\[
\frac{d}{dt}g(S,T)
=
g(\nabla_TS,T)
=
g(\nabla_ST,T)
=
\frac12\partial_sg(T,T).
\]
Each radial geodesic has constant speed $\left\lVert v+sw\right\rVert$. Integrate from $0$ to $1$. The initial value of $S$ is zero. The result follows after differentiation in $s$.
 \(\square\)

Radial directions are orthogonal to tangent directions of [[topology/metric-sphere|metric spheres]] in normal coordinates.

### First variation of energy

A variation of a [[topology/curve|curve]] $\gamma$ is a [[fiber-bundles/smooth-map|smooth map]]
\[
F:(-\varepsilon,\varepsilon)\times[a,b]\to M
\]
with $F(0,t)=\gamma(t)$. Let
\[
T=\frac{\partial F}{\partial t},
\qquad
S=\frac{\partial F}{\partial s}.
\]

**Theorem (First variation of energy).**
Let $E(s)$ be the energy of $t\mapsto F(s,t)$. Then
\[
E'(0)
=
g(S,T)\big|_a^b
-
\int_a^b
g\left(S,\frac{DT}{dt}\right)dt.
\]

*Proof.*
Differentiate under the integral:
\[
E'(0)=\int_a^b g(\nabla_ST,T)\,dt.
\]
The coordinate fields of a variation commute. Zero [[fiber-bundles/torsion-2-form|torsion]] gives $\nabla_ST=\nabla_TS$. Apply the product rule:
\[
g(\nabla_TS,T)
=
\frac{d}{dt}g(S,T)-g(S,\nabla_TT).
\]
Integrate.
 \(\square\)

**Corollary.**
A constant-speed [[topology/curve|curve]] is a [[real-analysis/critical-point|critical point]] of energy under all fixed-endpoint variations if and only if it is a geodesic.

### Local minimizing property

**Theorem.**
Let $U$ be a sufficiently small normal neighborhood of $p$. Each $q\in U$ is joined to $p$ by a unique radial geodesic in $U$. This geodesic has length
\[
\left\lVert \exp_p^{-1}(q)\right\rVert.
\]
It has smaller length than each other piecewise smooth [[topology/curve|curve]] from $p$ to $q$ that stays in $U$.

*Proof.*[Proof outline]
Write any [[topology/curve|curve]] in normal polar form
\[
\alpha(t)=\exp_p(r(t)u(t)),
\qquad
\left\lVert u(t)\right\rVert=1.
\]
Gauss lemma makes the radial and angular velocity components orthogonal. Thus
\[
\left\lVert \dot\alpha(t)\right\rVert^2\geq\left|r'(t)\right|^2.
\]
Integrate. The length is at least the total radial change. Equality requires zero angular component and monotone radial motion.
 \(\square\)

Geodesics are locally minimizing. A geodesic can fail to minimize after a longer time.

### Riemannian distance

For $p,q$ in the same [[topology/connected-component|connected component]], define
\[
d_g(p,q)
=
\inf\left\{L_g(\gamma):\gamma\text{ is a piecewise smooth curve from }p\text{ to }q\right\}.
\]
[[shared-foundations/set|Set]] $d_g(p,q)=\infty$ for points in different components when a global extended distance is useful.

**Theorem.**
On each [[topology/connected-component|connected component]], $d_g$ is a [[topology/metric|metric]]. Its [[topology/metric|metric]] [[topology/topology|topology]] equals the manifold [[topology/topology|topology]].

*Proof.*[Main points]
Symmetry follows by reversing [[topology/curve|curves]]. The [[real-analysis/triangle-inequality|triangle inequality]] follows by concatenation. Local minimizing geodesics in a normal neighborhood show that distinct nearby points have positive distance. A chain of normal neighborhoods gives positivity for all distinct points.

On a precompact coordinate [[topology/neighborhood|neighborhood]], the [[topology/metric|metric]] [[linear-algebra/matrix|matrix]] has [[linear-algebra/eigenvalue|eigenvalues]] [[real-analysis/bounded-above|bounded above]] and below by positive constants. Thus Riemannian lengths and Euclidean coordinate lengths compare by fixed constants. This comparison gives equality of the two [[topology/topology|topologies]].
 \(\square\)

A [[topology/curve|curve]] that realizes the distance between its endpoints is a minimizing geodesic after constant-speed parametrization.

### Completeness

**Definition.**
A [[differential-geometry/riemannian-manifold|Riemannian manifold]] is **geodesically complete** if each maximal geodesic is defined on all of $\mathbb{R}$. It is [[topology/complete-metric-space|metrically complete]] if each [[topology/cauchy-sequence|Cauchy sequence]] for $d_g$ converges.

**Theorem (Hopf--Rinow).**
Let $(M,g)$ be connected. The following conditions are equivalent:

1. $(M,d_g)$ is a [[topology/complete-metric-space|complete metric space]].
1. $(M,g)$ is geodesically complete.
1. For some $p\in M$, the map $\exp_p$ is defined on all of $T_pM$.
1. Closed and bounded [[shared-foundations/subset|subsets]] of $(M,d_g)$ are compact.

If these conditions hold, then each pair of points is joined by a minimizing geodesic.

**Corollary.**
Each compact [[differential-geometry/riemannian-manifold|Riemannian manifold]] is complete.

**Example.**
The open unit ball with the Euclidean [[topology/metric|metric]] is not complete. A radial [[shared-foundations/sequence|sequence]] can approach the missing [[topology/boundary|boundary]] in finite distance.

**Example.**
Hyperbolic upper half-space is complete. The factor $1/y^2$ sends the [[topology/boundary|boundary]] $y=0$ to infinite distance.

### Cut locus and injectivity radius

For $v\in T_pM$, a radial geodesic can stop minimizing even though it continues as a geodesic. The first such endpoint belongs to the **cut locus** of $p$.

The injectivity radius at $p$ is
\[
\operatorname{inj}(p)
=
\sup\left\{r>0:\exp_p\text{ is a diffeomorphism on }B_r(0)\subseteq T_pM\right\}.
\]
The global injectivity radius is $\inf_p\operatorname{inj}(p)$.

A compact [[differential-geometry/riemannian-manifold|Riemannian manifold]] has positive injectivity radius.

### Two exponential maps

A [[fiber-bundles/lie-group|Lie group]] has a Lie [[fiber-bundles/exponential-map|exponential map]]
\[
\exp_G:\mathfrak g\to G.
\]
A [[differential-geometry/riemannian-manifold|Riemannian metric]] has a Riemannian [[fiber-bundles/exponential-map|exponential map]]
\[
\exp_e^g:T_eG\to G.
\]
These maps can differ. They agree for a bi-invariant [[differential-geometry/riemannian-manifold|Riemannian metric]]. Chapter~18 proves this statement.

### Exercises

**Exercise.**
Compute geodesics in [[linear-algebra/euclidean-space|Euclidean space]] from the geodesic equation.

**Exercise.**
Compute radial geodesics in polar coordinates for the Euclidean plane. Explain the coordinate singularity at the origin.

**Exercise.**
Prove that an [[topology/isometry|isometry]] preserves affinely parametrized geodesics.

**Exercise.**
Use Hopf--Rinow to prove that a connected compact [[differential-geometry/riemannian-manifold|Riemannian manifold]] has finite [[topology/diameter|diameter]].

**Exercise.**
Show that the punctured Euclidean plane is not complete. Determine whether each pair of points has a minimizing geodesic.

 ## [[fiber-bundles/curvature|Curvature]] and Jacobi fields

**Required concepts.** [[fiber-bundles/connection-on-a-vector-bundle|Connections]], parallel transport, geodesics, normal coordinates, and tensor contraction.
**Result of this chapter.** The reader can compute the [[differential-geometry/riemann-curvature-tensor|Riemann curvature tensor]], sectional and [[differential-geometry/ricci-curvature|Ricci curvature]], and the Jacobi equation.

### Curvature of a connection

Let $E\to M$ have a [[fiber-bundles/connection-on-a-vector-bundle|connection]] $\nabla$.

**Definition.**
The [[fiber-bundles/curvature|curvature]] of $\nabla$ is
\[
R^{\nabla}(X,Y)s
=
\nabla_X\nabla_Ys
-\nabla_Y\nabla_Xs
-\nabla_{[X,Y]}s.
\]

**Proposition.**
The expression $R^{\nabla}(X,Y)s$ is $C^{\infty}(M)$-linear in $X$, $Y$, and $s$. Thus
\[
R^{\nabla}\in\Omega^2(M;\operatorname{End} E).
\]

*Proof.*
Substitute $fX$, $fY$, or $fs$ into the definition. The [[fiber-bundles/connection-on-a-vector-bundle|connection]] [[real-analysis/derivative|derivative]] terms cancel with the [[fiber-bundles/lie-bracket|Lie bracket]] or Leibniz terms. Antisymmetry in $X,Y$ is immediate.
 \(\square\)

[[fiber-bundles/curvature|Curvature]] [[measure-theory/measure|measures]] the noncommutativity of second covariant [[real-analysis/derivative|derivatives]]. It also [[measure-theory/measure|measures]] infinitesimal holonomy around small loops.

### Riemann curvature tensor

For the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]], write
\[
R(X,Y)Z
=
\nabla_X\nabla_YZ
-\nabla_Y\nabla_XZ
-\nabla_{[X,Y]}Z.
\]
This sign convention remains fixed in these notes.

Define the covariant four-tensor
\[
\operatorname{Rm}(X,Y,Z,W)
=g(R(X,Y)Z,W).
\]

In coordinates,
\[
R(\partial_i,\partial_j)\partial_k
=R^{\ell}{}_{kij}\partial_\ell,
\]
where
\[
R^{\ell}{}_{kij}
=
\partial_i\Gamma^{\ell}{}_{jk}
-\partial_j\Gamma^{\ell}{}_{ik}
+\Gamma^{m}{}_{jk}\Gamma^{\ell}{}_{im}
-\Gamma^{m}{}_{ik}\Gamma^{\ell}{}_{jm}.
\]

A [[topology/metric|metric]] is flat on a coordinate [[topology/neighborhood|neighborhood]] if and only if its [[fiber-bundles/curvature|curvature]] vanishes there and the [[topology/neighborhood|neighborhood]] is sufficiently small and simply connected. In that case, there are local coordinates with constant Euclidean [[topology/metric|metric]] components.

### Curvature symmetries

**Theorem.**
The [[differential-geometry/riemann-curvature-tensor|Riemann curvature tensor]] has these symmetries:
\[
\begin{aligned}
\operatorname{Rm}(X,Y,Z,W)
&=-\operatorname{Rm}(Y,X,Z,W),\\
\operatorname{Rm}(X,Y,Z,W)
&=-\operatorname{Rm}(X,Y,W,Z),\\
\operatorname{Rm}(X,Y,Z,W)
&=\operatorname{Rm}(Z,W,X,Y),\\
R(X,Y)Z+R(Y,Z)X+R(Z,X)Y&=0.
\end{aligned}
\]

The last identity is the first [[fiber-bundles/bianchi-identity|Bianchi identity]].

*Proof.*[Main steps]
The first symmetry follows from the definition. [[topology/metric|Metric]] compatibility gives the second symmetry by differentiating $g(Z,W)$ twice and subtracting. Torsion-freeness and the Jacobi identity for [[fiber-bundles/vector-field|vector fields]] give the first [[fiber-bundles/bianchi-identity|Bianchi identity]]. The first three properties imply the pair symmetry.
 \(\square\)

The covariant [[real-analysis/derivative|derivative]] of [[fiber-bundles/curvature|curvature]] satisfies the second [[fiber-bundles/bianchi-identity|Bianchi identity]]:
\[
(\nabla_XR)(Y,Z)
+(\nabla_YR)(Z,X)
+(\nabla_ZR)(X,Y)=0.
\]

### Cartan's second structure equation

Let $(E_i)$ be a local orthonormal frame. Let $\omega^i{}_j$ be the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] forms. Define [[fiber-bundles/curvature|curvature]] forms $\Omega^i{}_j$ by
\[
R(X,Y)E_j=\Omega^i{}_j(X,Y)E_i.
\]
Then
\[
\Omega^i{}_j
=d\omega^i{}_j
+\omega^i{}_k\wedge\omega^k{}_j.
\]
This is Cartan's second structure equation.

The [[fiber-bundles/bianchi-identity|Bianchi identity]] becomes
\[
d\Omega^i{}_j
+\omega^i{}_k\wedge\Omega^k{}_j
-\Omega^i{}_k\wedge\omega^k{}_j=0.
\]

### Sectional curvature

Let $\sigma\subseteq T_pM$ be a two-dimensional subspace. Choose a basis $X,Y$ of $\sigma$.

**Definition.**
The **sectional curvature** of $\sigma$ is
\[
K(\sigma)
=
\frac{g(R(X,Y)Y,X)}
{g(X,X)g(Y,Y)-g(X,Y)^2}.
\]

The value does not depend on the selected basis. For an [[linear-algebra/orthonormal-basis|orthonormal basis]],
\[
K(\sigma)=g(R(X,Y)Y,X).
\]

The sectional [[fiber-bundles/curvature|curvatures]] determine the full [[differential-geometry/riemann-curvature-tensor|Riemann tensor]] by polarization.

A manifold has **constant sectional curvature** $c$ when
\[
R(X,Y)Z
=c\bigl(g(Y,Z)X-g(X,Z)Y\bigr).
\]

[[linear-algebra/euclidean-space|Euclidean space]] has $c=0$. The unit round sphere has $c=1$. Hyperbolic space has $c=-1$.

For a round sphere of radius $r$, the sectional [[fiber-bundles/curvature|curvature]] is $1/r^2$.

### Ricci and scalar curvature

Let $(E_1,\ldots,E_n)$ be an [[linear-algebra/orthonormal-basis|orthonormal basis]] of $T_pM$.

**Definition.**
The [[differential-geometry/ricci-curvature|Ricci tensor]] is
\[
\operatorname{Ric}(X,Y)
=
\sum_{i=1}^{n}g(R(E_i,X)Y,E_i).
\]
The **scalar curvature** is
\[
\operatorname{Scal}=\operatorname{tr}_g\operatorname{Ric}
=
\sum_{i=1}^{n}\operatorname{Ric}(E_i,E_i).
\]

The definitions do not depend on the [[linear-algebra/orthonormal-basis|orthonormal basis]]. The [[differential-geometry/ricci-curvature|Ricci tensor]] is symmetric.

If $M$ has constant sectional [[fiber-bundles/curvature|curvature]] $c$, then
\[
\operatorname{Ric}=(n-1)c\,g,
\qquad
\operatorname{Scal}=n(n-1)c.
\]

In dimension two,
\[
\operatorname{Ric}=Kg,
\qquad
\operatorname{Scal}=2K.
\]
Thus Gaussian [[fiber-bundles/curvature|curvature]] determines all Riemannian [[fiber-bundles/curvature|curvature]] in dimension two.

The Einstein tensor is
\[
G=\operatorname{Ric}-\frac12\operatorname{Scal}\,g.
\]
The contracted second [[fiber-bundles/bianchi-identity|Bianchi identity]] gives
\[
\operatorname{div} G=0.
\]

### Curvature in normal coordinates

Let $(x^i)$ be orthonormal normal coordinates at $p$. Then
\[
g_{ij}(p)=\delta_{ij},
\qquad
\partial_kg_{ij}(p)=0.
\]
The second-order expansion is
\[
g_{ij}(x)
=
\delta_{ij}
-\frac13R_{ikj\ell}(p)x^kx^{\ell}
+O(\left\lVert x\right\rVert^{3}),
\]
where
\[
R_{ikj\ell}
=
\operatorname{Rm}(\partial_i,\partial_k,\partial_j,\partial_\ell).
\]

The volume density has expansion
\[
\sqrt{\det g(x)}
=
1-\frac16\operatorname{Ric}_{k\ell}(p)x^kx^{\ell}
+O(\left\lVert x\right\rVert^{3}).
\]
Thus [[differential-geometry/ricci-curvature|Ricci curvature]] controls the first non-Euclidean term in small-ball volume.

### Jacobi fields

Let $F(s,t)$ be a variation through geodesics. Thus each [[topology/curve|curve]] $t\mapsto F(s,t)$ is a geodesic. [[shared-foundations/set|Set]]
\[
T=\partial_tF,
\qquad
J=\partial_sF\big|_{s=0}.
\]

**Theorem (Jacobi equation).**
The variation field $J$ along $\gamma(t)=F(0,t)$ satisfies
\[
\frac{D^2J}{dt^2}
+R(J,\dot\gamma)\dot\gamma=0.
\]

*Proof.*
The variation coordinate fields commute, so $\nabla_ST=\nabla_TS$. Since each $t$-curve is geodesic,
\[
0=\nabla_S\nabla_TT.
\]
Use the [[fiber-bundles/curvature|curvature]] identity to exchange $\nabla_S$ and $\nabla_T$. This gives
\[
\nabla_T\nabla_TJ+R(J,T)T=0.
\]
 \(\square\)

A solution of the Jacobi equation is a **Jacobi field**. Initial values $J(0)$ and $DJ/dt(0)$ determine it uniquely.

The differential of the [[fiber-bundles/exponential-map|exponential map]] is described by Jacobi fields. If $J(0)=0$ and $DJ/dt(0)=w$, then
\[
J(1)=d(\exp_p)_v(w)
\]
along the geodesic $t\mapsto\exp_p(tv)$, with the appropriate scaling convention.

### Conjugate points

Points $\gamma(0)$ and $\gamma(t_0)$ are **conjugate along $\gamma$** if there is a nonzero Jacobi field $J$ with
\[
J(0)=J(t_0)=0.
\]
This occurs exactly when $d(\exp_{\gamma(0)})_{t_0\dot\gamma(0)}$ is singular.

Conjugate points mark failure of the [[fiber-bundles/exponential-map|exponential map]] to be a [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphism]]. They also affect minimizing properties.

### Second variation and index form

Let $\gamma:[a,b]\to M$ be a geodesic. Let $V$ be a variation field with $V(a)=V(b)=0$. The second variation of energy is
\[
E”(0)
=
\int_a^b
\left(
\left\lVert DV/dt\right\rVert^{2}
-g(R(V,\dot\gamma)\dot\gamma,V)
\right)dt
\]
after the standard choice of variation.

The bilinear index form is
\[
I(V,W)
=
\int_a^b
\left(
g(DV/dt,DW/dt)
-g(R(V,\dot\gamma)\dot\gamma,W)
\right)dt.
\]

Positive sectional [[fiber-bundles/curvature|curvature]] tends to focus geodesics. Negative sectional [[fiber-bundles/curvature|curvature]] tends to separate them.

### Selected global comparison theorems

**Theorem (Cartan--Hadamard).**
Let $(M,g)$ be complete and simply connected. Suppose that $K\leq 0$. Then each [[fiber-bundles/exponential-map|exponential map]]
\[
\exp_p:T_pM\to M
\]
is a covering map. Since $M$ is simply connected, it is a [[fiber-bundles/diffeomorphism|diffeomorphism]]. In particular, each pair of points has a unique geodesic.

**Theorem (Bonnet--Myers).**
Let $(M^n,g)$ be complete. Suppose that
\[
\operatorname{Ric}\geq(n-1)kg
\]
for a constant $k>0$. Then $M$ is compact and
\[
\operatorname{diam}(M)\leq\frac{\pi}{\sqrt{k}}.
\]
Its [[topology/fundamental-group|fundamental group]] is finite.

These theorems show how local [[fiber-bundles/curvature|curvature]] bounds control global [[topology/topology|topology]] and distance.

### Exercises

**Exercise.**
Prove that every one-dimensional [[differential-geometry/riemannian-manifold|Riemannian manifold]] has zero Riemann [[fiber-bundles/curvature|curvature]].

**Exercise.**
Show that the product of two flat manifolds is flat.

**Exercise.**
Let $M\times N$ have the product [[topology/metric|metric]]. Determine sectional [[fiber-bundles/curvature|curvature]] for planes tangent to one factor and for mixed planes.

**Exercise.**
Derive the Jacobi equation from a variation through geodesics.

**Exercise.**
Assume constant sectional [[fiber-bundles/curvature|curvature]] $c$. Verify the formulas for Ricci and scalar [[fiber-bundles/curvature|curvature]].

 ## Riemannian submanifolds and submersions

**Required concepts.** [[differential-geometry/embedded-submanifold|Embedded submanifolds]], induced [[topology/metric|metrics]], [[fiber-bundles/levicivita-connection-connection|Levi-Civita connections]], and [[fiber-bundles/curvature|curvature]].
**Result of this chapter.** The reader can compute second fundamental forms, shape operators, Gauss equations, mean [[fiber-bundles/curvature|curvature]], and quotient [[topology/metric|metrics]].

### Induced geometry

Let $(\overline M,\overline g)$ be a [[differential-geometry/riemannian-manifold|Riemannian manifold]]. Let $M\subseteq\overline M$ be an [[differential-geometry/embedded-submanifold|embedded submanifold]]. Give $M$ the induced [[topology/metric|metric]]
\[
g=\iota^{*}\overline g,
\]
where $\iota:M\hookrightarrow\overline M$ is the inclusion.

At each $p\in M$, there is an orthogonal decomposition
\[
T_p\overline M=T_pM\oplus N_pM.
\]
The bundle $NM$ is the [[differential-geometry/normal-bundle|normal bundle]].

Let $\overline\nabla$ be the ambient [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]]. Let $X,Y$ be [[fiber-bundles/tangent-space-at-a-point|tangent vector]] fields on $M$. Extend them locally to ambient fields. The tangential and normal parts of $\overline\nabla_XY$ do not depend on the extensions.

### Gauss formula and second fundamental form

**Definition.**
The **second fundamental form** is
\[
\mathrm{II}(X,Y)=(\overline\nabla_XY)^{\perp}.
\]

The tangential part defines
\[
\nabla_XY=(\overline\nabla_XY)^{\top}.
\]
Thus the **Gauss formula** is
\[
\overline\nabla_XY=\nabla_XY+\mathrm{II}(X,Y).
\]

**Theorem.**
The tangential [[fiber-bundles/connection-on-a-vector-bundle|connection]] $\nabla$ is the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] of the induced [[topology/metric|metric]]. The second fundamental form is symmetric and $C^{\infty}(M)$-bilinear.

*Proof.*
Tangential projection preserves the [[fiber-bundles/connection-on-a-vector-bundle|connection]] rules. Ambient [[topology/metric|metric]] compatibility gives compatibility with the induced [[topology/metric|metric]]. Ambient zero [[fiber-bundles/torsion-2-form|torsion]] gives
\[
\nabla_XY-\nabla_YX=[X,Y]
\]
and
\[
\mathrm{II}(X,Y)=\mathrm{II}(Y,X).
\]
The tensorial properties follow from the [[fiber-bundles/connection-on-a-vector-bundle|connection]] rules and normal projection. The Levi-Civita theorem identifies $\nabla$.
 \(\square\)

The second fundamental form [[measure-theory/measure|measures]] the difference between ambient and intrinsic covariant [[real-analysis/derivative|derivatives]].

### Shape operators and the Weingarten formula

Let $\xi$ be a normal [[fiber-bundles/vector-field|vector field]].

**Definition.**
The **shape operator** in direction $\xi$ is the [[algebra-category-theory/endomorphism-category|endomorphism]]
\[
A_\xi:TM\to TM
\]
defined by
\[
g(A_\xi X,Y)=\overline g(\mathrm{II}(X,Y),\xi).
\]

Each $A_\xi$ is self-adjoint.

Differentiate $\overline g(Y,\xi)=0$. This gives the **Weingarten formula**
\[
\overline\nabla_X\xi=-A_\xi X+\nabla_X^{\perp}\xi.
\]
The normal part $\nabla^{\perp}$ is a [[fiber-bundles/connection-on-a-vector-bundle|connection]] on the [[differential-geometry/normal-bundle|normal bundle]].

For a hypersurface with unit normal $\nu$, write $A=A_\nu$. Its [[linear-algebra/eigenvalue|eigenvalues]] are the **principal curvatures**. The signs depend on the selected normal.

### Gauss equation

Let $X,Y,Z,W$ be [[fiber-bundles/tangent-space-at-a-point|tangent vector]] fields.

**Theorem (Gauss equation).**
\[
\overline{\operatorname{Rm}}(X,Y,Z,W)
=
\operatorname{Rm}(X,Y,Z,W)
+\overline g(\mathrm{II}(X,W),\mathrm{II}(Y,Z))
-\overline g(\mathrm{II}(X,Z),\mathrm{II}(Y,W)).
\]

*Proof.*[Main calculation]
Insert the Gauss formula into the definition of $\overline R(X,Y)Z$. Take the tangential part. [[real-analysis/derivative|Derivatives]] of $\mathrm{II}$ contribute only normal or Codazzi terms. Pair with $W$. Use the Weingarten formula to convert tangential terms into pairings of second fundamental forms.
 \(\square\)

For an orthonormal pair $X,Y$,
\[
K_M(X,Y)
=
K_{\overline M}(X,Y)
+\overline g(\mathrm{II}(X,X),\mathrm{II}(Y,Y))
-\left\lVert \mathrm{II}(X,Y)\right\rVert^2.
\]

For a surface in $\mathbb{R}^3$,
\[
K=\det A.
\]
This is Gauss's Theorema Egregium. The intrinsic Gaussian [[fiber-bundles/curvature|curvature]] is determined by the first fundamental form even though the displayed formula uses an embedding.

### Codazzi and Ricci equations

Define
\[
(\nabla_X^{\perp}\mathrm{II})(Y,Z)
=
\nabla_X^{\perp}(\mathrm{II}(Y,Z))
-\mathrm{II}(\nabla_XY,Z)
-\mathrm{II}(Y,\nabla_XZ).
\]

The Codazzi equation is
\[
(\nabla_X^{\perp}\mathrm{II})(Y,Z)
-(\nabla_Y^{\perp}\mathrm{II})(X,Z)
=
(\overline R(X,Y)Z)^{\perp}.
\]

The Ricci equation relates the [[fiber-bundles/curvature|curvature]] of the normal [[fiber-bundles/connection-on-a-vector-bundle|connection]] to [[algebra-groups/commutator|commutators]] of shape operators:
\[
\overline g(R^{\perp}(X,Y)\xi,\eta)
=
\overline g(\overline R(X,Y)\xi,\eta)
+g([A_\xi,A_\eta]X,Y).
\]

The Gauss, Codazzi, and Ricci equations are compatibility conditions for submanifold data.

### Mean curvature and minimal submanifolds

Let $m=\dim M$. Let $(E_1,\ldots,E_m)$ be a local orthonormal frame.

**Definition.**
The **mean curvature vector** is
\[
H=\frac1m\sum_{i=1}^{m}\mathrm{II}(E_i,E_i).
\]
The submanifold is **minimal** if $H=0$.

For a hypersurface,
\[
H=\frac1m(\operatorname{tr} A)\nu.
\]
The scalar coefficient changes sign when the unit normal changes. The vector $H$ does not depend on that choice.

Minimal submanifolds are [[real-analysis/critical-point|critical points]] of the volume functional under compactly supported variations.

**Theorem (First variation of volume).**
Let $M$ be compact. Let $F_s:M\to\overline M$ be a smooth variation of an [[differential-geometry/immersed-submanifold|immersed submanifold]]. Let
\[
V=\frac{\partial F_s}{\partial s}\bigg|_{s=0}.
\]
If $M$ has no [[topology/boundary|boundary]], or if the [[topology/boundary|boundary]] term vanishes, then
\[
\frac{d}{ds}\bigg|_{0}\operatorname{Vol}(F_s(M))
=-m\int_M\overline g(H,V)\,d\operatorname{vol}_g.
\]

### Examples

**Example (Round sphere).**
For the [[linear-algebra/unit-sphere|unit sphere]] $S^n\subseteq\mathbb{R}^{n+1}$, take the outward unit normal $\nu(p)=p$. Then
\[
\overline\nabla_X\nu=X.
\]
The Weingarten formula gives $A=-\operatorname{id}$. Thus
\[
\mathrm{II}(X,Y)=-g(X,Y)\nu.
\]
The Gauss equation gives sectional [[fiber-bundles/curvature|curvature]] $1$.

**Example (Cylinder).**
The circular cylinder $S^1(r)\times\mathbb{R}\subseteq\mathbb{R}^3$ has principal [[fiber-bundles/curvature|curvatures]] $-1/r$ and $0$ for the outward normal under the sign convention of these notes. Its Gaussian [[fiber-bundles/curvature|curvature]] is zero.

**Example (Totally geodesic submanifold).**
A submanifold is **totally geodesic** if $\mathrm{II}=0$. Then each geodesic of the submanifold is an ambient geodesic. [[convex-analysis/linear-subspace|Linear subspaces]] of [[linear-algebra/euclidean-space|Euclidean space]] are totally geodesic.

### Tubular neighborhoods

The normal [[fiber-bundles/exponential-map|exponential map]] is
\[
\exp^{\perp}:NM\supseteq U\to\overline M,
\qquad
\exp^{\perp}(p,\xi)=\exp^{\overline M}_p(\xi).
\]

**Theorem (Tubular neighborhood theorem).**
For an [[differential-geometry/embedded-submanifold|embedded submanifold]] $M\subseteq\overline M$, there is a [[topology/neighborhood|neighborhood]] of the [[fiber-bundles/zero-section|zero section]] in $NM$ on which $\exp^{\perp}$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]] onto a [[topology/neighborhood|neighborhood]] of $M$ in $\overline M$. If $M$ is compact, one uniform normal radius can be used.

This theorem identifies a [[topology/neighborhood|neighborhood]] of a submanifold with a [[topology/neighborhood|neighborhood]] in its [[differential-geometry/normal-bundle|normal bundle]].

### Isometric embeddings

An isometric embedding realizes a [[differential-geometry/riemannian-manifold|Riemannian manifold]] as a Riemannian submanifold of another one.

**Theorem (Nash embedding theorem).**
Each smooth [[differential-geometry/riemannian-manifold|Riemannian manifold]] has a smooth isometric embedding into some [[linear-algebra/euclidean-space|Euclidean space]] $\mathbb{R}^N$.

The required dimension $N$ can be large. The theorem is global and nonlinear. Intrinsic Riemannian geometry does not require a selected embedding.

### Riemannian submersions

Let $\pi:(M,g)\to(B,h)$ be a [[fiber-bundles/smooth-submersion|smooth submersion]]. The vertical bundle is
\[
\mathcal V=\operatorname{ker} d\pi.
\]
The horizontal bundle is
\[
\mathcal H=\mathcal V^{\perp}.
\]

**Definition.**
The map $\pi$ is a **Riemannian submersion** if
\[
d\pi_p:\mathcal H_p\to T_{\pi(p)}B
\]
is an [[topology/isometry|isometry]] for each $p$.

A free proper isometric action can give a quotient [[topology/metric|metric]]. If the [[topology/metric|metric]] on $M$ is $G$-invariant, define the [[topology/metric|metric]] on $M/G$ by requiring the quotient map to be a Riemannian submersion.

The fibers of a Riemannian submersion are submanifolds. Their second fundamental form and the nonintegrability of the [[fiber-bundles/horizontal-distribution|horizontal distribution]] affect the [[fiber-bundles/curvature|curvature]] of the base.

### Exercises

**Exercise.**
Derive the Weingarten formula from [[linear-algebra/orthogonality|orthogonality]] of tangent and normal fields.

**Exercise.**
Compute the second fundamental form and mean [[fiber-bundles/curvature|curvature]] of a round sphere of radius $r$.

**Exercise.**
Use the Gauss equation to prove that a surface in $\mathbb{R}^3$ has Gaussian [[fiber-bundles/curvature|curvature]] equal to the product of its principal [[fiber-bundles/curvature|curvatures]].

**Exercise.**
Prove that $\mathrm{II}=0$ if and only if the ambient covariant [[real-analysis/derivative|derivative]] of [[fiber-bundles/tangent-space-at-a-point|tangent vector]] fields is tangent.

**Exercise.**
Let a [[lie-groups/compact-lie-group|compact Lie group]] act freely and isometrically on $(M,g)$. Construct the quotient [[topology/metric|metric]] and prove that $M\to M/G$ is a Riemannian submersion.

 ## [[fiber-bundles/lie-group|Lie groups]] in Riemannian geometry

**Required concepts.** [[fiber-bundles/lie-group|Lie groups]], [[lie-groups/homogeneous-space|homogeneous spaces]], [[differential-geometry/riemannian-manifold|Riemannian metrics]], [[fiber-bundles/levicivita-connection-connection|Levi-Civita connections]], [[fiber-bundles/curvature|curvature]], principal bundles, and submersions.
**Result of this chapter.** The reader can construct invariant [[topology/metric|metrics]], compare Lie and Riemannian [[fiber-bundles/exponential-map|exponential maps]], and use [[topology/isometry|isometry]] and [[fiber-bundles/holonomy-group|holonomy groups]].

### Left-invariant metrics

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] with [[lie-groups/lie-algebra|Lie algebra]] $\mathfrak g$.

**Definition.**
A [[differential-geometry/riemannian-manifold|Riemannian metric]] $g$ on $G$ is [[lie-groups/left-invariant-vector-field|left invariant]] if each [[lie-groups/left-translation|left translation]] $L_a$ is an [[topology/isometry|isometry]]:
\[
L_a^{*}g=g.
\]

An [[linear-algebra/inner-product|inner product]] $\left\langle \cdot,\cdot\right\rangle_e$ on $\mathfrak g=T_eG$ defines a left-invariant [[topology/metric|metric]] by
\[
g_a(u,v)
=
\inner{d(L_{a^{-1}})_a u}{d(L_{a^{-1}})_a v}_e.
\]
Conversely, a left-invariant [[topology/metric|metric]] is determined by its value at the identity.

**Theorem.**
Each [[fiber-bundles/lie-group|Lie group]] has a left-invariant [[differential-geometry/riemannian-manifold|Riemannian metric]].

*Proof.*
Choose any [[linear-algebra/inner-product|inner product]] on $\mathfrak g$. Extend it by [[lie-groups/left-translation|left translation]].
 \(\square\)

**Theorem.**
Each [[lie-groups/connected-lie-group|connected Lie group]] with a left-invariant [[differential-geometry/riemannian-manifold|Riemannian metric]] is complete.

*Proof.*[Proof outline]
Choose a normal neighborhood of the identity with compact closure. [[lie-groups/left-translation|Left translations]] give normal neighborhoods of the same [[topology/metric|metric]] size at every point. A finite-length [[topology/curve|curve]] cannot escape the manifold in finite time because each endpoint stage has a uniform extension [[topology/neighborhood|neighborhood]]. Apply Hopf--Rinow.
 \(\square\)

Thus a left-invariant [[topology/metric|metric]] gives a complete homogeneous [[differential-geometry/riemannian-manifold|Riemannian manifold]].

### Levi-Civita connection of a left-invariant metric

Let $X,Y,Z\in\mathfrak g$ and identify them with [[lie-groups/left-invariant-vector-field|left-invariant vector fields]]. [[topology/metric|Metric]] [[real-analysis/derivative|derivatives]] vanish. The Koszul formula gives
\[
2\left\langle \nabla_XY,Z\right\rangle
=
\left\langle [X,Y],Z\right\rangle
-\left\langle [Y,Z],X\right\rangle
+\left\langle [Z,X],Y\right\rangle.
\]

Let $\operatorname{ad}_X^{\dagger}$ be the adjoint of $\operatorname{ad}_X$ for the selected [[linear-algebra/inner-product|inner product]]. Then
\[
\nabla_XY
=
\frac12\left(
[X,Y]-\operatorname{ad}_X^{\dagger}Y-\operatorname{ad}_Y^{\dagger}X
\right).
\]

A geodesic $g(t)$ can be described by its left-trivialized velocity
\[
u(t)=d(L_{g(t)^{-1}})_{g(t)}\dot g(t)\in\mathfrak g.
\]
The geodesic equation becomes the Euler--Arnold equation
\[
\dot u=\operatorname{ad}_u^{\dagger}u
\]
with the left-trivialization convention of these notes.

### Bi-invariant metrics

**Definition.**
A [[topology/metric|metric]] is [[lie-groups/bi-invariant-metric|bi-invariant]] if both left and [[lie-groups/right-translation|right translations]] are [[topology/isometry|isometries]].

For a left-invariant [[topology/metric|metric]], the following conditions are equivalent:

1. The [[topology/metric|metric]] is right invariant.
1. The [[linear-algebra/inner-product|inner product]] on $\mathfrak g$ is $\operatorname{Ad}(G)$-invariant.
1. For connected $G$, each $\operatorname{ad}_X$ is skew-adjoint:
\[
\left\langle [X,Y],Z\right\rangle+\left\langle Y,[X,Z]\right\rangle=0.
\]

**Theorem.**
Each [[lie-groups/compact-lie-group|compact Lie group]] has a bi-invariant [[differential-geometry/riemannian-manifold|Riemannian metric]].

*Proof.*
Start with an [[linear-algebra/inner-product|inner product]] $b$ on $\mathfrak g$. Let $\mu$ be normalized [[harmonic-analysis/haar-measure|Haar measure]] on $G$. Define
\[
\left\langle X,Y\right\rangle
=
\int_G b(\operatorname{Ad}_gX,\operatorname{Ad}_gY)\,d\mu(g).
\]
The integral is positive definite and $\operatorname{Ad}(G)$-invariant. Extend it by [[lie-groups/left-translation|left translation]].
 \(\square\)

A noncompact [[fiber-bundles/lie-group|Lie group]] can fail to have a bi-invariant [[differential-geometry/riemannian-manifold|Riemannian metric]]. The obstruction is the absence of a positive-definite $\operatorname{Ad}$-invariant [[linear-algebra/inner-product|inner product]].

### Geometry of a bi-invariant metric

For [[lie-groups/left-invariant-vector-field|left-invariant vector fields]],
\[
\nabla_XY=\frac12[X,Y].
\]
Therefore the geodesics through the identity are
\[
t\mapsto\exp_G(tX).
\]
[[lie-groups/left-translation|Left translation]] gives all geodesics.

**Theorem.**
For a [[lie-groups/bi-invariant-metric|bi-invariant metric]], the Lie [[fiber-bundles/exponential-map|exponential map]] and the Riemannian [[fiber-bundles/exponential-map|exponential map]] at the identity agree:
\[
\exp_G=\exp_e^{g}.
\]

The [[fiber-bundles/curvature|curvature]] is
\[
R(X,Y)Z=-\frac14\left[\left[X,Y\right],Z\right].
\]
For an orthonormal pair $X,Y$,
\[
K(X,Y)=\frac14\left\lVert [X,Y]\right\rVert^2\geq 0.
\]

The [[differential-geometry/ricci-curvature|Ricci tensor]] is
\[
\operatorname{Ric}(X,Y)=-\frac14B(X,Y),
\]
where
\[
B(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)
\]
is the [[lie-groups/killing-form|Killing form]].

A [[lie-groups/bi-invariant-metric|bi-invariant metric]] is flat exactly when the [[lie-groups/lie-algebra|Lie algebra]] is abelian. A compact connected [[lie-groups/abelian-lie-group|abelian Lie group]] is a torus.

### Examples

**Example (Torus).**
The torus $T^n$ has a flat [[lie-groups/bi-invariant-metric|bi-invariant metric]] from any [[linear-algebra/inner-product|inner product]] on its [[lie-groups/abelian-lie-algebra|abelian Lie algebra]] $\mathbb{R}^n$ that is compatible with the lattice quotient.

**Example ($\operatorname{SO}(3)$).**
The negative [[lie-groups/killing-form|Killing form]] gives a [[lie-groups/bi-invariant-metric|bi-invariant metric]] on $\operatorname{SO}(3)$. Each two-plane in $\mathfrak{so}(3)$ has positive sectional [[fiber-bundles/curvature|curvature]] after a suitable normalization.

**Example (Heisenberg group).**
The [[lie-groups/heisenberg-group|Heisenberg group]] has left-invariant [[topology/metric|metrics]]. It has no bi-invariant [[differential-geometry/riemannian-manifold|Riemannian metric]] because its nonzero nilpotent adjoint maps cannot all be skew-adjoint for a positive-definite [[linear-algebra/inner-product|inner product]].

### Invariant metrics on homogeneous spaces

Let $M=G/H$, where $H$ is closed. The isotropy representation is the action of $H$ on
\[
T_{eH}(G/H)\cong\mathfrak g/\mathfrak h.
\]

**Theorem.**
$G$-invariant [[differential-geometry/riemannian-manifold|Riemannian metrics]] on $G/H$ correspond to $\operatorname{Ad}(H)$-invariant [[linear-algebra/inner-product|inner products]] on $\mathfrak g/\mathfrak h$.

*Proof.*
An invariant [[topology/metric|metric]] is determined by its value at $eH$. Elements of $H$ fix $eH$, so this [[linear-algebra/inner-product|inner product]] must be invariant under the isotropy representation.

Conversely, let an invariant [[linear-algebra/inner-product|inner product]] be given at $eH$. For $gH\in G/H$, move it by $d(L_g)_{eH}$. If $g$ is replaced by $gh$ with $h\in H$, isotropy invariance gives the same [[linear-algebra/inner-product|inner product]]. Smoothness follows from local sections of $G\to G/H$.
 \(\square\)

If $H$ is compact, such an [[linear-algebra/inner-product|inner product]] always exists. Average any [[linear-algebra/inner-product|inner product]] over $H$.

A decomposition
\[
\mathfrak g=\mathfrak h\oplus\mathfrak m
\]
is **reductive** if $\operatorname{Ad}(H)\mathfrak m\subseteq\mathfrak m$. Then $\mathfrak m$ identifies with $T_{eH}(G/H)$. Compact $H$ always permits a reductive [[shared-foundations/complement|complement]].

### Normal homogeneous metrics

Suppose that $G$ has an $\operatorname{Ad}(G)$-invariant [[linear-algebra/inner-product|inner product]] and that
\[
\mathfrak g=\mathfrak h\oplus\mathfrak m
\]
is the orthogonal decomposition. Restrict the [[linear-algebra/inner-product|inner product]] to $\mathfrak m$. The resulting [[topology/metric|metric]] on $G/H$ is a **normal homogeneous metric**.

The quotient map
\[
G\to G/H
\]
is a Riemannian submersion for the [[lie-groups/bi-invariant-metric|bi-invariant metric]] on $G$ and the normal homogeneous [[topology/metric|metric]] on $G/H$.

Normal [[lie-groups/homogeneous-space|homogeneous spaces]] have nonnegative sectional [[fiber-bundles/curvature|curvature]].

The round sphere
\[
S^n=\operatorname{SO}(n+1)/\operatorname{SO}(n)
\]
is a normal [[lie-groups/homogeneous-space|homogeneous space]].

### Symmetric spaces

**Definition.**
A connected [[differential-geometry/riemannian-manifold|Riemannian manifold]] is a **Riemannian symmetric space** if each point $p$ has an [[topology/isometry|isometry]] $s_p$ such that
\[
s_p(p)=p,
\qquad
ds_p|_p=-\operatorname{id}_{T_pM}.
\]

The map $s_p$ reverses geodesics through $p$. A complete simply connected symmetric space has a presentation $G/H$ from an involutive [[fiber-bundles/lie-group|Lie group]] [[algebra-category-theory/automorphism-category|automorphism]].

At the [[lie-groups/lie-algebra|Lie algebra]] level, an involution gives
\[
\mathfrak g=\mathfrak h\oplus\mathfrak m
\]
with
\[
[\mathfrak h,\mathfrak h]\subseteq\mathfrak h,
\qquad
[\mathfrak h,\mathfrak m]\subseteq\mathfrak m,
\qquad
[\mathfrak m,\mathfrak m]\subseteq\mathfrak h.
\]

[[linear-algebra/euclidean-space|Euclidean space]], spheres, hyperbolic spaces, and positive-definite [[linear-algebra/matrix|matrix]] spaces $\operatorname{GL}(n,\mathbb{R})/\mathrm O(n)$ are symmetric spaces.

### The isometry group

Let $(M,g)$ be connected. Write
\[
\operatorname{Isom}(M,g)=\left\{F:M\to M:F\text{ is an isometry}\right\}.
\]

**Theorem (Myers--Steenrod).**
The [[topology/isometry|isometry]] [[algebra-groups/group|group]] of a connected [[differential-geometry/riemannian-manifold|Riemannian manifold]] is a finite-dimensional [[fiber-bundles/lie-group|Lie group]]. Its action on $M$ is smooth.

The [[algebra-groups/stabilizer|stabilizer]] of $p$ acts faithfully on $T_pM$ by orthogonal maps. Thus it is isomorphic to a closed [[algebra-groups/subgroup|subgroup]] of $\mathrm O(T_pM)$ and is compact.

For $n=\dim M$,
\[
\dim\operatorname{Isom}(M,g)\leq\frac{n(n+1)}{2}.
\]
The simply connected constant-curvature spaces attain this bound.

The [[lie-groups/lie-algebra|Lie algebra]] of $\operatorname{Isom}(M,g)$ is the space of complete Killing fields. On a complete [[differential-geometry/riemannian-manifold|Riemannian manifold]], every Killing field is complete.

A [[differential-geometry/riemannian-manifold|Riemannian manifold]] is homogeneous exactly when its [[topology/isometry|isometry]] [[algebra-groups/group|group]] has a transitive [[algebra-groups/subgroup|subgroup]].

### Holonomy groups

Fix $p\in M$. Parallel transport around piecewise smooth loops based at $p$ gives orthogonal maps of $T_pM$.

**Definition.**
The [[fiber-bundles/holonomy-group|holonomy group]] $\operatorname{Hol}_p(g)$ is the [[algebra-groups/subgroup|subgroup]] of $\mathrm O(T_pM)$ generated by these parallel transports.

The [[fiber-bundles/restricted-holonomy-group|restricted holonomy group]] uses loops homotopic to the constant loop. It is a connected [[lie-groups/lie-subgroup|Lie subgroup]]. [[fiber-bundles/holonomy-group|Holonomy groups]] at different points are conjugate by parallel transport.

**Theorem (Ambrose--Singer).**
The [[lie-groups/lie-algebra|Lie algebra]] of the [[fiber-bundles/restricted-holonomy-group|restricted holonomy group]] is generated by parallel translates of [[fiber-bundles/curvature|curvature]] [[algebra-category-theory/endomorphism-category|endomorphisms]]
\[
R_q(X,Y):T_qM\to T_qM.
\]

Thus [[fiber-bundles/curvature|curvature]] is the infinitesimal generator of holonomy. A simply connected [[differential-geometry/riemannian-manifold|Riemannian manifold]] is flat exactly when its holonomy is trivial.

Reductions of holonomy produce additional geometric structures. Examples include Kähler, Calabi--Yau, $G_2$, and $\mathrm{Spin}(7)$ structures.

### Limits on the relation between manifolds and Lie groups

The following distinctions prevent common errors.

1. Every [[fiber-bundles/lie-group|Lie group]] is a [[fiber-bundles/smooth-manifold|smooth manifold]]. Not every [[fiber-bundles/smooth-manifold|smooth manifold]] has a [[fiber-bundles/lie-group|Lie group]] structure.
1. Every [[fiber-bundles/lie-group|Lie group]] is parallelizable. Parallelizability alone does not give a [[algebra-groups/group|group]] law.
1. Every manifold has a principal frame bundle. The manifold itself need not be a principal bundle or a [[fiber-bundles/lie-group|Lie group]].
1. A homogeneous manifold is $G/H$. It is a [[fiber-bundles/lie-group|Lie group]] only when $H$ is normal.
1. Every [[fiber-bundles/lie-group|Lie group]] has left-invariant [[topology/metric|metrics]]. It need not have a bi-invariant [[differential-geometry/riemannian-manifold|Riemannian metric]].
1. A [[differential-geometry/riemannian-manifold|Riemannian metric]] has an [[topology/isometry|isometry]] [[fiber-bundles/lie-group|Lie group]]. This [[algebra-groups/group|group]] can be finite or discrete.

A positive-dimensional [[lie-groups/compact-lie-group|compact Lie group]] has Euler characteristic zero. A nonzero [[lie-groups/left-invariant-vector-field|left-invariant vector field]] gives this fact by the Poincaré--Hopf theorem. Thus $S^{2k}$ cannot be a positive-dimensional [[fiber-bundles/lie-group|Lie group]].

### Exercises

**Exercise.**
Derive the Levi-Civita formula for a left-invariant [[topology/metric|metric]] from the Koszul formula.

**Exercise.**
Prove that an $\operatorname{Ad}(G)$-invariant [[linear-algebra/inner-product|inner product]] gives a [[lie-groups/bi-invariant-metric|bi-invariant metric]].

**Exercise.**
For a [[lie-groups/bi-invariant-metric|bi-invariant metric]], derive
\[
R(X,Y)Z=-\frac14\left[\left[X,Y\right],Z\right].
\]

**Exercise.**
Prove that a [[lie-groups/connected-lie-group|connected Lie group]] with a bi-invariant flat [[topology/metric|metric]] is abelian.

**Exercise.**
Show that a $G$-invariant [[topology/metric|metric]] on $G/H$ is determined by its value at $eH$ and prove the isotropy-invariance condition.

 ## Hodge operators and geometric analysis

**Required concepts.** [[differential-geometry/riemannian-manifold|Riemannian metrics]], [[differential-geometry/orientation-of-a-smooth-manifold|orientation]], [[fiber-bundles/differential-k-form|differential forms]], [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]], divergence, and compactness.
**Result of this chapter.** The reader can use the [[differential-geometry/hodge-star-operator|Hodge star]], [[differential-geometry/codifferential|codifferential]], [[differential-geometry/hodge-laplacian|Hodge Laplacian]], and the compact Hodge decomposition theorem.

### Inner products on forms

A [[differential-geometry/riemannian-manifold|Riemannian metric]] gives an [[linear-algebra/inner-product|inner product]] on $\Lambda^kT_p^{*}M$. If $(e^1,\ldots,e^n)$ is an orthonormal coframe, then the forms
\[
e^{i_1}\wedge\cdots\wedge e^{i_k},
\qquad
i_1<\cdots<i_k,
\]
form an [[linear-algebra/orthonormal-basis|orthonormal basis]] of $\Lambda^kT_p^{*}M$.

For compactly supported $k$-forms on an oriented manifold, define the $L^2$ [[linear-algebra/inner-product|inner product]]
\[
(\alpha,\beta)_{L^2}
=
\int_M\left\langle \alpha,\beta\right\rangle\,d\operatorname{vol}_g.
\]

### The Hodge star

**Definition.**
The [[differential-geometry/hodge-star-operator|Hodge star]] is the [[fiber-bundles/bundle-isomorphism|bundle isomorphism]]
\[
*:\Lambda^kT^{*}M\to\Lambda^{n-k}T^{*}M
\]
defined by
\[
\alpha\wedge *\beta=\left\langle \alpha,\beta\right\rangle\operatorname{vol}_g.
\]

The [[topology/metric|metric]] and [[differential-geometry/orientation-of-a-smooth-manifold|orientation]] both enter this definition.

For a positive orthonormal coframe,
\[
*(e^{i_1}\wedge\cdots\wedge e^{i_k})
=
\varepsilon_{I,J}
e^{j_1}\wedge\cdots\wedge e^{j_{n-k}},
\]
where $(I,J)$ is a permutation of $(1,\ldots,n)$ and $\varepsilon_{I,J}$ is its sign.

The star satisfies
\[
*^2=(-1)^{k(n-k)}
\]
on $k$-forms.

### Codifferential

For a $k$-form, define
\[
\delta=(-1)^{n(k+1)+1}*d*.
\]
Then
\[
\delta:\Omega^k(M)\to\Omega^{k-1}(M).
\]

For compactly supported forms,
\[
(d\alpha,\beta)_{L^2}=(\alpha,\delta\beta)_{L^2}.
\]
Thus $\delta$ is the formal $L^2$ adjoint of $d$.

In a local orthonormal frame $(E_i)$,
\[
\delta\omega=-\sum_i\iota_{E_i}(\nabla_{E_i}\omega).
\]

For a [[fiber-bundles/vector-field|vector field]] $X$,
\[
\delta(X^{\flat})=-\operatorname{div} X.
\]

### Divergence and volume

The divergence is characterized by
\[
\mathcal{L}_X\operatorname{vol}_g=(\operatorname{div} X)\operatorname{vol}_g.
\]
Because $d\operatorname{vol}_g=0$, Cartan's formula gives
\[
\mathcal{L}_X\operatorname{vol}_g=d(\iota_X\operatorname{vol}_g).
\]

**Theorem (Divergence theorem).**
Let $M$ be a compact oriented [[differential-geometry/riemannian-manifold|Riemannian manifold]] with [[topology/boundary|boundary]]. Let $\nu$ be the outward unit normal. Then
\[
\int_M\operatorname{div} X\,d\operatorname{vol}_g
=
\int_{\partial M}g(X,\nu)\,d\operatorname{vol}_{\partial M}.
\]

This is Stokes's theorem applied to $\iota_X\operatorname{vol}_g$.

### Hodge Laplacian

**Definition.**
The [[differential-geometry/hodge-laplacian|Hodge Laplacian]] is
\[
\Delta_H=d\delta+\delta d.
\]

It preserves form degree. For [[shared-foundations/function|functions]],
\[
\Delta_Hf=\delta df=-\operatorname{div}(\operatorname{grad} f)=-\Delta f,
\]
where $\Delta=\operatorname{div}\operatorname{grad}$ is the sign convention from Chapter~14.

For compactly supported forms,
\[
(\Delta_H\omega,\omega)_{L^2}
=
\left\lVert d\omega\right\rVert_{L^2}^2
+
\left\lVert \delta\omega\right\rVert_{L^2}^2.
\]
Thus $\Delta_H$ is formally nonnegative.

**Definition.**
A form is [[differential-geometry/harmonic-differential-form|harmonic]] if
\[
\Delta_H\omega=0.
\]

On a compact manifold without [[topology/boundary|boundary]], this is equivalent to
\[
d\omega=0,
\qquad
\delta\omega=0.
\]

### Hodge decomposition

**Theorem (Hodge theorem).**
Let $M$ be compact, oriented, and without [[topology/boundary|boundary]]. Then
\[
\Omega^k(M)
=
\mathcal H^k
\oplus
d\Omega^{k-1}(M)
\oplus
\delta\Omega^{k+1}(M),
\]
where $\mathcal H^k$ is the finite-dimensional space of harmonic $k$-forms. The sum is orthogonal in $L^2$.

Each de Rham cohomology class has a unique harmonic representative. Therefore
\[
\mathcal H^k\cong H^k_{\mathrm{dR}}(M).
\]

This theorem connects [[topology/topology|topology]], analysis, and Riemannian geometry. The [[linear-algebra/vector-space|vector space]] $H^k_{\mathrm{dR}}(M)$ is independent of the [[topology/metric|metric]]. The harmonic representative depends on the [[topology/metric|metric]].

### Weitzenböck and Bochner formulas

The [[differential-geometry/hodge-laplacian|Hodge Laplacian]] and the [[fiber-bundles/connection-on-a-vector-bundle|connection]] Laplacian differ by [[fiber-bundles/curvature|curvature]] terms. This [[shared-foundations/relation|relation]] is a Weitzenböck formula.

For [[shared-foundations/function|functions]], the Bochner formula is
\[
\frac12\Delta\left\lVert \operatorname{grad} f\right\rVert^2
=
\left\lVert \operatorname{Hess}f\right\rVert^2
+g(\operatorname{grad} f,\operatorname{grad}\Delta f)
+\operatorname{Ric}(\operatorname{grad} f,\operatorname{grad} f).
\]

On a compact manifold, integration removes the left side. [[fiber-bundles/curvature|Curvature]] signs can then force rigidity.

**Corollary.**
Let $M$ be compact and connected. Each harmonic [[shared-foundations/function|function]] is constant.

*Proof.*
For $\Delta f=0$,
\[
0
=
\int_M f\Delta f\,d\operatorname{vol}_g
=
-\int_M\left\lVert \operatorname{grad} f\right\rVert^2\,d\operatorname{vol}_g
\]
after [[real-analysis/integration-by-parts|integration by parts]]. Thus $\operatorname{grad} f=0$.
 \(\square\)

**Corollary (Bochner vanishing).**
If $M$ is compact and has positive [[differential-geometry/ricci-curvature|Ricci curvature]], then each harmonic one-form is zero. Hence
\[
H^1_{\mathrm{dR}}(M)=0.
\]

The proof uses the Weitzenböck formula for one-forms.

### Gauss--Bonnet in dimension two

**Theorem (Gauss--Bonnet).**
Let $(M^2,g)$ be a compact oriented surface without [[topology/boundary|boundary]]. Then
\[
\int_M K\,d\operatorname{vol}_g=2\pi\chi(M).
\]

The left side uses the [[differential-geometry/riemannian-manifold|Riemannian metric]]. The right side is topological. This theorem gives a direct global [[shared-foundations/relation|relation]] between [[fiber-bundles/curvature|curvature]] and [[topology/topology|topology]].

For a surface with [[topology/boundary|boundary]], an additional [[topology/boundary|boundary]] geodesic-curvature term occurs.

### Characteristic forms from principal bundles

Let $P\to M$ be a principal $G$-bundle with [[fiber-bundles/connection-on-a-vector-bundle|connection]] [[fiber-bundles/curvature|curvature]] $\Omega$. An invariant [[real-analysis/polynomial|polynomial]] on the [[lie-groups/lie-algebra|Lie algebra]] gives a [[fiber-bundles/closed-differential-form|closed differential form]] built from $\Omega$. Its de Rham cohomology class does not depend on the selected [[fiber-bundles/connection-on-a-vector-bundle|connection]].

This is the Chern--Weil construction. It produces [[fiber-bundles/characteristic-class|characteristic classes]] such as Chern classes and Pontryagin classes. For the tangent frame bundle, these classes constrain possible manifold and bundle structures.

The Euler class of an oriented even-rank bundle has a [[fiber-bundles/curvature|curvature]] representative. The Gauss--Bonnet theorem is a special case for the [[fiber-bundles/tangent-bundle|tangent bundle]].

### End of the main dependency chain

The main structures now have the following order:
\[
\begin{gathered}
\text{smooth atlas}\longrightarrow TM,T^{*}M
\longrightarrow\text{tensor and frame bundles},\\
\text{Lie group}\longrightarrow\text{principal bundles and homogeneous spaces},\\
\text{Riemannian metric}\longleftrightarrow\mathrm O(n)\text{-reduction},\\
\text{Levi-Civita connection}\longrightarrow\text{geodesics, curvature, holonomy},\\
\text{metric plus orientation}\longrightarrow *,\delta,\Delta_H
\longrightarrow\text{Hodge theory}.
\end{gathered}
\]

### Exercises

**Exercise.**
Compute the [[differential-geometry/hodge-star-operator|Hodge star]] on $\mathbb{R}^3$ with its standard [[differential-geometry/orientation-of-a-smooth-manifold|orientation]] and [[topology/metric|metric]].

**Exercise.**
Prove that $\delta(X^{\flat})=-\operatorname{div} X$.

**Exercise.**
Prove the divergence theorem from Stokes's theorem.

**Exercise.**
On the flat torus $T^n$, determine all harmonic one-forms.

**Exercise.**
Use Gauss--Bonnet to show that a compact oriented surface with everywhere positive Gaussian [[fiber-bundles/curvature|curvature]] has positive Euler characteristic.

# Appendices
# Part: Appendices
## Analytic and topological input theorems

This appendix lists the major results that the notes use without full proof. Each statement includes the role that it has in the dependency chain.

### Completeness of the real numbers

The ordered [[algebra-rings/field|field]] $\mathbb{R}$ is complete. Each nonempty [[shared-foundations/subset|subset]] that has an [[shared-foundations/upper-bound|upper bound]] has a least [[shared-foundations/upper-bound|upper bound]].

This axiom gives the convergence results of real analysis. It supports compactness of closed bounded [[real-analysis/interval|intervals]], the [[real-analysis/mean-value-theorem|mean value theorem]], and existence results for differential equations.

### Heine--Borel theorem

A [[shared-foundations/subset|subset]] of $\mathbb{R}^n$ is compact if and only if it is closed and bounded.

This theorem supports compactly contained coordinate [[topology/neighborhood|neighborhoods]], [[differential-geometry/bump-function|bump functions]], and local [[topology/metric|metric]] comparison.

### Inverse and implicit function theorems

If a $C^1$ map $f:\mathbb{R}^n\to\mathbb{R}^n$ has invertible [[real-analysis/derivative|derivative]] at $a$, then it is a local $C^1$ [[fiber-bundles/diffeomorphism|diffeomorphism]] near $a$. Smooth input gives a smooth inverse.

If $F(x,y)=0$ and $D_yF$ is invertible, then the zero [[shared-foundations/set|set]] is locally the graph of a [[fiber-bundles/smooth-map|smooth map]] $y=g(x)$.

These theorems give local coordinate inverses, local submanifold graphs, and the [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphism]] property of [[fiber-bundles/exponential-map|exponential maps]].

### Constant-rank theorem

A [[fiber-bundles/smooth-map|smooth map]] of constant [[linear-algebra/rank|rank]] $r$ has local coordinate form
\[
(x^1,\ldots,x^n)
\mapsto
(x^1,\ldots,x^r,0,\ldots,0).
\]

This theorem gives the local forms of immersions and submersions. It also gives the [[fiber-bundles/regular-value|regular value]] theorem and the [[algebra-groups/orbit|orbit]] theorem.

### Ordinary differential equation theorem

A locally Lipschitz [[fiber-bundles/vector-field|vector field]] has unique local integral [[topology/curve|curves]]. Smooth [[fiber-bundles/vector-field|vector fields]] give smooth dependence on initial data.

This theorem gives flows, geodesics, parallel transport, Jacobi fields, and the Lie [[fiber-bundles/exponential-map|exponential map]].

### Invariance of domain

A continuous [[shared-foundations/injective-function|injective]] map from an open [[shared-foundations/subset|subset]] of $\mathbb{R}^n$ to $\mathbb{R}^n$ has open [[shared-foundations/image|image]] and is a [[topology/homeomorphism|homeomorphism]] onto its [[shared-foundations/image|image]].

This theorem supports invariance of manifold dimension and the interior-boundary distinction for manifolds with [[topology/boundary|boundary]].

### Paracompactness of manifolds

Each [[topology/hausdorff-space|Hausdorff]] second-countable locally [[linear-algebra/euclidean-space|Euclidean space]] is [[fiber-bundles/paracompact-topological-space|paracompact]].

Combined with local [[differential-geometry/bump-function|bump functions]], this theorem gives smooth [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partitions of unity]]. [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|Partitions of unity]] give global [[differential-geometry/riemannian-manifold|Riemannian metrics]], [[fiber-bundles/bundle-metric|bundle metrics]], and [[fiber-bundles/connection-on-a-vector-bundle|connections]].

### Closed subgroup theorem

Each closed [[algebra-groups/subgroup|subgroup]] of a finite-dimensional [[fiber-bundles/lie-group|Lie group]] is an embedded [[lie-groups/lie-subgroup|Lie subgroup]].

This theorem gives manifold structures on [[algebra-groups/stabilizer|stabilizers]] and quotients $G/H$.

### Free proper quotient theorem

A smooth free [[lie-groups/proper-action-lie|proper action]] of a [[fiber-bundles/lie-group|Lie group]] $G$ on a manifold $M$ gives a smooth quotient $M/G$. The quotient map is a submersion and a principal $G$-bundle.

This theorem gives quotient manifolds and many principal bundles.

### Haar measure

Each [[topology/locally-compact-group|locally compact group]] has a nonzero left-invariant regular [[measure-theory/measure|measure]], unique up to scale. A compact [[algebra-groups/group|group]] has a normalized bi-invariant [[probability/probability-measure|probability measure]].

This theorem permits averaging over [[lie-groups/compact-lie-group|compact Lie groups]]. Averaging gives invariant [[topology/metric|metrics]] and invariant [[linear-algebra/inner-product|inner products]].

### Hopf--Rinow theorem

For a connected [[differential-geometry/riemannian-manifold|Riemannian manifold]], [[topology/metric|metric]] completeness, geodesic completeness, global definition of the [[fiber-bundles/exponential-map|exponential map]], and compactness of closed [[topology/bounded-set|bounded sets]] are equivalent. Completeness also gives minimizing geodesics between each pair of points.

This theorem connects local geodesic ODEs with global distance geometry.

### Tubular neighborhood theorem

An [[differential-geometry/embedded-submanifold|embedded submanifold]] has a [[topology/neighborhood|neighborhood]] diffeomorphic to a [[topology/neighborhood|neighborhood]] of the [[fiber-bundles/zero-section|zero section]] in its [[differential-geometry/normal-bundle|normal bundle]].

This theorem gives normal coordinates around a submanifold.

### Myers--Steenrod theorem

The [[topology/isometry|isometry]] [[algebra-groups/group|group]] of a connected [[differential-geometry/riemannian-manifold|Riemannian manifold]] is a finite-dimensional [[fiber-bundles/lie-group|Lie group]], and its action is smooth.

This theorem converts [[topology/metric|metric]] symmetry into [[fiber-bundles/lie-group|Lie group]] symmetry.

### Ambrose--Singer theorem

The restricted holonomy [[lie-groups/lie-algebra|Lie algebra]] is generated by parallel translates of [[fiber-bundles/curvature|curvature]] [[algebra-category-theory/endomorphism-category|endomorphisms]].

This theorem connects local [[fiber-bundles/curvature|curvature]] with the global [[fiber-bundles/lie-group|Lie group]] of parallel transport.

### Nash embedding theorem

Each smooth [[differential-geometry/riemannian-manifold|Riemannian manifold]] has a smooth isometric embedding into some [[linear-algebra/euclidean-space|Euclidean space]].

This theorem permits an extrinsic realization of every intrinsic [[differential-geometry/riemannian-manifold|Riemannian metric]].

### Hodge theorem

On a compact oriented [[differential-geometry/riemannian-manifold|Riemannian manifold]] without [[topology/boundary|boundary]], each de Rham cohomology class has a unique harmonic representative.

This theorem connects elliptic analysis with [[topology/topology|topology]].

### Dependency table

| Input theorem | Main uses |
| --- | --- |
| [[shared-foundations/inverse-function|Inverse function]] theorem | Chart inverses, [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphisms]], [[fiber-bundles/exponential-map|exponential map]]. |
| [[real-analysis/implicit-function-theorem|Implicit function theorem]] | Local level-set graphs, submanifold models. |
| Constant-rank theorem | Immersions, submersions, [[fiber-bundles/regular-value|regular values]], [[algebra-groups/orbit|orbits]]. |
| ODE theorem | Flows, parallel transport, geodesics, [[fiber-bundles/exponential-map|exponential maps]]. |
| Paracompactness | [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|Partitions of unity]], global [[topology/metric|metrics]], bundle [[fiber-bundles/connection-on-a-vector-bundle|connections]]. |
| [[lie-groups/closed-subgroup-theorem|Closed subgroup theorem]] | [[algebra-groups/stabilizer|Stabilizers]], $G/H$, [[linear-algebra/matrix|matrix]] [[lie-groups/lie-subgroup|Lie subgroups]]. |
| Free proper quotient theorem | Smooth [[lie-groups/orbit-space|orbit spaces]] and principal bundles. |
| [[harmonic-analysis/haar-measure|Haar measure]] | Compact-group averaging and [[lie-groups/bi-invariant-metric|bi-invariant metrics]]. |
| Hopf--Rinow | Completeness and minimizing geodesics. |
| Myers--Steenrod | [[topology/isometry|Isometry]] [[algebra-groups/group|groups]] as [[fiber-bundles/lie-group|Lie groups]]. |
| Ambrose--Singer | [[fiber-bundles/curvature|Curvature]] generation of holonomy. |
| [[differential-geometry/hodge-theorem|Hodge theorem]] | Harmonic representatives of cohomology classes. |

 ## Definitions, symbols, and formula summary

### Core structures

| Structure | Data | Main compatibility |
| --- | --- | --- |
| [[topology/topological-manifold|Topological manifold]] | [[topology/hausdorff-space|Hausdorff]], second-countable, locally [[linear-algebra/euclidean-space|Euclidean space]] | Charts are [[topology/homeomorphism|homeomorphisms]] to Euclidean open [[shared-foundations/set|sets]]. |
| [[fiber-bundles/smooth-manifold|Smooth manifold]] | [[topology/topological-manifold|Topological manifold]] and maximal [[fiber-bundles/smooth-atlas|smooth atlas]] | Transition maps are smooth [[fiber-bundles/diffeomorphism|diffeomorphisms]]. |
| [[fiber-bundles/lie-group|Lie group]] | [[fiber-bundles/smooth-manifold|Smooth manifold]] and [[algebra-groups/group|group]] law | Multiplication and inversion are smooth. |
| Fiber bundle | $E\xrightarrow{\pi}B$ with fiber $F$ | Local products preserve $\pi$. |
| [[fiber-bundles/vector-bundle|Vector bundle]] | Fiber bundle with [[linear-algebra/vector-space|vector-space]] fibers | Transition maps lie in $\operatorname{GL}(k,\mathbb{R})$. |
| Principal bundle | Right $G$-space $P\to B$ | $G$ acts freely and transitively on fibers. |
| [[differential-geometry/riemannian-manifold|Riemannian metric]] | $g\in\Gamma(\operatorname{Sym}^2T^{*}M)$ | Each $g_p$ is positive definite. |
| [[fiber-bundles/connection-on-a-vector-bundle|Connection]] | $\nabla_Xs$ | Tensorial in $X$ and Leibniz in $s$. |
| [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] | [[fiber-bundles/connection-on-a-vector-bundle|Connection]] on $TM$ | Zero [[fiber-bundles/torsion-2-form|torsion]] and $\nabla g=0$. |
| [[fiber-bundles/curvature|Curvature]] | $R(X,Y)=\left[\nabla_X,\nabla_Y\right]-\nabla_{[X,Y]}$ | Tensorial and skew in $X,Y$. |

### Main manifold--Lie group correspondences

| Geometric object | [[fiber-bundles/lie-group|Lie-group]] formulation |
| --- | --- |
| [[fiber-bundles/lie-group|Lie group]] | [[algebra-groups/group|Group]] [[algebra-category-theory/object|object]] in the [[differential-geometry/category-of-smooth-manifolds|category of smooth manifolds]]. |
| [[lie-groups/lie-algebra|Lie algebra]] of $G$ | $T_eG$ with bracket from [[lie-groups/left-invariant-vector-field|left-invariant vector fields]]. |
| Homogeneous manifold | Quotient $G/H$ for a closed [[algebra-groups/stabilizer|stabilizer]] $H$. |
| Principal $G$-bundle | Fiber bundle with a free transitive right $G$-action on each fiber. |
| Rank-$n$ [[fiber-bundles/vector-bundle|vector bundle]] | [[fiber-bundles/associated-bundle|Associated bundle]] of a principal $\operatorname{GL}(n,\mathbb{R})$-bundle. |
| [[fiber-bundles/tangent-bundle|Tangent bundle]] | $\operatorname{Fr}(M)\times_{\operatorname{GL}(n)}\mathbb{R}^n$. |
| [[differential-geometry/orientation-of-a-smooth-manifold|Orientation]] | Reduction of $\operatorname{Fr}(M)$ to $\operatorname{GL}^{+}(n,\mathbb{R})$. |
| [[differential-geometry/riemannian-manifold|Riemannian metric]] | Reduction of $\operatorname{Fr}(M)$ to $\mathrm O(n)$. |
| [[topology/metric|Metric]] [[fiber-bundles/connection-on-a-vector-bundle|connection]] | Principal $\mathrm O(n)$-connection on orthonormal frames. |
| [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] | Unique torsion-free principal $\mathrm O(n)$-connection. |
| Invariant [[topology/metric|metric]] on $G/H$ | $\operatorname{Ad}(H)$-invariant [[linear-algebra/inner-product|inner product]] on $\mathfrak g/\mathfrak h$. |
| [[topology/isometry|Isometry]] [[algebra-groups/group|group]] | [[fiber-bundles/lie-group|Lie group]] by Myers--Steenrod. |
| Holonomy | [[lie-groups/lie-subgroup|Lie subgroup]] of $\mathrm O(T_pM)$ generated by parallel transport. |

### Coordinate formulas

For a [[fiber-bundles/smooth-map|smooth map]] $F:M\to N$,
\[
dF_p(\partial_i)
=
\frac{\partial F^\alpha}{\partial x^i}\partial_{y^\alpha}.
\]

For [[fiber-bundles/vector-field|vector fields]] $X=X^i\partial_i$ and $Y=Y^i\partial_i$,
\[
[X,Y]^k=X^i\partial_iY^k-Y^i\partial_iX^k.
\]

For a [[topology/metric|metric]] $g=g_{ij}\,dx^i\otimes dx^j$,
\[
\Gamma^k{}_{ij}
=
\frac12g^{k\ell}
\left(
\partial_ig_{j\ell}
+\partial_jg_{i\ell}
-\partial_\ell g_{ij}
\right).
\]

For a field $V=V^k\partial_k$ along $\gamma$,
\[
\frac{DV^k}{dt}
=
\dot V^k+\Gamma^k{}_{ij}\dot\gamma^iV^j.
\]
The geodesic equation is
\[
\ddot\gamma^k+\Gamma^k{}_{ij}\dot\gamma^i\dot\gamma^j=0.
\]

The [[fiber-bundles/curvature|curvature]] components are
\[
R^\ell{}_{kij}
=
\partial_i\Gamma^\ell{}_{jk}
-\partial_j\Gamma^\ell{}_{ik}
+\Gamma^m{}_{jk}\Gamma^\ell{}_{im}
-\Gamma^m{}_{ik}\Gamma^\ell{}_{jm}.
\]

The [[real-analysis/gradient|gradient]] and Laplacian are
\[
\operatorname{grad} f=g^{ij}(\partial_jf)\partial_i,
\]
and
\[
\Delta f
=
\frac{1}{\sqrt{\det g}}
\partial_i\left(\sqrt{\det g}\,g^{ij}\partial_jf\right).
\]

The volume form in positive coordinates is
\[
\operatorname{vol}_g=\sqrt{\det g}\,dx^1\wedge\cdots\wedge dx^n.
\]

### Invariant metric formulas on Lie groups

For a left-invariant [[topology/metric|metric]],
\[
2\left\langle \nabla_XY,Z\right\rangle
=
\left\langle [X,Y],Z\right\rangle
-\left\langle [Y,Z],X\right\rangle
+\left\langle [Z,X],Y\right\rangle.
\]

For a [[lie-groups/bi-invariant-metric|bi-invariant metric]],
\[
\nabla_XY=\frac12[X,Y],
\]
\[
R(X,Y)Z=-\frac14\left[\left[X,Y\right],Z\right],
\]
and
\[
K(X,Y)=\frac14\left\lVert [X,Y]\right\rVert^2
\]
for orthonormal $X,Y$.

### Submanifold formulas

The Gauss and Weingarten formulas are
\[
\overline\nabla_XY=\nabla_XY+\mathrm{II}(X,Y),
\]
\[
\overline\nabla_X\xi=-A_\xi X+\nabla_X^{\perp}\xi.
\]

The shape operator satisfies
\[
g(A_\xi X,Y)=\overline g(\mathrm{II}(X,Y),\xi).
\]

The Gauss equation is
\[
\overline{\operatorname{Rm}}(X,Y,Z,W)
=
\operatorname{Rm}(X,Y,Z,W)
+\inner{\mathrm{II}(X,W)}{\mathrm{II}(Y,Z)}
-\inner{\mathrm{II}(X,Z)}{\mathrm{II}(Y,W)}.
\]

### Common distinctions

1. A chart is one coordinate map. An atlas is a compatible collection. A [[fiber-bundles/smooth-atlas|smooth structure]] is a maximal atlas.
1. A [[fiber-bundles/tangent-space-at-a-point|tangent vector]] is intrinsic. Its coordinate components depend on a chart.
1. An immersion is locally [[shared-foundations/injective-function|injective]] to first order. An embedding also has the [[topology/subspace-topology|subspace topology]] on its [[shared-foundations/image|image]].
1. A submersion has [[shared-foundations/surjective-function|surjective]] differential. A quotient map need not be a submersion without a smooth quotient theorem.
1. A [[fiber-bundles/vector-bundle|vector-bundle]] fiber has a [[linear-algebra/vector-space|vector-space]] origin. A principal-bundle fiber has no selected identity.
1. A [[fiber-bundles/connection-on-a-vector-bundle|connection]] is not a tensor. The difference of two [[fiber-bundles/connection-on-a-vector-bundle|connections]] is a tensor.
1. Christoffel symbols are not tensor components. [[fiber-bundles/curvature|Curvature]] components are tensor components.
1. A [[differential-geometry/riemannian-manifold|Riemannian metric]] tensor is not the same object as its induced distance [[shared-foundations/function|function]].
1. The Lie exponential and Riemannian exponential can differ on the same [[fiber-bundles/lie-group|Lie group]].
1. A [[lie-groups/homogeneous-space|homogeneous space]] $G/H$ is a [[algebra-groups/group|group]] only when $H$ is normal.

### Symbol list

| Symbol | Meaning |
| --- | --- |
| $T_pM$ | [[differential-geometry/tangent-space|Tangent space]] at $p$. |
| $T_p^{*}M$ | Cotangent space at $p$. |
| $TM,T^{*}M$ | Tangent and [[fiber-bundles/cotangent-bundle|cotangent bundles]]. |
| $\mathfrak X(M)$ | Smooth [[fiber-bundles/vector-field|vector fields]] on $M$. |
| $\Omega^k(M)$ | Smooth differential $k$-forms. |
| $dF_p$ | Differential of $F$ at $p$. |
| $F^{*}$ | [[algebra-category-theory/pullback|Pullback]] of covariant tensors, forms, or bundles. |
| $\operatorname{Fr}(E)$ | Frame bundle of a [[fiber-bundles/vector-bundle|vector bundle]] $E$. |
| $\mathfrak g$ | [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]] $G$. |
| $\exp_G$ | Lie [[fiber-bundles/exponential-map|exponential map]]. |
| $\exp_p$ | Riemannian [[fiber-bundles/exponential-map|exponential map]] at $p$. |
| $\operatorname{Ad},\operatorname{ad}$ | [[algebra-groups/group|Group]] and [[lie-groups/lie-algebra|Lie-algebra]] adjoint representations. |
| $\nabla$ | [[fiber-bundles/connection-on-a-vector-bundle|Connection]] or [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]]. |
| $R,\operatorname{Rm}$ | [[fiber-bundles/curvature|Curvature]] [[algebra-category-theory/endomorphism-category|endomorphism]] and covariant [[differential-geometry/riemann-curvature-tensor|Riemann tensor]]. |
| $K,\operatorname{Ric},\operatorname{Scal}$ | Sectional, Ricci, and scalar [[fiber-bundles/curvature|curvature]]. |
| $\mathrm{II},A_\xi,H$ | Second fundamental form, shape operator, mean [[fiber-bundles/curvature|curvature]] vector. |
| $*,\delta,\Delta_H$ | [[differential-geometry/hodge-star-operator|Hodge star]], [[differential-geometry/codifferential|codifferential]], and [[differential-geometry/hodge-laplacian|Hodge Laplacian]]. |

 ## Selected exercise solutions

These solutions show proof patterns. They do not replace full work on the other exercises.

### Double dual

Define $\iota:V\to V^{**}$ by
\[
\iota(v)(\lambda)=\lambda(v).
\]
The map is linear. If $v\neq0$, extend $v$ to a basis and select the first dual-basis covector $\lambda$. Then $\lambda(v)\neq0$. Thus $\iota(v)\neq0$, so $\iota$ is [[shared-foundations/injective-function|injective]]. Finite dimension gives
\[
\dim V=\dim V^{**}.
\]
Therefore $\iota$ is an [[algebra-category-theory/isomorphism-category|isomorphism]].

### Implicit graph of the circle

Let
\[
F(x,y)=x^2+y^2-1.
\]
At $(0,1)$,
\[
\frac{\partial F}{\partial y}=2.
\]
The [[real-analysis/implicit-function-theorem|implicit function theorem]] gives $y=g(x)$ near $x=0$. The branch is
\[
g(x)=\sqrt{1-x^2}.
\]
Differentiate $F(x,g(x))=0$:
\[
2x+2g(x)g'(x)=0.
\]
Thus $g'(0)=0$.

### The quotient $\mathbb{R}/\mathbb{Z}$

Define
\[
F:\mathbb{R}/\mathbb{Z}\to S^1,
\qquad
F([t])=e^{2\pi\mathrm{i} t}.
\]
The formula is well-defined because integer translation does not change the exponential. It is continuous by the quotient universal property. It is [[shared-foundations/bijective-function|bijective]]. The [[shared-foundations/domain|domain]] is compact, and the target is [[topology/hausdorff-space|Hausdorff]]. Thus $F$ is a [[topology/homeomorphism|homeomorphism]].

### Smooth maps into a product

Let $F:P\to M\times N$. If $F$ is smooth, then the component maps
\[
F_M=\operatorname{pr}_M\circ F,
\qquad
F_N=\operatorname{pr}_N\circ F
\]
are smooth.

Conversely, suppose that both components are smooth. In product charts, the coordinate representation of $F$ is the [[shared-foundations/ordered-pair|ordered pair]] of the two smooth coordinate representations. Thus it is smooth.

### Tangent bundle of a product

Define
\[
\Phi:T(M\times N)\to TM\times TN
\]
by
\[
\Phi(v)=\bigl(d\operatorname{pr}_M(v),d\operatorname{pr}_N(v)\bigr).
\]
At $(p,q)$, the map is the linear [[algebra-category-theory/isomorphism-category|isomorphism]]
\[
T_{(p,q)}(M\times N)\to T_pM\oplus T_qN.
\]
Product charts show that $\Phi$ and its inverse are smooth. It is a [[fiber-bundles/vector-bundle|vector-bundle]] [[algebra-category-theory/isomorphism-category|isomorphism]] over $M\times N$.

### The orthogonal group

Define
\[
F:M_n(\mathbb{R})\to\operatorname{Sym}_n(\mathbb{R}),
\qquad
F(A)=A^{T}A.
\]
Then $\mathrm O(n)=F^{-1}(I)$. The [[real-analysis/derivative|derivative]] is
\[
dF_A(H)=H^{T}A+A^{T}H.
\]
At $A\in\mathrm O(n)$, each symmetric [[linear-algebra/matrix|matrix]] $S$ is obtained from
\[
H=\frac12AS,
\]
because
\[
H^{T}A+A^{T}H=S.
\]
Thus $dF_A$ is [[shared-foundations/surjective-function|surjective]]. The [[fiber-bundles/regular-value|regular value]] theorem gives the [[differential-geometry/embedded-submanifold|embedded submanifold]]. At $I$,
\[
T_I\mathrm O(n)
=
\operatorname{ker} dF_I
=
\left\{H:H^{T}+H=0\right\}.
\]

### Rotation field flow

For
\[
X=x\partial_y-y\partial_x,
\]
the integral-curve equations are
\[
\dot x=-y,
\qquad
\dot y=x.
\]
The solution through $(x_0,y_0)$ is
\[
\Phi_t(x_0,y_0)
=
(x_0\cos t-y_0\sin t,
 x_0\sin t+y_0\cos t).
\]
It is defined for all $t$. Thus $X$ is complete.

### Lie derivative and exterior derivative

Cartan's formula gives
\[
\mathcal{L}_X=d\iota_X+\iota_Xd.
\]
Then
\[
d\mathcal{L}_X
=d(d\iota_X+\iota_Xd)
=d\iota_Xd
\]
because $d^2=0$. Also,
\[
\mathcal{L}_Xd
=(d\iota_X+\iota_Xd)d
=d\iota_Xd.
\]
Thus
\[
d\mathcal{L}_X=\mathcal{L}_Xd.
\]

### Trivial line bundles

Suppose that a [[fiber-bundles/line-bundle|real line bundle]] $L\to B$ has a [[fiber-bundles/nowhere-vanishing-section|nowhere-zero section]] $s$. Define
\[
B\times\mathbb{R}\to L,
\qquad
(b,t)\mapsto ts(b).
\]
This is a smooth fiberwise linear bijection. Local bundle coordinates show that its inverse is smooth. Thus $L$ is trivial.

A trivial [[fiber-bundles/line-bundle|line bundle]] has the [[fiber-bundles/nowhere-vanishing-section|nowhere-zero section]] $b\mapsto(b,1)$.

### Trivial principal bundles

Suppose that $P\to M$ has a [[fiber-bundles/section-of-a-fiber-bundle|global section]] $s$. Define
\[
M\times G\to P,
\qquad
(x,g)\mapsto s(x)g.
\]
The [[fiber-bundles/principal-action|principal action]] is free and transitive on each fiber, so the map is [[shared-foundations/bijective-function|bijective]]. [[fiber-bundles/local-trivialization|Local trivializations]] show that it is a [[fiber-bundles/diffeomorphism|diffeomorphism]] and a principal-bundle [[algebra-category-theory/isomorphism-category|isomorphism]].

Conversely, a [[fiber-bundles/trivial-principal-bundle-mgm|trivial principal bundle]] has the section $x\mapsto(x,e)$.

### Abelian connected Lie groups

If $G$ is abelian, then its [[lie-groups/lie-algebra|Lie algebra]] bracket is zero.

Suppose that $G$ is connected and $\mathfrak g$ has zero bracket. Then
\[
\operatorname{Ad}_{\exp X}=\exp(\operatorname{ad}_X)=I.
\]
The exponential [[shared-foundations/image|image]] contains a [[topology/neighborhood|neighborhood]] of the identity. Thus elements near the identity commute with all elements in the identity component. These elements generate the connected [[algebra-groups/group|group]]. Therefore $G$ is abelian.

### Compact free actions are proper

Let a [[lie-groups/compact-lie-group|compact Lie group]] $G$ act on $M$. Consider
\[
\Psi:G\times M\to M\times M,
\qquad
\Psi(g,p)=(g\cdot p,p).
\]
Let $K\subseteq M\times M$ be compact. Its projection to the second factor is compact. Then
\[
\Psi^{-1}(K)\subseteq G\times\operatorname{pr}_2(K).
\]
The [[shared-foundations/set|set]] on the right is compact. The inverse [[shared-foundations/image|image]] is closed because $K$ is closed and $\Psi$ is continuous. Thus $\Psi^{-1}(K)$ is compact. The action is proper. Freeness is not needed for this part.

### Conformal gradient

Let $\widetilde g=e^{2f}g$. By definition,
\[
\widetilde g(\operatorname{grad}_{\widetilde g}u,X)=du(X).
\]
Also,
\[
\begin{aligned}
du(X)
&=g(\operatorname{grad}_gu,X)\\
&=e^{2f}g(e^{-2f}\operatorname{grad}_gu,X)\\
&=\widetilde g(e^{-2f}\operatorname{grad}_gu,X).
\end{aligned}
\]
Nondegeneracy gives
\[
\operatorname{grad}_{\widetilde g}u=e^{-2f}\operatorname{grad}_gu.
\]

### Parallel transport preserves the metric

Let $V$ and $W$ be parallel fields along $\gamma$. Then
\[
\frac{d}{dt}g(V,W)
=(\nabla_{\dot\gamma}g)(V,W)
+g(DV/dt,W)
+g(V,DW/dt)
=0.
\]
Thus $g(V(t),W(t))$ is constant. The [[fiber-bundles/parallel-transport|parallel-transport]] map preserves [[linear-algebra/inner-product|inner products]].

### Isometries preserve geodesics

Let $F:(M,g)\to(N,h)$ be an [[topology/isometry|isometry]]. The [[algebra-category-theory/pullback|pullback]] of the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] of $h$ is torsion-free and compatible with $g$. Uniqueness of the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] gives
\[
dF(\nabla_XY)
=
\nabla^N_{dF(X)}dF(Y).
\]
For a geodesic $\gamma$,
\[
\frac{D}{dt}\frac{d}{dt}(F\circ\gamma)
=
dF\left(\frac{D\dot\gamma}{dt}\right)
=0.
\]
Thus $F\circ\gamma$ is a geodesic with the same affine parameter.

### Constant curvature contraction

Assume
\[
R(X,Y)Z
=c\bigl(g(Y,Z)X-g(X,Z)Y\bigr).
\]
For an [[linear-algebra/orthonormal-basis|orthonormal basis]] $(E_i)$,
\[
\begin{aligned}
\operatorname{Ric}(X,Y)
&=\sum_i g(R(E_i,X)Y,E_i)\\
&=c\sum_i\bigl(g(X,Y)-g(E_i,Y)g(X,E_i)\bigr)\\
&=(n-1)c\,g(X,Y).
\end{aligned}
\]
Taking the [[linear-algebra/trace|trace]] gives
\[
\operatorname{Scal}=n(n-1)c.
\]

### The round sphere

For the sphere of radius $r$, the outward unit normal is
\[
\nu(p)=\frac{p}{r}.
\]
Then
\[
\overline\nabla_X\nu=\frac1rX.
\]
The Weingarten formula gives
\[
A=-\frac1r\operatorname{id}.
\]
Therefore
\[
\mathrm{II}(X,Y)=-\frac1r g(X,Y)\nu,
\qquad
H=-\frac1r\nu.
\]
The Gauss equation gives sectional [[fiber-bundles/curvature|curvature]] $1/r^2$.

### Bi-invariant curvature

For left-invariant fields under a [[lie-groups/bi-invariant-metric|bi-invariant metric]],
\[
\nabla_XY=\frac12[X,Y].
\]
Then
\[
\begin{aligned}
R(X,Y)Z
&=\frac14[X,[Y,Z]]
-\frac14[Y,[X,Z]]
-\frac12\left[\left[X,Y\right],Z\right]\\
&=-\frac14\left[\left[X,Y\right],Z\right]
\end{aligned}
\]
by the Jacobi identity.

For orthonormal $X,Y$,
\[
\begin{aligned}
K(X,Y)
&=-\frac14\left\langle \left[\left[X,Y\right],Y\right],X\right\rangle\\
&=\frac14\left\langle [X,Y],[X,Y]\right\rangle.
\end{aligned}
\]

### Harmonic one-forms on a flat torus

Write the flat torus as $T^n=\mathbb{R}^n/\mathbb{Z}^n$. The coordinate one-forms $dx^1,\ldots,dx^n$ descend to global parallel one-forms. They are closed and coclosed. Thus they are harmonic.

Hodge theory gives
\[
\dim\mathcal H^1(T^n)
=
\dim H^1_{\mathrm{dR}}(T^n)
=n.
\]
Therefore every harmonic one-form is a constant [[convex-analysis/linear-combination|linear combination]]
\[
a_1dx^1+\cdots+a_ndx^n.
\]
 ## References and reading [[topology/path|paths]]

### Primary references

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd edition, Springer, 2013.

1. John M. Lee, *Introduction to Riemannian Manifolds*, 2nd edition, Springer, 2018.

1. Loring W. Tu, *An Introduction to Manifolds*, 2nd edition, Springer, 2011.

1. Manfredo P. do Carmo, *Riemannian Geometry*, Birkhäuser, 1992.

1. Peter Petersen, *Riemannian Geometry*, 3rd edition, Springer, 2016.

1. Frank W. Warner, *Foundations of Differentiable Manifolds and Lie Groups*, Springer, 1983.

1. Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd edition, Springer, 2015.

1. Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Volumes I and II, Wiley, 1963 and 1969.

1. David Bleecker, *Gauge Theory and Variational Principles*, Dover, 2005.

1. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982.

1. ASD Simplified Technical English Maintenance [[algebra-groups/group|Group]], *ASD-STE100 Simplified Technical English: Standard for Technical Documentation*, Issue 9, 2025.

### Reading paths

For a first course in [[fiber-bundles/smooth-manifold|smooth manifolds]], read Chapters 1--8. Then read Chapters 9--12 for bundles and [[fiber-bundles/lie-group|Lie groups]].

For a first course in Riemannian geometry, review Chapters 4--8. Then read Chapters 13--17.

For invariant geometry, read Chapters 9--12 and Chapter~18.

For geometric analysis, read Chapters 13--16 and Chapter~19.

For [[fiber-bundles/gauge-theory|gauge theory]], read Chapters 8--12, then study [[fiber-bundles/principal-connection|principal connections]], [[fiber-bundles/curvature|curvature]] forms, and Chern--Weil theory in more depth.

### Further topics

The next topics depend on the material in these notes:

1. Morse theory and geodesic index theory.
1. Comparison geometry and global [[fiber-bundles/curvature|curvature]] bounds.
1. Symplectic and Kähler geometry.
1. [[fiber-bundles/characteristic-class|Characteristic classes]] and Chern--Weil theory.
1. [[fiber-bundles/spin-structure|Spin structures]] and [[noncommutative-geometry/dirac-operator|Dirac operators]].
1. Geometric [[measure-theory/measure|measure]] theory and minimal submanifolds.
1. Ricci flow and geometric evolution equations.
1. Representation theory of [[lie-groups/compact-lie-group|compact Lie groups]].
1. Symmetric spaces and holonomy classification.
