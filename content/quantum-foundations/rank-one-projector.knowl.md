+++
id = "quantum-foundations/rank-one-projector"
title = "Rank-one projector"
kind = "knowl"
summary = "The orthogonal projection onto the line spanned by a normalized vector."
aliases = ["rank-one projector", "rank-one projection"]
domains = ["quantum-foundations", "linear-algebra"]
+++

For a [[quantum-foundations/normalized-state-vector|normalized vector]] \(\psi\) in a complex Hilbert space, the **rank-one projector** onto its span is the operator
\[
\Pi_\psi=|\psi\rangle\langle\psi|,\qquad
\Pi_\psi(x)=\langle\psi,x\rangle\psi.
\]
It is an [[linear-algebra/orthogonal-projection|orthogonal projection]], is [[quantum-foundations/positive-semidefinite-operator|positive semidefinite]], is idempotent, and has trace one. Multiplying \(\psi\) by a complex phase leaves \(\Pi_\psi\) unchanged, so the projector represents the associated one-dimensional complex line rather than a chosen vector on it.
