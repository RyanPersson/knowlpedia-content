+++
id = "algebra-homological/five-lemma"
title = "Five lemma"
kind = "knowl"
summary = "In a morphism of exact five-term sequences, suitable isomorphism, epimorphism, and monomorphism hypotheses force the middle map to be an isomorphism."
aliases = ["five-lemma", "Five lemma"]
domains = ["algebra-homological"]
legacy_source_path = "algebra-homological/five-lemma.md"
prerequisites = ["algebra-category-theory/abelian-category", "algebra-homological/four-lemma"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

In an [[algebra-category-theory/abelian-category|abelian category]], consider a commutative diagram with exact rows
```tikz-cd
A_1 \arrow[r] \arrow[d, "f_1"] & A_2 \arrow[r] \arrow[d, "f_2"] & A_3 \arrow[r] \arrow[d, "f_3"] & A_4 \arrow[r] \arrow[d, "f_4"] & A_5 \arrow[d, "f_5"] \\
B_1 \arrow[r] & B_2 \arrow[r] & B_3 \arrow[r] & B_4 \arrow[r] & B_5
```
If \(f_1\) is an epimorphism, \(f_2\) and \(f_4\) are isomorphisms, and \(f_5\) is a monomorphism, then \(f_3\) is an isomorphism. In particular, if \(f_1,f_2,f_4,f_5\) are isomorphisms, then so is \(f_3\).

## Remarks

For modules, “epimorphism” and “monomorphism” mean surjective and injective, respectively. The result combines the injectivity and surjectivity conclusions of the [[algebra-homological/four-lemma|four lemma]].

See also [[algebra-homological/five-lemma-corollary|five lemma corollary]] for standard “short exact sequence” consequences.

## Examples

1. **Two-out-of-three for quasi-isomorphisms in a short exact sequence of complexes.**
   Suppose
   \[
   0\to C'_\bullet \to C_\bullet \to C''_\bullet \to 0
   \quad\text{and}\quad
   0\to D'_\bullet \to D_\bullet \to D''_\bullet \to 0
   \]
   are short exact sequences of [[algebra-homological/chain-complex|chain complexes]], and we have a morphism between them inducing a commutative diagram of long exact sequences in [[algebra-homological/homology-module|homology]].
   If the induced maps \(H_n(C'_\bullet)\to H_n(D'_\bullet)\) and \(H_n(C''_\bullet)\to H_n(D''_\bullet)\) are isomorphisms for all \(n\), then the induced maps \(H_n(C_\bullet)\to H_n(D_\bullet)\) are isomorphisms for all \(n\), by applying the five lemma degree-by-degree to the long exact homology sequences.

2. **Comparing Tor groups via a map of short exact sequences.**
   Given a morphism between short exact sequences
   \[
   \begin{array}{ccccccccc}
   0 &\to& A' &\to& A &\to& A'' &\to& 0\\
    && \downarrow && \downarrow && \downarrow &&\\
   0 &\to& B' &\to& B &\to& B'' &\to& 0
   \end{array}
   \]
   and a fixed module \(M\), naturality of the [[algebra-homological/long-exact-sequence-tor|long exact Tor sequence]] gives a morphism of long exact sequences
   \[
   \cdots \to \operatorname{Tor}_n(A'',M)\to \operatorname{Tor}_{n-1}(A',M)\to \cdots
   \]
   If the induced maps \(\operatorname{Tor}_n(A',M)\to \operatorname{Tor}_n(B',M)\) and \(\operatorname{Tor}_n(A'',M)\to \operatorname{Tor}_n(B'',M)\) are isomorphisms for all relevant neighboring terms (for instance, if \(A'\to B'\) and \(A''\to B''\) are isomorphisms), then the five lemma implies \(\operatorname{Tor}_n(A,M)\to \operatorname{Tor}_n(B,M)\) is an isomorphism as well.

3. **Comparing Ext groups (same pattern).**
   With the same setup, applying the [[algebra-homological/long-exact-sequence-ext|long exact Ext sequence]] and using the five lemma shows that if the induced maps on the surrounding \(\operatorname{Hom}\) and \(\operatorname{Ext}\) terms are isomorphisms, then the middle \(\operatorname{Ext}\)-map is an isomorphism. This is a standard way to propagate isomorphisms through long exact sequences.
