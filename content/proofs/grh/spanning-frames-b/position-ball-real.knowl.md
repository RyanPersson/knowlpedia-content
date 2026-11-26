+++
id = "proofs/grh/spanning-frames-b/position-ball-real"
title = "Position ball at a real place"
kind = "definition"
summary = "The positions x of G1 for which all entries of x - 1 have modulus at most T^(99n)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.positionBall"]
lean_files = ["src/New/Spanning/Frames/RealShells.lean"]
+++

In the [[proofs/grh/spanning-frames-b/real-place-setting|notation at a real place]], let \(T\) be a real number. The **position ball at scale \(T\)** is the measurable set
\[
\mathcal{B}(T)=\bigl\{x\in G_1:\ \lvert(x-1)_{ac}\rvert\le T^{99n}\ \text{for all basis indices }a,c\bigr\},
\]
where \(x-1\) is the difference of the matrix of \(x\) and the identity matrix. Positions outside \(\mathcal{B}(T)\) are called *remote* at the scale \(T\).

## References

1. Lean: `New.Floors.positionBall`, `New.Floors.measurableSet_positionBall` in `src/New/Spanning/Frames/RealShells.lean`.
