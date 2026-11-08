"""Targeted content validation and exact matrix checks; not a proof of the cited theorem."""
from pathlib import Path
import hashlib, json, re, subprocess, tomllib
from fractions import Fraction as Q
root=Path(__file__).resolve().parents[2]
names=['maximal-order','quaternion-fractional-ideal','quaternion-ideal-class-set','ideal-tensor-multiplication-isomorphism']
paths=[root/'content/algebra-rings'/f'{n}.knowl.md' for n in names]
ids={}
for p in (root/'content').rglob('*.knowl.md'):
 m=tomllib.loads(p.read_text().split('+++\n',2)[1]); assert m['id'] not in ids,m['id']; ids[m['id']]=m
checks=[f'All {len(ids)} content knowls: valid TOML and unique IDs']
for p in paths:
 s=p.read_text();m=tomllib.loads(s.split('+++\n',2)[1])
 for target in re.findall(r'\[\[([^|\]]+)(?:\|[^\]]+)?\]\]',s):assert target in ids,target
 for a,b in [(r'\(',r'\)'),(r'\[',r'\]'),(r'\begin{pmatrix}',r'\end{pmatrix}')]:assert s.count(a)==s.count(b),(p,a)
 if p!=paths[-1]:
  before=subprocess.check_output(['git','show',f'HEAD:{p.relative_to(root)}'],cwd=root,text=True)
  assert m==tomllib.loads(before.split('+++\n',2)[1])
checks.append('All four proposed knowls: valid knowl links and balanced math delimiters; existing front matter unchanged')
active=set();done=set()
def visit(k):
 assert k in ids,k
 assert k not in active,f'prerequisite cycle: {k}'
 if k in done:return
 active.add(k)
 for dep in ids[k].get('prerequisites',[]):visit(dep)
 active.remove(k);done.add(k)
for k in ids:visit(k)
checks.append(f'All {len(done)} content prerequisite lists: existing targets and acyclic graph')
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def unit(i,j):return [[int((r,c)==(i,j)) for c in range(2)] for r in range(2)]
e11,e12,e21,e22=[unit(*p) for p in [(0,0),(0,1),(1,0),(1,1)]]
h=[[2,0],[0,1]];hi=[[Q(1,2),0],[0,1]]
assert mul(mul(e22,h),e22)==e22
assert mul(mul(e12,h),e21)==e11
assert mul(e12,e22)==e12
assert mul(h,hi)==[[1,0],[0,1]]
# Products of Z-bases establish JJ^{-1}=hOh^{-1} and J^{-1}J=O.
basis=[e11,e12,e21,e22]
for e in basis:
 assert any(mul(mul(h,a),mul(b,hi))==mul(mul(h,e),hi) for a in basis for b in basis)
 assert any(mul(mul(a,hi),mul(h,b))==e for a in basis for b in basis)
checks.append('Exact rational matrix checks: two displayed matrix-unit identities and both inverse-product lattice bases')
subprocess.run(['git','diff','--check'],cwd=root,check=True)
checks.append('git diff --check')
report={'base_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),'checks':checks,'source_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'limitations':['No general content compiler or site renderer is present in this checkout; rendered-page validation unavailable.','scripts/review_progress.py is absent; progress regeneration unavailable.','Mathematical review is targeted to the additions; automated checks do not prove the factorization theorem.']}
(root/'reviews/ideal-arithmetic/validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
