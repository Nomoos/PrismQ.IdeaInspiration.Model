"""Tests for IdeaInspiration model."""

import pytest
from prismq.idea.model import IdeaInspiration, ContentType


class TestIdeaInspirationBasic:
    """Test basic IdeaInspiration functionality."""

    def test_create_basic_idea(self):
        """Test creating a basic IdeaInspiration instance."""
        idea = IdeaInspiration(
            title="Test Title",
            description="Test Description",
            content="Test Content",
            keywords=["test", "example"],
        )

        assert idea.title == "Test Title"
        assert idea.description == "Test Description"
        assert idea.content == "Test Content"
        assert idea.keywords == ["test", "example"]
        assert idea.source_type == ContentType.UNKNOWN
        assert idea.metadata == {}
        assert idea.source_id is None
        assert idea.source_url is None

    def test_create_with_defaults(self):
        """Test creating IdeaInspiration with default values."""
        idea = IdeaInspiration(title="Test Title")

        assert idea.title == "Test Title"
        assert idea.description == ""
        assert idea.content == ""
        assert idea.keywords == []
        assert idea.source_type == ContentType.UNKNOWN
        assert idea.metadata == {}

    def test_create_with_all_fields(self):
        """Test creating IdeaInspiration with all fields."""
        metadata = {"key": "value", "count": 42}
        idea = IdeaInspiration(
            title="Test Title",
            description="Test Description",
            content="Test Content",
            keywords=["test", "example"],
            source_type=ContentType.TEXT,
            metadata=metadata,
            source_id="test-id-123",
            source_url="https://example.com/content",
        )

        assert idea.title == "Test Title"
        assert idea.description == "Test Description"
        assert idea.content == "Test Content"
        assert idea.keywords == ["test", "example"]
        assert idea.source_type == ContentType.TEXT
        assert idea.metadata == metadata
        assert idea.source_id == "test-id-123"
        assert idea.source_url == "https://example.com/content"


class TestIdeaInspirationSerialization:
    """Test serialization and deserialization."""

    def test_to_dict(self):
        """Test converting IdeaInspiration to dictionary."""
        idea = IdeaInspiration(
            title="Test Title",
            description="Test Description",
            content="Test Content",
            keywords=["test"],
            source_type=ContentType.TEXT,
            metadata={"key": "value"},
            source_id="test-id",
            source_url="https://example.com",
        )

        data = idea.to_dict()

        assert isinstance(data, dict)
        assert data["title"] == "Test Title"
        assert data["description"] == "Test Description"
        assert data["content"] == "Test Content"
        assert data["keywords"] == ["test"]
        assert data["source_type"] == "text"  # Converted to string
        assert data["metadata"] == {"key": "value"}
        assert data["source_id"] == "test-id"
        assert data["source_url"] == "https://example.com"

    def test_from_dict(self):
        """Test creating IdeaInspiration from dictionary."""
        data = {
            "title": "Test Title",
            "description": "Test Description",
            "content": "Test Content",
            "keywords": ["test"],
            "source_type": "video",
            "metadata": {"key": "value"},
            "source_id": "test-id",
            "source_url": "https://example.com",
        }

        idea = IdeaInspiration.from_dict(data)

        assert idea.title == "Test Title"
        assert idea.description == "Test Description"
        assert idea.content == "Test Content"
        assert idea.keywords == ["test"]
        assert idea.source_type == ContentType.VIDEO
        assert idea.metadata == {"key": "value"}
        assert idea.source_id == "test-id"
        assert idea.source_url == "https://example.com"

    def test_from_dict_with_missing_fields(self):
        """Test creating IdeaInspiration from dictionary with missing fields."""
        data = {"title": "Test Title"}
        idea = IdeaInspiration.from_dict(data)

        assert idea.title == "Test Title"
        assert idea.description == ""
        assert idea.content == ""
        assert idea.keywords == []
        assert idea.source_type == ContentType.UNKNOWN

    def test_from_dict_with_invalid_source_type(self):
        """Test handling invalid source_type in from_dict."""
        data = {"title": "Test Title", "source_type": "invalid_type"}
        idea = IdeaInspiration.from_dict(data)

        assert idea.source_type == ContentType.UNKNOWN

    def test_round_trip_serialization(self):
        """Test converting to dict and back."""
        original = IdeaInspiration(
            title="Test Title",
            description="Test Description",
            content="Test Content",
            keywords=["test", "example"],
            source_type=ContentType.AUDIO,
            metadata={"key": "value"},
            source_id="test-id",
            source_url="https://example.com",
        )

        data = original.to_dict()
        restored = IdeaInspiration.from_dict(data)

        assert restored.title == original.title
        assert restored.description == original.description
        assert restored.content == original.content
        assert restored.keywords == original.keywords
        assert restored.source_type == original.source_type
        assert restored.metadata == original.metadata
        assert restored.source_id == original.source_id
        assert restored.source_url == original.source_url


