+++
id = "proofs/grh/reduction-main/colength-divides"
title = "Colength dividing an element"
kind = "definition"
summary = "A basis-free substitute for 'the colength of N in M divides z': every finite family in M is carried into N by a square matrix whose determinant divides z."
aliases = ["colength divides", "ColengthDvd"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.ColengthDvd", "New.ColengthDvd.of_le", "New.ColengthDvd.of_dvd"]
lean_files = ["src/New/Reduction/Lattices/Colength.lean"]
+++

Let \(O\) be a [[?c:commutative ring|commutative ring]], \(V\) an \(O\)-[[algebra-modules/module|module]], \(M,N\subseteq V\) [[?c:submodule|submodules]] and \(z\in O\). No inclusion between \(M\) and \(N\) is assumed. We say that **the colength of \(N\) in \(M\) divides \(z\)**, written
\[
\operatorname{colen}(M,N)\mid z ,
\]
if for every integer \(n\ge 0\) and every family \(\Phi_1,\dots,\Phi_n\in M\) there is an \(n\times n\) matrix \(m=(m_{ik})\) with entries in \(O\) such that
\[
\det m \mid z \quad\text{in } O
\qquad\text{and}\qquad
\sum_{k=1}^{n} m_{ik}\,\Phi_k\in N\quad\text{for } i=1,\dots,n .
\]
(For \(n=0\) the empty matrix has [[?c:determinant of a square matrix|determinant]] \(1\).)

## Remarks

The symbol \(\operatorname{colen}(M,N)\) has no meaning on its own; only the relation "\(\operatorname{colen}(M,N)\mid z\)" is defined. Over a [[algebra-commutative/dvr|discrete valuation ring]] with valuation \(v\) and for finitely generated \(M\), the relation bounds the [[algebra-modules/length-module|length]] of \(M/(M\cap N)\) by \(v(z)\); see [[proofs/grh/reduction-main/colength-bounds-length|colength bounds a length]].

## Properties

1. If \(M\subseteq N\), then \(\operatorname{colen}(M,N)\mid z\) for every \(z\): take \(m\) the identity matrix.
2. If \(\operatorname{colen}(M,N)\mid z\) and \(z\mid z'\), then \(\operatorname{colen}(M,N)\mid z'\): the same matrices serve, since \(\det m\mid z\mid z'\).

Further rules are in [[proofs/grh/reduction-main/colength-calculus|the calculus of colengths]].

## References

1. Lean: `New.ColengthDvd`, `New.ColengthDvd.of_le`, `New.ColengthDvd.of_dvd` in `src/New/Reduction/Lattices/Colength.lean`.
