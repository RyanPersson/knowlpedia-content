+++
id = "proofs/grh/spanning-core/bounds-for-the-gram-section"
title = "Polynomial bounds for the Gram section and its derivative"
kind = "theorem"
summary = "If Z is bounded in the open cell by T >= 4 then the matrix of gamma_Z has norm at most T^18 and its real derivative at most T^25; boundedness in the cell is stable under small perturbations."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.RealPlace.IsBoundedInCell.norm_sectionMatrix_le", "New.RealPlace.norm_sectionMatrix_le_and_norm_fderiv_le", "New.RealPlace.norm_sectionMatrix_le_pow", "New.RealPlace.IsBoundedInCell.norm_sectionMatrix_le_pow", "New.RealPlace.norm_fderiv_sectionMatrix_le", "New.RealPlace.norm_sectionCoeff_le", "New.RealPlace.norm_sqrt_one_sub_invCorner_mul_le", "New.RealPlace.norm_inv_sqrt_one_sub_invCorner_mul_le", "New.RealPlace.IsBoundedInCell.of_mem_ball", "New.RealPlace.IsBoundedInCell.isUnit_det_and_norm_inv_le", "New.RealPlace.IsBoundedInCell.mul_oneSubNormSqInvCorner_le", "New.RealPlace.IsBoundedInCell.inv_sq_le_oneSubNormSqInvCorner", "New.RealPlace.IsBoundedInCell.gramDiscReal_div_two_le"]
lean_files = ["src/New/Spanning/Bessel/GramSection.lean"]
proof_status = "full"
+++

**Theorem.** Use the notation of the [[proofs/grh/spanning-core/open-cell-of-frame-matrices|open cell]] and the [[proofs/grh/spanning-core/gram-section|Gram section]]; norms are operator norms.

1. (Value.) Let \(P\ge8\), let \(Z\) be bounded in the cell by \(P\), and \(W\in\Omega\) with \(\lVert W^{-1}\rVert\le P\). Then \(\lVert M(Z,W)\rVert\le P^{12}\).
2. (Perturbation.) Let \(T\ge4\), \(Z\) bounded in the cell by \(T\), and \(\lVert Y-Z\rVert<T^{-6}\). Then \(Y\) is invertible, \(\lVert Y^{-1}\rVert\le2T\), \(\lVert Y^{-1}-Z^{-1}\rVert\le2T^{-4}\), \(\nu(Y)^2\ge(1-8T^{-2})\nu(Z)^2\), and \(Y\) is bounded in the cell by \(2T\). If moreover \(T\ge8\) and \(T\ge\varrho+1\), then \(\mathsf g(Y)\ge\tfrac12\mathsf g(Z)\).
3. (Derivative.) Let \(r>0\), \(P\ge8\), and suppose every \(Y\) with \(\lVert Y-Z\rVert<r\) is bounded in the cell by \(P\). Then the real derivative at \(Z\) of \(Y\mapsto M(Y,Y^*)\) has norm at most \(2P^{12}/r\).
4. Let \(T\ge4\) and \(Z\) bounded in the cell by \(T\). Then \(\lVert M(Z,Z^*)\rVert\le T^{18}\) and the real derivative of \(Y\mapsto M(Y,Y^*)\) at \(Z\) has norm at most \(T^{25}\).

## Proof

