A real Banach space is a real vector space \(E\) with a complete norm. Its unit sphere is
\[
S_E=\{x\in E:\lVert x\rVert=1\}.
\]
A surjective linear isometry of \(E\) is a bijective linear map \(T:E\to E\) satisfying \(\lVert Tx\rVert=\lVert x\rVert\) for every \(x\). These maps form the linear isometry group \(\operatorname{Iso}(E)\), which acts on \(S_E\).

The norm is called transitive when this action is transitive: for every \(x,y\in S_E\), some surjective linear isometry \(T\) satisfies \(Tx=y\). A real Hilbert space is a complete inner-product space; its norm obeys the parallelogram identity
\[
\lVert x+y\rVert^2+\lVert x-y\rVert^2=2\lVert x\rVert^2+2\lVert y\rVert^2.
\]

## Conjecture

Every separable real Banach space whose linear isometry group acts transitively on its unit sphere is linearly isometric to a real Hilbert space.

The hypothesis says that the norm looks exactly the same in every unit direction. The conclusion is stronger than abstract linear isomorphism: it says that the given norm itself is induced by an inner product.

## Known boundary

The finite-dimensional problem is solved: a finite-dimensional normed space with transitive linear isometry group is Euclidean. The infinite-dimensional separable case remains open. Variants weaken transitivity to almost transitivity or strengthen the regularity of the norm; those are related but not identical problems.

## Formal source

This page follows `FormalConjectures/Arxiv/math.0110202/BanachMazurRotation.lean`, whose conclusion supplies a linear isometric equivalence with a real Hilbert space.
