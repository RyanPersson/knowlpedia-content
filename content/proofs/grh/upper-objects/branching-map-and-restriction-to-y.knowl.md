+++
id = "proofs/grh/upper-objects/branching-map-and-restriction-to-y"
title = "The integral branching map and the restriction of forms from X_m to Y_m"
kind = "construction"
summary = "An integral matrix from the Weyl module of X_m to that of Y_m, equivariant up to the character with the branching exponents, bounded in norm and spanning the equivariant maps; and the restriction of algebraic forms built from it."
aliases = ["branching map", "restriction to Y_m", "restrictToY"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsBranchingMap", "New.Data.exists_isBranchingMap", "New.Data.exists_sum_columnsY_le_and_pow_le_exp", "New.Data.branching", "New.Data.lastIndexEquiv", "New.Data.borderU", "New.Data.restrictToY", "New.Data.restrictToYOfEq", "New.Data.cast_diagramWeight_columnCount"]
lean_files = ["src/New/UpperBound/Objects/Columns.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]]. Let \(\mathcal V(X_m)\) and \(\mathcal V(Y_m)\) be the Weyl modules (with their integral bases of standard fillings) of the [[proofs/grh/upper-objects/weights-of-the-definite-spaces|weights \(\mu(X_m)\) and \(\mu(Y_m)\)]]: column numbers \(c_\tau\), resp. \(c^Y_\tau\), and the same determinant exponents \(\ell_m\). Fix a bijection between the index set of \(Y_m\) (\(r+mt=n_m-1\) elements) and the indices of \(X_m\) other than the last; so \(X_m=Y_m\oplus E e_\ast\).

**Definition.** An integer matrix \(\mathrm{br}\colon\mathcal V(X_m)\to\mathcal V(Y_m)\) is a **branching map** if

1. over every field \(R\) of characteristic \(0\), for all \(g=(g_\tau)\in\prod_\tau\mathrm{GL}_{n_m-1}(R)\) and \(z=(z_\tau)\in\prod_\tau R^\times\): \(\mathrm{br}\circ\rho_{X}(\operatorname{diag}(g,z))=\prod_\tau z_\tau^{\,n_\tau}\cdot\rho_Y(g)\circ\mathrm{br}\), where \(n_\tau\) is the [[proofs/grh/upper-objects/branching-exponent-formula|branching exponent]];
2. \(\lVert\mathrm{br}\,\xi\rVert^2\le\exp(x^{70})\,\lVert\xi\rVert^2\) for all complex \(\xi\) (the [[?lean:New.weylNormSq|norm of the Weyl module]]);
3. every complex matrix \(\mathcal V(X_m)\to\mathcal V(Y_m)\) equivariant for the elements \(\operatorname{diag}(g,1)\), \(g\) unitary, is a multiple of \(\mathrm{br}\).

**Proposition.** A branching map exists. One is fixed and called \(\mathrm{br}\).

**Construction (restriction to \(Y_m\)).** For an algebraic form \(F\) on \(U(X_m)\) with values in \(\mathcal V(X_m)\),
\[
(\operatorname{res}_YF)(h)=\prod_{\tau}\tau(\bar\pi_N)^{-n_\tau}\cdot\mathrm{br}\big(F(\operatorname{diag}(h,1))\big),\qquad h\in U(Y_m)(\mathbb A_f),
\]
where \(\tau\) is read as its embedding in the CM type. This is an algebraic form on \(U(Y_m)\) with values in \(\mathcal V(Y_m)\) (smoothness because \(h\mapsto\operatorname{diag}(h,1)\) is continuous; equivariance under rational points by property 1 with \(z=1\)).

## Proof

Existence is the Lean lemma `New.exists_branching_matrix` of the library on integral branching for \(\mathrm{GL}_n\) (another area; cited). Its hypotheses are supplied by the [[proofs/grh/upper-objects/columns-of-the-weights|column description]]: the weights interlace, the columns counted by \(\operatorname{kept}\) keep their height and the others lose a box, \(\operatorname{kept}(n_m-1)=0\) so the last entries agree, and the exponent has the form of part 2 of the [[proofs/grh/upper-objects/branching-exponent-formula|branching exponent lemma]]. The norm bound of the library is \(((l^l)^3)^2\) for any \(l\) bounding the number of boxes \(\sum_\tau\sum_{k\le u<n_m-1}u\,c^Y_\tau(u)\) in the columns of height \(\ge k\) (heights below \(k\) are omitted because \(\operatorname{kept}\) vanishes there); with \(l=f\,n_m^2\,\Delta\) (using \(c^Y_\tau(u)\le\Delta\)) one has \(((l^l)^3)^2\le\exp(x^{70})\) by the size relations of the data. \(\square\)

## References

1. Lean: `New.Data.IsBranchingMap`, `New.Data.exists_isBranchingMap`, `New.Data.branching`, `New.Data.restrictToY` in `src/New/UpperBound/Objects/Columns.lean`.
