"""Targeted checks using the matrices and component equations in the knowl sources."""
from pathlib import Path
import re, tomllib, json, hashlib, subprocess
root=Path(__file__).resolve().parents[2]
paths=[root/'content/mathematical-physics'/f'{n}.knowl.md' for n in ('gamma-matrices','dirac-equation')]
g,d=[p.read_text() for p in paths]
checks=[]
def passed(s): checks.append(s)
def matrix(s): return [r.split('&') for r in s.strip().split(r'\\')]
def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(c,a): return [[c*x for x in r] for r in a]
def mul(a,b): return [[sum(x*y for x,y in zip(r,col)) for col in zip(*b)] for r in a]
def eye(n): return [[int(j==k) for k in range(n)] for j in range(n)]
def numeric(s): return complex(s.strip().replace('i','j').replace('-j','-1j')) if s.strip() not in ('i','-i') else (1j if s.strip()=='i' else -1j)
blocks=re.findall(r'\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}',g,re.S)
pauli=[[[numeric(x) for x in r] for r in matrix(b)] for b in blocks[:3]]
gammas=[[[numeric(x) for x in r] for r in matrix(b)] for b in blocks if len(matrix(b))==4]
assert len(gammas)==4
for j in range(3):
 for k in range(3): assert add(mul(pauli[j],pauli[k]),mul(pauli[k],pauli[j]))==scale(2*int(j==k),eye(2))
for j in range(3): assert mul(pauli[j],pauli[(j+1)%3])==scale(1j,pauli[(j+2)%3])
passed('Pauli squares, all 9 anticommutators, and 3 cyclic products')
for mu in range(4):
 for nu in range(4):
  assert add(mul(gammas[mu],gammas[nu]),mul(gammas[nu],gammas[mu]))==scale((2 if mu==0 else -2)*int(mu==nu),eye(4))
passed('All 16 Clifford anticommutators, using the displayed 4x4 matrices')
assert mul(gammas[1],gammas[2])==[[(-1j,1j,-1j,1j)[j]*int(j==k) for k in range(4)] for j in range(4)]
passed('gamma^1 gamma^2 = diag(-i,i,-i,i)')
operator=matrix(re.findall(r'\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}',d,re.S)[1])
assert len(operator)==4 and all(len(r)==4 for r in operator)
eqs=re.findall(r'\\\[\s*(.*?)\s*\\\]',d,re.S)
# The last row ends with a period; all four displays have '=0' followed by punctuation.
rows=[re.sub(r'=0[,.]$','',x.replace('\n','')) for x in eqs if r'\psi_' in x and r'\begin' not in x and re.search(r'=0[,.]$',x)]
assert len(rows)==4

def evaluate(s,ds,m,vs=None):
 s=s.replace('\n','').replace(' ','')
 for j in range(4): s=s.replace(r'\partial_'+str(j),f'd{j}')
 for j in range(1,5): s=s.replace(r'\psi_'+str(j),f'*v{j}')
 s=re.sub(r'i(?=d)', '1j*', s)
 s=s.replace('i','1j') if 'i' in s else s
 env={f'd{j}':ds[j] for j in range(4)}|{'m':m}
 if vs is not None: env|={f'v{j+1}':vs[j] for j in range(4)}
 assert re.fullmatch(r'[0-9jdvm+*()\-]+',s),s
 return eval(s,{'__builtins__':{}},env)
# Linear coefficients: four independent derivative symbols and mass.
for a in range(5):
 ds=[int(a==j) for j in range(4)]; m=int(a==4)
 actual=[[evaluate(x,ds,m) for x in row] for row in operator]
 expected=scale(-m,eye(4))
 for j in range(4): expected=add(expected,scale(1j*ds[j],gammas[j]))
 assert actual==expected
 for k in range(4):
  vs=[int(j==k) for j in range(4)]
  assert [evaluate(s,ds,m,vs) for s in rows]==[r[k] for r in expected]
passed('All derivative/mass coefficients in the displayed operator and four component equations')
# Compare every quadratic coefficient of commuting derivative symbols.
for j in range(4):
 assert mul(gammas[j],gammas[j])==scale(1 if j==0 else -1,eye(4))
 for k in range(j): assert add(mul(gammas[j],gammas[k]),mul(gammas[k],gammas[j]))==scale(0,eye(4))
passed('D_M squared equals (partial_0^2 - sum_j partial_j^2) I_4; conjugate-factor mass terms cancel')
ids={}
for p in (root/'content').rglob('*.knowl.md'):
 parts=p.read_text().split('+++\n',2)
 try: meta=tomllib.loads(parts[1])
 except Exception as e: raise AssertionError(f'{p}: {e}')
 assert meta['id'] not in ids,meta['id']
 ids[meta['id']]=meta
passed(f'All {len(ids)} content knowls: valid TOML and unique IDs')
for p,s in zip(paths,(g,d)):
 meta=tomllib.loads(s.split('+++\n',2)[1])
 original=subprocess.check_output(['git','show',f'HEAD:{p.relative_to(root)}'],cwd=root,text=True)
 assert meta==tomllib.loads(original.split('+++\n',2)[1])
 for target in re.findall(r'\[\[([^|\]]+)(?:\|[^\]]+)?\]\]',s): assert target in ids,target
 for target in meta.get('prerequisites',[]): assert target in ids,target
 for start,end in [(r'\[',r'\]'),(r'\(',r'\)')]: assert s.count(start)==s.count(end)
 for env in ('pmatrix',): assert s.count(r'\begin{'+env+'}')==s.count(r'\end{'+env+'}')
passed('Both edited knowls: unchanged metadata, valid link/prerequisite targets, balanced math delimiters and matrix environments')
# Prerequisite lists are unchanged; check reachability from these two entries.
active=set(); done=set()
def visit(key):
 assert key not in active, f'cycle through {key}'
 if key in done:return
 active.add(key)
 for dep in ids[key].get('prerequisites',[]): visit(dep)
 active.remove(key);done.add(key)
for p in paths:visit(tomllib.loads(p.read_text().split('+++\n',2)[1])['id'])
passed(f'Prerequisite closure of edited entries is acyclic ({len(done)} knowls)')
subprocess.run(['git','diff','--check'],cwd=root,check=True)
passed('git diff --check')
report={'base_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),'checks':checks,'source_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'limitations':['Repository contains no executable content validator, compiler, or scripts/review_progress.py; full site/render validation and progress regeneration unavailable.']}
(root/'reviews/dirac-representation/validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
