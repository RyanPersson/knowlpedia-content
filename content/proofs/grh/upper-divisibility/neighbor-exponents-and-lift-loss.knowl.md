+++
id = "proofs/grh/upper-divisibility/neighbor-exponents-and-lift-loss"
title = "Neighbours at a marked set: exponents, charges and the lift loss"
kind = "definition"
summary = "For a marked set and sets of marked indices: the diagonal neighbour, the exponent and the charge of a box, and the loss of a lift evaluated at a neighbour."
aliases = ["lift loss", "neighbor exponent", "neighbor charge", "neighbor diagonal", "marked indices"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.liftLoss", "New.Data.markedIndices", "New.Data.neighborExponent", "New.Data.neighborCharge", "New.Data.neighborDiagonal", "New.Data.IsMarked.map_ofSplitPlaces_neighborDiagonal"]
lean_files = ["src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean"]
+++

Let \(\Lambda\) be a [[proofs/grh/upper-divisibility/marked-set-of-primes|marked set]] of primes of \(E\) above \(p\) (at \(\iota\colon\mathbb{C}\to\mathbb{C}_p\)), with \(\Phi_\Lambda\), \(\Phi_{\bar\Lambda}\) the places inducing a prime of \(\Lambda\), respectively the conjugate of one. Let \(n'\) be an index set (the basis of \(X_{j+1}\)) and, for each prime \(\mathfrak l\), \(J(\mathfrak l)\subset n'\) a finite set.

- The **neighbour diagonal** is the element \(\nu_J\) of the finite adelic unitary group that at each \(\mathfrak l\in\Lambda\) is \(\operatorname{diag}(p\text{ on }J(\mathfrak l),\,1\text{ elsewhere})\), hence \(p^{-1}\) on \(J(\mathfrak l)\) at \(\bar{\mathfrak l}\), and \(1\) at all other places.
- The **marked indices** at \(\tau\in\Phi\) are \(J_\tau=J(w_\tau)\) if \(w_\tau\in\Lambda\), and \(J(\overline{w_\tau})\) otherwise.
- The **neighbour exponent** of an index \(b\) at \(\tau\) is \(\epsilon_\tau(b)=[\tau\in\Phi_\Lambda,\ b\in J_\tau]-[\tau\in\Phi_{\bar\Lambda},\ b\in J_\tau]\in\{1,0,-1\}\). Read in \(\mathbb{C}_p\) through \(\iota\circ\tau\circ\mathrm{conj}\), the neighbour diagonal is \(\operatorname{diag}\bigl(p^{-\epsilon_\tau(b)}\bigr)_b\).
- The **charge** of a box with index \(b\) in a column of height \(h\) at \(\tau\) is \(1\) if (\(\tau\in\Phi_\Lambda\), \(h=1\) and \(b\notin J_\tau\)) or (\(\tau\in\Phi_{\bar\Lambda}\) and \(b\in J_\tau\)); otherwise \(0\).
- The **lift loss** of stage \(j\) is
\[
\operatorname{ll}_\Lambda(j)=\mathfrak r\sum_{\sigma\in\Phi_\Lambda}c_j(\sigma)-\operatorname{db}_{p,j}(\Phi_\Lambda),
\]
with \(\mathfrak r=\mathfrak r(p)\), \(c_j\) the number of low columns and \(\operatorname{db}\) the [[proofs/grh/upper-divisibility/divisibility-bound|divisibility bound]] for the set \(\Phi_\Lambda\) of removed long rows.

## Remarks

The statement about the neighbour diagonal read at \(\tau\) holds because \(\iota\circ\tau\circ\mathrm{conj}\) factors through the completion at \(\overline{w_\tau}\), and \(\Lambda\) is disjoint from its conjugate.

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean`.
