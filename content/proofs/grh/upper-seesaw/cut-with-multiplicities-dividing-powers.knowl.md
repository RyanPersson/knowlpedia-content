+++
id = "proofs/grh/upper-seesaw/cut-with-multiplicities-dividing-powers"
title = "A cut whose multiplicities divide powers of q"
kind = "lemma"
summary = "For levels J inside A and a compact set D on which q-power powers of conjugates of J fall into A, there is a finite cut, stable under S meet A, whose cover multiplicities divide powers of q."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.exists_index_dvd_pow_of_pow_mem", "New.Seesaw.exists_index_stabilizer_dvd_pow", "New.Seesaw.exists_finset_coverMultiplicity_dvd_pow"]
lean_files = ["src/New/UpperBound/Seesaw/IntegralAsCosetSum.lean"]
proof_status = "full"
+++

Let \(G_f\) be the [[?lean:New.Gf|finite adelic unitary group]] of a [[?c:Hermitian space|hermitian space]] over a
[[?c:CM field|CM field]], a [[?c:Locally compact group|locally compact]] totally disconnected
group. A [[?lean:New.IsLevel|level]] is an open subgroup of the compact open subgroup of integral
points.

**Lemma.** Let \(S\) and \(J\le A\le B\) be subgroups of \(G_f\) with \(J\) and \(A\) levels, and
\(q\) a natural number. Let \(D\subseteq G_f\) be compact such that every \(x\in D\) lies in \(B\)
and admits \(n\) with \((xux^{-1})^{q^{n}}\in A\) for all \(u\in J\). Let \(W\) be a property of
points of \(G_f\) such that \(W(x)\) implies \(rx\in D\) for some \(r\in S\). Then there is a
finite set \(T\subseteq G_f/J\) such that

(a) \(T\) is stable under \(S\cap A\);
(b) every \(x\) with \(xJ\in T\) lies in \(B\);
(c) whenever \(xJ\in T\) or \(W(x)\), the
[[proofs/grh/upper-seesaw/cover-multiplicity|cover multiplicity]] \(m_T(xJ)\) (for \(S,A\))
divides a power of \(q\); in particular it is nonzero.

## Proof

*Step 1 (groups of exponent \(q^{n}\)).* If \(K\le G\) has finite index and \(g^{q^{n}}\in K\) for
all \(g\in G\), then \([G:K]\) divides a power of \(q\). Indeed the normal core \(K_0\) of \(K\)
contains every \(g^{q^n}\) (apply the hypothesis to the conjugates \(cgc^{-1}\)), so \(G/K_0\) is a
finite group in which every element has order dividing \(q^{n}\); its order divides a power of
\(q\) ([[?c:Cauchy's theorem for finite groups|Cauchy's theorem]]), and \([G:K]\mid[G:K_0]\).

*Step 2 (stabilisers).* Let \(x\in G_f\) with \((xux^{-1})^{q^{n}}\in A\) for all \(u\in J\), and
let \(Z\) be the stabiliser in \(S\) of \(xJ\). For \(z\in Z\), \(x^{-1}zx\in J\), so
\(z^{q^{n}}=(x\,(x^{-1}zx)\,x^{-1})^{q^{n}}\in A\). Moreover \(Z\subseteq xJx^{-1}\subseteq xAx^{-1}\),
a compact group in which the open subgroup \(A\cap xAx^{-1}\) has finite index; so \(Z\cap A\) has
finite index in \(Z\). By Step 1, \([Z:Z\cap A]\) divides a power of \(q\).

*Step 3 (the cut).* Choose a set \(C\) of representatives, inside the image of \(D\) in \(G_f/J\),
of the \(S\)-orbits meeting that image, and let \(T\) be the saturation of \(C\) under \(S\cap A\).
Then \(T\) is contained in the image of the compact set \(A\cdot D\) in the discrete space
\(G_f/J\), hence finite. (a) holds by construction. (b): if \(xJ\in T\) then \(x\in r\,d\,J\) with
\(r\in A\le B\), \(d\in D\subseteq B\), \(J\le B\). (c): in both cases \(xJ\) lies in the \(S\)-orbit
of some \(t=dJ\in C\), \(d\in D\) (if \(W(x)\), because \(rx\in D\)). By the two properties of the
cover multiplicity, \(m_T(xJ)=m_T(t)=[Z:Z\cap A]\) with \(Z\) the stabiliser of \(t\), which divides
a power of \(q\) by Step 2 applied to \(d\). \(\blacksquare\)

## References

1. Lean: `New.Seesaw.exists_finset_coverMultiplicity_dvd_pow` and the two lemmas before it, in `src/New/UpperBound/Seesaw/IntegralAsCosetSum.lean`.