(1) \(\lVert F\rVert,\lVert F'\rVert\le1\) and \(\lVert\delta(x)\rVert\le1+\lvert x\rvert\). From the definition, \(\lVert Y(Z,W)\rVert\le2+1\cdot P\cdot\tfrac52\cdot P\cdot3\le2+8P^2\) when \(\lVert Z^{-1}\rVert,\lVert W^{-1}\rVert\le P\). For \(Z,W\in\Omega\): \(\lvert s\rvert^2=\lvert1-\xi(Z)\xi(W)\rvert\le2\), so \(\lvert s\rvert\le2\); and \(\lvert1-\xi(Z)\xi(W)\rvert\ge1-\lvert\xi(Z)\rvert\ge\nu(Z)^2/4\) (as \(1-t\ge(1-t^2)/4\) for \(0\le t<1\)), so \(\lvert s^{-1}\rvert\le2/\nu(Z)\le2P\). Therefore \(\lVert S(Z,W)\rVert\le(2+8P^2+3)P\) and
\[
\lVert M(Z,W)\rVert\le3+(5+8P^2)P+\bigl(P+(5+8P^2)P(2+8P^2)\bigr)(1+2P)\le P^{12}\qquad(P\ge8),
\]
the last inequality because, written in \(t=P-8\ge0\), the difference is a polynomial with nonnegative coefficients.

(2) \(\lVert Z^{-1}(Y-Z)\rVert\le T\cdot T^{-6}\le\tfrac12\), so \(Y=Z(1+Z^{-1}(Y-Z))\) is invertible. From \(Y^{-1}-Z^{-1}=-Y^{-1}(Y-Z)Z^{-1}\), \(\lVert Y^{-1}-Z^{-1}\rVert\le\lVert Y^{-1}\rVert T^{-5}\le\tfrac12\lVert Y^{-1}\rVert\), whence \(\lVert Y^{-1}\rVert\le2T\) and then \(\lVert Y^{-1}-Z^{-1}\rVert\le2T^{-4}\). An entry is bounded by the norm, so \(\lvert\xi(Y)\rvert\le\lvert\xi(Z)\rvert+2T^{-4}\) and \(\lvert\xi(Y)\rvert^2\le\lvert\xi(Z)\rvert^2+8T^{-4}\). Since \(1/\nu(Z)\le T\) gives \(\nu(Z)^2\ge T^{-2}\), \(\nu(Y)^2\ge\nu(Z)^2-8T^{-4}\ge(1-8T^{-2})\nu(Z)^2\ge\tfrac12T^{-2}\ge(2T)^{-2}\). Also \(\lVert Y\rVert\le T+1\le2T\). So \(Y\) is bounded in the cell by \(2T\).

For the discriminant: \(Z=(1-(Y-Z)Y^{-1})Y\) and \(\lvert\det A\rvert\le\lVert A\rVert^{\varrho+1}\) give \(\lvert\det Z\rvert\le(1+2T^{-5})^{\varrho+1}\lvert\det Y\rvert\le e^{2T^{-4}}\lvert\det Y\rvert\le\tfrac98\lvert\det Y\rvert\) (using \(\varrho+1\le T\), \(T\ge8\)); and \(\nu(Y)^2\ge\tfrac78\nu(Z)^2\). With \(\mathsf g=\lvert\det\rvert^2\nu^2\): \(\tfrac12\mathsf g(Z)\le\tfrac{81}{128}\lvert\det Y\rvert^2\nu(Z)^2\le\lvert\det Y\rvert^2\cdot\tfrac78\nu(Z)^2\le\mathsf g(Y)\).

(3) Consider the pair \((x,w)\) in the ball of radius \(r\) about \((Z,Z^*)\) (maximum norm on pairs): then \(x\) and \(w^*\) are within \(r\) of \(Z\), hence bounded in the cell by \(P\); so \(w\in\Omega\), \(\lVert w^{-1}\rVert\le P\), and by [[proofs/grh/spanning-core/gram-section-is-a-section|holomorphy]] and (1), \((x,w)\mapsto M(x,w)\) is holomorphic and bounded by \(P^{12}\) on this ball. A holomorphic map bounded by \(B\) on a ball of radius \(r\) about \(c\) satisfies \(\lVert f(p)-f(c)\rVert\le\frac{2B}{r}\lVert p-c\rVert\) there (Schwarz lemma; library statement `New.norm_sub_le_of_holomorphic_bdd`). For \(p=(Y,Y^*)\), \(\lVert p-(Z,Z^*)\rVert=\lVert Y-Z\rVert\). So \(Y\mapsto M(Y,Y^*)\) is Lipschitz with constant \(2P^{12}/r\) near \(Z\), which bounds the derivative.

(4) By (2), every \(Y\) within \(r=T^{-6}\) of \(Z\) is bounded in the cell by \(P=2T\ge8\). By (1) (with \(W=Z^*\), for which \(\lVert W^{-1}\rVert=\lVert Z^{-1}\rVert\)) and (3): \(\lVert M(Z,Z^*)\rVert\le(2T)^{12}=4^6T^{12}\le T^{18}\), and the derivative is at most \(2(2T)^{12}T^6\le T\cdot T^{18}\cdot T^6=T^{25}\). \(\blacksquare\)

## References

1. Lean: `New.RealPlace.IsBoundedInCell.norm_sectionMatrix_le`, `New.RealPlace.norm_sectionMatrix_le_and_norm_fderiv_le`, `New.RealPlace.IsBoundedInCell.of_mem_ball`, `New.RealPlace.IsBoundedInCell.gramDiscReal_div_two_le` in `src/New/Spanning/Bessel/GramSection.lean`.
