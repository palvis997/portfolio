"""
Management command to seed the portfolio database with Pavis Mugo Muruga's verified data.
Run: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from main.models import (
    SiteSettings, SocialLink, Skill, Experience, ExperienceProject,
    Education, Project, CurrentlyBuilding, Recommendation, LearningTopic,
    Goal, TimelineEvent, BlogPost, Certification, Achievement, PlaygroundExperiment
)


class Command(BaseCommand):
    help = 'Seeds database with verified portfolio data for Pavis Mugo Muruga'

    def handle(self, *args, **options):
        self.stdout.write('Seeding verified portfolio data for Pavis Mugo Muruga...')

        # 1. Site Settings
        site, created = SiteSettings.objects.get_or_create(pk=1)
        site.site_name = 'Pavis Mugo Muruga'
        site.site_title = 'Information Technology Student | Python & Django Developer | IT Support'
        site.site_description = (
            'Pavis Mugo Muruga — Information Technology student at Kirinyaga University (Year 2, Expected Graduation: 2028). '
            'Python & Django developer with hands-on industrial attachment experience at the ICT Authority of Kenya.'
        )
        site.full_name = 'Pavis Mugo Muruga'
        site.profession = 'Information Technology Student | Python & Django Developer | IT Support'
        site.location = 'Kenya'
        site.bio = (
            'I am an Information Technology student at Kirinyaga University, currently in Year 2 '
            'pursuing a Bachelor of Science in Information Technology (Expected Graduation: 2028).\n\n'
            'I have practical industry experience gained during a comprehensive 13-week industrial attachment '
            'at the ICT Authority of Kenya (4 May 2026 – 31 July 2026). During this period, I contributed to '
            'software systems using Python and Django, worked on database-related operations, and provided active '
            'ICT support and technical troubleshooting across departments.\n\n'
            'I am driven by continuous learning, disciplined problem solving, and a commitment to writing clean, '
            'maintainable code for real-world digital solutions.'
        )
        site.hero_greeting = "Hi, I'm Pavis Mugo Muruga"
        site.hero_title = "Information Technology Student | Python & Django Developer | IT Support"
        site.hero_subtitle = (
            "Aspiring technology professional with verified industrial attachment experience at the "
            "ICT Authority of Kenya. Focused on software development with Python & Django, database management, and IT infrastructure support."
        )
        site.hero_status = "Available for opportunities & collaboration"
        site.email = "palvismugo06@gmail.com"
        site.phone = "0711652479"
        site.whatsapp_number = "254711652479"
        site.github_username = "palvis997"
        site.github_url = "https://github.com/palvis997"
        site.linkedin_url = ""
        site.profile_image = "images/profile 3.jpeg"
        site.footer_tagline = "Building practical solutions. Learning continuously. Growing as a developer."
        site.whatsapp_message = "Hello Pavis, I visited your portfolio and would like to connect with you."
        site.save()
        self.stdout.write(self.style.SUCCESS('[OK] SiteSettings configured with verified info for Pavis Mugo Muruga'))

        # 2. Social / Contact Links
        socials = [
            {'platform': 'github', 'url': 'https://github.com/palvis997', 'icon': 'fab fa-github', 'order': 1},
            {'platform': 'email', 'url': 'mailto:palvismugo06@gmail.com', 'icon': 'fas fa-envelope', 'order': 2},
            {'platform': 'whatsapp', 'url': 'https://wa.me/254711652479', 'icon': 'fab fa-whatsapp', 'order': 3},
            {'platform': 'other', 'url': 'tel:0711652479', 'icon': 'fas fa-phone', 'order': 4},
        ]
        SocialLink.objects.all().delete()
        for s in socials:
            SocialLink.objects.create(**s)
        self.stdout.write(self.style.SUCCESS('[OK] Social links configured'))

        # 3. Skills (including Data & Information Management / Data Capturing)
        skills = [
            # Programming
            {'name': 'Python', 'category': 'programming', 'level': 'intermediate', 'icon': 'fab fa-python', 'order': 1},
            {'name': 'JavaScript', 'category': 'programming', 'level': 'intermediate', 'icon': 'fab fa-js-square', 'order': 2},
            {'name': 'HTML5', 'category': 'programming', 'level': 'proficient', 'icon': 'fab fa-html5', 'order': 3},
            {'name': 'CSS3', 'category': 'programming', 'level': 'proficient', 'icon': 'fab fa-css3-alt', 'order': 4},

            # Frameworks
            {'name': 'Django', 'category': 'framework', 'level': 'intermediate', 'icon': 'fas fa-server', 'order': 1},
            {'name': 'Bootstrap 5', 'category': 'framework', 'level': 'proficient', 'icon': 'fab fa-bootstrap', 'order': 2},

            # Databases
            {'name': 'SQLite', 'category': 'database', 'level': 'intermediate', 'icon': 'fas fa-database', 'order': 1},
            {'name': 'PostgreSQL', 'category': 'database', 'level': 'learning', 'icon': 'fas fa-database', 'order': 2},
            {'name': 'Database Design & Queries', 'category': 'database', 'level': 'intermediate', 'icon': 'fas fa-table', 'order': 3},

            # Data & Information Management (Data Capturing)
            {'name': 'Data Capturing', 'category': 'data', 'level': 'proficient', 'icon': 'fas fa-keyboard', 'order': 1},
            {'name': 'Data Entry', 'category': 'data', 'level': 'proficient', 'icon': 'fas fa-file-invoice', 'order': 2},
            {'name': 'Data Organization', 'category': 'data', 'level': 'proficient', 'icon': 'fas fa-folder-tree', 'order': 3},
            {'name': 'Information Management', 'category': 'data', 'level': 'intermediate', 'icon': 'fas fa-sitemap', 'order': 4},
            {'name': 'Data Accuracy & Verification', 'category': 'data', 'level': 'proficient', 'icon': 'fas fa-check-double', 'order': 5},
            {'name': 'Digital Record Management', 'category': 'data', 'level': 'intermediate', 'icon': 'fas fa-archive', 'order': 6},

            # Tools
            {'name': 'Git', 'category': 'tool', 'level': 'intermediate', 'icon': 'fab fa-git-alt', 'order': 1},
            {'name': 'GitHub', 'category': 'tool', 'level': 'intermediate', 'icon': 'fab fa-github', 'order': 2},
            {'name': 'VS Code', 'category': 'tool', 'level': 'proficient', 'icon': 'fas fa-laptop-code', 'order': 3},

            # IT & Systems
            {'name': 'ICT Support Services', 'category': 'it', 'level': 'intermediate', 'icon': 'fas fa-headset', 'order': 1},
            {'name': 'Hardware Troubleshooting', 'category': 'it', 'level': 'intermediate', 'icon': 'fas fa-microchip', 'order': 2},
            {'name': 'Software Troubleshooting', 'category': 'it', 'level': 'intermediate', 'icon': 'fas fa-wrench', 'order': 3},
            {'name': 'Computer Networking', 'category': 'it', 'level': 'intermediate', 'icon': 'fas fa-network-wired', 'order': 4},
            {'name': 'System Administration', 'category': 'it', 'level': 'learning', 'icon': 'fas fa-cogs', 'order': 5},

            # Other Skills
            {'name': 'REST APIs', 'category': 'other', 'level': 'intermediate', 'icon': 'fas fa-plug', 'order': 1},
            {'name': 'Responsive Web Design', 'category': 'other', 'level': 'proficient', 'icon': 'fas fa-mobile-alt', 'order': 2},
            {'name': 'Problem Solving', 'category': 'other', 'level': 'proficient', 'icon': 'fas fa-lightbulb', 'order': 3},
            {'name': 'Teamwork & Communication', 'category': 'other', 'level': 'proficient', 'icon': 'fas fa-users', 'order': 4},
        ]
        Skill.objects.all().delete()
        for sk in skills:
            Skill.objects.create(**sk)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(skills)} Skills created (including Data & Information Management)'))

        # 4. Experience (ICT Authority of Kenya)
        Experience.objects.all().delete()
        exp = Experience.objects.create(
            organization='ICT Authority of Kenya',
            role='Industrial Attachment Student',
            duration='13 Weeks (4 May 2026 – 31 July 2026)',
            description=(
                'Completed a verified 13-week industrial attachment at the ICT Authority of Kenya, '
                'a State Corporation established under the Kenya State Corporations Act 446. '
                'Actively engaged in software and system development with Python & Django, database-related work, '
                'and comprehensive ICT support services across departments.'
            ),
            location='Kenya',
            is_current=False,
            order=1
        )

        exp_projects = [
            {
                'experience': exp,
                'name': 'Library Management System',
                'description': 'Participated in developing features for book cataloging, member borrowing, and availability records.',
                'responsibilities': 'Assisted in building database queries for inventory tracking, borrow and return logging, and catalog search filters.',
                'technologies': 'Python, Django, SQLite, Bootstrap, HTML5, CSS3',
                'lessons': 'Strengthened understanding of relational database transactions, data normalization, and user-centric query design.',
                'order': 1
            },
            {
                'experience': exp,
                'name': 'ICT Asset Management System',
                'description': 'Contributed to the design and implementation of an organizational asset management and tracking solution.',
                'responsibilities': 'Assisted in data modeling for hardware assets, assignment workflows, maintenance scheduling, and responsive form views.',
                'technologies': 'Python, Django, PostgreSQL, SQLite, Bootstrap 5, JavaScript',
                'lessons': 'Gained practical insights into organizational IT governance, asset lifecycle tracking, and database integrity.',
                'order': 2
            },
            {
                'experience': exp,
                'name': 'GBV System',
                'description': 'Contributed to the development of a confidential gender-based violence reporting platform.',
                'responsibilities': 'Worked on form validations, secure reference tracking identifiers, and role-separated administration views.',
                'technologies': 'Python, Django, HTML5, CSS3, JavaScript, Bootstrap',
                'lessons': 'Reinforced the critical importance of user confidentiality, data security, and intuitive workflow design.',
                'order': 3
            },
            {
                'experience': exp,
                'name': 'ICT Support Services & Infrastructure',
                'description': 'Provided direct technical assistance, equipment troubleshooting, and operational system maintenance.',
                'responsibilities': 'Diagnosed workstation hardware, performed software installations and updates, resolved connectivity issues, and assisted users with technical inquiries.',
                'technologies': 'Hardware Troubleshooting, Software Diagnostics, Networking, System Maintenance',
                'lessons': 'Developed strong problem-solving capabilities, clear technical communication, and effective teamwork under operational deadlines.',
                'order': 4
            },
        ]
        for ep in exp_projects:
            ExperienceProject.objects.create(**ep)
        self.stdout.write(self.style.SUCCESS('[OK] ICT Authority Experience & Attachment projects created'))

        # 5. Recommendation (Scholastica Mutuku - Software Engineer, ICT Authority of Kenya)
        Recommendation.objects.all().delete()
        Recommendation.objects.create(
            supervisor_name='Scholastica Mutuku',
            supervisor_role='Software Engineer',
            organization='ICT Authority of Kenya',
            organization_note='State Corporation under Kenya State Corporations Act 446',
            recommendation_date='20 July 2026',
            attachment_duration='4 May 2026 – 31 July 2026 (13 Weeks)',
            quote=(
                'Pavis Mugo Muruga successfully completed his 13-week industrial attachment at the ICT Authority of Kenya '
                'from 4 May 2026 to 31 July 2026. Throughout his tenure, he exhibited remarkable enthusiasm, dedication, '
                'and a strong willingness to learn, while making meaningful contributions to our software development and ICT support tasks.'
            ),
            highlights=(
                'Enthusiasm and strong commitment\n'
                'Strong willingness to learn and adapt quickly\n'
                'Proficiency in Python and Django development\n'
                'Solid ICT support and troubleshooting capabilities\n'
                'High level of professionalism and positive attitude\n'
                'Excellent problem-solving abilities\n'
                'Ability to work independently and as part of a team\n'
                'Effective communication and collaborative skills\n'
                'Quick comprehension of new concepts and technologies\n'
                'Dedication to delivering quality and dependable work'
            ),
            order=1,
            is_active=True
        )
        self.stdout.write(self.style.SUCCESS('[OK] Professional Recommendation configured'))

        # 6. Education (Kirinyaga University)
        Education.objects.all().delete()
        Education.objects.create(
            institution='Kirinyaga University',
            course='Bachelor of Science in Information Technology',
            level='Year 2',
            description=(
                'Pursuing a comprehensive curriculum encompassing software development, database systems, '
                'computer networking, system administration, and information management.'
            ),
            start_date='Current',
            end_date='2028 (Expected)',
            relevant_areas='Web Development, Python & Django, Database Management, Computer Networks, Information Systems, System Administration, Data Structures',
            achievements='',
            is_current=True,
            order=1
        )
        self.stdout.write(self.style.SUCCESS('[OK] Education configured (Kirinyaga University, Year 2, Expected 2028)'))

        # 7. Projects (4 Core Projects with Verified Live URLs and Statuses)
        Project.objects.all().delete()
        projects = [
            {
                'title': 'GBV / Digital Safe Space System',
                'slug': 'gbv-system',
                'category': 'django',
                'status': 'live',
                'is_featured': True,
                'order': 1,
                'role': 'Django Developer (Attachment Project)',
                'short_description': 'A secure, confidential reporting platform for gender-based violence incidents with unique reference tracking and caseworker triage.',
                'overview': (
                    'A digital reporting platform engineered to provide a confidential channel for submitting incident reports, '
                    'allowing caseworkers to review cases while giving users anonymous tracking identifiers.'
                ),
                'problem': 'Victims and community members frequently lack safe, discrete channels to report sensitive incidents without fear of compromised privacy.',
                'solution': 'Developed a secure reporting workflow that generates unique reference codes for tracking status without exposing private data publicly.',
                'features': (
                    'Confidential and secure incident reporting form\n'
                    'Automatic generation of unique Incident Reference Numbers\n'
                    'Authorized caseworker dashboard for case triage\n'
                    'Incident status lookup using tracking code only\n'
                    'Support resources and helpline directory\n'
                    'Responsive layout for mobile and desktop access'
                ),
                'technologies': 'Python, Django, HTML5, CSS3, Bootstrap 5, JavaScript, SQLite',
                'development_process': 'Designed strict data validation, separated public submission views from internal caseworker views, and ensured secure session handling.',
                'challenges': 'Balancing simplicity of reporting for users under stress with capturing structured data required for caseworkers.',
                'lessons_learned': 'Gained a deep appreciation for software security principles, privacy preservation, and empathetic UX design.',
                'results': 'Produced a secure and dependable incident reporting architecture focused on user privacy and rapid case handling.',
                'github_url': '',
                'live_url': 'https://gbv-system.onrender.com/',
            },
            {
                'title': 'Library Management System',
                'slug': 'library-management-system',
                'category': 'django',
                'status': 'live',
                'is_featured': True,
                'order': 2,
                'role': 'Full-Stack Developer (Attachment Project)',
                'short_description': 'A digital library system managing catalog inventory, member borrowing privileges, return tracking, and availability.',
                'overview': (
                    'A digital management system designed for school and organizational libraries to replace manual record keeping with an '
                    'automated platform tracking book titles, copy availability, loans, and returns.'
                ),
                'problem': 'Manual book ledgers cause inaccurate availability counts, difficult catalog search, and slow check-out/check-in operations.',
                'solution': 'Built an integrated Django application with automated inventory tracking upon borrowing, due date calculation, and instant catalog search.',
                'features': (
                    'Book catalog management with ISBN, Authors, and Categories\n'
                    'Real-time book availability and copy count tracking\n'
                    'Member registration and borrowing privilege management\n'
                    'Borrow and return transaction logs with due dates\n'
                    'Instant catalog search by title, author, or category\n'
                    'Librarian overview dashboard'
                ),
                'technologies': 'Python, Django, HTML5, CSS3, JavaScript, SQLite, Bootstrap',
                'development_process': 'Constructed normalized models for Books, Members, and Loans. Implemented transactional checks to ensure copy counts adjust accurately on checkout and return.',
                'challenges': 'Ensuring atomic database operations so that book availability stays accurate during simultaneous user operations.',
                'lessons_learned': 'Mastered Django ORM transactions, date handling with timezone awareness, and responsive table design.',
                'results': 'Created a reliable, easy-to-use library management system that streamlines lending workflows.',
                'github_url': '',
                'live_url': 'https://library-system-n109.onrender.com/',
            },
            {
                'title': 'ICT Asset Management System',
                'slug': 'ict-asset-management-system',
                'category': 'django',
                'status': 'in_development',
                'is_featured': True,
                'order': 3,
                'role': 'Backend & Full-Stack Developer (Attachment Project)',
                'short_description': 'A web-based platform for registering, assigning, and maintaining ICT assets with tracking workflows and audit histories.',
                'overview': (
                    'The ICT Asset Management System was developed to address the operational challenges of managing technology hardware '
                    'and licenses across an organization. It provides organized tracking from acquisition to servicing with structured status records.'
                ),
                'problem': (
                    'Organizations often experience difficulties maintaining equipment inventories manually, leading to untracked asset locations, '
                    'overlooked maintenance schedules, and inefficient handover records.'
                ),
                'solution': (
                    'Developed a full-stack Django solution with relational models for Asset Categories, Assets, Custodians, and Maintenance Logs. '
                    'Includes searchable asset listings, status indicators, and structured data views.'
                ),
                'features': (
                    'Asset registration with serial number and category tagging\n'
                    'Custodian assignment and transfer records\n'
                    'Maintenance history tracking and servicing logs\n'
                    'Multi-parameter search and status filtering\n'
                    'Role-based access for administrators and IT staff\n'
                    'Summary overview dashboard with asset status distribution'
                ),
                'technologies': 'Python, Django, Bootstrap 5, JavaScript, SQLite, PostgreSQL',
                'development_process': (
                    '1. Analyzed organizational asset workflow requirements.\n'
                    '2. Designed normalized relational database schema with Django ORM.\n'
                    '3. Implemented secure views, model forms, and role-based permissions.\n'
                    '4. Built responsive interface with Bootstrap 5.\n'
                    '5. Tested CRUD operations, database queries, and edge cases.'
                ),
                'challenges': 'Designing flexible data models that accommodate varying hardware attributes while maintaining strict database integrity.',
                'lessons_learned': 'Deepened expertise in Django ORM relationships, query optimization using select_related, and clean form validation.',
                'results': 'Delivered an intuitive, structured system for managing and tracking organizational ICT assets effectively.',
                'github_url': '',
                'live_url': '',
            },
            {
                'title': 'Interactive Job Portal',
                'slug': 'interactive-job-portal',
                'category': 'web',
                'status': 'in_development',
                'is_featured': False,
                'order': 4,
                'role': 'Developer (Web Application Project)',
                'short_description': 'A recruitment web portal connecting job applicants with opportunities, featuring role-based dashboards and application tracking.',
                'overview': (
                    'A modern web portal facilitating employment connections. Employers can post vacancies and candidates can browse, filter, '
                    'and submit applications with resume documents.'
                ),
                'problem': 'Job seekers often face fragmented application steps, while employers struggle with unorganized candidate submissions.',
                'solution': 'Engineered a full-featured web app with user authentication, categorized job listings, resume uploads, and candidate status management.',
                'features': (
                    'Role-based access (Job Seeker / Employer)\n'
                    'Job posting creation and management\n'
                    'Multi-parameter search by keyword, category, and location\n'
                    'Resume upload and streamlined application submission\n'
                    'Application status tracking for candidates\n'
                    'Employer candidate management dashboard'
                ),
                'technologies': 'Python, Django, JavaScript, Bootstrap 5, SQLite',
                'development_process': 'Implemented user role separation with custom user models, dynamic job filtering, and secure file handling for resumes.',
                'challenges': 'Designing clean role permissions so employers only manage their own listings while job seekers only edit their own submissions.',
                'lessons_learned': 'Advanced proficiency in Django class-based views, decorators, and authentication flows.',
                'results': 'Built a functional, organized job application portal prototype.',
                'github_url': '',
                'live_url': '',
            }
        ]
        for p in projects:
            Project.objects.create(**p)
        self.stdout.write(self.style.SUCCESS('[OK] 4 Projects created with authentic roles, case studies, and live links'))

        # 7.5 Playground Experiments
        PlaygroundExperiment.objects.all().delete()
        experiments = [
            {
                'title': 'Password Strength & Entropy Analyzer',
                'slug': 'password-strength-checker',
                'description': 'Client-side password evaluation measuring length, character sets, entropy score, and common pattern detection.',
                'icon': 'fas fa-shield-alt',
                'status': 'in_development',
                'technology': 'JavaScript, Regular Expressions, CSS3',
                'order': 1
            },
            {
                'title': 'Interactive QR Code Generator',
                'slug': 'qr-code-generator',
                'description': 'Lightweight tool converting URLs and contact text into customizable, high-resolution QR codes.',
                'icon': 'fas fa-qrcode',
                'status': 'in_development',
                'technology': 'JavaScript, Canvas API, HTML5',
                'order': 2
            },
            {
                'title': 'Dynamic Data Table & Filter',
                'slug': 'data-table-filter',
                'description': 'Front-end data grid with client-side sorting, multi-column search, pagination, and CSV export capabilities.',
                'icon': 'fas fa-table',
                'status': 'experimental',
                'technology': 'JavaScript (ES6), HTML5, Bootstrap 5',
                'order': 3
            },
            {
                'title': 'IP & Subnet Network Calculator',
                'slug': 'ip-subnet-calculator',
                'description': 'Network engineering utility computing network address, broadcast address, CIDR masks, and usable host ranges.',
                'icon': 'fas fa-network-wired',
                'status': 'experimental',
                'technology': 'Python / JavaScript, Networking Math',
                'order': 4
            }
        ]
        for exp_item in experiments:
            PlaygroundExperiment.objects.create(**exp_item)
        self.stdout.write(self.style.SUCCESS('[OK] Playground Experiments seeded'))

        # 8. Currently Building Projects
        CurrentlyBuilding.objects.all().delete()
        building_items = [
            {
                'name': 'Student Academic & Resource Hub',
                'description': 'A collaborative web platform for Information Technology students to share verified revision materials, lecture notes, and code repositories.',
                'technologies': 'Python, Django, PostgreSQL, Bootstrap 5, JavaScript',
                'status': 'In Development',
                'progress_percent': 65,
                'github_url': '',
                'live_url': '',
                'order': 1,
            },
            {
                'name': 'Smart IT Support Helpdesk Portal',
                'description': 'A ticket-based IT service desk system for tracking hardware/software issue requests, SLA escalation, and technical knowledge base articles.',
                'technologies': 'Python, Django, SQLite, Bootstrap 5',
                'status': 'Testing',
                'progress_percent': 80,
                'github_url': '',
                'live_url': '',
                'order': 2,
            },
            {
                'name': 'Campus Event & Notice Dispatcher',
                'description': 'A real-time notification and departmental notice bulletin web app with categorized announcements and email alerts.',
                'technologies': 'Python, Django, REST APIs, JavaScript',
                'status': 'Planning',
                'progress_percent': 35,
                'github_url': '',
                'live_url': '',
                'order': 3,
            },
        ]
        for b in building_items:
            CurrentlyBuilding.objects.create(**b)
        self.stdout.write(self.style.SUCCESS('[OK] Currently Building items seeded'))

        # 9. Currently Learning Topics
        topics = [
            {'name': 'Advanced Python', 'description': 'Deepening knowledge of asynchronous programming, design patterns, and performance optimization.', 'icon': 'fab fa-python', 'order': 1},
            {'name': 'Django', 'description': 'Mastering advanced ORM queries, custom middleware, signals, and scalable architecture.', 'icon': 'fas fa-server', 'order': 2},
            {'name': 'REST APIs', 'description': 'Designing and consuming robust RESTful APIs using Django REST Framework.', 'icon': 'fas fa-plug', 'order': 3},
            {'name': 'PostgreSQL', 'description': 'Relational schema design, advanced indexing, and query performance tuning.', 'icon': 'fas fa-database', 'order': 4},
            {'name': 'JavaScript', 'description': 'Modern ES6+ features, asynchronous fetch APIs, and dynamic DOM manipulation.', 'icon': 'fab fa-js-square', 'order': 5},
            {'name': 'Cloud Deployment', 'description': 'Containerization basics, production server configuration with Gunicorn and WhiteNoise.', 'icon': 'fas fa-cloud', 'order': 6},
            {'name': 'Cybersecurity', 'description': 'Web application security best practices, input sanitization, and defensive coding.', 'icon': 'fas fa-shield-alt', 'order': 7},
            {'name': 'Software Architecture', 'description': 'Clean code principles, modular system design, and maintainable software patterns.', 'icon': 'fas fa-drafting-compass', 'order': 8},
        ]
        LearningTopic.objects.all().delete()
        for t in topics:
            LearningTopic.objects.create(**t)
        self.stdout.write(self.style.SUCCESS('[OK] Currently Learning topics seeded'))

        # 10. Goals
        goals = [
            {'title': 'Future Software Developer', 'description': 'Build a strong foundation in software engineering and grow into a versatile, professional developer.', 'icon': 'fas fa-laptop-code', 'order': 1},
            {'title': 'Build Scalable Digital Solutions', 'description': 'Design and engineer reliable, maintainable systems that solve practical organizational challenges.', 'icon': 'fas fa-project-diagram', 'order': 2},
            {'title': 'Deepen Backend Mastery', 'description': 'Excel in Python, Django, REST APIs, database architecture, and backend systems.', 'icon': 'fas fa-server', 'order': 3},
            {'title': 'Cloud & Infrastructure Skills', 'description': 'Gain proficiency in modern deployment workflows, Linux server management, and cloud hosting.', 'icon': 'fas fa-cloud', 'order': 4},
            {'title': 'Security-Minded Engineering', 'description': 'Integrate cybersecurity best practices and data privacy principles into every software project.', 'icon': 'fas fa-shield-alt', 'order': 5},
            {'title': 'Meaningful Tech Contributions', 'description': 'Participate in technology initiatives that positively impact communities and improve public services.', 'icon': 'fas fa-hands-helping', 'order': 6},
        ]
        Goal.objects.all().delete()
        for g in goals:
            Goal.objects.create(**g)
        self.stdout.write(self.style.SUCCESS('[OK] Goals seeded'))

        # 11. Timeline Events (My Journey)
        timeline = [
            {
                'title': 'BSc. in Information Technology — Kirinyaga University',
                'description': 'Commenced Bachelor of Science in Information Technology, building core competencies in programming, networks, and databases (Year 2, Expected Graduation: 2028).',
                'date': '2026',
                'icon': 'fas fa-graduation-cap',
                'category': 'education',
                'order': 1
            },
            {
                'title': 'Industrial Attachment — ICT Authority of Kenya',
                'description': '13-week industrial attachment (4 May 2026 – 31 July 2026) gaining practical experience in software development, Python, Django, databases, and ICT support.',
                'date': 'May – Jul 2026',
                'icon': 'fas fa-briefcase',
                'category': 'experience',
                'order': 2
            },
            {
                'title': 'Python & Django Practical Development',
                'description': 'Deepened hands-on full-stack development skills with Python, Django ORM, template views, and database integrations.',
                'date': '2026',
                'icon': 'fab fa-python',
                'category': 'project',
                'order': 3
            },
            {
                'title': 'Library Management System & ICT Asset Management System',
                'description': 'Built practical systems for catalog management, lending workflows, asset tracking, and maintenance operations.',
                'date': '2026',
                'icon': 'fas fa-code',
                'category': 'project',
                'order': 4
            },
            {
                'title': 'GBV System Development & ICT Support',
                'description': 'Contributed to secure incident reporting workflows and provided active technical hardware/network support.',
                'date': '2026',
                'icon': 'fas fa-shield-alt',
                'category': 'project',
                'order': 5
            },
            {
                'title': 'Expected University Graduation',
                'description': 'Complete Bachelor of Science in Information Technology at Kirinyaga University and transition into professional software development.',
                'date': '2028',
                'icon': 'fas fa-award',
                'category': 'goal',
                'order': 6
            },
        ]
        TimelineEvent.objects.all().delete()
        for ev in timeline:
            TimelineEvent.objects.create(**ev)
        self.stdout.write(self.style.SUCCESS('[OK] Timeline events seeded'))

        # 12. Clear Certifications (Do NOT list unverified TVET CDACC)
        Certification.objects.all().delete()
        Achievement.objects.all().delete()

        # 13. Sample Blog Posts
        blog_posts = [
            {
                'title': 'Building Scalable Web Applications with Django & Python',
                'slug': 'building-scalable-web-applications-django-python',
                'excerpt': 'Key principles of relational data modeling, query optimization, and clean architecture when building full-stack applications with Django.',
                'content': (
                    'Django offers an exceptional developer experience for building structured, secure web applications. '
                    'Having built systems ranging from Asset Management to Incident Reporting, here are key architectural insights I have learned:\n\n'
                    '### 1. The Importance of Clean Model Design\n\n'
                    'Your database models form the backbone of your application. When architecting models in Django, always prioritize:\n'
                    '- Explicit null and blank constraints to prevent unexpected data states.\n'
                    '- Clear indexing on frequently filtered fields like slugs, status flags, and timestamps.\n'
                    '- Utilizing helper methods on models rather than cluttering views with business logic.\n\n'
                    '### 2. Optimizing Query Performance\n\n'
                    'The N+1 query problem can quietly degrade performance as your database grows. By utilizing select_related for foreign keys '
                    'and prefetch_related for reverse relationships, you reduce hundreds of database trips down to single optimized queries.\n\n'
                    '### 3. Modular Architecture\n\n'
                    'Splitting functionality into cohesive Django apps keeps your codebase maintainable and testable.'
                ),
                'category': 'Django Development',
                'tags': 'Python, Django, Backend, Web Development, Database',
                'author': 'Pavis Mugo Muruga',
                'reading_time': 4,
                'published': True,
                'featured': True,
            },
            {
                'title': 'Key Lessons from My Industrial Attachment at the ICT Authority of Kenya',
                'slug': 'lessons-from-industrial-attachment-ict-authority',
                'excerpt': 'Reflections and insights gained during 13 weeks of hands-on experience in public sector ICT support, system development, and teamwork.',
                'content': (
                    'My 13-week industrial attachment at the ICT Authority of Kenya (4 May 2026 – 31 July 2026) was a transformative milestone '
                    'that bridged classroom theory with real-world engineering and support operations.\n\n'
                    '### 1. Real-World Troubleshooting Requires Methodical Thinking\n\n'
                    'Whether diagnosing network connectivity issues or troubleshooting workstation hardware, isolating variables step by step '
                    'is far more effective than guessing. Documenting recurring issues and creating repeatable checklists saves valuable hours.\n\n'
                    '### 2. Security and Privacy Are Non-Negotiable\n\n'
                    'Working on systems like Gender-Based Violence (GBV) Reporting reinforced how critical data protection, anonymous identifiers, '
                    'and strict authorization policies are in software that impacts people directly.\n\n'
                    '### 3. Continuous Learning is the Core Skill\n\n'
                    'Technology is constantly evolving. The most valuable skill in IT is not knowing every answer upfront, but possessing the curiosity '
                    'and discipline to research, understand, and solve complex problems quickly.'
                ),
                'category': 'IT & Career Journey',
                'tags': 'IT Support, Career, Industrial Attachment, Networking, Python, Experience',
                'author': 'Pavis Mugo Muruga',
                'reading_time': 5,
                'published': True,
                'featured': True,
            },
        ]
        BlogPost.objects.all().delete()
        for bp in blog_posts:
            BlogPost.objects.create(**bp)
        self.stdout.write(self.style.SUCCESS('[OK] Blog Posts seeded with author Pavis Mugo Muruga'))

        self.stdout.write(self.style.SUCCESS('\n>>> Verified database seeding for Pavis Mugo Muruga complete!'))
