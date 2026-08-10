+++
id = "langlands/automorphic-galois-correspondence"
title = "Automorphic-Galois correspondence"
kind = "knowl"
summary = "The conjectural and partially proved association between algebraic automorphic representations and l-adic Galois representations."
aliases = ["automorphic to Galois correspondence", "automorphic Galois representation", "Galois representations attached to automorphic representations"]
domains = ["langlands", "number-theory", "representation-theory"]
section_mode = "progressive"
+++

The **automorphic–Galois correspondence** predicts that suitably
[[langlands/l-algebraic-automorphic-representation|\(L\)-algebraic]]
[[langlands/automorphic-representation|automorphic representations]] of a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] \(G\) over a
[[langlands-letter/knowls/global-local-fields-completions|number field]]
\(F\) have associated continuous \(\ell\)-adic homomorphisms

\[
\rho_{\pi,\iota}:
\operatorname{Gal}(\overline F/F)
\longrightarrow
{}^L G(\overline{\mathbb Q}_\ell),
\]

from the [[langlands-letter/knowls/galois-extension-and-group|absolute Galois
group]] into the [[langlands/l-group|\(L\)-group]], whose projection to the
Galois factor is the canonical one. The
representation should be unramified almost everywhere and satisfy
[[langlands/local-global-compatibility|local–global compatibility]].

This is a general conjecture with many major proved cases, not one theorem in
full generality.

## Unramified characterization

For almost every finite place \(v\nmid\ell\), the
[[algebra-groups/conjugacy-class|conjugacy class]] of the
[[langlands-letter/knowls/frobenius-unramified|Frobenius element]]
\(\rho_{\pi,\iota}(\operatorname{Frob}_v)\) should equal the image under
\(\iota\) of the [[langlands/satake-parameter|Satake parameter]] of
\(\pi_v\). Applying an algebraic representation
\(r:{}^LG\to\operatorname{GL}(V)\) should therefore give matching local
Euler factors.

## General linear groups

For [[langlands/regular-algebraic-cuspidal-automorphic-representation|regular algebraic cuspidal automorphic representations]] of
\(\operatorname{GL}_n\), [[langlands/compatible-system-of-galois-representations|compatible systems]] of \(n\)-dimensional Galois
representations are known in broad settings. The strongest theorem available
depends on the base field, regularity, self-duality or polarization, and the
place at which compatibility is requested. These hypotheses must not be
suppressed when citing a result.

## C-algebraic representations

A [[langlands/c-algebraic-automorphic-representation|\(C\)-algebraic]]
representation is naturally expected to produce a representation valued in
the \(C\)-group rather than necessarily in the ordinary \(L\)-group.
Twisting converts the two normalizations for many general linear groups but
not uniformly for all reductive groups.

## Not a naive bijection

A Galois representation can determine only an \(L\)-packet for a general
group, and global multiplicities require additional packet data. Conversely,
the compatible \(\ell\)-adic realization captures the algebraic part of the
automorphic spectrum, whereas a hypothetical global Langlands group is meant
to parameterize more general automorphic representations.

## References

1. Kevin Buzzard and Toby Gee, “The conjectural connections between
   automorphic representations and Galois representations,” Conjecture
   3.2.1. [arXiv](https://arxiv.org/abs/1009.0785).
2. Laurent Clozel, Michael Harris, and Richard Taylor, “Automorphy for some
   \(\ell\)-adic lifts of automorphic mod \(\ell\) Galois
   representations,” 2008.
3. Peter Scholze, “On torsion in the cohomology of locally symmetric
   varieties,” *Annals of Mathematics* 182 (2015), 945–1066.
   [DOI](https://doi.org/10.4007/annals.2015.182.3.3).
