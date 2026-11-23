import json, collections, random
from common import *

URL = 'https://spgrifes.github.io/Rh/sites/estilo/'
SRC = 'site-estilo'
TITLE = 'Use Grifes: roupas masculinas de grife para usar no dia a dia | SP Grifes, Brás'
DESC = 'Camisetas, polos, shorts e conjuntos de grife para usar com estilo. Escolha sua marca, monte o look e veja na loja online da SP Grifes ou prove na loja do Brás.'
random.seed(7)
TOPS = [p for p in P if p['c'] in ('Camisetas', 'Polos') and 'Regata' not in p['n']]
BOTS = [p for p in P if p['c'] in ('Shorts e bermudas', 'Calças')]
brands = [m for m, n in collections.Counter(p['m'] for p in TOPS + BOTS).most_common() if n >= 4][:14]
def pick_brand(m, n=8):
    xs = sorted([p for p in P if p['m'] == m and p['c'] in ('Camisetas', 'Polos', 'Shorts e bermudas', 'Conjuntos', 'Calças')], key=lambda p: p['d'], reverse=True)
    return xs[:n]
GAL = {m: pick_brand(m) for m in brands}
HERO = [p for p in P if p['m'] == 'Lacoste' and p['c'] == 'Conjuntos'][:1] + [p for p in P if p['m'] == 'Hugo Boss' and p['c'] == 'Camisetas'][:1]
LOOK_T = sorted(TOPS, key=lambda p: -p['e'])[:12]
LOOK_B = sorted(BOTS, key=lambda p: -p['e'])[:8]
LOOK_B.sort(key=lambda p: 0 if 'Reserva' in p['n'] else 1)
VIDS = [(IDS[6], 'Gucci de perto na SP Grifes'), (IDS[3], 'Ralph Lauren na arara da loja'), (IDS[20], 'Fred Perry vestindo de verdade')]

FAQ = [
 ("Como usar roupa de grife sem exagero?", "Uma peça protagonista por look. Se a camiseta tem estampa ou logo grande, o resto fica liso: short neutro, tênis branco e cores de base como preto, branco, marinho e cinza."),
 ("Qual a diferença entre malha Pima e malha egípcia?", "As duas são algodões de fibra longa, com toque macio. A Pima é peruana, muito lisa e com brilho discreto. A egípcia é encorpada e firme, com ótimo caimento no corpo. Nas fichas da loja online cada peça diz a malha."),
 ("Como acertar o tamanho comprando pela internet?", "Compare com uma camiseta sua que veste bem: meça a largura de axila a axila e o comprimento. Cada produto da loja online tem a tabela de medidas para conferir antes de comprar."),
 ("Posso provar antes de comprar?", "Pode. Na loja física da SP Grifes, no Brás, você prova as peças. Fica no Shopping Feira da Madrugada, Piso 1, Corredor D, Loja 1202, de segunda a sábado, das 7h às 16h."),
 ("Como cuidar para a peça durar mais?", "Lave do avesso, em água fria, sem alvejante, e seque à sombra. Não passe ferro em cima de estampa ou bordado. Assim a cor e o logo duram muito mais."),
]

