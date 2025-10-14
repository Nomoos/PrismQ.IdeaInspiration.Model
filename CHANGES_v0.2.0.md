# Version 0.2.0 - Scoring and Category Fields

## Overview

This release adds comprehensive scoring and categorization capabilities to the IdeaInspiration model, enabling content evaluation and performance tracking across different markets and demographics.

## New Features

### 1. Score Field (`Optional[int]`)
- Numerical score value for overall content evaluation
- Optional field, defaults to `None`
- Example: `score=85`

### 2. Category Field (`Optional[str]`)
- Category classification for content organization
- Optional field, defaults to `None`
- Example: `category="technology"`

### 3. Score Detail (`Dict[str, int]`)
- Category-specific score multipliers showing performance percentages
- Indicates how content performs vs. industry standard/baseline
- Empty dict by default
- Example use cases:
  - Market performance: `{"US": 250, "Europe": 180}` (250% performance in US vs standard)
  - Demographic performance: `{"woman": 150, "man": 140}` (150% performance with women demographic)
  - Category performance: `{"tech": 180, "startup": 200}` (180% performance in tech category)

### 4. Category Flags (`Dict[str, int]`)
- Content flavor strength ratings on 0-100 scale
- Indicates how strongly content aligns with specific themes/categories
- Empty dict by default
- Example: `{"innovation": 95, "technology": 88, "education": 70}`

## API Changes

### Data Model Updates

**Before (v0.1.0):**
```python
@dataclass
class IdeaInspiration:
    title: str
    description: str = ""
    content: str = ""
    keywords: List[str] = field(default_factory=list)
    source_type: ContentType = ContentType.UNKNOWN
    metadata: Dict[str, str] = field(default_factory=dict)
    source_id: Optional[str] = None
    source_url: Optional[str] = None
```

**After (v0.2.0):**
```python
@dataclass
class IdeaInspiration:
    title: str
    description: str = ""
    content: str = ""
    keywords: List[str] = field(default_factory=list)
    source_type: ContentType = ContentType.UNKNOWN
    metadata: Dict[str, str] = field(default_factory=dict)
    source_id: Optional[str] = None
    source_url: Optional[str] = None
    score: Optional[int] = None  # NEW
    category: Optional[str] = None  # NEW
    score_detail: Dict[str, int] = field(default_factory=dict)  # NEW
    category_flags: Dict[str, int] = field(default_factory=dict)  # NEW
```

### Factory Method Updates

All factory methods now support the new fields:

- `IdeaInspiration.from_text()` - Added `score`, `category`, `score_detail`, `category_flags` parameters
- `IdeaInspiration.from_video()` - Added `score`, `category`, `score_detail`, `category_flags` parameters
- `IdeaInspiration.from_audio()` - Added `score`, `category`, `score_detail`, `category_flags` parameters

### Serialization Updates

- `to_dict()` - Now includes new scoring and category fields
- `from_dict()` - Now correctly deserializes new fields

## Usage Examples

### Basic Scoring
```python
idea = IdeaInspiration.from_text(
    title="Introduction to Machine Learning",
    text_content="ML is revolutionizing...",
    score=85,
    category="technology"
)
```

### Score Detail - Market Performance
```python
idea = IdeaInspiration.from_video(
    title="Tech Startup Success Stories",
    subtitle_text="Learn from entrepreneurs...",
    score=90,
    category="business",
    score_detail={
        "US": 250,      # 250% vs standard in US market
        "Europe": 180,  # 180% vs standard in Europe
        "woman": 150,   # 150% performance with women
    }
)
```

### Category Flags - Content Flavor
```python
idea = IdeaInspiration.from_audio(
    title="Healthcare Innovation Podcast",
    transcription="Breakthrough technologies...",
    score=88,
    category="healthcare",
    category_flags={
        "innovation": 95,   # Very strong innovation flavor
        "technology": 88,   # Strong technology flavor
        "healthcare": 92,   # Very strong healthcare flavor
    }
)
```

## Testing

### New Test Coverage
- 12 new comprehensive tests added
- Total tests: 32 (up from 20)
- Test coverage: 98%
- All tests passing

### Test Classes Added
- `TestIdeaInspirationScoringFields` - Comprehensive testing of new scoring features

## Backward Compatibility

✅ **Fully backward compatible** - All existing code will continue to work without modifications:
- New fields are optional with sensible defaults
- Existing serialization/deserialization works unchanged
- Factory methods accept new parameters but don't require them
- All v0.1.0 tests pass without modification

## Documentation Updates

### Updated Files
- `README.md` - Added new fields to data model table, added scoring examples section
- `prismq/idea/model/idea_inspiration.py` - Updated docstrings with new field descriptions
- `tests/test_idea_inspiration.py` - Added comprehensive test suite

### New Files
- `scoring_demo.py` - Interactive demonstration of scoring features
- `CHANGES_v0.2.0.md` - This changelog

## Demo Script

Run the new scoring demonstration:

```bash
python scoring_demo.py
```

This demonstrates:
- Basic scoring and category assignment
- Score detail with market-specific multipliers
- Category flags with flavor strength ratings
- Comprehensive scoring examples with visual output
- Serialization with scoring fields

## Quality Assurance

✅ All checks passing:
- ✅ Black formatting
- ✅ Flake8 linting
- ✅ MyPy type checking
- ✅ CodeQL security scanning (0 vulnerabilities)
- ✅ 32 tests passing (100% success rate)
- ✅ 98% code coverage

## Migration Guide

### No Migration Required
Since this release is fully backward compatible, no code changes are needed. To use the new features, simply update to v0.2.0 and start using the new optional fields.

### To Add Scoring to Existing Code
```python
# Old code (still works)
idea = IdeaInspiration.from_text(
    title="My Article",
    text_content="Content..."
)

# Enhanced with scoring (v0.2.0)
idea = IdeaInspiration.from_text(
    title="My Article",
    text_content="Content...",
    score=85,
    category="technology",
    score_detail={"US": 250},
    category_flags={"innovation": 90}
)
```

## Contributors

- PrismQ Development Team
- GitHub Copilot

## Version Info

- **Version**: 0.2.0
- **Previous Version**: 0.1.0
- **Release Date**: 2025-10-14
- **Python Compatibility**: Python 3.8+
