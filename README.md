# NOVA Store

Demostración personal de una tienda de moda urbana para portafolio de desarrollo web. Catálogo ficticio, sin ventas, cobros, afiliados, publicidad ni recogida de datos.

## Características
- 16 productos, categorías, búsqueda sin distinción de acentos, precio máximo y orden por precio.
- Fichas con talla, color y cantidad; favoritos y bolsa persistentes en localStorage.
- Variantes independientes, cantidades enteras entre 1 y 10 por variante; subtotales y totales en COP.
- Checkout y confirmación simulados, sin campos de datos personales, pagos, backend ni servicios de terceros.
- Diseño adaptable, navegación por teclado, foco visible, cierre con Escape y respeto a movimiento reducido.

## Desarrollo
Requiere Node.js 20.19+ (recomendado 22/24) y npm.
```sh
npm ci
npm run dev
npm test
npm run build
npm run preview
```
Prueba de navegador opcional: iniciar preview, instalar Python Playwright y Chromium (`python -m playwright install chromium`), ejecutar `python tests/browser_smoke.py`. Se puede especificar `NOVA_URL` y `CHROMIUM_PATH`.

## Estructura
- `src/main.jsx`: interfaz y catálogo.
- `src/store.js`: almacenamiento, validación, importes y lógica de carrito.
- `src/style.css`: tema y layouts.
- `public/images/`: fotos ilustrativas WebP locales.
- `tests/`: pruebas unitarias y smoke test.
- `vercel.json`: build estático y encabezados de seguridad.

## Despliegue
Framework Vite, instalación `npm ci`, build `npm run build`, salida `dist`. Sin variables de entorno. Vercel Hobby es para uso personal/no comercial; no utilizar como tienda operativa ni como sitio de promoción comercial sin verificar condiciones y cambiar de plan cuando corresponda.

## Imágenes
Las fotos se obtuvieron de los enlaces originales de Unsplash y se optimizaron localmente. Consulte [licencia](https://unsplash.com/license). Son ilustrativas: no representan inventario real; colores y tallas son opciones simuladas. No existe afiliación con las marcas que pudieran aparecer. Consulte `IMAGE_SOURCES.md` para enlaces de origen. La licencia fotográfica no equivale a autorización independiente de marcas o derechos de imagen.

## Privacidad
Solo se conserva el carrito y los identificadores de favoritos en el navegador. No se solicitan datos personales. Se pueden borrar los datos eliminando los elementos o limpiando el almacenamiento del sitio.
