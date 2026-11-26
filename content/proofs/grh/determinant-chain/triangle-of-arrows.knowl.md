+++
id = "proofs/grh/determinant-chain/triangle-of-arrows"
title = "Triangle of arrows"
kind = "definition"
summary = "An abstract triangular diagram of inner product spaces with arrows along rows and down to the next row, whose squares commute up to scalars."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Exchange.IsTriangle", "New.Exchange.SquareCommutes", "New.Exchange.weightedChain"]
lean_files = ["src/New/Determinant/Chain/TriangleNorms.lean"]
+++

Fix a set \(I\) of parameters, an integer \(m\ge0\), complex [[?c:Inner product space|inner product spaces]] \(V\) and \(F_{i,n}\) (\(i,n\ge0\)), with inner products \(\langle\cdot,\cdot\rangle\) conjugate-linear in the first variable, and for each \(t\in I\)

- linear maps \(a_{t,i,n}\colon F_{i,n}\to F_{i,n+1}\) (arrows along row \(i\)),
- linear maps \(d_{t,i,n}\colon F_{i,n+1}\to F_{i+1,n}\) (arrows down to the next row),
- natural numbers \(w_t(n)\) (weights),

and linear isometries \(j_i\colon V\to F_{i,0}\) not depending on \(t\).

For a function \(\beta\colon I\to\mathbb{C}\), the **square at \((i,n)\) commutes up to \(\beta\)** if for all \(t\) and all \(y\in F_{i,n+1}\)
\[
w_t(n)\cdot a_{t,i+1,n}\,d_{t,i,n}\,y\;=\;\frac{w_t(n+2)}{\overline{\beta(t)}}\cdot d_{t,i,n+1}\,a_{t,i,n+1}\,y ,
\]
where the quotient is read as \(0\) if \(\beta(t)=0\).

These data form a **triangle of size \(m\)** if

1. for all \(i,n\) with \(i+n+2\le m\) the square at \((i,n)\) commutes up to some \(\beta\);
2. for \(i<m\), all \(t\), \(y\in V\) and \(z\in F_{i,1}\): \(\langle z,\,a_{t,i,0}\,j_i y\rangle=\langle d_{t,i,0}\,z,\ j_{i+1}y\rangle\);
3. for \(i<m\), all \(t\) and \(y\in V\): \(d_{t,i,0}\,a_{t,i,0}\,j_iy\in j_{i+1}(V)\);
4. for \(i<m\), all \(t\) and \(y\in V\): if \(d_{t,i,0}\,a_{t,i,0}\,j_iy=0\) then \(y=0\).

The **weighted \(n\)-chain of row \(i\)** is the composite
\[
X_{t,i,n}=\big(w_t(n-1)\,a_{t,i,n-1}\big)\circ\dots\circ\big(w_t(0)\,a_{t,i,0}\big)\colon F_{i,0}\to F_{i,n},\qquad X_{t,i,0}=\mathrm{id}.
\]

## Remarks

In the application ([[proofs/grh/determinant-chain/triangle-of-theta-lifts|the triangle of theta lifts]]) \(F_{i,n}\) is attached to the interval \([i+1,i+n]\), the arrow \(a\) adds the greatest element (a theta lift), \(d\) is the adjoint of the map that adds the least element, and \(I\) is a set of moduli.

## References

1. Lean: `New.Exchange.IsTriangle` in `src/New/Determinant/Chain/TriangleNorms.lean`.
2. Lean: `New.Exchange.SquareCommutes` in `src/New/Determinant/Chain/TriangleNorms.lean`.
3. Lean: `New.Exchange.weightedChain` in `src/New/Determinant/Chain/TriangleNorms.lean`.
