# Add template files and README, requirements, workflow
import os, textwrap, json
root = 'european-mobility-site'

# Basic layout template using Bootstrap CDN
base_html = textwrap.dedent('''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{{ config.site.title }} - {{ page_title|default('Home') }}</title>
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="/assets/css/style.css" rel="stylesheet">
      </head>
      <body>
        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
          <div class="container-fluid">
            <a class="navbar-brand" href="/index.html">{{ config.site.title }}</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav ms-auto">
                <li class="nav-item"><a class="nav-link" href="/about.html">About</a></li>
                <li class="nav-item"><a class="nav-link" href="/program.html">Program</a></li>
                <li class="nav-item"><a class="nav-link" href="/contact.html">Contact</a></li>
              </ul>
            </div>
          </div>
        </nav>

        {% block content %}{% endblock %}

        <footer class="bg-light text-center py-4 mt-5">
          <p class="mb-0">© {{ config.site.title }} {{ now().year }}</p>
        </footer>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
      </body>
    </html>
''')

index_html = textwrap.dedent('''
    {% extends 'base.html' %}
    {% block content %}
    <!-- Header image -->
    {% if upper_image %}
    <div class="container-fluid p-0">
      <img src="/upper_image/{{ upper_image }}" class="img-fluid w-100" alt="Header image">
    </div>
    {% endif %}

    <div class="container my-5">
      <h1 class="text-center mb-4">{{ config.event.title }}</h1>
      <p class="lead text-center">{{ config.event.description }}</p>
      <div class="row mt-4">
        <div class="col-md-4 text-center">
          <h3>📅 Dates</h3>
          <p>{{ config.event.dates }}</p>
        </div>
        <div class="col-md-4 text-center">
          <h3>🏢 Venue</h3>
          <p>{{ config.event.venue }}<br>{{ config.event.address }}</p>
        </div>
        <div class="col-md-4 text-center">
          {% if program_pdf %}
          <h3>📄 Program</h3>
          <a class="btn btn-primary" href="/program/{{ program_pdf }}" download>Download PDF</a>
          {% endif %}
        </div>
      </div>
    </div>

    <!-- Sponsors -->
    {% if sponsors %}
    <div class="container my-5">
      <h2 class="text-center mb-4">Sponsors</h2>
      <div class="row justify-content-center align-items-center">
        {% for sp in sponsors %}
        <div class="col-4 col-md-2 text-center my-2">
          <img src="/sponsors/{{ sp.filename }}" class="img-fluid" alt="{{ sp.name }} logo">
        </div>
        {% endfor %}
      </div>
    </div>
    {% endif %}
    {% endblock %}
''')

about_html = textwrap.dedent('''
    {% extends 'base.html' %}
    {% block content %}
    <div class="container my-5">
      <h1>About the Symposium</h1>
      <p>{{ content.about }}</p>
    </div>
    {% endblock %}
''')

program_html = textwrap.dedent('''
    {% extends 'base.html' %}
    {% block content %}
    <div class="container my-5">
      <h1>Program</h1>
      {% if program_pdf %}
      <p>You can download the full program <a href="/program/{{ program_pdf }}">here</a>.</p>
      {% endif %}
      {% if content.program_schedule %}
      {{ content.program_schedule | safe }}
      {% endif %}
    </div>
    {% endblock %}
''')

contact_html = textwrap.dedent('''
    {% extends 'base.html' %}
    {% block content %}
    <div class="container my-5">
      <h1>Contact</h1>
      <p>If you have any questions, please email us at <a href="mailto:info@example.com">info@example.com</a>.</p>
    </div>
    {% endblock %}
''')

template_dir = os.path.join(root, 'templates')
os.makedirs(template_dir, exist_ok=True)
files = {
    'base.html': base_html,
    'index.html': index_html,
    'about.html': about_html,
    'program.html': program_html,
    'contact.html': contact_html,
}
for fname, content in files.items():
    with open(os.path.join(template_dir, fname), 'w') as f:
        f.write(content)

# Content files
about_md = """The European Mobility Symposium is a two-day event focused on advancing research and collaboration in human mobility studies. Participants include academics, industry experts, and policymakers."""
with open(os.path.join(root, 'content', 'about.md'), 'w') as f:
    f.write(about_md)

# Configuration YAML
yaml_conf = {
    'site': {
        'title': 'European Mobility Symposium',
        'description': 'Sharing insights from recent works on human mobility',
        'url': 'https://username.github.io/european-mobility-symposium',
        'author': 'European Mobility Symposium Organizers'
    },
    'event': {
        'title': 'European Mobility Symposium',
        'dates': 'November 21-22, 2024',
        'venue': 'Officine Garibaldi, Aula Master',
        'address': 'Via Vincenzo Gioberti, 39, 56124 Pisa PI',
        'description': 'The European Mobility Symposium has the goal of sharing insights from recent works on human mobility and exploring new perspectives and potential collaborations—both in terms of research papers and project proposals.'
    }
}
import yaml
with open(os.path.join(root, 'config.yaml'), 'w') as f:
    yaml.safe_dump(yaml_conf, f)

# Simple CSS placeholder
with open(os.path.join(root, 'assets', 'css', 'style.css'), 'w') as f:
    f.write("body { scroll-behavior: smooth; }")

# requirements.txt
with open(os.path.join(root, 'requirements.txt'), 'w') as f:
    f.write("Jinja2\nPyYAML")

# README.md
readme_text = textwrap.dedent('''
    # European Mobility Symposium Static Site

    This repository contains the source code and build pipeline for the European Mobility Symposium static website. The site is generated with a simple Python script using Jinja2 templating and can be deployed to GitHub Pages.

    ## Prerequisites

    * Python 3.8+
    * pip

    ## Setup

    ```bash
    pip install -r requirements.txt
    ```

    ## Building the site

    ```bash
    python build.py build
    ```

    The generated HTML files will be in the `output/` folder.

    ## Serving locally

    ```bash
    python build.py serve --port 8000
    ```

    ## Deploying to GitHub Pages

    ```bash
    python build.py deploy
    ```

    or simply push to `main` and GitHub Actions will build and deploy automatically.
    ''')
with open(os.path.join(root, 'README.md'), 'w') as f:
    f.write(readme_text)

# GitHub Actions workflow
workflow = textwrap.dedent('''
    name: Build and Deploy

    on:
      push:
        branches: [ main ]

    permissions:
      contents: write

    jobs:
      build-deploy:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout
            uses: actions/checkout@v4

          - name: Setup Python
            uses: actions/setup-python@v5
            with:
              python-version: '3.x'

          - name: Install dependencies
            run: |
              python -m pip install --upgrade pip
              pip install -r requirements.txt

          - name: Build site
            run: python build.py build

          - name: Deploy to GitHub Pages
            uses: peaceiris/actions-gh-pages@v4
            with:
              github_token: ${{ secrets.GITHUB_TOKEN }}
              publish_dir: ./output
''')

wf_path = os.path.join(root, '.github', 'workflows', 'gh-pages.yml')
os.makedirs(os.path.dirname(wf_path), exist_ok=True)
with open(wf_path, 'w') as f:
    f.write(workflow)

print("Templates, content, workflow, README created.")