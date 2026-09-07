# Axiomatic dependency review

Work branch: `dependency-structure`. Baseline: `develop` at `34087053`.

This is a new semantic pass, separate from the earlier missing-link review.
A current review requires an individual finding and a SHA-256 matching the
source being served. A graph audit does not certify mathematical correctness.
Conjectures from the separate catalog are excluded from this corpus count.

Run the application repository's `scripts/dependency_review_progress.py` to
regenerate `progress.json`. Duplicate reviews count once. Redirects are retired
IDs, not additional knowls. Records under `triage_records` are preliminary
candidates, not completed reviews. A later source edit makes an old review stale.

The first batch repairs topology, linear algebra, probability/measure theory,
Lie theory, operators, and the local-curvature transformation ancestry. It adds
missing topology/homology definitions and consolidates four duplicate topology
theorems with redirects and updated internal links.

`graph-audit.json` records structural validation. `graph-metrics.json` records
the longest chain and local-curvature ancestry after the batch. Shorter chains
are a consequence of removing false dependencies, not an optimization target.
Definitions of objects appearing in theorem conclusions still count as
prerequisites; theorems about later applications do not. Explicit proof
ingredients may be prerequisites even when unnecessary for parsing the statement.

Gauge theory remains in fiber-bundles: its principal bundles, connections and
curvature form a coherent mathematical cluster. A future navigation grouping
could make it easier to browse without introducing a second subject hierarchy.

The remaining corpus is not certified by this pass. In particular, the geometry
triage queue must receive full source/target review before it is counted.
