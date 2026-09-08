+++
id = "fiber-bundles/pontryagin-class"
title = "Pontryagin class"
kind = "knowl"
summary = "Integral characteristic classes of a real vector bundle defined from the Chern classes of its complexification."
aliases = ["pontryagin-class", "Pontryagin class via Chern–Weil theory"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/pontryagin-class.md"
prerequisites = ["fiber-bundles/topological-real-vector-bundle", "fiber-bundles/integral-chern-classes", "linear-algebra/complexification", "topology/singular-cohomology-group", "fiber-bundles/paracompact-topological-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 2
+++

Let \(E\to X\) be a rank-\(r\) [[fiber-bundles/topological-real-vector-bundle|topological real vector bundle]] over a paracompact Hausdorff space. Its complexification \(E^{\mathbb C}\) has fibers \(E_x\otimes_{\mathbb R}\mathbb C\), with local trivializations obtained by regarding the real transition matrices as complex matrices. For \(k\ge0\), the **\(k\)th Pontryagin class** is
\[
p_k(E)=(-1)^k c_{2k}(E^{\mathbb C})\in H^{4k}(X;\mathbb Z),
\]
where \(c_{2k}\) is the [[fiber-bundles/integral-chern-classes|integral Chern class]]. Thus \(p_0(E)=1\) and \(p_k(E)=0\) for \(2k>r\). The **total Pontryagin class** is \(p(E)=1+p_1(E)+p_2(E)+\cdots\).

## Chern–Weil representatives

If \(X=M\) is a smooth manifold and \(E\) is smooth, choose a fiber metric and a compatible connection \(\nabla\) with curvature \(F_\nabla\). Its complexification induces a complex connection \(\nabla^{\mathbb C}\).
Define the **Pontryagin forms** by
\[
p_k(\nabla)\;:=\;(-1)^k\,c_{2k}(\nabla^{\mathbb C})\in \Omega^{4k}(M),
\]
where \(c_{2k}(\nabla^{\mathbb C})\) is the corresponding [[fiber-bundles/chern-class|Chern–Weil Chern form]].

Then:
1. Each \(p_k(\nabla)\) is closed: \(d\,p_k(\nabla)=0\), where \(d\) is the [[fiber-bundles/exterior-derivative|exterior derivative]].
2. The de Rham class \([p_k(\nabla)]\in H^{4k}_{\mathrm{dR}}(M)\) is independent of the choice of compatible connection.
3. The de Rham class \([p_k(\nabla)]\) is the real image of the integral class \(p_k(E)\).

The de Rham representative detects only the real image of \(p_k(E)\), not any torsion in the integral class. Equivalently, this real image is the Chern–Weil class associated to the structure group \(O(r)\) (or \(SO(r)\) in the oriented case) by applying an \(Ad\)-invariant polynomial on \(\mathfrak{so}(r)\) corresponding to the \(k\)th elementary symmetric polynomial in the squares of the formal curvature eigenvalues.

## Naturality

For any continuous map \(f:Y\to X\) between paracompact Hausdorff spaces, the topological classes satisfy
\[
p_k(f^*E)=f^*p_k(E).
\]

## Examples
1. **Trivial bundle / flat connection.** If \(E\cong M\times\mathbb R^r\) is trivial, then \(p_k(E)=0\) for all \(k\ge 1\). More generally, a flat connection has \(F_\nabla=0\), so its Pontryagin forms vanish and the real (hence rational) images of the positive-degree Pontryagin classes are zero.

2. **Underlying real bundle of a [[fiber-bundles/line-bundle|complex line bundle]].** Let \(L\to M\) be a complex line bundle with \(c_1(L)=x\in H^2(M;\mathbb Z)\). For the underlying real rank-2 bundle \(L_{\mathbb R}\) one has
   \[
   p_1(L_{\mathbb R})=x^2\in H^4(M;\mathbb Z),
   \]
   because \(p_1=(-1)c_2\big((L_{\mathbb R})^{\mathbb C}\big)\) and \((L_{\mathbb R})^{\mathbb C}\cong L\oplus \overline{L}\).

3. **Dimensional vanishing.** If \(\dim M < 4k\), then every \(4k\)-form vanishes and hence \(p_k(E)=0\) in de Rham cohomology (and therefore in rational cohomology) for degree reasons.
