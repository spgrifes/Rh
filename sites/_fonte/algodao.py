import json
from common import *

URL = 'https://spgrifes.github.io/Rh/sites/algodao/'
SRC = 'site-algodao'
TITLE = 'Atlas do Algodão: do campo à camiseta, entenda fio, malha e qualidade | Algodão Turco'
DESC = 'O guia visual do algodão em português: tipos de algodão (Pima, egípcio, turco, brasileiro), fio 30.1, 40.1 e 50.1, penteado ou cardado, tipos de malha e como reconhecer qualidade na mão.'

FIB = [
 # nome, origem, espécie, fibra mm (min,max), toque, onde se usa, cor
 ("Algodão comum", "Brasil, EUA, Índia, China", "Gossypium hirsutum", 22, 28, "Macio, mais simples, ótimo custo", "Camisetas básicas, jeans, moletom", "#9aa5b8"),
 ("Algodão turco (Egeu)", "Turquia, região do Mar Egeu", "Gossypium hirsutum de fibra média-longa", 28, 32, "Macio e absorvente, encorpado", "Toalhas, roupões, camisetas e malhas", "#c4683f"),
 ("Pima peruano", "Costa norte do Peru", "Gossypium barbadense", 34, 41, "Liso, sedoso, com brilho discreto", "Camisetas premium, polos, roupa de bebê", "#2f6f5e"),
 ("Egípcio (Giza)", "Delta do Nilo, Egito", "Gossypium barbadense", 35, 42, "Firme, fino e muito resistente", "Camisas, lençóis, malhas encorpadas", "#b08a3e"),
]
TIT = [(20, "Grosso e firme", "Moletom, peças de trabalho, camisetas mais pesadas"), (24, "Encorpado", "Camisetas resistentes do dia a dia"), (30, "Equilíbrio", "O padrão das boas camisetas: macia e durável"), (40, "Fino", "Camisetas leves e de toque liso"), (50, "Extra fino", "Malhas premium, leves e frescas")]
MAL = [
 ("Meia malha (jersey)", "A malha da camiseta. Lisa na frente, com pequenos laços no avesso. Estica bem para os lados.", "camiseta"),
 ("Piquet", "Trama em relevo, parecida com favo de mel. Respira bem e segura a forma. É a malha das polos.", "polo"),
 ("Ribana", "Canelados verticais com muita elasticidade. Usada em golas, punhos e regatas justas.", "gola"),
 ("Moletom", "Por fora é lisa, por dentro é felpuda ou flanelada. Guarda calor.", "moletom"),
 ("Suedine", "Meia malha escovada, com toque aveludado tipo camurça.", "toque"),
 ("Malha mercerizada", "Recebe um banho que dá brilho, deixa a cor mais viva e a fibra mais forte.", "brilho"),
]
GLOS = [
 ("Acabamento", "Tudo que é feito no tecido depois de pronto: amaciar, tingir, dar brilho, encolher antes."),
 ("Bolinha (pilling)", "Fibras curtas que se soltam e enrolam com o atrito. Acontece menos em fio penteado e de fibra longa."),
 ("Cardado", "Fio feito com as fibras só desembaraçadas. Mais barato, um pouco mais áspero."),
 ("Encolhimento", "Quanto a peça diminui depois de lavar. Malha pré-encolhida encolhe pouco."),
 ("Fibra extra-longa (ELS)", "Algodão com fibra de cerca de 35 mm ou mais, como o Pima e o egípcio Giza."),
 ("Fio", "As fibras torcidas juntas. É do fio que se tece a malha."),
 ("Gramatura", "O peso do tecido por metro quadrado (g/m²). Quanto maior, mais encorpada a malha."),
 ("Jersey", "Outro nome da meia malha, a malha das camisetas."),
 ("Mercerização", "Banho alcalino com o fio esticado: dá brilho, resistência e cor mais intensa."),
 ("Penteado", "Fio que passa por um pente que tira as fibras curtas. Fica mais liso, macio e resistente."),
 ("Pima", "Algodão de fibra extra-longa. O peruano é cultivado na costa norte do Peru."),
 ("Piquet", "Malha com relevo de pequenos favos, típica das camisas polo."),
 ("Ribana", "Malha canelada e elástica, usada em golas e punhos."),
 ("Título do fio", "O número que diz a grossura do fio, como 30.1. Quanto maior o número, mais fino o fio."),
 ("Torção", "Quantas voltas o fio recebe. Mais torção deixa o fio mais firme."),
]
FAQ = [
 ("Qual o melhor algodão para camiseta?", "Depende do que você quer. Para toque liso e sofisticado, algodão de fibra extra-longa como o Pima peruano. Para firmeza e caimento, o egípcio. Para o dia a dia com bom preço, um algodão comum penteado 30.1 já entrega muita qualidade."),
 ("O que significa fio 30.1?", "É o título do fio no sistema inglês. O 30 indica a grossura: quanto maior o número, mais fino o fio. O 1 quer dizer que é um fio simples, de um cabo só."),
 ("Fio penteado é melhor que cardado?", "Para camiseta, quase sempre. O fio penteado perde as fibras curtas no processo, então fica mais liso, faz menos bolinha e dura mais. O cardado é mais barato e mais rústico."),
 ("Algodão turco é a mesma coisa que algodão egípcio?", "Não. O algodão turco vem principalmente da região do Mar Egeu, na Turquia, e é famoso pela maciez e absorção, muito usado em toalhas. O egípcio vem do delta do Nilo e tem fibra extra-longa."),
 ("Como saber se a malha é boa só pegando na mão?", "Olhe contra a luz (malha boa é fechada, sem buracos), estique e solte (tem que voltar ao lugar), passe a mão (liso e sem pelinhos soltos) e veja a costura dos ombros e da gola."),
]

