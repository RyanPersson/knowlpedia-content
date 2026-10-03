+++
id = "ergodic-theory/von-neumann-mean-ergodic-theorem"
title = "Von Neumann mean ergodic theorem"
kind = "theorem"
summary = "Cesaro averages of an isometry converge in norm to the projection onto its fixed vectors."
aliases = ["mean ergodic theorem"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["linear-algebra/hilbert-space", "linear-algebra/orthogonal-projection", "functional-analysis/unitary-operator"]
+++

Let \(U\) be a linear isometry on a [[linear-algebra/hilbert-space|Hilbert space]] \(H\), and let \(P\) be the [[linear-algebra/orthogonal-projection|orthogonal projection]] onto \(\ker(I-U)\). The **mean ergodic theorem** states
\[
\frac1N\sum_{n=0}^{N-1}U^nf\longrightarrow Pf
\quad\text{in the norm of }H\qquad(f\in H).
\]
In particular it applies to unitary operators and to Koopman isometries of noninvertible probability-preserving maps.

## Proof by telescoping

For an isometry, \(\ker(I-U^*)=\ker(I-U)\), so
\[
H=\ker(I-U)\oplus\overline{\operatorname{ran}(I-U)}.
\]
The averages fix the first summand. On \(f=(I-U)h\), they equal \((h-U^Nh)/N\), whose norm is at most \(2\|h\|/N\). The averages have norm at most one; approximation therefore gives convergence to zero on the second summand.

## Conditional expectation

For \(U=U_T\) on a probability space, \(P f=\mathbb E[f\mid\mathcal I_T]\), with \(\mathcal I_T\) the [[ergodic-theory/invariant-sigma-algebra|invariant sigma-algebra]]. This is [[probability/conditional-expectation|conditional expectation]], which is orthogonal projection in \(L^2\). If \(T\) is ergodic, \(Pf=(\int f\,d\mu)1\).

## Mode of convergence

The conclusion is convergence in \(L^2\) for each observable, not operator-norm convergence of the averaging operators. It alone does not imply pointwise convergence along trajectories.

## References

1. Jesse Peterson, [*Lecture notes on ergodic theory*](https://www.math.vanderbilt.edu/~peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf), 2011. §1.6.1.
