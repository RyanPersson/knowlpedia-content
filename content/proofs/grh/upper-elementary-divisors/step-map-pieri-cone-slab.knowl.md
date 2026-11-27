+++
id = "proofs/grh/upper-elementary-divisors/step-map-pieri-cone-slab"
title = "Step map, Pieri cone and degree slab"
kind = "definition"
summary = "The linear map of signed gaps between consecutive letters, the cone cut out by Pieri's interlacing inequalities, and the slab of nonnegative vectors with degrees in unit intervals."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.permStep", "New.degreeSlab", "New.pieriCone", "New.positiveStepSet", "New.detOneSubPerm", "New.isBounded_degreeSlab"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/PieriCone.lean"]
+++

Let \(k\ge0\), let \(\mathcal{T}\) be a finite cyclic set of **letters** (\(\mathbb{Z}/N\) with \(N\ge1\), or \(\{0,\dots,m\}\) with addition modulo \(m+1\)), let \(v\colon\mathcal{T}\to\{+,-\}\) be a choice of signs and \(P\in\mathbb{R}\). Vectors are real functions \(\nu\) on pairs \((b,j)\), \(0\le b<k\), \(j\in\mathcal{T}\); the **block** \(j\) of \(\nu\) is \((\nu(b,j))_b\).

- **Step map.** For a family \(\sigma=(\sigma_j)_{j\in\mathcal{T}}\) of permutations of \(\{0,\dots,k-1\}\), the linear map \(\mathrm{St}_\sigma=\mathrm{St}_{v,P,\sigma}\) on \(\mathbb{R}^{k\times\mathcal{T}}\) is
\[
(\mathrm{St}_\sigma\nu)(b,j)=v_j\cdot\bigl(P\,\nu(b,j+1)-\nu(\sigma_j(b),j)\bigr).
\]
Write \(\mathrm{St}=\mathrm{St}_1\) for trivial permutations; the entries of \(\mathrm{St}\,\nu\) are the **steps** of \(\nu\).
- **Degree slab.** For \(D\colon\mathcal{T}\to\mathbb{R}\): \(\mathrm{Slab}_k(D)=\{\beta\ge0:\ D_j-1\le\sum_b\beta(b,j)\le D_j\text{ for all }j\}\). It is bounded (each entry lies in \([0,D_j]\)).
- **Pieri cone.** \(\mathcal{C}_{v,P}\) is the set of \(\nu\) such that for all \(j\) and all \(b\) with \(b+1<k\):
\[
P\,\nu(b+1,j+1)\le\nu(b,j)\ \text{ if }v_j=+,\qquad \nu(b+1,j)\le P\,\nu(b,j+1)\ \text{ if }v_j=-.
\]
(In the formal source this is written as \((\mathrm{St}\,\nu)(b^{*},j)\le\nu(b,j)-\nu(b+1,j)\) with \(b^{*}=b+1\) for \(v_j=+\) and \(b^{*}=b\) for \(v_j=-\), which is the same.)
- **Positive step sets.** For families \(\sigma,\tau\) of permutations and a set \(Y\): \(\mathrm{Pos}_D(\sigma,\tau,Y)\) is the set of \(\nu\) such that \(\sum_b(\mathrm{St}\,\nu)(b,j)\in[D_j-1,D_j]\) for all \(j\), and \(\mathrm{St}_\sigma(\nu^{\tau})\) has all entries \(>0\) and lies in \(Y\), where \(\nu^{\tau}(b,j)=\nu(\tau_j(b),j)\).
- For real \(q\ne0\) and a permutation \(\pi\) of \(\{0,\dots,k-1\}\): \(\Delta_q(\pi)=\det(1-q^{-1}\Pi_\pi)\), with \(\Pi_\pi\) the map \(x\mapsto x\circ\pi\) on \(\mathbb{R}^{k}\).

## Remarks

Pieri's inequalities are one half of the interlacing inequalities between the block \(j\) of \(\nu\) and \(P\) times the block \(j+1\); together with positivity of the steps they give full interlacing (see [[proofs/grh/upper-elementary-divisors/signed-count-of-positive-steps|the signed count]]). In the application the sign \(v_j\) is \(+\) on even letters.

## References

1. Lean: `New.permStep`, `New.degreeSlab`, `New.pieriCone`, `New.positiveStepSet`, `New.detOneSubPerm`, `New.isBounded_degreeSlab` in `src/New/UpperBound/ElementaryDivisors/PieriCone.lean`.
