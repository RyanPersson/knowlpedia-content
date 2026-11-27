+++
id = "proofs/grh/spanning-unfolding-a/number-of-classes-of-the-source-level"
title = "The number of classes of the source level"
kind = "theorem"
summary = "The number of classes on U(X_0) is |H-bar| (N^k - 1)^f mass_k, and the main second moment is (|H-bar| (N^k-1)^f mass_k d)^2 / (deg mass_r)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.card_classes_eq_card_mul_pow_mul_mass", "New.Data.relIndex_latticeStabilizer", "New.Data.filling_mainSecondMoment_eq"]
lean_files = ["src/New/Spanning/Unfolding/FillingAdmissible.lean"]
proof_status = "full"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]] with prime level \(N\), ranks \(k\le r\), \(f\) [[?c:Infinite place of a number field|infinite places]], and \(S_D\) its [[?lean:New.Data.filling|filling data]]. Let \(K_0\) be the group of integral finite adelic points of \(U(X_0)\) ([[?lean:New.stdLevel|standard level]]), \(\iota\) the inclusion into the group of \(V\), \(K\) the lattice stabiliser, \(\bar H\) the [[proofs/grh/spanning-unfolding-a/reduced-levi-group|reduction of \(U(X_0)\)]] and \(\operatorname{mass}_l\) the [[?lean:New.mass|mass]] in rank \(l\). Then:

1. \([K_0:\iota^{-1}(K)]=(N^k-1)^f\);
2. the number of [[?lean:New.Filling.Classes|classes]] is \(n_X=\lvert\bar H\rvert\,(N^k-1)^f\operatorname{mass}_k\);
3. the [[?lean:New.Filling.mainSecondMoment|main second moment]] is \(\dfrac{\bigl(\lvert\bar H\rvert(N^k-1)^f\operatorname{mass}_k\,d\bigr)^2}{\deg\cdot\operatorname{mass}_r}\), with \(d\) the number of tuples of Bessel coordinates and \(\deg\) the Bessel degree.

## Proof

1. By the proposition on [[proofs/grh/spanning-unfolding-a/unitary-group-of-x0-in-lattice-basis|\(U(X_0)\) in the lattice basis]], \(\iota^{-1}(K)\) consists of the integral \(x\) whose row \(k_0\) is congruent to that of \(1\) modulo \(\pi\). An integral adele is divisible by \(\pi\) iff it reduces to \(0\) at each of the places dividing \(\pi\) ([[?lean:New.Data.piNPlaces|places dividing \(\pi\)]]); there are \(f\) of them, with [[algebra-commutative/residue-field|residue fields]] of \(N\) elements, none conjugate to another. So \(\iota^{-1}(K)\) is the preimage under reduction at these places of the product of the subgroups \(H_w\subseteq GL_k(\mathbb F_w)\) of matrices whose row \(k_0\) is the unit vector, i.e. whose inverse transpose fixes the unit vector. The index of such a preimage in \(K_0\) is the product of the indices of the \(H_w\) ([[?lean:New.relIndex_levelOf|index of a level defined by reduction]]), and the stabiliser of a nonzero vector in \(GL_k(\mathbb F_w)\) has index \(N^k-1\), the number of nonzero vectors ([[algebra-groups/orbit-stabilizer-theorem|orbit–stabiliser theorem]]).

2. The stabilisers of the classes are trivial, so the number of classes is the class sum of \(1\) for the source level, which is the index of the source level in \(K_0\) times the class sum for \(K_0\), namely \(\operatorname{mass}_k\) ([[?lean:New.classSum_one_of_le|class sums and indices]]). The index factors along \(\text{source level}\subseteq\iota^{-1}(K)\subseteq K_0\): the first index is \(\lvert\bar H\rvert\) by the theorem on the [[proofs/grh/spanning-unfolding-a/reduced-levi-group|reduced Levi group]] (the source level is \(\iota^{-1}(K(M))\)), the second is given by 1.

3. The main second moment is by definition \((n_Xd)^2/(\deg\operatorname{mass}_r)\).

## References

1. Lean: `New.Data.card_classes_eq_card_mul_pow_mul_mass` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
2. Lean: `New.Data.relIndex_latticeStabilizer` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
3. Lean: `New.Data.filling_mainSecondMoment_eq` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
