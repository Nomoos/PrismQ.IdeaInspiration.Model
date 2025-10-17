"""Demonstration of SQLite/S3DB compatibility.

This script shows how to store and retrieve IdeaInspiration objects
in a SQLite database using the string-based metadata.
"""

import sqlite3
import json
import os
from pathlib import Path
from prismq.idea.model import IdeaInspiration, ContentType


def get_database_path():
    """Get the database path at the PrismQ top level.
    
    Returns the path to the database file at the same level as the PrismQ
    top level directory. This allows multiple PrismQ modules to share the
    same database.
    
    The database location can be overridden using the PRISMQ_DB_PATH
    environment variable.
    
    Repository structure:
        VideoMaking/
          PrismQ/                    <- PrismQ top level directory
            IdeaInspiration/
              Model/                 <- Current repository
                scripts/
          prismq_ideas.db            <- Database location (same level as PrismQ)
    """
    # Check for environment variable override
    env_db_path = os.getenv('PRISMQ_DB_PATH')
    if env_db_path:
        return Path(env_db_path)
    
    # Get the current script's directory
    current_dir = Path(__file__).parent.absolute()
    
    # Go up 3 levels from Model/ to get to the same level as PrismQ/
    # Model/ -> IdeaInspiration/ -> PrismQ/ -> VideoMaking/
    db_dir = current_dir.parent.parent.parent
    
    # Database file at the same level as PrismQ directory
    db_path = db_dir / "prismq_ideas.db"
    
    return db_path


def create_database():
    """Create a SQLite database with ideas table."""
    db_path = get_database_path()
    
    # Ensure the directory exists
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Database location: {db_path}")
    print()
    
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE ideas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            content TEXT,
            keywords TEXT,
            source_type TEXT,
            metadata TEXT,
            source_id TEXT,
            source_url TEXT
        )
    ''')
    
    return conn


def store_idea(conn, idea: IdeaInspiration):
    """Store an IdeaInspiration in the database."""
    cursor = conn.cursor()
    
    # Convert idea to dict
    data = idea.to_dict()
    
    # Store keywords and metadata as JSON strings (common SQLite pattern)
    cursor.execute('''
        INSERT INTO ideas (title, description, content, keywords, source_type, metadata, source_id, source_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['title'],
        data['description'],
        data['content'],
        json.dumps(data['keywords']),
        data['source_type'],
        json.dumps(data['metadata']),
        data['source_id'],
        data['source_url']
    ))
    
    conn.commit()
    return cursor.lastrowid


def retrieve_idea(conn, idea_id: int) -> IdeaInspiration:
    """Retrieve an IdeaInspiration from the database."""
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM ideas WHERE id = ?', (idea_id,))
    row = cursor.fetchone()
    
    if not row:
        raise ValueError(f"No idea found with id {idea_id}")
    
    # Reconstruct the data dictionary
    data = {
        'title': row[1],
        'description': row[2],
        'content': row[3],
        'keywords': json.loads(row[4]),
        'source_type': row[5],
        'metadata': json.loads(row[6]),
        'source_id': row[7],
        'source_url': row[8]
    }
    
    return IdeaInspiration.from_dict(data)


def main():
    """Run the SQLite demonstration."""
    print("=" * 60)
    print("SQLite/S3DB Compatibility Demonstration")
    print("=" * 60)
    print()
    
    # Create database
    conn = create_database()
    print("✓ Created SQLite database")
    
    # Create test ideas with different content types
    ideas = [
        IdeaInspiration.from_text(
            title="Python Best Practices",
            description="A guide to writing clean Python code",
            text_content="Follow PEP 8 style guide...",
            keywords=["python", "best-practices", "coding"],
            metadata={
                "author": "John Developer",
                "publish_date": "2025-01-15",
                "word_count": "1500",
                "category": "programming"
            }
        ),
        IdeaInspiration.from_video(
            title="Machine Learning Tutorial",
            subtitle_text="Welcome to ML basics...",
            keywords=["ml", "tutorial", "ai"],
            metadata={
                "channel": "AI Academy",
                "views": "50000",
                "likes": "2500",
                "duration_seconds": "1800"
            }
        ),
        IdeaInspiration.from_audio(
            title="Tech Podcast Episode 10",
            transcription="Today we discuss...",
            keywords=["podcast", "tech", "interview"],
            metadata={
                "host": "Sarah Tech",
                "episode": "10",
                "duration_seconds": "3600",
                "format": "mp3"
            }
        )
    ]
    
    # Store ideas
    stored_ids = []
    for idea in ideas:
        idea_id = store_idea(conn, idea)
        stored_ids.append(idea_id)
        print(f"✓ Stored: {idea.title} (ID: {idea_id})")
    
    print()
    
    # Retrieve and verify
    print("Retrieving and verifying ideas:")
    for idea_id, original in zip(stored_ids, ideas):
        retrieved = retrieve_idea(conn, idea_id)
        
        # Verify all fields match
        assert retrieved.title == original.title
        assert retrieved.description == original.description
        assert retrieved.content == original.content
        assert retrieved.keywords == original.keywords
        assert retrieved.source_type == original.source_type
        assert retrieved.metadata == original.metadata
        
        print(f"✓ ID {idea_id}: {retrieved.title}")
        print(f"  Type: {retrieved.source_type.value}")
        print(f"  Metadata: {retrieved.metadata}")
        
        # Verify all metadata values are strings
        for key, value in retrieved.metadata.items():
            assert isinstance(value, str), f"Metadata value should be string, got {type(value)}"
        
        print(f"  ✓ All metadata values are strings (SQLite compatible)")
        print()
    
    # Clean up
    conn.close()
    
    print("=" * 60)
    print("✓ SQLite/S3DB compatibility verified successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
