+++
id = "proofs/grh/spanning-frames-b/shell"
title = "Shell of positions"
kind = "definition"
summary = "A set of positions of a given height that is covered by few position balls and on which a large height forces a deep vector."
aliases = ["shell", "shell of height h"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.Gauge.IsShell", "New.Floors.Gauge.IsShell.subset_positions"]
lean_files = ["src/New/Spanning/Frames/Shells.lean"]
+++

In the [[proofs/grh/spanning-frames-b/frames-setting|standing notation]], let \(\Gamma\) be a gauge for the place datum \(F\), with loss \(\Lambda\), let \(j\ge 0\), let \(p,q\) be sequences of units of \(A\), and let \(W\colon G\to\mathbb{C}^I\). A set \(S\subseteq G\) is a **shell of height \(h\)** for \((\Gamma,j,p,q,W)\), where \(h\in[0,\infty]\), if

1. \(1\le h<\infty\);
2. (*few balls*) there is a finite set \(\mathcal{G}\) of gauges for \(F\) with
\[
\#\mathcal{G}\le 2h^{9n},\qquad S\subseteq\bigcup_{\Gamma'\in\mathcal{G}}\mathcal{P}(\Gamma'),\qquad \Lambda_{\Gamma'}\le\Lambda h^2\ \text{ for all }\Gamma'\in\mathcal{G},
\]
where \(\mathcal{P}(\Gamma')\) is the [[?lean:New.Floors.Gauge.positionsOfSize|position ball]] of \(\Gamma'\);
3. (*far means deep*) for every \(x\in S\) and every \(\sigma\in[0,1)\) with
\[
\Lambda^{1200n^2}\le\sigma^{400n^2}\,h ,
\]
the position \(x\) [[?lean:New.Floors.PlaceData.HasDeepVector|has a deep vector]] of depth \(\sigma^{-2}\) after the head: every point \(y\in G\) that is [[?lean:New.Floors.PlaceData.IsActive|active]] at \(x\) (that is, \(\langle W(y),W(yx)\rangle\ne0\), and \(w_p^{-1}y\), \(w_q^{-1}yx\) are near at \(j\), with \(w_p,w_q\) the Weyl elements of the heads) has an index \(a\) with \(j\le a<\varrho\) and \(\mathrm{depth}_a(y,x)\ge\sigma^{-2}\).

## Properties

Every shell is contained in the set of positions of \(F\), because each position ball is, by definition, a set of positions.

## References

1. Lean: `New.Floors.Gauge.IsShell`, `New.Floors.Gauge.IsShell.subset_positions` in `src/New/Spanning/Frames/Shells.lean`.
