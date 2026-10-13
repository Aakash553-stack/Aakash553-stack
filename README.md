<!--
  AAKASH.EXE // profile README
  You're reading the source, so here's the tour: every graphic on this page is a hand-written
  SVG animated with plain CSS. No JavaScript, no third-party widgets. The activity card and the
  snake are rebuilt daily by .github/workflows/profile-assets.yml.
  The robot in the footer is unit-553. It blinks. That's its whole job.
-->

<a href="https://aakashmunawar.com"><img src="assets/hero.svg" width="100%" alt="AAKASH.EXE — Aakash Munawar. Computer Science Student @ Rutgers University. Full-Stack Development • AI • Data Science. Building practical software. Exploring intelligent systems. Always learning. HackRU 2026 — Best Regeneron Entry Winner."></a>

<p align="center">
  <a href="https://aakashmunawar.com"><b>aakashmunawar.com</b></a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/aakash-munawar-760019268">LinkedIn</a> &nbsp;·&nbsp;
  <a href="mailto:aakashmunawar.dev@gmail.com">Email</a> &nbsp;·&nbsp;
  <a href="#projects">Projects</a> &nbsp;·&nbsp;
  <a href="https://trialwright.tech">Pre-Flight live demo</a>
</p>

## 🏆 HackRU 2026 — Best Regeneron Entry Winner

<a href="https://trialwright.tech"><img src="assets/award.svg" width="100%" alt="Award card: HackRU 2026 — Best Regeneron Entry Winner. Protocol Pre-Flight, AI-powered clinical trial protocol analysis. Flags missing sections, contradictions and patient burden. Team: Yash Lalwani, Hanumath Mandadi, Aakash Munawar."></a>

At HackRU 2026, my team built **Protocol Pre-Flight**, an AI-powered tool that reviews clinical trial protocols before a trial starts. It won the **Best Regeneron Entry** award.

