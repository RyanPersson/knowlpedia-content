---
title: "TikZ diagram lab: category theory lecture notes"
description: "A diagram-heavy category theory note for practicing TikZ, tikz-cd, and compiler rendering behavior."
---

These notes are a scratch space for category-theory diagrams. The mathematical
content is intentionally compact; the main point is to exercise the renderer on
commutative diagrams, universal properties, adjunction triangles, and string-like
composition pictures.

## 1. A category as composable arrows

A category has objects, morphisms, identities, and associative composition. In a
small local picture, the equality \(h = g \circ f\) is represented by the
commutative triangle:

```tikz-cd
A \arrow[r, "f"] \arrow[dr, "h"'] & B \arrow[d, "g"] \\
& C
```

The same idea in raw TikZ gives more control over placement and labels:

```tikz
\node (A) at (0,0) {$A$};
\node (B) at (3,0) {$B$};
\node (C) at (3,-2) {$C$};
\draw[-{Stealth[length=3mm]}] (A) -- node[above] {$f$} (B);
\draw[-{Stealth[length=3mm]}] (B) -- node[right] {$g$} (C);
\draw[-{Stealth[length=3mm]}] (A) -- node[below left] {$g\circ f$} (C);
```

## 2. Functors preserve shape

A functor \(F : \mathcal{C} \to \mathcal{D}\) sends objects to objects and
morphisms to morphisms while preserving identity arrows and composition.

```tikz-cd
A \arrow[r, "f"] \arrow[d, mapsto] & B \arrow[d, mapsto] \\
F A \arrow[r, "Ff"'] & F B
```

Functoriality says the following two routes in \(\mathcal{D}\) agree whenever
the upper route agrees in \(\mathcal{C}\):

```tikz-cd
F A \arrow[r, "Ff"] \arrow[dr, "F(g\circ f)"'] & F B \arrow[d, "Fg"] \\
& F C
```

## 3. Natural transformations as squares

For functors \(F,G : \mathcal{C}\to\mathcal{D}\), a natural transformation
\(\eta : F \Rightarrow G\) assigns a component \(\eta_A : F A \to G A\) to
each object \(A\). Naturality means every morphism \(f : A\to B\) gives a
commutative square.

```tikz-cd
F A \arrow[r, "Ff"] \arrow[d, "\eta_A"'] & F B \arrow[d, "\eta_B"] \\
G A \arrow[r, "Gf"'] & G B
```

Here is the same square with visual emphasis on the two parallel paths:

```tikz
\node (FA) at (0,0) {$F A$};
\node (FB) at (3.2,0) {$F B$};
\node (GA) at (0,-2.1) {$G A$};
\node (GB) at (3.2,-2.1) {$G B$};
\draw[-{Stealth[length=3mm]}, thick] (FA) -- node[above] {$Ff$} (FB);
\draw[-{Stealth[length=3mm]}, thick] (FA) -- node[left] {$\eta_A$} (GA);
\draw[-{Stealth[length=3mm]}] (FB) -- node[right] {$\eta_B$} (GB);
\draw[-{Stealth[length=3mm]}] (GA) -- node[below] {$Gf$} (GB);
\draw[dashed, rounded corners] (-0.6,0.45) rectangle (3.8,-2.55);
\node at (1.6,-1.05) {$\eta_B\circ Ff = Gf\circ \eta_A$};
```

## 4. Pullbacks

A pullback of \(f : X\to Z\) and \(g : Y\to Z\) is an object \(P\) equipped
with projections such that every compatible cone factors uniquely through \(P\).

```tikz-cd
T \arrow[ddr, bend right=18, "u"'] \arrow[drr, bend left=18, "v"] \arrow[dr, dashed, "\exists!" description] & & \\
& P \arrow[r, "p_2"] \arrow[d, "p_1"'] & Y \arrow[d, "g"] \\
& X \arrow[r, "f"'] & Z
```

The outer equations are \(f u = g v\), and the dashed arrow is the unique map
whose composites with \(p_1,p_2\) are \(u,v\).

## 5. Adjunctions

An adjunction \(F \dashv G\) can be recognized by a natural bijection
\[
  \mathcal{D}(F C, D) \cong \mathcal{C}(C, G D).
\]
The unit and counit satisfy the triangle identities:

```tikz-cd
F C \arrow[r, "F\eta_C"] \arrow[dr, equal] & F G F C \arrow[d, "\varepsilon_{F C}"] \\
& F C
```

```tikz-cd
G D \arrow[r, "\eta_{G D}"] \arrow[dr, equal] & G F G D \arrow[d, "G\varepsilon_D"] \\
& G D
```

The hom-set bijection is often the most useful diagram for computation:

```tikz
\node (left) at (0,0) {$\mathcal{D}(F C,D)$};
\node (right) at (5.1,0) {$\mathcal{C}(C,G D)$};
\draw[-{Stealth[length=3mm]}, bend left=18] (left) to node[above] {$\Phi_{C,D}$} (right);
\draw[-{Stealth[length=3mm]}, bend left=18] (right) to node[below] {$\Phi^{-1}_{C,D}$} (left);
\node[align=center] at (2.55,-2.05) {$\Phi(f)=Gf\circ\eta_C$\\[0.35em]$\Phi^{-1}(h)=\varepsilon_D\circ Fh$};
```

## 6. Yoneda shape

The Yoneda embedding sends an object \(A\) to the representable functor
\(\mathcal{C}(-,A)\). A morphism \(u:A\to B\) induces a natural transformation
by postcomposition.

```tikz-cd
\mathcal{C}(X,A) \arrow[r, "{u\circ -}"] \arrow[d, "{-\circ f}"'] &
\mathcal{C}(X,B) \arrow[d, "{-\circ f}"] \\
\mathcal{C}(Y,A) \arrow[r, "{u\circ -}"'] &
\mathcal{C}(Y,B)
```

One way to remember the lemma is that every natural transformation out of a
representable functor is determined by the image of the identity:

```tikz
\node (Nat) at (0,0) {$\operatorname{Nat}(\mathcal{C}(-,A),F)$};
\node (FA) at (6.2,0) {$F A$};
\draw[-{Stealth[length=3mm]}, thick] (Nat) -- node[above] {$\alpha \mapsto \alpha_A(1_A)$} (FA);
\draw[-{Stealth[length=3mm]}, thick] (FA) to[bend left=35] node[below] {$x\mapsto (f\mapsto Ff(x))$} (Nat);
```
