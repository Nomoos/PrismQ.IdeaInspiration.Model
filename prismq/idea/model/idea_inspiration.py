"""IdeaInspiration model for PrismQ content processing.

This module defines the core IdeaInspiration data model used across
PrismQ.IdeaInspiration.Scoring, PrismQ.IdeaInspiration.Classification,
and other PrismQ modules.

The model provides a unified structure for representing content ideas
from various sources (text, video, audio) and includes factory methods
for creating instances from different content types.
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional
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
        metadata: Additional source-specific metadata
        source_id: Optional unique identifier from the source platform
        source_url: Optional URL to the original content
    
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
    metadata: Dict[str, Any] = field(default_factory=dict)
    source_id: Optional[str] = None
    source_url: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert IdeaInspiration to dictionary representation.
        
        Returns:
            Dictionary containing all fields with ContentType converted to string
        """
        data = asdict(self)
        data['source_type'] = self.source_type.value
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'IdeaInspiration':
        """Create IdeaInspiration from dictionary.
        
        Args:
            data: Dictionary containing IdeaInspiration fields
            
        Returns:
            IdeaInspiration instance
        """
        # Handle source_type conversion
        source_type_value = data.get('source_type', 'unknown')
        if isinstance(source_type_value, str):
            try:
                source_type = ContentType(source_type_value)
            except ValueError:
                source_type = ContentType.UNKNOWN
        else:
            source_type = source_type_value
        
        return cls(
            title=data.get('title', ''),
            description=data.get('description', ''),
            content=data.get('content', ''),
            keywords=data.get('keywords', []),
            source_type=source_type,
            metadata=data.get('metadata', {}),
            source_id=data.get('source_id'),
            source_url=data.get('source_url')
        )
    
    @classmethod
    def from_text(
        cls,
        title: str,
        description: str = "",
        text_content: str = "",
        keywords: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        source_id: Optional[str] = None,
        source_url: Optional[str] = None
    ) -> 'IdeaInspiration':
        """Create IdeaInspiration from text content.
        
        Args:
            title: Article or post title
            description: Brief description or summary
            text_content: Full text content
            keywords: List of keywords or tags
            metadata: Additional metadata
            source_id: Optional source identifier
            source_url: Optional source URL
            
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
            source_url=source_url
        )
    
    @classmethod
    def from_video(
        cls,
        title: str,
        description: str = "",
        subtitle_text: str = "",
        keywords: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        source_id: Optional[str] = None,
        source_url: Optional[str] = None
    ) -> 'IdeaInspiration':
        """Create IdeaInspiration from video content with subtitles.
        
        Args:
            title: Video title
            description: Video description
            subtitle_text: Subtitles or transcription text
            keywords: List of keywords or tags
            metadata: Additional video metadata (views, likes, etc.)
            source_id: Optional video identifier
            source_url: Optional video URL
            
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
            source_url=source_url
        )
    
    @classmethod
    def from_audio(
        cls,
        title: str,
        description: str = "",
        transcription: str = "",
        keywords: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        source_id: Optional[str] = None,
        source_url: Optional[str] = None
    ) -> 'IdeaInspiration':
        """Create IdeaInspiration from audio content with transcription.
        
        Args:
            title: Audio title or episode name
            description: Audio description
            transcription: Transcribed audio text
            keywords: List of keywords or tags
            metadata: Additional audio metadata
            source_id: Optional audio identifier
            source_url: Optional audio URL
            
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
            source_url=source_url
        )
    
    @classmethod
    def from_youtube_video(
        cls,
        video_data: Dict[str, Any],
        transcription: str = ""
    ) -> 'IdeaInspiration':
        """Create IdeaInspiration from YouTube video data.
        
        This is a convenience method for YouTube API responses.
        
        Args:
            video_data: YouTube API video response dictionary
            transcription: Video transcription or subtitle text
            
        Returns:
            IdeaInspiration instance with ContentType.VIDEO
            
        Example:
            >>> video_data = {
            ...     'id': 'abc123',
            ...     'snippet': {
            ...         'title': 'Video Title',
            ...         'description': 'Video Description',
            ...         'tags': ['tag1', 'tag2']
            ...     },
            ...     'statistics': {
            ...         'viewCount': '1000',
            ...         'likeCount': '50'
            ...     }
            ... }
            >>> idea = IdeaInspiration.from_youtube_video(video_data, "transcription...")
        """
        snippet = video_data.get('snippet', {})
        video_id = video_data.get('id', '')
        
        return cls(
            title=snippet.get('title', ''),
            description=snippet.get('description', ''),
            content=transcription,
            keywords=snippet.get('tags', []),
            source_type=ContentType.VIDEO,
            metadata={
                'platform': 'youtube',
                'channel': snippet.get('channelTitle', ''),
                'statistics': video_data.get('statistics', {}),
                'raw_data': video_data
            },
            source_id=video_id,
            source_url=f"https://youtube.com/watch?v={video_id}" if video_id else None
        )
    
    @classmethod
    def from_reddit_post(
        cls,
        post_data: Dict[str, Any]
    ) -> 'IdeaInspiration':
        """Create IdeaInspiration from Reddit post data.
        
        This is a convenience method for Reddit API responses.
        
        Args:
            post_data: Reddit API post response dictionary
            
        Returns:
            IdeaInspiration instance with ContentType.TEXT
            
        Example:
            >>> post_data = {
            ...     'title': 'AITA for...',
            ...     'selftext': 'Post body text...',
            ...     'id': 'abc123',
            ...     'subreddit': 'AmItheAsshole',
            ...     'score': 1000
            ... }
            >>> idea = IdeaInspiration.from_reddit_post(post_data)
        """
        post_id = post_data.get('id', '')
        subreddit = post_data.get('subreddit', '')
        
        return cls(
            title=post_data.get('title', ''),
            description=post_data.get('selftext', '')[:500],  # First 500 chars as description
            content=post_data.get('selftext', ''),
            keywords=[subreddit] if subreddit else [],
            source_type=ContentType.TEXT,
            metadata={
                'platform': 'reddit',
                'subreddit': subreddit,
                'score': post_data.get('score', 0),
                'num_comments': post_data.get('num_comments', 0),
                'raw_data': post_data
            },
            source_id=post_id,
            source_url=f"https://reddit.com/r/{subreddit}/comments/{post_id}" if post_id and subreddit else None
        )
    
    def __repr__(self) -> str:
        """String representation of IdeaInspiration."""
        return (
            f"IdeaInspiration(title='{self.title[:50]}...', "
            f"source_type={self.source_type.value}, "
            f"keywords={len(self.keywords)} items)"
        )
