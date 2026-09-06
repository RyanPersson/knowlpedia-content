+++
id = "posts/introductory-real-analysis"
title = "Introductory Real Analysis: Completeness, Sequences, and Continuity"
kind = "page"
summary = "A knowl-rich first lecture on completeness, sequences, Cauchy sequences, and continuity."
aliases = ["introductory-real-analysis", "Introductory Real Analysis"]
domains = ["posts", "real-analysis"]
knowls_open = true
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

# Introductory Real Analysis: [[real-analysis/completeness-axiom|Completeness]], [[shared-foundations/sequence|Sequences]], and [[topology/continuous-map|Continuity]]

Real analysis begins with the [[shared-foundations/real-numbers|real numbers]] and asks why approximation processes have limits. Algebra supplies addition, multiplication, and order. Analysis adds a decisive structural fact: the [[shared-foundations/real-numbers|real line]] has no gaps.

These notes develop that idea through three connected themes:

1. order, [[shared-foundations/upper-bound|upper bounds]], and [[real-analysis/completeness-axiom|completeness]];
2. [[shared-foundations/sequence|sequences]] and the [[real-analysis/cauchy-criterion-in-rk|Cauchy criterion]];
3. [[topology/continuous-map|continuity]] as preservation of limits.

Most substantive mathematical terms in the prose are expandable knowls. Open one when you want a definition, theorem statement, example, or prerequisite without leaving the lecture.

## 1. Order and [[real-analysis/completeness-axiom|completeness]]

The [[shared-foundations/real-numbers|real numbers]] form an [[real-analysis/order-axioms|ordered field]]. Their order is governed by the [[real-analysis/order-axioms|order axioms]], while [[real-analysis/absolute-value|absolute value]] turns order into [[topology/metric|distance]]:

\[
d(x,y)=|x-y|.
\]

An [[real-analysis/interval|interval]] contains every [[shared-foundations/real-numbers|real number]] lying between any two of its points. [[real-analysis/interval|Intervals]] express the geometric idea that the [[shared-foundations/real-numbers|real line]] is continuous rather than discrete.

The [[shared-foundations/rational-numbers|rational numbers]] are also ordered and [[topology/dense-set|dense]], but they are not complete. Consider

\[
S=\{q\in\mathbb Q:q>0\text{ and }q^2<2\}.
\]

This set is nonempty and [[real-analysis/bounded-above|bounded above]] in [[shared-foundations/rational-numbers|\(\mathbb Q\)]], but it has no [[real-analysis/supremum|supremum]] in [[shared-foundations/rational-numbers|\(\mathbb Q\)]]. The missing boundary would have to be \(\sqrt 2\).

### Definition: [[real-analysis/supremum|supremum]]

Let \(A\subseteq\mathbb R\) be nonempty and [[real-analysis/bounded-above|bounded above]]. A number \(s\in\mathbb R\) is the [[real-analysis/supremum|supremum]] of \(A\) when:

1. \(s\) is an [[shared-foundations/upper-bound|upper bound]] of \(A\); and
2. every [[shared-foundations/upper-bound|upper bound]] \(u\) of \(A\) satisfies \(s\le u\).

Thus the [[real-analysis/supremum|supremum]] is the [[real-analysis/supremum|least upper bound]]. It need not belong to the set, so it need not be a [[real-analysis/maximum|maximum]].

### The [[real-analysis/least-upper-bound-theorem|least-upper-bound theorem]]

Every nonempty [[shared-foundations/subset|subset]] of [[shared-foundations/real-numbers|\(\mathbb R\)]] that is [[real-analysis/bounded-above|bounded above]] has a [[real-analysis/supremum|supremum]] in [[shared-foundations/real-numbers|\(\mathbb R\)]]. This [[real-analysis/least-upper-bound-theorem|least-upper-bound theorem]] is one standard form of the [[real-analysis/completeness-axiom|completeness axiom]].

### Example: constructing \(\sqrt 2\)

Let

\[
A=\{x\in\mathbb R:x\ge0\text{ and }x^2<2\}.
\]

The set is nonempty because \(1\in A\), and it is [[real-analysis/bounded-above|bounded above]] because \(2\) is an [[shared-foundations/upper-bound|upper bound]]. [[real-analysis/completeness-axiom|Completeness]] gives \(s=\sup A\). One proves that \(s^2=2\): if \(s^2<2\), a sufficiently small positive increment keeps the square below \(2\), contradicting that \(s\) is an [[shared-foundations/upper-bound|upper bound]]; if \(s^2>2\), a sufficiently small decrement remains an [[shared-foundations/upper-bound|upper bound]], contradicting the minimality of \(s\).

