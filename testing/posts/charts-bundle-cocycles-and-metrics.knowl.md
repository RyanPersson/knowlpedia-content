+++
id = "posts/charts-bundle-cocycles-and-metrics"
title = "Charts and Morphisms in Diff — knowlified transcript"
kind = "document"
summary = "The verbatim conversation transcript with mathematical terminology linked to Knowlpedia."
aliases = ["Charts and morphisms in Diff conversation", "Principal bundle cocycle conversation"]
domains = ["differential-geometry", "fiber-bundles", "category-theory"]
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

## User

Consider the
[[differential-geometry/category-of-smooth-manifolds|category
\(\,\mathbf{Diff}\)]],

Are [[fiber-bundles/smooth-chart-coordinate-chart|Charts]], [[algebra-category-theory/morphism|morphisms]] in this [[algebra-category-theory/category|category]]?

## Assistant

Let [[differential-geometry/category-of-smooth-manifolds|\(\mathbf{Diff}\)]] denote the [[algebra-category-theory/category|category]] whose [[algebra-category-theory/object|objects]] are [[fiber-bundles/smooth-manifold|smooth manifolds]] and whose [[algebra-category-theory/morphism|morphisms]] are [[fiber-bundles/smooth-map|smooth maps]].

A [[fiber-bundles/smooth-chart-coordinate-chart|chart]] on an \(n\)-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\) is a pair

\[
(U,\varphi),
\]

where

\[
U\subseteq M
\]

is open and

\[
\varphi:U\longrightarrow \varphi(U)\subseteq \mathbb{R}^{n}
\]

is a [[topology/homeomorphism|homeomorphism]] onto an [[topology/open-set|open subset]] \(\varphi(U)\subseteq\mathbb{R}^{n}\), compatible with the [[fiber-bundles/smooth-atlas|smooth atlas]].

Since [[topology/open-set|open subsets]] of [[fiber-bundles/smooth-manifold|smooth manifolds]] are themselves [[fiber-bundles/smooth-manifold|smooth manifolds]], both

\[
U
\qquad\text{and}\qquad
\varphi(U)
\]

are [[algebra-category-theory/object|objects]] of [[differential-geometry/category-of-smooth-manifolds|\(\mathbf{Diff}\)]]. Moreover, the compatibility condition implies that

\[
\varphi:U\longrightarrow \varphi(U)
\]

and

\[
\varphi^{-1}:\varphi(U)\longrightarrow U
\]

are smooth. Therefore,

\[
\varphi\in\operatorname{Hom}_{\mathbf{Diff}}(U,\varphi(U))
\]

is an [[differential-geometry/coordinate-chart-isomorphism-in-smooth-manifolds|isomorphism in \(\mathbf{Diff}\)]].

However, there are two qualifications.

First, the **[[fiber-bundles/smooth-chart-coordinate-chart|chart]]** is the pair \((U,\varphi)\), so strictly speaking the [[fiber-bundles/smooth-chart-coordinate-chart|chart]] itself is not merely a [[algebra-category-theory/morphism|morphism]]; its coordinate map \(\varphi\) is a [[algebra-category-theory/morphism|morphism]].

Second, \(\varphi\) is generally not a [[algebra-category-theory/morphism|morphism]] with [[shared-foundations/domain|domain]] \(M\):

\[
\varphi:M\longrightarrow\mathbb{R}^{n}
\]

because \(\varphi\) is defined only on \(U\subseteq M\). Instead, one has the diagram

\[
U \xrightarrow{\ \varphi\ } \varphi(U)\subseteq\mathbb{R}^{n},
\]

together with the smooth inclusion

\[
\iota_U:U\hookrightarrow M.
\]

Thus, the coordinate map is an isomorphism between two
[[differential-geometry/open-submanifold|open submanifolds]]:

\[
\boxed{\text{The coordinate map of a chart is an isomorphism in }\mathbf{Diff}
\text{ between two open submanifolds.}}
\]

For two overlapping [[fiber-bundles/smooth-chart-coordinate-chart|charts]] \((U,\varphi)\) and \((V,\psi)\), the transition map

\[
\psi\circ\varphi^{-1}:
\varphi(U\cap V)\longrightarrow\psi(U\cap V)
\]

is likewise an [[algebra-category-theory/isomorphism-category|isomorphism]] in [[differential-geometry/category-of-smooth-manifolds|\(\mathbf{Diff}\)]].

## User

Define what it meant for an atlas of [[fiber-bundles/smooth-chart-coordinate-chart|charts]] to be maximal again, I forgot the axiomatic structure

## Assistant

Let \(M\) be a topological \(n\)-manifold.

## 1. [[fiber-bundles/smooth-chart-coordinate-chart|Charts]]

A [[fiber-bundles/smooth-chart-coordinate-chart|chart]] on \(M\) is a pair

\[
(U,\varphi),
\]

where

\[
U\subseteq M
\]

is open and

\[
\varphi:U\longrightarrow \varphi(U)
\]

is a [[topology/homeomorphism|homeomorphism]], with

\[
\varphi(U)\subseteq \mathbb{R}^{n}
\]

open.

## 2. [[fiber-bundles/smooth-compatibility-of-charts-and-atlases|Compatibility of charts]]

Let

\[
(U,\varphi)
\qquad\text{and}\qquad
(V,\psi)
\]

be [[fiber-bundles/smooth-chart-coordinate-chart|charts]] on \(M\).

They are called **[[fiber-bundles/smooth-compatibility-of-charts-and-atlases|smoothly compatible]]** if either

\[
U\cap V=\varnothing,
\]

