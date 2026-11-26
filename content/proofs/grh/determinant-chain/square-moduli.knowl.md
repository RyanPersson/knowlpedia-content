+++
id = "proofs/grh/determinant-chain/square-moduli"
title = "Moduli of the squares of a triangle"
kind = "definition"
summary = "The hypothesis that the constants of the squares of a triangle have prescribed moduli and that each square obeys an adjoint law."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Exchange.HasSquareModuli", "New.Exchange.SquareAdjoint"]
lean_files = ["src/New/Determinant/Chain/TriangleNorms.lean"]
+++

Let \((F,V,a,d,w,j)\) be the data of a [[proofs/grh/determinant-chain/triangle-of-arrows|triangle of arrows]] with parameter set \(I\), and \(m\ge0\). Let \(\mathcal{M}\) be a relation between functions \(c\colon I\to\mathbb{C}\) and \(f\colon I\to\mathbb{R}\), read "\(c\) has modulus \(f\)", and let \(L_{r,k}\colon I\to\mathbb{R}\) be functions (\(r,k\ge0\)).

For \(\kappa\colon I\to\mathbb{C}\), the square at \((i,n)\) obeys the **adjoint law with constant \(\kappa\)** if for every \(t\) and every \(z\in F_{i,n+2}\) there is \(x\in F_{i,n+1}\) such that
\[
\langle a_{t,i,n+1}\,y,\ z\rangle=\langle y,x\rangle\ \ (y\in F_{i,n+1}),\qquad
\langle d_{t,i,n}\,x,\ y\rangle=\kappa(t)\,\langle d_{t,i,n+1}\,z,\ a_{t,i+1,n}\,y\rangle\ \ (y\in F_{i+1,n}).
\]

The data **have square moduli \(L\)** (with respect to \(\mathcal M\), in size \(m\)) if

1. \(\mathcal{M}(1,1)\), and \(\mathcal M(c,f)\), \(\mathcal M(c',f')\) imply \(\mathcal M(cc',ff')\);
2. for \(i+n+2\le m\) the square at \((i,n)\) commutes up to some \(\beta\) with \(\mathcal M(\beta,\ L_{i+1,\,i+n+2})\);
3. for \(i+n+2\le m\) the square at \((i,n)\) obeys the adjoint law with some constant \(\kappa\) with \(\mathcal M(\kappa,1)\).

## Remarks

The spaces need not be finite-dimensional or complete, so the adjoint vector \(x\) of \(z\) for \(a\) is asked to exist. The relation \(\mathcal M\) is abstract so that the same induction serves for "\(\lvert c(t)\rvert^2=f(t)\)" and for finer statements such as [[proofs/grh/determinant-chain/modulus-relation-of-the-chain|the modulus relation used for the chain]].

## References

1. Lean: `New.Exchange.HasSquareModuli` in `src/New/Determinant/Chain/TriangleNorms.lean`.
2. Lean: `New.Exchange.SquareAdjoint` in `src/New/Determinant/Chain/TriangleNorms.lean`.
