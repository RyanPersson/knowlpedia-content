+++
id = "proofs/grh/derivatives-vacuum/vector-determined-by-jet-series"
title = "A vector of the finite part is determined by its jet series"
kind = "lemma"
summary = "If the jet series at a nonzero scale of a vector of the finite part vanishes, the vector is zero."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Space.eq_zero_of_jetSeries_eq_zero"]
lean_files = ["src/New/Derivatives/Vacuum/TightFrames.lean"]
proof_status = "outline"
+++

Notation as in [[proofs/grh/derivatives-vacuum/taylor-series-on-a-line-from-jet-series|the lemma on Taylor series along lines]]: \(V\) has all signs \(+1\).

**Lemma.** Let \(f\) lie in the finite part of \(V\) and let \(a\in\mathbb{C}\), \(a\ne0\). If \(J_a(f)=0\), then \(f=0\).

## Proof

Fix \(y\in Z\). By [[proofs/grh/derivatives-vacuum/taylor-series-on-a-line-from-jet-series|the line lemma]] the Taylor series at \(0\) of the entire function \(t\mapsto\Theta_f(a\,t\,y)\) is a substitution into \(J_a(f)=0\), hence is \(0\); an [[?c:Entire function|entire function]] with vanishing Taylor series vanishes identically. At \(t=a^{-1}\) this gives \(\Theta_f(y)=0\), hence \(\theta(\varrho(y)f)=0\), and for \(f\) in the finite part this value is \(f(\operatorname{realVec}y)\) up to the nonzero Gaussian factor. Finally a Schwartz vector that vanishes at all vectors \(\operatorname{realVec}y\) is \(0\); this last step is asserted here (Lean `New.Space.eq_zero_of_apply_realVec_eq_zero`).

## References

1. Lean: `New.Space.eq_zero_of_jetSeries_eq_zero` in `src/New/Derivatives/Vacuum/TightFrames.lean`.
