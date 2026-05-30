#!/usr/bin/env python3
import os
import shutil

# Modular structure representing the Library of Alexandria
LIBRARY_STRUCTURE = {
    "fiction": {
        "classics": [
            "western",
            "russian",
            "indian",
            "japanese",
            "chinese",
        ],
        "fantasy": [
            "epic-fantasy",
            "dark-fantasy",
            "urban-fantasy",
            "progression-fantasy",
        ],
        "science-fiction": [
            "hard-scifi",
            "space-opera",
            "cyberpunk",
            "dystopian",
            "post-apocalyptic",
        ],
        "historical-fiction": [
            "ancient",
            "medieval",
            "modern",
            "war",
        ],
        "mystery-thriller": [
            "detective",
            "crime",
            "psychological",
            "espionage",
        ],
        "philosophical-fiction": [
            "existentialism",
            "political",
            "social",
            "spiritual",
        ],
    },
    "non-fiction": {
        "mind": {
            "learning": [
                "learning-science",
                "memory",
                "reading",
                "note-taking",
                "deliberate-practice",
                "productivity",
            ],
            "thinking": [
                "critical-thinking",
                "systems-thinking",
                "mental-models",
                "decision-making",
                "problem-solving",
            ],
            "psychology": [
                "cognitive-biases",
                "habits",
                "motivation",
                "emotional-intelligence",
                "behavioral-psychology",
            ],
            "communication": [
                "speaking",
                "writing",
                "storytelling",
                "negotiation",
                "persuasion",
            ],
            "philosophy": [
                "stoicism",
                "ethics",
                "logic",
                "epistemology",
                "eastern-philosophy",
            ],
        },
        "wealth": {
            "personal-finance": [
                "budgeting",
                "saving",
                "insurance",
                "retirement",
            ],
            "investing": [
                "index-funds",
                "stocks",
                "value-investing",
                "growth-investing",
                "reits",
                "asset-allocation",
            ],
            "economics": [
                "microeconomics",
                "macroeconomics",
                "economic-history",
                "monetary-systems",
            ],
            "real-estate": [
                "residential",
                "commercial",
                "reits",
            ],
            "taxation": [
                "personal-tax",
                "business-tax",
            ],
        },
        "business": {
            "entrepreneurship": [
                "startups",
                "bootstrapping",
                "solopreneurship",
                "venture-capital",
            ],
            "business-models": [
                "saas",
                "agencies",
                "marketplaces",
                "ecommerce",
                "consulting",
            ],
            "sales": [
                "b2b",
                "enterprise-sales",
                "closing",
                "prospecting",
            ],
            "marketing": [
                "branding",
                "content-marketing",
                "seo",
                "digital-marketing",
                "copywriting",
            ],
            "leadership": [
                "management",
                "hiring",
                "delegation",
                "strategy",
            ],
            "side-income": [
                "dropshipping",
                "print-on-demand",
                "affiliate-marketing",
                "self-publishing",
                "digital-products",
                "freelancing-gig-economy",
            ],
        },
        "technology": {
            "computer-science": [
                "algorithms",
                "data-structures",
                "operating-systems",
                "networking",
                "databases",
            ],
            "software-engineering": [
                "clean-code",
                "architecture",
                "testing",
                "design-patterns",
                "refactoring",
            ],
            "programming": [
                "python",
                "javascript",
                "typescript",
                "go",
                "rust",
            ],
            "backend": [
                "apis",
                "fastapi",
                "authentication",
                "scalability",
                "microservices",
            ],
            "cloud": [
                "linux",
                "docker",
                "aws",
                "terraform",
                "kubernetes",
            ],
            "distributed-systems": [
                "redis",
                "kafka",
                "event-driven",
                "consistency",
                "consensus",
            ],
            "artificial-intelligence": [
                "machine-learning",
                "deep-learning",
                "llms",
                "rag",
                "agents",
                "ai-engineering",
            ],
        },
        "society": {
            "history": [
                "ancient",
                "medieval",
                "modern",
                "technology-history",
            ],
            "politics": [
                "democracy",
                "geopolitics",
                "public-policy",
            ],
            "law": [
                "contracts",
                "business-law",
                "intellectual-property",
            ],
            "religion": [
                "hinduism",
                "buddhism",
                "christianity",
                "islam",
                "comparative-religion",
            ],
        },
        "life": {
            "health": [
                "nutrition",
                "exercise",
                "sleep",
                "longevity",
            ],
            "relationships": [
                "dating",
                "marriage",
                "family",
                "friendships",
            ],
            "career": [
                "interviews",
                "resumes",
                "networking",
                "personal-branding",
                "skilled-trades",
                "modern-agriculture",
                "alternative-careers",
            ],
        },
    },
}

def generate_numbered_paths(data, current_prefix=""):
    """
    Recursively generates structured paths with double-digit zero-padded
    prefixes to preserve ordering in file explorers.
    """
    paths = []
    if isinstance(data, dict):
        for i, (key, value) in enumerate(data.items(), 1):
            numbered_key = f"{i:02d}-{key}"
            new_prefix = (
                os.path.join(current_prefix, numbered_key)
                if current_prefix
                else numbered_key
            )
            subpaths = generate_numbered_paths(value, new_prefix)
            if subpaths:
                paths.extend(subpaths)
            else:
                paths.append(new_prefix)
    elif isinstance(data, list):
        for i, item in enumerate(data, 1):
            numbered_item = f"{i:02d}-{item}"
            path = os.path.join(current_prefix, numbered_item)
            paths.append(path)
    elif isinstance(data, str):
        path = os.path.join(current_prefix, f"01-{data}")
        paths.append(path)
    return paths

def safe_remove_directory(path):
    """
    Removes a directory only if it is completely empty or contains
    only empty subdirectories (no actual user files).
    """
    if os.path.exists(path):
        has_files = False
        for _, _, files in os.walk(path):
            if files:
                has_files = True
                break
        if not has_files:
            try:
                shutil.rmtree(path)
                print(f"Removed old unnumbered directory: {path}")
            except Exception as e:
                print(f"Could not remove old directory {path}: {e}")
        else:
            print(f"Note: '{path}' contains files, keeping it to avoid data loss.")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Initializing Library of Alexandria structure in: {base_dir}")

    # Generate the structured numbered paths
    numbered_paths = generate_numbered_paths(LIBRARY_STRUCTURE)

    # 1. Create all new structured numbered directories
    created_count = 0
    for path in numbered_paths:
        full_path = os.path.join(base_dir, path)
        if not os.path.exists(full_path):
            os.makedirs(full_path, exist_ok=True)
            created_count += 1

    print(f"Created {created_count} subfolders matching the numbered hierarchy.")

    # 2. Clean up old unnumbered folders (only if safe)
    old_folders = ["fiction", "non-fiction"]
    for folder in old_folders:
        old_path = os.path.join(base_dir, folder)
        safe_remove_directory(old_path)

    print("\nInitialization Complete! Your knowledge repository is structured.")

if __name__ == "__main__":
    main()
