/**
 * PAVIS MUGO MURUGA — PORTFOLIO CLIENT JAVASCRIPT
 * Full-stack dynamic features, theme switching, filtering, and animations.
 */

document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initAccessibilityBar();
    initNavbar();
    initTypingEffect();
    initScrollAnimations();
    initProjectFilters();
    initCertificateModal();
    initBackToTop();
    initGitHubStats();
});

/* ==============================================================================
   1. THEME MANAGEMENT (CENTRALIZED)
   ============================================================================== */
function setAppTheme(theme) {
    const validTheme = (theme === 'light') ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', validTheme);
    localStorage.setItem('portfolio-theme', validTheme);
    updateThemeIcons(validTheme);
    updateThemeA11yCards(validTheme);
}

function initTheme() {
    const savedTheme = localStorage.getItem('portfolio-theme') || 'dark';
    setAppTheme(savedTheme);

    const desktopBtn = document.getElementById('theme-toggle-desktop');
    const mobileBtn = document.getElementById('theme-toggle-mobile');

    function toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setAppTheme(nextTheme);
    }

    if (desktopBtn) desktopBtn.addEventListener('click', toggleTheme);
    if (mobileBtn) mobileBtn.addEventListener('click', toggleTheme);
}

function updateThemeIcons(theme) {
    const iconClass = theme === 'dark' ? 'fas fa-moon' : 'fas fa-sun';
    const desktopIcon = document.getElementById('theme-icon-desktop');
    const mobileIcon = document.getElementById('theme-icon-mobile');
    if (desktopIcon) desktopIcon.className = iconClass;
    if (mobileIcon) mobileIcon.className = iconClass;
}

function updateThemeA11yCards(theme) {
    const darkBtn = document.getElementById('a11y-theme-dark');
    const lightBtn = document.getElementById('a11y-theme-light');
    if (darkBtn) darkBtn.classList.toggle('active', theme === 'dark');
    if (lightBtn) lightBtn.classList.toggle('active', theme === 'light');
}

/* ==============================================================================
   2. NAVBAR SCROLL & MOBILE AUTO-CLOSE
   ============================================================================== */
function initNavbar() {
    const navbar = document.getElementById('main-navbar');
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link:not(.dropdown-toggle)');
    const navbarCollapse = document.getElementById('navbarNav');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 40) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Close mobile menu on link click
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navbarCollapse && navbarCollapse.classList.contains('show')) {
                const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
                if (bsCollapse) {
                    bsCollapse.hide();
                }
            }
        });
    });
}

/* ==============================================================================
   3. HERO TYPING EFFECT
   ============================================================================== */
function initTypingEffect() {
    const typedElement = document.getElementById('typed-text');
    if (!typedElement) return;

    const phrases = [
        window.heroTitle || 'Information Technology Student & Web Developer',
        'Python & Django Developer',
        'Practical Software Solutions Builder',
        'IT Systems & Database Enthusiast'
    ];

    let phraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 80;

    function type() {
        const currentPhrase = phrases[phraseIndex];

        if (isDeleting) {
            typedElement.textContent = currentPhrase.substring(0, charIndex - 1);
            charIndex--;
            typingSpeed = 40;
        } else {
            typedElement.textContent = currentPhrase.substring(0, charIndex + 1);
            charIndex++;
            typingSpeed = 80;
        }

        if (!isDeleting && charIndex === currentPhrase.length) {
            typingSpeed = 2200; // Pause at full phrase
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            phraseIndex = (phraseIndex + 1) % phrases.length;
            typingSpeed = 500; // Pause before typing next
        }

        setTimeout(type, typingSpeed);
    }

    type();
}

/* ==============================================================================
   4. SCROLL-DRIVEN ANIMATIONS (INTERSECTION OBSERVER)
   ============================================================================== */
function initScrollAnimations() {
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    if (!animatedElements.length) return;

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                obs.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.12,
        rootMargin: '0px 0px -40px 0px'
    });

    animatedElements.forEach(el => observer.observe(el));
}

/* ==============================================================================
   5. PROJECT CATEGORY FILTERS
   ============================================================================== */
function initProjectFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectItems = document.querySelectorAll('.project-item');

    if (!filterButtons.length || !projectItems.length) return;

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            projectItems.forEach(item => {
                const category = item.getAttribute('data-category');
                if (filterValue === 'all' || category === filterValue) {
                    item.style.display = 'block';
                    setTimeout(() => {
                        item.style.opacity = '1';
                        item.style.transform = 'scale(1)';
                    }, 50);
                } else {
                    item.style.opacity = '0';
                    item.style.transform = 'scale(0.95)';
                    setTimeout(() => {
                        item.style.display = 'none';
                    }, 250);
                }
            });
        });
    });
}

/* ==============================================================================
   6. CERTIFICATE MODAL HANDLER
   ============================================================================== */
function initCertificateModal() {
    const certModalEl = document.getElementById('certModal');
    if (!certModalEl) return;

    certModalEl.addEventListener('show.bs.modal', (event) => {
        const trigger = event.relatedTarget;
        if (!trigger) return;

        const imgUrl = trigger.getAttribute('data-image');
        const title = trigger.getAttribute('data-title');
        const verifyUrl = trigger.getAttribute('data-verify');

        const modalTitle = certModalEl.querySelector('#certModalLabel');
        const modalImg = certModalEl.querySelector('#certModalImage');
        const modalVerify = certModalEl.querySelector('#certModalVerify');

        if (modalTitle) modalTitle.textContent = title || 'Certificate';
        if (modalImg) modalImg.src = imgUrl || '';
        if (modalVerify) {
            if (verifyUrl) {
                modalVerify.href = verifyUrl;
                modalVerify.style.display = 'inline-flex';
            } else {
                modalVerify.style.display = 'none';
            }
        }
    });
}

/* ==============================================================================
   7. BACK TO TOP BUTTON
   ============================================================================== */
function initBackToTop() {
    const backToTopBtn = document.getElementById('back-to-top');
    if (!backToTopBtn) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 400) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }
    });

    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/* ==============================================================================
   8. GITHUB STATS PUBLIC API FETCH
   ============================================================================== */
function initGitHubStats() {
    const username = window.githubUsername;
    if (!username || username === 'YOUR_GITHUB_USERNAME' || username === '') return;

    const reposEl = document.getElementById('gh-repos');
    const followersEl = document.getElementById('gh-followers');
    const followingEl = document.getElementById('gh-following');

    if (!reposEl) return;

    fetch(`https://api.github.com/users/${username}`)
        .then(res => {
            if (!res.ok) throw new Error('User not found');
            return res.json();
        })
        .then(data => {
            if (reposEl) reposEl.textContent = data.public_repos ?? '—';
            if (followersEl) followersEl.textContent = data.followers ?? '—';
            if (followingEl) followingEl.textContent = data.following ?? '—';
        })
        .catch(() => {
            // Silently fallback if rate limited or invalid
            if (reposEl) reposEl.textContent = '—';
            if (followersEl) followersEl.textContent = '—';
            if (followingEl) followingEl.textContent = '—';
        });
}

/* ==============================================================================
   9. ACCESSIBILITY FLOATING BAR & PREFERENCES CONTROLLER (13 FEATURES)
   ============================================================================== */
