"""Run against npm run preview (requires Python Playwright + Chromium)."""
from playwright.sync_api import sync_playwright
import os
URL=os.environ.get('NOVA_URL','http://127.0.0.1:4173')
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path=os.environ.get('CHROMIUM_PATH'),args=['--no-sandbox'])
 for width in [320,390,768,1024,1440]:
  p=b.new_page(viewport={'width':width,'height':900})
  errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
  p.goto(URL);p.locator('.products article').first.wait_for()
  assert p.locator('.products article').count()==16
  assert p.evaluate('document.documentElement.scrollWidth <= innerWidth'),width
  p.locator('footer').scroll_into_view_if_needed()
  p.wait_for_function("Array.from(document.images).every(i=>i.complete && i.naturalWidth>0)")
  p.get_by_role('button',name='Accesorios',exact=True).click()
  assert p.locator('.products article').count()==2
  p.get_by_role('button',name='Todos',exact=True).click()
  p.get_by_label('Buscar producto').fill('pantalon')
  assert p.locator('.products article').count()==4
  p.get_by_label('Buscar producto').fill('')
  p.get_by_label('Ordenar').select_option('asc')
  assert 'Gorra' in p.locator('.productname').first.inner_text()
  p.get_by_label('Ordenar').select_option('desc')
  assert 'Tenis Motion' in p.locator('.productname').first.inner_text()
  p.locator('input[type=range]').fill('70000')
  assert p.locator('.products article').count()==2
  p.locator('input[type=range]').fill('300000')
  p.get_by_role('button',name='Añadir a favoritos: Camiseta Essential').click()
  p.reload()
  p.get_by_role('button',name='Favoritos: 1').click()
  assert p.locator('.products article').count()==1
  p.get_by_role('button',name='Ver Camiseta Essential').click()
  p.get_by_label('Talla').select_option('L')
  p.get_by_label('Color').select_option('Gris')
  p.get_by_label('Cantidad').fill('2')
  p.get_by_role('button',name='Agregar a la bolsa').click()
  assert '139.800' in p.locator('.drawer').inner_text()
  p.keyboard.press('Escape')
  p.reload()
  p.get_by_role('button',name='Bolsa: 2 productos').click()
  assert 'L / Gris' in p.locator('.drawer').inner_text()
  p.get_by_role('button',name='Aumentar cantidad de Camiseta Essential').click()
  assert '209.700' in p.locator('.drawer').inner_text()
  p.get_by_role('button',name='Reducir cantidad de Camiseta Essential').click()
  p.get_by_role('button',name='Continuar pedido').click()
  assert p.locator('form input').count()==0
  p.get_by_role('button',name='Confirmar pedido simulado').click()
  assert p.get_by_text('¡Pedido simulado!').is_visible()
  p.get_by_role('button',name='Seguir explorando').click()
  p.reload()
  assert p.get_by_role('button',name='Bolsa: 0 productos').is_visible()
  assert not errors,errors
  print(f'PASS {width}px: catálogo, imágenes, responsive, filtros, variantes, favoritos, persistencia, totales, checkout y consola')
  p.close()
 b.close()
