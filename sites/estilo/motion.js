/* Movimento do Supergrifes: GSAP (rolagem) + Three.js (poeira dourada). Tudo opcional e leve. */
(function () {
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  function load(src) {
    return new Promise(function (ok, fail) {
      var s = document.createElement('script');
      s.src = src; s.async = true; s.onload = ok; s.onerror = fail;
      document.head.appendChild(s);
    });
  }

  function startGsap() {
    var gsap = window.gsap, ST = window.ScrollTrigger;
    if (!gsap || !ST) return;
    gsap.registerPlugin(ST);

    var bar = document.createElement('div');
    bar.className = 'prog';
    document.body.appendChild(bar);
    gsap.to(bar, { scaleX: 1, ease: 'none', scrollTrigger: { start: 0, end: 'max', scrub: 0.3 } });

    gsap.from('.hero .tx > *', { y: 30, opacity: 0, duration: 1, ease: 'power3.out', stagger: 0.13, delay: 0.15, clearProps: 'all' });

    var img = document.querySelector('.hero .ph img');
    if (img) {
      gsap.to(img, { yPercent: 8, scale: 1.08, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: 0.6 } });
    }

    document.querySelectorAll('section h2').forEach(function (h) {
      gsap.from(h, { y: 36, opacity: 0, duration: 0.9, ease: 'power3.out', clearProps: 'all', scrollTrigger: { trigger: h, start: 'top 88%', once: true } });
    });
  }

  function startThree() {
    var hero = document.querySelector('.hero');
    if (!hero || !window.WebGLRenderingContext) return;
    import('https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js').then(function (THREE) {
      var box = document.createElement('div');
      box.className = 'dust';
      box.setAttribute('aria-hidden', 'true');
      hero.appendChild(box);
      var renderer;
      try { renderer = new THREE.WebGLRenderer({ antialias: false, alpha: true }); } catch (e) { box.remove(); return; }
      renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
      box.appendChild(renderer.domElement);

      var scene = new THREE.Scene();
      var cam = new THREE.PerspectiveCamera(50, 1, 0.1, 50);
      cam.position.z = 8;

      // textura redonda e macia para cada grão
      var c = document.createElement('canvas'); c.width = c.height = 64;
      var x = c.getContext('2d'), g = x.createRadialGradient(32, 32, 0, 32, 32, 32);
      g.addColorStop(0, 'rgba(255,240,200,1)'); g.addColorStop(0.4, 'rgba(201,164,92,.55)'); g.addColorStop(1, 'rgba(201,164,92,0)');
      x.fillStyle = g; x.fillRect(0, 0, 64, 64);

      var N = innerWidth < 700 ? 90 : 220, pos = new Float32Array(N * 3), spd = new Float32Array(N);
      for (var i = 0; i < N; i++) {
        pos[i * 3] = (Math.random() - 0.5) * 18;
        pos[i * 3 + 1] = (Math.random() - 0.5) * 11;
        pos[i * 3 + 2] = (Math.random() - 0.5) * 8;
        spd[i] = 0.15 + Math.random() * 0.35;
      }
      var geo = new THREE.BufferGeometry();
      geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
      var pts = new THREE.Points(geo, new THREE.PointsMaterial({ size: 0.22, map: new THREE.CanvasTexture(c), transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, opacity: 0.85 }));
      scene.add(pts);

      function size() {
        var w = box.clientWidth || 300, h = box.clientHeight || 300;
        renderer.setSize(w, h, false); cam.aspect = w / h; cam.updateProjectionMatrix();
      }
      size(); addEventListener('resize', size);

      var mx = 0, my = 0, visible = true;
      addEventListener('pointermove', function (e) { mx = e.clientX / innerWidth - 0.5; my = e.clientY / innerHeight - 0.5; }, { passive: true });
      if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { visible = es[0].isIntersecting; }).observe(hero);

      var last = performance.now();
      (function loop(t) {
        requestAnimationFrame(loop);
        if (!visible || document.hidden) { last = t; return; }
        var dt = Math.min((t - last) / 1000, 0.05); last = t;
        var p = geo.attributes.position.array;
        for (var i = 0; i < N; i++) {
          p[i * 3 + 1] += spd[i] * dt;
          p[i * 3] += Math.sin(t / 1800 + i) * 0.003;
          if (p[i * 3 + 1] > 5.5) p[i * 3 + 1] = -5.5;
        }
        geo.attributes.position.needsUpdate = true;
        pts.rotation.y += ((mx * 0.5) - pts.rotation.y) * 0.04;
        pts.rotation.x += ((my * 0.25) - pts.rotation.x) * 0.04;
        renderer.render(scene, cam);
      })(last);
      requestAnimationFrame(function () { box.classList.add('on'); });
    }).catch(function () {});
  }

  function init() {
    load('https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js')
      .then(function () { return load('https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js'); })
      .then(startGsap).catch(function () {});
    (window.requestIdleCallback || function (f) { setTimeout(f, 800); })(startThree);
  }
  if (document.readyState === 'complete') init(); else addEventListener('load', init);
})();