[[real-analysis/completeness-axiom|Completeness]] has produced a [[shared-foundations/real-numbers|real number]] from an approximation process. That pattern recurs throughout analysis.

### The [[real-analysis/archimedean-property|Archimedean property]]

The [[real-analysis/archimedean-property|Archimedean property]] says that the [[shared-foundations/natural-numbers|natural numbers]] are unbounded in the [[shared-foundations/real-numbers|real numbers]]. Equivalently, for every \(\varepsilon>0\), some \(n\in\mathbb N\) satisfies \(1/n<\varepsilon\). This lets discrete indices control arbitrarily fine estimates.

## 2. [[shared-foundations/sequence|Sequences]] and limits

A [[shared-foundations/sequence|sequence]] is a [[shared-foundations/function|function]] \(a:\mathbb N\to\mathbb R\), usually written \((a_n)\). We say that the [[shared-foundations/sequence|sequence]] converges to \(L\) if, for every \(\varepsilon>0\), there exists \(N\in\mathbb N\) such that

\[
n\ge N\quad\Longrightarrow\quad |a_n-L|<\varepsilon.
\]

The number \(L\) is the [[real-analysis/limit-of-a-sequence|limit of the sequence]]. The definition separates the requested accuracy \(\varepsilon\) from the stage \(N\) after which that accuracy is guaranteed.

### Example: a rational [[shared-foundations/sequence|sequence]]

Consider

\[
a_n=\frac{n}{n+1}=1-\frac{1}{n+1}.
\]

Given \(\varepsilon>0\), choose \(N>1/\varepsilon\). If \(n\ge N\), then

\[
|a_n-1|=\frac{1}{n+1}<\varepsilon.
\]

Hence \(a_n\to1\). Once basic limits are known, the [[real-analysis/limit-algebra-for-sequences|limit algebra for sequences]] combines them under addition, multiplication, and division when the limiting denominator is nonzero.

Every [[topology/convergent-sequence|convergent sequence]] is a [[real-analysis/bounded-sequence|bounded sequence]]. The converse is false: \((-1)^n\) is bounded but does not converge. Nevertheless, [[real-analysis/bounded-sequence|boundedness]] guarantees partial [[real-analysis/limit-of-a-sequence|convergence]]. The [[topology/bolzano-weierstrass-theorem|Bolzano–Weierstrass theorem]] says that every [[real-analysis/bounded-sequence|bounded sequence]] in \(\mathbb R^k\) has a [[topology/convergent-sequence|convergent subsequence]].

A [[real-analysis/subsequence|subsequence]] selects terms \(a_{n_1},a_{n_2},\ldots\) with strictly increasing indices. It can reveal limiting behavior hidden by the full [[shared-foundations/sequence|sequence]]. For example, the even and odd [[real-analysis/subsequence|subsequences]] of \((-1)^n\) converge to different values, proving that the original [[shared-foundations/sequence|sequence]] cannot converge.

## 3. [[topology/cauchy-sequence|Cauchy sequences]]

The [[real-analysis/limit-of-a-sequence|definition of convergence]] mentions the proposed limit \(L\). Sometimes we can prove that approximations stabilize before knowing what their limit should be.

A [[shared-foundations/sequence|sequence]] \((a_n)\) is a [[topology/cauchy-sequence|Cauchy sequence]] if, for every \(\varepsilon>0\), there exists \(N\in\mathbb N\) such that

\[
m,n\ge N\quad\Longrightarrow\quad |a_m-a_n|<\varepsilon.
\]

The terms eventually become close to one another. The [[real-analysis/cauchy-criterion-in-rk|Cauchy criterion]] states that a real [[shared-foundations/sequence|sequence]] converges if and only if it is Cauchy.

### Proof idea

If \(a_n\to L\), the [[real-analysis/triangle-inequality|triangle inequality]] gives, for sufficiently large \(m,n\),

\[
|a_m-a_n|\le |a_m-L|+|a_n-L|<\varepsilon.
\]

