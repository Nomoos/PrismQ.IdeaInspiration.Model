"""Demonstration of scoring and category fields in IdeaInspiration.

This script demonstrates how to use the new scoring and category features
added to the IdeaInspiration model for content evaluation and classification.
"""

from prismq.idea.model import IdeaInspiration


def main():
    """Demonstrate scoring and category functionality."""
    print("=" * 70)
    print("PrismQ IdeaInspiration - Scoring and Category Features Demo")
    print("=" * 70)
    print()

    # Example 1: Basic scoring
    print("Example 1: Basic Content with Score")
    print("-" * 70)
    idea1 = IdeaInspiration.from_text(
        title="Introduction to Machine Learning",
        text_content="Machine learning is revolutionizing technology...",
        keywords=["ML", "AI", "technology"],
        score=85,
        category="technology",
    )
    print(f"Title: {idea1.title}")
    print(f"Score: {idea1.score}")
    print(f"Category: {idea1.category}")
    print()

    # Example 2: Score detail with market multipliers
    print("Example 2: Score Detail - Market Performance Multipliers")
    print("-" * 70)
    idea2 = IdeaInspiration.from_video(
        title="Tech Startup Success Stories",
        subtitle_text="Learn from successful entrepreneurs...",
        keywords=["startup", "business", "entrepreneur"],
        score=90,
        category="business",
        score_detail={
            "US": 250,  # 250% vs industry standard in US market
            "Europe": 180,  # 180% vs industry standard in Europe
            "Asia": 220,  # 220% vs industry standard in Asia
            "woman": 150,  # 150% performance for women demographic
            "man": 140,  # 140% performance for men demographic
        },
    )
    print(f"Title: {idea2.title}")
    print(f"Overall Score: {idea2.score}")
    print("Market Performance Multipliers:")
    for market, multiplier in idea2.score_detail.items():
        print(f"  {market}: {multiplier}% vs standard")
    print()

    # Example 3: Category flags with flavor strength
    print("Example 3: Category Flags - Content Flavor Strength")
    print("-" * 70)
    idea3 = IdeaInspiration.from_audio(
        title="Healthcare Innovation Podcast",
        transcription="Today we discuss breakthrough healthcare technologies...",
        keywords=["healthcare", "innovation", "technology"],
        score=88,
        category="healthcare",
        category_flags={
            "innovation": 95,  # Very strong innovation flavor
            "technology": 88,  # Strong technology flavor
            "healthcare": 92,  # Very strong healthcare flavor
            "education": 70,  # Moderate educational flavor
            "research": 85,  # Strong research flavor
        },
    )
    print(f"Title: {idea3.title}")
    print(f"Category: {idea3.category}")
    print("Content Flavor Strengths (0-100 scale):")
    for flavor, strength in idea3.category_flags.items():
        bar = "█" * (strength // 5)  # Visual bar representation
        print(f"  {flavor:15s}: {strength:3d}/100 {bar}")
    print()

    # Example 4: Comprehensive scoring example
    print("Example 4: Comprehensive Scoring Example")
    print("-" * 70)
    idea4 = IdeaInspiration(
        title="AI-Powered Climate Solutions",
        description="Using artificial intelligence to combat climate change",
        content="Artificial intelligence and machine learning are being deployed...",
        keywords=["AI", "climate", "sustainability", "innovation"],
        score=92,
        category="sustainability",
        score_detail={
            "US": 280,  # Exceptional US market performance
            "tech_industry": 300,  # Outstanding in tech sector
            "woman": 165,  # Strong appeal to women
            "millennial": 220,  # Strong millennial engagement
        },
        category_flags={
            "innovation": 98,  # Extremely innovative
            "sustainability": 95,  # Very strong sustainability focus
            "technology": 90,  # Strong tech component
            "impact": 88,  # Strong social impact
            "education": 75,  # Good educational value
        },
    )
    print(f"Title: {idea4.title}")
    print(f"Description: {idea4.description}")
    print(f"Overall Score: {idea4.score}/100")
    print()
    print("Performance Multipliers:")
    for segment, multiplier in sorted(idea4.score_detail.items(), key=lambda x: x[1], reverse=True):
        print(f"  {segment:20s}: {multiplier}%")
    print()
    print("Content Flavors:")
    for flavor, strength in sorted(idea4.category_flags.items(), key=lambda x: x[1], reverse=True):
        print(f"  {flavor:20s}: {strength}/100")
    print()

    # Example 5: Serialization with scoring fields
    print("Example 5: Serialization with Scoring Fields")
    print("-" * 70)
    data = idea4.to_dict()
    print("Serialized to dictionary:")
    print(f"  Score: {data['score']}")
    print(f"  Category: {data['category']}")
    print(f"  Score Detail Keys: {list(data['score_detail'].keys())}")
    print(f"  Category Flags Keys: {list(data['category_flags'].keys())}")
    print()

    # Restore from dictionary
    restored = IdeaInspiration.from_dict(data)
    print("Successfully restored from dictionary:")
    print(f"  Score matches: {restored.score == idea4.score}")
    print(f"  Category matches: {restored.category == idea4.category}")
    print(f"  Score detail matches: {restored.score_detail == idea4.score_detail}")
    print(f"  Category flags match: {restored.category_flags == idea4.category_flags}")
    print()

    print("=" * 70)
    print("Demo Complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