or the transition maps

\[
\psi\circ\varphi^{-1}:
\varphi(U\cap V)\longrightarrow \psi(U\cap V)
\]

and

\[
\varphi\circ\psi^{-1}:
\psi(U\cap V)\longrightarrow \varphi(U\cap V)
\]

are smooth.

Since these transition maps are inverses, it is equivalent to require that either one be a [[fiber-bundles/diffeomorphism|diffeomorphism]].

## 3. [[fiber-bundles/smooth-atlas|Smooth atlas]]

A [[fiber-bundles/smooth-atlas|smooth atlas]] on \(M\) is a set of [[fiber-bundles/smooth-chart-coordinate-chart|charts]]

\[
\mathcal{A}
=
\{(U_\alpha,\varphi_\alpha)\}_{\alpha\in I}
\]

such that:

\[
M=\bigcup_{\alpha\in I}U_\alpha,
\]

and every pair of [[fiber-bundles/smooth-chart-coordinate-chart|charts]] in \(\mathcal{A}\) is smoothly compatible.

Thus an atlas has two axioms:

\[
\boxed{\text{the chart domains cover }M}
\]

and

\[
\boxed{\text{all charts are pairwise smoothly compatible}.}
\]

## 4. [[fiber-bundles/maximal-smooth-atlas|Maximal atlas]]

A [[fiber-bundles/smooth-atlas|smooth atlas]] \(\mathcal{A}\) on \(M\) is **maximal** if there is no [[fiber-bundles/smooth-atlas|smooth atlas]] \(\mathcal{B}\) on \(M\) satisfying

\[
\mathcal{A}\subsetneq\mathcal{B}.
\]

Equivalently,

\[
\boxed{
\mathcal{A}\text{ contains every chart on }M
\text{ that is smoothly compatible with every chart in }\mathcal{A}.
}
\]

More explicitly, \(\mathcal{A}\) is maximal if, for every [[fiber-bundles/smooth-chart-coordinate-chart|chart]] \((V,\psi)\) on \(M\),

\[
\left[
\forall (U,\varphi)\in\mathcal{A},
\quad
(U,\varphi)\text{ and }(V,\psi)\text{ are smoothly compatible}
\right]
\Longrightarrow
(V,\psi)\in\mathcal{A}.
\]

This is the axiomatic maximality condition.

## 5. [[fiber-bundles/maximal-smooth-atlas|Maximal atlas]] generated by an atlas

Given any [[fiber-bundles/smooth-atlas|smooth atlas]] \(\mathcal{A}\), define

\[
\overline{\mathcal{A}}
:=
\left\{
(V,\psi)
\;\middle|\;
\begin{array}{l}
(V,\psi)\text{ is a chart on }M,\\[2mm]
(V,\psi)\text{ is smoothly compatible}\\
\text{with every chart in }\mathcal{A}
\end{array}
\right\}.
\]

Then:

\[
\mathcal{A}\subseteq\overline{\mathcal{A}},
\]

and \(\overline{\mathcal{A}}\) is the unique [[fiber-bundles/maximal-smooth-atlas|maximal smooth atlas]] containing \(\mathcal{A}\).

A [[fiber-bundles/smooth-structure|smooth structure]] on \(M\) is usually defined to be such a [[fiber-bundles/maximal-smooth-atlas|maximal smooth atlas]]. Hence a [[fiber-bundles/smooth-manifold|smooth manifold]] is a pair

\[
(M,\mathcal{A}_{\max}),
\]

where \(M\) is a [[topology/topological-manifold|topological manifold]] and \(\mathcal{A}_{\max}\) is a [[fiber-bundles/maximal-smooth-atlas|maximal smooth atlas]].

## User

def [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]]

## Assistant

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]].

A **smooth [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]]** on \(M\) is a family of smooth [[shared-foundations/function|functions]]

\[
\{\rho_\alpha:M\to[0,1]\}_{\alpha\in A}
\]

satisfying the following axioms.

### 1. [[topology/locally-finite-family|Local finiteness]]

For every \(p\in M\), there exists an open [[topology/neighborhood|neighborhood]] \(W\subseteq M\) of \(p\) such that

\[
\left\{
\alpha\in A:
\rho_\alpha|_W\not\equiv 0
\right\}
\]

is finite.

Equivalently, the family of [[shared-foundations/support-of-a-function|supports]]

\[
\{\operatorname{supp}(\rho_\alpha)\}_{\alpha\in A}
\]

is locally finite, where

\[
\operatorname{supp}(\rho_\alpha)
:=
\overline{
\{p\in M:\rho_\alpha(p)\neq 0\}
}.
\]

### 2. Sum-to-one condition

For every \(p\in M\),

\[
\sum_{\alpha\in A}\rho_\alpha(p)=1.
\]

The sum is well-defined because local finiteness implies that only finitely many terms are nonzero near each point.

Thus:

\[
\boxed{
\{\rho_\alpha\}_{\alpha\in A}
\text{ is a smooth partition of unity}
\iff
\begin{cases}
\rho_\alpha\in C^\infty(M,[0,1]),\\
\{\operatorname{supp}(\rho_\alpha)\}_{\alpha\in A}
\text{ is locally finite},\\
\displaystyle\sum_{\alpha\in A}\rho_\alpha=1_M.
\end{cases}
}
\]

Here

\[
1_M:M\to\mathbb{R},
\qquad
1_M(p)=1.
\]

## Subordinate to an [[topology/open-cover|open cover]]

Let

\[
\mathcal{U}=\{U_\alpha\}_{\alpha\in A}
\]

