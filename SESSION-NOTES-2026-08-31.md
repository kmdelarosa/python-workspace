# Session Notes — Portfolio Planning & Setup

**Date:** August 31, 2026

---

## What We Did

### 1. Python Project Recommendations

Discussed building Python projects alongside the Udemy Complete Python Bootcamp (Jose Portilla). Recommended 8 projects ordered by complexity, mapped to bootcamp progression:

| # | Project | Bootcamp Stage |
|---|---------|---------------|
| 01 | CLI Expense Tracker | Basics, data structures, file I/O |
| 02 | Password Generator | String manipulation, modules |
| 03 | Personal Finance Dashboard | OOP, JSON, classes |
| 04 | Web Scraper — Job Listings | Web scraping section |
| 05 | Automated File Organizer | Advanced modules, pathlib |
| 06 | PDF Report Generator | File handling, data processing |
| 07 | Email Automation Tool | Advanced modules, SMTP |
| 08 | Flask REST API — Notes App | Capstone — full stack Python |

---

### 2. Project Outlines & Portfolio Descriptions

For each project, produced:
- Feature list and scope of work
- Tech stack
- Portfolio-ready description (ready to paste into the website)

---

### 3. Project Folders Created

All 8 projects scaffolded under `python-workspace/portfolio-projects/`:

```
portfolio-projects/
├── 00-portfolio-website/
├── 01-cli-expense-tracker/
├── 02-password-generator/
├── 03-personal-finance-dashboard/
├── 04-web-scraper-jobs/
├── 05-file-organizer/
├── 06-pdf-report-generator/
├── 07-email-automation/
└── 08-flask-notes-api/
```

Each folder contains:
- `README.md` — description, features, tech stack, structure, usage
- `requirements.txt` — pinned dependencies
- `src/` — skeleton Python source files with working structure
- Supporting files (`.env.example`, `config.json`, sample data, templates)

---

### 4. Portfolio Website Mockup

Created `00-portfolio-website/` with a full interactive HTML mockup.

**File:** `mockup/mockup.html` — open in any browser, no server needed.

**Pages:**
- **Home/Hero** — intro, tagline, CTA buttons, featured project strip
- **About** — bio, skills grid, stats cards, learning journey timeline
- **Projects** — all 8 project cards with descriptions, tags, GitHub links, demo modals
- **Contact** — social/GitHub/email links + contact form with success state

**Design:**
- Dark navy (`#0f172a`) + electric blue (`#3b82f6`) accent
- Inter font (Google Fonts)
- Fixed nav, smooth page transitions (no reload)
- Project cards open modals with terminal/API demo previews
- Modals close on backdrop click or Escape key

---

## Next Steps

- [ ] Work through bootcamp sections and implement each project
- [ ] Push each project to its own GitHub repo
- [ ] Replace placeholder GitHub/LinkedIn/email links in the portfolio mockup
- [ ] Build out the actual portfolio site HTML/CSS once design is approved
- [ ] Deploy portfolio to GitHub Pages