Conversely, a [[topology/cauchy-sequence|Cauchy sequence]] is bounded. The [[topology/bolzano-weierstrass-theorem|Bolzano–Weierstrass theorem]] supplies a [[topology/convergent-sequence|convergent subsequence]], and the [[topology/cauchy-sequence|Cauchy property]] forces the entire [[shared-foundations/sequence|sequence]] toward that subsequential limit. This reverse implication is where [[real-analysis/completeness-axiom|completeness]] enters.

In a general [[topology/metric-space|metric space]], not every [[topology/cauchy-sequence|Cauchy sequence]] must converge. A [[topology/metric-space|metric space]] in which every [[topology/cauchy-sequence|Cauchy sequence]] converges is called a [[topology/complete-metric-space|complete metric space]]. Thus [[real-analysis/completeness-axiom|completeness]] converts internal consistency of approximations into existence of a limit.

## 4. [[topology/continuous-map|Continuity]] preserves limits

Let \(f:\mathbb R\to\mathbb R\). The [[shared-foundations/function|function]] is [[real-analysis/continuity-at-a-point|continuous at a point]] \(x\) if, for every \(\varepsilon>0\), there exists \(\delta>0\) such that

\[
|y-x|<\delta\quad\Longrightarrow\quad |f(y)-f(x)|<\varepsilon.
\]

The [[real-analysis/continuity-via-sequences|sequential criterion for continuity]] says that \(f\) is [[real-analysis/continuity-at-a-point|continuous at]] \(x\) exactly when

\[
x_n\to x\quad\Longrightarrow\quad f(x_n)\to f(x).
\]

[[topology/continuous-map|Continuity]] therefore transports [[topology/convergent-sequence|convergent input approximations]] to convergent output approximations.

### Example: [[topology/continuous-map|continuity]] of \(f(x)=x^2\)

Fix \(x\in\mathbb R\). For \(y\) near \(x\),

\[
|y^2-x^2|=|y-x|\,|y+x|.
\]

First require \(|y-x|<1\), which implies \(|y+x|\le2|x|+1\). It is then enough to choose

\[
\delta=\min\left\{1,\frac{\varepsilon}{2|x|+1}\right\}.
\]

This is a common estimate pattern: impose a coarse local bound first, then tune the remaining factor to \(\varepsilon\).

## 5. A global consequence of [[topology/continuous-map|continuity]]

The [[real-analysis/intermediate-value-theorem|intermediate value theorem]] says that if a [[topology/continuous-map|continuous function]] \(f:[a,b]\to\mathbb R\) takes values on opposite sides of a number \(u\), then it takes the value \(u\) somewhere in the [[real-analysis/interval|interval]].

Apply the theorem to the [[real-analysis/polynomial|polynomial]] \(f(x)=x^2-2\). Since \(f(1)<0\) and \(f(2)>0\), there is \(c\in(1,2)\) with \(c^2=2\). Earlier, [[real-analysis/completeness-axiom|completeness]] produced \(\sqrt2\) as a [[real-analysis/supremum|supremum]]; now [[topology/continuous-map|continuity]] produces it as a zero. These are two manifestations of the gap-free structure of the [[shared-foundations/real-numbers|real numbers]].

## 6. Exercises

1. Prove directly from the [[real-analysis/limit-of-a-sequence|definition of convergence]] that \((2n+1)/(n+3)\to2\).
2. Prove that every [[topology/convergent-sequence|convergent sequence]] is bounded.
3. Prove that a [[shared-foundations/sequence|sequence]] has at most one limit.
4. Show directly that every [[topology/convergent-sequence|convergent sequence]] is a [[topology/cauchy-sequence|Cauchy sequence]].
5. Use the [[real-analysis/continuity-via-sequences|sequential criterion for continuity]] to prove that \(f(x)=3x-5\) is continuous.
6. Let \(f(x)=x^3+x-1\). Use the [[real-analysis/intermediate-value-theorem|intermediate value theorem]] to prove that \(f\) has a zero in \((0,1)\).
7. Identify exactly where [[real-analysis/completeness-axiom|completeness]] is used in the proof of the [[real-analysis/cauchy-criterion-in-rk|Cauchy criterion]].

## Takeaway

The [[real-analysis/supremum|least-upper-bound property]], [[real-analysis/limit-of-a-sequence|convergence]] of [[topology/cauchy-sequence|Cauchy sequences]], and preservation of limits by [[topology/continuous-map|continuous functions]] are not isolated techniques. They are different expressions of one organizing principle: the [[shared-foundations/real-numbers|real numbers]] contain the limits demanded by consistent approximation.