Changing a protocol after a trial starts is expensive, and [many of those amendments are avoidable](https://pubmed.ncbi.nlm.nih.gov/30227022/). Pre-Flight looks for the problems early: missing required sections, numbers or rules that contradict each other across sections, heavy patient burden, and anything else a person should check. Every finding points to the page that supports it, and an AI finding is dropped unless the text it quotes is actually on the page it cites. A person accepts or rejects each finding.

- **My part:** I built the Next.js and TypeScript frontend, which is the upload page and the PDF review workspace where each finding is highlighted on the page it cites. I also built the typed API layer that connects the frontend to the team's FastAPI backend.
- **Team:** [Yash Lalwani](https://github.com/Yash-Lalwani), [Hanumath Mandadi](https://github.com/Hanumath1506) and me.
- **Stack:** `Next.js` `React` `TypeScript` `Tailwind CSS` `Python` `FastAPI` `PyMuPDF`

**[Live demo → trialwright.tech](https://trialwright.tech)** &nbsp;·&nbsp; **[Source code (TrialWright repo)](https://github.com/Yash-Lalwani/TrialWright)**

<img src="assets/projects/protocol-pre-flight.svg" width="100%" alt="How Protocol Pre-Flight works: 1 parse the protocol PDF into a structured Protocol Graph, 2 rule checks against ICH M11 and SPIRIT 2025, 3 AI review by four reviewer roles with quotes verified on the cited page, 4 human review of each finding, 5 report with score and PDF, DOCX and USDM JSON exports.">

<img src="assets/divider.svg" width="100%" alt="">

## About

<img src="assets/terminal.svg" width="100%" alt="Terminal: ./aakash.exe --init. Identity: Aakash Munawar. Education: Computer Science @ Rutgers University–New Brunswick. Previously: Raritan Valley Community College, Computer Science. Focus: Full-Stack Development, AI, Data Science. Award: HackRU 2026 — Best Regeneron Entry Winner. whoami: a CS student who likes building complete applications. Open to software engineering, full-stack, AI/ML and data internships.">

I'm a Computer Science student at **Rutgers University–New Brunswick**. I started my CS coursework at Raritan Valley Community College before transferring. I'm most interested in full-stack development, artificial intelligence and data science.

I like building complete applications: designing the database, writing the backend API, building the interface, and working out the algorithm in between. So far that has meant a Spring Boot app with JWT authentication, a SQL dashboard over nearly 480,000 public records, and graph and backtracking algorithms written from scratch. At HackRU 2026, my team won Best Regeneron Entry for Protocol Pre-Flight.

I'm still early in AI and machine learning, and I learn something new with every project. I'm looking for internships, research and collaborative projects where I can keep building.

<img src="assets/divider.svg" width="100%" alt="">

## Projects

<a href="https://github.com/Aakash553-stack/aakashmunawar-site/tree/master/projects/study-group-matcher"><img src="assets/projects/study-group-matcher.svg" width="100%" alt="Study Group Matcher project card: matches Rutgers students into study groups by shared courses and overlapping weekly free time. 41 JUnit tests passing; matcher checked against brute force."></a>

**Study Group Matcher** &nbsp;·&nbsp; [Live demo](https://study.aakashmunawar.com) (one-click "Try the demo") &nbsp;·&nbsp; [Source](https://github.com/Aakash553-stack/aakashmunawar-site/tree/master/projects/study-group-matcher)<br>
**Problem:** finding classmates who take the same courses and are free at the same times.<br>
**How it works:** a Spring Boot REST API with Spring Security and JWT authentication, PostgreSQL through JPA with Flyway migrations, and a plain HTML, CSS and JavaScript frontend where students paint their free time on a weekly grid.<br>
**Highlight:** the matching algorithm is written from scratch and checked against a brute-force model, with 41 passing JUnit tests. The public demo account runs in a separate sandbox, so a demo login never shows real students' names or schedules.

`Java` `Spring Boot` `Spring Security` `JWT` `PostgreSQL` `JPA` `Flyway` `JUnit`

<a href="https://github.com/Aakash553-stack/aakashmunawar-site/tree/master/projects/crime-data-explorer"><img src="assets/projects/chicago-crime-explorer.svg" width="100%" alt="Chicago Crime Explorer project card: interactive dashboard over 478,089 Chicago Police Department incidents in a normalized SQL schema with six analyses."></a>

**Chicago Crime Explorer** &nbsp;·&nbsp; [Live dashboard](https://crime.aakashmunawar.com) &nbsp;·&nbsp; [Source](https://github.com/Aakash553-stack/aakashmunawar-site/tree/master/projects/crime-data-explorer)<br>
**Problem:** making two years of public crime data explorable without writing SQL.<br>
**How it works:** 478,089 Chicago Police Department incident reports from the City of Chicago Data Portal, loaded into a normalized SQLite schema. A FastAPI backend serves six analyses to a Chart.js dashboard with filters for date, category, district, community area, arrests and domestic incidents.<br>
**Highlight:** the backend doesn't duplicate the analysis. It runs the same `queries.sql` file as the Jupyter notebook and adds filters to each query.

`Python` `SQL` `SQLite` `FastAPI` `pandas` `Jupyter` `matplotlib` `Chart.js`

<a href="https://github.com/Aakash553-stack/aakashmunawar-site/tree/master/projects/schedule-builder"><img src="assets/projects/schedule-builder.svg" width="100%" alt="Schedule Builder project card: finds every conflict-free Rutgers class schedule with backtracking and ranks them by preference; 5.9 times faster than brute force on a 5-course search."></a>

**Schedule Builder** &nbsp;·&nbsp; [Source](https://github.com/Aakash553-stack/aakashmunawar-site/tree/master/projects/schedule-builder)<br>
**Problem:** five courses with several sections each can add up to over two million possible schedules, far too many to check by hand.<br>
**How it works:** a command-line tool over real Rutgers Fall 2026 section data (1,110 sections across 148 CS and Math courses). A backtracking search drops a partial schedule as soon as it has a time conflict, then ranks the results by days on campus, gaps between classes, later mornings or campus switches.<br>
**Highlight:** on a 5-course search, backtracking skips 87% of the 2.26 million combinations and runs 5.9× faster than brute force (2.0 s vs. 11.5 s).

`Python` `Backtracking` `Standard library only`

<a href="https://github.com/Aakash553-stack/aakashmunawar-site/tree/master/projects/campus-route-finder"><img src="assets/projects/campus-route-finder.svg" width="100%" alt="Campus Route Finder project card: shortest walking routes across Rutgers–New Brunswick with Dijkstra's algorithm and a hand-built binary-heap queue over 24 real OpenStreetMap locations."></a>

**Campus Route Finder** &nbsp;·&nbsp; [Source](https://github.com/Aakash553-stack/aakashmunawar-site/tree/master/projects/campus-route-finder)<br>
**Problem:** finding the shortest walk between buildings on a campus split by the Raritan River.<br>
**How it works:** a graph of 24 real campus locations plus a bridge waypoint, with Dijkstra's algorithm and a binary-heap priority queue both written from scratch. It can also find the nearest locations of a type, such as the three closest dining halls, and draw the route on a map.<br>
**Highlight:** every coordinate comes from OpenStreetMap and keeps its OSM ID, so any location can be checked on the map.

`Python` `Graph algorithms` `Dijkstra` `unittest` `matplotlib`

<a href="https://github.com/Aakash553-stack/opstrack-police-operations-platform"><img src="assets/projects/opstrack.svg" width="100%" alt="OpsTrack project card, in progress: a 13-table PostgreSQL schema, Alembic migrations and a FastAPI REST layer are done; authentication is next."></a>

**OpsTrack** *(in progress)* &nbsp;·&nbsp; [Source](https://github.com/Aakash553-stack/opstrack-police-operations-platform)<br>
**Problem:** an internal operations system with complex relationships and rules: officers, units, assignments, patrols and incidents. All data is fictional.<br>
**Done so far:** a hand-written 3NF PostgreSQL schema with 13 tables, Alembic migrations, and a FastAPI REST API for all 13 resources. Authentication, a full test suite and the React frontend are next.<br>
**Highlight:** the Alembic migration reproduces the hand-written schema exactly (verified with a `pg_dump` diff), and database rule violations come back from the API as clear `409 Conflict` errors.

`Python` `FastAPI` `PostgreSQL` `SQLAlchemy` `Alembic` `Docker`

<details>
<summary><b>Earlier projects</b></summary>
<br>

- [Task Manager REST API](https://github.com/Aakash553-stack/taskmanager): a task management REST API with Spring Boot and an in-memory H2 database.
- [Student Grade Tracker](https://github.com/Aakash553-stack/StudentGradeTracker): a Java Swing desktop app for grades, class averages and letter grades.
- [Bank Account Simulator](https://github.com/Aakash553-stack/BankAccountSimulator): a command-line Java banking simulator with overdraft protection.

</details>

<img src="assets/divider.svg" width="100%" alt="">

## Tech I've Built With

<img src="assets/tech.svg" width="100%" alt="Tech stack. Languages: Java, Python, SQL, TypeScript, JavaScript. Backend: Spring Boot, Spring Security, JWT, JPA, FastAPI, SQLAlchemy. Data: PostgreSQL, SQLite, Alembic, pandas, Jupyter, matplotlib. Frontend: React, Next.js, Tailwind CSS, Chart.js, HTML and CSS. Tooling: Git and GitHub, Docker, Maven, JUnit and pytest, Vercel and Render.">

<details>
<summary><b>Where each one shows up</b></summary>
<br>

| Area | Tools | Used in |
|---|---|---|
| Java backend | Java, Spring Boot, Spring Security, JWT, JPA, Flyway, Maven, JUnit | Study Group Matcher, Task Manager API |
| Python backend | Python, FastAPI, SQLAlchemy, Alembic, pytest | OpsTrack, Chicago Crime Explorer |
| Databases | PostgreSQL, SQLite, SQL | Study Group Matcher, OpsTrack, Chicago Crime Explorer |
| Data analysis | pandas, Jupyter, matplotlib | Chicago Crime Explorer, Campus Route Finder |
| Frontend | TypeScript, React, Next.js, Tailwind CSS | Protocol Pre-Flight |
| Frontend | JavaScript, HTML, CSS, Chart.js | Study Group Matcher, Chicago Crime Explorer |
| Algorithms | Backtracking, Dijkstra, binary heaps | Schedule Builder, Campus Route Finder |
| Shipping | Git, GitHub, Docker, Vercel, Render | Version control everywhere; Docker for OpsTrack and Study Group Matcher; live demos on Vercel and Render |

</details>

## Currently Exploring

<img src="assets/exploring.svg" width="100%" alt="Currently exploring: Applied AI, Machine Learning, Data Science, Backend Architecture, Full-Stack Development, Database Systems, Algorithms, Intelligent Software.">

I'm learning these areas through coursework and projects. I'm not claiming expertise in them yet, but each new project usually goes a bit further into one of them.

<img src="assets/divider.svg" width="100%" alt="">

## GitHub Activity

<a href="https://github.com/Aakash553-stack"><img src="https://raw.githubusercontent.com/Aakash553-stack/Aakash553-stack/output/activity.svg" width="100%" alt="GitHub activity card, regenerated daily: contributions and active days over the past year, longest streak, public repositories, weekly contributions and languages in featured repos."></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Aakash553-stack/Aakash553-stack/output/snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Aakash553-stack/Aakash553-stack/output/snake-light.svg">
  <img src="https://raw.githubusercontent.com/Aakash553-stack/Aakash553-stack/output/snake-dark.svg" width="100%" alt="A snake moving across my GitHub contribution graph, eating each day that had contributions.">
</picture>

## Let's Connect & Build Something

I'm always glad to meet other developers, learn from people further along, and work on interesting projects together. Whether you're a student, engineer, researcher or recruiter, feel free to reach out.

**Open to:** internships · collaboration · research opportunities · learning opportunities · connecting with other developers

<p align="center">
  <a href="https://aakashmunawar.com"><img src="assets/connect/website.svg" width="196" alt="Website: aakashmunawar.com"></a>
  <a href="https://www.linkedin.com/in/aakash-munawar-760019268"><img src="assets/connect/linkedin.svg" width="196" alt="LinkedIn: aakash-munawar"></a>
  <a href="mailto:aakashmunawar.dev@gmail.com"><img src="assets/connect/email.svg" width="196" alt="Email: aakashmunawar.dev@gmail.com"></a>
  <a href="https://github.com/Aakash553-stack"><img src="assets/connect/github.svg" width="196" alt="GitHub: Aakash553-stack"></a>
</p>

<p align="center"><code>aakashmunawar.dev@gmail.com</code></p>

<img src="assets/footer.svg" width="100%" alt="Footer: a small pixel robot, unit-553, hovers next to a speech bubble reading 'Currently compiling ideas'. exit 0, thanks for stopping by.">
