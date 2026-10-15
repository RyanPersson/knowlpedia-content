+++
id = "catalog/relationships/regular-module-endomorphisms"
title = "Endomorphisms of the left and right regular modules"
kind = "theorem"
summary = "Endomorphisms of the left and right regular modules."
aliases = []
domains = ["catalog", "algebra-rings"]
prerequisites = ["catalog/categories/left-modules", "catalog/categories/right-modules"]
+++

For a unital ring \(A\), the regular modules have endomorphism rings
\[
\operatorname{End}_{A-\mathrm{Mod}}({}_A A)\cong A^{\mathrm{op}},\qquad
\operatorname{End}_{\mathrm{Mod}-A}(A_A)\cong A.
\]
Endomorphisms are added pointwise and multiplied by composition. The first isomorphism sends \(a\in A^{\mathrm{op}}\) to \(R_a:{}_A A\to {}_A A\), \(R_a(x)=xa\). The second sends \(a\in A\) to \(L_a:A_A\to A_A\), \(L_a(x)=ax\). In \(A^{\mathrm{op}}\) the product is \(a\star b=ba\).

## Proof

For \(a,b,x\in A\), associativity gives \(R_a(bx)=bR_a(x)\) and \(L_a(xb)=L_a(x)b\); distributivity gives additivity. Every left-linear map \(f:{}_A A\to {}_A A\) satisfies \(f(x)=xf(1)\), and every right-linear map \(g:A_A\to A_A\) satisfies \(g(x)=g(1)x\). Evaluation at \(1\) therefore gives the inverse bijections.

Addition is preserved since \(R_{a+b}=R_a+R_b\) and \(L_{a+b}=L_a+L_b\). Both send \(1\) to the identity map. For composition,
\[
(R_a\circ R_b)(x)=(xb)a=x(ba)=R_{ba}(x),
\]
\[
(L_a\circ L_b)(x)=a(bx)=(ab)x=L_{ab}(x).
\]
Thus \(a\mapsto R_a\) is multiplicative from the opposite ring, while \(a\mapsto L_a\) is multiplicative from \(A\).

## Automorphisms

If \(a\) is a unit, the inverses are \(R_{a^{-1}}\) and \(L_{a^{-1}}\). Conversely a module inverse has the same form, and its two composite identities imply \(ab=ba=1\) for its parameter \(b\). Hence the automorphism groups are \((A^{\mathrm{op}})^\times\) and \(A^\times\), respectively. A zero endomorphism is allowed; preserving the element \(1\) is not required.

## Noncommutative test case

Take [[catalog/algebras/m-2-r|\(A=M_2(\mathbb R)\)]]. For matrix units \(a=E_{12}\) and \(b=E_{21}\), we have \(ab=E_{11}\) and \(ba=E_{22}\). At \(I_2\), the composites \(R_a\circ R_b\) and \(L_a\circ L_b\) therefore take distinct values \(E_{22}\) and \(E_{11}\).

The map \(R_a\) is left-linear but not right-linear: \(R_a(I_2b)=ba\ne ab=R_a(I_2)b\). The map \(L_a\) is right-linear but not left-linear: \(L_a(bI_2)=ab\ne ba=bL_a(I_2)\). Although transpose identifies [[catalog/algebras/m-2-r-op|\(A^{\mathrm{op}}\)]] with \(A\), identifying their matrices without transposing would lose this composition order.