be an [[topology/open-cover|open cover]] of \(M\). A [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]]

\[
\{\rho_\alpha\}_{\alpha\in A}
\]

is **subordinate to** \(\mathcal{U}\) if

\[
\operatorname{supp}(\rho_\alpha)\subseteq U_\alpha
\]

for every \(\alpha\in A\).

More generally, one may allow a separate index set \(B\) and require a map

\[
\sigma:B\to A
\]

such that

\[
\operatorname{supp}(\rho_\beta)\subseteq U_{\sigma(\beta)}
\]

for every \(\beta\in B\).

For paracompact [[fiber-bundles/smooth-manifold|smooth manifolds]], every [[topology/open-cover|open cover]] admits a smooth [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]] subordinate to that cover.

## User

transcribe this screenshot:

[User attached 1 [[shared-foundations/image|image]]; [[shared-foundations/image|image]] contents were not included]

## Assistant

**Example.** Let \(P=M\times G\) on which \(G\) acts freely via the action

\[
(x,h)g := (x,hg).
\]

Then the projection map

\[
\pi:P\to M
\]

given by

\[
\pi(x,g)=x
\]

defines a principal \(G\)-bundle over \(M\). Seeing how simple and easy it looks, it’s called a [[fiber-bundles/trivial-principal-bundle-mgm|trivial bundle]]. (Trivial but essential!)

**Intuition.** One way to imagine \(P\) is that it consists of different copies of the [[algebra-groups/group|group]] \(G\) hovering over each point of \(M\) and blended together in a generally twisted fashion. (Or as a bunch of [[fiber-bundles/trivial-principal-bundle-mgm|trivial bundles]] \(U\times G\), for various [[topology/open-set|open sets]] \(U\), glued together in some smooth and topological way.)

**Particle Fields.** To describe a particle field one needs a [[algebra-representation-theory/group-representation|representation]]

\[
\rho:G\to GL(V)
\]

of the [[algebra-groups/group|group]] \(G\) acting as invertible operators on a complex [[linear-algebra/vector-space|vector space]] \(V\). It is chosen appropriately depending on the particle’s type (spin, mass, charge, etc). Given \(\rho\) and a principal \(G\)-bundle as above, a particle field can then be defined as a [[real-analysis/differentiable-map|differentiable map]]

\[
\Psi:P\to V
\]

satisfying the \(G\)-equivariant condition

\[
\Psi(pg)=\rho(g^{-1})\Psi(p),
\qquad
\forall p\in P,\ g\in G.
\]

**Discussion.** Using the [[algebra-representation-theory/group-representation|representation]] \(\rho\) and the principal \(G\)-bundle

\[
\pi:P\to M,
\]

we can construct a [[fiber-bundles/vector-bundle|vector bundle]]

\[
E=P\times_{\rho}V
\]

over \(M\) with [[fiber-bundles/fiber-of-a-map|fiber]] \(V\). Then differentiable sections

*[The remainder is cropped from the screenshot.]*

## User

I noticed this part:

"Intuition. One way to imagine P is that it consists of different copies of the [[algebra-groups/group|group]] G hovering over each point of M and blended together in a generally twisted fashion. (Or as a bunch of [[fiber-bundles/trivial-principal-bundle-mgm|trivial bundles]] U×G, for various [[topology/open-set|open sets]] U, glued together in some smooth and topological way.)"

Is there some precise relationship between the various "copies" of G, "blended and twisted together" on M, and the underlying smooth [[fiber-bundles/maximal-smooth-atlas|maximal atlas]] of [[fiber-bundles/smooth-chart-coordinate-chart|charts]] on M?

## Assistant

Yes. The relationship is mediated by a second kind of atlas: a **[[fiber-bundles/bundle-atlas|bundle atlas]] of [[fiber-bundles/local-trivialization|local trivializations]]**. It is related to, but not the same as, the [[fiber-bundles/maximal-smooth-atlas|maximal smooth atlas]] on \(M\).

## 1. [[fiber-bundles/g-torsor|Fibers are \(G\)-torsors]]

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]], and let

\[
\pi:P\to M
\]

be a principal right \(G\)-bundle. For each \(x\in M\), define the [[fiber-bundles/fiber-of-a-map|fiber]]

\[
P_x:=\pi^{-1}(\{x\}).
\]

The right action

\[
P\times G\to P,
\qquad
(p,g)\mapsto pg
\]

restricts to a free and [[algebra-groups/transitive-action|transitive action]]

\[
P_x\times G\to P_x.
\]

Thus, for each \(p_0\in P_x\), the map

\[
G\to P_x,
\qquad
g\mapsto p_0g
\]

is a \(G\)-equivariant [[fiber-bundles/diffeomorphism|diffeomorphism]].

However, this identification depends on the choice of \(p_0\). Therefore \(P_x\) is not canonically a copy of \(G\) as a [[algebra-groups/group|group]]. It is canonically a **[[fiber-bundles/g-torsor|right \(G\)-torsor]]**.

This is the precise meaning of saying that a copy of \(G\) lies over each point \(x\in M\).

## 2. [[fiber-bundles/local-trivialization|Local trivializations]]

The local-triviality axiom states that every \(x\in M\) has an open [[topology/neighborhood|neighborhood]] \(U\subseteq M\) and a \(G\)-equivariant [[fiber-bundles/diffeomorphism|diffeomorphism]]

\[
\Phi_U:\pi^{-1}(U)\longrightarrow U\times G
\]

such that

\[
\operatorname{pr}_1\circ\Phi_U
=
\pi|_{\pi^{-1}(U)}.
\]

