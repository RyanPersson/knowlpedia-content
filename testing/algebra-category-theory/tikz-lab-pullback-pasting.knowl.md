+++
id = "algebra-category-theory/tikz-lab-pullback-pasting"
title = "TikZ lab: pullback pasting"
kind = "knowl"
summary = "A TikZ-heavy test knowl for pullback pasting diagrams and surrounding LaTeX."
aliases = ["tikz-lab-pullback-pasting", "TikZ lab: pullback pasting"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/tikz-lab-pullback-pasting.md"
+++

Let
\[
\begin{aligned}
P &= X\times_Z Y,\\
Q &= Y\times_V W.
\end{aligned}
\]
The pasting principle says that if the right square and the outer rectangle are
[[algebra-category-theory/pullback|pullbacks]], then the left square is a pullback.
Conversely, if the left and right squares are pullbacks, then the outer rectangle
is a pullback.

```tikz-cd
P \arrow[r, "q"] \arrow[d, "p"'] & Y \arrow[r, "r"] \arrow[d, "g"'] & W \arrow[d, "h"] \\
X \arrow[r, "f"'] & Z \arrow[r, "k"'] & V
```

The universal comparison map is the unique arrow forced by the equations
\[
p\circ u = a,\qquad q\circ u=b,\qquad r\circ b=c.
\]

```tikz
\node (T) at (-1.2,1.25) {$T$};
\node (P) at (1.2,0) {$P$};
\node (Y) at (3.8,0) {$Y$};
\node (W) at (6.4,0) {$W$};
\node (X) at (1.2,-2.0) {$X$};
\node (Z) at (3.8,-2.0) {$Z$};
\node (V) at (6.4,-2.0) {$V$};

\draw[-{Stealth[length=3mm]}, dashed] (T) -- (P);
\node at (-0.35,0.38) {$u$};
\draw[-{Stealth[length=3mm]}, bend right=18] (T) to node[left] {$a$} (X);
\draw[-{Stealth[length=3mm]}, bend left=10] (T) to node[above] {$b$} (Y);
\draw[-{Stealth[length=3mm]}, bend left=18] (T) to node[above] {$c$} (W);

\draw[-{Stealth[length=3mm]}] (P) -- node[above] {$q$} (Y);
\draw[-{Stealth[length=3mm]}] (Y) -- node[above] {$r$} (W);
\draw[-{Stealth[length=3mm]}] (P) -- node[left] {$p$} (X);
\draw[-{Stealth[length=3mm]}] (Y) -- node[right] {$g$} (Z);
\draw[-{Stealth[length=3mm]}] (W) -- node[right] {$h$} (V);
\draw[-{Stealth[length=3mm]}] (X) -- node[below] {$f$} (Z);
\draw[-{Stealth[length=3mm]}] (Z) -- node[below] {$k$} (V);
```

The same shape as a raw TikZ picture is useful for checking labelled regions,
line weights, and the way dark mode treats non-matrix diagrams.

```tikz
\node (P) at (0,0) {$P$};
\node (Y) at (2.7,0) {$Y$};
\node (W) at (5.4,0) {$W$};
\node (X) at (0,-2.0) {$X$};
\node (Z) at (2.7,-2.0) {$Z$};
\node (V) at (5.4,-2.0) {$V$};

\draw[-{Stealth[length=3mm]}, thick] (P) -- node[above] {$q$} (Y);
\draw[-{Stealth[length=3mm]}, thick] (Y) -- node[above] {$r$} (W);
\draw[-{Stealth[length=3mm]}] (P) -- node[left] {$p$} (X);
\draw[-{Stealth[length=3mm]}] (Y) -- node[right] {$g$} (Z);
\draw[-{Stealth[length=3mm]}] (W) -- node[right] {$h$} (V);
\draw[-{Stealth[length=3mm]}] (X) -- node[below] {$f$} (Z);
\draw[-{Stealth[length=3mm]}] (Z) -- node[below] {$k$} (V);

\draw[dashed, rounded corners] (-0.55,0.45) rectangle (3.25,-2.45);
\draw[dashed, rounded corners] (2.15,0.45) rectangle (5.95,-2.45);
\node[align=center] at (1.35,-1.0) {left\\square};
\node[align=center] at (4.05,-1.0) {right\\square};
```
