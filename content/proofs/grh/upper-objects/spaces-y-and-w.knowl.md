+++
id = "proofs/grh/upper-objects/spaces-y-and-w"
title = "The hermitian spaces Y_j and W_j"
kind = "construction"
summary = "The spaces Y_j, with their lattices: X_j plus a string of 2 rho + 1 - j vectors (hyperbolic pairs and a middle vector of norm -N) for j < m, standard for j >= m; and the diagonal spaces W_j of rank r."
aliases = ["space Y_j", "space W_j", "Y_0", "level places of a twist"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.spaceY", "New.Data.exists_space_isStd_of_le_and_gram_eq_of_lt", "New.Data.isStd_spaceY_of_le", "New.Data.spaceY_gram_eq", "New.Data.exists_spaceY_xFin_eq", "New.Data.isStd_spaceY_last", "New.Data.spaceW", "New.Data.indexEquivY", "New.Shape.besselIndexEquiv", "New.Data.chosenIdele", "New.Data.valued_chosenIdele", "New.Data.ideleA", "New.Data.piNIdele", "New.Data.isSplitSquarefree_piNIdele", "New.Data.latticeScale", "New.Data.levelPlaces", "New.Data.twistModulus", "New.Data.normQ_mem_and_notMem_of_mem_Q"]
lean_files = ["src/New/UpperBound/Objects/Rows.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]]: CM field \(E\), \(m=2\varrho+2\) lifts, level prime \(N=\pi_N\bar\pi_N\), the integer \(\pi_M\) whose prime divisors are the chosen places. A [[?lean:New.Space|space]] is a hermitian space given by a Gram matrix \(J\) over \(E\) together with a point \(x\in\mathrm{GL}_n(\mathbb A_E)\) such that \(x^{*}Jx\) is \(\operatorname{diag}(s)\) at the infinite places (signs \(s\)) and \(1\) at the finite places; the finite part of \(x\) is a basis of a self-dual lattice.

**Construction.**

1. *(Ideles.)* The *chosen idele* is a finite idele generating the ideal \((\pi_M)\) and equal to \(1\) away from the chosen places. Put \(\mathfrak a=\alpha/\bar\beta\), with \(\alpha\) the idele of the [[?lean:New.WeilData|Weil data]] and \(\beta\) the chosen idele (so \(\bar\beta\) generates \((\bar\pi_M)\)); the lattice scale of index \(j\) is \((\mathfrak a/\bar{\mathfrak a})^{\lceil(m-j)/2\rceil}\) (exponent \(0\) for \(j\ge m\)). The principal idele of \(\pi_N\) is a uniformiser exactly at the places of \(P_N\).
2. *(The spaces \(Y_j\).)* For each \(j\ge0\), \(Y_j\) is a space on the [[proofs/grh/upper-objects/index-sets-of-the-hermitian-spaces|index set of \(Y_j\)]] with the [[proofs/grh/upper-objects/grid-nodes|signs of \(Y_j\)]] such that:
   * for \(j\ge m\), \(Y_j\) is the standard definite space (Gram matrix \(1\), point \(1\));
   * for \(j<m\), in a basis indexed by \(X_j\sqcup\{0,\dots,2\varrho-j\}\) (the *string*), the Gram matrix is the identity on \(X_j\), and string vectors \(a,b\) pair to \(1\) if \(a+b=2\varrho-j\), \(a\ne b\), to \(-N\) if \(a=b=(2\varrho-j)/2\), and to \(0\) otherwise ([[?lean:New.gradedGram|graded Gram matrix]]);
   * for \(j<m\), the lattice basis (finite part of the point) is the [[?lean:New.gradedLatticeBasis|graded lattice basis]] built from \(\mathfrak a\), the idele of \(\pi_N\) and the lattice scale, times an integral invertible matrix that reduces to \(1\) at every chosen place.

   Such spaces exist; one is chosen for each \(j\).
3. *(The spaces \(W_j\).)* \(W_j\) is the diagonal hermitian space of rank \(r\) on the row index set with Gram matrix \(\operatorname{diag}(s_j)\), \(s_j\) the [[proofs/grh/upper-objects/signs-and-parameter-of-w|signs of \(W_j\)]].
4. *(Level places of a tame character.)* For a [[?lean:New.Data.TameChar|tame character]] \(\vartheta\) with set of places \(Q\): the [[?lean:New.LevelPlaces|level places]] with \(M\)-part the chosen places above \(p_0,p_1\) and \(Q\)-part the set \(Q\). (A place of \(Q\) or its conjugate divides neither \(\pi_M\) nor \(N\), so all these places are distinct and none is conjugate to another.)

In particular \(Y_0\) is \(X_0\) plus \(\varrho\) hyperbolic planes and one line of norm \(-N\), of rank \(k+2\varrho+1=r\); for \(j=0\) the identification of the index sets is the canonical one (\(e_a\), middle \(z\), \(e^*_{2\varrho-a}\)), for \(j>0\) it is an arbitrary bijection. \(Y_m\) and \(W_m\) are standard definite.

## Proof

*Existence in 2.* For \(j\ge m\) all signs of \(Y_j\) are \(+1\) ([[proofs/grh/upper-objects/properties-of-grid-nodes|properties of the nodes]]) and the standard space works. Let \(j<m\), \(J\) the graded Gram matrix and \(L\) the graded lattice basis.

*Infinite places.* The number of negative signs of \(Y_j\) is \(\lfloor(m-j)/2\rfloor=\lceil(2\varrho+1-j)/2\rceil\), half the length of the string rounded up. The form \(J\) at an infinite place is the identity on \(X_j\) plus, on the string, hyperbolic pairs (each of signature \((1,1)\)) and, if the length is odd, a middle vector of norm \(-N<0\); so it has exactly that many negative signs, and there is \(y_w\in\mathrm{GL}(\mathbb C)\) with \(y_w^*\,w(J)\,y_w=\operatorname{diag}(\text{signs of }Y_j)\) (Lean: `exists_conjTranspose_mul_gradedGram_mul_eq_signMatrix`, cited).

*Finite places.* The lattice with basis \(L\) is unimodular for \(J\) (Lean: `isUnimodular_gradedLatticeBasis_gram`, cited; it uses that the idele of \(\pi_N\) satisfies \(N=\pi_N\bar\pi_N\)), and a unimodular hermitian lattice over the integral finite adeles of the stably unramified field \(E\) has an orthonormal basis: there is an integral invertible \(l\) with \(l^*(L^*JL)l=1\) (Lean: `exists_orthonormal_Ô`, cited). Choose an integral unitary \(k\) (for the standard form) whose reductions at the chosen places are the inverses of those of \(l\) (reduction of the integral unitary points onto \(\prod_w\mathrm{GL}(\mathbb F_w)\) at split places is surjective). The point with archimedean part \((y_w)\) and finite part \(L\cdot lk\) satisfies the condition of a space, and \(lk\) is integral invertible and reduces to \(1\) at every chosen place. \(\square\)

## References

1. Lean: `New.Data.spaceY`, `New.Data.spaceY_gram_eq`, `New.Data.exists_spaceY_xFin_eq`, `New.Data.spaceW`, `New.Data.levelPlaces` in `src/New/UpperBound/Objects/Rows.lean`.
