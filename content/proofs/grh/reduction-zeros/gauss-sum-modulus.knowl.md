+++
id = "proofs/grh/reduction-zeros/gauss-sum-modulus"
title = "The modulus of the Gauss sum of a primitive character"
kind = "lemma"
summary = "The Gauss sum of a primitive Dirichlet character modulo q has absolute value sqrt(q)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.norm_gaussSum_of_isPrimitive"]
lean_files = ["src/Lib/Analytic/PolyaVinogradov.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\chi\) be a [[?c:primitive Dirichlet character|primitive]] complex Dirichlet character modulo \(q\ge1\) and \(\tau(\chi)=\sum_{a\bmod q}\chi(a)e^{2\pi ia/q}\) its [[?c:Gauss sum|Gauss sum]]. Then \(\lvert\tau(\chi)\rvert=\sqrt q\).

## Proof

For primitive \(\chi\) the [[?c:discrete Fourier transform on a finite cyclic group|discrete Fourier transform]] of \(\chi\) is \(\widehat\chi(k)=\chi^{-1}(-k)\,\tau(\chi)\). Applying the transform again and using \(\widehat{\widehat\chi}(k)=q\,\chi(-k)\) at \(k=-1\):
\[
q=q\chi(1)=\tau(\chi)\sum_{a}\chi^{-1}(-a)e^{2\pi ia/q}=\tau(\chi)\,\overline{\tau(\chi)},
\]
because \(\chi^{-1}=\overline\chi\) and \(\overline{\tau(\chi)}=\sum_a\overline{\chi(a)}e^{-2\pi ia/q}=\sum_a\overline\chi(-a)e^{2\pi ia/q}\). \(\blacksquare\)

## References

1. Lean: `New.norm_gaussSum_of_isPrimitive` in `src/Lib/Analytic/PolyaVinogradov.lean`.
