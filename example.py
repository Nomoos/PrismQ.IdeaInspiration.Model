"""Example usage of PrismQ.IdeaInspiration.Model

This script demonstrates how to use the IdeaInspiration model to create,
serialize, and work with content ideas from various sources.
"""

from prismq.idea.model import IdeaInspiration, ContentType


def example_basic_creation():
    """Example 1: Basic creation of IdeaInspiration."""
    print("=" * 60)
    print("Example 1: Basic Creation")
    print("=" * 60)

    idea = IdeaInspiration(
        title="Introduction to Machine Learning",
        description="A comprehensive guide to ML basics",
        content="Machine learning is a subset of artificial intelligence...",
        keywords=["machine learning", "AI", "tutorial"],
        source_type=ContentType.TEXT,
    )

    print(f"Title: {idea.title}")
    print(f"Description: {idea.description}")
    print(f"Content Length: {len(idea.content)} characters")
    print(f"Keywords: {idea.keywords}")
    print(f"Source Type: {idea.source_type.value}")
    print()


def example_from_text():
    """Example 2: Creating from text content."""
    print("=" * 60)
    print("Example 2: Creating from Text")
    print("=" * 60)

    idea = IdeaInspiration.from_text(
        title="The Future of Quantum Computing",
        description="Exploring the potential of quantum computers",
        text_content="Quantum computing represents a paradigm shift...",
        keywords=["quantum", "computing", "technology"],
        metadata={"author": "Dr. Jane Smith", "date": "2025-01-15"},
        source_url="https://example.com/quantum-article",
    )

    print(f"Title: {idea.title}")
    print(f"Author: {idea.metadata.get('author', 'Unknown')}")
    print(f"URL: {idea.source_url}")
    print(f"Keywords: {', '.join(idea.keywords)}")
    print()


def example_from_video():
    """Example 3: Creating from video with subtitles."""
    print("=" * 60)
    print("Example 3: Creating from Video")
    print("=" * 60)

    idea = IdeaInspiration.from_video(
        title="Python Tutorial for Beginners",
        description="Learn Python programming in 30 minutes",
        subtitle_text="Welcome to this Python tutorial. Today we'll cover variables, loops, and functions...",
        keywords=["python", "tutorial", "programming", "beginners"],
        metadata={"views": 500000, "likes": 25000, "duration": 1800},  # seconds
        source_id="video-abc-123",
    )

    print(f"Title: {idea.title}")
    print(f"Views: {idea.metadata['views']:,}")
    print(f"Likes: {idea.metadata['likes']:,}")
    print(f"Duration: {idea.metadata['duration'] // 60} minutes")
    print(f"Content Preview: {idea.content[:100]}...")
    print()


def example_serialization():
    """Example 4: Serialization and deserialization."""
    print("=" * 60)
    print("Example 4: Serialization")
    print("=" * 60)

    # Create an idea
    original = IdeaInspiration.from_text(
        title="Blockchain Technology Explained",
        description="Understanding blockchain and its applications",
        text_content="Blockchain is a distributed ledger technology...",
        keywords=["blockchain", "cryptocurrency", "technology"],
    )

    # Serialize to dictionary
    data = original.to_dict()
    print("Serialized to dictionary:")
    for key, value in data.items():
        if isinstance(value, str) and len(value) > 50:
            print(f"  {key}: {value[:50]}...")
        elif isinstance(value, list) and value:
            print(f"  {key}: {value}")
        elif value:
            print(f"  {key}: {value}")

    # Deserialize back
    restored = IdeaInspiration.from_dict(data)
    print(f"\nDeserialized successfully!")
    print(f"Titles match: {original.title == restored.title}")
    print(f"Content matches: {original.content == restored.content}")
    print(f"Keywords match: {original.keywords == restored.keywords}")
    print()


def example_from_audio():
    """Example 5: Creating from audio with transcription."""
    print("=" * 60)
    print("Example 5: Creating from Audio")
    print("=" * 60)

    idea = IdeaInspiration.from_audio(
        title="PrismQ Podcast - Episode 15: AI in 2025",
        description="Discussion about the current state of AI",
        transcription="Welcome to the PrismQ Podcast. Today we're discussing artificial intelligence in 2025...",
        keywords=["podcast", "AI", "technology", "2025"],
        metadata={"duration": 3600, "host": "John Doe", "guest": "Dr. Jane Smith", "episode": 15},
        source_id="podcast-ep15",
    )

    print(f"Title: {idea.title}")
    print(f"Episode: {idea.metadata['episode']}")
    print(f"Host: {idea.metadata['host']}")
    print(f"Guest: {idea.metadata['guest']}")
    print(f"Duration: {idea.metadata['duration'] // 60} minutes")
    print(f"Transcription Preview: {idea.content[:100]}...")
    print()


def example_content_types():
    """Example 6: Working with different content types."""
    print("=" * 60)
    print("Example 6: Content Type Comparison")
    print("=" * 60)

    text_idea = IdeaInspiration.from_text(title="Text Article", text_content="Article content...")

    video_idea = IdeaInspiration.from_video(
        title="Video Tutorial", subtitle_text="Video subtitles..."
    )

    audio_idea = IdeaInspiration.from_audio(
        title="Podcast Episode", transcription="Audio transcription..."
    )

    ideas = [text_idea, video_idea, audio_idea]

    print("Content Type Summary:")
    for idea in ideas:
        print(f"  {idea.title:20} -> {idea.source_type.value:8}")

    print(f"\nAvailable ContentType values:")
    for content_type in ContentType:
        print(f"  - {content_type.value}")
    print()


def main():
    """Run all examples."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  PrismQ.IdeaInspiration.Model - Usage Examples".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    print("\n")

    example_basic_creation()
    example_from_text()
    example_from_video()
    example_serialization()
    example_from_audio()
    example_content_types()

    print("=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
