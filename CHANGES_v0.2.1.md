# Version 0.2.1 - Field Naming Improvements

## Overview

This release improves field naming to follow best practices for general/aggregated content naming, making the API more intuitive and self-documenting.

## Breaking Changes

### Field Name Changes

Two fields have been renamed for better clarity and alignment with best practices:

1. **`score_detail` → `performance_multipliers`**
   - Old name was vague and didn't clearly indicate the purpose
   - New name explicitly describes that these are performance multipliers (percentages)
   - Better conveys that values represent performance vs. industry standard/baseline

2. **`category_flags` → `content_strengths`**
   - Old name implied boolean flags, which was misleading
   - New name accurately reflects that these are strength ratings (0-100 scale)
   - More descriptive of the actual data being stored

## Migration Required

⚠️ **Action Required:** Code using the old field names must be updated. See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for detailed instructions.

### Quick Migration Examples

**Before (v0.2.0):**
```python
idea = IdeaInspiration.from_text(
    title="Article",
    score_detail={"US": 250},
    category_flags={"tech": 90}
)
us_perf = idea.score_detail["US"]
tech_strength = idea.category_flags["tech"]
```

**After (v0.2.1):**
```python
idea = IdeaInspiration.from_text(
    title="Article",
    performance_multipliers={"US": 250},
    content_strengths={"tech": 90}
)
us_perf = idea.performance_multipliers["US"]
tech_strength = idea.content_strengths["tech"]
```

## What Changed

### Core Model (`idea_inspiration.py`)
- Renamed `score_detail` field to `performance_multipliers`
- Renamed `category_flags` field to `content_strengths`
- Updated all method signatures in factory methods (`from_text`, `from_video`, `from_audio`)
- Updated docstrings to reflect new field names

### Tests (`test_idea_inspiration.py`)
- Updated all test methods to use new field names
- Renamed test methods for clarity:
  - `test_create_with_score_detail` → `test_create_with_performance_multipliers`
  - `test_create_with_category_flags` → `test_create_with_content_strengths`
- All 32 tests passing

### Documentation
- **README.md**: Updated all examples and field descriptions
- **CHANGES_v0.2.0.md**: Updated to reflect new field names
- **MIGRATION_GUIDE.md**: New comprehensive migration guide created
- **scoring_demo.py**: Updated demo script with new field names

## Benefits

1. **Clearer Intent**: Field names now clearly communicate their purpose
2. **Better Type Safety**: More descriptive names help IDEs provide better autocomplete
3. **Self-Documenting**: Code is more readable without needing to reference documentation
4. **Industry Standard**: Follows naming best practices for aggregated/general content

## Rationale

### Why `performance_multipliers`?
- "Performance" clearly indicates these are performance metrics
- "Multipliers" explicitly states these are percentage multipliers (e.g., 250% = 2.5x)
- The name answers "what is this?" without requiring additional context

### Why `content_strengths`?
- "Content" indicates these relate to the content itself
- "Strengths" conveys the 0-100 rating scale concept
- Avoids confusion with boolean "flags"
- More intuitive for developers using the API

## Backward Compatibility

⚠️ **Breaking Changes**: This release is **not** backward compatible with code using the old field names.

To minimize disruption:
- Follow the [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for step-by-step instructions
- Use the provided migration script to automate updates
- Test thoroughly after migration

## Testing

- ✅ All 32 existing tests updated and passing
- ✅ Black formatting applied
- ✅ CodeQL security scan: 0 vulnerabilities
- ✅ End-to-end integration tests passing
- ✅ Demo scripts verified working

## Files Changed

- `prismq/idea/model/idea_inspiration.py` - Core model updated
- `tests/test_idea_inspiration.py` - All tests updated
- `README.md` - Documentation updated
- `CHANGES_v0.2.0.md` - Historical changelog updated
- `scoring_demo.py` - Demo script updated
- `MIGRATION_GUIDE.md` - New migration guide created
- `example.py`, `sqlite_demo.py`, `setup.py` - Black formatting applied

## Contributors

- PrismQ Development Team
- GitHub Copilot

## Version Info

- **Version**: 0.2.1
- **Previous Version**: 0.2.0
- **Release Date**: 2025-10-14
- **Python Compatibility**: Python 3.8+

## Next Steps

After upgrading to v0.2.1:
1. Review the [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)
2. Update your code to use the new field names
3. Run your tests to verify everything works
4. Update any documentation referencing the old field names
