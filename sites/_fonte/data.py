import json, re, html
E = html.escape
R = json.load(open('/tmp/ns/prod.json'))
ASSET = 'https://assets.sistemawbuy.com.br/arquivos/d4f5e78d4ac93ad4b60af828faff16f5/produtos/'
LOJA = 'https://www.spgrifes.com.br/'
GRUPO = 'https://sndflw.com/i/spgrifes-gruposoficial'
BLOG = 'https://blog.spgrifes.com.br/'
MAPS = 'https://maps.google.com/maps?cid=17213522362754495172'
IG = 'https://www.instagram.com/fabioleiite/'
YT = 'https://www.youtube.com/@camisas-importadas-atacado'
END = 'Rua Monsenhor Andrade, 987 – Shopping Feira da Madrugada, Piso 1, Corredor D, Loja 1202, Brás, São Paulo/SP'
HOR = 'Segunda a sábado, das 7h às 16h'
BRANDFIX = {'Casa blanca':'Casablanca','Casa Blanca':'Casablanca','Abercrombie e Fitch':'Abercrombie & Fitch','Dolce e Gabbana':'Dolce & Gabbana','Dolce & Cabbana':'Dolce & Gabbana','Hermés':'Hermès','Empório Armani':'Emporio Armani','Off White':'Off-White'}
SKIPCAT = {'Cosméticos','Feminino','Fitness'}
CATFIX = {'Gola Polo':'Polos','Shorts e Bermudas':'Shorts e bermudas','Jaquetas & Blusas de Frio':'Jaquetas e suéteres','Suéteres':'Jaquetas e suéteres','Tenis e Chuteiras':'Tênis','Camisas Sociais':'Camisas sociais','Boné':'Acessórios','Cintos':'Acessórios','Meias':'Meias e cuecas','Cuecas':'Meias e cuecas','Armani Exchange':'Camisetas'}
def img(path, w=600):
    u = path if path.startswith('http') else ASSET + path
    return 'https://i0.wp.com/' + u.replace('https://', '') + f'?w={w}'
def clean_name(n):
    n = re.sub(r'\s+', ' ', n.replace('&apos;', "'")).strip(' .')
    n = re.sub(r'\b(original|promocional|PROMOCIONAL|Original)\b', '', n, flags=re.I)
    n = re.sub(r'\s*\(\s*\)', '', n)
    return re.sub(r'\s+', ' ', n).strip(' .-/')
P = []
seen = set()
for r in R:
    if len(r) > 10:
        r = [r[0], r[1] + '|' + r[2]] + r[3:]  # nome com "A|X"
        r[1] = r[1]; r = r[:2] + r[2:]
    id_, nome, marca, cat, cat2, foto, url, est, data = r[:9]
    foto2 = r[9] if len(r) > 9 else ''
    if cat in SKIPCAT: continue
    if marca in ('[]', '') or len(marca) > 30: marca = cat2 or ''
    marca = BRANDFIX.get(marca, marca)
    if not marca: continue
    nome = clean_name(nome)
    if nome.lower() in seen: continue
    seen.add(nome.lower())
    try: est = float(est)
    except: est = 0
    P.append(dict(id=id_, n=nome, m=marca, c=CATFIX.get(cat, cat), f=foto, f2=foto2.replace(ASSET, ''), u=LOJA + url, e=est, d=data))
def utm(u, src, med='site'):
    return u + ('&' if '?' in u else '?') + f'utm_source={src}&utm_medium={med}'
# vídeos verticais (shorts) conferidos
import sys
sys.path.insert(0, '/tmp/bv')
IDS = open('/tmp/bv/ids.txt').read().split()
T = {}
exec(open('/tmp/bv/tags.py').read())
def vids(tags, n=3, avoid=()):
    out = []
    for t in tags:
        for i, tg in sorted(T.items()):
            if i < 350 and tg.split()[0] == t and 'ai' not in tg.split()[1:] and IDS[i] not in out and IDS[i] not in avoid:
                out.append(IDS[i])
                if len(out) >= n: return out
    return out
if __name__ == '__main__':
    import collections
    print(len(P)); print(collections.Counter(p['c'] for p in P).most_common()); print(collections.Counter(p['m'] for p in P).most_common(45))
