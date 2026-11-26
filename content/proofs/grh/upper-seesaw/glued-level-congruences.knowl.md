+++
id = "proofs/grh/upper-seesaw/glued-level-congruences"
title = "Congruence levels inside the stabiliser of the glued lattice"
kind = "lemma"
summary = "A unitary element on X whose last row is that of 1 modulo pi maps into the stabiliser of the glued lattice, and congruences to 1 at places off N are preserved."
aliases = ["gluing condition for isometries"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Grading.exists_inclXFin_sub_one_eq", "New.Grading.inclXFin_mem_stdLevel", "New.mem_levelOf_bot", "New.Grading.inclXFin_mem_levelOf"]
lean_files = ["src/New/UpperBound/Seesaw/GluedLevel.lean"]
proof_status = "full"
+++

Let \(Y\) grade \(V\) by \(X\sqcup\{y_0\}\) and a string of \(s\) vectors, and suppose \(Y\)
[[proofs/grh/upper-seesaw/graded-lattice-basis|spans the lattice]] of \((a,\pi,u)\). The grading
embeds the [[?c:Finite adele ring of a number field|finite adelic]] unitary group of \(X\sqcup\{y_0\}\) into that of \(V\), by
\(h\mapsto h\oplus1\) in rational coordinates; write \(j(h)\in G_f(V)\) for the image
([[?lean:New.Grading.inclXFin|Lean: the inclusion of the small group]]), a matrix in the
coordinates of the frame \(x_f\).

**Lemma.**

1. There is an integral matrix \(R\) (rows indexed by \(X\sqcup\{y_0\}\)) such that for all \(h\)
   \[
   j(h)-1=R^{*}\,M_h\,R,
   \]
   where \(M_h=h-1\) if \(s\) is even, and for odd \(s\), \(M_h\) is \(h-1\) with its last row
   (index \(y_0\)) multiplied by \(\pi^{-1}\) and its last column by \(\bar\pi^{-1}\).
2. Let \((P,N,\pi)\) be a [[proofs/grh/upper-seesaw/split-squarefree-factorisation|split
   squarefree factorisation]]. If \(h\) is integral and its last row is congruent to that of \(1\)
   modulo \(\pi\widehat{\mathcal{O}}\), then \(j(h)\) stabilises the standard lattice
   \(\widehat{\mathcal{O}}^{\iota}\) (the glued lattice in the coordinates of \(x_f\)).
3. If moreover \((w_i)_{i\in I}\) are [[algebra-fields-galois/place-of-global-field|finite places]] with \(w_i,\bar w_i\notin P\) and \(h\) is
   congruent to \(1\) at every \(w_i\), then \(j(h)\) is integral and congruent to \(1\) at every
   \(w_i\).

## Proof

(1) Write \(x_f=\mathcal{B}k\), \(k\in\mathrm{GL}(\widehat{\mathcal{O}})\). In the coordinates of
\(x_f\), \(j(h)=x_f^{-1}(h\oplus1)x_f\), and since \(x_f^{*}Jx_f=1\) at the finite places,
\(x_f^{-1}=x_f^{*}J\); hence \(j(h)-1=x_f^{*}J\bigl((h\oplus1)-1\bigr)x_f\). The matrix
\(J((h\oplus1)-1)\) is supported on the block \(X\sqcup\{y_0\}\), where \(J=1\), and equals
\(h-1\) there. So \(j(h)-1=A^{*}(h-1)A\) with \(A\) the rows of \(x_f\) indexed by
\(X\sqcup\{y_0\}\). From the shape of \(\mathcal{B}\), these rows are the rows \(R\) of \(k\),
the last one divided by \(\bar\pi\) when \(s\) is odd: \(A=DR\) with \(D\) diagonal. Moving \(D\)
and \(D^{*}\) onto \(h-1\) gives \(M_h\).

(2) By (1) it suffices that \(M_h\) is integral: then \(j(h)=1+R^{*}M_hR\) is an integral
matrix, and it is unitary, so its inverse \(j(h)^{*}\) is integral too. For even \(s\) this is the
integrality of \(h\). For odd \(s\) check integrality place by place. Since \(P\cap\bar P=\emptyset\),
at every finite place \(w\) at least one of \(\pi_w\) and \((\bar\pi)_w=\overline{\pi_{\bar w}}\) is
a unit, so at \(w\) at most one of the two divisions matters.

* If \((\bar\pi)_w\) is a unit: only the division of the last row by \(\pi\) matters, and the last
  row of \(h-1\) is divisible by \(\pi\) by hypothesis (including the corner entry).
* If \(\pi_w\) is a unit: only the division of the last column by \(\bar\pi\) matters. The
  integral matrices whose last row is that of \(1\) modulo \(\pi\) form a group, so \(h^{-1}=h^{*}\)
  has the same property: \(\overline{h_{j,y_0}}-\delta_{j,y_0}\in\pi\widehat{\mathcal{O}}\) for all
  \(j\). Conjugating, the last column of \(h-1\) is divisible by \(\bar\pi\).

(3) By (2) \(j(h)\) is integral. An element is congruent to \(1\) at \(w_i\) iff it is integral and
all entries of \(g-1\) have valuation \(<1\) at \(w_i\). The entries of \(M_h\) are entries of
\(h-1\) times some of \(\pi^{-1},\bar\pi^{-1}\), which are units at \(w_i\); so they have valuation
\(<1\) at \(w_i\), and so do the entries of \(R^{*}M_hR\), sums of products of an entry of \(M_h\)
with two integral elements. \(\blacksquare\)

## Remarks

Part 2 is related to Nikulin's criterion for extending isometries to an overlattice: the
congruence on \(h\) plays the part of the condition that an isometry preserve the gluing.

## References

1. Lean: `New.Grading.exists_inclXFin_sub_one_eq`, `New.Grading.inclXFin_mem_stdLevel`, `New.Grading.inclXFin_mem_levelOf` in `src/New/UpperBound/Seesaw/GluedLevel.lean`.