Equivariance means

\[
\Phi_U(pg)
=
\Phi_U(p)g,
\]

where the action on \(U\times G\) is

\[
(x,h)g=(x,hg).
\]

Hence, locally over \(U\),

\[
\pi^{-1}(U)\cong U\times G.
\]

A family

\[
\left\{
\Phi_i:\pi^{-1}(U_i)\to U_i\times G
\right\}_{i\in I}
\]

with

\[
M=\bigcup_{i\in I}U_i
\]

is called a **[[fiber-bundles/bundle-atlas|principal-bundle atlas]]** or an [[fiber-bundles/bundle-atlas|atlas of local trivializations]].

This is distinct from a [[fiber-bundles/smooth-atlas|smooth atlas]] of [[fiber-bundles/smooth-chart-coordinate-chart|coordinate charts]]

\[
\varphi_\alpha:V_\alpha\to\mathbb{R}^{\dim M}.
\]

## 3. [[fiber-bundles/section-of-a-fiber-bundle|Local sections]] and choices of [[fiber-bundles/fiber-coordinates|fiber coordinates]]

A [[fiber-bundles/local-trivialization|local trivialization]] is equivalent to choosing a smooth [[fiber-bundles/section-of-a-fiber-bundle|local section]]

\[
s_i:U_i\to P
\]

satisfying

\[
\pi\circ s_i=\operatorname{id}_{U_i}.
\]

Given \(s_i\), every \(p\in\pi^{-1}(U_i)\) can be written uniquely as

\[
p=s_i(x)h,
\qquad
x=\pi(p),
\quad
h\in G.
\]

The corresponding trivialization is

\[
\Phi_i(p)=(x,h).
\]

Thus \(s_i(x)\in P_x\) serves as a local choice of origin in the \(G\)-torsor \(P_x\). It identifies every [[fiber-bundles/fiber-of-a-map|fiber]] over \(U_i\) with \(G\).

## 4. The twisting is encoded by [[fiber-bundles/principal-bundle-transition-function|transition functions]]

Suppose \(U_i\cap U_j\neq\varnothing\). Since \(s_i(x)\) and \(s_j(x)\) lie in the same [[fiber-bundles/fiber-of-a-map|fiber]], there exists a unique element

\[
g_{ij}(x)\in G
\]

such that

\[
s_j(x)=s_i(x)g_{ij}(x).
\]

This defines a smooth [[fiber-bundles/principal-bundle-transition-function|transition function]]

\[
g_{ij}:U_i\cap U_j\to G.
\]

If

\[
p=s_i(x)h_i=s_j(x)h_j,
\]

then

\[
h_j=g_{ij}(x)^{-1}h_i.
\]

Consequently, the change between [[fiber-bundles/local-trivialization|local trivializations]] is

\[
\Phi_j\circ\Phi_i^{-1}:
(U_i\cap U_j)\times G
\longrightarrow
(U_i\cap U_j)\times G,
\]

given by

\[
\Phi_j\circ\Phi_i^{-1}(x,h)
=
\left(x,g_{ij}(x)^{-1}h\right).
\]

The base point \(x\) is unchanged. Only the chosen identification of the [[fiber-bundles/fiber-of-a-map|fiber]] \(P_x\) with \(G\) changes.

On triple overlaps, the [[fiber-bundles/principal-bundle-transition-function|transition functions]] satisfy

\[
g_{ii}(x)=e_G,
\]

\[
g_{ji}(x)=g_{ij}(x)^{-1},
\]

and

\[
g_{ik}(x)=g_{ij}(x)g_{jk}(x).
\]

The family

\[
\{g_{ij}\}
\]

is the bundle’s [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycle]] data. This is what the phrase “twisted together” refers to.

For the [[fiber-bundles/trivial-principal-bundle-mgm|trivial bundle]]

\[
P=M\times G,
\]

one can choose the [[fiber-bundles/section-of-a-fiber-bundle|global section]]

\[
s:M\to M\times G,
\qquad
s(x)=(x,e_G),
\]

so no change of local [[fiber-bundles/fiber-coordinates|fiber coordinates]] is required.

## 5. Relationship with the [[fiber-bundles/maximal-smooth-atlas|maximal smooth atlas]] on \(M\)

Let

\[
\mathcal{A}_M
\]

be the [[fiber-bundles/maximal-smooth-atlas|maximal smooth atlas]] of \(M\).

The atlas \(\mathcal{A}_M\) does not itself determine the [[fiber-bundles/principal-g-bundle|principal bundle]]. Instead, it determines what it means for the [[fiber-bundles/principal-bundle-transition-function|transition functions]]

\[
g_{ij}:U_i\cap U_j\to G
\]

to be smooth.

More explicitly, let

\[
\varphi_\alpha:V_\alpha\to\varphi_\alpha(V_\alpha)
\subseteq\mathbb{R}^{n}
\]

be a [[fiber-bundles/smooth-chart-coordinate-chart|chart]] in \(\mathcal{A}_M\), and let

\[
\chi_\beta:W_\beta\to\chi_\beta(W_\beta)
\subseteq\mathbb{R}^{r}
\]

be a [[fiber-bundles/smooth-chart-coordinate-chart|chart]] on \(G\), where

\[
n=\dim M,
\qquad
r=\dim G.
\]

After replacing \(U_i\) by [[shared-foundations/intersection|intersections]] \(U_i\cap V_\alpha\), the map

\[
\pi^{-1}(U_i\cap V_\alpha)
\xrightarrow{\Phi_i}
(U_i\cap V_\alpha)\times G
\]

