import json, os
from common import *

URL = 'https://asenhaoutlet.com.br/'
SRC = 'site-asenhaoutlet'
TITLE = 'A Senha Outlet: queima de estoque de moda masculina no Brás | SP Grifes'
DESC = 'Outlet da SP Grifes: jaquetas, suéteres, linho, polos e conjuntos com preço de saída. Black Friday só no site, de 23 a 30/11, comprando a partir de 1 peça.'

GR = [
 ('jaqueta', 'Frio fora de época', 'Jaquetas e suéteres que esperavam o inverno. Peça de qualidade, preço de saída.', lambda p: p['c'] == 'Jaquetas e suéteres'),
 ('linho', 'Linho de verão', 'Conjuntos, calças, bermudas e camisas de linho. Fresco, elegante e leve.', lambda p: 'linho' in p['n'].lower()),
 ('polo', 'Polos', 'Polos de piquet e poliamida, incluindo a linha Lacoste peruana.', lambda p: p['c'] == 'Polos'),
 ('conjunto', 'Conjuntos', 'Conjunto pronto: camisa e bermuda que já combinam. Um look, uma compra.', lambda p: p['c'] == 'Conjuntos' and 'linho' not in p['n'].lower()),
]
items, seen = [], set()
for k, t, d, f in GR:
    xs = sorted([p for p in P if f(p) and p['id'] not in seen], key=lambda p: -p['e'])[:12]
    for p in xs:
        seen.add(p['id']); items.append(dict(k=k, n=p['n'], m=p['m'], f=img(p['f'], 500), f2=img(p['f2'] or p['f'], 500), u=utm(p['u'], SRC, k)))
