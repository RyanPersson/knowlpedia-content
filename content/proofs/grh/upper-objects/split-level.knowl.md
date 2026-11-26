+++
id = "proofs/grh/upper-objects/split-level"
title = "Split level at a prime N"
kind = "definition"
summary = "A finite set of places containing one place of each conjugate pair above a split prime N, with reduction modulo N and the character psi_N."
aliases = ["split level", "reduction modulo N at a split level", "character psi_N"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsSplitLevel", "New.residueOverN", "New.IsSplitLevel.residueEquiv", "New.IsSplitLevel.reduction", "New.IsSplitLevel.reduction_eq_iff", "New.IsSplitLevel.reduction_surjective", "New.IsSplitLevel.reductionGL", "New.IsSplitLevel.inclGL", "New.IsSplitLevel.liftGL", "New.IsSplitLevel.diagN", "New.IsSplitLevel.diagNInv", "New.IsSplitLevel.psiN"]
lean_files = ["src/New/UpperBound/Objects/LiftLawsModuloN.lean"]
+++

Let \(E\) be a [[?c:CM field|CM field]] with complex conjugation \(x\mapsto\bar x\), let \(N\) be a prime number, and let \(P\) be a finite set of finite [[algebra-fields-galois/place-of-global-field|places]] of \(E\). For a finite place \(w\) write \(E_w\) for the [[algebra-fields-galois/completion-at-place|completion]], \(\lvert\cdot\rvert_w\) for its normalised [[?c:absolute value of a nonarchimedean local field|absolute value]] (a uniformiser has absolute value \(e^{-1}\)), \(\mathcal O_w\) for its ring of integers, \(\mathbb F_w\) for its [[algebra-commutative/residue-field|residue field]], and \(\bar w\) for the conjugate place.

**Definition (split level).** The set \(P\) is a **split level for \(N\)** if

1. for every \(w\in P\) the conjugate place \(\bar w\) is not in \(P\) (in particular \(w\ne\bar w\));
2. for every \(w\in P\) the residue field \(\mathbb F_w\) has exactly \(N\) elements;
3. for every \(w\in P\), \(\lvert N\rvert_w=e^{-1}\), i.e. \(N\) is a uniformiser of \(E_w\);
4. a finite place \(w\) of \(E\) lies above \(N\) (i.e. \(N\) belongs to the prime ideal of \(w\)) if and only if \(w\in P\) or \(\bar w\in P\).

For a split level put \(E_P=\prod_{w\in P}E_w\) and \(\mathcal O_P=\prod_{w\in P}\mathcal O_w\). By 2 there is a unique ring isomorphism \(\mathbb F_w\cong\mathbb Z/N\) for each \(w\in P\), and the **reduction modulo \(N\)** is the ring homomorphism
\[
\mathcal O_P\longrightarrow(\mathbb Z/N)^P,\qquad x\longmapsto \bar x=(x_w \bmod N)_{w\in P}.
\]
It is applied entrywise to vectors and matrices over \(\mathcal O_P\), in particular it gives a group homomorphism \(\mathrm{GL}_n(\mathcal O_P)\to\mathrm{GL}_n((\mathbb Z/N)^P)\).

For \(y\in(\mathbb Z/N)^P\) let \(y/N\) denote the finite [[?c:finite adele ring of a number field|adele]] of \(E\) whose component at \(w\in P\) is \(\tilde y_w/N\), where \(\tilde y_w\in\{0,\dots,N-1\}\) represents \(y_w\), and whose other components are \(0\). Given the additive character \(\psi\) of the finite adeles of \(E\) fixed by the [[?lean:New.WeilData|Weil data]] (the [[?lean:New.stdLattice.selfDualAddChar|self-dual additive character]]), the **character \(\psi_N\)** is
\[
\psi_N\colon(\mathbb Z/N)^P\to\mathbb C,\qquad \psi_N(y)=\psi(-y/N).
\]

For an index set \(n\) write \(n^+=n\sqcup\{\ast\}\); the index \(\ast\) is called the *last* index and \(e_\ast\) the *last basis vector*. The matrix \(D_N=\operatorname{diag}(1,\dots,1,N^{-1})\in\mathrm{GL}_{n^+}(E_P)\) has the entry \(N^{-1}\) (at every place of \(P\)) in position \((\ast,\ast)\).

## Properties

**Criterion for the reduction.** For \(x\in\mathcal O_P\) and \(c\in(\mathbb Z/N)^P\), \(\bar x=c\) if and only if \(\lvert (x_w-\tilde c_w)/N\rvert_w\le1\) for all \(w\in P\). Indeed \(x_w-\tilde c_w\) has residue \(0\) exactly when its absolute value is \(<1\), i.e. \(\le e^{-1}=\lvert N\rvert_w\). In particular \(\bar x=0\) iff \(\lvert x_w\rvert_w\le e^{-1}\) for all \(w\), and \(\bar x=1\) iff \(\lvert x_w-1\rvert_w\le e^{-1}\) for all \(w\).

**Surjectivity.** The reduction is surjective (the family \((\tilde y_w)_w\) of integers reduces to \(y\)) and it is a local homomorphism: \(x\) is a unit of \(\mathcal O_P\) iff \(\bar x\) is a unit. Consequently \(\mathrm{GL}_n(\mathcal O_P)\to\mathrm{GL}_n((\mathbb Z/N)^P)\) is surjective; the Lean text fixes a set-theoretic section of it.

## Remarks

In the application \(N\) is the level prime of the data, \(N=\pi_N\bar\pi_N\) splits completely in \(E\), and \(P\) is the set of places dividing \(\pi_N\) (see [[proofs/grh/upper-objects/level-places-of-the-data|level places of the data]]).

The Lean definition of \(D_N^{-1}\) (called `diagN n S`) allows the entry \(N\) only at the places of \(P\) in an auxiliary set \(S\); only \(S=P\) is used in this file.

## References

1. Lean: `New.IsSplitLevel`, `New.residueOverN`, `New.IsSplitLevel.reduction`, `New.IsSplitLevel.psiN`, `New.IsSplitLevel.diagNInv` in `src/New/UpperBound/Objects/LiftLawsModuloN.lean`.
