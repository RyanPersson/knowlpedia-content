+++
id = "proofs/grh/upper-objects/ramified-vector-at-split-level"
title = "Ramified vector at a split level"
kind = "definition"
summary = "A vector of a representation of GL at a split level that, at each place, is of the form psi minus a unit scalar applied to psi."
aliases = ["ramified vector"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsSplitLevel.ramified", "New.IsSplitLevel.map_mem_ramified", "New.IsSplitLevel.upOperator_mem_ramified", "New.IsSplitLevel.upOperator_pow_mem_ramified"]
lean_files = ["src/New/UpperBound/Objects/LiftLawsModuloN.lean"]
+++

Let \(P\) be a [[proofs/grh/upper-objects/split-level|split level]] for \(N\) and \(\pi\) a complex [[algebra-representation-theory/group-representation|representation]] of \(\mathrm{GL}_{n^+}(E_P)\).

**Definition.** A vector \(\varphi\in\pi\) is **ramified** if for every place \(w\in P\) there are a unit \(x\in\mathcal O_P^\times\) with \(\bar x_{w'}=1\) in \(\mathbb Z/N\) for all \(w'\in P\setminus\{w\}\), and a vector \(\psi\in\pi\), such that
\[
\varphi=\psi-\pi(x\cdot 1)\psi ,
\]
where \(x\cdot1\) is the scalar matrix.

## Properties

1. If \(T\colon\pi\to\pi'\) is a linear map with \(\pi'(x\cdot1)\,T=T\,\pi(x\cdot1)\) for all \(x\in\mathcal O_P^\times\), then \(T\) maps ramified vectors to ramified vectors (apply \(T\) to \(\psi\)).
2. The [[proofs/grh/upper-objects/up-operator|operator Up]] and all its powers preserve ramified vectors, because Up commutes with scalar matrices.

## Remarks

A vector fixed by the scalars congruent to \(1\) modulo \(N\) whose mean over the unit scalars at each \(w\in P\) is zero has this form (this motivates the name and is how ramified source forms arise; it is not used in this file).

## References

1. Lean: `New.IsSplitLevel.ramified`, `map_mem_ramified`, `upOperator_pow_mem_ramified` in `src/New/UpperBound/Objects/LiftLawsModuloN.lean`.