function initAccessibilityBar() {
    const triggerBtn = document.getElementById('a11y-toggle-btn');
    const panel = document.getElementById('a11y-panel');
    const backdrop = document.getElementById('a11y-backdrop');
    const closeBtn = document.getElementById('a11y-close-btn');

    if (!triggerBtn || !panel) return;

    // 1 & 2. Available text font scale factors (80% to 130%)
    const fontScales = [80, 90, 100, 110, 120, 130];
    let currentScale = parseInt(localStorage.getItem('a11y-font-scale') || '100', 10);
    if (!fontScales.includes(currentScale)) currentScale = 100;

    // Toggle options dictionary (Features 3 - 10, 12)
    const options = {
        highContrast: localStorage.getItem('a11y-high-contrast') === 'true',
        grayscale: localStorage.getItem('a11y-grayscale') === 'true',
        highlightLinks: localStorage.getItem('a11y-highlight-links') === 'true',
        readableFont: localStorage.getItem('a11y-readable-font') === 'true',
        lineSpacing: localStorage.getItem('a11y-line-spacing') === 'true',
        letterSpacing: localStorage.getItem('a11y-letter-spacing') === 'true',
        largeCursor: localStorage.getItem('a11y-large-cursor') === 'true',
        stopAnimations: localStorage.getItem('a11y-stop-animations') === 'true',
        keyboardNav: localStorage.getItem('a11y-keyboard-nav') === 'true'
    };

    // DOM Elements
    const scaleBadge = document.getElementById('a11y-scale-value');
    const btnFontDec = document.getElementById('a11y-font-decrease');
    const btnFontRes = document.getElementById('a11y-font-reset');
    const btnFontInc = document.getElementById('a11y-font-increase');

    const cardHighContrast = document.getElementById('a11y-high-contrast');
    const cardGrayscale = document.getElementById('a11y-grayscale');
    const cardHighlightLinks = document.getElementById('a11y-highlight-links');
    const cardReadableFont = document.getElementById('a11y-readable-font');
    const cardLineSpacing = document.getElementById('a11y-line-spacing');
    const cardLetterSpacing = document.getElementById('a11y-letter-spacing');
    const cardLargeCursor = document.getElementById('a11y-large-cursor');
    const cardStopAnimations = document.getElementById('a11y-stop-animations');
    const cardKeyboardNav = document.getElementById('a11y-keyboard-nav');

    const btnReadAloud = document.getElementById('a11y-read-aloud');
    const readIcon = document.getElementById('a11y-read-icon');
    const readLabel = document.getElementById('a11y-read-label');
    const readSub = document.getElementById('a11y-read-sub');
    const readStatus = document.getElementById('a11y-read-status');

    const btnResetAll = document.getElementById('a11y-reset-all');
    const toast = document.getElementById('a11y-toast');

    // -------------------------------------------------------------
    // Apply Settings Functions
    // -------------------------------------------------------------
    function applyFontScale(scale) {
        currentScale = scale;
        document.documentElement.style.fontSize = scale === 100 ? '' : `${scale}%`;
        if (scaleBadge) scaleBadge.textContent = `${scale}%`;
        localStorage.setItem('a11y-font-scale', scale.toString());
    }

    function applyToggleOption(key, attrName, cardEl, state) {
        options[key] = state;
        document.documentElement.setAttribute(attrName, state ? 'true' : 'false');
        if (cardEl) {
            cardEl.classList.toggle('active', state);
            cardEl.setAttribute('aria-pressed', state ? 'true' : 'false');
        }
        localStorage.setItem(`a11y-${attrName.replace('data-', '')}`, state.toString());
    }

    // Initial state hydration
    applyFontScale(currentScale);
    applyToggleOption('highContrast', 'data-high-contrast', cardHighContrast, options.highContrast);
    applyToggleOption('grayscale', 'data-grayscale', cardGrayscale, options.grayscale);
    applyToggleOption('highlightLinks', 'data-highlight-links', cardHighlightLinks, options.highlightLinks);
    applyToggleOption('readableFont', 'data-readable-font', cardReadableFont, options.readableFont);
    applyToggleOption('lineSpacing', 'data-line-spacing', cardLineSpacing, options.lineSpacing);
    applyToggleOption('letterSpacing', 'data-letter-spacing', cardLetterSpacing, options.letterSpacing);
    applyToggleOption('largeCursor', 'data-large-cursor', cardLargeCursor, options.largeCursor);
    applyToggleOption('stopAnimations', 'data-stop-animations', cardStopAnimations, options.stopAnimations);
    applyToggleOption('keyboardNav', 'data-keyboard-nav', cardKeyboardNav, options.keyboardNav);

    // -------------------------------------------------------------
    // Open / Close Panel (Side Drawer Push Transition)
    // -------------------------------------------------------------
    function openPanel() {
        panel.hidden = false;
        panel.classList.add('open');
        document.body.classList.add('a11y-drawer-open');
        triggerBtn.setAttribute('aria-expanded', 'true');
        triggerBtn.classList.add('active');

        setTimeout(() => {
            if (closeBtn) closeBtn.focus();
        }, 100);
    }

    function closePanel() {
        panel.classList.remove('open');
        document.body.classList.remove('a11y-drawer-open');
        triggerBtn.setAttribute('aria-expanded', 'false');
        triggerBtn.classList.remove('active');

        setTimeout(() => {
            panel.hidden = true;
            triggerBtn.focus();
        }, 350);
    }

    triggerBtn.addEventListener('click', () => {
        const isOpen = panel.classList.contains('open');
        if (isOpen) {
            closePanel();
        } else {
            openPanel();
        }
    });

    if (closeBtn) closeBtn.addEventListener('click', closePanel);
    if (backdrop) backdrop.addEventListener('click', closePanel);

    // Escape key listener
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && panel.classList.contains('open')) {
            closePanel();
        }
    });

    // -------------------------------------------------------------
    // Font Sizing Listeners (1. Text Size + / 2. Text Size -)
    // -------------------------------------------------------------
    if (btnFontDec) {
        btnFontDec.addEventListener('click', () => {
            const idx = fontScales.indexOf(currentScale);
            if (idx > 0) applyFontScale(fontScales[idx - 1]);
        });
    }

    if (btnFontRes) {
        btnFontRes.addEventListener('click', () => {
            applyFontScale(100);
        });
    }

    if (btnFontInc) {
        btnFontInc.addEventListener('click', () => {
            const idx = fontScales.indexOf(currentScale);
            if (idx < fontScales.length - 1) applyFontScale(fontScales[idx + 1]);
        });
    }

    // -------------------------------------------------------------
    // Toggle Button Listeners (Features 3-10, 12)
    // -------------------------------------------------------------
    if (cardHighContrast) {
        cardHighContrast.addEventListener('click', () => {
            applyToggleOption('highContrast', 'data-high-contrast', cardHighContrast, !options.highContrast);
        });
    }

    if (cardGrayscale) {
        cardGrayscale.addEventListener('click', () => {
            applyToggleOption('grayscale', 'data-grayscale', cardGrayscale, !options.grayscale);
        });
    }

    if (cardHighlightLinks) {
        cardHighlightLinks.addEventListener('click', () => {
            applyToggleOption('highlightLinks', 'data-highlight-links', cardHighlightLinks, !options.highlightLinks);
        });
    }

    if (cardReadableFont) {
        cardReadableFont.addEventListener('click', () => {
            applyToggleOption('readableFont', 'data-readable-font', cardReadableFont, !options.readableFont);
        });
    }

    if (cardLineSpacing) {
        cardLineSpacing.addEventListener('click', () => {
            applyToggleOption('lineSpacing', 'data-line-spacing', cardLineSpacing, !options.lineSpacing);
        });
    }

    if (cardLetterSpacing) {
        cardLetterSpacing.addEventListener('click', () => {
            applyToggleOption('letterSpacing', 'data-letter-spacing', cardLetterSpacing, !options.letterSpacing);
        });
    }

    if (cardLargeCursor) {
        cardLargeCursor.addEventListener('click', () => {
            applyToggleOption('largeCursor', 'data-large-cursor', cardLargeCursor, !options.largeCursor);
        });
    }

    if (cardStopAnimations) {
        cardStopAnimations.addEventListener('click', () => {
            applyToggleOption('stopAnimations', 'data-stop-animations', cardStopAnimations, !options.stopAnimations);
        });
    }

    if (cardKeyboardNav) {
        cardKeyboardNav.addEventListener('click', () => {
            applyToggleOption('keyboardNav', 'data-keyboard-nav', cardKeyboardNav, !options.keyboardNav);
        });
    }

    // -------------------------------------------------------------
    // 11. Read Aloud (Browser SpeechSynthesis API)
    // -------------------------------------------------------------
    let isSpeaking = false;
    let speechUtterance = null;

    function stopSpeaking() {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
        }
        isSpeaking = false;
        if (btnReadAloud) {
            btnReadAloud.classList.remove('active');
            btnReadAloud.setAttribute('aria-pressed', 'false');
        }
        if (readLabel) readLabel.textContent = 'Read Aloud';
        if (readSub) readSub.textContent = 'Listen to page content';
        if (readStatus) {
            readStatus.textContent = 'Play';
            readStatus.className = 'badge bg-secondary-subtle text-light small px-2 py-1';
        }
        if (readIcon) readIcon.className = 'fas fa-volume-up fs-5';
        document.documentElement.removeAttribute('data-speaking');
    }

    function startSpeaking() {
        if (!('speechSynthesis' in window)) {
            alert('Text-to-speech is not supported by your browser.');
            return;
        }

        window.speechSynthesis.cancel();

        // Extract key content to read
        const mainContent = document.querySelector('main') || document.body;
        const textElements = mainContent.querySelectorAll('h1, h2, h3, p, .lead, .hero-title');
        let textToRead = '';
        textElements.forEach((el) => {
            const txt = el.innerText.trim();
            if (txt && !el.closest('#a11y-widget') && !el.closest('footer')) {
                textToRead += txt + '. ';
            }
        });

        if (!textToRead.trim()) {
            textToRead = document.title + '. Welcome to Pavis Mugo Muruga portfolio website.';
        }

        speechUtterance = new SpeechSynthesisUtterance(textToRead.substring(0, 4000));
        speechUtterance.rate = 0.95;
        speechUtterance.pitch = 1.0;

        speechUtterance.onend = () => {
            stopSpeaking();
        };

        speechUtterance.onerror = () => {
            stopSpeaking();
        };

        window.speechSynthesis.speak(speechUtterance);
        isSpeaking = true;

        if (btnReadAloud) {
            btnReadAloud.classList.add('active');
            btnReadAloud.setAttribute('aria-pressed', 'true');
        }
        if (readLabel) readLabel.textContent = 'Reading Aloud...';
        if (readSub) readSub.textContent = 'Click to stop speech';
        if (readStatus) {
            readStatus.textContent = 'Stop';
            readStatus.className = 'badge bg-danger text-white small px-2 py-1';
        }
        if (readIcon) readIcon.className = 'fas fa-volume-mute fs-5';
        document.documentElement.setAttribute('data-speaking', 'true');
    }

    if (btnReadAloud) {
        btnReadAloud.addEventListener('click', () => {
            if (isSpeaking) {
                stopSpeaking();
            } else {
                startSpeaking();
            }
        });
    }

    // Stop speech when navigating away
    window.addEventListener('beforeunload', stopSpeaking);

    // -------------------------------------------------------------
    // 13. Reset All Accessibility Settings
    // -------------------------------------------------------------
    if (btnResetAll) {
        btnResetAll.addEventListener('click', () => {
            stopSpeaking();

            // Clear stored preferences
            const a11yKeys = [
                'a11y-font-scale', 'a11y-high-contrast', 'a11y-grayscale',
                'a11y-highlight-links', 'a11y-readable-font', 'a11y-line-spacing',
                'a11y-letter-spacing', 'a11y-large-cursor', 'a11y-stop-animations',
                'a11y-keyboard-nav'
            ];
            a11yKeys.forEach(k => localStorage.removeItem(k));

            // Reset states & styles
            applyFontScale(100);
            applyToggleOption('highContrast', 'data-high-contrast', cardHighContrast, false);
            applyToggleOption('grayscale', 'data-grayscale', cardGrayscale, false);
            applyToggleOption('highlightLinks', 'data-highlight-links', cardHighlightLinks, false);
            applyToggleOption('readableFont', 'data-readable-font', cardReadableFont, false);
            applyToggleOption('lineSpacing', 'data-line-spacing', cardLineSpacing, false);
            applyToggleOption('letterSpacing', 'data-letter-spacing', cardLetterSpacing, false);
            applyToggleOption('largeCursor', 'data-large-cursor', cardLargeCursor, false);
            applyToggleOption('stopAnimations', 'data-stop-animations', cardStopAnimations, false);
            applyToggleOption('keyboardNav', 'data-keyboard-nav', cardKeyboardNav, false);

            // Toast feedback
            if (toast) {
                toast.style.display = 'flex';
                setTimeout(() => {
                    toast.style.display = 'none';
                }, 2500);
            }
        });
    }
}

