function animateCounter(el, target, suffix = '', duration = 2000) {
    if (!el) return;
    let start = 0, step = target / duration * 16;
    let t = setInterval(() => {
        start = Math.min(start + step, target);
        el.textContent = Math.round(start) + suffix;
        if (start >= target) clearInterval(t);
    }, 16);
}

document.addEventListener('DOMContentLoaded', () => {
    // Les valeurs cibles sont injectées par le template home.html en fin de fichier
    
    const obs = new IntersectionObserver((entries) => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                e.target.classList.add('revealed');
                e.target.querySelectorAll('.skill-fill').forEach(b => { b.style.width = b.dataset.w + '%' });
                obs.unobserve(e.target);
            }
        });
    }, { threshold: .12 });
    document.querySelectorAll('.reveal').forEach(el => obs.observe(el));

    window.addEventListener('scroll', () => {
        const secs = document.querySelectorAll('section');
        const links = document.querySelectorAll('.nav-links a');
        let cur = '';
        secs.forEach(s => { if (window.scrollY >= s.offsetTop - 80) cur = s.id });
        links.forEach(a => { a.style.color = a.getAttribute('href') === '#' + cur ? 'var(--python2)' : '' });
    });
});