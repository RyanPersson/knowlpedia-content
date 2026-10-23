+++
id = "algebra-homological/snake-lemma"
title = "Snake lemma"
kind = "knowl"
summary = "From a commutative diagram with exact rows, produces an exact sequence of kernels and cokernels with a canonical connecting map."
aliases = ["snake-lemma", "Snake lemma"]
domains = ["algebra-homological"]
legacy_source_path = "algebra-homological/snake-lemma.md"
prerequisites = ["algebra-category-theory/abelian-category", "algebra-category-theory/kernel-categorical", "algebra-category-theory/cokernel-categorical", "algebra-modules/cokernel-module", "algebra-modules/exact-sequence-modules"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Snake lemma**: Let \(R\) be a ring, and suppose a commutative diagram of \(R\)-modules has [[algebra-modules/exact-sequence-modules|exact]] rows
\[
\begin{array}{ccccccccc}
0 &\to& A' &\xrightarrow{i}& A &\xrightarrow{p}& A'' &\to& 0\\
 & & \downarrow f' & & \downarrow f & & \downarrow f'' & & \\
0 &\to& B' &\xrightarrow{j}& B &\xrightarrow{q}& B'' &\to& 0
\end{array}
\]
Then there is a homomorphism \(\delta:\ker(f'')\to\operatorname{coker}(f')\), the **connecting homomorphism**, such that the sequence
\[
0 \to \ker(f') \to \ker(f) \to \ker(f'') \xrightarrow{\ \delta\ } \operatorname{coker}(f') \to \operatorname{coker}(f) \to \operatorname{coker}(f'') \to 0
\]
is exact. The maps other than \(\delta\) are induced by \(i,p,j,q\), and \(\operatorname{coker}(f')=B'/\operatorname{im}(f')\) is the [[algebra-modules/cokernel-module|cokernel]].

The same statement holds in any [[algebra-category-theory/abelian-category|abelian category]], with [[algebra-category-theory/kernel-categorical|kernels]] and [[algebra-category-theory/cokernel-categorical|cokernels]] taken in the categorical sense.

## Construction of the connecting homomorphism

Given \(x\in \ker(f'')\subseteq A''\):
1. pick \(a\in A\) with \(p(a)=x\);
2. since \(f''(x)=0\), commutativity implies \(q(f(a))=0\), hence \(f(a)\in \operatorname{im}(j)\);
3. choose \(b'\in B'\) with \(j(b')=f(a)\);
4. define \(\delta(x)\) to be the class of \(b'\) in \(\operatorname{coker}(f')=B'/\operatorname{im}(f')\).

A standard diagram chase shows this is well-defined (independent of choices) and gives exactness.

The map \(\delta\) is natural in the diagram, and it is the prototype for the [[algebra-homological/connecting-homomorphism-lemma|connecting homomorphism]] appearing in long exact sequences.

## Examples

1. **Induced map on quotients: the “kernel–cokernel” exact sequence.**
   Let \(g:M\to M'\) be an \(R\)-linear map, and let \(N\subseteq M\), \(N'\subseteq M'\) satisfy \(g(N)\subseteq N'\). Consider the commutative diagram with exact rows:
   \[
   \begin{array}{ccccccccc}
   0 &\to& N &\to& M &\to& M/N &\to& 0\\
    & & \downarrow g|_N & & \downarrow g & & \downarrow \overline g & & \\
   0 &\to& N' &\to& M' &\to& M'/N' &\to& 0
   \end{array}
   \]
   The snake lemma produces the exact sequence
   \[
   0\to \ker(g|_N)\to \ker(g)\to \ker(\overline g)\xrightarrow{\delta}
   \operatorname{coker}(g|_N)\to \operatorname{coker}(g)\to \operatorname{coker}(\overline g)\to 0,
   \]
   which cleanly measures how kernels/cokernels change when passing to quotients.

2. **Boundary map in homology from a short exact sequence of complexes.**
   Given a degreewise short exact sequence of [[algebra-homological/chain-complex|chain complexes]]
   \[
   0\to C'_\bullet \to C_\bullet \to C''_\bullet \to 0,
   \]
   one applies the snake lemma to the diagram of cycles and boundaries in each degree to construct the connecting map
   \[
   \partial: H_n(C''_\bullet)\longrightarrow H_{n-1}(C'_\bullet),
   \]
   yielding the usual long exact sequence in [[algebra-homological/homology-module|homology]]. (This is the chain-complex analogue of [[algebra-homological/long-exact-sequence-derived|long exact sequences from derived functors]].)

3. **Computing a boundary map concretely (multiplication on a quotient).**
   Fix integers \(m,n\) and consider the diagram
   \[
   \begin{array}{ccccccccc}
   0&\to& \mathbb Z &\xrightarrow{\cdot m}& \mathbb Z &\to& \mathbb Z/m &\to& 0\\
    && \downarrow \cdot n && \downarrow \cdot n && \downarrow \cdot n &&\\
   0&\to& \mathbb Z &\xrightarrow{\cdot m}& \mathbb Z &\to& \mathbb Z/m &\to& 0
   \end{array}
   \]
   The connecting map \(\delta:\ker(\cdot n:\mathbb Z/m\to \mathbb Z/m)\to \operatorname{coker}(\cdot n:\mathbb Z\to \mathbb Z)\cong \mathbb Z/n\)
   sends a class \(\overline{x}\in\mathbb Z/m\) with \(nx\in m\mathbb Z\) to the class of \(\frac{nx}{m}\) in \(\mathbb Z/n\). This is a concrete instance of how \(\delta\) encodes the failure of lifting across the diagram.
