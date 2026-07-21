+++
id = "algebra-category-theory/tikz-lab-adjunction-naturality"
title = "TikZ lab: adjunction naturality"
kind = "knowl"
summary = "A diagram stress test for adjunction bijections, units, counits, and LaTeX formulas."
aliases = ["tikz-lab-adjunction-naturality", "TikZ lab: adjunction naturality"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/tikz-lab-adjunction-naturality.md"
+++

For an [[algebra-category-theory/adjoint-functors|adjunction]] \(F\dashv G\), the
hom-set bijection
\[
\Phi_{C,D}:\mathcal D(F C,D)\longrightarrow \mathcal C(C,G D)
\]
is natural in both variables. If \(u:C'\to C\) and \(v:D\to D'\), naturality is
encoded by the square
\[
\Phi_{C',D'}(v\circ f\circ F u)=Gv\circ \Phi_{C,D}(f)\circ u.
\]

```tikz-cd
\mathcal D(F C,D) \arrow[r, "\Phi_{C,D}"] \arrow[d, "{v\circ -\circ F u}"'] &
\mathcal C(C,G D) \arrow[d, "{Gv\circ -\circ u}"] \\
\mathcal D(F C',D') \arrow[r, "\Phi_{C',D'}"'] &
\mathcal C(C',G D')
```

The unit and counit recover the bijection by
\[
\Phi_{C,D}(f)=Gf\circ\eta_C,\qquad
\Phi_{C,D}^{-1}(h)=\varepsilon_D\circ Fh.
\]

```tikz-cd
C \arrow[r, "\eta_C"] \arrow[dr, "h"'] & G F C \arrow[d, "G f"] \\
& G D
```

```tikz-cd
F C \arrow[r, "Fh"] \arrow[dr, "f"'] & F G D \arrow[d, "\varepsilon_D"] \\
& D
```

The following raw TikZ picture exercises curved arrows and a central formula
inside a framed diagram.

```tikz
\node (L) at (0,0) {$\mathcal D(F C,D)$};
\node (R) at (7.0,0) {$\mathcal C(C,G D)$};

\draw[-{Stealth[length=3mm]}, thick, bend left=24] (L) to node[above] {$\Phi$} (R);
\draw[-{Stealth[length=3mm]}, thick, bend left=24] (R) to node[below] {$\Phi^{-1}$} (L);

\node[align=center] at (3.5,1.75) {$\Phi(f)=Gf\circ\eta_C$};
\node[align=center] at (3.5,-1.75) {$\Phi^{-1}(h)=\varepsilon_D\circ Fh$};
\node[align=center] at (3.5,0) {$f\leftrightarrow h$};
\draw[rounded corners] (-1.0,-2.35) rectangle (8.0,2.35);
```
