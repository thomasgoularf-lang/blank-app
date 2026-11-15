// Print each HTML file to a one-page A4 PDF, shrinking the font slightly if a page overflows.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const [, , inDir, outDir] = process.argv;
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const A4_PX = 1122; // 297mm at 96 dpi
  for (const f of fs.readdirSync(inDir).filter(x => x.endsWith('.html')).sort()) {
    await page.goto('file://' + path.resolve(inDir, f));
    await page.evaluate(() => document.fonts.ready);
    const isLetter = await page.evaluate(() => document.body.classList.contains('letter'));
    let fs_pt = isLetter ? 10.6 : 10.2;
    for (let i = 0; i < 20; i++) {
      await page.evaluate(v => {
        const t = document.body.classList.contains('letter') ? document.body : document.body;
        t.style.setProperty('--fs', v + 'pt');
        if (document.body.classList.contains('letter')) document.body.style.fontSize = v + 'pt';
      }, fs_pt);
      const h = await page.evaluate(() => document.querySelector('.page').scrollHeight);
      if (h <= A4_PX - 2) break;
      fs_pt = Math.round((fs_pt - 0.15) * 100) / 100;
    }
    const out = path.join(outDir, f.replace(/\.html$/, '.pdf'));
    await page.pdf({ path: out, format: 'A4', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
    console.log(f, 'font', fs_pt + 'pt');
  }
  await browser.close();
})();
