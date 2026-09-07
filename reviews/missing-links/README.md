# Linking review ledger

This is a new review scope on the `missing-links` branch. Previous full-math
and prerequisite reviews remain in `reviews/refactor-ledger.json`; they do not
establish exhaustive phrase-link coverage.

- `baseline.json`: initial production discovery counts and corpus fingerprint.
- `seeds.txt`: explicit phrases to investigate even below the frequency threshold.
- `reviews.json`: append-only completed/blocked linking reviews; initially empty.

The application repository owns `docs/missing-links-roadmap.md` and the audit
and progress scripts. Follow its stages and review-entry convention. The first
baseline covers 3,442 eligible production knowls; none are yet counted as
reviewed in this new scope. Generated full candidate reports remain in the
application's ignored `tmp/missing-links/` directory and can be regenerated.

Do not create knowls solely because their phrases appear in the gap queue.
For example, “tensor product” can point to the existing “Tensor product of
modules” depending on context. Check related-target suggestions and read the
source and target definitions before deciding. Ordinary links and mathematical
prerequisites are separate editorial decisions.
