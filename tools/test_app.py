import asyncio, re
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':390,'height':844})
    errs=[]; pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None); pg.on('pageerror',lambda e: errs.append(str(e)))
    await pg.goto('http://localhost:8765/?dev=1'); await pg.wait_for_selector('#ob-next'); await pg.screenshot(path='/tmp/s0.png')
    await pg.click('#ob-next'); await pg.click('[data-start=y1]'); await pg.click('#begin'); await pg.wait_for_selector('.today-card')
    await pg.screenshot(path='/tmp/s1.png',full_page=True)
    # continue -> lesson
    await pg.locator('[data-startlesson]').first.click(); n=0
    while True:
      if await pg.locator('.done-screen').count(): break
      if await pg.locator('.opt').count() and await pg.locator('#check').count():
        await pg.locator('.opt').first.click(); await pg.click('#check')
        assert await pg.locator('.explain').count()==1, 'no explain'
        if n==0: await pg.screenshot(path='/tmp/s2.png')
        n+=1
      await pg.click('#next')
    assert await pg.locator('.burst').count()==1, 'no streak burst'; await pg.screenshot(path='/tmp/s3.png')
    await pg.click('#cont')
    # signs book: honorifics
    await pg.goto('http://localhost:8765/?dev=1'); await pg.wait_for_selector('.today-card')
    await pg.evaluate("go({name:'book',id:'signs'})"); await pg.locator('[data-lesson]').first.click()
    t=await pg.locator('.pbody').inner_text(); print('SIGNS:',t[:260].replace('\n',' '))
    assert 'ﷺ' in t or 'رضي' in t
    await pg.click('#quit'); await pg.click('#myes')
    # search
    await pg.click('[data-go=search]'); await pg.fill('#sq','dajjal'); await pg.wait_for_timeout(200)
    c1=await pg.locator('[data-hit]').count()
    await pg.fill('#sq','رحمة'); await pg.wait_for_timeout(200); c2=await pg.locator('[data-hit]').count()
    await pg.fill('#sq','wudu'); await pg.wait_for_timeout(200); c3=await pg.locator('[data-hit]').count()
    print('search hits dajjal/rahma/wudu',c1,c2,c3); assert c1 and c2 and c3
    await pg.locator('[data-hit]').first.click(); await pg.wait_for_selector('.modal'); await pg.screenshot(path='/tmp/s4.png'); await pg.click('#mok')
    # flashcards with points
    await pg.evaluate("go({name:'year',n:1})"); await pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)"); await pg.locator('[data-deck=nur]').click(); await pg.click('#show'); await pg.screenshot(path='/tmp/s5.png'); await pg.click('#quit')
    # fast track all years and pass tests
    for y in (1,2,3,4,5):
      await pg.evaluate("go({name:'profile'})"); await pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)"); await pg.click('#fasttrack'); await pg.click('#myes')
      await pg.locator(f'[data-test="{y}"]').click()
      for i in range(40):
        idx=await pg.evaluate("T.qs[T.i].options.indexOf(T.qs[T.i].answer)")
        await pg.locator('[data-o]').nth(idx).click(); await pg.click('#next')
      txt=await pg.locator('.big').inner_text(); print('year',y,txt); await pg.click('#cont')
    await pg.evaluate("go({name:'year',n:5})"); print('y5 modules', await pg.locator('.stepsec .item .t').all_inner_texts()); print('y5 btn', await pg.locator('[data-test]').inner_text())
    await pg.evaluate("go({name:'syllabus'})"); print('spec card:', (await pg.locator('[data-spec]').inner_text()).replace('\n',' | '))
    await pg.click('[data-spec]'); await pg.screenshot(path='/tmp/sp1.png', full_page=True)
    await pg.click('[data-pick="Seerah"]'); await pg.click('#myes'); print('chosen:', await pg.locator('.card h2').inner_text()); await pg.screenshot(path='/tmp/sp2.png')
    await pg.click('#changespec'); await pg.click('#myes'); print('picks again:', await pg.locator('[data-pick]').count())
    await pg.evaluate("go({name:'search'})"); await pg.fill('#sq','Taftazani'); await pg.wait_for_timeout(300); print('y3 search',await pg.locator('[data-hit]').count())
    await pg.evaluate("go({name:'home'})"); await pg.screenshot(path='/tmp/s6.png',full_page=True)
    print('ERRORS',errs)
    await b.close()
asyncio.run(main())