can be combined with \(\varphi_\alpha\) and \(\chi_\beta\) to produce [[fiber-bundles/smooth-chart-coordinate-chart|coordinate charts]] on \(P\):

\[
p
\longmapsto
\left(
\varphi_\alpha(\pi(p)),
\chi_\beta(h_i(p))
\right).
\]

Thus the [[fiber-bundles/smooth-atlas|smooth atlas]] on \(P\) is locally constructed from:

\[
\text{charts on }M,
\]

\[
\text{charts on }G,
\]

and

\[
\text{bundle transition functions }g_{ij}:U_i\cap U_j\to G.
\]

The [[fiber-bundles/coordinate-transition-map|coordinate transition maps]] on \(P\) contain both the coordinate changes on \(M\),

\[
\varphi_\gamma\circ\varphi_\alpha^{-1},
\]

and the fiber-coordinate changes,

\[
h\mapsto g_{ij}(x)^{-1}h.
\]

## 6. The distinction

There are therefore three related structures:

\[
\begin{array}{c|c|c}
\text{Structure} & \text{Local model} & \text{Transition data}\\
\hline
\text{Smooth atlas on }M
&
\mathbb{R}^{n}
&
\varphi_j\circ\varphi_i^{-1}
\\[1mm]
\text{Smooth atlas on }P
&
\mathbb{R}^{n+\dim G}
&
\text{coordinate transitions on }P
\\[1mm]
\text{Principal-bundle atlas}
&
U_i\times G
&
g_{ij}:U_i\cap U_j\to G
\end{array}
\]

The [[fiber-bundles/maximal-smooth-atlas|maximal smooth atlas]] on \(M\) specifies the smooth base geometry. The [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycle]]

\[
\{g_{ij}\}
\]

specifies how the \(G\)-torsors over different points are assembled into the total space \(P\).

In particular, the same [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\), with the same [[fiber-bundles/maximal-smooth-atlas|maximal smooth atlas]], may support many nonisomorphic principal \(G\)-bundles. The twisting is additional data; it is not already contained in the [[fiber-bundles/smooth-atlas|smooth atlas]] of \(M\).

## User

This [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycle]] data looks fascinating, can you expand on it? Does it carry any other algebraic or [[algebra-groups/group|group]] structure? Is it related to [[differential-geometry/riemannian-manifold|Riemannian metrics]] in some way?

## Assistant

Yes. The [[fiber-bundles/principal-bundle-transition-function|transition functions]] of a [[fiber-bundles/principal-g-bundle|principal bundle]] form a **Čech \(1\)-cocycle**, and their algebraic structure depends strongly on whether \(G\) is abelian.

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]], let \(G\) be a [[fiber-bundles/lie-group|Lie group]], and let

\[
\mathcal{U}=\{U_i\}_{i\in I}
\]

be an [[topology/open-cover|open cover]] of \(M\). Suppose a principal \(G\)-bundle

\[
\pi:P\to M
\]

has [[fiber-bundles/section-of-a-fiber-bundle|local sections]]

\[
s_i:U_i\to P.
\]

On each overlap

\[
U_{ij}:=U_i\cap U_j,
\]

define

\[
g_{ij}:U_{ij}\to G
\]

by

\[
s_j(x)=s_i(x)g_{ij}(x).
\]

## 1. The [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycle]] equations

The [[fiber-bundles/principal-bundle-transition-function|transition functions]] satisfy:

\[
g_{ii}(x)=e_G,
\]

\[
g_{ji}(x)=g_{ij}(x)^{-1},
\]

and, on every triple overlap

\[
U_{ijk}:=U_i\cap U_j\cap U_k,
\]

\[
g_{ik}(x)=g_{ij}(x)g_{jk}(x).
\]

The last identity follows from

\[
s_k(x)
=
s_j(x)g_{jk}(x)
=
s_i(x)g_{ij}(x)g_{jk}(x),
\]

while also

\[
s_k(x)=s_i(x)g_{ik}(x).
\]

Thus

\[
g_{ik}=g_{ij}g_{jk}.
\]

Equivalently,

\[
g_{ij}g_{jk}g_{ki}=e_G.
\]

A family

\[
g=\{g_{ij}:U_{ij}\to G\}
\]

satisfying these equations is called a **smooth Čech \(1\)-cocycle with values in \(G\)**.

## 2. Constructing a bundle from [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycle]] data

One can reverse the construction.

Start with the [[differential-geometry/disjoint-union-of-smooth-manifolds|disjoint union]]

\[
\bigsqcup_{i\in I}(U_i\times G).
\]

Define an [[shared-foundations/equivalence-relation|equivalence relation]] by

\[
(x,h)_i\sim(x,g_{ij}(x)^{-1}h)_j
\]

for every

\[
x\in U_{ij},
\qquad
h\in G.
\]

The [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycle]] equation ensures transitivity. Indeed,

\[
(x,h)_i
\sim
(x,g_{ij}(x)^{-1}h)_j
\sim
\left(x,g_{jk}(x)^{-1}g_{ij}(x)^{-1}h\right)_k,
\]

and

\[
g_{jk}^{-1}g_{ij}^{-1}
=
(g_{ij}g_{jk})^{-1}
=
g_{ik}^{-1}.
\]

The [[shared-foundations/quotient-set|quotient]]

\[
P_g
:=
\left(
\bigsqcup_{i\in I}U_i\times G
\right)\big/\sim
\]

is a principal \(G\)-bundle over \(M\).

Thus the phrase “glue together copies of \(G\)” is represented exactly by the [[shared-foundations/quotient-set|quotient]] relation determined by the maps \(g_{ij}\).

