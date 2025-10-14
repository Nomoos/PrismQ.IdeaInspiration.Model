# PrismQ.IdeaInspiration.Model

**Core data model for content ideas across the PrismQ ecosystem**

## Overview

This package provides the `IdeaInspiration` data model used across PrismQ modules including:
- **[PrismQ.IdeaInspiration.Scoring](https://github.com/Nomoos/PrismQ.IdeaInspiration.Scoring)** - Content scoring engine
- **[PrismQ.IdeaInspiration.Classification](https://github.com/Nomoos/PrismQ.IdeaInspiration.Classification)** - Content classification
- **PrismQ.IdeaInspiration.Builder** - Model construction from various sources
- **PrismQ.IdeaInspiration.Sources** - Content source integrations

The model provides a unified structure for representing content ideas from various sources (text, video, audio) with factory methods for easy creation from different content types.

## Features

- 🎯 **Unified Data Model** - Single structure for text, video, and audio content
- 🏭 **Factory Methods** - Easy creation from different sources (text, YouTube, Reddit, etc.)
- 📦 **Serialization** - Convert to/from dictionaries for storage and transmission
- 🔌 **Zero Dependencies** - Pure Python with no external requirements
- 🧪 **Well Tested** - Comprehensive test coverage
- 📝 **Type Hints** - Full type annotation support

## Installation

### From Source

```bash
git clone https://github.com/Nomoos/PrismQ.IdeaInspiration.Model.git
cd PrismQ.IdeaInspiration.Model
pip install -e .
```

### For Development

```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from prismq.idea.model import IdeaInspiration, ContentType

# Create from text content
idea = IdeaInspiration.from_text(
    title="Introduction to Python",
    description="Learn Python basics",
    text_content="Python is a high-level programming language...",
    keywords=["python", "programming", "tutorial"]
)

# Create from video with subtitles
video_idea = IdeaInspiration.from_video(
    title="Python Tutorial",
    description="Video tutorial",
    subtitle_text="Welcome to this tutorial...",
    keywords=["python", "video", "tutorial"]
)

# Create from audio with transcription
audio_idea = IdeaInspiration.from_audio(
    title="Python Podcast",
    description="Episode 1",
    transcription="Today we discuss Python...",
    keywords=["python", "podcast"]
)
```

## Usage Examples

### Basic Creation

```python
from prismq.idea.model import IdeaInspiration, ContentType

# Manual creation
idea = IdeaInspiration(
    title="My Article",
    description="Article description",
    content="Full article text",
    keywords=["article", "example"],
    source_type=ContentType.TEXT,
    metadata={"author": "John Doe"},
    source_id="article-123",
    source_url="https://example.com/article"
)
```

### Serialization

```python
from prismq.idea.model import IdeaInspiration

# Create an idea
idea = IdeaInspiration.from_text(
    title="Test Article",
    text_content="Article content",
    keywords=["test"]
)

# Convert to dictionary
data = idea.to_dict()
print(data)
# {
#     'title': 'Test Article',
#     'description': '',
#     'content': 'Article content',
#     'keywords': ['test'],
#     'source_type': 'text',
#     'metadata': {},
#     'source_id': None,
#     'source_url': None
# }

# Create from dictionary
restored = IdeaInspiration.from_dict(data)
assert restored.title == idea.title
```

## Data Model

### IdeaInspiration

The core data model with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `title` | `str` | Content title or headline |
| `description` | `str` | Brief description or summary |
| `content` | `str` | Main text content (body, subtitles, or transcription) |
| `keywords` | `List[str]` | List of relevant keywords or tags |
| `source_type` | `ContentType` | Type of content source (TEXT/VIDEO/AUDIO/UNKNOWN) |
| `metadata` | `Dict[str, str]` | Additional source-specific metadata (string key-value pairs for SQLite compatibility) |
| `source_id` | `Optional[str]` | Unique identifier from source platform |
| `source_url` | `Optional[str]` | URL to original content |

### ContentType

Enumeration for content source types:

- `ContentType.TEXT` - Text articles, blog posts, Reddit posts
- `ContentType.VIDEO` - Video content with subtitles/transcriptions
- `ContentType.AUDIO` - Audio content with transcriptions
- `ContentType.UNKNOWN` - Unknown or unspecified source type

## Metadata Examples

The `metadata` field uses `Dict[str, str]` (string key-value pairs) for SQLite/S3DB compatibility. Here are examples for different content types:

### Text Content Metadata

```python
idea = IdeaInspiration.from_text(
    title="Understanding Neural Networks",
    text_content="Neural networks are...",
    metadata={
        "author": "Dr. Sarah Johnson",
        "publish_date": "2025-01-15",
        "word_count": "2500",
        "reading_time_minutes": "12",
        "category": "machine-learning",
        "platform": "medium",
        "language": "en",
    }
)
```

### Video Content Metadata

```python
idea = IdeaInspiration.from_video(
    title="Python Deep Dive",
    subtitle_text="In this video...",
    metadata={
        "channel": "CodeMasters",
        "channel_id": "UC123456",
        "views": "150000",
        "likes": "8500",
        "duration_seconds": "2400",
        "upload_date": "2025-01-10",
        "resolution": "1080p",
        "language": "en",
    }
)
```

### Audio Content Metadata

```python
idea = IdeaInspiration.from_audio(
    title="Tech Talk Podcast #42",
    transcription="Welcome everyone...",
    metadata={
        "host": "Mike Developer",
        "guest": "Jane Engineer",
        "episode_number": "42",
        "season": "3",
        "duration_seconds": "4200",
        "release_date": "2025-01-12",
        "format": "mp3",
        "bitrate": "128kbps",
        "language": "en",
    }
)
```

### SQLite/S3DB Best Practices

- **All values as strings**: Store numeric values as strings, convert when needed
- **Date format**: Use ISO 8601 format (YYYY-MM-DD) for dates
- **Key naming**: Use snake_case for consistency
- **Easy serialization**: Data can be easily serialized to JSON for SQLite TEXT fields

## Factory Methods

### General Purpose

- `IdeaInspiration.from_text()` - Create from text content
- `IdeaInspiration.from_video()` - Create from video with subtitles
- `IdeaInspiration.from_audio()` - Create from audio with transcription

### Serialization

- `IdeaInspiration.to_dict()` - Convert to dictionary
- `IdeaInspiration.from_dict()` - Create from dictionary

## Testing

Run the test suite:

```bash
# Install test dependencies
pip install -e ".[test]"

# Run tests
pytest

# Run with coverage
pytest --cov=prismq --cov-report=html

# Run specific test file
pytest tests/test_idea_inspiration.py -v
```

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/Nomoos/PrismQ.IdeaInspiration.Model.git
cd PrismQ.IdeaInspiration.Model

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

### Code Quality

```bash
# Format code with black
black prismq/ tests/

# Check code style with flake8
flake8 prismq/ tests/

# Type checking with mypy
mypy prismq/
```

## Integration with Other PrismQ Modules

### With Builder Module

The Builder module (PrismQ.IdeaInspiration.Builder) handles platform-specific transformations from various sources (YouTube, Reddit, etc.) into the clean IdeaInspiration model:

```python
from prismq.idea.model import IdeaInspiration
from prismq.idea.builder import YouTubeBuilder, RedditBuilder

# Builder transforms YouTube data into clean model
youtube_builder = YouTubeBuilder()
idea = youtube_builder.build(video_data, transcription)

# Builder transforms Reddit data into clean model  
reddit_builder = RedditBuilder()
idea = reddit_builder.build(post_data)
```

### With Scoring Module

```python
from prismq.idea.model import IdeaInspiration
from prismq.idea.scoring import ScoringEngine

engine = ScoringEngine()
idea = IdeaInspiration.from_text(
    title="My Article",
    text_content="Article content..."
)
score_results = engine.score_idea_inspiration(idea)
```

### With Classification Module

```python
from prismq.idea.model import IdeaInspiration
from prismq.idea.classification import TextClassifier

classifier = TextClassifier()
idea = IdeaInspiration.from_text(
    title="My Story",
    text_content="This is my story..."
)
result = classifier.classify(idea)
```

## Package Structure

```
PrismQ.IdeaInspiration.Model/
├── prismq/
│   └── idea/
│       └── model/
│           ├── __init__.py              # Package exports
│           └── idea_inspiration.py      # Core model
├── tests/
│   ├── __init__.py
│   └── test_idea_inspiration.py         # Comprehensive tests
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml                       # Project configuration
├── requirements.txt                     # Dependencies (none)
└── setup.py                             # Setup configuration
```

## Design Principles

1. **Zero Dependencies** - Pure Python with no external requirements
2. **Type Safe** - Full type hints for IDE support
3. **Extensible** - Easy to add new factory methods for different sources
4. **Serializable** - Convert to/from dictionaries for storage
5. **SQLite Compatible** - Metadata uses string values for database compatibility
6. **Well Documented** - Clear documentation and examples
7. **Well Tested** - Comprehensive test coverage
8. **Single Responsibility** - Each class and method has one clear purpose

## Version History

- **v0.1.0** - Initial release with core IdeaInspiration model

## License

This repository is proprietary software. All Rights Reserved - Copyright (c) 2025 PrismQ

## Related Projects

- **[PrismQ.IdeaInspiration.Scoring](https://github.com/Nomoos/PrismQ.IdeaInspiration.Scoring)** - Scoring engine for content evaluation
- **[PrismQ.IdeaInspiration.Classification](https://github.com/Nomoos/PrismQ.IdeaInspiration.Classification)** - Content classification system
- **PrismQ.IdeaInspiration.Builder** - Builder for creating models from sources
- **PrismQ.IdeaInspiration.Sources** - Content source integrations

## Support

For questions, issues, or feature requests:
1. Open an issue on GitHub
2. Review the documentation
3. Check the test files for usage examples

---

**Part of the PrismQ Ecosystem** - Unified content processing and generation platform