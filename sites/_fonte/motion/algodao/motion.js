/* Movimento do Atlas do Algodão: GSAP (rolagem) + Three.js (algodão 3D). Tudo opcional e leve. */
(function () {
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) return;

  function load(src) {
    return new Promise(function (ok, fail) {
      var s = document.createElement('script');
      s.src = src; s.async = true; s.onload = ok; s.onerror = fail;
      document.head.appendChild(s);
    });
  }

  /* ---------- GSAP: entrada do topo, títulos e barra de progresso ---------- */
  function startGsap() {
    var gsap = window.gsap, ST = window.ScrollTrigger;
    if (!gsap || !ST) return;
    gsap.registerPlugin(ST);

    var bar = document.createElement('div');
    bar.className = 'prog';
    document.body.appendChild(bar);
    gsap.to(bar, { scaleX: 1, ease: 'none', scrollTrigger: { start: 0, end: 'max', scrub: 0.3 } });

    var hs = document.querySelectorAll('.hero small, .hero h1, .hero p, .hero .w > *:not(small):not(h1):not(p)');
    gsap.from(hs, { y: 28, opacity: 0, duration: 0.9, ease: 'power3.out', stagger: 0.12, delay: 0.1, clearProps: 'all' });

    document.querySelectorAll('section h2').forEach(function (h) {
      gsap.from(h, {
        y: 34, opacity: 0, duration: 0.9, ease: 'power3.out', clearProps: 'all',
        scrollTrigger: { trigger: h, start: 'top 88%', once: true }
      });
    });

    var boll = document.querySelector('.boll3d') || document.querySelector('.boll');
    if (boll) {
      gsap.to(boll, { y: 70, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: 0.6 } });
    }
  }

  /* ---------- Three.js: capulho de algodão 3D no topo ---------- */
  function startThree() {
    var hero = document.querySelector('.hero');
    if (!hero || !window.WebGLRenderingContext) return;
    import('https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js').then(function (THREE) {
      var box = document.createElement('div');
      box.className = 'boll3d';
      box.setAttribute('aria-hidden', 'true');
      hero.insertBefore(box, hero.firstChild);

      var renderer;
      try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true }); } catch (e) { box.remove(); return; }
      renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
      box.appendChild(renderer.domElement);

      var scene = new THREE.Scene();
      var cam = new THREE.PerspectiveCamera(35, 1, 0.1, 100);
      cam.position.set(0, 0.2, 9);
      scene.add(new THREE.HemisphereLight(0xffffff, 0xe9dcc2, 1.7));
      var sun = new THREE.DirectionalLight(0xfff6e6, 1.6);
      sun.position.set(3, 5, 6);
      scene.add(sun);

      var group = new THREE.Group();
      scene.add(group);

      // esfera "fofa": icosaedro com ruído nos vértices
      function fluff(r, seed) {
        var g = new THREE.IcosahedronGeometry(r, 4), p = g.attributes.position, v = new THREE.Vector3();
        for (var i = 0; i < p.count; i++) {
          v.fromBufferAttribute(p, i);
          var n = Math.sin(v.x * 3.1 + seed) * Math.cos(v.y * 2.7 - seed) * Math.sin(v.z * 3.3 + seed * 0.5);
          v.multiplyScalar(1 + n * 0.09);
          p.setXYZ(i, v.x, v.y, v.z);
        }
        var nrm = g.attributes.normal;
        for (var j = 0; j < p.count; j++) { v.fromBufferAttribute(p, j).normalize(); nrm.setXYZ(j, v.x, v.y, v.z); }
        return g;
      }
      var mat = new THREE.MeshStandardMaterial({ color: 0xffffff, emissive: 0xf4efe4, emissiveIntensity: 0.2, roughness: 1, metalness: 0 });
      [[0, 0.5, 0, 1.05], [-1.0, 0, 0.1, 0.95], [1.0, 0, 0.1, 0.95], [-0.5, -0.85, 0.3, 0.9], [0.55, -0.85, 0.3, 0.9], [0, 1.4, -0.1, 0.75]].forEach(function (c, i) {
        var m = new THREE.Mesh(fluff(c[3], i * 1.7), mat);
        m.position.set(c[0], c[1], c[2]);
        group.add(m);
      });
      var base = new THREE.Mesh(new THREE.ConeGeometry(1.15, 1.1, 5, 1, true), new THREE.MeshStandardMaterial({ color: 0x7a5a3a, roughness: 0.9, side: THREE.DoubleSide }));
      base.position.set(0, -1.9, 0);
      base.rotation.x = Math.PI;
      group.add(base);
      group.rotation.x = 0.12;

      function size() {
        var w = box.clientWidth || 300, h = box.clientHeight || 300;
        renderer.setSize(w, h, false);
        cam.aspect = w / h; cam.updateProjectionMatrix();
      }
      size(); addEventListener('resize', size);

      var mx = 0, my = 0, visible = true;
      addEventListener('pointermove', function (e) { mx = e.clientX / innerWidth - 0.5; my = e.clientY / innerHeight - 0.5; }, { passive: true });
      if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (es) { visible = es[0].isIntersecting; }).observe(hero);
      }
      var t0 = performance.now();
      (function loop(t) {
        requestAnimationFrame(loop);
        if (!visible || document.hidden) return;
        var s = (t - t0) / 1000;
        group.rotation.y = s * 0.25 + mx * 0.8;
        group.rotation.x = 0.12 + my * 0.4;
        group.position.y = Math.sin(s * 0.9) * 0.12;
        renderer.render(scene, cam);
      })(t0);
      requestAnimationFrame(function () { box.classList.add('on'); hero.classList.add('has3d'); });
    }).catch(function () { /* sem 3D: fica o desenho original */ });
  }

  function init() {
    load('https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js')
      .then(function () { return load('https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js'); })
      .then(startGsap).catch(function () {});
    var idle = window.requestIdleCallback || function (f) { setTimeout(f, 800); };
    idle(startThree);
  }
  if (document.readyState === 'complete') init(); else addEventListener('load', init);
})();
