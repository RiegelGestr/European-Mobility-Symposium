
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
