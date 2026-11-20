import json, collections
from common import *

URL = 'https://spgrifes.github.io/Rh/sites/catalogo/'
SRC = 'site-catalogo'
TITLE = f'Catálogo SP Grifes: {len(P)} peças masculinas de grife com estoque hoje | Brás'
DESC = 'Catálogo atualizado da SP Grifes: camisetas, polos, shorts, conjuntos e acessórios de grife com estoque. Filtre por marca e tipo de peça e veja cores e tamanhos na loja online.'
CATS = [c for c, n in collections.Counter(p['c'] for p in P).most_common()]
BRANDS = sorted({p['m'] for p in P}, key=lambda s: s.lower())
COVER = {}
for c in CATS:
    xs = sorted([p for p in P if p['c'] == c], key=lambda p: -p['e'])
    COVER[c] = xs[0]
DATA = [[p['n'], p['m'], CATS.index(p['c']), p['f'], p['f2'], p['u'].replace(LOJA, ''), p['d'].replace('-', ''), int(p['e'])] for p in P]
N = len(P)
FAQ = [
 ("As peças do catálogo estão disponíveis?", "Este catálogo é montado com as peças que têm estoque na loja online da SP Grifes. As cores e os tamanhos de cada uma ficam na página do produto, que é atualizada na hora."),
 ("Como compro uma peça do catálogo?", "Toque na peça e depois em Ver na loja online. Lá você escolhe cor e tamanho e finaliza a compra, com envio para todo o Brasil."),
 ("Tem preço de atacado?", "Sim. Na loja online o atacado vale a partir de 3 peças, misturando modelos. Na loja física, no Brás, a partir de 6 peças."),
 ("Posso ver as peças pessoalmente?", "Pode. A loja física fica no Shopping Feira da Madrugada, Piso 1, Corredor D, Loja 1202, no Brás, de segunda a sábado, das 7h às 16h."),
]
css = '''
:root{--bg:#f4f2ee;--ink:#141414;--mut:#6d6a64;--line:#dedad2;--card:#fff;--acc:#b2271f}
*{box-sizing:border-box;margin:0}body{background:var(--bg);color:var(--ink);font:16px/1.55 "Manrope",Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}a{color:inherit}img{max-width:100%}
h1,h2{font-family:"Bodoni Moda",Didot,Georgia,serif;font-weight:600;letter-spacing:-.01em;line-height:1}
.w{max-width:1280px;margin:0 auto;padding:0 20px}
.mast{padding:26px 0 0}.mast .w{display:flex;align-items:center;gap:16px}.mast img{height:44px;width:auto}.mast a.lo{margin-left:auto;font-weight:800;font-size:14px;text-decoration:none;border-bottom:2px solid var(--acc);padding-bottom:2px}
.cover{padding:30px 0 10px}.cover h1{font-size:clamp(54px,11vw,150px)}.cover h1 em{font-style:italic;color:var(--acc)}
.cover .meta{display:flex;flex-wrap:wrap;gap:22px;align-items:end;justify-content:space-between;border-top:2px solid var(--ink);margin-top:18px;padding-top:14px}
.cover p{max-width:560px;color:var(--mut);font-size:17px}.cover b.big{font:600 46px "Bodoni Moda",serif}
.cats{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin:30px 0 8px}.cat{position:relative;overflow:hidden;border:0;padding:0;cursor:pointer;background:#ddd;aspect-ratio:4/5;text-align:left}
.cat img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s}.cat:hover img{transform:scale(1.06)}.cat span{position:absolute;left:0;right:0;bottom:0;padding:30px 12px 10px;background:linear-gradient(transparent,rgba(0,0,0,.75));color:#fff;font-weight:800;font-size:15px}.cat span small{display:block;font-weight:600;opacity:.8;font-size:12px}
.cat.on{outline:3px solid var(--acc);outline-offset:-3px}
@media(max-width:900px){.cats{grid-template-columns:repeat(5,40%);overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:6px}.cat{scroll-snap-align:start}}
.bar{position:sticky;top:0;z-index:20;background:rgba(244,242,238,.96);backdrop-filter:blur(8px);border-bottom:1px solid var(--line);padding:12px 0}
.bar .w{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.bar input,.bar select{font:600 15px Manrope,sans-serif;padding:12px 14px;border:1.5px solid var(--ink);background:#fff;border-radius:0;color:var(--ink)}.bar input{flex:1 1 240px}
.bar .n{font-weight:800;font-size:14px;margin-left:auto}.bar button{font:700 14px Manrope,sans-serif;padding:12px 14px;border:1.5px solid var(--ink);background:transparent;cursor:pointer}
.grid{display:grid;grid-template-columns:repeat(5,1fr);gap:22px 14px;padding:24px 0 40px}
.it{cursor:pointer;background:none;border:0;padding:0;text-align:left;font:inherit;color:inherit}.it .ph{aspect-ratio:3/4;background:#e7e3db;overflow:hidden;position:relative}
.it img{width:100%;height:100%;object-fit:cover;display:block;transition:opacity .4s}.it img.b{position:absolute;inset:0;opacity:0}.it:hover img.b{opacity:1}
.it small{display:block;margin-top:10px;font-size:11px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--acc)}.it b{display:block;font-weight:600;font-size:14px;line-height:1.35;margin-top:3px}
.it .nv{position:absolute;top:8px;left:8px;background:var(--ink);color:#fff;font-size:11px;font-weight:800;letter-spacing:.1em;padding:4px 8px}
@media(max-width:1000px){.grid{grid-template-columns:repeat(3,1fr)}}@media(max-width:640px){.grid{grid-template-columns:repeat(2,1fr);gap:18px 10px}}
.more{display:block;margin:0 auto 60px;font:800 15px Manrope,sans-serif;padding:16px 28px;border:2px solid var(--ink);background:transparent;cursor:pointer}
.empty{padding:50px 0;text-align:center;color:var(--mut);display:none}
.md{position:fixed;inset:0;z-index:50;background:rgba(20,20,20,.86);display:none;align-items:center;justify-content:center;padding:16px}.md.on{display:flex}
.box{background:var(--bg);max-width:860px;width:100%;display:grid;grid-template-columns:1.05fr 1fr;max-height:92vh;overflow:auto}
.box .gl{display:grid;grid-template-columns:1fr;gap:4px;background:#e7e3db}.box .gl img{width:100%;aspect-ratio:3/4;object-fit:cover;display:block}
.box .tx{padding:28px}.box small{font-size:12px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--acc)}.box h2{font-size:30px;margin:8px 0 14px;line-height:1.1}.box p{color:var(--mut);font-size:15px;margin-bottom:16px}
.btn{display:block;text-align:center;padding:16px;font-weight:800;text-decoration:none;margin-top:10px;border:2px solid var(--ink)}.b1{background:var(--ink);color:#fff}.b2{background:transparent}
.x{position:fixed;top:12px;right:16px;font-size:36px;color:#fff;background:none;border:0;cursor:pointer;z-index:51}
@media(max-width:700px){.box{grid-template-columns:1fr}.box .gl{grid-template-columns:1fr 1fr}}
.info{border-top:2px solid var(--ink);padding:40px 0 30px;display:grid;grid-template-columns:1fr 1fr;gap:30px}.info h2{font-size:38px;margin-bottom:14px}
details{border-bottom:1px solid var(--line);padding:14px 0}summary{font-weight:800;cursor:pointer}details p{color:var(--mut);margin-top:8px}
@media(max-width:800px){.info{grid-template-columns:1fr}}
footer{padding:28px 0 90px;color:var(--mut);font-size:14px;border-top:1px solid var(--line)}footer a{margin-right:16px}
.dock{display:none;position:fixed;left:50%;bottom:14px;transform:translateX(-50%);z-index:30;background:var(--ink);padding:6px;border-radius:999px;gap:6px}.dock a{color:#fff;text-decoration:none;font-weight:800;font-size:13px;padding:10px 15px;border-radius:999px}.dock .l{background:var(--acc)}
@media(max-width:760px){.dock{display:flex}}
'''
cats_html = ''.join(f'<button class="cat" data-c="{i}"><img src="{img(COVER[c]["f"],500)}" alt="{E(c)} masculinas de grife – SP Grifes" loading="{"eager" if i<5 else "lazy"}" width="500" height="625"><span>{E(c)}<small>{sum(1 for p in P if p["c"]==c)} peças</small></span></button>' for i, c in enumerate(CATS))
opts = '<option value="">Todas as grifes</option>' + ''.join(f'<option>{E(b)}</option>' for b in BRANDS)
faq = ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in FAQ)
itemlist = '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"ItemList","name":"Catálogo SP Grifes","numberOfItems":N,"itemListElement":[{"@type":"ListItem","position":i+1,"url":p['u'],"name":p['n']} for i,p in enumerate(P[:60])]}, ensure_ascii=False) + '</script>'
ASSETB = ASSET
page = head(TITLE, DESC, URL, img(P[0]['f'], 1200), 'family=Bodoni+Moda:ital,opsz,wght@0,6..96,600;1,6..96,600&family=Manrope:wght@500;600;700;800') + f'''
<style>{css}</style>{faq_ld(FAQ)}{itemlist}{store_ld(URL, 'Catálogo SP Grifes')}</head><body>
<div class="mast"><div class="w"><img src="../img/logo-sp-grifes-colorido.png" alt="SP Grifes – moda masculina importada no Brás" width="140" height="87"><a class="lo" href="{utm(LOJA, SRC, 'topo')}" target="_blank" rel="noopener">Loja online →</a></div></div>
<header class="cover"><div class="w"><h1>Catálogo<br><em>de grifes.</em></h1>
<div class="meta"><p>Todas as peças masculinas com estoque na SP Grifes, num lugar só. Escolha o tipo, filtre pela marca e toque para ver de perto. Cores e tamanhos ficam na loja online.</p><div><b class="big">{N}</b><br><span style="color:var(--mut);font-weight:700">peças hoje · {len(BRANDS)} grifes</span></div></div>
<div class="cats">{cats_html}</div></div></header>
<div class="bar"><div class="w"><input id="q" type="search" placeholder="Buscar: polo, Lacoste, tactel…" aria-label="Buscar no catálogo"><select id="m" aria-label="Grife">{opts}</select><select id="o" aria-label="Ordenar"><option value="n">Novidades primeiro</option><option value="e">Mais estoque primeiro</option><option value="a">De A a Z</option></select><button id="clr">Limpar</button><span class="n" id="cnt"></span></div></div>
<main class="w"><div class="grid" id="g"></div><p class="empty" id="em">Nenhuma peça com esse filtro. Tente outra grife ou limpe a busca.</p><button class="more" id="more">Ver mais peças</button>
<section class="info"><div><h2>Como comprar</h2><p style="color:var(--mut)">Toque na peça, depois em Ver na loja online. Atacado a partir de 3 peças na loja online e de 6 na loja física.</p><p style="margin-top:14px"><b>Loja física:</b> {E(END)}. {HOR}.</p>
<a class="btn b1" href="{utm(LOJA, SRC, 'info')}" target="_blank" rel="noopener" style="max-width:320px">Ver na loja online</a><a class="btn b2" href="{GRUPO}" target="_blank" rel="noopener" style="max-width:320px">Receber novidades no Grupo VIP</a></div><div><h2>Dúvidas</h2>{faq}</div></section></main>
<footer><div class="w">SP Grifes · moda masculina importada no Brás · <a href="{utm(LOJA, SRC, 'rodape')}" target="_blank" rel="noopener">Loja online</a><a href="{BLOG}" target="_blank" rel="noopener">Blog</a><a href="{IG}" target="_blank" rel="noopener">Instagram @fabioleiite</a><a href="{MAPS}" target="_blank" rel="noopener">Como chegar</a><br>Compre só pelos canais oficiais da SP Grifes.</div></footer>
<div class="md" id="md" role="dialog" aria-modal="true"><button class="x" id="x" aria-label="Fechar">×</button><div class="box"><div class="gl" id="mg"></div><div class="tx"><small id="mm"></small><h2 id="mn"></h2><p>Veja na loja online as cores e os tamanhos disponíveis hoje. Atacado a partir de 3 peças.</p><a class="btn b1" id="mu" target="_blank" rel="noopener">Ver na loja online</a><a class="btn b2" id="ms" target="_blank" rel="noopener">Enviar para um amigo</a></div></div></div>
<nav class="dock"><a href="#q" onclick="setTimeout(function(){{document.getElementById('q').focus()}},50)">Buscar</a><a class="l" href="{utm(LOJA, SRC, 'barra')}" target="_blank" rel="noopener">Loja online</a></nav>
<script>
(function(){{var D={json.dumps(DATA, ensure_ascii=False, separators=(',',':'))},C={json.dumps(CATS, ensure_ascii=False)},A="https://i0.wp.com/{ASSETB.replace('https://','')}",L="{LOJA}",U="utm_source={SRC}&utm_medium=catalogo";
function im(p,w){{return p?A+p+'?w='+w:''}}function esc(s){{var d=document.createElement('div');d.textContent=s;return d.innerHTML}}
function norm(s){{return s.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'')}}
var cat=-1,lim=40,list=[],g=document.getElementById('g');var NEW=D.map(function(x){{return x[6]}}).sort().reverse()[Math.min(30,D.length-1)];
function card(x,i){{return '<button class="it" data-i="'+i+'"><div class="ph"><img src="'+im(x[3],420)+'" alt="'+esc(x[0])+' – SP Grifes, Brás" loading="lazy" width="420" height="560">'+(x[4]?'<img class="b" src="'+im(x[4],420)+'" alt="" loading="lazy" width="420" height="560">':'')+(x[6]>=NEW?'<span class="nv">Novo</span>':'')+'</div><small>'+esc(x[1])+'</small><b>'+esc(x[0])+'</b></button>'}}
function run(){{var q=norm(document.getElementById('q').value.trim()),m=document.getElementById('m').value,o=document.getElementById('o').value;
list=D.map(function(x,i){{return i}}).filter(function(i){{var x=D[i];return (cat<0||x[2]===cat)&&(!m||x[1]===m)&&(!q||norm(x[0]+' '+x[1]+' '+C[x[2]]).indexOf(q)>-1)}});
list.sort(function(a,b){{var x=D[a],y=D[b];return o==='e'?y[7]-x[7]:o==='a'?x[0].localeCompare(y[0]):(y[6]>x[6]?1:y[6]<x[6]?-1:0)}});
document.getElementById('cnt').textContent=list.length+(list.length===1?' peça':' peças');document.getElementById('em').style.display=list.length?'none':'block';draw()}}
function draw(){{g.innerHTML=list.slice(0,lim).map(function(i){{return card(D[i],i)}}).join('');document.getElementById('more').style.display=list.length>lim?'block':'none'}}
document.getElementById('more').onclick=function(){{lim+=40;draw()}};
['q','m','o'].forEach(function(k){{document.getElementById(k).addEventListener('input',function(){{lim=40;run()}})}});
document.getElementById('clr').onclick=function(){{document.getElementById('q').value='';document.getElementById('m').value='';cat=-1;document.querySelectorAll('.cat').forEach(function(c){{c.classList.remove('on')}});lim=40;run()}};
document.querySelectorAll('.cat').forEach(function(b){{b.addEventListener('click',function(){{var c=+b.dataset.c;cat=cat===c?-1:c;document.querySelectorAll('.cat').forEach(function(x){{x.classList.toggle('on',+x.dataset.c===cat)}});lim=40;run();document.querySelector('.bar').scrollIntoView({{behavior:'smooth'}})}})}});
var md=document.getElementById('md');g.addEventListener('click',function(e){{var b=e.target.closest('.it');if(!b)return;var x=D[+b.dataset.i];
document.getElementById('mg').innerHTML='<img src="'+im(x[3],900)+'" alt="'+esc(x[0])+'">'+(x[4]?'<img src="'+im(x[4],900)+'" alt="'+esc(x[0])+' – detalhe" loading="lazy">':'');
document.getElementById('mm').textContent=x[1];document.getElementById('mn').textContent=x[0];var u=L+x[5]+(x[5].indexOf('?')>-1?'&':'?')+U;document.getElementById('mu').href=u;
document.getElementById('ms').href='https://wa.me/?text='+encodeURIComponent('Olha essa peça da SP Grifes: '+x[0]+' '+L+x[5]);md.classList.add('on')}});
function cl(){{md.classList.remove('on')}}document.getElementById('x').onclick=cl;md.addEventListener('click',function(e){{if(e.target===md)cl()}});addEventListener('keydown',function(e){{if(e.key==='Escape')cl()}});
run();
}})();
</script></body></html>'''
import os
os.makedirs('/home/claude/rh/sites/catalogo', exist_ok=True)
open('/home/claude/rh/sites/catalogo/index.html', 'w').write(page)
print(len(page), CATS)