## 3. Dependence on the choice of [[fiber-bundles/section-of-a-fiber-bundle|local sections]]

The [[shared-foundations/function|functions]] \(g_{ij}\) are not intrinsic individually. They depend on the [[fiber-bundles/section-of-a-fiber-bundle|local sections]] \(s_i\).

Let

\[
h_i:U_i\to G
\]

be [[fiber-bundles/smooth-map|smooth maps]], and define new sections

\[
s_i'(x):=s_i(x)h_i(x).
\]

Let \(g_{ij}'\) denote the [[fiber-bundles/principal-bundle-transition-function|transition functions]] determined by the \(s_i'\). Then

\[
s_j'(x)
=
s_j(x)h_j(x)
=
s_i(x)g_{ij}(x)h_j(x).
\]

Since

\[
s_i(x)=s_i'(x)h_i(x)^{-1},
\]

we obtain

\[
s_j'(x)
=
s_i'(x)
h_i(x)^{-1}g_{ij}(x)h_j(x).
\]

Therefore

\[
\boxed{
g_{ij}'(x)
=
h_i(x)^{-1}g_{ij}(x)h_j(x).
}
\]

This transformation is called a **[[fiber-bundles/equivalence-of-cocycles|coboundary transformation]]**, a **[[fiber-bundles/equivalence-of-cocycles|change of local trivialization]]**, or a [[fiber-bundles/local-gauge-transformation|local gauge transformation]].

Two [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycles]] determine isomorphic principal \(G\)-bundles precisely when, after possibly refining the cover, they are related in this way.

## 4. [[fiber-bundles/nonabelian-cech-h1-principal-bundles|Nonabelian Čech cohomology]]

Write

\[
Z^1(\mathcal{U},G)
\]

for the set of smooth \(G\)-valued \(1\)-cocycles on \(\mathcal{U}\).

The set of \(0\)-cochains is

\[
C^0(\mathcal{U},G)
=
\prod_{i\in I}C^\infty(U_i,G).
\]

An element

\[
h=\{h_i\}_{i\in I}
\]

acts on [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycles]] by

\[
(h\cdot g)_{ij}
=
h_i^{-1}g_{ij}h_j.
\]

The [[shared-foundations/quotient-set|quotient]] is denoted

\[
\check H^1(\mathcal{U},G)
:=
Z^1(\mathcal{U},G)/C^0(\mathcal{U},G).
\]

For a general nonabelian [[algebra-groups/group|group]] \(G\), this is usually only a **[[shared-foundations/pointed-set|pointed set]]**, not a [[algebra-groups/group|group]]. Its distinguished point is the class of the trivial [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycle]]

\[
g_{ij}(x)=e_G.
\]

After taking a suitable limit over refinements of [[topology/open-cover|open covers]], one obtains

\[
\check H^1(M,G),
\]

which classifies principal \(G\)-bundles under appropriate hypotheses.

More precisely, one usually regards \(G\) as the [[algebraic-geometry-foundations/sheaf|sheaf]]

\[
U\longmapsto C^\infty(U,G).
\]

Then principal \(G\)-bundles are classified by the [[fiber-bundles/nonabelian-cech-h1-principal-bundles|nonabelian cohomology set]]

\[
\check H^1\!\left(M,C^\infty(-,G)\right).
\]

## 5. What changes when \(G\) is abelian?

Suppose \(G\) is abelian. Then [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycles]] can be multiplied pointwise:

\[
(gg')_{ij}(x)
:=
g_{ij}(x)g_{ij}'(x).
\]

This again satisfies the [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycle]] equation. Consequently,

\[
Z^1(\mathcal{U},G)
\]

is an [[algebra-groups/abelian-group|abelian group]].

The coboundaries form a [[algebra-groups/subgroup|subgroup]], so

\[
\check H^1(\mathcal{U},G)
\]

is an [[algebra-groups/abelian-group|abelian group]].

For example, when

\[
G=U(1),
\]

principal \(U(1)\)-bundles correspond to [[fiber-bundles/line-bundle|complex line bundles]]. Their [[algebra-category-theory/isomorphism-category|isomorphism]] classes form an [[algebra-groups/abelian-group|abelian group]] under [[algebra-modules/tensor-product|tensor product]]:

\[
[L_1]+[L_2]
:=
[L_1\otimes L_2].
\]

If \(g_{ij}\) and \(g_{ij}'\) are the [[fiber-bundles/principal-bundle-transition-function|transition functions]] for \(L_1\) and \(L_2\), then the [[fiber-bundles/principal-bundle-transition-function|transition functions]] for \(L_1\otimes L_2\) are

\[
g_{ij}g_{ij}'.
\]

For sufficiently well-behaved spaces,

\[
\{\text{complex line bundles over }M\}/\cong
\;\cong\;
H^2(M;\mathbb{Z}),
\]

with the correspondence given by the [[fiber-bundles/chern-class|first Chern class]]

\[
L\longmapsto c_1(L).
\]

## 6. A [[algebra-category-theory/groupoid|groupoid]] structure for general \(G\)

Although the set of [[algebra-category-theory/isomorphism-category|isomorphism]] classes need not be a [[algebra-groups/group|group]] when \(G\) is nonabelian, the [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycles]] naturally form a **[[algebra-category-theory/groupoid|groupoid]]**.

Its [[algebra-category-theory/object|objects]] are [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycles]]

\[
\{g_{ij}\},
\]

and a [[algebra-category-theory/morphism|morphism]]

