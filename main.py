import json,os,sys,urllib.request,urllib.error,time
E=os.environ;U=E.get("MAKEFUN_ENV_URL")or sys.exit();S=int(E.get("MAKEFUN_TRIAL_SEED","0"))
P=100,320,330,500,900,0;M={}
for i in range(128):
 if i&0x88==0:M[i]={}
D=[-16,-15,-17,1,16,15,17,-1,-16,-15,-17,1,16,15,17,-1]
K=[-33,-31,-18,-14,14,18,31,33]
def A(p):
 b={};f=p.split()[0].split('/');r=7
 for R in f:
  c=0
  for x in R:
   if x.isdigit():c+=int(x)
   else:
    s=r*16+c;b[s]=x;c+=1
  r-=1
 return b,1 if p.split()[1]=='w'else-1
def G(b,t):
 l=[]
 for s,p in b.items():
  if(p>'Z')==(t==-1):continue
  c=p.lower()
  if c=='p':
   d=-16*t
   if b.get(s+d)is None:
    l.append((s,s+d))
    if(s//16==(1 if t==1 else 6))and b.get(s+2*d)is None:l.append((s,s+2*d))
   for x in(-15*t,-17*t):
    if 0<=s+x<128 and(s+x)&0x88==0:
     v=b.get(s+x)
     if v and(v>'Z')==(t==1):l.append((s,s+x))
  elif c=='n':
   for d in K:
    s2=s+d
    if 0<=s2<128 and s2&0x88==0:
     v=b.get(s2)
     if not v or(v>'Z')==(t==1):l.append((s,s2))
  elif c in'bq':
   for d in(-17,-15,15,17):
    s2=s
    while 1:
     s2+=d
     if s2&0x88 or not(0<=s2<128):break
     v=b.get(s2)
     if v:
      if(v>'Z')==(t==1):l.append((s,s2))
      break
     l.append((s,s2))
  if c in'rq':
   for d in(-16,-1,1,16):
    s2=s
    while 1:
     s2+=d
     if s2&0x88 or not(0<=s2<128):break
     v=b.get(s2)
     if v:
      if(v>'Z')==(t==1):l.append((s,s2))
      break
     l.append((s,s2))
  elif c=='k':
   for d in(-17,-16,-15,-1,1,15,16,17):
    s2=s+d
    if 0<=s2<128 and s2&0x88==0:
     v=b.get(s2)
     if not v or(v>'Z')==(t==1):l.append((s,s2))
 return l
def V(b,t):
 s=0
 for q,p in b.items():
  v=P['pnbrqk'.index(p.lower())]
  s+=v if p<'a'else -v
 return s*t
def S(m,b):
 f,t=m;p=b.get(f);c=p.lower()
 if c=='p'and(t//16==0 or t//16==7):return 4
 return 0
def N(b,t):
 return len(G(b,t))==0
def C(b,t):
 for s,p in b.items():
  if p.lower()=='k'and(p<'a')==(t==1):
   for d in(-17,-15,15,17,-16,-1,1,16):
    s2=s+d
    while 0<=s2<128 and s2&0x88==0:
     v=b.get(s2)
     if v:
      if(v>'Z')==(t==-1)and v.lower()in'qrb':return True
      break
     if v:break
 return False
H={}
def U(b,t,d,a,b_,T):
 k=(tuple(sorted(b.items())),t,d)
 if k in H:return H[k]
 if d==0 or time.time()>T:return V(b,t)
 if N(b,t):return -9999*t if C(b,t)else 0
 g=G(b,t)
 g.sort(key=lambda m:(b.get(m[1],' ').lower()in'pnbrqk',-P['pnbrqk'.index(b.get(m[1],'p').lower())]if b.get(m[1])else 0))
 v=-99999
 for m in g:
  f,t_=m;p=b[f];c=b.get(t_);b[t_]=p;del b[f]
  v=max(v,-U(b,-t,d-1,-b_,-a,T))
  b[f]=p
  if c:b[t_]=c
  else:del b[t_]
  if v>=b_:break
 H[k]=v
 return v
def F(b,t,T):
 g=G(b,t)
 if not g:return None
 g.sort(key=lambda m:(b.get(m[1],' ').lower()in'pnbrqk',-P['pnbrqk'.index(b.get(m[1],'p').lower())]if b.get(m[1])else 0))
 b_,m_=-99999,g[0]
 for d in range(1,99):
  if time.time()>T:break
  for m in g:
   f,t_=m;p=b[f];c=b.get(t_);b[t_]=p;del b[f]
   v=-U(b,-t,d-1,-99999,-b_,T)
   b[f]=p
   if c:b[t_]=c
   else:del b[t_]
   if v>b_:b_,m_=v,m
 return m_
def P_(j):
 r=urllib.request.Request(U+j,data=json.dumps({}).encode(),headers={'content-type':'application/json'})
 try:return json.load(urllib.request.urlopen(r))
 except urllib.error.HTTPError as e:sys.exit(f"{j}: HTTP {e.code} {e.read().decode()}")
def M_(g,m):
 r=urllib.request.Request(U+'/move',data=json.dumps({'game':g,'move':m}).encode(),headers={'content-type':'application/json'})
 try:return json.load(urllib.request.urlopen(r))
 except urllib.error.HTTPError as e:sys.exit(f"/move: HTTP {e.code} {e.read().decode()}")
while 1:
 g=P_('/game')
 if g['status']=='done':break
 b,t=A(g['fen'])
 T=time.time()+g['move_limit_ms']/1000-0.1
 while g['status']=='your_move':
  m=F(b,t,T)
  if not m:break
  u=f"{'abcdefgh'[m[0]%16]}{8-m[0]//16}{'abcdefgh'[m[1]%16]}{8-m[1]//16}"
  g=M_(g['game'],u)
  b,t=A(g['fen'])