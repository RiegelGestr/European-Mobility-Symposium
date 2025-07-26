# European Mobility Symposium Website

A Python-based static site generator that reproduces the European Mobility Symposium website using Jinja2 templates and Bootstrap 5.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git (for deployment)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/username/european-mobility-symposium.git
cd european-mobility-symposium
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Build the website:
```bash
python build.py
```

4. Open `output/index.html` in your browser to view the site.

## 🛠️ Usage

### Basic Build
```bash
# Build the site
python build.py

# Build and serve locally
python build.py --serve

# Build and serve on custom port
python build.py --serve --port 8080
```

### Development Workflow
```bash
# Build and serve with auto-reload during development
python build.py --serve
```

### Deployment to GitHub Pages
```bash
# Deploy to GitHub Pages (requires git setup)
python build.py --deploy
```

## 📁 Project Structure

```
european-mobility-symposium/
├── build.py                 # Main build script
├── config.yaml             # Site configuration
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── content/               # Content files
│   └── symposium.yaml     # Symposium data
├── templates/             # Jinja2 templates
│   └── index.html         # Main template
├── assets/                # Static assets
│   ├── css/
│   │   └── style.css      # Custom CSS
│   └── js/
│       └── main.js        # Custom JavaScript
├── output/                # Generated site (created after build)
└── .github/
    └── workflows/
        └── gh-pages.yml   # GitHub Actions workflow
```

## ⚙️ Configuration

### Site Configuration (`config.yaml`)

Edit `config.yaml` to customize:
- Site title and description
- Bootstrap theme
- Social media links
- Navigation menu

### Content (`content/symposium.yaml`)

Edit `content/symposium.yaml` to update:
- Event details (dates, venue, location)
- Participant list
- Organizer information
- Program information

## 🎨 Customization

### Templates

The main template is in `templates/index.html`. It uses Jinja2 templating:
- `{{ variable }}` for simple variables
- `{% for item in items %}` for loops
- `{% if condition %}` for conditionals

### Styling

Custom CSS is in `assets/css/style.css`. The site uses:
- Bootstrap 5.3.0 from CDN
- Font Awesome 6.4.0 for icons
- Custom CSS for additional styling

### JavaScript

Custom JavaScript is in `assets/js/main.js` and includes:
- Smooth scrolling navigation
- Active navigation highlighting
- Card hover effects
- Mobile menu handling

## 🚀 Deployment

### GitHub Pages (Recommended)

1. Push your code to a GitHub repository
2. Go to repository Settings > Pages
3. Set source to "GitHub Actions"
4. The included workflow will automatically build and deploy

### Manual GitHub Pages

```bash
# Build the site
python build.py

# Deploy to gh-pages branch
python build.py --deploy
```

### Other Hosting Providers

The generated `output/` folder contains a complete static website that can be hosted on:
- Netlify
- Vercel
- AWS S3
- Any web server

## 🔧 Advanced Usage

### Custom Templates

Create additional templates in the `templates/` folder and render them in `build.py`:

```python
generator.render_page(
    template_name="custom.html",
    output_name="custom.html",
    context={"custom_data": data}
)
```

### Multiple Pages

Add multiple pages by creating new templates and updating the build script:

```python
# In build.py build() method
self.render_page("about.html", "about.html", context)
self.render_page("contact.html", "contact.html", context)
```

### Custom Content Types

Add new content files in `content/` directory:
- JSON files: `content/speakers.json`
- YAML files: `content/schedule.yaml`
- Markdown files: Process with additional libraries

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test the build: `python build.py`
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Original website: [European Mobility Symposium 2024](https://ems2024pisa.github.io/europeanmobilitysymposium/)
- Built with [Python](https://python.org/)
- Templates powered by [Jinja2](https://jinja.palletsprojects.com/)
- Styled with [Bootstrap 5](https://getbootstrap.com/)
- Icons from [Font Awesome](https://fontawesome.com/)

## 📞 Support

If you encounter any issues:

1. Check the [Issues](https://github.com/username/european-mobility-symposium/issues) page
2. Create a new issue with detailed information
3. Include your Python version and operating system

## 🔄 Updates

To update the site content:

1. Edit `content/symposium.yaml`
2. Run `python build.py`
3. Commit and push changes (auto-deployment will handle the rest)

---

**Built with ❤️ using Python and Bootstrap**