css = '''
:root{--bg:#fbf8f1;--ink:#1f2a44;--mut:#5d6476;--t:#c4683f;--line:#e7e0d1;--card:#fff;--sand:#f1e9d8}
*{box-sizing:border-box;margin:0}html{scroll-behavior:smooth}body{background:var(--bg);color:var(--ink);font:17px/1.65 "Inter Tight",Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}img{max-width:100%}h1,h2,h3{font-family:Newsreader,Georgia,serif;font-weight:500;line-height:1.05;letter-spacing:-.015em}h1 em,h2 em{color:var(--t)}
.w{max-width:1120px;margin:0 auto;padding:0 22px}
.top{position:sticky;top:0;z-index:20;background:rgba(251,248,241,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}.top .w{display:flex;align-items:center;height:62px;gap:20px}
.brand{font:600 22px Newsreader,serif;text-decoration:none}.brand span{color:var(--t)}.top nav{margin-left:auto;display:flex;gap:18px;font-size:15px;font-weight:600}.top nav a{text-decoration:none}
@media(max-width:820px){.top nav{display:none}}
.hero{padding:70px 0 40px;position:relative;overflow:hidden}.hero .w{position:relative;z-index:2}
.hero small{font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--t);font-size:13px}.hero h1{font-size:clamp(46px,8vw,104px);margin:16px 0 20px;max-width:900px}
.hero p{font-size:20px;color:var(--mut);max-width:640px}
.boll{position:absolute;right:-60px;top:20px;width:520px;opacity:.9;z-index:1}
@media(max-width:820px){.boll{width:300px;right:-90px;top:auto;bottom:-40px;opacity:.35}}
.route{display:flex;flex-wrap:wrap;gap:10px;margin-top:30px}.route a{display:inline-flex;gap:8px;align-items:center;background:var(--card);border:1px solid var(--line);padding:11px 16px;border-radius:999px;text-decoration:none;font-weight:600;font-size:15px}.route a b{color:var(--t)}
section{padding:80px 0}.sh{max-width:760px;margin-bottom:36px}.sh small{font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--t);font-size:12px}.sh h2{font-size:clamp(34px,5vw,56px);margin:10px 0 12px}.sh p{color:var(--mut);font-size:18px}
.alt{background:var(--sand)}
.fib{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.fb{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:22px;cursor:pointer;transition:transform .2s,box-shadow .2s;text-align:left;font:inherit;color:inherit}
.fb:hover,.fb.on{transform:translateY(-3px);box-shadow:0 14px 34px rgba(31,42,68,.12)}.fb.on{outline:2px solid var(--ink)}.fb i{display:block;width:14px;height:14px;border-radius:50%;margin-bottom:12px}
.fb h3{font-size:23px;margin-bottom:6px}.fb span{font-size:14px;color:var(--mut)}
.ruler{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:26px;margin-top:18px}
.ruler .lab{display:flex;justify-content:space-between;font-size:13px;color:var(--mut);margin-bottom:8px}
.track{position:relative;height:120px;border-bottom:2px solid var(--ink);background:repeating-linear-gradient(90deg,transparent 0 calc(10% - 1px),var(--line) calc(10% - 1px) 10%)}
.fiber{position:absolute;left:0;height:6px;border-radius:6px;transition:width .6s cubic-bezier(.2,.8,.2,1)}
.fiber em{position:absolute;left:0;top:-19px;font:600 12px "Inter Tight",sans-serif;font-style:normal;white-space:nowrap}.ruler{overflow:hidden}
.det{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:20px}.det div{background:var(--bg);border-radius:14px;padding:14px}.det b{display:block;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--t)}.det p{font-size:15px;margin-top:4px}
@media(max-width:860px){.fib{grid-template-columns:1fr 1fr}.det{grid-template-columns:1fr 1fr}}
.tit{display:grid;grid-template-columns:1fr 1fr;gap:30px;align-items:center}.tit input{width:100%;accent-color:var(--t);height:30px}.tit .val{font:500 84px Newsreader,serif;line-height:1}.tit .val small{font-size:26px;color:var(--mut)}
.yarn{height:220px;background:var(--card);border:1px solid var(--line);border-radius:22px;display:flex;align-items:center;justify-content:center;overflow:hidden}
.yarn svg{width:90%;height:auto}
@media(max-width:820px){.tit{grid-template-columns:1fr}}
.pc{display:grid;grid-template-columns:1fr 1fr;gap:16px}.pc>div{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:26px}.pc h3{font-size:28px;margin-bottom:10px}.pc ul{padding-left:18px;color:var(--mut)}.pc li{margin:6px 0}.pc .bad{border-style:dashed}
.pc svg{width:100%;height:110px;margin-bottom:12px}
@media(max-width:760px){.pc{grid-template-columns:1fr}}
.mal{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.ml{background:var(--card);border:1px solid var(--line);border-radius:20px;overflow:hidden}.ml .pat{height:120px}.ml div{padding:18px}.ml h3{font-size:22px;margin-bottom:6px}.ml p{font-size:15px;color:var(--mut)}
@media(max-width:860px){.mal{grid-template-columns:1fr 1fr}}@media(max-width:520px){.mal{grid-template-columns:1fr}}
.p1{background:radial-gradient(circle at 50% 30%,#d9d2c2 2px,transparent 3px) 0 0/12px 10px,#efe9dc}
.p2{background:radial-gradient(circle,#c9c0ad 3px,transparent 4px) 0 0/14px 14px,radial-gradient(circle,#c9c0ad 3px,transparent 4px) 7px 7px/14px 14px,#efe9dc}
.p3{background:repeating-linear-gradient(90deg,#d7cfbd 0 6px,#efe9dc 6px 12px)}
.p4{background:linear-gradient(180deg,#efe9dc 0 50%,#e2d7c2 50%),repeating-linear-gradient(45deg,transparent 0 3px,#d2c7b1 3px 4px)}
.p5{background:radial-gradient(circle at 30% 30%,#f6f1e6,#ddd3bf)}
.p6{background:linear-gradient(120deg,#e9e2d3,#fff 45%,#e0d6c2 55%,#f2ece0)}
.hand{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.hd{background:var(--ink);color:#eef0f5;border-radius:22px;padding:24px}.hd b{font:500 46px Newsreader,serif;color:#f2b38f;display:block;line-height:1}.hd h3{font-size:22px;margin:10px 0 6px;color:#fff}.hd p{font-size:15px;color:#c3c8d4}
@media(max-width:860px){.hand{grid-template-columns:1fr 1fr}}
.map{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.mp{border-left:4px solid var(--t);background:var(--card);padding:18px 20px;border-radius:0 16px 16px 0}.mp h3{font-size:22px}.mp span{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--t);font-weight:700}.mp p{font-size:15px;color:var(--mut);margin-top:6px}
@media(max-width:860px){.map{grid-template-columns:1fr}}
.gl input{width:100%;font:500 17px "Inter Tight",sans-serif;padding:14px 16px;border:1.5px solid var(--ink);border-radius:14px;background:#fff;margin-bottom:16px}
.gl dl{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}.gl dl div{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 16px}.gl dt{font-weight:700}.gl dd{color:var(--mut);font-size:15px}
@media(max-width:700px){.gl dl{grid-template-columns:1fr}}
.shop{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.sp{text-decoration:none;background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden;display:block}.sp img{width:100%;aspect-ratio:3/4;object-fit:cover;display:block}.sp small{display:block;padding:12px 14px 0;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--t)}.sp b{display:block;padding:2px 14px 14px;font-size:15px;line-height:1.35}
@media(max-width:860px){.shop{grid-template-columns:1fr 1fr}}
.vids{display:grid;grid-template-columns:repeat(2,minmax(0,300px));gap:16px}
details{border-bottom:1px solid var(--line);padding:18px 0;max-width:860px}summary{font:500 22px Newsreader,serif;cursor:pointer}details p{color:var(--mut);margin-top:8px}
.cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:26px}.btn{display:inline-flex;padding:15px 22px;border-radius:14px;font-weight:700;text-decoration:none}.b1{background:var(--ink);color:#fff}.b2{border:2px solid var(--ink)}.b3{background:var(--t);color:#fff}
footer{background:var(--ink);color:#c3c8d4;padding:50px 0 60px;font-size:15px}footer .w{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:28px}footer b{color:#fff;display:block;margin-bottom:8px}footer a{display:block;text-decoration:none;margin:4px 0}footer a:hover{color:#f2b38f}
@media(max-width:760px){footer .w{grid-template-columns:1fr}}
.rv{opacity:0;transform:translateY(20px);transition:opacity .7s,transform .7s}.rv.in{opacity:1;transform:none}
''' + VCSS

