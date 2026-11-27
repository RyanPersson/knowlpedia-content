+++
id = "proofs/grh/upper-seesaw/standard-lattice-membership"
title = "Membership in the glued standard lattice"
kind = "lemma"
summary = "Coordinate criterion for the lattice spanned by the glued lattice basis; the lattice is graded."
aliases = ["line ideles", "the standard lattice is graded"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.lineIdele", "New.Grading.SpansLattice.exists_gradedLatticeBasis_mulVec_eq", "New.Grading.SpansLattice.mem_lattice_iff", "New.Grading.SpansLattice.isGraded", "New.gradedLatticeBasis_mulVec_apply_inl", "New.gradedLatticeBasis_mulVec_apply_inr"]
lean_files = ["src/New/UpperBound/Seesaw/StandardLines.lean"]
proof_status = "full"
+++

Let \(V\) be a [[?lean:New.Space|hermitian space with a point]] over a [[?c:CM field|CM field]]
\(E\), with a [[?lean:New.Grading|grading]] \(Y\) by \(X\sqcup\{y_0\}\) (grade \(0\)) and a string
\(z_0,\dots,z_{s-1}\) (\(z_b\) of grade \(s-1-2b\)), and suppose \(Y\)
[[proofs/grh/upper-seesaw/graded-lattice-basis|spans the lattice]] of \((a,\pi,u)\). Write
\(\widehat{\mathcal{O}}=\widehat{\mathcal{O}}_E\), let \(\Lambda=x_f\widehat{\mathcal{O}}^{\iota}\) be
the [[?lean:New.Space.lattice|lattice of \(V\)]] and define the **line ideles**
\[
\lambda_b=\begin{cases}u,& s \text{ odd},\\ u\,a^{-1},& s\text{ even},\ 2b<s,\\ u\,\bar a,& s\text{ even},\ 2b\ge s.\end{cases}
\]

**Lemma.** A vector \(y\in\mathbb{A}_{E,f}^{\iota}\), with coordinates \(y_i\) (\(i\in X\)),
\(y_e\) (at the distinguished vector \(y_0\); the subscript \(e\) keeps it apart from the string coordinate \(y_b\) at \(b=0\)) and \(y_b\) (at \(z_b\)), lies in \(\Lambda\) if and only if

1. \(y_i\in\widehat{\mathcal{O}}\) for all \(i\in X\);
2. \(\bar\pi\,y_e\in\widehat{\mathcal{O}}\) if \(s\) is odd, \(y_e\in\widehat{\mathcal{O}}\) if \(s\) is even;
3. for every \(b\): \(\lambda_b^{-1}y_b\in\widehat{\mathcal{O}}\) if \(b\neq s-1-b\), and
   \(\lambda_b^{-1}y_b-\pi^{-1}y_e\in\widehat{\mathcal{O}}\) for the middle index \(b=s-1-b\).

Consequently \(\Lambda\) is *graded*: it contains the component in each grade of each of its
vectors.

## Proof

Since \(x_f=\mathcal{B}k\) with \(k\in\mathrm{GL}(\widehat{\mathcal{O}})\), we have
\(\Lambda=\mathcal{B}\,\widehat{\mathcal{O}}^{\iota}\): every \(y\) is \(\mathcal{B}c\) for a
unique \(c\), and \(y\in\Lambda\) iff \(c\) is integral. Reading off the columns of \(\mathcal{B}\):
\(y_i=c_i\) on \(X\); \(y_e=\bar\pi^{-1}c_e\) (odd \(s\)) or \(c_e\) (even \(s\)); and
\(y_b=\lambda_bc_b\), plus \(u(\pi\bar\pi)^{-1}c_e\) at the middle index. Solving,
\(c_e=\bar\pi y_e\) resp. \(y_e\), and at the middle index (which exists only for odd \(s\), where
\(\lambda_b=u\))
\[
c_b=\lambda_b^{-1}y_b-(\pi\bar\pi)^{-1}\bar\pi\,y_e=\lambda_b^{-1}y_b-\pi^{-1}y_e .
\]
This is the criterion.

*Graded.* The only condition linking two coordinates links \(y_e\) and the middle coordinate, both
of grade \(0\) (the middle vector has grade \(s-1-2b=0\)). The component of \(y\) in grade \(d\)
keeps the coordinates of grade \(d\) and replaces the others by \(0\); the three conditions are
preserved. \(\blacksquare\)

## References

1. Lean: `New.Grading.SpansLattice.mem_lattice_iff`, `New.Grading.SpansLattice.isGraded` in `src/New/UpperBound/Seesaw/StandardLines.lean`.
