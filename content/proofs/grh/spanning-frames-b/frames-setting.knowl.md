+++
id = "proofs/grh/spanning-frames-b/frames-setting"
title = "Standing notation for pairs of frames at one place"
kind = "notation"
summary = "The place, the split hermitian form, the place datum, the gauge, heads, cut Bessel functions and the quantities attached to them, as used in the second half of the frames estimates."
aliases = ["frames setting", "notation for the frames estimates"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = []
lean_files = ["src/New/Spanning/Frames/Shells.lean"]
+++

**Standing notation (pairs of frames at one place).** Throughout the frames estimates the following objects are fixed; all of them are defined in the first half of the area and are only named here.

* \(A\) is a [[?lean:New.Floors.Place|place]]: a locally compact commutative topological ring with a continuous involution \(x\mapsto\bar x\), a [[harmonic-analysis/haar-measure|Haar measure]] (its volume), a modulus \(\lvert\cdot\rvert_A\colon A\to[0,\infty]\), a unitary additive character \(\psi\), a skew unit \(\delta\), and a constant \(c_A\in[0,\infty]\) (the *kernel bound* of Plancherel's formula). In the applications \(A=\mathbb{C}\) with complex conjugation, or \(A\) is the product of the rings of integers localised at a finite set of finite places.
* A [[?lean:New.Shape|shape]] fixes \(\varrho\ge 0\), a finite index set \(\kappa\) of cardinality \(k\) and \(n=\varrho+1\). The space \(V\) has the basis \(e_0,\dots,e_{\varrho-1}\), \(x_i\ (i\in\kappa)\), \(z\), \(e^*_0,\dots,e^*_{\varrho-1}\); the hermitian form is the [[?lean:New.Shape.Form.splitGram|split Gram matrix]] of a hermitian matrix \(T\) on the middle block \(\langle x_i,z\rangle\): the \(e_a,e^*_a\) are \(\varrho\) hyperbolic pairs orthogonal to the middle block. It is assumed hermitian and invertible, and \(G\) denotes its [[?lean:New.Shape.Form.G|unitary group]] over \(A\). The *frame* is \((e_0,\dots,e_{\varrho-1},z)\).
* \(G^{(l)}\) is the [[?lean:New.FloorGroups.floorGroup|floor group]]: the isometries fixing the basis vectors of floor \(<l\) (both \(e_a\) and \(e_a^*\) have floor \(a\), \(z\) has floor \(\varrho\), the \(x_i\) have floor \(\varrho+1\)); \(H=G^{(\varrho+1)}\). \(R^{(l)}\) is the [[?lean:New.Shape.Form.partialUnitriangularGroup|partial unitriangular group]] and \(U\) the [[?lean:New.Shape.Form.besselU|Bessel unipotent group]].
* \(F\) is a [[?lean:New.Floors.PlaceData|place datum]]: a unit \(M\) (the *level*), a compact set \(K\subset G\) (the *box*), a measurable set of *positions* in \(G\), a set of *close pairs* of vectors, an adapted basis with \(m\) further hyperbolic pairs and an orthonormal part indexed by \(\iota\), and floor measures \(\theta_l\) whose convolution with the Heisenberg measures is the [[?lean:New.Floors.PlaceData.groupMeasure|group measure]] \(\mathsf{M}\) on \(G\). The number \(s\) is the [[?lean:New.Floors.PlaceData.volumeExponent|volume exponent]] of \(F\), and \(X'\) denotes the span of the free orthonormal vectors, of rank \(\lvert\iota\rvert-2(2m+2)\).
* \(\Gamma\) is a [[?lean:New.Floors.Gauge|gauge]] for \(F\): a filtration of \(A\) by sets of numbers "of size \(i\)" together with a finite constant \(\Lambda=\Lambda_\Gamma\ge 2\), the *loss*, whose powers bound moduli and volumes. Its [[?lean:New.Floors.Gauge.positionsOfSize|position ball]] \(\mathcal{P}(\Gamma)\) is the set of positions \(x\) for which all entries of \((x-1)/M\) have size \(1\).
* A sequence of units \(p=(p_0,p_1,\dots)\) of \(A\) is a [[?lean:New.Floors.Size.IsHead|head]] of length \(j\) for \(\Gamma\) if the inverses of the products \(p_0\cdots p_{l-1}\), \(l\le j\), have size \(1\). For two sequences \(p,q\), \(\kappa_j(p,q)\) is the [[?lean:New.Floors.PlaceData.headDensity|head density]] \(\prod_{a<j}\lvert p_aq_a\rvert_A^{d_a/2}\), \(d_a=k+1+2(\varrho-a-1)\).
* \(W\colon G\to\mathbb{C}^I\) (\(I\) finite) is a [[?lean:New.Floors.PlaceData.IsCut|cut Bessel function]] for \(F\): bounded, measurable, \(W(ux)=\psi(M^{-1}\sigma_0(u))W(x)\) for \(u\in U\), where \(\sigma_0(u)\) is the sum of the superdiagonal entries of the frame block, and \(W(x)=0\) unless \(Ux\) meets \(K\).
* For a position \(x\): \(\mathsf{N}_j(p,q;W;x)\) is the [[?lean:New.Floors.PlaceData.formMajorant|form majorant]], \(\mathsf{P}^{\Gamma}_j(p,q;W;x)\) the [[?lean:New.Floors.Gauge.weightedSquareProduct|weighted square product]], \(\lVert W\rVert_{\mathrm{corr}}^2\) the [[?lean:New.Floors.PlaceData.pairingNormSq|squared norm of the correlation]] of \(W\), and \(\mathrm{depth}_a(y,x)\) the [[?lean:New.Floors.PlaceData.depth|depth]] of \(e_a\) at the points \(y\), \(yx\).
* The statement "the mass of floor \(j\) is at most \(V\)" means the [[?lean:New.Floors.PlaceData.FloorMassLe|floor mass bound]] with the constant function \(1\): for every \(g\in G\), \(\theta_j\{\sigma:\ \sigma g\text{ is near at }j+1\}\le V\), where a point \(g\) is [[?lean:New.Floors.PlaceData.IsNear|near at \(l\)]] if \(R^{(l)}g\) meets \(K\).

All integrals of functions with values in \([0,\infty]\) are [[measure-theory/lebesgue-integral-nonnegative|Lebesgue integrals of nonnegative functions]] and may be infinite; inequalities are in \([0,\infty]\).

## References

1. Lean: heads of `src/New/Spanning/Frames/Lengths.lean`, `Levels.lean`, `Correlations.lean`, `Densities.lean` (definitions), and `src/New/Spanning/Frames/Shells.lean`.
