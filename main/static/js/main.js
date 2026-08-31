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
   9. ACCESSIBILITY FLOATING BAR & PREFERENCES CONTROLLER
   ============================================================================== */
function initAccessibilityBar() {
    const triggerBtn = document.getElementById('a11y-toggle-btn');
    const panel = document.getElementById('a11y-panel');
    const backdrop = document.getElementById('a11y-backdrop');
    const closeBtn = document.getElementById('a11y-close-btn');

    if (!triggerBtn || !panel) return;

    // 1. Text font scale factors (80% to 130%)
    const fontScales = [80, 90, 100, 110, 120, 130];
    let currentScale = parseInt(localStorage.getItem('a11y-font-scale') || '100', 10);
    if (!fontScales.includes(currentScale)) currentScale = 100;

    // 2. Font Style (Inter, Open Sans, Lexend, Georgia, Atkinson, System)
    let currentFontStyle = localStorage.getItem('a11y-font-style') || 'inter';

    // 3. Toggle options dictionary
    const options = {
        highContrast: localStorage.getItem('a11y-high-contrast') === 'true',
        grayscale: localStorage.getItem('a11y-grayscale') === 'true',
        highlightLinks: localStorage.getItem('a11y-highlight-links') === 'true',
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

    const fontCards = document.querySelectorAll('.a11y-font-card');

    const cardHighContrast = document.getElementById('a11y-high-contrast');
    const cardGrayscale = document.getElementById('a11y-grayscale');
    const cardHighlightLinks = document.getElementById('a11y-highlight-links');
    const cardLineSpacing = document.getElementById('a11y-line-spacing');
    const cardLetterSpacing = document.getElementById('a11y-letter-spacing');
    const cardLargeCursor = document.getElementById('a11y-large-cursor');
    const cardStopAnimations = document.getElementById('a11y-stop-animations');
    const cardKeyboardNav = document.getElementById('a11y-keyboard-nav');

    const btnReadPlay = document.getElementById('a11y-read-play');
    const btnReadStop = document.getElementById('a11y-read-stop');

    const btnVoiceToggle = document.getElementById('a11y-voice-toggle');
    const voiceIcon = document.getElementById('a11y-voice-icon');
    const voiceBtnText = document.getElementById('a11y-voice-btn-text');
    const voiceFeedback = document.getElementById('a11y-voice-feedback');
    const voiceStatusBadge = document.getElementById('a11y-voice-status');

    const btnResetAll = document.getElementById('a11y-reset-all');
    const toast = document.getElementById('a11y-toast');
    const toastText = document.getElementById('a11y-toast-text');

    function showToast(msg) {
        if (!toast) return;
        if (toastText) toastText.textContent = msg || 'Settings updated.';
        toast.style.display = 'flex';
        setTimeout(() => {
            toast.style.display = 'none';
        }, 2500);
    }

    // -------------------------------------------------------------
    // Apply Settings Functions
    // -------------------------------------------------------------
    function applyFontScale(scale) {
        currentScale = scale;
        document.documentElement.style.fontSize = scale === 100 ? '' : `${scale}%`;
        if (scaleBadge) scaleBadge.textContent = `${scale}%`;
        localStorage.setItem('a11y-font-scale', scale.toString());
    }

    function applyFontStyle(fontKey) {
        currentFontStyle = fontKey;
        if (fontKey === 'inter') {
            document.documentElement.removeAttribute('data-font-style');
        } else {
            document.documentElement.setAttribute('data-font-style', fontKey);
        }
        fontCards.forEach(card => {
            card.classList.toggle('active', card.getAttribute('data-font') === fontKey);
        });
        localStorage.setItem('a11y-font-style', fontKey);
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
    applyFontStyle(currentFontStyle);
    applyToggleOption('highContrast', 'data-high-contrast', cardHighContrast, options.highContrast);
    applyToggleOption('grayscale', 'data-grayscale', cardGrayscale, options.grayscale);
    applyToggleOption('highlightLinks', 'data-highlight-links', cardHighlightLinks, options.highlightLinks);
    applyToggleOption('lineSpacing', 'data-line-spacing', cardLineSpacing, options.lineSpacing);
    applyToggleOption('letterSpacing', 'data-letter-spacing', cardLetterSpacing, options.letterSpacing);
    applyToggleOption('largeCursor', 'data-large-cursor', cardLargeCursor, options.largeCursor);
    applyToggleOption('stopAnimations', 'data-stop-animations', cardStopAnimations, options.stopAnimations);
    applyToggleOption('keyboardNav', 'data-keyboard-nav', cardKeyboardNav, options.keyboardNav);

    // -------------------------------------------------------------
    // Open / Close Panel
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

    function togglePanel() {
        if (panel.classList.contains('open')) {
            closePanel();
        } else {
            openPanel();
        }
    }

    triggerBtn.addEventListener('click', togglePanel);
    if (closeBtn) closeBtn.addEventListener('click', closePanel);
    if (backdrop) backdrop.addEventListener('click', closePanel);

    // -------------------------------------------------------------
    // Font Sizing Listeners
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
    // Font Style Picker Listeners
    // -------------------------------------------------------------
    fontCards.forEach(card => {
        card.addEventListener('click', () => {
            const fKey = card.getAttribute('data-font');
            if (fKey) {
                applyFontStyle(fKey);
                showToast(`Font changed to ${card.querySelector('.a11y-font-name')?.textContent || fKey}`);
            }
        });
    });

    // -------------------------------------------------------------
    // Toggle Button Listeners
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
    // Read Aloud (Browser SpeechSynthesis API)
    // -------------------------------------------------------------
    let isSpeaking = false;
    let speechUtterance = null;

    function stopSpeaking() {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
        }
        isSpeaking = false;
        if (btnReadPlay) {
            btnReadPlay.classList.remove('btn-success');
            btnReadPlay.classList.add('btn-success-custom');
            btnReadPlay.innerHTML = '<i class="fas fa-volume-up"></i><span class="fw-bold">Read Page</span>';
        }
        document.documentElement.removeAttribute('data-speaking');
    }

    function startSpeaking() {
        if (!('speechSynthesis' in window)) {
            alert('Text-to-speech is not supported by your browser.');
            return;
        }

        window.speechSynthesis.cancel();

        const mainContent = document.querySelector('main') || document.body;
        const textElements = mainContent.querySelectorAll('h1, h2, h3, p, .lead, .hero-title, .section-title');
        let textToRead = '';
        textElements.forEach((el) => {
            const txt = el.innerText.trim();
            if (txt && !el.closest('#a11y-widget') && !el.closest('footer') && !el.closest('nav')) {
                textToRead += txt + '. ';
            }
        });

        if (!textToRead.trim()) {
            textToRead = document.title + '. Welcome to Pavis Mugo Muruga portfolio.';
        }

        speechUtterance = new SpeechSynthesisUtterance(textToRead.substring(0, 4500));
        speechUtterance.rate = 0.95;
        speechUtterance.pitch = 1.0;

        speechUtterance.onend = stopSpeaking;
        speechUtterance.onerror = stopSpeaking;

        window.speechSynthesis.speak(speechUtterance);
        isSpeaking = true;

        if (btnReadPlay) {
            btnReadPlay.innerHTML = '<i class="fas fa-spinner fa-spin"></i><span class="fw-bold">Reading...</span>';
        }
        document.documentElement.setAttribute('data-speaking', 'true');
    }

    if (btnReadPlay) {
        btnReadPlay.addEventListener('click', () => {
            if (isSpeaking) {
                stopSpeaking();
            } else {
                startSpeaking();
            }
        });
    }

    if (btnReadStop) {
        btnReadStop.addEventListener('click', stopSpeaking);
    }

    window.addEventListener('beforeunload', stopSpeaking);

    // -------------------------------------------------------------
    // Voice Control (Speech Recognition API)
    // -------------------------------------------------------------
    let recognition = null;
    let isListening = false;

    const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SpeechRec) {
        recognition = new SpeechRec();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';

        recognition.onstart = () => {
            isListening = true;
            if (btnVoiceToggle) btnVoiceToggle.classList.add('listening');
            if (voiceBtnText) voiceBtnText.textContent = 'Listening... Speak Now';
            if (voiceIcon) voiceIcon.className = 'fas fa-microphone-slash';
            if (voiceFeedback) {
                voiceFeedback.textContent = 'Listening for commands...';
                voiceFeedback.classList.add('text-primary');
            }
            if (voiceStatusBadge) {
                voiceStatusBadge.textContent = 'Listening';
                voiceStatusBadge.className = 'badge bg-danger small';
            }
        };

        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript.toLowerCase().trim();
            handleVoiceCommand(transcript);
        };

        recognition.onerror = (event) => {
            stopListening();
            if (voiceFeedback) {
                voiceFeedback.textContent = event.error === 'no-speech' ? 'No speech detected. Try again.' : `Voice error: ${event.error}`;
                voiceFeedback.classList.remove('text-primary');
            }
        };

        recognition.onend = () => {
            stopListening();
        };
    }

    function startListening() {
        if (!recognition) {
            alert('Voice speech recognition is not supported in this browser. Please try Google Chrome or Microsoft Edge.');
            return;
        }
        try {
            recognition.start();
        } catch (e) {
            recognition.stop();
        }
    }

    function stopListening() {
        isListening = false;
        if (btnVoiceToggle) btnVoiceToggle.classList.remove('listening');
        if (voiceBtnText) voiceBtnText.textContent = 'Start Voice Control';
        if (voiceIcon) voiceIcon.className = 'fas fa-microphone';
        if (voiceStatusBadge) {
            voiceStatusBadge.textContent = 'Alt+V';
            voiceStatusBadge.className = 'badge bg-secondary-custom small';
        }
    }

    function handleVoiceCommand(cmd) {
        if (voiceFeedback) {
            voiceFeedback.textContent = `Heard: "${cmd}"`;
        }

        // Navigation commands
        if (cmd.includes('home') || cmd.includes('go home')) {
            showToast('Navigating to Home...');
            setTimeout(() => { window.location.href = '/'; }, 600);
        } else if (cmd.includes('about')) {
            showToast('Navigating to About...');
            setTimeout(() => { window.location.href = '/about/'; }, 600);
        } else if (cmd.includes('skills') || cmd.includes('skill')) {
            showToast('Navigating to Skills...');
            setTimeout(() => { window.location.href = '/skills/'; }, 600);
        } else if (cmd.includes('project') || cmd.includes('projects')) {
            showToast('Navigating to Projects...');
            setTimeout(() => { window.location.href = '/projects/'; }, 600);
        } else if (cmd.includes('cv') || cmd.includes('resume')) {
            showToast('Opening CV / Resume...');
            setTimeout(() => { window.location.href = '/resume/'; }, 600);
        } else if (cmd.includes('dashboard')) {
            showToast('Navigating to Dashboard...');
            setTimeout(() => { window.location.href = '/dashboard/'; }, 600);
        } else if (cmd.includes('contact') || cmd.includes('message')) {
            showToast('Navigating to Contact...');
            setTimeout(() => { window.location.href = '/contact/'; }, 600);
        } else if (cmd.includes('credentials') || cmd.includes('credential') || cmd.includes('certificate')) {
            showToast('Navigating to Credentials...');
            setTimeout(() => { window.location.href = '/credentials/'; }, 600);
        }
        // Action & Accessibility commands
        else if (cmd.includes('dark mode') || cmd.includes('dark theme')) {
            setTheme('dark');
            showToast('Dark mode enabled');
        } else if (cmd.includes('light mode') || cmd.includes('light theme')) {
            setTheme('light');
            showToast('Light mode enabled');
        } else if (cmd.includes('read page') || cmd.includes('read aloud') || cmd.includes('speak')) {
            startSpeaking();
            showToast('Reading page aloud');
        } else if (cmd.includes('stop reading') || cmd.includes('stop speech') || cmd.includes('stop speak')) {
            stopSpeaking();
            showToast('Stopped reading');
        } else if (cmd.includes('contrast') || cmd.includes('high contrast')) {
            applyToggleOption('highContrast', 'data-high-contrast', cardHighContrast, !options.highContrast);
            showToast('Contrast toggled');
        } else if (cmd.includes('grayscale')) {
            applyToggleOption('grayscale', 'data-grayscale', cardGrayscale, !options.grayscale);
            showToast('Grayscale toggled');
        } else if (cmd.includes('reset') || cmd.includes('clear')) {
            if (btnResetAll) btnResetAll.click();
        } else if (cmd.includes('close') || cmd.includes('exit')) {
            closePanel();
        } else {
            if (voiceFeedback) {
                voiceFeedback.textContent = `Unrecognized: "${cmd}". Try: "Go home", "Projects", "Read page", "Dark mode"`;
            }
        }
    }

    if (btnVoiceToggle) {
        btnVoiceToggle.addEventListener('click', () => {
            if (isListening) {
                if (recognition) recognition.stop();
                stopListening();
            } else {
                startListening();
            }
        });
    }

    // -------------------------------------------------------------
    // Keyboard Shortcuts (Alt+A, Alt+V, Alt+R, Alt+H, Alt+P, Alt+C, Esc)
    // -------------------------------------------------------------
    document.addEventListener('keydown', (e) => {
        // Close on Esc
        if (e.key === 'Escape' && panel.classList.contains('open')) {
            closePanel();
            return;
        }

        // Alt key combos
        if (e.altKey && !e.ctrlKey && !e.metaKey) {
            const key = e.key.toLowerCase();
            if (key === 'a') {
                e.preventDefault();
                togglePanel();
            } else if (key === 'v') {
                e.preventDefault();
                if (btnVoiceToggle) btnVoiceToggle.click();
            } else if (key === 'r') {
                e.preventDefault();
                if (isSpeaking) {
                    stopSpeaking();
                } else {
                    startSpeaking();
                }
            } else if (key === 'h') {
                e.preventDefault();
                window.location.href = '/';
            } else if (key === 'p') {
                e.preventDefault();
                window.location.href = '/projects/';
            } else if (key === 'c') {
                e.preventDefault();
                window.location.href = '/contact/';
            }
        }
    });

    // -------------------------------------------------------------
    // Reset All Accessibility Settings
    // -------------------------------------------------------------
    if (btnResetAll) {
        btnResetAll.addEventListener('click', () => {
            stopSpeaking();
            stopListening();

            // Clear stored preferences
            const a11yKeys = [
                'a11y-font-scale', 'a11y-font-style', 'a11y-high-contrast', 'a11y-grayscale',
                'a11y-highlight-links', 'a11y-line-spacing', 'a11y-letter-spacing',
                'a11y-large-cursor', 'a11y-stop-animations', 'a11y-keyboard-nav'
            ];
            a11yKeys.forEach(k => localStorage.removeItem(k));

            // Reset states & styles
            applyFontScale(100);
            applyFontStyle('inter');
            applyToggleOption('highContrast', 'data-high-contrast', cardHighContrast, false);
            applyToggleOption('grayscale', 'data-grayscale', cardGrayscale, false);
            applyToggleOption('highlightLinks', 'data-highlight-links', cardHighlightLinks, false);
            applyToggleOption('lineSpacing', 'data-line-spacing', cardLineSpacing, false);
            applyToggleOption('letterSpacing', 'data-letter-spacing', cardLetterSpacing, false);
            applyToggleOption('largeCursor', 'data-large-cursor', cardLargeCursor, false);
            applyToggleOption('stopAnimations', 'data-stop-animations', cardStopAnimations, false);
            applyToggleOption('keyboardNav', 'data-keyboard-nav', cardKeyboardNav, false);

            showToast('All accessibility settings restored to default.');
        });
    }
}

