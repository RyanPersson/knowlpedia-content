# Linking review ledger

This ledger records the linking/dependency review on `missing-links`. It is
separate from `reviews/refactor-ledger.json`: completing this scope does not
certify every mathematical claim or prove that automated phrase discovery has
perfect recall.

- `baseline.json`: initial production discovery counts and corpus fingerprint.
- `seeds.txt`: phrases investigated below the normal frequency threshold.
- `reviews.json`: accepted, source-hash-verified snapshot for every canonical
  production entry. Future reviews append entries; the latest entry per ID wins.
- `progress.json`: counts from a fresh production audit, including containers.
- `cal_*.json`, `batch_*.json`: calibration and full-source batch reviews.
- `gap-triage-*.json`: decisions for all 768 original candidate phrase groups.
- `new-*.json`, `link-new-*.json`: new definitions and subsequent caller reviews.
- `qa-*.json`, `final-*.json`, `syntax-repairs.json`: independent checks and
  corrective follow-ups. Earlier shard hashes remain as review history and may
  be superseded; only the accepted ledger determines current coverage.
- `redirects.json`: the two legacy redirect sources, checked separately from
  canonical entries.

The first accepted snapshot consolidates the batch shards after checking each
hash against the actual source. `outcome` records the net result relative to the
baseline (new definitions count as corrected); `last_pass_outcome` preserves the
last review pass's result, and `review_batch` identifies its evidence. A later
unchanged verification does not erase an earlier correction from progress.

All 57 production containers are included in this completed review scope. The
initial baseline excluded them and counted 3,442 eligible non-container knowls;
the accepted scope also includes the 16 new definitions. Development-only and
locally composed external packages are not production review entries.

From the application repository, regenerate the audit and progress:

```sh
.venv/bin/python scripts/audit_missing_links.py \
  --content-package ../knowlpedia-content \
  --seeds ../knowlpedia-content/reviews/missing-links/seeds.txt \
  --report tmp/missing-links/current-audit.json
.venv/bin/python scripts/link_review_progress.py \
  --audit tmp/missing-links/current-audit.json \
  --ledger ../knowlpedia-content/reviews/missing-links/reviews.json \
  --include-containers \
  --report ../knowlpedia-content/reviews/missing-links/progress.json
```

A mismatched source hash returns a knowl to the remaining queue. Both blocked
and unreviewed entries remain unfinished. Full generated discovery reports stay
under the application's ignored `tmp/`; their candidate counts are not error
counts. A known phrase can be locally defined, generic, repeated, or refer to a
different mathematical sense. Ordinary expansion links and actual prerequisite
edges remain separate editorial decisions.
