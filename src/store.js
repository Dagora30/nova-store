export const money=n=>new Intl.NumberFormat('es-CO',{style:'currency',currency:'COP',maximumFractionDigits:0}).format(n)+' COP';
export const normalize=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
export const quantity=n=>Math.max(1,Math.min(10,Math.floor(Number(n)||1)));
export function load(k){try{const v=JSON.parse(localStorage.getItem(k));return Array.isArray(v)?v:[]}catch{return []}}
export function save(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch{/* Storage blocked: session still works. */}}
export const cartTotal=cart=>cart.reduce((s,p)=>s+p.price*p.qty,0);
export function addLine(cart,p,size,color,qty){const key=`${p.id}-${size}-${color}`;return cart.some(x=>x.key===key)?cart.map(x=>x.key===key?{...x,qty:quantity(x.qty+qty)}:x):[...cart,{...p,key,size,color,qty:quantity(qty)}]}
export function restoreFavorites(items,products){return [...new Set(items.filter(id=>products.some(p=>p.id===id)))]}
export function restoreCart(items,products){return items.reduce((cart,row)=>{const p=products.find(p=>p.id===row?.id);if(!p)return cart;const sizes=p.category==='Calzado'?['38','39','40','41','42']:p.category==='Accesorios'?['Única']:['S','M','L','XL'];if(!sizes.includes(row.size)||!['Negro','Blanco','Gris'].includes(row.color))return cart;return addLine(cart,p,row.size,row.color,quantity(row.qty))},[])}
