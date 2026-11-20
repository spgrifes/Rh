import json, collections
from common import *

URL = 'https://spgrifes.github.io/Rh/sites/revenda/'
SRC = 'site-revenda'
N_MOD = len(P)
N_BR = len({p['m'] for p in P})
# kit de largada: as peças com mais estoque (as que mais giram e mais têm reposição)
def top(cat, n):
    xs = sorted([p for p in P if p['c'] == cat], key=lambda p: -p['e'])
    out, seen = [], collections.Counter()
    for p in xs:
        if seen[p['m']] >= (1 if cat != 'Camisetas' else 2) or 'Regata' in p['n']: continue
        seen[p['m']] += 1; out.append(p)
        if len(out) >= n: break
    return out
KIT = top('Camisetas', 8) + top('Polos', 4) + top('Shorts e bermudas', 4) + top('Conjuntos', 2)
HERO = [KIT[1], KIT[8], KIT[0]]
VIDS = vids(['general'], 3)
VIDS = [IDS[39], IDS[2], IDS[27]]

FAQ = [
 ("Qual o pedido mínimo para comprar no atacado?", "Na loja online da SP Grifes o preço de atacado vale a partir de 3 peças. Na loja física, no Brás, a partir de 6 peças. Dá para misturar marcas, modelos e tamanhos."),
 ("Preciso ter CNPJ para revender?", "Não para começar. Muita gente começa vendendo para amigos, no Instagram e no status do WhatsApp. Quando o volume crescer, vale formalizar como MEI, que é simples e barato."),
 ("Quanto dinheiro eu preciso para começar?", "Dá para começar pequeno, com 10 a 15 peças, testar o que sai mais na sua região e reinvestir o lucro. Use o simulador desta página com o custo real das peças para ver quanto investe e quanto pode lucrar."),
 ("Que peças vendem mais para quem está começando?", "Camisetas de grife em cores básicas (preto, branco e marinho), gola polo e shorts de tactel no verão. São peças fáceis de explicar, de mostrar em foto e de acertar o tamanho."),
 ("Vocês enviam para outras cidades?", "Sim. A loja online envia para todo o Brasil assim que o pagamento é confirmado. As cores e tamanhos que aparecem lá são os que estão disponíveis no dia."),
 ("Como sei que estou comprando da SP Grifes de verdade?", "Compre só pelos canais oficiais: a loja online spgrifes.com.br, a loja física no Brás e o Grupo VIP oficial. Na dúvida, não faça Pix antes de confirmar com a equipe."),
]

def kit_card(p, k):
    return f'''<article class="kc" data-c="{E(p['c'])}" style="--d:{(k%8)*60}ms"><a href="{utm(p['u'], SRC, 'kit')}" target="_blank" rel="noopener"><div class="ki"><img src="{img(p['f'],500)}" alt="{E(p['n'])} – peça para revender, SP Grifes, Brás" loading="lazy" width="500" height="667"></div><small>{E(p['m'])}</small><b>{E(p['n'])}</b><span>Ver na loja online →</span></a></article>'''

cats = []
for p in KIT:
    if p['c'] not in cats: cats.append(p['c'])

TITLE = 'Revender camisetas de grife: comece seu negócio de moda masculina | SP Grifes'
DESC = 'Comece a revender moda masculina de grife com a SP Grifes, no Brás: atacado a partir de 3 peças na loja online, simulador de lucro, kit de largada e plano de 7 dias.'

