+++
id = "algebra-category-theory/tikz-lab-whiskering-coherence"
title = "TikZ lab: whiskering and coherence"
kind = "knowl"
summary = "A TikZ-heavy test knowl for natural transformations, whiskering, and coherence diagrams."
aliases = ["tikz-lab-whiskering-coherence", "TikZ lab: whiskering and coherence"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/tikz-lab-whiskering-coherence.md"
+++

Let \(\eta:F\Rightarrow G\) be a
[[algebra-category-theory/natural-transformation|natural transformation]] between
functors \(F,G:\mathcal C\to\mathcal D\), and let
\(H:\mathcal D\to\mathcal E\). Left whiskering produces
\[
H\eta:HF\Rightarrow HG,\qquad (H\eta)_X=H(\eta_X).
\]

```tikz-cd
H F X \arrow[r, "H F f"] \arrow[d, "H\eta_X"'] &
H F Y \arrow[d, "H\eta_Y"] \\
H G X \arrow[r, "H G f"'] &
H G Y
```

Right whiskering by \(K:\mathcal B\to\mathcal C\) produces
\[
\eta K:F K\Rightarrow G K,\qquad (\eta K)_B=\eta_{K B}.
\]
Both operations preserve vertical composition:
\[
H(\theta\circ\eta)=H\theta\circ H\eta,\qquad
(\theta\circ\eta)K=(\theta K)\circ(\eta K).
\]

```tikz
\node (C) at (0,0) {$\mathcal C$};
\node (D) at (3.4,0) {$\mathcal D$};
\node (E) at (6.8,0) {$\mathcal E$};
\node (C2) at (0,-2.45) {$\mathcal C$};
\node (E2) at (6.8,-2.45) {$\mathcal E$};
\coordinate (CDmid) at ($(C)!0.5!(D)$);

\draw[-{Stealth[length=3mm]}, bend left=20] (C) to (D);
\draw[-{Stealth[length=3mm]}, bend right=20] (C) to (D);
\node (Flabel) at ($(CDmid)+(0,0.58)$) {$F$};
\node (Glabel) at ($(CDmid)+(0,-0.58)$) {$G$};
\draw[-{Stealth[length=3mm]}, thick] (D) -- node[above] {$H$} (E);
\draw[-{Stealth[length=2.4mm]}, double distance=1.4pt, shorten <=1pt, shorten >=1pt]
  (Flabel.south) -- node[right] {$\eta$} (Glabel.north);

\draw[-{Stealth[length=3mm]}, bend left=18] (C2) to node[pos=0.5, above=5pt] {$HF$} (E2);
\draw[-{Stealth[length=3mm]}, bend right=18] (C2) to node[pos=0.5, below=5pt] {$HG$} (E2);
\draw[-{Stealth[length=2.4mm]}, double distance=1.4pt] (3.4,-1.95) -- node[right] {$H\eta$} (3.4,-2.95);
\draw[dashed, rounded corners] (-0.55,0.85) rectangle (7.35,-3.95);
```

The associator in a monoidal category is governed by Mac Lane's pentagon. In
formulas, the two composites
\[
(((A\otimes B)\otimes C)\otimes D)\longrightarrow
A\otimes(B\otimes(C\otimes D))
\]
agree.

\begin{tikzcd}[column sep=large,row sep=large]
(((A\otimes B)\otimes C)\otimes D)
  \arrow[r, "\alpha_{A\otimes B,C,D}"]
  \arrow[d, "\alpha_{A,B,C}\otimes 1_D"'] &
((A\otimes B)\otimes (C\otimes D))
  \arrow[r, "\alpha_{A,B,C\otimes D}"] &
A\otimes (B\otimes (C\otimes D)) \\
(A\otimes (B\otimes C))\otimes D
  \arrow[rr, "\alpha_{A,B\otimes C,D}"'] &&
A\otimes ((B\otimes C)\otimes D)
  \arrow[u, "1_A\otimes\alpha_{B,C,D}"']
\end{tikzcd}
