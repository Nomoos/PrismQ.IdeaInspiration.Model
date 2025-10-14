"""IdeaInspiration model for PrismQ content processing.

This module defines the core IdeaInspiration data model used across
PrismQ.IdeaInspiration.Scoring, PrismQ.IdeaInspiration.Classification,
and other PrismQ modules.

The model provides a unified structure for representing content ideas
from various sources (text, video, audio) and includes factory methods
for creating instances from different content types.
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any
from enum import Enum


class ContentType(Enum):
    """Type of content source."""

    TEXT = "text"
    VIDEO = "video"
    AUDIO = "audio"
    UNKNOWN = "unknown"


@dataclass
class IdeaInspiration:
    """Core data model for content ideas across different media types.

    This model represents content ideas that can originate from text articles,
    video content (with subtitles/transcriptions), or audio content (with
    transcriptions). It provides a unified structure for processing and analyzing
    content across the PrismQ ecosystem.

    Attributes:
        title: The title or headline of the content
        description: A brief description or summary
        content: The main text content (body text, subtitles, or transcription)
        keywords: List of relevant keywords or tags
        source_type: Type of content source (text/video/audio)
        metadata: Additional source-specific metadata (string key-value pairs for
                  SQLite compatibility)
        source_id: Optional unique identifier from the source platform
        source_url: Optional URL to the original content
        score: Optional numerical score value for the content
        category: Optional category classification for the content
        score_detail: Audience fit scores showing how well content fits different 
                      audiences (e.g., {'woman': 65, 'man': 30, '10-15': 150, 
                      '15-20': 89, 'us': 65, 'english': 110, 'spanish': 45})
        category_flags: Secondary category tags with strength scores indicating 
                        how strongly content aligns with each category 
                        (e.g., {'Scary': 100, 'Action': 75, 'Drama': 60})

    Example:
        >>> idea = IdeaInspiration(
        ...     title="Introduction to Python",
        ...     description="Learn Python basics",
        ...     content="Python is a high-level programming language...",
        ...     keywords=["python", "programming", "tutorial"],
        ...     source_type=ContentType.TEXT
        ... )
    """

    title: str
    description: str = ""
    content: str = ""
    keywords: List[str] = field(default_factory=list)
    source_type: ContentType = ContentType.UNKNOWN
    metadata: Dict[str, str] = field(default_factory=dict)
    source_id: Optional[str] = None
    source_url: Optional[str] = None
    score: Optional[int] = None
    category: Optional[str] = None
    score_detail: Dict[str, int] = field(default_factory=dict)
    category_flags: Dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert IdeaInspiration to dictionary representation.

        Returns:
            Dictionary containing all fields with ContentType converted to string
        """
        data = asdict(self)
        data["source_type"] = self.source_type.value
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "IdeaInspiration":
        """Create IdeaInspiration from dictionary.

        Args:
            data: Dictionary containing IdeaInspiration fields

        Returns:
            IdeaInspiration instance
        """
        # Handle source_type conversion
        source_type_value = data.get("source_type", "unknown")
        if isinstance(source_type_value, str):
            try:
                source_type = ContentType(source_type_value)
            except ValueError:
                source_type = ContentType.UNKNOWN
        else:
            source_type = source_type_value

        return cls(
            title=data.get("title", ""),
            description=data.get("description", ""),
            content=data.get("content", ""),
            keywords=data.get("keywords", []),
            source_type=source_type,
            metadata=data.get("metadata", {}),
            source_id=data.get("source_id"),
            source_url=data.get("source_url"),
            score=data.get("score"),
            category=data.get("category"),
            score_detail=data.get("score_detail", {}),
            category_flags=data.get("category_flags", {}),
        )

    @classmethod
    def from_text(
        cls,
        title: str,
        description: str = "",
        text_content: str = "",
        keywords: Optional[List[str]] = None,
        metadata: Optional[Dict[str, str]] = None,
        source_id: Optional[str] = None,
        source_url: Optional[str] = None,
        score: Optional[int] = None,
        category: Optional[str] = None,
        score_detail: Optional[Dict[str, int]] = None,
        category_flags: Optional[Dict[str, int]] = None,
    ) -> "IdeaInspiration":
        """Create IdeaInspiration from text content.

        Args:
            title: Article or post title
            description: Brief description or summary
            text_content: Full text content
            keywords: List of keywords or tags
            metadata: Additional metadata (string key-value pairs for SQLite compatibility)
            source_id: Optional source identifier
            source_url: Optional source URL
            score: Optional numerical score value
            category: Optional category classification
            score_detail: Optional audience fit scores (e.g., demographics, age groups, regions)
            category_flags: Optional secondary category tags with strength scores (0-100)

        Returns:
            IdeaInspiration instance with ContentType.TEXT
        """
        return cls(
            title=title,
            description=description,
            content=text_content,
            keywords=keywords or [],
            source_type=ContentType.TEXT,
            metadata=metadata or {},
            source_id=source_id,
            source_url=source_url,
            score=score,
            category=category,
            score_detail=score_detail or {},
            category_flags=category_flags or {},
        )

    @classmethod
    def from_video(
        cls,
        title: str,
        description: str = "",
        subtitle_text: str = "",
        keywords: Optional[List[str]] = None,
        metadata: Optional[Dict[str, str]] = None,
        source_id: Optional[str] = None,
        source_url: Optional[str] = None,
        score: Optional[int] = None,
        category: Optional[str] = None,
        score_detail: Optional[Dict[str, int]] = None,
        category_flags: Optional[Dict[str, int]] = None,
    ) -> "IdeaInspiration":
        """Create IdeaInspiration from video content with subtitles.

        Args:
            title: Video title
            description: Video description
            subtitle_text: Subtitles or transcription text
            keywords: List of keywords or tags
            metadata: Additional video metadata
                      (string key-value pairs, e.g., views="1000", likes="50")
            source_id: Optional video identifier
            source_url: Optional video URL
            score: Optional numerical score value
            category: Optional category classification
            score_detail: Optional audience fit scores (e.g., demographics, age groups, regions)
            category_flags: Optional secondary category tags with strength scores (0-100)

        Returns:
            IdeaInspiration instance with ContentType.VIDEO
        """
        return cls(
            title=title,
            description=description,
            content=subtitle_text,
            keywords=keywords or [],
            source_type=ContentType.VIDEO,
            metadata=metadata or {},
            source_id=source_id,
            source_url=source_url,
            score=score,
            category=category,
            score_detail=score_detail or {},
            category_flags=category_flags or {},
        )

    @classmethod
    def from_audio(
        cls,
        title: str,
        description: str = "",
        transcription: str = "",
        keywords: Optional[List[str]] = None,
        metadata: Optional[Dict[str, str]] = None,
        source_id: Optional[str] = None,
        source_url: Optional[str] = None,
        score: Optional[int] = None,
        category: Optional[str] = None,
        score_detail: Optional[Dict[str, int]] = None,
        category_flags: Optional[Dict[str, int]] = None,
    ) -> "IdeaInspiration":
        """Create IdeaInspiration from audio content with transcription.

        Args:
            title: Audio title or episode name
            description: Audio description
            transcription: Transcribed audio text
            keywords: List of keywords or tags
            metadata: Additional audio metadata
                      (string key-value pairs, e.g., duration="3600", format="mp3")
            source_id: Optional audio identifier
            source_url: Optional audio URL
            score: Optional numerical score value
            category: Optional category classification
            score_detail: Optional audience fit scores (e.g., demographics, age groups, regions)
            category_flags: Optional secondary category tags with strength scores (0-100)

        Returns:
            IdeaInspiration instance with ContentType.AUDIO
        """
        return cls(
            title=title,
            description=description,
            content=transcription,
            keywords=keywords or [],
            source_type=ContentType.AUDIO,
            metadata=metadata or {},
            source_id=source_id,
            source_url=source_url,
            score=score,
            category=category,
            score_detail=score_detail or {},
            category_flags=category_flags or {},
        )

    def __repr__(self) -> str:
        """String representation of IdeaInspiration."""
        return (
            f"IdeaInspiration(title='{self.title[:50]}...', "
            f"source_type={self.source_type.value}, "
            f"keywords={len(self.keywords)} items)"
        )
