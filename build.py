#!/usr/bin/env python3
"""
Static Site Generator for European Mobility Symposium
Reproduces the symposium website using Python, Jinja2, and Bootstrap
"""

import os
import json
import yaml
import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
import argparse
import subprocess
import sys

class StaticSiteGenerator:
    def __init__(self, config_file="config.yaml"):
        
        self.base_dir = Path(__file__).parent
        self.templates_dir = self.base_dir / "templates"
        self.content_dir = self.base_dir / "content"
        self.assets_dir = self.base_dir / "assets"
        self.output_dir = self.base_dir / "output"

        # Load configuration
        self.config = self.load_config(config_file)

        # Setup Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(str(self.templates_dir)),
            autoescape=True
        )

    def load_config(self, config_file):
        """Load site configuration from YAML file"""
        config_path = self.base_dir / config_file
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        return {}

    def load_content(self, content_file):
        """Load content from JSON or YAML file"""
        content_path = self.content_dir / content_file
        if not content_path.exists():
            return {}

        with open(content_path, 'r', encoding='utf-8') as f:
            if content_file.endswith('.json'):
                return json.load(f)
            elif content_file.endswith(('.yaml', '.yml')):
                return yaml.safe_load(f)
        return {}

    def ensure_output_dir(self):
        """Create or clean output directory"""
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def copy_assets(self):
        """Copy static assets to output directory"""
        if self.assets_dir.exists():
            dest_assets = self.output_dir / "assets"
            shutil.copytree(self.assets_dir, dest_assets, dirs_exist_ok=True)
            print(f"Copied assets to {dest_assets}")
            
            # List copied image files for debugging
            images_dir = dest_assets / "images"
            if images_dir.exists():
                print("⚠️  No images directory found in assets!")
        else:
            print("⚠️  Assets directory not found!")
    def render_page(self, template_name, output_name, context=None):
        """Render a single page using Jinja2 template"""
        if context is None:
            context = {}

        # Add global context
        context.update({
            'site': self.config.get('site', {}),
            'config': self.config
        })

        template = self.env.get_template(template_name)
        rendered = template.render(**context)

        output_path = self.output_dir / output_name
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered)

        print(f"Generated {output_path}")

    def build(self):
        """Build the complete site"""
        print("Building European Mobility Symposium website...")

        # Ensure clean output directory
        self.ensure_output_dir()

        # Copy static assets
        self.copy_assets()

        # Load content data
        symposium_data = self.load_content("symposium.yaml")

        # Render main page
        self.render_page(
            template_name="index.html",
            output_name="index.html",
            context={"symposium": symposium_data}
        )
        '''
        data = self.load_content("symposium.yaml")

        self.render_page(
            template_name="index.html",
            context={
                **data,               # exposes hero_image & sponsors automatically
                "map_query": self.get_map_query(data),
            },
            output_path="output/index.html",
        )
        '''
        print("✅ Site built successfully!")
        print(f"📁 Output directory: {self.output_dir}")
        print(f"🌐 Open {self.output_dir / 'index.html'} in your browser")

    def serve(self, port=8000):
        """Serve the site locally for development"""
        import http.server
        import socketserver
        import webbrowser

        os.chdir(self.output_dir)
        handler = http.server.SimpleHTTPRequestHandler

        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"🚀 Serving at http://localhost:{port}")
            webbrowser.open(f"http://localhost:{port}")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\n⏹️ Server stopped")

    def deploy_to_github_pages(self):
        """Deploy to GitHub Pages (optional)"""
        if not (self.base_dir / ".git").exists():
            print("❌ Not a git repository. Initialize git first.")
            return

        try:
            # Add and commit changes
            subprocess.run(["git", "add", "output/"], check=True)
            subprocess.run(["git", "commit", "-m", "Update site"], check=True)

            # Push to gh-pages branch
            subprocess.run(["git", "subtree", "push", "--prefix", "output", "origin", "gh-pages"], check=True)
            print("✅ Deployed to GitHub Pages!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Deployment failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Static Site Generator for European Mobility Symposium")
    parser.add_argument("--config", default="config.yaml", help="Configuration file")
    parser.add_argument("--serve", action="store_true", help="Serve the site locally after building")
    parser.add_argument("--port", type=int, default=8000, help="Port for local server")
    parser.add_argument("--deploy", action="store_true", help="Deploy to GitHub Pages")

    args = parser.parse_args()

    generator = StaticSiteGenerator(args.config)
    generator.build()

    if args.deploy:
        generator.deploy_to_github_pages()
    elif args.serve:
        generator.serve(args.port)

if __name__ == "__main__":
    main()