css = '''
:root{--p:#f6f2ea;--ink:#13211a;--g:#1f6f47;--g2:#174f34;--lime:#d8f36a;--mut:#56645c;--card:#fffdf8;--line:#e3dccd}
*{box-sizing:border-box;margin:0}html{scroll-behavior:smooth}body{background:var(--p);color:var(--ink);font:17px/1.6 Inter,system-ui,-apple-system,Segoe UI,Arial,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}img{max-width:100%}h1,h2,h3{font-family:"Space Grotesk",Inter,sans-serif;letter-spacing:-.02em;line-height:1.08}
.w{max-width:1120px;margin:0 auto;padding:0 20px}
.top{position:sticky;top:0;z-index:20;background:rgba(246,242,234,.94);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.top .w{display:flex;align-items:center;gap:18px;height:64px}.top img{height:38px;width:auto}.top nav{margin-left:auto;display:flex;gap:18px;font-weight:600;font-size:15px}.top nav a{text-decoration:none}.top .b{background:var(--ink);color:#fff;padding:9px 16px;border-radius:999px}
@media(max-width:760px){.top nav a:not(.b){display:none}}
.hero{padding:56px 0 40px}.hero .w{display:grid;grid-template-columns:1.1fr .9fr;gap:42px;align-items:center}
.tag{display:inline-flex;gap:8px;align-items:center;background:var(--lime);color:var(--ink);font-weight:700;font-size:13px;letter-spacing:.06em;text-transform:uppercase;padding:7px 14px;border-radius:999px}
.hero h1{font-size:clamp(38px,6vw,68px);margin:18px 0 16px}.hero h1 em{font-style:normal;color:var(--g);background:linear-gradient(transparent 62%,var(--lime) 62%)}
.hero p.l{font-size:19px;color:var(--mut);max-width:560px}
.cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:26px}.btn{display:inline-flex;align-items:center;gap:8px;padding:16px 24px;border-radius:14px;font-weight:700;text-decoration:none;font-size:16px;transition:transform .2s,box-shadow .2s}.btn:hover{transform:translateY(-2px)}
.b1{background:var(--g);color:#fff;box-shadow:0 10px 24px rgba(31,111,71,.3)}.b2{background:#fff;color:var(--ink);border:2px solid var(--ink)}
.stack{position:relative;height:520px}.stack figure{position:absolute;width:62%;border-radius:22px;overflow:hidden;box-shadow:0 30px 60px rgba(19,33,26,.25);background:#fff;animation:fl 7s ease-in-out infinite}
.stack figure{aspect-ratio:3/4}.stack figure img{display:block;width:100%;height:100%;object-fit:cover}.stack figure:nth-child(1){left:0;top:40px;transform:rotate(-6deg)}.stack figure:nth-child(2){right:0;top:0;transform:rotate(5deg);animation-delay:-2s}.stack figure:nth-child(3){left:22%;bottom:0;width:54%;animation-delay:-4s;z-index:2}
@keyframes fl{50%{translate:0 -12px}}
.nums{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:34px;max-width:520px}.nums div{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:18px}.nums b{display:block;font:700 34px "Space Grotesk",sans-serif;color:var(--g)}.nums span{font-size:14px;color:var(--mut)}
@media(max-width:860px){.hero .w{grid-template-columns:1fr}.stack{height:380px;max-width:420px;margin:0 auto;width:100%}}
section{padding:72px 0}.sh{max-width:720px;margin-bottom:34px}.sh h2{font-size:clamp(30px,4.4vw,46px);margin:10px 0 12px}.sh p{color:var(--mut);font-size:18px}
.k{font-weight:800;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--g)}
.sim{background:var(--ink);color:#f3f1ea;border-radius:28px;padding:38px;display:grid;grid-template-columns:1fr 1fr;gap:34px}
.sim h2{color:#fff}.sim .k{color:var(--lime)}.sim p{color:#c7cec9}
.pre{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0}.pre button{background:transparent;color:#fff;border:1.5px solid #4b5b52;padding:9px 14px;border-radius:999px;font:600 14px Inter,sans-serif;cursor:pointer}.pre button.on,.pre button:hover{background:var(--lime);color:var(--ink);border-color:var(--lime)}
.f{margin:16px 0}.f label{display:flex;justify-content:space-between;font-weight:600;font-size:15px;margin-bottom:8px}.f output{color:var(--lime);font-weight:800}
.f input{width:100%;accent-color:var(--lime);height:28px}
.res{background:#1d3127;border-radius:22px;padding:26px;display:grid;gap:14px;align-content:start}.res div{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid #31463b;padding-bottom:12px}.res div:last-child{border:0}
.res span{color:#c7cec9;font-size:15px}.res b{font:700 26px "Space Grotesk",sans-serif;color:#fff}.res .big b{color:var(--lime);font-size:38px}
.res small{color:#9fb0a6;font-size:13px;line-height:1.5}
@media(max-width:860px){.sim{grid-template-columns:1fr;padding:26px}}
.paths{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.pc{background:var(--card);border:1px solid var(--line);border-radius:24px;padding:28px;position:relative;overflow:hidden}
.pc .n{font:700 64px "Space Grotesk",sans-serif;color:var(--lime);-webkit-text-stroke:1.5px var(--g);line-height:1}.pc h3{font-size:24px;margin:12px 0 10px}.pc ul{padding-left:18px;color:var(--mut);font-size:16px}.pc li{margin:6px 0}
@media(max-width:860px){.paths{grid-template-columns:1fr}}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:22px}.chips button{border:1.5px solid var(--ink);background:transparent;padding:9px 16px;border-radius:999px;font:600 14px Inter,sans-serif;cursor:pointer;color:var(--ink)}.chips button.on{background:var(--ink);color:#fff}
.kit{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.kc a{display:block;text-decoration:none;background:var(--card);border:1px solid var(--line);border-radius:20px;overflow:hidden;transition:transform .25s,box-shadow .25s;height:100%}
.kc a:hover{transform:translateY(-4px);box-shadow:0 18px 40px rgba(19,33,26,.14)}.ki{aspect-ratio:3/4;overflow:hidden;background:#eee}.ki img{width:100%;height:100%;object-fit:cover;transition:transform .5s}.kc a:hover img{transform:scale(1.05)}
.kc small{display:block;padding:14px 16px 0;font-size:12px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--g)}.kc b{display:block;padding:4px 16px;font-size:15px;line-height:1.35}.kc span{display:block;padding:8px 16px 16px;font-weight:700;font-size:14px;color:var(--g)}
.kc.hide{display:none}
@media(max-width:900px){.kit{grid-template-columns:repeat(2,1fr);gap:12px}.kc b{font-size:14px}}
.vids{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;max-width:900px}
@media(max-width:760px){.vids{grid-template-columns:repeat(3,78%);overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:8px}.vids>*{scroll-snap-align:start}}
.plan{display:grid;gap:12px;max-width:820px}.day{display:flex;gap:16px;align-items:flex-start;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:18px 20px;cursor:pointer;transition:background .2s}
.day input{width:24px;height:24px;accent-color:var(--g);flex:none;margin-top:3px}.day b{display:block;font-size:17px}.day span{color:var(--mut);font-size:15px}.day.ok{background:#e9f4dc}.day.ok b{text-decoration:line-through;text-decoration-color:var(--g)}
.bar{height:10px;background:var(--line);border-radius:99px;overflow:hidden;max-width:820px;margin-bottom:18px}.bar i{display:block;height:100%;width:0;background:var(--g);transition:width .4s}
details{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin-bottom:10px;max-width:860px}summary{font-weight:700;cursor:pointer;font-size:17px}details p{margin-top:10px;color:var(--mut)}
.final{background:var(--g);color:#fff;border-radius:30px;padding:48px;text-align:center}.final h2{font-size:clamp(30px,4.5vw,48px);color:#fff;margin-bottom:12px}.final p{color:#d9eadf;max-width:620px;margin:0 auto 24px;font-size:18px}
.final .btn.b1{background:var(--lime);color:var(--ink)}.final .btn.b2{background:transparent;color:#fff;border-color:#fff}.final .cta{justify-content:center}
footer{padding:46px 0 90px;font-size:15px;color:var(--mut)}footer .w{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:28px}footer b{color:var(--ink);display:block;margin-bottom:8px}footer a{display:block;text-decoration:none;margin:4px 0}footer a:hover{color:var(--g)}
@media(max-width:760px){footer .w{grid-template-columns:1fr}.dock{display:flex}}
.dock{display:none;position:fixed;left:50%;bottom:14px;transform:translateX(-50%);z-index:30;gap:8px;background:rgba(19,33,26,.92);padding:7px;border-radius:999px;box-shadow:0 12px 30px rgba(0,0,0,.25)}.dock a{color:#fff;text-decoration:none;font-weight:700;font-size:14px;padding:10px 16px;border-radius:999px}.dock a.l{background:var(--lime);color:var(--ink)}
.rv{opacity:0;transform:translateY(22px);transition:opacity .7s,transform .7s;transition-delay:var(--d,0ms)}.rv.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.rv{opacity:1;transform:none}.stack figure{animation:none}}
''' + VCSS