css = '''
:root{--bg:#0c0b0a;--ink:#f3ede2;--mut:#b8afa1;--gold:#c9a45c;--line:#2a2622;--card:#151311}
*{box-sizing:border-box;margin:0}html{scroll-behavior:smooth}body{background:var(--bg);color:var(--ink);font:17px/1.65 "DM Sans",Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}img{max-width:100%}h1,h2,h3{font-family:Fraunces,Georgia,serif;font-weight:500;letter-spacing:-.01em;line-height:1.05}
h1 i,h2 i{color:var(--gold)}
.w{max-width:1160px;margin:0 auto;padding:0 22px}
.top{position:fixed;inset:0 0 auto 0;z-index:30;transition:background .3s}.top.s{background:rgba(12,11,10,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.top .w{display:flex;align-items:center;height:66px;gap:18px}.top img{height:36px;width:auto}.top nav{margin-left:auto;display:flex;gap:20px;font-size:14px;letter-spacing:.08em;text-transform:uppercase}.top nav a{text-decoration:none}.top .b{border:1px solid var(--gold);color:var(--gold);padding:8px 14px}
@media(max-width:760px){.top nav a:not(.b){display:none}}
.hero{min-height:100svh;display:grid;grid-template-columns:1fr 1fr;position:relative}
.hero .ph{position:relative;overflow:hidden}.hero .ph img{width:100%;height:100%;object-fit:cover;display:block;animation:kb 18s ease-in-out infinite alternate}
@keyframes kb{to{transform:scale(1.08)}}
.hero .tx{display:flex;flex-direction:column;justify-content:center;padding:120px 7vw 60px}
.ey{font-size:13px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold)}
.hero h1{font-size:clamp(48px,7vw,104px);margin:18px 0 22px}.hero p{color:var(--mut);font-size:19px;max-width:500px}
.cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}.btn{display:inline-flex;align-items:center;padding:16px 26px;text-decoration:none;font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:14px;transition:all .25s}
.b1{background:var(--gold);color:#120f0a}.b1:hover{background:#e0bd76}.b2{border:1px solid var(--ink);color:var(--ink)}.b2:hover{background:var(--ink);color:var(--bg)}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero .ph{height:62svh}.hero .tx{padding:34px 22px 56px}.hero .ph:nth-child(2){display:none}}
section{padding:96px 0}.sh{max-width:760px;margin-bottom:40px}.sh h2{font-size:clamp(36px,5.4vw,64px);margin:12px 0 14px}.sh p{color:var(--mut);font-size:18px}
.chips{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:28px}.chips button{background:transparent;border:1px solid #3b352e;color:var(--ink);padding:10px 18px;font:600 14px "DM Sans",sans-serif;letter-spacing:.04em;cursor:pointer;transition:all .2s}.chips button.on,.chips button:hover{border-color:var(--gold);color:#120f0a;background:var(--gold)}
.gal{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}.g{position:relative;overflow:hidden;background:var(--card);cursor:zoom-in;animation:up .6s both;animation-delay:var(--d)}
@keyframes up{from{opacity:0;transform:translateY(16px)}}
.g img{width:100%;aspect-ratio:3/4;object-fit:cover;display:block;transition:transform .6s}.g:hover img{transform:scale(1.06)}
.g figcaption{padding:12px 14px 16px}.g small{color:var(--gold);font-size:12px;letter-spacing:.14em;text-transform:uppercase}.g b{display:block;font-weight:500;font-size:15px;line-height:1.35;margin-top:4px}
@media(max-width:900px){.gal{grid-template-columns:repeat(2,1fr);gap:10px}}
.lk{display:grid;grid-template-columns:1fr 1.1fr;gap:40px;align-items:start}
.pick{min-width:0}.board{min-width:0}.pick h3{font-size:24px;margin:0 0 12px}.row{display:flex;gap:10px;overflow-x:auto;padding-bottom:10px;margin-bottom:22px;scroll-snap-type:x mandatory}
.row button{flex:none;width:92px;border:2px solid transparent;background:var(--card);padding:0;cursor:pointer;scroll-snap-align:start}.row button.on{border-color:var(--gold)}.row img{width:100%;aspect-ratio:3/4;object-fit:cover;display:block}
.board{display:grid;grid-template-columns:1fr 1fr;gap:12px;background:var(--card);padding:16px;border:1px solid var(--line)}.board figure{margin:0}.board img{width:100%;aspect-ratio:3/4;object-fit:cover;display:block;transition:opacity .3s}.board figcaption{font-size:14px;color:var(--mut);margin-top:8px;min-height:42px}
.board .acts{grid-column:1/-1;display:flex;gap:10px;flex-wrap:wrap}
@media(max-width:860px){.lk{grid-template-columns:1fr}}
.rules{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border:1px solid var(--line)}.rules div{background:var(--bg);padding:30px 24px}.rules b{font:500 54px Fraunces,serif;color:var(--gold);display:block;line-height:1}.rules h3{font-size:22px;margin:14px 0 8px}.rules p{color:var(--mut);font-size:15px}
@media(max-width:860px){.rules{grid-template-columns:1fr 1fr}}@media(max-width:520px){.rules{grid-template-columns:1fr}}
.malhas{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}.malhas div{border:1px solid var(--line);padding:24px;background:linear-gradient(160deg,#18150f,#0c0b0a)}.malhas h3{font-size:26px;margin-bottom:8px}.malhas span{display:inline-block;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:10px}.malhas p{color:var(--mut);font-size:15px}
@media(max-width:900px){.malhas{grid-template-columns:1fr 1fr}}@media(max-width:520px){.malhas{grid-template-columns:1fr}}
.vids{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;max-width:920px}
@media(max-width:760px){.vids{grid-template-columns:repeat(3,78%);overflow-x:auto;scroll-snap-type:x mandatory}.vids>*{scroll-snap-align:start}}
.visit{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:56px 0}
.visit dl{display:grid;gap:14px}.visit dt{color:var(--gold);font-size:12px;letter-spacing:.18em;text-transform:uppercase}.visit dd{font-size:18px}
@media(max-width:860px){.visit{grid-template-columns:1fr}}
details{border-bottom:1px solid var(--line);padding:20px 0;max-width:880px}summary{cursor:pointer;font:500 22px Fraunces,serif;list-style:none}summary::after{content:"+";float:right;color:var(--gold)}details[open] summary::after{content:"–"}details p{color:var(--mut);margin-top:10px}
footer{padding:56px 0 100px;color:var(--mut);font-size:15px;border-top:1px solid var(--line)}footer .w{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:28px}footer b{display:block;color:var(--ink);margin-bottom:8px;letter-spacing:.1em;text-transform:uppercase;font-size:13px}footer a{display:block;text-decoration:none;margin:5px 0}footer a:hover{color:var(--gold)}
@media(max-width:760px){footer .w{grid-template-columns:1fr}}
.zm{position:fixed;inset:0;z-index:60;background:rgba(0,0,0,.92);display:none;align-items:center;justify-content:center;padding:20px}.zm.on{display:flex}.zm .in{max-width:520px;width:100%;text-align:center}.zm img{max-height:72vh;width:auto;max-width:100%;display:block;margin:0 auto 14px}.zm b{display:block;font:500 22px Fraunces,serif;margin-bottom:14px}.zm .x{position:absolute;top:14px;right:18px;background:none;border:0;color:#fff;font-size:34px;cursor:pointer}
.dock{display:none;position:fixed;left:50%;bottom:14px;transform:translateX(-50%);z-index:30;gap:6px;background:rgba(21,19,17,.95);border:1px solid #3b352e;padding:6px;border-radius:999px}.dock a{text-decoration:none;font-weight:700;font-size:13px;padding:10px 15px;border-radius:999px;letter-spacing:.04em}.dock .l{background:var(--gold);color:#120f0a}
@media(max-width:760px){.dock{display:flex}}
.rv{opacity:0;transform:translateY(24px);transition:opacity .8s,transform .8s}.rv.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.rv{opacity:1;transform:none}.hero .ph img{animation:none}}
''' + VCSS

