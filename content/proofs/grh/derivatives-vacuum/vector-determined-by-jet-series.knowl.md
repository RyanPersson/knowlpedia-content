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

Fix \(y\in Z\). By [[proofs/grh/derivatives-vacuum/taylor-series-on-a-line-from-jet-series|the line lemma]] the Taylor series at \(0\) of the entire function \(t\mapsto\Theta_f(a\,t\,y)\) is a substitution into \(J_a(f)=0\), hence is \(0\); an [[?c:Entire function|entire function]] with vanishing Taylor series vanishes identically. At \(t=a^{-1}\) this gives \(\Theta_f(y)=0\). By definition \(\Theta_f(y)=f(\operatorname{realVec}y)\,e^{\lvert y\rvert^2/2}\), where \(f(x)=\theta(\varrho(x)f)\) is the theta evaluation of the vector \(f\) at the adelic vector \(x\); so \(f(\operatorname{realVec}y)=0\) for all \(y\), i.e. the theta evaluations of \(f\) vanish at all adelic vectors with finite part zero. Finally, a vector of \(\mathcal{S}(V)\) whose theta evaluations vanish at all such vectors is \(0\). This is a statement about theta evaluations in the Weil model, not about arbitrary functions: translation by a rational vector changes the evaluation by a factor of absolute value one and removes a rational finite part, the vectors with rational finite part are dense by strong approximation, and the evaluations are continuous and determine \(f\). This last step is asserted here (Lean `New.Space.eq_zero_of_apply_realVec_eq_zero`).

## References

1. Lean: `New.Space.eq_zero_of_jetSeries_eq_zero` in `src/New/Derivatives/Vacuum/TightFrames.lean`.
