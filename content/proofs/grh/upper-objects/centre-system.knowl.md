+++
id = "proofs/grh/upper-objects/centre-system"
title = "Centre system and its parameters"
kind = "definition"
summary = "A stem and a finite set of centres with lengths and kinds (up or down) at one infinite place; for each subset B the parameter lambda_B made of the stem and the blocks of B, with signs counted by the centres outside B."
aliases = ["centre system", "separated centre system", "parameter of a centre system"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CentreSystem", "New.CentreSystem.block", "New.CentreSystem.entries", "New.CentreSystem.rank", "New.CentreSystem.lowering", "New.CentreSystem.CountsFor", "New.CentreSystem.sign", "New.CentreSystem.IsSeparated", "New.CentreSystem.IsParam", "New.CentreSystem.IsSeparated.subset", "New.CentreSystem.IsParam.neg_signs"]
lean_files = ["src/New/UpperBound/Objects/InsertBlock.lean"]
+++

For \(d\ge0\) and \(e\in\mathbb Z\) let \(e+[d]=\{e+\tfrac{d-1}2,e+\tfrac{d-3}2,\dots,e+\tfrac{1-d}2\}\) (the *block* of length \(d\) centred at \(e\)); all entries below are half-integers and the Lean text stores their doubles.

**Definition.** A **centre system** \(X\) (at one infinite place) consists of

* an index set \(I\) of *labels* and a distinguished finite subset \(C\subseteq I\), the *centres*; and for each label \(c\in I\): a *value* \(c\in\mathbb Z\) (written like the centre), a *length* \(l_c\in\mathbb N\) and a *kind*, **up** or **down**;
* a finite set \(S\subset\tfrac12\mathbb Z\), the *stem*.

For a finite set of labels \(B\subseteq I\) (in the results on gaps and insertions \(B\subseteq C\) is assumed; the definitions do not need it) define

* the set of entries \(\lambda^+_B=S\cup\bigcup_{c\in B}(c+[l_c])\);
* the rank \(n_B=\lvert S\rvert+\sum_{c\in B}l_c\);
* the lowering \(\delta_B=\tfrac12\) if \(\lvert S\rvert\) and \(\lvert B\rvert\) are both odd, and \(\delta_B=0\) otherwise;
* a centre \(c\) **counts for** an entry \(y\) if \(c\) is down and \(y<c\), or \(c\) is up and \(c<y\);
* the sign \(\operatorname{sgn}_B(y)=(-1)^{\#\{c\in C\setminus B\,:\,c\text{ counts for }y\}}\).

The system is **separated with bound \(h\)** (\(h\in\mathbb N\)) if

1. \(l_c\equiv\lvert S\rvert\pmod 2\) for all \(c\in C\);
2. \(S\subset\tfrac12+\mathbb Z\) if \(\lvert S\rvert\) is even and \(S\subset\mathbb Z\) if \(\lvert S\rvert\) is odd;
3. \(\lvert y-c\rvert\ge(h+l_c)/2\) for all \(c\in C\), \(y\in S\);
4. \(\lvert y-c\rvert\ge(h+l_c)/2\) for all \(c\ne c'\) in \(C\) and \(y\in c'+[l_{c'}]\).

Let \(V\) be a space with a finite coordinate set \(n\) and signs \(s\colon n\to\{\pm1\}\), and \(\lambda\colon n\to\tfrac12\mathbb Z\) (a [[?lean:New.HCParam|Harish-Chandra parameter]] on \(V\), stored doubled). For a finite \(B\subseteq I\) and \(\sigma\in\{\pm1\}\), **\(\lambda\) is the parameter \(\lambda_B\) with common sign \(\sigma\)** if

* \(\lvert n\rvert=n_B\);
* \(\{\lambda_x+\delta_B: x\in n\}=\lambda^+_B\);
* \(s_x=\sigma\cdot\operatorname{sgn}_B(\lambda_x+\delta_B)\) for all \(x\in n\).

## Remarks

Passing to a subset of the centres preserves separation. If \(\lambda\) is \(\lambda_B\) with common sign \(\sigma\) on the space with signs \(s\), it is \(\lambda_B\) with common sign \(-\sigma\) on the opposite space (signs \(-s\)). The parameters of all chains and grids of spaces of the proof are built from centre systems.

## References

1. Lean: `New.CentreSystem`, `New.CentreSystem.IsSeparated`, `New.CentreSystem.IsParam` in `src/New/UpperBound/Objects/InsertBlock.lean`.
