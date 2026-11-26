import test from 'node:test';
import assert from 'node:assert/strict';
import { quantity, normalize, cartTotal, addLine, restoreCart, restoreFavorites, money, load, save } from '../src/store.js';
const p={id:0,name:'Camiseta',category:'Ropa superior',price:69900};
test('COP and accent-insensitive search',()=>{assert.match(money(69900),/69[.,]900.*COP/);assert.equal(normalize('PANTALÓN'),'pantalon')});
test('integer quantity limits',()=>{for(const [n,v] of [[-2,1],[100,10],[2.7,2],['',1],['bad',1]])assert.equal(quantity(n),v)});
test('variant merges and subtotal',()=>{let c=addLine([],p,'M','Negro',2);c=addLine(c,p,'M','Negro',3);c=addLine(c,p,'L','Negro',1);assert.equal(c.length,2);assert.equal(cartTotal(c),419400);assert.equal(addLine(c,p,'M','Negro',10)[0].qty,10)});
test('storage restoration validates catalog, prices and options',()=>{const c=restoreCart([{id:0,size:'M',color:'Negro',qty:99,price:1},{id:9},{id:0,size:'invalid',color:'Negro',qty:1}], [p]);assert.equal(c.length,1);assert.equal(c[0].price,69900);assert.equal(c[0].qty,10);assert.deepEqual(restoreFavorites([0,0,9],[p]),[0])});
test('unavailable storage does not crash',()=>{assert.deepEqual(load('test'),[]);assert.doesNotThrow(()=>save('test',[]))});