hero_figs = ''.join(f'<figure><img src="{img(p["f"],700)}" alt="{E(p["n"])} – SP Grifes, Brás" width="700" height="933"></figure>' for p in HERO)
chips = '<button class="on" data-f="*">Todas</button>' + ''.join(f'<button data-f="{E(c)}">{E(c)}</button>' for c in cats)
kit = ''.join(kit_card(p, k) for k, p in enumerate(KIT))
vhtml = ''.join(vcard(v, t) for v, t in zip(VIDS, ['Como revender camisetas de grife', 'Peças que mais giram na revenda', 'Grupo VIP de novidades da SP Grifes']))
PLAN = [
 ("Dia 1 · Escolha seu canal", "Instagram, status do WhatsApp ou venda direta para conhecidos. Comece por um só."),
 ("Dia 2 · Defina o público", "Para quem você vai vender? Trabalho, academia, faculdade, bairro. Anote 20 nomes."),
 ("Dia 3 · Monte o primeiro pedido", "10 a 15 peças em cores básicas e tamanhos M e G. Use o simulador para fechar a conta."),
 ("Dia 4 · Fotos que vendem", "Luz do dia, fundo limpo, peça no cabide e vestida. Mostre etiqueta e malha de perto."),
 ("Dia 5 · Poste e avise", "Poste as peças e mande mensagem para os 20 nomes. Ofereça reserva por 24 horas."),
 ("Dia 6 · Venda e anote", "Anote o que vendeu, cor e tamanho. Isso diz o que repor."),
 ("Dia 7 · Reponha o que girou", "Reinvista o lucro nas peças que saíram primeiro. É assim que a loja cresce."),
]
plan = ''.join(f'<label class="day rv"><input type="checkbox" data-i="{i}"><div><b>{E(t)}</b><span>{E(d)}</span></div></label>' for i, (t, d) in enumerate(PLAN))
faq = ''.join(f'<details class="rv"><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in FAQ)
share = wa_share('Olha esse guia para começar a revender roupa de grife: ' + URL)

page = head(TITLE, DESC, URL, img(HERO[0]['f'], 1200), 'family=Inter:wght@400;600;700;800&family=Space+Grotesk:wght@600;700') + f'''
<style>{css}</style>{faq_ld(FAQ)}{store_ld(URL, 'SP Grifes Revenda')}</head><body>
<header class="top"><div class="w"><a href="#topo" aria-label="SP Grifes"><img src="../img/logo-sp-grifes-colorido.png" alt="SP Grifes – moda masculina importada no Brás" width="140" height="87"></a>
<nav><a href="#simulador">Simulador</a><a href="#kit">Kit de largada</a><a href="#plano">Plano de 7 dias</a><a href="#duvidas">Dúvidas</a><a class="b" href="{utm(LOJA, SRC, 'menu')}" target="_blank" rel="noopener">Loja online</a></nav></div></header>
<main id="topo">
<div class="hero"><div class="w"><div class="rv">
<span class="tag">Revenda · Brás · São Paulo</span>
<h1>Seu negócio de <em>moda masculina</em> começa com 3 peças.</h1>
<p class="l">A SP Grifes está há 10 anos no Brás abastecendo quem revende roupa de grife no Brasil inteiro. Aqui você faz a conta do lucro, escolhe as primeiras peças e segue um plano simples de 7 dias.</p>
<div class="cta"><a class="btn b1" href="#simulador">Fazer a conta do meu lucro</a><a class="btn b2" href="{GRUPO}" target="_blank" rel="noopener">Entrar no Grupo VIP</a></div>
<div class="nums"><div><b>3</b><span>peças para ter preço de atacado na loja online</span></div><div><b>6</b><span>peças para atacado na loja física</span></div><div><b>{N_MOD}</b><span>modelos com estoque hoje</span></div><div><b>{N_BR}</b><span>grifes para escolher</span></div></div>
</div><div class="stack rv" style="--d:150ms">{hero_figs}</div></div></div>

<section id="simulador"><div class="w"><div class="sim rv">
<div><span class="k">Simulador de revenda</span><h2>Quanto você investe e quanto pode lucrar</h2><p>Coloque o custo real de cada peça (o preço que você pagar no atacado) e o preço que pretende vender. A conta é sua, sem promessa.</p>
<div class="pre"><button data-q="10" class="on">Começo pequeno · 10 peças</button><button data-q="30">Loja de bairro · 30</button><button data-q="60">Revenda forte · 60</button></div>
<div class="f"><label>Quantidade de peças <output id="oq">10</output></label><input id="q" type="range" min="3" max="120" value="10"></div>
<div class="f"><label>Custo médio por peça <output id="oc">R$ 70</output></label><input id="c" type="range" min="20" max="250" step="5" value="70"></div>
<div class="f"><label>Preço de venda por peça <output id="ov">R$ 129</output></label><input id="v" type="range" min="30" max="450" step="5" value="129"></div>
</div>
<div class="res" aria-live="polite"><div><span>Você investe</span><b id="ri">R$ 700</b></div><div><span>Você fatura vendendo tudo</span><b id="rf">R$ 1.290</b></div><div class="big"><span>Seu lucro</span><b id="rl">R$ 590</b></div><div><span>Margem sobre a venda</span><b id="rm">46%</b></div><div><span>Peças para pagar o investimento</span><b id="rp">6</b></div><small>Conta simples, sem frete, taxas da maquininha e embalagem. Some esses custos ao custo da peça para chegar no seu lucro real.</small></div>
</div></div></section>

<section><div class="w"><div class="sh rv"><span class="k">Escolha o seu jeito</span><h2>3 caminhos para começar a revender</h2><p>Não precisa de loja. Comece pelo canal que você já usa todo dia.</p></div>
<div class="paths">
<div class="pc rv"><div class="n">01</div><h3>Instagram e status</h3><ul><li>Foto boa de cada peça e preço claro</li><li>Stories com prova: etiqueta, malha, caimento</li><li>Reserva por 24 horas para criar urgência</li></ul></div>
<div class="pc rv" style="--d:100ms"><div class="n">02</div><h3>Venda de mão em mão</h3><ul><li>Trabalho, academia, faculdade, condomínio</li><li>Leve a peça para a pessoa sentir o tecido</li><li>Ofereça o combo camiseta e short</li></ul></div>
<div class="pc rv" style="--d:200ms"><div class="n">03</div><h3>Sua loja ou arara</h3><ul><li>Atacado a partir de 6 peças na loja física</li><li>Misture grifes e tamanhos no mesmo pedido</li><li>Reponha toda semana o que mais saiu</li></ul></div>
</div></div></section>

<section id="kit"><div class="w"><div class="sh rv"><span class="k">Kit de largada</span><h2>As peças com mais reposição na loja hoje</h2><p>Escolhemos as peças que a SP Grifes tem em maior quantidade: são as que mais vendem e que você consegue repor sem ficar sem estoque. Toque para ver cores e tamanhos na loja online.</p></div>
<div class="chips rv" role="tablist">{chips}</div><div class="kit">{kit}</div>
<div class="cta rv" style="margin-top:28px"><a class="btn b1" href="{utm(LOJA, SRC, 'kit')}" target="_blank" rel="noopener">Ver as {N_MOD} peças na loja online</a></div></div></section>

<section><div class="w"><div class="sh rv"><span class="k">Direto da loja</span><h2>Veja como funciona na prática</h2><p>Vídeos gravados na SP Grifes, no Brás. Toque para assistir aqui mesmo.</p></div>
<div class="vids rv">{vhtml}</div>
<div class="cta rv"><a class="btn b2" href="{YT}?sub_confirmation=1" target="_blank" rel="noopener">Inscreva-se no canal do YouTube</a></div></div></section>

<section id="plano"><div class="w"><div class="sh rv"><span class="k">Plano de 7 dias</span><h2>Do zero à primeira venda em uma semana</h2><p>Marque cada passo conforme for fazendo. Fica salvo neste celular.</p></div>
<div class="bar"><i id="pb"></i></div><div class="plan">{plan}</div></div></section>

<section id="duvidas"><div class="w"><div class="sh rv"><span class="k">Dúvidas</span><h2>Perguntas de quem está começando</h2></div>{faq}</div></section>

<section><div class="w"><div class="final rv"><h2>Pronto para o primeiro pedido?</h2><p>Monte seu pedido na loja online com preço de atacado a partir de 3 peças, ou venha ao Brás escolher pessoalmente.</p>
<div class="cta"><a class="btn b1" href="{utm(LOJA, SRC, 'final')}" target="_blank" rel="noopener">Ver na loja online</a><a class="btn b2" href="{GRUPO}" target="_blank" rel="noopener">Entrar no Grupo VIP</a><a class="btn b2" href="{share}" target="_blank" rel="noopener">Enviar para um amigo</a></div></div></div></section>
</main>
<footer><div class="w"><div><b>SP Grifes · Revenda</b>{E(END)}<br>{HOR}<br><br>Compre só pelos canais oficiais da SP Grifes. Na dúvida, não faça Pix antes de confirmar com a equipe.</div>
<div><b>Canais oficiais</b><a href="{utm(LOJA, SRC, 'rodape')}" target="_blank" rel="noopener">Loja online</a><a href="{GRUPO}" target="_blank" rel="noopener">Grupo VIP de novidades</a><a href="{BLOG}" target="_blank" rel="noopener">Blog SP Grifes</a><a href="{MAPS}" target="_blank" rel="noopener">Como chegar à loja</a></div>
<div><b>Acompanhe</b><a href="{IG}" target="_blank" rel="noopener">Instagram @fabioleiite</a><a href="{YT}" target="_blank" rel="noopener">Canal no YouTube</a><a href="{BLOG}fornecedor-roupas-importadas/" target="_blank" rel="noopener">Fornecedor de roupas importadas</a></div></div></footer>
<nav class="dock" aria-label="Atalhos"><a href="#simulador">Simular lucro</a><a class="l" href="{utm(LOJA, SRC, 'barra')}" target="_blank" rel="noopener">Loja online</a></nav>
<script>
(function(){{
var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{threshold:.12}});document.querySelectorAll('.rv').forEach(function(el){{io.observe(el)}});
function $(i){{return document.getElementById(i)}}function brl(n){{return 'R$ '+Math.round(n).toLocaleString('pt-BR')}}
function calc(){{var q=+$('q').value,c=+$('c').value,v=+$('v').value;$('oq').textContent=q;$('oc').textContent=brl(c);$('ov').textContent=brl(v);
var i=q*c,f=q*v,l=f-i;$('ri').textContent=brl(i);$('rf').textContent=brl(f);$('rl').textContent=brl(l);$('rm').textContent=(f>0?Math.round(l/f*100):0)+'%';$('rp').textContent=v>0?Math.ceil(i/v):'-'}}
['q','c','v'].forEach(function(k){{$(k).addEventListener('input',function(){{document.querySelectorAll('.pre button').forEach(function(b){{b.classList.remove('on')}});calc()}})}});
document.querySelectorAll('.pre button').forEach(function(b){{b.addEventListener('click',function(){{document.querySelectorAll('.pre button').forEach(function(x){{x.classList.remove('on')}});b.classList.add('on');$('q').value=b.dataset.q;calc()}})}});calc();
document.querySelectorAll('.chips button').forEach(function(b){{b.addEventListener('click',function(){{document.querySelectorAll('.chips button').forEach(function(x){{x.classList.remove('on')}});b.classList.add('on');var f=b.dataset.f;document.querySelectorAll('.kc').forEach(function(k){{k.classList.toggle('hide',f!=='*'&&k.dataset.c!==f)}})}})}});
var K='spg-revenda-plano',st={{}};try{{st=JSON.parse(localStorage.getItem(K)||'{{}}')}}catch(e){{}}
function prog(){{var bs=document.querySelectorAll('.day input'),n=0;bs.forEach(function(b){{b.closest('.day').classList.toggle('ok',b.checked);if(b.checked)n++}});$('pb').style.width=(n/bs.length*100)+'%'}}
document.querySelectorAll('.day input').forEach(function(b){{b.checked=!!st[b.dataset.i];b.addEventListener('change',function(){{st[b.dataset.i]=b.checked;try{{localStorage.setItem(K,JSON.stringify(st))}}catch(e){{}}prog()}})}});prog();
}})();
</script>{VID_JS}</body></html>'''
import os
os.makedirs('/home/claude/rh/sites/revenda', exist_ok=True)
open('/home/claude/rh/sites/revenda/index.html', 'w').write(page)
print(len(page), len(KIT), VIDS)
