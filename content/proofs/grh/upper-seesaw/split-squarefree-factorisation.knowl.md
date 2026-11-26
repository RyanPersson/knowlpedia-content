+++
id = "proofs/grh/upper-seesaw/split-squarefree-factorisation"
title = "Split squarefree factorisation of N"
kind = "definition"
summary = "A factorisation N = pi pi-bar by a finite idele that is a uniformiser exactly at a set of places disjoint from its conjugate."
aliases = ["IsSplitSquarefree"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.IsSplitSquarefree"]
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleCombinations.lean"]
+++

Let \(E\) be a [[?c:CM field|CM field]] with complex conjugation \(x\mapsto\bar x\), which also
acts on the [[?c:Finite adele ring of a number field|finite adeles]] \(\mathbb{A}_{E,f}\) and on
the [[algebra-fields-galois/place-of-global-field|finite places]] of \(E\). Let \(P\) be a finite set of finite places of \(E\), let \(N\in E\) and
let \(\pi\) be a [[?c:Idele group|finite idele]] of \(E\). The triple \((P,N,\pi)\) is a **split
squarefree factorisation** if

1. \(N=\pi\,\bar\pi\) in \(\mathbb{A}_{E,f}\);
2. for every finite place \(w\): \(\pi_w\) is a [[?c:Uniformizer|uniformiser]] at \(w\) if \(w\in P\), and a unit at
   \(w\) if \(w\notin P\);
3. for every \(w\in P\) the conjugate place \(\bar w\) is not in \(P\).

## Remarks

Then \(N\) has valuation \(1\) at the places of \(P\cup\bar P\) and \(0\) elsewhere, and every place
dividing \(N\) is split over the maximal totally real subfield. In the proof, \(N\) is the level
prime (a rational prime split in \(E\)), \(\pi=\pi_N\) and \(P\) is the set of places dividing
\(\pi_N\).

## References

1. Lean: `New.Seesaw.IsSplitSquarefree` in `src/New/UpperBound/Seesaw/AdmissibleCombinations.lean`.
