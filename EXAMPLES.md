# Example: Adding New Content

## Scenario: Adding a Workshop Section

### 1. Update Content File
Add to `content/symposium.yaml`:

```yaml
workshops:
  - title: "Data Mining for Mobility Analysis"
    speaker: "Dr. Alice Johnson"
    time: "14:00-15:30"
    room: "Room A"
    description: "Introduction to data mining techniques for human mobility data"

  - title: "Privacy-Preserving Mobility Analytics"
    speaker: "Prof. Bob Wilson"
    time: "16:00-17:30" 
    room: "Room B"
    description: "Methods for analyzing mobility data while preserving privacy"
```

### 2. Update Template
Add to `templates/index.html` (after the Program section):

```html
<!-- Workshops -->
<section id="workshops" class="py-5 bg-light">
    <div class="container">
        <h2 class="text-center mb-5">Workshops</h2>
        <div class="row">
            {% for workshop in symposium.workshops %}
            <div class="col-lg-6 mb-4">
                <div class="card h-100">
                    <div class="card-body">
                        <h5 class="card-title text-primary">{{ workshop.title }}</h5>
                        <p class="text-muted mb-2">
                            <i class="fas fa-user me-2"></i>{{ workshop.speaker }}
                        </p>
                        <p class="text-muted mb-2">
                            <i class="fas fa-clock me-2"></i>{{ workshop.time }}
                        </p>
                        <p class="text-muted mb-3">
                            <i class="fas fa-door-open me-2"></i>{{ workshop.room }}
                        </p>
                        <p class="card-text">{{ workshop.description }}</p>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>
```

### 3. Update Navigation
Add to navbar in template:
```html
<li class="nav-item">
    <a class="nav-link" href="#workshops">Workshops</a>
</li>
```

### 4. Rebuild and Deploy
```bash
python build.py --serve  # Test locally
git add .
git commit -m "Add workshops section"
git push origin main     # Auto-deploy via GitHub Actions
```

## Result
The website now includes a workshops section with cards showing workshop details, integrated seamlessly with the existing design.
