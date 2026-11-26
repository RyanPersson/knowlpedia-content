+++
id = "proofs/grh/spanning-frames-b/dyadic-shell"
title = "Dyadic shell at a real place"
kind = "definition"
summary = "The positions x for which 2^i is the least power of 2 bounding the entries of x - 1."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.dyadicShell", "New.Floors.exists_mem_dyadicShell", "New.Floors.notMem_positionBall_of_mem_dyadicShell"]
lean_files = ["src/New/Spanning/Frames/RealShells.lean"]
+++

In the [[proofs/grh/spanning-frames-b/real-place-setting|notation at a real place]], let \(i\ge0\) be an integer. The **dyadic shell of index \(i\)** is
\[
\mathcal{S}_i=\Bigl\{x\in G_1:\ i=\min\bigl\{l\in\mathbb{N}:\ \lvert(x-1)_{ac}\rvert\le2^{l}\ \text{for all }a,c\bigr\}\Bigr\}.
\]

## Properties

1. Every \(x\in G_1\) lies in exactly one dyadic shell: the entries of \(x-1\) are bounded, so the set of admissible \(l\) is nonempty and has a least element.
2. If \(T\ge1\) and \(2T^{99n}\le2^{i}\), then \(\mathcal{S}_i\) is disjoint from the [[proofs/grh/spanning-frames-b/position-ball-real|position ball]] \(\mathcal{B}(T)\). Indeed \(i\ge1\) because \(2T^{99n}\ge2\); if \(x\in\mathcal{S}_i\cap\mathcal{B}(T)\), the entries of \(x-1\) would be at most \(T^{99n}\le2^{i-1}\), against the minimality of \(i\).

## References

1. Lean: `New.Floors.dyadicShell`, `New.Floors.exists_mem_dyadicShell`, `New.Floors.notMem_positionBall_of_mem_dyadicShell` in `src/New/Spanning/Frames/RealShells.lean`.
