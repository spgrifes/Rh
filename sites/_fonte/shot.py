import sys, asyncio
from playwright.async_api import async_playwright
async def main(url, out, w, h):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=1)
        await pg.goto(url, wait_until='networkidle', timeout=60000)
        await pg.evaluate("document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'))")
        await pg.evaluate("(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){scrollTo(0,y);await new Promise(r=>setTimeout(r,120))}scrollTo(0,0)})()")
        await pg.wait_for_timeout(2500)
        await pg.wait_for_timeout(1500)
        await pg.screenshot(path=out, full_page=True)
        sw = await pg.evaluate("document.documentElement.scrollWidth")
        broken = await pg.evaluate("[...document.images].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src).slice(0,5)")
        print(out, 'scrollWidth', sw, 'broken', broken)
        await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])))
