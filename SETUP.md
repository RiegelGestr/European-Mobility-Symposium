# European Mobility Symposium - Setup Guide

## 🚀 Complete Setup Instructions

### 1. Initial Setup

```bash
# Clone or download the project
git clone https://github.com/username/european-mobility-symposium.git
cd european-mobility-symposium

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

#### Update Site Information
Edit `config.yaml`:
```yaml
site:
  title: "Your Symposium Title"
  url: "https://yourusername.github.io/your-repo"
```

#### Update Content
Edit `content/symposium.yaml` to modify:
- Event details (dates, venue)
- Participant list
- Organizer information

### 3. Building the Site

```bash
# Basic build
python build.py

# Build and serve locally
python build.py --serve

# Build and serve on different port
python build.py --serve --port 3000
```

### 4. GitHub Pages Deployment

#### Option A: Automatic Deployment (Recommended)
1. Push code to GitHub repository
2. Go to repository Settings → Pages
3. Set source to "GitHub Actions"
4. The workflow will automatically deploy on push to main

#### Option B: Manual Deployment
```bash
python build.py --deploy
```

### 5. Customization Examples

#### Adding New Participants
Edit `content/symposium.yaml`:
```yaml
participants:
  - institution: "New University"
    people:
      - "Dr. Jane Smith"
      - "Prof. John Doe"
```

#### Updating Event Details
```yaml
event:
  venue: "New Venue Name"
  dates: "March 15-16, 2025"
  location_name: "New Location"
```

#### Custom Styling
Edit `assets/css/style.css` to modify:
- Colors and themes
- Layout adjustments
- Typography

### 6. Advanced Usage

#### Multiple Pages
Create new template in `templates/`:
```html
<!-- templates/speakers.html -->
<h1>{{ page_title }}</h1>
<!-- Your content -->
```

Update `build.py`:
```python
# In build() method
self.render_page("speakers.html", "speakers.html", {"page_title": "Speakers"})
```

#### Custom Content Types
Create new content files:
- `content/speakers.yaml`
- `content/schedule.json`

Load in `build.py`:
```python
speakers = self.load_content("speakers.yaml")
```

### 7. Troubleshooting

#### Common Issues

**Build fails with missing modules:**
```bash
pip install -r requirements.txt
```

**GitHub Pages not updating:**
- Check Actions tab for build errors
- Ensure `gh-pages.yml` workflow is enabled
- Verify repository settings

**CSS/JS not loading:**
- Check file paths in templates
- Ensure assets are in correct directories
- Verify Bootstrap CDN links

#### File Structure Check
```
project/
├── build.py ✓
├── config.yaml ✓
├── content/symposium.yaml ✓
├── templates/index.html ✓
└── assets/css/style.css ✓
```

### 8. Development Workflow

1. Edit content in `content/symposium.yaml`
2. Modify templates in `templates/`
3. Update styles in `assets/css/style.css`
4. Test locally: `python build.py --serve`
5. Commit and push to GitHub
6. GitHub Actions deploys automatically

### 9. Production Checklist

- [ ] Update all placeholder content
- [ ] Add real program PDF to `assets/`
- [ ] Update GitHub repository URL in config
- [ ] Test all navigation links
- [ ] Verify mobile responsiveness
- [ ] Check Google Maps integration
- [ ] Test GitHub Pages deployment

### 10. Maintenance

#### Regular Updates
- Update Bootstrap version in templates
- Update Python dependencies: `pip install -r requirements.txt --upgrade`
- Monitor GitHub Actions for security updates

#### Content Updates
- Edit YAML files for content changes
- No need to modify HTML templates
- Automatic deployment on git push

---

Need help? Check the README.md or create an issue on GitHub!
