+++
id = "proofs/grh/onelift-comparison/projection-to-lifts-does-not-increase-norm"
title = "Projection to a space of lifts does not increase any conjugate norm"
kind = "theorem"
summary = "On forms orthogonal to the false lifts, the orthogonal projection to a subspace Z of the image of a central idempotent killed by a Hecke polynomial does not increase the norm at any automorphism sigma."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.mem_sup_ker_sup_range_of_isOrthogonalToFalseLifts", "New.DescentPair.normSqAt_starProjection_le"]
lean_files = ["src/New/OneLift/TestedForms.lean"]
proof_status = "full"
+++

**Theorem.** Let \(O\) be a [[?lean:New.DescentPair|descent pair]] with Weil data, \(e_0\in\mathbb{C}[\bar G_M]\) a central idempotent, \(w\ne\bar w\) a finite place off the level, \(A=H_w(X_*(w))\) the Hecke polynomial operator at the lift Hecke root, and \(Z\) a subspace of the forms on \(V\) with
\[
Z\subseteq\operatorname{im}(e_0)\cap\ker A .
\]
Let \(y\) be [[proofs/grh/onelift-comparison/false-lifts|orthogonal to the false lifts]] for \((e_0,Z^\perp)\). Then:

1. \(y\in Z+\ker(e_0)+\operatorname{im}(A)\) (this part needs no hypothesis on \(Z\));
2. for every \(\sigma\in\operatorname{Aut}(\mathbb{C})\), the [[linear-algebra/orthogonal-projection|orthogonal projection]] \(\operatorname{pr}_Zy\) (for \(\sigma=1\)) satisfies \(\lVert\operatorname{pr}_Zy\rVert_\sigma^2\le\lVert y\rVert_\sigma^2\).

## Proof

All facts quoted are in [[proofs/grh/onelift-comparison/hecke-polynomial-is-normal|the lemma on normality]].

1. Let \(S=Z+\ker e_0+\operatorname{im}A\); the space of forms is finite-dimensional, so \(S=S^{\perp\perp}\) and it suffices to show \(y\perp S^\perp\). Let \(u\in S^\perp\). Then \(u\in Z^\perp\); \(u\perp\ker e_0\), and since \(e_0\) is self-adjoint \((\ker e_0)^\perp=\operatorname{im}e_0\), so \(u\in\operatorname{im}e_0\); and \(u\perp\operatorname{im}A\), so \(u\in\ker A\). Thus \(u\in\operatorname{im}(e_0)\cap\ker A\cap Z^\perp=\mathrm{FL}_w(e_0,Z^\perp)\), and \(y\perp u\) by hypothesis.

2. Write \(y=z+x\) with \(z\in Z\), \(x=k+Av\), \(e_0k=0\). For any \(\tau\in\operatorname{Aut}(\mathbb{C})\) and \(z'\in Z\), write \(z'=e_0u\) with \(Az'=0\). Then \(\langle k,e_0u\rangle_\tau=\langle e_0k,u\rangle_\tau=0\) and \(\langle Av,z'\rangle_\tau=0\) because \(z'\in\ker A\). Hence \(\langle x,z'\rangle_\tau=0\) for all \(z'\in Z\) and all \(\tau\). With \(\tau=1\) this says \(y-z\perp Z\), so \(z=\operatorname{pr}_Zy\). With \(\tau=\sigma\), Pythagoras at \(\sigma\) gives \(\lVert z\rVert_\sigma^2\le\lVert z+x\rVert_\sigma^2=\lVert y\rVert_\sigma^2\).

## Remarks

The point is that orthogonality is tested only at \(\sigma=1\), but the decomposition \(y=z+x\) is orthogonal at every conjugate \(\sigma\), because it is cut out by operators (\(e_0\), \(A\)) that are self-adjoint or normal for every \(\langle\ ,\ \rangle_\sigma\).

## References

1. Lean: `New.DescentPair.mem_sup_ker_sup_range_of_isOrthogonalToFalseLifts`, `New.DescentPair.normSqAt_starProjection_le` in `src/New/OneLift/TestedForms.lean`.
