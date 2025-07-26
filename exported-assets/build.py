#!/usr/bin/env python3
"""
European Mobility Symposium Static Site Generator
Build script for generating the static website using Jinja2 templates
"""

import os
import sys
import json
import yaml
import shutil
import subprocess
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
import requests
from urllib.parse import urljoin, urlparse
import argparse


class SiteBuilder:
    def __init__(self, config_path="config.yaml"):
        self.root_dir = Path(__file__).parent.absolute()
        self.config_path = self.root_dir / config_path
        self.config = self.load_config()

        # Setup paths
        self.templates_dir = self.root_dir / "templates"
        self.content_dir = self.root_dir / "content" 
        self.assets_dir = self.root_dir / "assets"
        self.output_dir = self.root_dir / "output"
        self.program_dir = self.root_dir / "program"
        self.upper_image_dir = self.root_dir / "upper_image"
        self.sponsors_dir = self.root_dir / "sponsors"

        # Setup Jinja2 environment
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(self.templates_dir)),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def load_config(self):
        """Load site configuration"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Config file {self.config_path} not found. Using defaults.")
            return self.get_default_config()

    def get_default_config(self):
        """Return default configuration"""
        return {
            'site': {
                'title': 'European Mobility Symposium',
                'description': 'Sharing insights from recent works on human mobility',
                'url': 'https://username.github.io/european-mobility-symposium',
                'author': 'European Mobility Symposium Organizers'
            },
            'event': {
                'title': 'European Mobility Symposium',
                'dates': 'November 21-22, 2024',
                'venue': 'Officine Garibaldi, second floor, Aula Master',
                'address': 'Via Vincenzo Gioberti, 39, 56124 Pisa PI',
                'description': 'The European Mobility Symposium has the goal of sharing insights from recent works on human mobility and exploring new perspectives and potential collaborations—both in terms of research papers and project proposals.'
            }
        }

    def load_content(self):
        """Load page content from markdown/yaml files"""
        content = {}

        # Load main content
        for content_file in self.content_dir.glob("*.md"):
            with open(content_file, 'r', encoding='utf-8') as f:
                content[content_file.stem] = f.read()

        for content_file in self.content_dir.glob("*.yaml"):
            with open(content_file, 'r', encoding='utf-8') as f:
                content[content_file.stem] = yaml.safe_load(f)

        return content

    def get_sponsors(self):
        """Get list of sponsor images"""
        sponsors = []
        if self.sponsors_dir.exists():
            for img_file in self.sponsors_dir.glob("*"):
                if img_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.svg']:
                    sponsors.append({
                        'filename': img_file.name,
                        'name': img_file.stem.replace('_', ' ').replace('-', ' ').title()
                    })
        return sponsors

    def get_upper_image(self):
        """Get the main header image"""
        if self.upper_image_dir.exists():
            for img_file in self.upper_image_dir.glob("*"):
                if img_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
                    return img_file.name
        return None

    def get_program_pdf(self):
        """Get the program PDF file"""
        if self.program_dir.exists():
            for pdf_file in self.program_dir.glob("*.pdf"):
                return pdf_file.name
        return None

    def clean_output(self):
        """Clean the output directory"""
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def copy_assets(self):
        """Copy static assets to output directory"""
        if self.assets_dir.exists():
            shutil.copytree(self.assets_dir, self.output_dir / "assets", dirs_exist_ok=True)

        # Copy program PDF
        if self.program_dir.exists():
            shutil.copytree(self.program_dir, self.output_dir / "program", dirs_exist_ok=True)

        # Copy upper image
        if self.upper_image_dir.exists():
            shutil.copytree(self.upper_image_dir, self.output_dir / "upper_image", dirs_exist_ok=True)

        # Copy sponsors
        if self.sponsors_dir.exists():
            shutil.copytree(self.sponsors_dir, self.output_dir / "sponsors", dirs_exist_ok=True)

    def render_template(self, template_name, context, output_path):
        """Render a template with context and save to output path"""
        template = self.jinja_env.get_template(template_name)
        rendered = template.render(**context)

        output_file = self.output_dir / output_path
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(rendered)

        print(f"Generated: {output_path}")

    def build_site(self):
        """Build the complete site"""
        print("Building European Mobility Symposium website...")

        # Clean and prepare output directory
        self.clean_output()

        # Copy static assets
        self.copy_assets()

        # Load content
        content = self.load_content()

        # Prepare template context
        context = {
            'config': self.config,
            'content': content,
            'sponsors': self.get_sponsors(),
            'upper_image': self.get_upper_image(),
            'program_pdf': self.get_program_pdf()
        }

        # Render pages
        pages = [
            ('index.html', 'index.html'),
            ('about.html', 'about.html'),
            ('program.html', 'program.html'),
            ('contact.html', 'contact.html')
        ]

        for template_name, output_name in pages:
            if (self.templates_dir / template_name).exists():
                self.render_template(template_name, context, output_name)
            else:
                print(f"Warning: Template {template_name} not found")

        print("Site build completed successfully!")

    def serve_locally(self, port=8000):
        """Serve the site locally for development"""
        os.chdir(self.output_dir)
        try:
            import http.server
            import socketserver

            Handler = http.server.SimpleHTTPRequestHandler
            with socketserver.TCPServer(("", port), Handler) as httpd:
                print(f"Serving at http://localhost:{port}")
                print("Press Ctrl+C to stop the server")
                httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

    def deploy_to_github(self):
        """Deploy to GitHub Pages (commits and pushes to gh-pages branch)"""
        print("Deploying to GitHub Pages...")

        try:
            # Add and commit changes
            subprocess.run(['git', 'add', '.'], check=True, cwd=self.root_dir)
            subprocess.run(['git', 'commit', '-m', 'Update site content'], 
                         check=True, cwd=self.root_dir)

            # Push to main branch
            subprocess.run(['git', 'push', 'origin', 'main'], check=True, cwd=self.root_dir)

            # Deploy to gh-pages using subtree
            subprocess.run(['git', 'subtree', 'push', '--prefix', 'output', 'origin', 'gh-pages'], 
                         check=True, cwd=self.root_dir)

            print("Successfully deployed to GitHub Pages!")

        except subprocess.CalledProcessError as e:
            print(f"Deployment failed: {e}")
            print("Make sure you have git configured and the repository set up correctly.")


def main():
    parser = argparse.ArgumentParser(description='European Mobility Symposium Site Builder')
    parser.add_argument('command', choices=['build', 'serve', 'deploy'], 
                       help='Command to execute')
    parser.add_argument('--port', type=int, default=8000, 
                       help='Port for local server (default: 8000)')
    parser.add_argument('--config', default='config.yaml',
                       help='Configuration file path')

    args = parser.parse_args()

    builder = SiteBuilder(args.config)

    if args.command == 'build':
        builder.build_site()
    elif args.command == 'serve':
        builder.build_site()
        builder.serve_locally(args.port)
    elif args.command == 'deploy':
        builder.build_site()
        builder.deploy_to_github()


if __name__ == '__main__':
    main()