def gfig(p, k):
    return f'''<figure class="g" style="--d:{k*60}ms" data-full="{img(p['f'],1000)}" data-n="{E(p['n'])}" data-u="{utm(p['u'], SRC, 'galeria')}"><img src="{img(p['f'],500)}" alt="{E(p['n'])} – look masculino de grife, SP Grifes, Brás" loading="lazy" width="500" height="667"><figcaption><small>{E(p['m'])}</small><b>{E(p['n'])}</b></figcaption></figure>'''
galdata = {m: [[img(p['f'],500), img(p['f'],1000), p['n'], utm(p['u'], SRC, 'galeria'), p['m']] for p in GAL[m]] for m in brands}
chips = ''.join(f'<button data-m="{E(m)}"{" class=on" if i==0 else ""}>{E(m)}</button>' for i, m in enumerate(brands))
gal0 = ''.join(gfig(p, k) for k, p in enumerate(GAL[brands[0]]))
def rbtn(p, grp, on):
    return f'<button data-g="{grp}" data-img="{img(p["f"],600)}" data-n="{E(p["n"])}" data-u="{utm(p["u"], SRC, "look")}"{" class=on" if on else ""} aria-label="{E(p["n"])}"><img src="{img(p["f"],200)}" alt="{E(p["n"])}" loading="lazy" width="92" height="123"></button>'
