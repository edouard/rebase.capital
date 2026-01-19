# Copilot Instructions for rebase.capital

## Project Overview

**Rebase.capital** is a holding company that invests in and builds SaaS products. This repository contains the company's static website.

## Project Structure

```
index.html    # Main entry point - single-page static site
```

## Deployment

- Hosted on **GitHub Pages**
- Merges to `main` branch auto-deploy to production
- No build step - files are served directly

## Development Guidelines

### Tech Stack
- **Plain HTML with Tailwind CSS** via Play CDN (no build step)
- No npm, node_modules, or bundlers required
- Files are served as-is

### Tailwind CSS Setup
Include the Play CDN in `<head>`:
```html
<script src="https://cdn.tailwindcss.com"></script>
```

Custom configuration (optional):
```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          brand: '#your-color',
        }
      }
    }
  }
</script>
```

### Code Standards
- Use semantic HTML5 elements (`<header>`, `<main>`, `<section>`, `<footer>`)
- Use Tailwind utility classes for styling
- Mobile-first responsive design with Tailwind breakpoints (`sm:`, `md:`, `lg:`)
- Keep accessibility in mind (proper alt text, ARIA labels where needed)

### Adding Assets
- Custom CSS: Use `<style type="text/tailwindcss">` for Tailwind directives
- JavaScript: Use inline `<script>` or create `script.js` in root
- Images: Place in root or `images/` directory, optimize for web

### Local Development
- Open `index.html` directly in a browser, or
- Use a simple local server: `python3 -m http.server 8000`

## Content Guidelines

This is a corporate site for a SaaS holding company. Content should be:
- Professional and concise
- Focused on the company's investment thesis and portfolio
- Clean, modern design aesthetic