class TestIdeaInspirationFactoryMethods:
    """Test factory methods for creating IdeaInspiration."""

    def test_from_text(self):
        """Test creating IdeaInspiration from text content."""
        idea = IdeaInspiration.from_text(
            title="Article Title",
            description="Article description",
            text_content="Full article text content",
            keywords=["article", "text"],
            metadata={"author": "John Doe"},
            source_id="article-123",
            source_url="https://example.com/article",
        )

        assert idea.title == "Article Title"
        assert idea.description == "Article description"
        assert idea.content == "Full article text content"
        assert idea.keywords == ["article", "text"]
        assert idea.source_type == ContentType.TEXT
        assert idea.metadata == {"author": "John Doe"}
        assert idea.source_id == "article-123"
        assert idea.source_url == "https://example.com/article"

    def test_from_text_minimal(self):
        """Test creating IdeaInspiration from text with minimal fields."""
        idea = IdeaInspiration.from_text(title="Minimal Article")

        assert idea.title == "Minimal Article"
        assert idea.description == ""
        assert idea.content == ""
        assert idea.keywords == []
        assert idea.source_type == ContentType.TEXT

    def test_from_video(self):
        """Test creating IdeaInspiration from video content."""
        idea = IdeaInspiration.from_video(
            title="Video Title",
            description="Video description",
            subtitle_text="Video subtitles and transcription",
            keywords=["video", "tutorial"],
            metadata={"views": "1000", "likes": "50"},
            source_id="video-123",
            source_url="https://example.com/video",
        )

        assert idea.title == "Video Title"
        assert idea.description == "Video description"
        assert idea.content == "Video subtitles and transcription"
        assert idea.keywords == ["video", "tutorial"]
        assert idea.source_type == ContentType.VIDEO
        assert idea.metadata == {"views": "1000", "likes": "50"}
        assert idea.source_id == "video-123"
        assert idea.source_url == "https://example.com/video"

    def test_from_audio(self):
        """Test creating IdeaInspiration from audio content."""
        idea = IdeaInspiration.from_audio(
            title="Podcast Episode",
            description="Episode description",
            transcription="Full audio transcription",
            keywords=["podcast", "audio"],
            metadata={"duration": "3600", "format": "mp3"},
            source_id="audio-123",
            source_url="https://example.com/podcast",
        )

        assert idea.title == "Podcast Episode"
        assert idea.description == "Episode description"
        assert idea.content == "Full audio transcription"
        assert idea.keywords == ["podcast", "audio"]
        assert idea.source_type == ContentType.AUDIO
        assert idea.metadata == {"duration": "3600", "format": "mp3"}
        assert idea.source_id == "audio-123"
        assert idea.source_url == "https://example.com/podcast"


class TestContentTypeEnum:
    """Test ContentType enumeration."""

    def test_content_type_values(self):
        """Test ContentType enum values."""
        assert ContentType.TEXT.value == "text"
        assert ContentType.VIDEO.value == "video"
        assert ContentType.AUDIO.value == "audio"
        assert ContentType.UNKNOWN.value == "unknown"

    def test_content_type_from_string(self):
        """Test creating ContentType from string value."""
        assert ContentType("text") == ContentType.TEXT
        assert ContentType("video") == ContentType.VIDEO
        assert ContentType("audio") == ContentType.AUDIO
        assert ContentType("unknown") == ContentType.UNKNOWN

    def test_content_type_invalid(self):
        """Test handling invalid ContentType value."""
        with pytest.raises(ValueError):
            ContentType("invalid")


