# Pavis Mugo Muruga — Professional Personal Portfolio & CMS

[![Django](https://img.shields.io/badge/Django-5.0+-092e20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952b3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A modern, high-performance, responsive personal portfolio website and full Content Management System (CMS) designed for **Pavis Mugo Muruga** — Information Technology Student at Kirinyaga University, Python & Django Developer, and IT Support Specialist.

Built with **Django**, **Bootstrap 5**, **Vanilla CSS3 Design System**, and **SQLite/PostgreSQL**.

---

## 🌟 Key Highlights & Features

- 🌓 **Seamless Dark & Light Themes**: Persistent theme switcher with custom CSS variable architecture.
- 📱 **100% Mobile Responsive**: Tested from 320px ultra-compact viewports up to 4K ultra-wide monitors.
- ⚡ **Full Django Admin CMS**: Manage every project, skill, work experience, supervisor recommendation, currently building item, certification, blog post, and site setting without touching code.
- 📜 **Official Recommendation Support**: Dedicated section and modal for supervisor Scholastica Mutuku (Software Engineer, ICT Authority of Kenya) with PDF upload support.
- 📄 **Dedicated Printable CV Page (`/cv/`)**: Structured, verified Curriculum Vitae ready for browser printing or PDF saving with no-print utility controls.
- 💼 **Comprehensive Case Studies**: Dedicated case study detail pages with problem breakdowns, solutions, roles, features, architectures, challenges, and lessons learned.
- 🔨 **Currently Building Showcase**: Live development progress bars and status indicators (`Planning`, `In Development`, `Testing`, `Completed`).
- 📰 **Integrated Tech Blog Engine**: Markdown-friendly content, categorization, tag filtering, real-time search, and reading-time calculations.
- 🛡️ **Defensive Security & Performance**: CSRF protection, SQL injection prevention, XSS mitigation, secure cookies, WhiteNoise static compression, and environment-based secret isolation.
- 🚀 **One-Click Render Deployment**: Includes `render.yaml` blueprint, `build.sh`, and production WSGI configuration.
- 💬 **Interactive Contact & WhatsApp**: Contact messages logged directly into the database with Django Admin triage + configurable direct contact details.
- 🔍 **SEO & Social Graph Ready**: Automated XML Sitemap generation (`/sitemap.xml`), `robots.txt`, dynamic Open Graph & Twitter card metadata.

---

## 📁 Project File Architecture

```text
portfolio/
│
├── manage.py                   # Django management utility
├── requirements.txt            # Python package dependencies
├── render.yaml                 # Render cloud blueprint
├── build.sh                    # Automated build script for deployment
├── Procfile                    # Web process configuration for Gunicorn
├── .env.example                # Template for environment variables
├── .env                        # Local development variables (git ignored)
├── .gitignore                  # Git ignore rules
├── README.md                   # Complete documentation
│
├── portfolio/                  # Django project configuration
│   ├── __init__.py
│   ├── settings.py             # Split development/production settings
│   ├── urls.py                 # Master URL routing & sitemaps
│   ├── wsgi.py                 # Production WSGI entry point
│   └── asgi.py                 # ASGI entry point
│
├── main/                       # Core portfolio application
│   ├── models.py               # Database models (Projects, Recommendation, CurrentlyBuilding, Skills, etc.)
│   ├── admin.py                # Customized Django Admin with previews & filters
│   ├── views.py                # Views for Home, CV, Case Studies, Blog, Contact, Error Handlers
│   ├── forms.py                # Contact form with server-side validation
│   ├── urls.py                 # App-level routing
│   ├── context_processors.py   # Global SiteSettings injector
│   ├── sitemaps.py             # Dynamic XML sitemaps
│   │
│   ├── management/
│   │   └── commands/
│   │       └── seed_data.py    # Database seeder with Pavis Mugo Muruga's profile
│   │
│   ├── templates/
│   │   └── main/
│   │       ├── base.html           # Master layout (Nav, Footer, Theme toggle, WhatsApp)
│   │       ├── home.html           # Main portfolio single-page application
│   │       ├── cv.html             # Dedicated printable Curriculum Vitae
│   │       ├── project_detail.html # Comprehensive project case study page
│   │       ├── blog_list.html      # Blog listing with search & filters
│   │       ├── blog_detail.html    # Single article detail page
│   │       ├── contact_success.html# Submission confirmation
│   │       ├── 404.html            # Custom 404 error page
│   │       ├── 403.html            # Custom 403 error page
│   │       ├── 500.html            # Custom 500 error page
│   │       └── includes/           # Modular section components
│   │           ├── hero.html
│   │           ├── about.html
│   │           ├── services.html
│   │           ├── skills.html
│   │           ├── projects.html
│   │           ├── experience.html
│   │           ├── education.html
│   │           ├── learning.html
│   │           ├── recommendation.html
│   │           ├── goals.html
│   │           ├── timeline.html
│   │           ├── cta.html
│   │           ├── blog_preview.html
│   │           └── contact.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css       # Complete CSS design system & custom properties
│       ├── js/
│       │   └── main.js         # Interactive features (Theme, typing effect, filters)
│       └── images/             # Static image assets
│
└── media/                      # Uploaded files (profile photo, CV, recommendation letters, screenshots)
```

---

## 🛠️ Tech Stack

| Domain | Technology |
|---|---|
| **Backend Framework** | Django 5.x, Python 3.10+ |
| **Web Server / WSGI** | Gunicorn |
| **Database** | SQLite (Dev) / PostgreSQL (Production via `dj-database-url`) |
| **Static File Compression** | WhiteNoise |
| **Frontend Framework** | Bootstrap 5.3 (Grid & Utilities) |
| **Styling & Layout** | Custom Vanilla CSS3 Design System with Glassmorphism |
| **Typography** | Google Fonts (*Inter* & *JetBrains Mono*) |
| **Icons** | Font Awesome 6.5 |
| **Deployment Target** | Render (PaaS) |

---

## 🚀 Getting Started (Local Development)

### 1. Prerequisites
- **Python 3.10+** installed on your system.
- **Git** installed.

### 2. Clone or Navigate to the Project
```bash
cd C:\Users\USER\.gemini\antigravity-ide\scratch\portfolio
```

### 3. Create and Activate a Virtual Environment
**On Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Copy `.env.example` to `.env` (already pre-configured for local dev):
```bash
# On Windows
copy .env.example .env

# On Linux/macOS
cp .env.example .env
```

### 6. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Seed Initial Portfolio Data
Populate the database with Pavis Mugo Muruga's profile, skills, industrial attachment, 4 core projects, goals, and articles:
```bash
python manage.py seed_data
```

### 8. Create a Superuser for Django Admin
```bash
python manage.py createsuperuser
```
*(Enter your desired username, email, and password)*

### 9. Start the Development Server
```bash
python manage.py runserver
```

Open your browser and visit:
- **Portfolio Website**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Django Admin CMS**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## ⚙️ Content Management (Django Admin)

You can manage all aspects of your portfolio via the Django Admin panel without writing HTML or CSS:

1. **Site Settings (Singleton)**:
   - Edit your Name, Bio, Location, Email, Phone, WhatsApp Number, GitHub & LinkedIn links.
   - Upload your Profile Picture, Resume/CV (PDF), and Open Graph Social Banner.
2. **Projects**:
   - Add/Edit projects, upload cover images, add screenshots, write case studies, categorize by technology, and link Live Demos/GitHub repositories.
3. **Skills**:
   - Add programming languages, frameworks, tools, databases, and IT skills. Set levels (*Learning*, *Intermediate*, *Proficient*).
4. **Experience & Projects**:
   - Manage your Industrial Attachment at ICT Authority of Kenya or future jobs, with nested project contributions.
5. **Education**:
   - Update Kirinyaga University details, graduation dates, and relevant coursework.
6. **Blog Engine**:
   - Draft and publish tech articles with tags, categories, and cover images.
7. **Contact Messages**:
   - Review incoming messages sent through the website contact form, with search and read/unread status.

---

## 🌐 Deploying to Render

This project is pre-configured with `render.yaml` for zero-friction cloud deployment.

### Step-by-Step Deployment:
1. **Push your repository to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial portfolio commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/portfolio.git
   git push -u origin main
   ```
2. **Sign up / Log in to [Render](https://render.com/)**.
3. Click **New +** → **Blueprint**.
4. Connect your GitHub repository. Render will automatically detect `render.yaml` and configure:
   - Python Web Service (Gunicorn)
   - Managed PostgreSQL Database
   - Environment variables
   - Automated build & migration script (`build.sh`)
5. Click **Apply**. Render will build and deploy your live portfolio in ~2 minutes!

---

## 🔒 Security Best Practices Implemented

- **No Hardcoded Secrets**: All sensitive values (`SECRET_KEY`, `DATABASE_URL`, `DEBUG`) are loaded via environment variables using `python-decouple`.
- **CSRF & XSS Protection**: All forms utilize Django CSRF tokens and sanitized widget rendering.
- **Production Headers**: Auto-configured HSTS, SSL redirect, content-type nosniff, and clickjacking protection when `DEBUG=False`.
- **Database Safety**: Parameterized queries via Django ORM to prevent SQL injection.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
