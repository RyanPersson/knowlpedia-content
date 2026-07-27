+++
id = "algebra-homological/ext"
title = "Ext"
kind = "knowl"
summary = "The right derived functors of Hom; measures extension classes and failure of exactness of Hom."
aliases = ["ext"]
domains = ["algebra-homological"]
legacy_source_path = "algebra-homological/ext.md"
+++

Let $R$ be a [[algebra-rings/ring|ring]] and let $M,N$ be left [[algebra-modules/module|$R$-modules]].

For $n\ge 0$, the group $\operatorname{Ext}^n_R(M,N)$ is the $n$-th [[algebra-homological/derived-functor|right derived functor]] of $\operatorname{Hom}_R(-,N)$, evaluated at $M$. It may be computed from a projective resolution of $M$:
$$
\operatorname{Ext}^n_R(M,N)
=H^n\!\bigl(\operatorname{Hom}_R(P_\bullet,N)\bigr).
$$

## Computation from a projective resolution

Choose a [[algebra-homological/projective-resolution|projective resolution]] $P_\bullet \to M$:
$$
\cdots \to P_2 \xrightarrow{d_2} P_1 \xrightarrow{d_1} P_0 \to M \to 0
$$
with each $P_i$ projective. Applying [[algebra-modules/hom-module|$\operatorname{Hom}_R(-,N)$]] gives the [[algebra-homological/cochain-complex|cochain complex]]
$$
0 \to \mathrm{Hom}_R(P_0,N) \xrightarrow{d_1^*} \mathrm{Hom}_R(P_1,N) \xrightarrow{d_2^*} \mathrm{Hom}_R(P_2,N) \to \cdots.
$$
Here $H^n(-)$ denotes [[algebra-homological/cohomology-module|cohomology]].

This construction is independent of the chosen resolution up to canonical isomorphism. It is functorial: $\operatorname{Ext}^n_R(-,N)$ is contravariant in the first variable and $\operatorname{Ext}^n_R(M,-)$ is covariant in the second.

## Equivalent definition (via an injective resolution)
Alternatively, choose an [[algebra-homological/injective-resolution|injective resolution]] $N\to I^\bullet$ and set
$$
\mathrm{Ext}^n_R(M,N) \;:=\; H^n\!\big(\mathrm{Hom}_R(M,I^\bullet)\big).
$$

In either approach, $\operatorname{Ext}^0_R(M,N)\cong\operatorname{Hom}_R(M,N)$.

## Conceptual meaning
- $\operatorname{Ext}^1_R(M,N)$ classifies extensions
  $$
  0 \to N \to E \to M \to 0
  $$
  up to the usual equivalence relation; see [[algebra-homological/ext1-classifies-extensions|Ext^1 classifies extensions]].
- Higher $\operatorname{Ext}^n$ groups can be viewed as higher obstructions.
- A [[algebra-modules/short-exact-sequence|short exact sequence]] in either variable yields a [[algebra-homological/long-exact-sequence-ext|long exact sequence in Ext]], which is a special case of [[algebra-homological/long-exact-sequence-derived|the long exact sequence for derived functors]].

## Examples

### Example 1: Vector spaces over a field
Let $k$ be a field and $V,W$ be $k$-vector spaces. Every $k$-module is free, so a projective resolution can be taken to have length $0$. Therefore,
$$
\mathrm{Ext}^n_k(V,W)=0 \quad (n>0), \qquad \mathrm{Ext}^0_k(V,W)=\mathrm{Hom}_k(V,W).
$$

### Example 2: $\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,A)\cong A/nA$
Take the standard projective resolution of $\mathbb Z/n$:
$$
0 \to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n \to 0.
$$
Apply $\operatorname{Hom}_{\mathbb Z}(-,A)$:
$$
0 \to \mathrm{Hom}(\mathbb Z/n,A) \to \mathrm{Hom}(\mathbb Z,A)\xrightarrow{\times n} \mathrm{Hom}(\mathbb Z,A)\to \mathrm{Ext}^1(\mathbb Z/n,A)\to 0.
$$
Using $\operatorname{Hom}(\mathbb Z,A)\cong A$, the last map shows
$$
\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n,A)\;\cong\; \mathrm{coker}(A \xrightarrow{\times n} A)\;\cong\; A/nA.
$$
In particular, $\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z)\cong\mathbb Z/n$.

### Example 3: $\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)$
Taking $A=\mathbb Z/m$ in the preceding example gives
$$
\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\cong (\mathbb Z/m)/n(\mathbb Z/m)\cong \mathbb Z/\gcd(n,m).
$$

For these cyclic $\mathbb Z$-modules, $\operatorname{Ext}^i_{\mathbb Z}(\mathbb Z/n,-)=0$ for $i\ge2$, because $\mathbb Z/n$ has projective dimension $1$.
