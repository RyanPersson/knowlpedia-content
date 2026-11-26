+++
id = "proofs/grh/reduction-main/colength-calculus"
title = "Calculus of colengths: chains, preimages, images, compositions"
kind = "lemma"
summary = "The relation 'colength divides z' multiplies along chains and passes along linear maps in both directions."
aliases = ["colength calculus"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.ColengthDvd.trans", "New.ColengthDvd.comap", "New.ColengthDvd.map", "New.ColengthDvd.comp"]
lean_files = ["src/New/Reduction/Lattices/Colength.lean"]
proof_status = "full"
+++

**Lemma.** Let \(O\) be a [[?c:commutative ring|commutative ring]], \(U,V\) two \(O\)-[[algebra-modules/module|modules]], \(M,N,P\subseteq V\) and \(M',N'\subseteq U\) [[?c:submodule|submodules]], and \(z,z',a\in O\). We use the relation [[proofs/grh/reduction-main/colength-divides|\(\operatorname{colen}(M,N)\mid z\)]].

1. **(Chains.)** If \(\operatorname{colen}(M,N)\mid z\) and \(\operatorname{colen}(N,P)\mid a\), then \(\operatorname{colen}(M,P)\mid za\).
2. **(Preimages.)** Let \(f:U\to V\) be \(O\)-[[?c:linear map|linear]] with \(f(M')\subseteq M\), and suppose every \(x\in M'\) with \(f(x)\in N\) lies in \(N'\). If \(\operatorname{colen}(M,N)\mid z\), then \(\operatorname{colen}(M',N')\mid z\).
3. **(Images.)** Let \(f:V\to U\) be \(O\)-linear with \(M'\subseteq f(M)+N'\) and \(f(N)\subseteq N'\). If \(\operatorname{colen}(M,N)\mid z\), then \(\operatorname{colen}(M',N')\mid z\).
4. **(Compositions.)** Let \(f:V\to V\) be \(O\)-linear with \(f(M)\subseteq M\). If \(\operatorname{colen}(M,\,f(M)+aM)\mid z\) and \(\operatorname{colen}(M,\,N+aM)\mid z'\), then \(\operatorname{colen}(M,\,f(N)+aM)\mid zz'\).

## Proof

(1) Let \(\Phi_1,\dots,\Phi_n\in M\). Choose \(m\) with \(\det m\mid z\) and \(\Psi_i:=\sum_k m_{ik}\Phi_k\in N\). Apply the second hypothesis to the family \(\Psi\): there is \(m'\) with \(\det m'\mid a\) and \(\sum_j m'_{ij}\Psi_j\in P\). Now \(\sum_j m'_{ij}\Psi_j=\sum_k (m'm)_{ik}\Phi_k\), and \(\det(m'm)=\det m'\det m\) divides \(az=za\).

(2) Let \(\Phi_1,\dots,\Phi_n\in M'\). The family \(f(\Phi_k)\) lies in \(M\), so there is \(m\) with \(\det m\mid z\) and \(\sum_k m_{ik}f(\Phi_k)\in N\). The element \(x_i=\sum_k m_{ik}\Phi_k\) lies in \(M'\) and \(f(x_i)\in N\), hence \(x_i\in N'\).

(3) Let \(\Phi_1,\dots,\Phi_n\in M'\). Write \(\Phi_k=f(x_k)+y_k\) with \(x_k\in M\), \(y_k\in N'\). Choose \(m\) with \(\det m\mid z\) and \(\sum_k m_{ik}x_k\in N\). Then
\[
\sum_k m_{ik}\Phi_k=f\Bigl(\sum_k m_{ik}x_k\Bigr)+\sum_k m_{ik}y_k\in f(N)+N'\subseteq N'.
\]

(4) Apply (3) to the hypothesis \(\operatorname{colen}(M,N+aM)\mid z'\), with the map \(f\), with \(M'=f(M)+aM\) and \(N'=f(N)+aM\). The two conditions hold: \(M'=f(M)+aM\subseteq f(M)+N'\), and \(f(N+aM)=f(N)+a\,f(M)\subseteq f(N)+aM\) because \(f(M)\subseteq M\). Hence \(\operatorname{colen}(f(M)+aM,\ f(N)+aM)\mid z'\). Chaining this after \(\operatorname{colen}(M,f(M)+aM)\mid z\) by (1) gives the claim.

## References

1. Lean: `New.ColengthDvd.trans`, `.comap`, `.map`, `.comp` in `src/New/Reduction/Lattices/Colength.lean`.