BOLL = '''<svg class="boll" viewBox="0 0 400 400" aria-hidden="true"><g fill="#fff" stroke="#e7e0d1" stroke-width="2"><circle cx="200" cy="170" r="70"/><circle cx="140" cy="200" r="62"/><circle cx="262" cy="205" r="62"/><circle cx="170" cy="250" r="58"/><circle cx="235" cy="255" r="58"/><circle cx="200" cy="120" r="48"/></g><g fill="#7a5a3a"><path d="M200 300c-40 0-70 18-82 40 36-6 60-2 82 12 22-14 46-18 82-12-12-22-42-40-82-40z"/><path d="M196 352h8v48h-8z"/></g></svg>'''
fib_btns = ''.join(f'<button class="fb{" on" if i==2 else ""}" data-i="{i}"><i style="background:{c}"></i><h3>{E(n)}</h3><span>{E(o)}</span></button>' for i, (n, o, s, a, b, t, u, c) in enumerate(FIB))
fibdata = json.dumps([dict(n=n, o=o, s=s, a=a, b=b, t=t, u=u, c=c) for (n, o, s, a, b, t, u, c) in FIB], ensure_ascii=False)
titdata = json.dumps(TIT, ensure_ascii=False)
mal = ''.join(f'<article class="ml rv"><div class="pat p{i+1}"></div><div><h3>{E(n)}</h3><p>{E(d)}</p></div></article>' for i, (n, d, k) in enumerate(MAL))
glos = ''.join(f'<div data-k="{E(t.lower())}"><dt>{E(t)}</dt><dd>{E(d)}</dd></div>' for t, d in GLOS)
pima = [p for p in P if 'Pima' in p['n'] or 'Peruana' in p['n']][:4]
egip = [p for p in P if 'Egípci' in p['n']][:4]
def shop(xs, k):
    return ''.join(f'<a class="sp rv" href="{utm(p["u"], SRC, k)}" target="_blank" rel="noopener"><img src="{img(p["f"],500)}" alt="{E(p["n"])} – malha {k}, SP Grifes" loading="lazy" width="500" height="667"><small>{E(p["m"])}</small><b>{E(p["n"])}</b></a>' for p in xs)
