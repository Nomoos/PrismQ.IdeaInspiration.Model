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

### YouTube Integration

```python
from prismq.idea.model import IdeaInspiration

# From YouTube API response
video_data = {
    'id': 'abc123',
    'snippet': {
        'title': 'Amazing Python Tutorial',
        'description': 'Learn Python in 10 minutes',
        'tags': ['python', 'tutorial', 'programming'],
        'channelTitle': 'Code Academy'
    },
    'statistics': {
        'viewCount': '1000000',
        'likeCount': '50000',
        'commentCount': '1000'
    }
}

transcription = "Welcome to this Python tutorial..."

idea = IdeaInspiration.from_youtube_video(video_data, transcription)

print(f"Title: {idea.title}")
print(f"Channel: {idea.metadata['channel']}")
print(f"Views: {idea.metadata['statistics']['viewCount']}")
print(f"URL: {idea.source_url}")
```

### Reddit Integration

```python
from prismq.idea.model import IdeaInspiration

# From Reddit API response
post_data = {
    'id': 'post123',
    'title': 'AITA for leaving early?',
    'selftext': 'Here is my full story...',
    'subreddit': 'AmItheAsshole',
    'score': 5000,
    'num_comments': 250
}

idea = IdeaInspiration.from_reddit_post(post_data)

print(f"Title: {idea.title}")
print(f"Subreddit: {idea.metadata['subreddit']}")
print(f"Score: {idea.metadata['score']}")
print(f"URL: {idea.source_url}")
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
| `metadata` | `Dict[str, Any]` | Additional source-specific metadata |
| `source_id` | `Optional[str]` | Unique identifier from source platform |
| `source_url` | `Optional[str]` | URL to original content |

### ContentType

Enumeration for content source types:

- `ContentType.TEXT` - Text articles, blog posts, Reddit posts
- `ContentType.VIDEO` - Video content with subtitles/transcriptions
- `ContentType.AUDIO` - Audio content with transcriptions
- `ContentType.UNKNOWN` - Unknown or unspecified source type

## Factory Methods

### General Purpose

- `IdeaInspiration.from_text()` - Create from text content
- `IdeaInspiration.from_video()` - Create from video with subtitles
- `IdeaInspiration.from_audio()` - Create from audio with transcription

### Platform-Specific

- `IdeaInspiration.from_youtube_video()` - Create from YouTube API data
- `IdeaInspiration.from_reddit_post()` - Create from Reddit API data

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

### In Scoring Module

```python
from prismq.idea.model import IdeaInspiration
from prismq.idea.scoring import ScoringEngine

engine = ScoringEngine()
idea = IdeaInspiration.from_youtube_video(video_data, transcription)
score_results = engine.score_idea_inspiration(idea)
```

### In Classification Module

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
5. **Well Documented** - Clear documentation and examples
6. **Well Tested** - Comprehensive test coverage

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