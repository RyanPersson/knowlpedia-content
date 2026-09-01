+++
id = "algebra-homological/long-exact-sequence-tor"
title = "Long exact sequence for Tor"
kind = "knowl"
summary = "The natural long exact sequence in Tor induced by a short exact sequence of modules."
aliases = ["long-exact-sequence-tor", "Long exact sequence for Tor"]
domains = ["algebra-homological"]
prerequisites = ["algebra-modules/short-exact-sequence", "algebra-homological/connecting-homomorphism-lemma", "algebra-homological/long-exact-sequence-derived"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-homological/long-exact-sequence-tor.md"
+++

Let \(R\) be a ring, let
\[
0 \longrightarrow A' \xrightarrow{u} A \xrightarrow{v} A'' \longrightarrow 0
\]
be a [[algebra-modules/short-exact-sequence|short exact sequence]] of **right** \(R\)-modules, and let \(B\) be a **left** \(R\)-module. Then there are natural connecting homomorphisms
\[
\delta_n:\operatorname{Tor}_n^R(A'',B)\longrightarrow \operatorname{Tor}_{n-1}^R(A',B)
\quad (n\ge 1),
\]
(see [[algebra-homological/connecting-homomorphism-lemma|connecting homomorphism]]) such that the following sequence is exact:
\[
\cdots \to \operatorname{Tor}_2^R(A'',B)\xrightarrow{\delta_2}\operatorname{Tor}_1^R(A',B)\to
\operatorname{Tor}_1^R(A,B)\to \operatorname{Tor}_1^R(A'',B)
\xrightarrow{\delta_1} A'\otimes_R B \to A\otimes_R B \to A''\otimes_R B \to 0.
\]

Equivalently, for every \(n\ge 1\) one has exactness at the three-term window
\[
\operatorname{Tor}_n^R(A',B)\longrightarrow \operatorname{Tor}_n^R(A,B)\longrightarrow \operatorname{Tor}_n^R(A'',B)\xrightarrow{\delta_n}\operatorname{Tor}_{n-1}^R(A',B).
\]

This is a special case of the general [[algebra-homological/long-exact-sequence-derived|long exact sequence for derived functors]].

## Examples

1. **Computing \(\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\).**
   Use the short exact sequence
   \[
   0\to \mathbb Z \xrightarrow{\cdot n}\mathbb Z \to \mathbb Z/n \to 0.
   \]
   Tensor with \(\mathbb Z/m\). Since \(\mathbb Z\otimes \mathbb Z/m\cong \mathbb Z/m\), the relevant part of the long exact sequence becomes
   \[
   0 \to \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/n,\mathbb Z/m) \to \mathbb Z/m \xrightarrow{\cdot n} \mathbb Z/m \to (\mathbb Z/n)\otimes \mathbb Z/m \to 0.
   \]
   Hence
   \[
   \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\cong \ker(\cdot n:\mathbb Z/m\to \mathbb Z/m)\cong \mathbb Z/\gcd(n,m).
   \]
   (Also \(\operatorname{Tor}_i^{\mathbb Z}(\mathbb Z/n,-)=0\) for \(i\ge 2\) because \(\mathbb Z/n\) has a length-1 projective resolution.)

2. **Over a field, higher Tor vanishes.**
   If \(R=k\) is a field and \(V,W\) are \(k\)-vector spaces, then \(V\) is free (hence projective), so \(\operatorname{Tor}_i^k(V,W)=0\) for all \(i\ge 1\). The long exact sequence above reduces to exactness of
   \[
   0\to V'\otimes_k W \to V\otimes_k W \to V''\otimes_k W \to 0,
   \]
   reflecting that \(-\otimes_k W\) is exact.

3. **Dual numbers.** Let \(R=k[\varepsilon]/(\varepsilon^2)\) and regard \(k=R/(\varepsilon)\) as an \(R\)-module. The periodic free resolution
   \[
   \cdots\xrightarrow{\cdot\varepsilon}R\xrightarrow{\cdot\varepsilon}R
   \xrightarrow{\cdot\varepsilon}R\longrightarrow k\longrightarrow0
   \]
   becomes a complex with zero differentials after tensoring with \(k\). Hence
   \[
   \operatorname{Tor}_i^R(k,k)\cong k\qquad(i\ge1).
   \]
