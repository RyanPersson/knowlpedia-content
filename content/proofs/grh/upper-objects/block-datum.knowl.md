+++
id = "proofs/grh/upper-objects/block-datum"
title = "Block datum of a descent pair"
kind = "definition"
summary = "The finite Schwartz datum of a descent pair: at the places of M the indicator of the inclusion matrix, at the places of Q the tame character of a minor, and the vacuum elsewhere."
aliases = ["block datum", "identity block indicator"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.residueBlockDatum", "New.DescentPair.blockDatum", "New.DescentPair.identityBlockIndicator", "New.LevelPlaces.TwistGL", "New.LevelPlaces.twistResidue", "New.LevelPlaces.twistResidueLift"]
lean_files = ["src/New/UpperBound/Objects/AuxiliaryPair.lean"]
+++

Let \(O\) be a [[proofs/grh/upper-objects/descent-pair|descent pair]] with places \(M,Q\), injection \(u\colon r\hookrightarrow n\), inclusion matrix \(\iota_u\) and tame part \((\psi_w)\).

**Definition.** The **residue block datum** is the function of families \(X=(X_w)_{w\in M\sqcup Q}\) of \(n\times r\) matrices over the residue fields \(k_w\),
\[
\Psi_{\mathrm{bl}}(X)=\begin{cases}\displaystyle\prod_{w\in Q}\psi_w\big(\det (X_w)_{u}\big)&\text{if }X_w=\iota_u\text{ for all }w\in M,\\[1ex]0&\text{otherwise,}\end{cases}
\]
where \((X_w)_u\) is the \(r\times r\) matrix of the rows of \(X_w\) indexed by \(u\) (and \(\psi_w(0)=0\)).

The **block datum** \(\Psi_{\mathrm{bl}}\otimes\mathrm{vac}\) is the element of the finite part of the [[?lean:New.Space.hom|Schwartz space of \(\operatorname{Hom}(W,V)\)]] that is the [[?lean:New.vacuumDatum|vacuum datum]] of the function "apply \(\Psi_{\mathrm{bl}}\) to the reductions at the places of \(M\) and \(Q\)" of matrices modulo \(M^2Q\): it is this function on integral matrices at \(M,Q\), tensored with the finite vacuum at all other finite places (in the Heisenberg model of the development the finite vacuum vanishes off the lattice and equals a semicharacter, a root-of-unity phase, on it; it is not the plain indicator).

The **identity block indicator** \(\Psi^1\) is the indicator of the matrices \(y\) modulo \(MQ\) with \(y\equiv\iota_u\) at every place of \(M\) and \((y)_u\equiv1\) at every place of \(Q\).

## Remarks

Reading the block datum modulo \(MQ\) instead of \(M^2Q\) gives the same vector. Its two basic properties are in [[proofs/grh/upper-objects/block-datum-laws|laws of the block datum]].

## References

1. Lean: `New.DescentPair.residueBlockDatum`, `New.DescentPair.blockDatum`, `New.DescentPair.identityBlockIndicator` in `src/New/UpperBound/Objects/AuxiliaryPair.lean`.
