/* Grades + Finalizar contagem + Histórico (SP Grifes). Funciona em todas as páginas de checklist. */
(function(){
var URL_DB='https://cuiqmczhtcrrxafmzmhh.supabase.co/rest/v1/checklist_contagens';
var KEY_DB='sb_publishable_2A36EPYGbgAXMOPj0Up6yg_IxSsYmak';
var H={apikey:KEY_DB,Authorization:'Bearer '+KEY_DB,'Content-Type':'application/json'};
var main=document.querySelector('main');
if(!main)return;
var cards=[].slice.call(main.querySelectorAll('.card'));
if(!cards.length)return;
var menu=(location.pathname.match(/(checklist-[a-z0-9-]+)/)||[,'checklist'])[1];
var titulo=(typeof CFG!=='undefined'&&CFG&&CFG.titulo)||document.title||menu;
var d=new Date(),dia=d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2);
var SK='grades-'+menu+'-'+dia;
var gr={};try{gr=JSON.parse(localStorage.getItem(SK)||'{}')||{};}catch(e){}
function save(){try{localStorage.setItem(SK,JSON.stringify(gr));}catch(e){}}

var css=document.createElement('style');
css.textContent='.gr{grid-column:1/-1;display:flex;align-items:center;justify-content:center;gap:8px;margin:8px 0 2px;padding:8px;border-radius:12px;background:rgba(0,0,0,.25);font:700 13px system-ui,sans-serif;color:#fff}'+
'.gr button{width:44px;height:44px;border-radius:12px;border:0;background:#d4af37;color:#111;font:800 24px system-ui;cursor:pointer}'+
'.gr b{min-width:34px;text-align:center;font-size:24px}.gr.zero b{color:#ff6b6b}.gr.baixo b{color:#ffb020}'+
'.gr span{font-size:12px;opacity:.9}'+
'#hs-fin{position:sticky;bottom:10px;z-index:30;display:block;width:calc(100% - 24px);max-width:660px;margin:16px auto;padding:16px;border:0;border-radius:14px;background:#d4af37;color:#111;font:800 17px system-ui,sans-serif;box-shadow:0 6px 18px rgba(0,0,0,.5);cursor:pointer}'+
'#hs-fin.conf{background:#1fa34a;color:#fff}'+
'#hs-msg{max-width:660px;margin:6px auto;padding:10px 14px;border-radius:10px;font:600 14px system-ui,sans-serif;color:#fff;display:none}'+
'#hs-his{max-width:680px;margin:24px auto 90px;padding:0 12px;font-family:system-ui,sans-serif;color:#fff}'+
'#hs-his h2{font-size:18px;margin:0 0 10px;color:#d4af37}'+
'#hs-his details{background:#1b1b1b;border:1px solid #333;border-radius:12px;margin-bottom:8px;overflow:hidden}'+
'#hs-his summary{padding:14px;font-weight:700;font-size:15px;cursor:pointer;display:flex;justify-content:space-between;gap:8px}'+
'#hs-his summary i{font-style:normal;font-weight:600;font-size:12px;opacity:.85}'+
'#hs-his .al{color:#ff6b6b}'+
'.hs-r{display:flex;align-items:center;gap:10px;padding:8px 14px;border-top:1px solid #2a2a2a;font-size:14px}'+
'.hs-r .t{width:48px;height:48px;border-radius:8px;object-fit:cover;background:#333;flex:none;cursor:zoom-in;display:block}'+
'.hs-r .dot{width:48px;height:48px;border-radius:8px;flex:none}'+
'.hs-r .nm2{flex:1;text-transform:uppercase;font-weight:600}'+
'.hs-r .g{font-weight:800;font-size:16px;white-space:nowrap}'+
'.hs-r.low .g{color:#ff6b6b}.hs-r.no{color:#ff6b6b}.hs-r.no .g{font-size:13px}'+
'#hs-z{position:fixed;inset:0;background:rgba(0,0,0,.9);z-index:99;display:none;align-items:center;justify-content:center}#hs-z.on{display:flex}#hs-z img{max-width:96%;max-height:92%;border-radius:10px}';
document.head.appendChild(css);

function nome(c){var e=c.querySelector('.sw b')||c.querySelector('.ph .n')||c.querySelector('.nm');
 if(!e)return'Item';var x=e.cloneNode(true);[].forEach.call(x.querySelectorAll('small,.st'),function(s){s.remove();});return x.textContent.replace(/\s+/g,' ').trim();}
function thumb(c){var i=c.querySelector('img');if(i&&i.src)return{src:i.src};var s=c.querySelector('.sw i');if(s)return{cor:getComputedStyle(s).backgroundColor};return null;}
var nomes=cards.map(nome);

function setGr(i,v){v=Math.max(0,Math.min(999,v));gr[i]=v;save();var el=cards[i].querySelector('.gr');if(el)pintaGr(el,v);}
function pintaGr(el,v){el.querySelector('b').textContent=v;el.classList.toggle('zero',v===0);el.classList.toggle('baixo',v>0&&v<=2);
 el.querySelector('span').textContent=v===0?'informe as grades':(v<=2?'pouco: avisar para trazer':'grades');}
function sync(i){var c=cards[i],ok=c.classList.contains('ok'),el=c.querySelector('.gr');
 if(ok&&!el){el=document.createElement('div');el.className='gr';
  el.innerHTML='<button type="button">−</button><b>0</b><button type="button">+</button><span></span>';
  var bs=el.querySelectorAll('button');
  bs[0].onclick=function(e){e.stopPropagation();setGr(i,(gr[i]||0)-1);};
  bs[1].onclick=function(e){e.stopPropagation();setGr(i,(gr[i]||0)+1);};
  c.appendChild(el);pintaGr(el,gr[i]||0);}
 else if(!ok&&el){el.remove();delete gr[i];save();}}
cards.forEach(function(c,i){sync(i);new MutationObserver(function(){sync(i);}).observe(c,{attributes:true,attributeFilter:['class']});});

var msg=document.createElement('div');msg.id='hs-msg';
var bt=document.createElement('button');bt.id='hs-fin';bt.type='button';bt.textContent='Finalizar contagem';
var his=document.createElement('section');his.id='hs-his';
var z=document.createElement('div');z.id='hs-z';z.innerHTML='<img alt="">';z.onclick=function(){z.classList.remove('on');};
main.parentNode.insertBefore(msg,main.nextSibling);msg.after(bt);bt.after(his);document.body.appendChild(z);
function aviso(t,cor){msg.style.display='block';msg.style.background=cor||'#333';msg.textContent=t;}
function zoom(src){z.querySelector('img').src=src;z.classList.add('on');}

function coleta(){var it=[];cards.forEach(function(c,i){var ok=c.classList.contains('ok'),no=c.classList.contains('no');
 if(ok)it.push({n:nomes[i],s:'ok',g:gr[i]||0});else if(no)it.push({n:nomes[i],s:'no'});});return it;}

var tmr;function rb(){bt.classList.remove('conf');bt.textContent='Finalizar contagem';delete bt.dataset.c;}
bt.onclick=function(){
 var it=coleta();
 if(!it.length){aviso('Marque TENHO ou NÃO TENHO em algum item antes de finalizar.','#a33');return;}
 var sem=it.filter(function(x){return x.s==='ok'&&!x.g;}).length;
 if(!bt.dataset.c){bt.dataset.c=1;bt.classList.add('conf');
  bt.textContent=sem?('Faltam grades em '+sem+' item(ns). Toque de novo para finalizar assim'):'Toque de novo para confirmar';
  clearTimeout(tmr);tmr=setTimeout(rb,5000);return;}
 rb();bt.disabled=true;bt.textContent='Salvando…';
 var al=it.filter(function(x){return x.s==='ok'&&x.g<=2;}).length;
 fetch(URL_DB,{method:'POST',headers:Object.assign({Prefer:'return=minimal'},H),body:JSON.stringify({menu:menu,titulo:titulo,itens:it,alertas:al})})
 .then(function(r){if(!r.ok)throw new Error(r.status);aviso('Contagem salva e enviada. '+(al?al+' item(ns) com poucas grades: aviso enviado.':''),'#1fa34a');carrega();})
 .catch(function(){aviso('Não consegui salvar. Confira a internet e tente de novo.','#a33');})
 .then(function(){bt.disabled=false;bt.textContent='Finalizar contagem';});
};

function quando(s){var x=new Date(s);var p=function(n){return('0'+n).slice(-2);};
 return p(x.getDate())+'/'+p(x.getMonth()+1)+' às '+p(x.getHours())+':'+p(x.getMinutes());}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function carrega(){
 fetch(URL_DB+'?menu=eq.'+encodeURIComponent(menu)+'&select=id,criado_em,itens,alertas&order=criado_em.desc&limit=40',{headers:H})
 .then(function(r){return r.json();}).then(function(rows){
  if(!rows.length){his.innerHTML='<h2>Histórico de contagens</h2><div style="opacity:.7;font-size:14px">Nenhuma contagem finalizada ainda.</div>';return;}
  his.innerHTML='<h2>Histórico de contagens</h2>';
  rows.forEach(function(r,k){
   var tem=r.itens.filter(function(x){return x.s==='ok';}),nao=r.itens.filter(function(x){return x.s==='no';});
   var det=document.createElement('details');if(k===0)det.open=false;
   var h='<summary><span>'+quando(r.criado_em)+'</span><i>'+tem.length+' tem · '+nao.length+' não tem'+(r.alertas?' · <span class="al">'+r.alertas+' alerta(s)</span>':'')+'</i></summary>';
   tem.forEach(function(x){var ix=nomes.indexOf(x.n),t=ix>=0?thumb(cards[ix]):null,low=(x.g||0)<=2;
    h+='<div class="hs-r'+(low?' low':'')+'">'+(t&&t.src?'<img class="t" src="'+t.src+'" data-z="1">':(t&&t.cor?'<div class="dot" style="background:'+t.cor+'"></div>':'<div class="dot" style="background:#333"></div>'))+
    '<div class="nm2">'+esc(x.n)+'</div><div class="g">'+(x.g||0)+' grade(s)'+(low?' ⚠':'')+'</div></div>';});
   nao.forEach(function(x){var ix=nomes.indexOf(x.n),t=ix>=0?thumb(cards[ix]):null;
    h+='<div class="hs-r no">'+(t&&t.src?'<img class="t" src="'+t.src+'" data-z="1">':(t&&t.cor?'<div class="dot" style="background:'+t.cor+'"></div>':'<div class="dot" style="background:#333"></div>'))+
    '<div class="nm2">'+esc(x.n)+'</div><div class="g">NÃO TEM</div></div>';});
   det.innerHTML=h;his.appendChild(det);});
  [].forEach.call(his.querySelectorAll('img[data-z]'),function(im){im.onclick=function(){zoom(im.src);};});
 }).catch(function(){his.innerHTML='<h2>Histórico de contagens</h2><div style="opacity:.7;font-size:14px">Não foi possível carregar o histórico agora.</div>';});
}
carrega();
})();
