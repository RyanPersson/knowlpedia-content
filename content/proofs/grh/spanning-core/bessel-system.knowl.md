+++
id = "proofs/grh/spanning-core/bessel-system"
title = "Bessel system at a real place"
kind = "definition"
summary = "The data of a Bessel function and its cut at a real place, with the bounds used in the filling argument."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.BesselSystem"]
lean_files = ["src/New/Spanning/Bessel/Basic.lean"]
+++

Let \(\mathfrak s\) be a [[?lean:New.Shape|shape]] with real unitary group \(G_1\) of rank \(r\), \(b\in\mathbb{R}\) and \(f\in\mathbb{N}\). A **Bessel system** for \((\mathfrak s,b,f)\) consists of

* a finite nonempty index set \(I\) (the value space is \(\pi=\mathbb{C}^I\));
* two continuous functions \(W=W^{\mathrm{full}}\) (the Bessel function) and \(W^\flat=W^{\mathrm{cut}}\) (its cut) from \(G_1\) to \(\mathbb{C}^I\);
* a real number \(\deg>0\) (the **degree**);
* a homomorphism \(\mathrm{rep}\colon U(\kappa)\to U(I)\) (the **type**);
* forms \(J_i(p,q)\) (the **band limit**),

such that

1. \((W,W^\flat)\) is a [[proofs/grh/spanning-core/cut-pair-of-bessel-functions|cut pair]] for \((b,f,\mathrm{rep})\);
2. \(\mathrm{rep}\) is irreducible in the sense that every \(I\times I\) matrix commuting with all \(\mathrm{rep}(h)\) is scalar;
3. for every \(P\ge b^5\), \(W\) [[proofs/grh/spanning-core/schur-bound-for-a-bessel-function|has the Schur bound]] with constants \(P\) and \(\lvert I\rvert/\deg\);
4. \(8r\le b\);
5. \(W^\flat\) [[proofs/grh/spanning-core/local-bounds-of-a-bessel-function|has local bounds]] \((b,\deg,J)\).

## References

1. Lean: `New.BesselSystem` in `src/New/Spanning/Bessel/Basic.lean`.
