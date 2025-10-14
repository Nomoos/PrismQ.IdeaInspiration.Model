"""PrismQ IdeaInspiration Model package.

This package provides the core IdeaInspiration data model used across
the PrismQ ecosystem for content processing, scoring, and classification.

Main exports:
    - IdeaInspiration: Core data model for content ideas
    - ContentType: Enum for content source types (text/video/audio)

Example:
    >>> from prismq.idea.model import IdeaInspiration, ContentType
    >>>
    >>> # Create from text
    >>> idea = IdeaInspiration.from_text(
    ...     title="My Article",
    ...     description="Article description",
    ...     text_content="Full article text...",
    ...     keywords=["python", "tutorial"]
    ... )
    >>>
    >>> # Create from video
    >>> idea = IdeaInspiration.from_video(
    ...     title="Video Title",
    ...     subtitle_text="Video transcription...",
    ...     keywords=["educational"]
    ... )
"""

from prismq.idea.model.idea_inspiration import IdeaInspiration, ContentType

__version__ = "0.1.0"

__all__ = [
    "IdeaInspiration",
    "ContentType",
]
