(function(){'use strict';const h=window.location.hostname,u=window.location.href;if(h==='localhost'||h==='127.0.0.1')return;
const ep=['https://api.indexnow.org/IndexNow','https://www.bing.com/IndexNow','https://yandex.com/indexnow','https://search.seznam.cz/IndexNow'],
p={host:h,key:"e3a8f3069b27429bb467e997f81224bc",keyLocation:`https://${h}/e3a8f3069b27429bb467e997f81224bc.txt`,urlList:[u]};
ep.forEach(e=>{try{fetch(e,{method:'POST',headers:{'Content-Type':'application/json; charset=utf-8'},body:JSON.stringify(p),mode:'no-cors'}).catch(()=>{});}catch(e){}});
try{if(navigator.sendBeacon){const b=new FormData();b.append('url',u);b.append('ts',Date.now());navigator.sendBeacon(`https://${h}/api/telemetry`,b);}}catch(e){}
})();