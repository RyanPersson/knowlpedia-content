+++
id = "proofs/grh/spanning-unfolding-b/norm-one-pairs-under-inversion-and-unipotent-multiplication"
title = "Norm-one pairs under inversion and unipotent multiplication"
kind = "lemma"
summary = "The condition that a norm-one pair occurs from an index is preserved by inversion and by left multiplication with the Bessel unipotent group, and it lets one prescribe the top coefficients of a shared vector."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.NormOnePairOccursFrom.inv", "New.NormOnePairOccursFrom.besselU_mul", "New.Filling.exists_frameImage_eq_of_pairOccursAt", "New.Filling.exists_frameImage_eq_of_normOnePairOccursFrom"]
lean_files = ["src/New/Spanning/Unfolding/Link.lean"]
proof_status = "full"
+++

**Lemma.** Let \(F\) be a commutative ring with involution, \(\gamma\) an isometry of a split Gram matrix, \(f\) the frame, and \(j\ge0\). Suppose [[proofs/grh/spanning-unfolding-b/cell-rank-of-a-term|a norm-one pair occurs from \(j\)]] for \(\gamma\).

1. A norm-one pair occurs from \(j\) for \(\gamma^{-1}\).
2. For every \(u\) in the [[?lean:New.Shape.Form.besselU|Bessel unipotent group]], a norm-one pair occurs from \(j\) for \(u\gamma\).
3. If \(j\le\varrho+1\), then for every \(y\in F^{\varrho+1}\) there are \(x,y'\in F^{\varrho+1}\) with \(f\cdot x=\gamma f\cdot y'\) and \(y'_a=y_a\) for all \(a\ge j\). (For this, it suffices that for some fixed \(c\) the pair \((c,1)\) occurs at every \(a\ge j\).)

## Proof

Let \(c\) with \(c\bar c=1\) be given, and for \(a\ge j\) let \(x,y\) satisfy \(f\cdot x=\gamma f\cdot y\), \(x_a=c\), \(y_a=1\), \(x_b=y_b=0\) for \(b>a\).

(1) Applying \(\gamma^{-1}\) gives \(f\cdot y=\gamma^{-1}f\cdot x\). Multiply by \(\bar c\): the vectors \(\bar cy\) and \(\bar cx\) have leading coefficients \(\bar c\) and \(\bar cc=1\) at \(a\) and vanish above \(a\). So the pair \((\bar c,1)\) occurs at \(a\) for \(\gamma^{-1}\), and \(\bar c\,\bar{\bar c}=1\).

(2) An element \(u\) of the Bessel unipotent group maps the span of the frame to itself, acting on coefficient vectors by an upper unitriangular matrix \(U\): \(u(f\cdot x)=f\cdot(Ux)\) ([[?lean:New.frameMatrix_unitriangular|the frame block of a unipotent element]]). Since \(x_b=0\) for \(b>a\), \((Ux)_b=x_b\) for all \(b\ge a\). Hence \(f\cdot(Ux)=u\gamma f\cdot y\) with \((Ux)_a=c\), \(y_a=1\) and vanishing above \(a\).

(3) Descending induction on \(j\). For \(j=\varrho+1\) take \(x=y'=0\). Suppose the statement holds for \(j+1\): there are \(x,z\) with \(f\cdot x=\gamma f\cdot z\) and \(z_a=y_a\) for \(a>j\). Let \(X,Y\) be a shared pair at \(j\): \(f\cdot X=\gamma f\cdot Y\), \(Y_j=1\), \(Y_b=0\) for \(b>j\). Then \(x+(y_j-z_j)X\) and \(y'=z+(y_j-z_j)Y\) satisfy \(f\cdot(x+(y_j-z_j)X)=\gamma f\cdot y'\), \(y'_j=y_j\) and \(y'_a=z_a=y_a\) for \(a>j\).

## References

1. Lean: `New.NormOnePairOccursFrom.inv`, `New.NormOnePairOccursFrom.besselU_mul`, `New.Filling.exists_frameImage_eq_of_pairOccursAt`, `New.Filling.exists_frameImage_eq_of_normOnePairOccursFrom` in `src/New/Spanning/Unfolding/Link.lean`.
