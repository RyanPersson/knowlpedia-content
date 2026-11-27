+++
id = "proofs/grh/spanning-core/open-cell-bound"
title = "Open cell bound for a Bessel system"
kind = "definition"
summary = "The mean L2 bound for the kernels W(gamma t z) tensor conj W(t z) over shifts t fixing the frame, with a bounding measure of mass at most the pairing bound."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.BesselSystem.IsOpenCellBound", "New.BesselSystem.IsKernelBound", "New.Shape.FixerFactors"]
lean_files = ["src/New/Spanning/Bessel/OpenCellBound.lean"]
+++

Let \(X\) be a [[proofs/grh/spanning-core/bessel-system|Bessel system]] on \(G_1\) with full function \(W\colon G_1\to\mathbb{C}^I\) and degree \(\deg\), let \(\gamma\in G_1\) and \(\rho\in\mathbb{R}\). Recall ([[?lean:New.IsL2Contraction|`IsL2Contraction`]]) that a finite family of kernels \(k_i(x,y)\) is an **\(L^2\) contraction** for measures \(m\) (in \(x\)), \(\mu\) and \(\nu\) (in \(y\)) if for every bounded measurable \(\varphi\)
\[
\int\sum_i\Bigl\lvert\int\varphi(y)k_i(x,y)\,d\mu(y)\Bigr\rvert^2dm(x)\le\int\lvert\varphi\rvert^2d\nu .
\]
An **open cell bound** for \((X,\gamma,\rho)\) consists of a measurable space \(T\) with a measure \(m\), a set \(A\subseteq G_1\), a measure \(\nu\) on \(G_1\) and a map \(t\colon T\to G_1\) such that

1. \(A\) is compact; \(t\) is measurable and every \(t(x)\) fixes each frame vector; \(m\) is a probability measure;
2. the kernels \(k_{(i,j)}(x,z)=W_i(\gamma\,t(x)\,z)\,\overline{W_j(t(x)\,z)}\), \((i,j)\in I\times I\), are an \(L^2\) contraction for \(m\), Haar measure restricted to \(A\), and \(\nu\);
3. \(\nu\) is finite, of total mass at most the [[proofs/grh/spanning-core/local-bounds-of-a-bessel-function|pairing bound]] \(\bigl(\rho^{9n}/\mathsf g\bigr)^{10^5n^4}\lvert I\rvert^2/\bigl(\deg\,c_G\,(\mathsf g/2)^{k-1}\bigr)\), \(\mathsf g=\mathsf g(Z(\gamma))\);
4. for \(m\)-almost every \(x\), \(A\) contains every \(z\) in the [[proofs/grh/spanning-core/bessel-length|frame box]] of radius \(\rho\) with \(\ell(\gamma\,t(x)\,z)\le\rho\).

(In the source the intermediate notion `IsKernelBound` is the same with a general family \(g(x)\) in place of \(\gamma t(x)\), a bound \(C\) for the mass and a radius \(M\).)

## References

1. Lean: `New.BesselSystem.IsOpenCellBound`, `New.BesselSystem.IsKernelBound` in `src/New/Spanning/Bessel/OpenCellBound.lean`.
