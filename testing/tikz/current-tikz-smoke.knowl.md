+++
id = "tikz/current-tikz-smoke"
title = "Current TikZ rendering smoke test"
kind = "knowl"
summary = "A development-only knowl used to verify the live TikZ rendering pipeline."
aliases = ["current-tikz-smoke"]
domains = ["testing"]
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

This development-only knowl checks the current end-to-end TikZ rendering path.
The triangle should commute: the diagonal arrow is the composite of the two
edge arrows.

```tikz
\node (A) at (0,0) {$A$};
\node (B) at (4,0) {$B$};
\node (C) at (4,-2.5) {$C$};
\draw[-{Stealth[length=3mm]}, thick] (A) -- node[above] {$f$} (B);
\draw[-{Stealth[length=3mm]}, thick] (B) -- node[right] {$g$} (C);
\draw[-{Stealth[length=3mm]}, thick] (A) -- node[below left] {$g\circ f$} (C);
```

Expected result: three labeled nodes, three directed arrows, and no displayed
TikZ source or error message.
