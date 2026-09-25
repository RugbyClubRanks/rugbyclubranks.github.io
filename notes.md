# CSS Pattern System Documentation

## Pattern System Overview

The site uses CSS-based header patterns instead of images to avoid copyright issues and provide easy customization. All patterns are defined in `_sass/_07_layout.scss` and use corporate identity colors from `_sass/_01_settings_colors.scss`.

## Available CSS Patterns

- `pattern-rugby` - Dark blue with subtle diagonal stripes (for rugby pages)
- `pattern-data` - Dark blue with grid lines (for data-heavy/blog content)
- `pattern-clean` - Purple gradient (for design/modern pages)
- `pattern-dark` - Professional dark with subtle texture (for about/changelog)
- `pattern-racing` - Blue with speed lines (ready for F1)
- `pattern-football` - Green with horizontal lines (ready for college football)
- `pattern-tech` - Multi-color gradient (for technical documentation)

## Corporate Identity Color Variables

Located in `_sass/_01_settings_colors.scss`:
- `$ci-1` through `$ci-13` - Brand colors that all patterns reference
- Update these hex codes to change all patterns automatically

## Current Pattern Assignments

### ✅ Already Using Patterns

**Rugby-Related:**
- Homepage (`pages/pages-root-folder/index.md`) → `pattern-rugby`
- Rugby Homepage (`pages/rugby/index.md`) → `pattern-rugby`

**Professional/About:**
- About Page (`pages/info.md`) → `pattern-dark`
- Changelog (`pages/changelog.md`) → `pattern-dark`

**Design/Documentation:**
- Roadmap (`pages/roadmap.md`) → `pattern-clean`
- Design Pages (`pages/design.md`, `pages/headers.md`) → `pattern-clean`
- Documentation (`pages/documentation.md`) → `pattern-tech`

**Blog:**
- Blog Pages (`blog/index.html`, `blog/archive.html`) → `pattern-data`

### ❌ Currently Using Default Blue Background

**Core Rugby Pages (High Priority):**
- Current Projections (`pages/rugby/Current_Projections.md`) → Should use `pattern-rugby`
- Competitions (`pages/rugby/Competitions.md`) → Should use `pattern-rugby`
- Recent Matches (`pages/rugby/Recent_Matches.md`) → Should use `pattern-rugby`
- Accuracy Page (`pages/rugby/accuracy_page.md`) → Should use `pattern-data`

**General Pages (Medium Priority):**
- Contact Page (`pages/contact.md`) → Should use `pattern-dark`
- FAQ Page (`pages/faq.md`) → Should use `pattern-light`

## How to Apply Patterns to Pages

### Example: Changing Current Projections Page

**Current file** (`pages/rugby/Current_Projections.md`):
```yaml
---
layout: page
title: Current Projections
key: page-projections
categories: rugby
---
```

**Add pattern_class to front matter:**
```yaml
---
layout: page
title: Current Projections
key: page-projections
categories: rugby
header:
  pattern_class: pattern-rugby
---
```

### General Pattern Application

To add a pattern to any page, add this to the front matter:

```yaml
---
header:
  pattern_class: pattern-rugby  # or any other pattern name
---
```

## Pattern Selection Guidelines

### **Rugby-Related Pages → `pattern-rugby`**
- Use for main rugby section pages
- Core rugby content and landing pages
- Competition overview pages

### **Data/Analysis Pages → `pattern-data`**
- Accuracy and statistics pages
- Grid lines suggest data analysis focus
- Blog and documentation with data content

### **Design/Documentation Pages → `pattern-clean` or `pattern-tech`**
- `pattern-clean`: Modern, clean design pages
- `pattern-tech`: Technical documentation with multi-color gradients

### **Professional/About Pages → `pattern-dark`**
- About pages, contact pages
- Professional content with subtle texture
- Changelog and informational pages

### **Future Sections:**
- **F1 Pages** → `pattern-racing` (speed lines theme)
- **College Football Pages** → `pattern-football` (field lines theme)

## Pages That Don't Need Patterns

**Individual competition/projection pages** (50+ competition files, 80+ projection files):
- These are data-heavy pages where users focus on content/plots
- Default blue background provides consistency without distraction
- Adding patterns might create visual fatigue
- Better to keep default for better focus on data

## Color Coordination

All patterns reference the corporate identity color variables:
- `$ci-1` - Main brand color (currently #334D5C)
- `$ci-2` - Secondary accent color (currently #45B29D)
- `$ci-3` through `$ci-13` - Additional brand colors

**To update brand colors:**
1. Extract colors from logo using color picker tool
2. Update hex codes in `_sass/_01_settings_colors.scss`
3. All patterns automatically update to use new colors
4. No need to modify individual pattern definitions

## Customizing Patterns

Patterns use SCSS functions for color variations:
- `darken($ci-1, 20%)` - Makes color 20% darker
- `lighten($ci-1, 15%)` - Makes color 15% lighter
- `mix($color1, $color2, 50%)` - Blends two colors

Edit patterns in `_sass/_07_layout.scss` (lines 367-485) to adjust:
- Gradient angles (change `135deg` to other angles)
- Pattern density (adjust pixel values like `10px` to `15px`)
- Opacity (change `rgba(255,255,255,0.03)` to make patterns more/less visible)

## Testing Changes

1. Edit color variables in `_sass/_01_settings_colors.scss`
2. Run `bundle exec jekyll build` to rebuild
3. Run `bundle exec jekyll serve` to test locally
4. View at `http://127.0.0.1:4000`
5. Changes auto-regenerate when SCSS files are modified

## Benefits of This System

- **Zero copyright issues** - All patterns are CSS-generated
- **Lightweight** - No additional HTTP requests
- **Consistent branding** - Easy to customize via CI variables
- **Future-proof** - Patterns ready for F1 and college football sections
- **Rights-free** - Completely original CSS patterns
- **Maintainable** - Single source of truth for all colors


3. External CSS Pattern Tools
CSS Gradient Generators:

cssgradient.io - Create and preview CSS gradients
gradientmagic.buttonshift.io - Complex gradient patterns
webgradients.com - Pre-made CSS gradients
Pattern Generators:

transparenttextures.com - CSS pattern library
patternizer.com - Create stripe/dot patterns
csspatterns.com - Various CSS patterns

🔧 Recommended Workflow:
Open http://127.0.0.1:4000/pattern-preview/ in your browser
Edit _01_settings_colors.scss to change colors
Save the file
Refresh the preview page - see changes instantly
Fine-tune colors until satisfied
Apply to actual pages using the pattern names