cnt = {k: sum(1 for i in items if i['k'] == k) for k, *_ in GR}
FAQ = [
 ("A Black Friday vale na loja física?", "Não. A Black Friday da SP Grifes é só no site. Na loja física do Brás os preços e as regras de atacado continuam os de sempre."),
 ("Qual a compra mínima na Black?", "De 23 a 30 de novembro dá para comprar a partir de 1 peça no site. A partir de 1º de dezembro volta o mínimo de 3 peças."),
 ("Por que essas peças estão no outlet?", "São peças boas que ficaram paradas por causa da estação ou da grade. Em vez de guardar, a gente prefere girar o estoque e trazer coleção nova."),
 ("Qual a forma de pagamento com melhor preço?", "O Pix fica com o melhor preço da promoção. No cartão há um pequeno acréscimo."),
 ("As promoções mudam durante a semana?", "Sim. As ofertas entram em ondas, um pouco por dia. Vale voltar todo dia ou entrar no Grupo VIP para ser avisado primeiro."),
]
css = '''
:root{--bg:#0b0b0c;--ink:#f5f1e8;--mut:#a7a29a;--gold:#d8b25a;--red:#e2232f;--card:#151517;--line:#26262a}
*{box-sizing:border-box;margin:0}html{scroll-behavior:smooth}body{background:var(--bg);color:var(--ink);font:16px/1.6 "Archivo",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}img{max-width:100%}.w{max-width:1160px;margin:0 auto;padding:0 20px}
h1,h2,h3{font-family:"Archivo Black","Archivo",sans-serif;letter-spacing:-.02em;line-height:1}
.bar{background:var(--red);color:#fff;text-align:center;font-weight:800;font-size:14px;padding:9px 12px;letter-spacing:.02em}
.top{position:sticky;top:0;z-index:20;background:rgba(11,11,12,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}.top .w{display:flex;align-items:center;height:60px;gap:16px}
.brand{font:900 22px "Archivo Black",sans-serif;text-decoration:none}.brand span{color:var(--gold)}.top a.go{margin-left:auto;background:var(--gold);color:#111;font-weight:800;text-decoration:none;padding:10px 16px;border-radius:10px;font-size:14px}
.hero{padding:64px 0 40px;background:radial-gradient(900px 380px at 80% 0,rgba(216,178,90,.22),transparent),radial-gradient(700px 320px at 0 100%,rgba(226,35,47,.18),transparent)}
.tag{display:inline-block;border:1px solid var(--gold);color:var(--gold);font-weight:800;font-size:12px;letter-spacing:.2em;text-transform:uppercase;padding:6px 12px;border-radius:999px}
.hero h1{font-size:clamp(46px,9vw,118px);margin:18px 0}.hero h1 em{font-style:normal;color:var(--gold)}.hero h1 b{color:var(--red)}
.hero p{font-size:19px;color:var(--mut);max-width:640px}
.clock{display:flex;gap:10px;margin-top:26px;flex-wrap:wrap}.clock div{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:12px 16px;min-width:82px;text-align:center}.clock b{display:block;font:900 34px "Archivo Black",sans-serif;color:var(--gold)}.clock span{font-size:12px;color:var(--mut);text-transform:uppercase;letter-spacing:.12em}
.clock-l{margin-top:22px;font-weight:700;color:var(--ink)}
.rules{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:36px}.rules div{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px}.rules b{display:block;font:900 26px "Archivo Black",sans-serif;color:var(--gold)}.rules p{color:var(--mut);font-size:14px;margin-top:4px}
@media(max-width:860px){.rules{grid-template-columns:1fr 1fr}}
section{padding:64px 0}.sh{margin-bottom:24px}.sh h2{font-size:clamp(32px,5vw,54px)}.sh h2 em{font-style:normal;color:var(--gold)}.sh p{color:var(--mut);margin-top:10px;max-width:640px}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:22px;position:sticky;top:60px;z-index:10;background:var(--bg);padding:12px 0}.chips button{font:700 14px "Archivo",sans-serif;background:var(--card);color:var(--ink);border:1px solid var(--line);padding:10px 14px;border-radius:999px;cursor:pointer}.chips button.on{background:var(--gold);color:#111;border-color:var(--gold)}
.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}@media(max-width:900px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
.it{background:var(--card);border:1px solid var(--line);border-radius:16px;overflow:hidden;text-decoration:none;display:block;position:relative}.it .ph{position:relative;aspect-ratio:3/4;background:#1d1d20}.it img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .3s}.it img+img{opacity:0}.it:hover img+img{opacity:1}
.it .st{position:absolute;left:10px;top:10px;background:var(--red);color:#fff;font-weight:800;font-size:11px;letter-spacing:.1em;text-transform:uppercase;padding:5px 8px;border-radius:8px;z-index:2}
.it small{display:block;padding:12px 12px 0;color:var(--gold);font-weight:800;font-size:12px;letter-spacing:.1em;text-transform:uppercase}.it b{display:block;padding:2px 12px 6px;font-weight:600;font-size:14px;line-height:1.35}.it i{display:block;padding:0 12px 14px;font-style:normal;color:var(--mut);font-size:13px;font-weight:700}
.why{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.why div{border-top:3px solid var(--gold);background:var(--card);border-radius:0 0 16px 16px;padding:20px}.why h3{font-size:22px;margin-bottom:8px}.why p{color:var(--mut);font-size:15px}
@media(max-width:860px){.why{grid-template-columns:1fr}}
.vids{display:grid;grid-template-columns:repeat(3,minmax(0,280px));gap:14px}@media(max-width:700px){.vids{grid-template-columns:repeat(2,minmax(0,1fr))}}
details{border-bottom:1px solid var(--line);padding:16px 0;max-width:860px}summary{font-weight:800;font-size:18px;cursor:pointer}details p{color:var(--mut);margin-top:8px}
.cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:26px}.btn{display:inline-flex;padding:15px 22px;border-radius:12px;font-weight:800;text-decoration:none}.b1{background:var(--gold);color:#111}.b2{border:2px solid var(--ink)}.b3{background:var(--red);color:#fff}
footer{border-top:1px solid var(--line);padding:40px 0 70px;color:var(--mut);font-size:14px}footer .w{display:grid;grid-template-columns:1.5fr 1fr;gap:24px}footer b{color:var(--ink);display:block;margin-bottom:6px}footer a{display:block;text-decoration:none;margin:4px 0}
@media(max-width:700px){footer .w{grid-template-columns:1fr}}
.dock{position:fixed;left:12px;right:12px;bottom:12px;z-index:30;display:none}.dock a{display:block;text-align:center;background:var(--gold);color:#111;font-weight:900;text-decoration:none;padding:15px;border-radius:14px;box-shadow:0 10px 30px rgba(0,0,0,.5)}
@media(max-width:700px){.dock{display:block}}
''' + VCSS
chips = '<button class="on" data-k="*">Tudo (' + str(len(items)) + ')</button>' + ''.join(f'<button data-k="{k}">{E(t)} ({cnt[k]})</button>' for k, t, *_ in GR if cnt[k])
grid = ''.join(f'<a class="it" data-k="{i["k"]}" href="{i["u"]}" target="_blank" rel="noopener"><div class="ph"><span class="st">Outlet</span><img src="{i["f"]}" alt="{E(i["n"])} – outlet SP Grifes" loading="lazy" width="500" height="667"><img src="{i["f2"]}" alt="" loading="lazy" width="500" height="667"></div><small>{E(i["m"])}</small><b>{E(i["n"])}</b><i>Ver na loja online →</i></a>' for i in items)
why = ''.join(f'<div><h3>{E(t)}</h3><p>{E(d)}</p></div>' for k, t, d, f in GR if cnt[k])
vh = vcard(IDS[2], 'SP Grifes no Brás') + vcard(IDS[27], 'Novidades da loja') + vcard(IDS[39], 'Peças da SP Grifes')
faq = ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in FAQ)
il = '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"ItemList","name":"A Senha Outlet – SP Grifes","itemListElement":[{"@type":"ListItem","position":n+1,"name":i['n'],"url":i['u'].split('?')[0]} for n, i in enumerate(items)]}, ensure_ascii=False) + '</script>'
page = head(TITLE, DESC, URL, items[0]['f'], 'family=Archivo:wght@400;600;700;800&family=Archivo+Black') + f'''
<style>{css}</style>{faq_ld(FAQ)}{store_ld(URL, 'A Senha Outlet')}{il}</head><body>
<div class="bar">Black Friday só no site · de 23 a 30/11 · compra a partir de 1 peça</div>
<header class="top"><div class="w"><a class="brand" href="#">A Senha <span>Outlet</span></a><a class="go" href="{utm(LOJA, SRC, 'topo')}" target="_blank" rel="noopener">Ver na loja online</a></div></header>
<main>
<div class="hero"><div class="w"><span class="tag">Outlet SP Grifes · Brás</span><h1>A senha é <em>girar</em> o estoque. <b>Você ganha.</b></h1><p>Peças boas que ficaram paradas por causa da estação ou da grade, com preço de saída. Jaqueta fora de época, linho, polos e conjuntos, direto da SP Grifes, há 10 anos no Brás.</p>
<p class="clock-l" id="cl-l">A Black Friday do site começa em:</p><div class="clock" id="clock"><div><b id="d">0</b><span>dias</span></div><div><b id="h">0</b><span>horas</span></div><div><b id="m">0</b><span>min</span></div><div><b id="s">0</b><span>seg</span></div></div>
<div class="rules"><div><b>1 peça</b><p>Compra mínima no site de 23 a 30/11</p></div><div><b>Só no site</b><p>A Black não vale na loja física</p></div><div><b>Pix</b><p>Fica com o melhor preço</p></div><div><b>Ondas</b><p>Ofertas novas entram todo dia</p></div></div></div></div>
<section id="pecas"><div class="w"><div class="sh"><h2>Peças do <em>outlet</em></h2><p>Toque na peça para ver preço, cores e tamanhos na loja online.</p></div><div class="chips" id="chips">{chips}</div><div class="grid" id="grid">{grid}</div></div></section>
<section style="background:#111113"><div class="w"><div class="sh"><h2>Por que essas peças estão <em>aqui</em></h2></div><div class="why">{why}</div></div></section>
<section><div class="w"><div class="sh"><h2>Veja a loja <em>por dentro</em></h2></div><div class="vids">{vh}</div></div></section>
<section style="background:#111113"><div class="w"><div class="sh"><h2>Perguntas da <em>Black</em></h2></div>{faq}
<div class="cta"><a class="btn b1" href="{utm(LOJA, SRC, 'final')}" target="_blank" rel="noopener">Ver na loja online</a><a class="btn b3" href="{GRUPO}" target="_blank" rel="noopener">Entrar no Grupo VIP</a><a class="btn b2" href="{wa_share('Olha esse outlet de moda masculina do Brás: ' + URL)}" target="_blank" rel="noopener">Mandar para um amigo</a></div></div></section>
</main>
<footer><div class="w"><div><b>A Senha Outlet · SP Grifes</b>Outlet de moda masculina da SP Grifes. {E(END)}. {HOR}.</div><div><b>SP Grifes</b><a href="{utm(LOJA, SRC, 'rodape')}" target="_blank" rel="noopener">Loja online</a><a href="{IG}" target="_blank" rel="noopener">Instagram</a><a href="{MAPS}" target="_blank" rel="noopener">Como chegar</a></div></div></footer>
<div class="dock"><a href="{utm(LOJA, SRC, 'dock')}" target="_blank" rel="noopener">Ver na loja online</a></div>
<script>(function(){{var A=new Date('2026-11-23T00:00:00-03:00'),B=new Date('2026-12-01T00:00:00-03:00');function t(){{var n=new Date(),alvo=n<A?A:B,l=document.getElementById('cl-l');if(n>=B){{document.getElementById('clock').style.display='none';l.textContent='A Black Friday terminou. O outlet continua no site.';return}}l.textContent=n<A?'A Black Friday do site começa em:':'A Black Friday do site termina em:';var s=Math.max(0,Math.floor((alvo-n)/1000));document.getElementById('d').textContent=Math.floor(s/86400);document.getElementById('h').textContent=Math.floor(s%86400/3600);document.getElementById('m').textContent=Math.floor(s%3600/60);document.getElementById('s').textContent=s%60}}t();setInterval(t,1000);
document.querySelectorAll('#chips button').forEach(function(b){{b.onclick=function(){{document.querySelectorAll('#chips button').forEach(function(x){{x.classList.toggle('on',x===b)}});document.querySelectorAll('#grid .it').forEach(function(i){{i.style.display=(b.dataset.k==='*'||i.dataset.k===b.dataset.k)?'':'none'}})}}}})}})();</script>{VID_JS}</body></html>'''
os.makedirs('/home/claude/rh/sites/outlet', exist_ok=True)
open('/home/claude/rh/sites/outlet/index.html', 'w').write(page)
print(len(items), cnt)