faq = ''.join(f'<details class="rv"><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in FAQ)
article = '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"Article","headline":"Atlas do Algodão: do campo à camiseta","about":["algodão Pima","algodão egípcio","algodão turco","título do fio","malha"],"inLanguage":"pt-BR","publisher":{"@type":"Organization","name":"SP Grifes","url":LOJA},"mainEntityOfPage":URL}, ensure_ascii=False) + '</script>'
vh = vcard(IDS[29], 'Algodão Pima no Peru') + vcard(IDS[0], 'Malha peruana de perto')

page = head(TITLE, DESC, URL, img(pima[0]['f'] if pima else P[0]['f'], 1200), 'family=Newsreader:opsz,wght@6..72,500;6..72,600&family=Inter+Tight:wght@400;600;700') + f'''
<style>{css}</style>{faq_ld(FAQ)}{article}</head><body>
<header class="top"><div class="w"><a class="brand" href="#inicio">Algodão <span>Turco</span></a><nav><a href="#fibras">Fibras</a><a href="#fio">Fio</a><a href="#malhas">Malhas</a><a href="#mao">Teste da mão</a><a href="#glossario">Glossário</a></nav></div></header>
<main id="inicio">
<div class="hero">{BOLL}<div class="w"><small>Atlas do Algodão</small><h1>Do campo à <em>camiseta</em>.</h1><p>Tudo o que muda a qualidade de uma peça de algodão, explicado com figuras e em português claro: a fibra, o fio, a malha e o acabamento. Para quem compra, para quem vende e para quem fabrica.</p>
<div class="route"><a href="#fibras"><b>1</b> A fibra</a><a href="#fio"><b>2</b> O fio</a><a href="#penteado"><b>3</b> Penteado ou cardado</a><a href="#malhas"><b>4</b> A malha</a><a href="#mao"><b>5</b> Teste da mão</a><a href="#mundo"><b>6</b> Onde nasce</a></div></div></div>

<section id="fibras" class="alt"><div class="w"><div class="sh rv"><small>1 · A fibra</small><h2>O tamanho da fibra <em>muda tudo</em></h2><p>Fibra mais longa vira fio mais liso e resistente, com menos pelinhos soltos. Toque em cada algodão e compare o comprimento na régua.</p></div>
<div class="fib rv">{fib_btns}</div>
<div class="ruler rv"><div class="lab"><span>0 mm</span><span>Comprimento médio da fibra</span><span>45 mm</span></div><div class="track" id="trk"></div>
<div class="det" id="det"></div></div></div></section>

<section id="fio"><div class="w"><div class="tit"><div class="rv"><div class="sh" style="margin:0"><small>2 · O fio</small><h2>O que quer dizer <em>30.1</em>?</h2><p>É o título do fio. Quanto maior o número, mais fino o fio. O ".1" quer dizer fio simples, de um cabo só. Arraste e veja.</p></div>
<div class="val" id="tv">30<small>.1</small></div><input id="ti" type="range" min="0" max="4" value="2" aria-label="Título do fio"><p id="tt" style="font-size:19px;margin-top:6px"></p></div>
<div class="yarn rv"><svg viewBox="0 0 400 120" id="ys"></svg></div></div></div></section>

<section id="penteado" class="alt"><div class="w"><div class="sh rv"><small>3 · Penteado ou cardado</small><h2>O pente que separa o <em>bom</em> do comum</h2><p>As duas formas de preparar o fio. A diferença aparece no toque, nas bolinhas e na vida útil da peça.</p></div>
<div class="pc rv"><div><svg viewBox="0 0 300 110"><g stroke="#1f2a44" stroke-width="3" fill="none">{''.join(f'<path d="M10 {15+i*12} C100 {10+i*12},200 {20+i*12},290 {15+i*12}"/>' for i in range(8))}</g></svg><h3>Penteado</h3><ul><li>Tira as fibras curtas</li><li>Fio liso e alinhado</li><li>Menos bolinha e mais brilho</li><li>Mais caro, dura mais</li></ul></div>
<div class="bad"><svg viewBox="0 0 300 110"><g stroke="#8a90a0" stroke-width="2" fill="none">{''.join(f'<path d="M{10+(i*37)%240} {12+(i*23)%90} q{20+i%5*6} {-10+i%3*9} {50+i%4*10} {5-i%6*3}"/>' for i in range(18))}</g></svg><h3>Cardado</h3><ul><li>Só desembaraça as fibras</li><li>Fio mais aberto e peludo</li><li>Mais bolinha com o uso</li><li>Mais barato, toque rústico</li></ul></div></div></div></section>

<section id="malhas"><div class="w"><div class="sh rv"><small>4 · A malha</small><h2>Seis malhas que você <em>já vestiu</em></h2><p>O mesmo fio vira peças bem diferentes conforme o jeito de tecer.</p></div><div class="mal">{mal}</div></div></section>

<section id="mao" class="alt"><div class="w"><div class="sh rv"><small>5 · Teste da mão</small><h2>Reconheça qualidade <em>em 30 segundos</em></h2><p>Sem etiqueta, sem laboratório. Só a mão e a luz.</p></div>
<div class="hand rv"><div class="hd"><b>1</b><h3>Contra a luz</h3><p>Malha boa é fechada e uniforme. Muita luz passando é sinal de malha rala.</p></div><div class="hd"><b>2</b><h3>Estica e solta</h3><p>Puxe de leve na largura. Ela precisa voltar ao lugar, sem ficar deformada.</p></div><div class="hd"><b>3</b><h3>Passa a mão</h3><p>Toque liso e frio, sem pelinhos soltos. Pelinho é fibra curta: vira bolinha.</p></div><div class="hd"><b>4</b><h3>Olha a costura</h3><p>Ombro reforçado, gola firme e pontos retos. É onde a peça barata entrega o preço.</p></div></div></div></section>

<section id="mundo"><div class="w"><div class="sh rv"><small>6 · Onde nasce</small><h2>Os algodões e suas <em>terras</em></h2><p>Clima, solo e colheita mudam a fibra. Por isso o nome do lugar virou sinônimo de qualidade.</p></div>
<div class="map"><div class="mp rv"><span>Peru</span><h3>Pima peruano</h3><p>Cultivado nos vales da costa norte. Fibra extra-longa, toque sedoso.</p></div><div class="mp rv"><span>Egito</span><h3>Egípcio (Giza)</h3><p>Do delta do Nilo. Fibra extra-longa, fina e resistente, famosa em camisas e lençóis.</p></div><div class="mp rv"><span>Turquia</span><h3>Algodão turco</h3><p>Da região do Mar Egeu. Macio e absorvente, tradicional em toalhas e malhas.</p></div><div class="mp rv"><span>Brasil</span><h3>Algodão brasileiro</h3><p>Mato Grosso e Bahia lideram a produção. O Brasil está entre os maiores exportadores do mundo.</p></div><div class="mp rv"><span>EUA</span><h3>Pima americano</h3><p>Plantado no sudoeste. O nome homenageia o povo indígena Pima.</p></div><div class="mp rv"><span>China e Índia</span><h3>Os gigantes</h3><p>Os maiores produtores do mundo, com todo tipo de qualidade, do básico ao premium.</p></div></div></div></section>

<section class="alt"><div class="w"><div class="sh rv"><small>Na prática</small><h2>Sinta a diferença <em>na peça</em></h2><p>Camisetas em malha Pima e egípcia na SP Grifes, no Brás. Toque para ver malha, cores e tamanhos.</p></div>
<div class="shop">{shop(pima, 'pima')}{shop(egip, 'egipcia')}</div>
<div class="vids rv" style="margin-top:30px">{vh}</div>
<div class="cta rv"><a class="btn b3" href="{utm(LOJA, SRC, 'pratica')}" target="_blank" rel="noopener">Ver na loja online</a><a class="btn b2" href="{BLOG}algodao-egipcio-ou-pima-peruano-camiseta-masculina/" target="_blank" rel="noopener">Pima ou egípcio: o comparativo</a></div></div></section>

<section id="glossario"><div class="w gl"><div class="sh rv"><small>Glossário</small><h2>As palavras do <em>tecido</em></h2></div><input id="gq" type="search" placeholder="Procure um termo: penteado, gramatura, piquet…" aria-label="Buscar no glossário"><dl id="gd">{glos}</dl></div></section>

<section class="alt"><div class="w"><div class="sh rv"><small>Perguntas</small><h2>O que todo mundo <em>pergunta</em></h2></div>{faq}
<div class="cta rv"><a class="btn b1" href="{wa_share('Achei um guia muito bom sobre algodão e malha: ' + URL)}" target="_blank" rel="noopener">Enviar para um amigo</a><a class="btn b2" href="{GRUPO}" target="_blank" rel="noopener">Grupo VIP de novidades</a></div></div></section>
</main>
<footer><div class="w"><div><b>Algodão Turco · Atlas do Algodão</b>Um projeto da SP Grifes, loja de moda masculina importada no Brás há 10 anos.<br>{E(END)}. {HOR}.</div><div><b>Continue aprendendo</b><a href="{BLOG}" target="_blank" rel="noopener">Blog SP Grifes</a><a href="{BLOG}camiseta-fio-40-1-ou-30-1/" target="_blank" rel="noopener">Fio 40.1 ou 30.1</a><a href="{YT}" target="_blank" rel="noopener">Vídeos no YouTube</a></div><div><b>SP Grifes</b><a href="{utm(LOJA, SRC, 'rodape')}" target="_blank" rel="noopener">Loja online</a><a href="{IG}" target="_blank" rel="noopener">Instagram @fabioleiite</a><a href="{MAPS}" target="_blank" rel="noopener">Como chegar</a></div></div></footer>
<script>
(function(){{var F={fibdata},T={titdata};
var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{threshold:.1}});document.querySelectorAll('.rv').forEach(function(el){{io.observe(el)}});
var trk=document.getElementById('trk'),det=document.getElementById('det');
trk.innerHTML=F.map(function(f,i){{return '<div class="fiber" data-i="'+i+'" style="top:'+(18+i*26)+'px;background:'+f.c+';width:0"><em>'+f.n+' · '+f.a+' a '+f.b+' mm</em></div>'}}).join('');
function sel(i){{document.querySelectorAll('.fb').forEach(function(b){{b.classList.toggle('on',+b.dataset.i===i)}});var f=F[i];
document.querySelectorAll('.fiber').forEach(function(el){{var x=F[+el.dataset.i];el.style.width=((x.a+x.b)/2/45*100*0.82)+'%';el.style.opacity=(+el.dataset.i===i)?1:.28;el.style.height=(+el.dataset.i===i)?'9px':'5px'}});
det.innerHTML='<div><b>Origem</b><p>'+f.o+'</p></div><div><b>Espécie</b><p>'+f.s+'</p></div><div><b>Toque</b><p>'+f.t+'</p></div><div><b>Onde se usa</b><p>'+f.u+'</p></div>'}}
document.querySelectorAll('.fb').forEach(function(b){{b.addEventListener('click',function(){{sel(+b.dataset.i)}})}});setTimeout(function(){{sel(2)}},300);
var ys=document.getElementById('ys');function yarn(k){{var t=T[k],w=Math.max(4,40-t[0]*0.62),n=Math.round(4+t[0]/6),s='';for(var i=0;i<n;i++){{var y=60+Math.sin(i)*2;s+='<path d="M'+(i*400/n)+' '+(60-w)+' C'+(i*400/n+30)+' '+(60-w)+','+(i*400/n+10)+' '+(60+w)+','+((i+1)*400/n)+' '+(60+w)+'" stroke="#c4683f" stroke-width="'+(w*0.9)+'" fill="none" stroke-linecap="round" opacity=".85"/>'}}ys.innerHTML=s;
document.getElementById('tv').innerHTML=t[0]+'<small>.1</small>';document.getElementById('tt').innerHTML='<b>'+t[1]+'.</b> '+t[2]+'.'}}
document.getElementById('ti').addEventListener('input',function(e){{yarn(+e.target.value)}});yarn(2);
document.getElementById('gq').addEventListener('input',function(e){{var q=e.target.value.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');document.querySelectorAll('#gd div').forEach(function(d){{var t=(d.dataset.k+' '+d.textContent).toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');d.style.display=t.indexOf(q)>-1?'':'none'}})}});
}})();
</script>{VID_JS}</body></html>'''
import os
os.makedirs('/home/claude/rh/sites/algodao', exist_ok=True)
open('/home/claude/rh/sites/algodao/index.html', 'w').write(motion(page, 'algodao'))
print(len(page), len(pima), len(egip))
