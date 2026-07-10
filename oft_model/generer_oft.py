#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generer_oft.py - Genere un modele Outlook (.oft) a partir d'un fichier HTML d'emailing.

Methode validee : le corps est stocke en HTML (PR_HTML) et chaque image referencee
en chemin relatif (src="images/...") est INTEGREE directement dans le HTML en base64
(data:image/...). Resultat : un .oft dont le corps s'affiche mis en forme, avec les
visuels, et SANS aucune piece jointe (le fichier n'en contient aucune).

USAGE
    python generer_oft.py <entree.html> <sortie.oft> [--subject "Objet"] [--txt corps.txt]

EXEMPLE
    python generer_oft.py ..\\pmr_brief_rentree\\fontLocale\\pmr_brief_rentree.html ..\\pmr_brief_rentree\\fontLocale\\pmr_brief_rentree.oft

UTILISATION DU .OFT
    Importer le fichier dans Outlook via "Mes modeles".

LIMITE (envoi reel)
    Les images sont en base64 dans le HTML : parfait pour l'affichage et la
    previsualisation, mais certains clients (Gmail, Outlook classique) bloquent les
    images base64 a la reception. Pour un envoi de masse, utiliser la version HTML
    avec images hebergees (routeur d'emailing).
"""
import os, re, struct, base64, argparse

PT_LONG=0x0003; PT_BOOL=0x000B; PT_SYSTIME=0x0040; PT_STRING=0x001F; PT_BINARY=0x0102
NOSTREAM=0xFFFFFFFF; ENDOFCHAIN=0xFFFFFFFE; FATSECT=0xFFFFFFFD; FREESECT=0xFFFFFFFF
SECSZ=512; MINISZ=64; MINICUTOFF=4096

class Prop:
    __slots__=('tag','flags','ptype','value','data')
    def __init__(self,tag,flags,value=None,data=None):
        self.tag=tag; self.flags=flags; self.ptype=tag&0xFFFF; self.value=value; self.data=data
def us(s): return s.encode('utf-16-le')
def psn(tag): return '__substg1.0_%08X'%tag

def build_props_stream(props, toplevel, attach_count=0, recip_count=0):
    out=bytearray()
    if toplevel:
        out+=b'\x00'*8
        out+=struct.pack('<I',recip_count)+struct.pack('<I',attach_count)
        out+=struct.pack('<I',recip_count)+struct.pack('<I',attach_count)+b'\x00'*8
    else: out+=b'\x00'*8
    for p in props:
        out+=struct.pack('<I',p.tag)+struct.pack('<I',p.flags)
        if p.ptype in (PT_STRING,0x001E,PT_BINARY):
            raw=p.data or b''
            out+=struct.pack('<I',len(raw)+(2 if p.ptype in (PT_STRING,0x001E) else 0))+b'\x00'*4
        elif p.ptype==PT_BOOL: out+=struct.pack('<H',1 if p.value else 0)+b'\x00'*6
        elif p.ptype==PT_LONG:  out+=struct.pack('<I',p.value & 0xFFFFFFFF)+b'\x00'*4
        elif p.ptype==PT_SYSTIME:out+=struct.pack('<Q',p.value)
        else: out+=b'\x00'*8
    return bytes(out)

class Ent:
    def __init__(self,name,etype):
        self.name=name; self.etype=etype; self.data=b''; self.children=[]; self.clsid=b'\x00'*16
        self.idx=-1; self.left=NOSTREAM; self.right=NOSTREAM; self.child=NOSTREAM
        self.color=1; self.start=ENDOFCHAIN; self.size=0
def cmp_key(name): return (len(name), name.upper().encode('utf-16-le'))
def build_rb(children):
    order=sorted(range(len(children)), key=lambda i: cmp_key(children[i].name))
    def build(lo,hi):
        if lo>hi: return NOSTREAM
        mid=(lo+hi)//2; node=children[order[mid]]
        node.left=build(lo,mid-1); node.right=build(mid+1,hi); return node.idx
    return build(0,len(children)-1)

def serialize_cfb(root):
    entries=[]
    def collect(e):
        e.idx=len(entries); entries.append(e)
        for c in e.children: collect(c)
    collect(root)
    for e in entries: e.child=build_rb(e.children) if e.children else NOSTREAM
    sectors=[]; fat=[]
    def alloc(data):
        if len(data)==0: return ENDOFCHAIN
        n=(len(data)+SECSZ-1)//SECSZ; start=len(sectors)
        for i in range(n):
            c=data[i*SECSZ:(i+1)*SECSZ]; sectors.append(c+b'\x00'*(SECSZ-len(c))); fat.append(start+i+1)
        fat[-1]=ENDOFCHAIN; return start
    for e in entries:
        if e.etype==2 and len(e.data)>=MINICUTOFF: e.start=alloc(e.data); e.size=len(e.data)
    mini=bytearray(); minifat=[]
    for e in entries:
        if e.etype==2 and 0<len(e.data)<MINICUTOFF:
            nm=(len(e.data)+MINISZ-1)//MINISZ; e.start=len(minifat); e.size=len(e.data)
            mini+=e.data+b'\x00'*(nm*MINISZ-len(e.data))
            for i in range(nm): minifat.append(e.start+i+1)
            minifat[-1]=ENDOFCHAIN
        elif e.etype==2 and len(e.data)==0: e.start=ENDOFCHAIN; e.size=0
    root.size=len(mini); root.start=alloc(bytes(mini)) if mini else ENDOFCHAIN
    def deb(e):
        nm=(e.name.encode('utf-16-le')+b'\x00\x00')[:64]; b=bytearray(128); b[0:len(nm)]=nm
        struct.pack_into('<H',b,64,len(nm)); b[66]=e.etype; b[67]=e.color
        struct.pack_into('<I',b,68,e.left & 0xFFFFFFFF); struct.pack_into('<I',b,72,e.right & 0xFFFFFFFF)
        struct.pack_into('<I',b,76,e.child & 0xFFFFFFFF); b[80:96]=e.clsid
        struct.pack_into('<I',b,116,e.start & 0xFFFFFFFF); struct.pack_into('<Q',b,120,e.size); return bytes(b)
    dirb=bytearray()
    for e in entries: dirb+=deb(e)
    while len(dirb)%SECSZ!=0:
        fb=bytearray(128)
        for o in (68,72,76): struct.pack_into('<I',fb,o,NOSTREAM)
        dirb+=fb
    dir_start=alloc(bytes(dirb))
    if minifat:
        mfb=bytearray()
        for v in minifat: mfb+=struct.pack('<I',v)
        while len(mfb)%SECSZ!=0: mfb+=struct.pack('<I',FREESECT)
        mf_start=alloc(bytes(mfb)); mf_count=len(mfb)//SECSZ
    else: mf_start=ENDOFCHAIN; mf_count=0
    ds=len(sectors); fc=1
    while True:
        need=((ds+fc)*4+SECSZ-1)//SECSZ
        if need<=fc: fc=need; break
        fc=need
    fstart=len(sectors)
    for i in range(fc): sectors.append(b''); fat.append(FATSECT)
    fa=fat[:]
    while len(fa)%(SECSZ//4)!=0: fa.append(FREESECT)
    fatb=bytearray()
    for v in fa: fatb+=struct.pack('<I',v & 0xFFFFFFFF)
    for i in range(fc): sectors[fstart+i]=bytes(fatb[i*SECSZ:(i+1)*SECSZ])
    h=bytearray(512); h[0:8]=b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1'
    struct.pack_into('<H',h,24,0x003E); struct.pack_into('<H',h,26,0x0003)
    struct.pack_into('<H',h,28,0xFFFE); struct.pack_into('<H',h,30,9); struct.pack_into('<H',h,32,6)
    struct.pack_into('<I',h,40,0); struct.pack_into('<I',h,44,fc)
    struct.pack_into('<I',h,48,dir_start); struct.pack_into('<I',h,56,MINICUTOFF)
    struct.pack_into('<I',h,60,mf_start); struct.pack_into('<I',h,64,mf_count)
    struct.pack_into('<I',h,68,ENDOFCHAIN); struct.pack_into('<I',h,72,0)
    for i in range(109):
        v=(fstart+i) if i<fc else FREESECT
        struct.pack_into('<I',h,76+i*4,v & 0xFFFFFFFF)
    return bytes(h)+b''.join(sectors)

def _mime(fn):
    fn=fn.lower()
    if fn.endswith('.png'): return 'image/png'
    if fn.endswith(('.jpg','.jpeg')): return 'image/jpeg'
    if fn.endswith('.gif'): return 'image/gif'
    return 'application/octet-stream'

def make_oft(html_path, out_path, subject=None, txt_path=None):
    html=open(html_path,encoding='utf-8',errors='replace').read()
    if subject is None:
        m=re.search(r'<title>(.*?)</title>', html, re.S|re.I)
        subject=re.sub(r'\s+',' ',(m.group(1) if m else 'Sans objet')).strip()
        import html as _h; subject=_h.unescape(subject)
    base=os.path.dirname(os.path.abspath(html_path)); n=[0]
    def repl(m):
        s=m.group(1)
        if s.lower().startswith(('http:','https:','cid:','data:')): return m.group(0)
        p=os.path.join(base, s.replace('/',os.sep))
        if not os.path.exists(p): print('  !! image introuvable:',s); return m.group(0)
        b=base64.b64encode(open(p,'rb').read()).decode('ascii'); n[0]+=1
        return 'src="data:%s;base64,%s"'%(_mime(os.path.basename(s)), b)
    html_bytes=re.sub(r'src\s*=\s*"([^"]+)"', repl, html).encode('utf-8')
    plain=''
    if txt_path and os.path.exists(txt_path): plain=open(txt_path,encoding='utf-8',errors='replace').read()
    sb=us(subject)
    tp=[Prop(0x0E070003,6,value=8),Prop(0x00170003,6,value=1),Prop(0x00360003,6,value=0),
        Prop(0x001A001F,6,data=us('IPM.Note')),Prop(0x0037001F,6,data=sb),
        Prop(0x0E1D001F,6,data=sb),Prop(0x0070001F,6,data=sb),
        Prop(0x1000001F,6,data=us(plain)),Prop(0x10130102,6,data=html_bytes),
        Prop(0x3FDE0003,6,value=65001),Prop(0x3FF10003,6,value=1036),
        Prop(0x30070040,2,value=0),Prop(0x30080040,2,value=0)]
    root=Ent('Root Entry',5); root.clsid=bytes.fromhex('0b0d020000000000c000000000000046')
    for p in tp:
        if p.data is not None:
            st=Ent(psn(p.tag),2); st.data=p.data; root.children.append(st)
    nameid=Ent('__nameid_version1.0',1)
    for nm in ('__substg1.0_00020102','__substg1.0_00030102','__substg1.0_00040102'):
        st=Ent(nm,2); st.data=b''; nameid.children.append(st)
    root.children.append(nameid)
    ps=Ent('__properties_version1.0',2); ps.data=build_props_stream(tp,True,attach_count=0)
    root.children.append(ps)
    open(out_path,'wb').write(serialize_cfb(root))
    print('  OK ->',out_path,'(%d images integrees en base64, 0 piece jointe)'%n[0])

if __name__=='__main__':
    ap=argparse.ArgumentParser(description="Genere un .oft Outlook (corps HTML, images base64, sans piece jointe).")
    ap.add_argument('html'); ap.add_argument('oft')
    ap.add_argument('--subject', default=None); ap.add_argument('--txt', default=None)
    a=ap.parse_args(); make_oft(a.html, a.oft, a.subject, a.txt)
