+++
id = "proofs/grh/spanning-core/bessel-period-group-and-average"
title = "The group of the Bessel period and the Bessel average"
kind = "construction"
summary = "The group R = U x H at a real place with its Haar measure du dh, and the integral over R of a discrete series coefficient that defines the Bessel function."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Shape.besselGraph", "New.Shape.besselGraphChart", "New.Shape.besselGraphMeasure", "New.Shape.besselGraphMeasure_isMulRightInvariant", "New.Shape.besselGraphMeasure_isMulLeftInvariant", "New.Shape.embedH_conj_mem_besselU_iff", "New.Shape.mem_besselGraph_iff_mul_inv_mem", "New.DiscreteSeries.besselGraph_fst_mem_besselS", "New.DiscreteSeries.besselIntegrand", "New.DiscreteSeries.besselAverage"]
lean_files = ["src/New/Spanning/Bessel/Average.lean"]
+++

Let \(G_1\) be the real unitary group of a [[?lean:New.Shape|shape]] (see [[proofs/grh/spanning-core/bessel-length|Bessel length]]), \(\mathsf U\) the Bessel unipotent group with Haar measure \(du\), and \(U(\kappa)\) the unitary group of \(X_0\), embedded in \(G_1\) as \(H\) and carrying its Haar measure \(dh\) ([[?lean:New.haarU|`haarU`]]). \(H\) normalises \(\mathsf U\).

1. The **group of the Bessel period** is \(R=\mathsf U\rtimes H\), realised as the closed subgroup of \(G_1\times U(\kappa)\) of the pairs \((g,h)\) with \(h^{-1}g\in\mathsf U\) (equivalently \(gh^{-1}\in\mathsf U\)). The map \((u,h)\mapsto(hu,h)\) is a homeomorphism \(\mathsf U\times U(\kappa)\to R\).
2. The **measure \(du\,dh\) on \(R\)** is the image of \(du\otimes dh\) under this map. It is a left and right invariant Haar measure on \(R\).
3. For \((g,h)\in R\), \(g\) lies in the Bessel subgroup \(S\).
4. Let \(\varepsilon\) be signs with a [[?lean:New.SignFrame|sign frame]] for the form of \(G_1\), \(l\) a doubled Harish-Chandra parameter for \(\varepsilon\) with [[?lean:New.HCParam.dsCoeffInFrame|discrete series coefficient \(c_\lambda\) read in that frame]], \(\mathrm{rep}\colon U(\kappa)\to U(I)\) a unitary representation, \(x\in G_1\) and \(v\in\mathbb{C}^I\). The **Bessel average** is the function of \(y\in G_1\)
\[
\mathcal W_{x,v}(y)=\int_Rc_\lambda\bigl(x^{-1}g\,y\bigr)\;\psi(g)^{-1}\,\mathrm{rep}(h)^{-1}v\;\,du\,dh\qquad(s=(g,h)\in R),
\]
where \(\psi(g)^{-1}=e^{-(\sigma-\bar\sigma)}\) with \(\sigma=\sigma(g)\) the sum of the entries of \(g\) just above the diagonal on the frame ([[?lean:New.simpleRootSum|`simpleRootSum`]]). The integral is the Bochner integral, with the convention that it is \(0\) if the integrand is not integrable.

## Proof

*Invariance of \(du\,dh\).* Right multiplication by \((h'u',h')\) sends the point with coordinates \((u,h)\) to that with coordinates \((h'^{-1}uh'\,u',\,hh')\); conjugation by \(h'^{-1}\in S\) preserves \(du\) (library statement `New.RealPlace.measurePreserving_conj_bessel`: conjugation by an element of \(S\) preserves every Haar measure of a subgroup cut out by entry conditions and normalised by \(S\)), and right translations preserve \(du\) and \(dh\). Left multiplication by \((h'u',h')\) sends \((u,h)\) to \(((h^{-1}u'h)\,u,\,h'h)\): over each \(h\) a left translation of \(\mathsf U\), combined with a left translation of \(U(\kappa)\). The measure is positive on open sets and finite on compact sets as the image of such a measure under a homeomorphism.

(3) \(g=(gh^{-1})h\) with \(gh^{-1}\in\mathsf U\). \(\blacksquare\)

## References

1. Lean: `New.Shape.besselGraph`, `New.Shape.besselGraphMeasure`, `New.DiscreteSeries.besselIntegrand`, `New.DiscreteSeries.besselAverage` in `src/New/Spanning/Bessel/Average.lean`.
