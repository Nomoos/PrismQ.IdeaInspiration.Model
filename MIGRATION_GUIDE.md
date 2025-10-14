# Migration Guide: Field Naming Improvements

## Overview

This guide helps you migrate from the old field names to the new, more descriptive field names that better follow best practices for general/aggregated content naming.

## Field Name Changes

### 1. `score_detail` → `performance_multipliers`

**Old Name:** `score_detail`
**New Name:** `performance_multipliers`

**Rationale:** The new name is more descriptive and clearly indicates that these are performance multipliers (percentages) showing how content performs vs. industry standard/baseline.

### 2. `category_flags` → `content_strengths`

**Old Name:** `category_flags`
**New Name:** `content_strengths`

**Rationale:** The term "flags" implies boolean values, but these are actually strength ratings (0-100 scale). The new name "content_strengths" better describes what they represent.

## Migration Steps

### Step 1: Update Model Instantiation

**Before:**
```python
idea = IdeaInspiration(
    title="Article Title",
    score=85,
    score_detail={"US": 250, "woman": 150},
    category_flags={"innovation": 95, "tech": 88}
)
```

**After:**
```python
idea = IdeaInspiration(
    title="Article Title",
    score=85,
    performance_multipliers={"US": 250, "woman": 150},
    content_strengths={"innovation": 95, "tech": 88}
)
```

### Step 2: Update Factory Methods

**Before:**
```python
idea = IdeaInspiration.from_text(
    title="Article",
    text_content="Content...",
    score_detail={"US": 200},
    category_flags={"tech": 90}
)
```

**After:**
```python
idea = IdeaInspiration.from_text(
    title="Article",
    text_content="Content...",
    performance_multipliers={"US": 200},
    content_strengths={"tech": 90}
)
```

### Step 3: Update Field Access

**Before:**
```python
us_multiplier = idea.score_detail["US"]
tech_strength = idea.category_flags["tech"]
```

**After:**
```python
us_multiplier = idea.performance_multipliers["US"]
tech_strength = idea.content_strengths["tech"]
```

### Step 4: Update Serialization/Deserialization

**Before:**
```python
data = {
    "title": "Test",
    "score_detail": {"US": 250},
    "category_flags": {"innovation": 90}
}
idea = IdeaInspiration.from_dict(data)
```

**After:**
```python
data = {
    "title": "Test",
    "performance_multipliers": {"US": 250},
    "content_strengths": {"innovation": 90}
}
idea = IdeaInspiration.from_dict(data)
```

## Automated Migration Script

If you have a large codebase, you can use this script to help with the migration:

```python
import re
import os

def migrate_field_names(file_path):
    """Migrate old field names to new ones in a Python file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace field names
    content = content.replace('score_detail', 'performance_multipliers')
    content = content.replace('category_flags', 'content_strengths')
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"Migrated: {file_path}")

# Usage:
# migrate_field_names("your_file.py")
```

## Breaking Changes

⚠️ **Important:** These are breaking changes. Code using the old field names will need to be updated.

### Affected Areas:
- Direct field access (`idea.score_detail`, `idea.category_flags`)
- Factory method parameters
- Dictionary keys in serialization/deserialization
- Type hints and documentation

## Benefits of the New Names

1. **`performance_multipliers`**: Clearly indicates these are multipliers showing performance percentages
2. **`content_strengths`**: Better reflects that these are strength ratings (0-100 scale), not boolean flags

## Need Help?

If you encounter any issues during migration, please:
1. Review this guide carefully
2. Check the updated examples in `README.md`
3. Run the demo script: `python scoring_demo.py`
4. Review the comprehensive tests in `tests/test_idea_inspiration.py`

## Version Information

- **Old field names:** Deprecated in v0.2.1
- **New field names:** Introduced in v0.2.1
- **Full removal of old names:** Planned for v0.3.0