\[
\{g_{ij}\}\longrightarrow \{g_{ij}'\}
\]

is a family

\[
\{h_i:U_i\to G\}
\]

such that

\[
g_{ij}'
=
h_i^{-1}g_{ij}h_j.
\]

Composition is pointwise multiplication of the \(h_i\), with the order determined by the convention above.

This [[fiber-bundles/cech-cocycle-groupoid|cocycle groupoid]] retains [[algebra-category-theory/automorphism-category|automorphism]] information that is discarded when one passes only to [[algebra-category-theory/isomorphism-category|isomorphism]] classes.

## 7. [[fiber-bundles/gauge-transformation|Gauge transformations]]

A [[fiber-bundles/gauge-transformation|gauge transformation]] of \(P\) is a principal-bundle [[algebra-category-theory/automorphism-category|automorphism]]

\[
F:P\to P
\]

satisfying

\[
\pi\circ F=\pi
\]

and

\[
F(pg)=F(p)g.
\]

Relative to [[fiber-bundles/section-of-a-fiber-bundle|local sections]] \(s_i\), such an [[algebra-category-theory/automorphism-category|automorphism]] is represented by [[fiber-bundles/smooth-map|smooth maps]]

\[
u_i:U_i\to G.
\]

These local maps are not arbitrary. On overlaps, they satisfy a conjugation relation determined by the [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycle]]. Depending on the chosen convention, one obtains

\[
u_j
=
g_{ij}^{-1}u_i g_{ij}.
\]

Globally, [[fiber-bundles/gauge-transformation|gauge transformations]] correspond to smooth sections of the associated [[algebra-groups/group|group]] bundle

\[
\operatorname{Ad}(P)
:=
P\times_{\operatorname{Ad}}G,
\]

where \(G\) acts on itself by conjugation:

\[
\operatorname{Ad}_g(h)=ghg^{-1}.
\]

The [[fiber-bundles/gauge-transformation|gauge transformations]] form a [[algebra-groups/group|group]]

\[
\operatorname{Gau}(P)
\cong
\Gamma^\infty(M,\operatorname{Ad}(P)).
\]

Thus, even when the bundle classes do not form a [[algebra-groups/group|group]], each individual bundle has an [[algebra-groups/automorphism-group|automorphism group]].

# Relationship with [[differential-geometry/riemannian-manifold|Riemannian metrics]]

There are several direct relationships.

## 8. The [[fiber-bundles/tangent-bundle-cocycle-from-coordinate-changes|tangent bundle cocycle]] comes from the [[fiber-bundles/smooth-atlas|smooth atlas]]

Let \(M\) be an \(n\)-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]] with [[fiber-bundles/smooth-chart-coordinate-chart|coordinate charts]]

\[
\varphi_i:U_i\to\varphi_i(U_i)\subseteq\mathbb{R}^n.
\]

On an overlap \(U_{ij}\), the coordinate transition map is

\[
\varphi_j\circ\varphi_i^{-1}:
\varphi_i(U_{ij})
\to
\varphi_j(U_{ij}).
\]

Its [[real-analysis/derivative|derivative]] determines the tangent-bundle [[fiber-bundles/transition-function|transition function]]

\[
A_{ij}:U_{ij}\to GL(n,\mathbb{R}),
\]

where

\[
A_{ij}(x)
=
D\!\left(
\varphi_j\circ\varphi_i^{-1}
\right)_{\varphi_i(x)}.
\]

The [[real-analysis/chain-rule|chain rule]] gives

\[
A_{ik}(x)
=
A_{jk}(x)A_{ij}(x),
\]

with the precise multiplication order depending on whether coordinate components are treated as column vectors and on the convention for \(g_{ij}\).

Thus the [[fiber-bundles/tangent-bundle|tangent bundle]]

\[
TM\to M
\]

is constructed from the [[real-analysis/derivative|derivatives]] of the coordinate changes of the [[fiber-bundles/smooth-atlas|smooth atlas]].

This is a particularly direct relation between an atlas [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycle]] and a geometrically important bundle.

## 9. The [[fiber-bundles/frame-bundle-fr-of-a-manifold-m|frame bundle]]

For each \(x\in M\), let

\[
\operatorname{Fr}(T_xM)
\]

be the set of ordered bases of the [[linear-algebra/vector-space|vector space]] \(T_xM\). Define

\[
\operatorname{Fr}(M)
:=
\bigsqcup_{x\in M}\operatorname{Fr}(T_xM).
\]

There is a projection

\[
\pi_{\operatorname{Fr}}:
\operatorname{Fr}(M)\to M.
\]

The [[algebra-groups/group|group]]

\[
GL(n,\mathbb{R})
\]

acts freely and transitively on each [[fiber-bundles/fiber-of-a-map|fiber]] by changing the basis. Therefore

\[
\operatorname{Fr}(M)\to M
\]

is a principal \(GL(n,\mathbb{R})\)-bundle.

The [[fiber-bundles/principal-bundle-transition-function|transition functions]] of the [[fiber-bundles/frame-bundle-fr-of-a-manifold-m|frame bundle]] are the Jacobian matrices of coordinate changes.

## 10. A [[differential-geometry/riemannian-manifold|Riemannian metric]] as a [[fiber-bundles/reduction-of-structure-group|reduction of structure group]]

A [[differential-geometry/riemannian-manifold|Riemannian metric]] on \(M\) is a smooth assignment

\[
x\longmapsto \langle-,-\rangle_x
\]

of a positive-definite [[linear-algebra/inner-product|inner product]] on every [[differential-geometry/tangent-space|tangent space]] \(T_xM\).