class TestIdeaInspirationRepr:
    """Test string representation."""

    def test_repr_short_title(self):
        """Test __repr__ with short title."""
        idea = IdeaInspiration(title="Short Title", keywords=["test", "example"])

        repr_str = repr(idea)
        assert "Short Title" in repr_str
        assert "unknown" in repr_str
        assert "2 items" in repr_str

    def test_repr_long_title(self):
        """Test __repr__ with long title (truncated)."""
        long_title = "A" * 100
        idea = IdeaInspiration(title=long_title)

        repr_str = repr(idea)
        assert len(repr_str) < len(long_title) + 100  # Truncated
        assert "..." in repr_str


class TestIdeaInspirationSQLiteCompatibility:
    """Test SQLite (S3DB) compatibility with string metadata."""

    def test_metadata_string_values_only(self):
        """Test that metadata only accepts string values for SQLite compatibility."""
        # All metadata values should be strings
        idea = IdeaInspiration.from_text(
            title="Test Article",
            text_content="Content",
            metadata={
                "author": "John Doe",
                "publish_date": "2025-01-15",
                "views": "1000",  # numeric values as strings
                "rating": "4.5",  # float values as strings
                "category": "technology",
            }
        )
        
        # Verify all metadata values are strings
        for key, value in idea.metadata.items():
            assert isinstance(value, str), f"Metadata value for '{key}' should be string, got {type(value)}"
    
    def test_metadata_examples_for_different_sources(self):
        """Test metadata examples for text, video, and audio sources."""
        # Text metadata examples
        text_idea = IdeaInspiration.from_text(
            title="Article Title",
            metadata={
                "author": "Jane Smith",
                "publish_date": "2025-01-15",
                "word_count": "1500",
                "reading_time": "7",
                "platform": "medium",
            }
        )
        assert text_idea.metadata["word_count"] == "1500"
        
        # Video metadata examples
        video_idea = IdeaInspiration.from_video(
            title="Tutorial Video",
            metadata={
                "channel": "TechChannel",
                "views": "50000",
                "likes": "2500",
                "duration": "1800",
                "upload_date": "2025-01-10",
                "resolution": "1080p",
            }
        )
        assert video_idea.metadata["views"] == "50000"
        
        # Audio metadata examples
        audio_idea = IdeaInspiration.from_audio(
            title="Podcast Episode",
            metadata={
                "host": "John Podcast",
                "episode_number": "42",
                "duration": "3600",
                "release_date": "2025-01-12",
                "format": "mp3",
                "bitrate": "128kbps",
            }
        )
        assert audio_idea.metadata["episode_number"] == "42"
    
    def test_sqlite_serialization_round_trip(self):
        """Test that data can be serialized to dict and restored for SQLite storage."""
        import json
        
        original = IdeaInspiration.from_video(
            title="Python Tutorial",
            description="Learn Python basics",
            subtitle_text="Welcome to Python...",
            keywords=["python", "tutorial"],
            metadata={
                "views": "10000",
                "likes": "500",
                "duration": "1200",
            },
            source_id="vid-123",
            source_url="https://example.com/video"
        )
        
        # Convert to dict (simulating SQLite storage)
        data_dict = original.to_dict()
        
        # Serialize to JSON (common for SQLite TEXT fields)
        json_str = json.dumps(data_dict)
        
        # Deserialize from JSON
        restored_dict = json.loads(json_str)
        
        # Restore object
        restored = IdeaInspiration.from_dict(restored_dict)
        
        # Verify restoration
        assert restored.title == original.title
        assert restored.metadata == original.metadata
        assert all(isinstance(v, str) for v in restored.metadata.values())


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
