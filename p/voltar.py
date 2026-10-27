"""Coloca o botão "← Central" e o noindex em cada página hospedada em /Rh/p/.
Também troca links de artefatos do Claude pelas páginas do site, quando a página existe aqui.
Uso: python3 -I p/voltar.py  (rodar na raiz do repositório Rh)"""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))

# artefato do Claude -> página hospedada (só entra aqui o que já existe no site)
MAPA = {
    'K6GBYs7zA4MWsPQ5SArZgG': 'estante-colmeia',
    'JFVN83cWmYwTzRnKcjHez7': 'kit-da-marca',
    'ET1fNSToAit6obM6D23BXP': 'ciclo-de-palavras',
    'BiWzuqzkNWswPtGLNP2uf6': 'contagem-perfumes',
    'AR9PyY4U5hCN3kQspLLzky': 'comandos-do-boss',
    'B5cHPp7kC2fgESXRKXiB1C': 'pia-da-loja',
    'GLYExSQVMiP2sEjWt7E8AG': 'parede-vm',
    'G11UVv3H1wB1dTzFPSBMN9': 'retirada-cte',
    '9evRKyCjmAPkL5ERA97RVN': 'apresentacao',
    'L3PLzLyfqJpTzNxoE3MAwv': 'cueca-performance',
    'GLr7p8G9oRp43ZyLaoYM4y': 'plaquinha-google',
    'NXaiFtAjax8n5yGhTacv6e': 'sp-exclusive',
    'P2mxipwJrqVimWA4zu4zbF': 'monograma-fl',
    'XFHQZbkqf6KnkL76Gte2Mf': 'painel-de-vendas',
    'JDRfiAq3eGYRrMgPZfxQWj': 'raio-x-bagy',
    'ATDTy62XTTYUrVr4MHUywe': 'dossie-do-robo',
    'QiMZqKnnqJ2hwD3ye4Gqmq': 'lulu-automacoes',
    'HRMitd6XizGJf2RTsvr43v': 'fluxos-da-lulu',
    '1tBDKNraBwbRUAegtGn3Qf': 'deposito-do-site',
    '8Ys1H6W2a6mwy5V5AnEfS7': 'relatorio-multas',
}

BOTAO = ('<a id="cc-voltar" href="/Rh/central/" style="position:fixed;z-index:2147483000;'
         'left:max(12px,env(safe-area-inset-left,0px));bottom:calc(12px + env(safe-area-inset-bottom,0px));'
         'font:600 13px/1 -apple-system,BlinkMacSystemFont,\'Segoe UI\',sans-serif;color:#fff;background:rgba(20,20,20,.86);'
         'text-decoration:none;padding:10px 14px;border-radius:99px;box-shadow:0 2px 10px rgba(0,0,0,.18)">← Central</a>')
NOINDEX = '<meta name="robots" content="noindex,nofollow">'


def existe(pasta):
    return os.path.isfile(os.path.join(BASE, pasta, 'index.html'))


def ajusta(caminho):
    with open(caminho, encoding='utf-8') as f:
        s = f.read()
    orig = s
    if 'id="cc-voltar"' not in s:
        i = s.rfind('</body>')
        s = s[:i] + BOTAO + '\n' + s[i:] if i >= 0 else s + '\n' + BOTAO
    if 'name="robots"' not in s:
        s = s.replace('<head>', '<head>' + NOINDEX, 1) if '<head>' in s else NOINDEX + s

    def troca(m):
        pasta = MAPA.get(m.group(2))
        return '/Rh/p/%s/' % pasta if pasta and existe(pasta) else m.group(0)
    s = re.sub(r'https://claude\.ai/(code/)?artifact/([A-Za-z0-9-]+)', troca, s)
    if s != orig:
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(s)
        return True
    return False


if __name__ == '__main__':
    for nome in sorted(os.listdir(BASE)):
        arq = os.path.join(BASE, nome, 'index.html')
        if os.path.isfile(arq):
            print(('ajustado ' if ajusta(arq) else 'ok       ') + nome)