Given a [[differential-geometry/riemannian-manifold|Riemannian metric]], one may restrict the [[fiber-bundles/frame-bundle-fr-of-a-manifold-m|frame bundle]] to [[fiber-bundles/orthonormal-frame-bundle-o-of-a-riemannian-manifold|orthonormal frames]]:

\[
\operatorname{OFr}(M)
:=
\left\{
(e_1,\ldots,e_n)\in\operatorname{Fr}(M):
\langle e_a,e_b\rangle_x=\delta_{ab}
\right\}.
\]

Then

\[
\operatorname{OFr}(M)\to M
\]

is a principal \(O(n)\)-bundle.

This is called a **[[fiber-bundles/reduction-of-structure-group|reduction of structure group]]**

\[
GL(n,\mathbb{R})
\longrightarrow
O(n).
\]

In arbitrary coordinate frames, the [[fiber-bundles/tangent-bundle-cocycle-from-coordinate-changes|tangent-bundle transition functions]] take values in

\[
GL(n,\mathbb{R}).
\]

In local [[fiber-bundles/orthonormal-frame-bundle-o-of-a-riemannian-manifold|orthonormal frames]], the [[fiber-bundles/principal-bundle-transition-function|transition functions]] take values in

\[
O(n).
\]

Hence a [[differential-geometry/riemannian-manifold|Riemannian metric]] can be described by the existence of a [[fiber-bundles/bundle-atlas|bundle atlas]] for the tangent or [[fiber-bundles/frame-bundle-fr-of-a-manifold-m|frame bundle]] whose [[fiber-bundles/principal-bundle-transition-function|transition functions]] satisfy

\[
g_{ij}(x)\in O(n)
\]

for all \(x\in U_{ij}\).

If \(M\) is oriented and [[fiber-bundles/orthonormal-frame-bundle-o-of-a-riemannian-manifold|orthonormal frames]] are chosen compatibly with the orientation, then the [[fiber-bundles/principal-bundle-transition-function|transition functions]] take values in

\[
SO(n).
\]

## 11. Coordinate expression of a metric

In a [[fiber-bundles/smooth-chart-coordinate-chart|coordinate chart]]

\[
\varphi_i:U_i\to\mathbb{R}^n,
\]

a [[differential-geometry/riemannian-manifold|Riemannian metric]] is represented by a smooth matrix-valued [[shared-foundations/function|function]]

\[
G_i:U_i\to \operatorname{Sym}_{++}(n,\mathbb{R}),
\]

where the target is the cone of
[[linear-algebra/symmetric-positive-definite-matrix|symmetric positive-definite matrices]],

\[
\operatorname{Sym}_{++}(n,\mathbb{R})
\]

is the set of positive-definite symmetric \(n\times n\) matrices.

On overlaps, these matrices satisfy the
[[differential-geometry/coordinate-transformation-law-riemannian-metric|coordinate transformation law]]

\[
G_j
=
J_{ij}^{-T}G_iJ_{ij}^{-1}
\]

or the equivalent transpose formula under the opposite Jacobian convention.

This is the tensorial compatibility law ensuring that the locally defined matrices represent one global metric.

Thus:

\[
\boxed{
\text{The smooth atlas supplies the }GL(n,\mathbb{R})\text{-valued tangent cocycle,}
}
\]

while

\[
\boxed{
\text{a Riemannian metric reduces that cocycle to }O(n)\text{-valued transition data.}
}
\]

## 12. [[fiber-bundles/principal-connection|Connections]] and [[fiber-bundles/curvature|curvature]]

A [[differential-geometry/riemannian-manifold|Riemannian metric]] is also related to [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycle]] data through [[fiber-bundles/principal-connection|connections]].

For a principal \(G\)-bundle, a [[fiber-bundles/principal-connection|connection]] is locally represented by Lie-algebra-valued \(1\)-forms

\[
A_i\in\Omega^1(U_i;\mathfrak{g}),
\]

where

\[
\mathfrak{g}:=T_{e_G}G.
\]

On overlaps, the local [[fiber-bundles/principal-connection|connection]] forms satisfy a transformation rule of the form

\[
A_j
=
\operatorname{Ad}_{g_{ij}^{-1}}A_i
+
g_{ij}^{-1}dg_{ij},
\]

subject to the selected convention for [[fiber-bundles/principal-bundle-transition-function|transition functions]].

The [[fiber-bundles/curvature|curvature]] is locally

\[
F_i
=
dA_i+\frac12[A_i\wedge A_i],
\]

and transforms by

\[
F_j
=
\operatorname{Ad}_{g_{ij}^{-1}}F_i.
\]

For the [[fiber-bundles/orthonormal-frame-bundle-o-of-a-riemannian-manifold|orthonormal frame bundle]] of a [[differential-geometry/riemannian-manifold|Riemannian manifold]], the metric determines the unique torsion-free metric-compatible [[fiber-bundles/principal-connection|connection]]: the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]].

Therefore the progression is

\[
\text{smooth atlas}
\longrightarrow
GL(n,\mathbb{R})\text{-frame bundle}
\longrightarrow
O(n)\text{-reduction from a metric}
\longrightarrow
\text{Levi-Civita connection}
\longrightarrow
\text{Riemann curvature}.
\]

The [[fiber-bundles/smooth-g-valued-cech-1-cocycle|cocycle]] encodes the global bundle [[topology/topology|topology]], while the [[fiber-bundles/principal-connection|connection]] and [[fiber-bundles/curvature|curvature]] encode additional differential-geometric data on that bundle.