rowT = ''.join(rbtn(p, 't', i == 0) for i, p in enumerate(LOOK_T))
rowB = ''.join(rbtn(p, 'b', i == 0) for i, p in enumerate(LOOK_B))
vh = ''.join(vcard(v, t) for v, t in VIDS)
faq = ''.join(f'<details class="rv"><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in FAQ)
share = wa_share('Achei esse guia de grifes masculinas, olha: ' + URL)
hero = ''.join(f'<div class="ph"><img src="{img(p["f"],1100)}" alt="{E(p["n"])} – SP Grifes" width="1100" height="1467"{" fetchpriority=high" if i==0 else ""}></div>' for i, p in enumerate(HERO[:1]))

page = head(TITLE, DESC, URL, img(HERO[0]['f'], 1200), 'family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;1,9..144,500&family=DM+Sans:wght@400;600;700') + f'''
<style>{css}</style>{faq_ld(FAQ)}{store_ld(URL, 'Use Grifes')}</head><body>
<header class="top" id="top"><div class="w"><a href="#inicio"><img src="../img/logo-sp-grifes-branco.png" alt="SP Grifes – moda masculina importada no Brás" width="130" height="81"></a>
<nav><a href="#grifes">Grifes</a><a href="#look">Monte o look</a><a href="#malhas">Malhas</a><a href="#loja">Visite</a><a class="b" href="{utm(LOJA, SRC, 'menu')}" target="_blank" rel="noopener">Loja online</a></nav></div></header>
<main id="inicio">
<div class="hero">{hero}<div class="tx"><span class="ey">Use Grifes · SP Grifes · Brás</span><h1>Use <i>grife.</i><br>Do jeito certo.</h1>
<p>Camisetas, polos, shorts e conjuntos das grifes que você gosta, para vestir no dia a dia com caimento bom e malha que se sente na mão.</p>
<div class="cta"><a class="btn b1" href="#grifes">Escolher minha grife</a><a class="btn b2" href="#look">Montar um look</a></div></div></div>

<section id="grifes"><div class="w"><div class="sh rv"><span class="ey">Qual é a sua?</span><h2>Escolha a <i>grife</i>.<br>Veja as peças.</h2><p>As novidades de cada marca na SP Grifes. Toque na foto para ampliar e ver na loja online.</p></div>
<div class="chips rv">{chips}</div><div class="gal" id="gal">{gal0}</div>
<div class="cta rv"><a class="btn b2" id="galall" href="{utm(LOJA, SRC, 'galeria')}" target="_blank" rel="noopener">Ver todas na loja online</a></div></div></section>

<section id="look" style="background:#110f0d"><div class="w"><div class="sh rv"><span class="ey">Monte o look</span><h2>Um toque em cima.<br>Um toque <i>embaixo</i>.</h2><p>Combine a parte de cima com a de baixo e veja o look pronto. Gostou? Abra cada peça na loja online.</p></div>
<div class="lk"><div class="pick rv"><h3>Parte de cima</h3><div class="row" id="rt">{rowT}</div><h3>Parte de baixo</h3><div class="row" id="rb">{rowB}</div></div>
<div class="board rv"><figure><img id="lt" src="{img(LOOK_T[0]['f'],600)}" alt="Parte de cima do look" width="600" height="800"><figcaption id="ct">{E(LOOK_T[0]['n'])}</figcaption></figure><figure><img id="lb" src="{img(LOOK_B[0]['f'],600)}" alt="Parte de baixo do look" width="600" height="800"><figcaption id="cb">{E(LOOK_B[0]['n'])}</figcaption></figure>
<div class="acts"><a class="btn b1" id="ut" href="{utm(LOOK_T[0]['u'], SRC, 'look')}" target="_blank" rel="noopener">Ver a de cima</a><a class="btn b2" id="ub" href="{utm(LOOK_B[0]['u'], SRC, 'look')}" target="_blank" rel="noopener">Ver a de baixo</a></div></div></div></div></section>

<section><div class="w"><div class="sh rv"><span class="ey">Estilo sem erro</span><h2>4 regras para usar <i>grife</i> com classe</h2></div>
<div class="rules rv"><div><b>1</b><h3>Uma estrela por look</h3><p>Logo grande ou estampa forte? O resto fica liso e neutro.</p></div><div><b>2</b><h3>Caimento antes da marca</h3><p>Ombro no lugar, manga no meio do braço, barra no quadril.</p></div><div><b>3</b><h3>Base de 4 cores</h3><p>Preto, branco, marinho e cinza combinam com tudo o que você tem.</p></div><div><b>4</b><h3>Cuide da malha</h3><p>Do avesso, água fria e secar à sombra. A peça dura anos.</p></div></div></div></section>

<section id="malhas"><div class="w"><div class="sh rv"><span class="ey">Malha boa se sente na mão</span><h2>Entenda o <i>tecido</i> antes de comprar</h2><p>O nome da malha aparece em cada peça da loja online. Aqui está o que cada uma entrega.</p></div>
<div class="malhas rv"><div><span>Algodão peruano</span><h3>Pima jersey</h3><p>Fibra longa, toque liso e macio, brilho discreto. Fica elegante até no básico.</p></div><div><span>Algodão de fibra longa</span><h3>Egípcia</h3><p>Malha mais encorpada e firme, com ótimo caimento e boa durabilidade.</p></div><div><span>Gola polo</span><h3>Piquet</h3><p>Trama em relevo que respira bem. É o tecido clássico das polos de grife.</p></div><div><span>Shorts</span><h3>Tactel</h3><p>Leve, seca rápido e não amassa. Perfeito para o verão e para a praia.</p></div></div>
<div class="cta rv"><a class="btn b2" href="{BLOG}" target="_blank" rel="noopener">Aprender mais no blog</a></div></div></section>

<section><div class="w"><div class="sh rv"><span class="ey">Na loja</span><h2>Veja as peças <i>vestidas</i></h2><p>Vídeos gravados na SP Grifes. Toque para assistir aqui mesmo.</p></div><div class="vids rv">{vh}</div>
<div class="cta rv"><a class="btn b2" href="{YT}?sub_confirmation=1" target="_blank" rel="noopener">Inscreva-se no canal</a></div></div></section>

<section id="loja"><div class="w"><div class="visit rv"><div><span class="ey">Prove antes de levar</span><h2 style="font-size:clamp(34px,5vw,58px);margin:12px 0 16px">Venha <i>provar</i> no Brás</h2><p style="color:var(--mut)">Na loja física você sente a malha, prova o tamanho e sai vestido.</p><div class="cta"><a class="btn b1" href="{MAPS}" target="_blank" rel="noopener">Como chegar</a><a class="btn b2" href="{GRUPO}" target="_blank" rel="noopener">Grupo VIP de novidades</a></div></div>
<dl><dt>Endereço</dt><dd>{E(END)}</dd><dt>Horário</dt><dd>{HOR}</dd><dt>Loja online</dt><dd>Envio para todo o Brasil</dd></dl></div></div></section>

<section><div class="w"><div class="sh rv"><span class="ey">Dúvidas</span><h2>Perguntas de <i>estilo</i></h2></div>{faq}
<div class="cta rv" style="margin-top:36px"><a class="btn b1" href="{utm(LOJA, SRC, 'final')}" target="_blank" rel="noopener">Ver na loja online</a><a class="btn b2" href="{share}" target="_blank" rel="noopener">Enviar para um amigo</a></div></div></section>
</main>
<footer><div class="w"><div><b>SP Grifes · Use Grifes</b>{E(END)}<br>{HOR}<br><br>Compre só pelos canais oficiais da SP Grifes.</div><div><b>Canais oficiais</b><a href="{utm(LOJA, SRC, 'rodape')}" target="_blank" rel="noopener">Loja online</a><a href="{GRUPO}" target="_blank" rel="noopener">Grupo VIP</a><a href="{BLOG}" target="_blank" rel="noopener">Blog SP Grifes</a></div><div><b>Acompanhe</b><a href="{IG}" target="_blank" rel="noopener">Instagram @fabioleiite</a><a href="{YT}" target="_blank" rel="noopener">YouTube</a><a href="{MAPS}" target="_blank" rel="noopener">Como chegar</a></div></div></footer>
<div class="zm" id="zm" role="dialog" aria-modal="true"><button class="x" aria-label="Fechar">×</button><div class="in"><img id="zi" alt="" src="data:image/gif;base64,R0lGODlhAQABAAAAACw="><b id="zn"></b><a class="btn b1" id="zu" target="_blank" rel="noopener">Ver na loja online</a></div></div>
<nav class="dock"><a href="#grifes">Grifes</a><a href="#look">Look</a><a class="l" href="{utm(LOJA, SRC, 'barra')}" target="_blank" rel="noopener">Loja online</a></nav>
<script>
(function(){{var D={json.dumps(galdata, ensure_ascii=False)};
var top=document.getElementById('top');addEventListener('scroll',function(){{top.classList.toggle('s',scrollY>40)}},{{passive:true}});
var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{threshold:.1}});document.querySelectorAll('.rv').forEach(function(el){{io.observe(el)}});
function esc(s){{var d=document.createElement('div');d.textContent=s;return d.innerHTML}}
var gal=document.getElementById('gal');
document.querySelectorAll('.chips button').forEach(function(b){{b.addEventListener('click',function(){{document.querySelectorAll('.chips button').forEach(function(x){{x.classList.remove('on')}});b.classList.add('on');
gal.innerHTML=D[b.dataset.m].map(function(x,k){{return '<figure class="g" style="--d:'+(k*60)+'ms" data-full="'+x[1]+'" data-n="'+esc(x[2])+'" data-u="'+x[3]+'"><img src="'+x[0]+'" alt="'+esc(x[2])+' – SP Grifes, Brás" loading="lazy" width="500" height="667"><figcaption><small>'+esc(x[4])+'</small><b>'+esc(x[2])+'</b></figcaption></figure>'}}).join('')}})}});
var zm=document.getElementById('zm');gal.addEventListener('click',function(e){{var f=e.target.closest('.g');if(!f)return;document.getElementById('zi').src=f.dataset.full;document.getElementById('zi').alt=f.dataset.n;document.getElementById('zn').textContent=f.dataset.n;document.getElementById('zu').href=f.dataset.u;zm.classList.add('on')}});
zm.addEventListener('click',function(e){{if(e.target===zm||e.target.classList.contains('x'))zm.classList.remove('on')}});addEventListener('keydown',function(e){{if(e.key==='Escape')zm.classList.remove('on')}});
document.querySelectorAll('.row button').forEach(function(b){{b.addEventListener('click',function(){{var g=b.dataset.g;document.querySelectorAll('.row button[data-g='+g+']').forEach(function(x){{x.classList.remove('on')}});b.classList.add('on');
var im=document.getElementById(g==='t'?'lt':'lb');im.style.opacity=.2;im.onload=function(){{im.style.opacity=1}};im.src=b.dataset.img;document.getElementById(g==='t'?'ct':'cb').textContent=b.dataset.n;document.getElementById(g==='t'?'ut':'ub').href=b.dataset.u}})}});
}})();
</script>{VID_JS}</body></html>'''
import os
os.makedirs('/home/claude/rh/sites/estilo', exist_ok=True)
open('/home/claude/rh/sites/estilo/index.html', 'w').write(motion(page, 'estilo'))
print(len(page), brands, len(LOOK_T), len(LOOK_B), HERO[0]['n'])
