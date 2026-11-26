+++
id = "proofs/grh/reduction-main/covolume-add-index-nonneg"
title = "A twist for each prime: covolume plus twice the index is bounded below"
kind = "theorem"
summary = "In a twisted lattice with injective lifts, a family completed to a basis satisfies c + 2 delta + n'(b_short + b_denom) + b_volume >= 0, where b_volume bounds the height of Z(1)/Z(xi_iota)."
aliases = ["a twist for each prime", "covolume_add_index_nonneg"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.TwistedLattice.covolume_add_index_nonneg"]
lean_files = ["src/New/Reduction/Lattices/TwistedLattice.lean"]
proof_status = "full"
+++

**Theorem (a twist for each prime).** Let \(L\) be a [[proofs/grh/reduction-main/twisted-lattice|twisted lattice]] on a finite-dimensional complex inner product space \(V\), with twists \(T\), lifts \(\Theta_\xi\), lattices \(\Lambda_{\xi,\iota}\) and [[proofs/grh/reduction-main/twisted-lattice-volume|volumes \(Z(\xi)\)]]. Assume:

- every \(\Theta_\xi\), \(\xi\in T\), is injective;
- \(y_1,\dots,y_n,z_1,\dots,z_{n'}\) are linearly independent in \(V\) and \(\dim V=n+n'\) (so they form a basis);
- for each [[proofs/grh/reduction-main/prime-padic-iso|finite place \(\iota\mid\ell\)]] a twist \(\xi_\iota\) allowed at \(\ell\) is given;
- \(y\) has [[proofs/grh/reduction-main/covolume-bound|covolume at most \(c\)]] and [[proofs/grh/reduction-main/index-bound|index at most \(\delta\)]];
- numbers \(\gamma(\xi)\in\mathbb C^\times\), \(\xi\in T\), are given such that \(\gamma(\xi)\Theta_\xi z_i\in\Lambda_{\xi,\iota}\) for all \(i\), all \(\iota\mid\ell\) and all \(\xi\) allowed at \(\ell\);
- \(\lVert\Theta_1z_i\rVert_\sigma^2\le e^{b_{\mathrm{short}}}\) for all \(i\) and all \(\sigma\in\operatorname{Aut}(\mathbb C)\);
- the family \(\iota\mapsto\lvert\gamma(\xi_\iota)\rvert^{-2}\) has [[proofs/grh/reduction-main/height-bound|height at most \(b_{\mathrm{denom}}\)]], and the family \(\iota\mapsto Z(1)/Z(\xi_\iota)\) has height at most \(b_{\mathrm{volume}}\).

Then
\[
c+2\delta+n'\,(b_{\mathrm{short}}+b_{\mathrm{denom}})+b_{\mathrm{volume}}\ \ge\ 0 .
\]

## Proof

For a twist \(\xi\) let \(\operatorname{Gram}(\xi)\) be the Gram determinant of the \(n+n'\) vectors \(\Theta_\xi y_k,\Theta_\xi z_i\). By property (2) of the [[proofs/grh/reduction-main/twisted-lattice-volume|volume]], \(\operatorname{Gram}(\xi)=Z(\xi)\,g\) with \(g\) the Gram determinant of the basis \((y,z)\) of \(V\), and \(Z(\xi)\ne0\) by injectivity. Hence for every \(\iota\), with \(\gamma_\iota=\gamma(\xi_\iota)\),
\[
\operatorname{Gram}(1)=\Bigl(\lvert\gamma_\iota\rvert^{2n'}\operatorname{Gram}(\xi_\iota)\Bigr)\cdot\Bigl(\lvert\gamma_\iota\rvert^{-2}\Bigr)^{n'}\cdot\frac{Z(1)}{Z(\xi_\iota)} .
\]
The three factors, as families in \(\iota\), have heights at most \(2\delta\) (by part (3) of [[proofs/grh/reduction-main/gram-determinant-valuation|valuations of Gram determinants]]; the hypothesis on \(\gamma\) is applied at \(\iota\) and at \(\bar\iota\), both over \(\ell\)), \(n'b_{\mathrm{denom}}\) and \(b_{\mathrm{volume}}\) respectively. By the product and power rules of [[proofs/grh/reduction-main/height-calculus|the calculus of heights]], the *constant* family \(\operatorname{Gram}(1)\) has height at most \(2\delta+n'b_{\mathrm{denom}}+b_{\mathrm{volume}}\).

On the other hand \(\operatorname{Gram}(1)\ne0\), because \(\Theta_1\) is injective and so the vectors \(\Theta_1y_k,\Theta_1z_i\) are linearly independent. By rules (4) and (2) of [[proofs/grh/reduction-main/covolume-calculus|the calculus of covolumes]], the family \((y,z)\) has covolume at most \(c+n'b_{\mathrm{short}}\), and \(\lvert\sigma\operatorname{Gram}(1)\rvert\le e^{c+n'b_{\mathrm{short}}}\) for all \(\sigma\in\operatorname{Aut}(\mathbb C)\).

Part (2) of the [[proofs/grh/reduction-main/height-product-formula|product formula for heights]] now gives \(-(2\delta+n'b_{\mathrm{denom}}+b_{\mathrm{volume}})\le c+n'b_{\mathrm{short}}\).

## References

1. Lean: `New.TwistedLattice.covolume_add_index_nonneg` in `src/New/Reduction/Lattices/TwistedLattice.lean`.
