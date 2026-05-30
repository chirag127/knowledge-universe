# Book Files Generator Prompt

> **Location**: `knowledge-universe/prompts/book-files-generator.md`
> **Purpose**: A master prompt to give to an AI assistant to generate all structured files for any book in this Library of Alexandria knowledge system.
> **Usage**: Copy the prompt block below, fill in the book details, and send it to the AI.

---

## How to Use This Prompt

1. Find the exact folder path where the book will live (e.g. `02-non-fiction/01-mind/01-learning/01-learning-science/03-make-it-stick`).
2. Copy the prompt template below.
3. Fill in all the `[VARIABLES]` with the real book information.
4. Send it to the AI and it will create all files in one shot.

> **Important**: The AI must search the web **multiple times** at each stage — not just once. Each file requires its own dedicated web searches for accuracy. See the SEARCH INSTRUCTIONS section inside the prompt template.

---

## Files the AI Will Create for Every Book

Each book folder contains exactly **5 files**:

| File | Purpose |
|---|---|
| `README.md` | Book metadata (title, authors, year, genre) + "Should I read the full book?" verdict + navigation links to all other files |
| `summary.md` | Combined thematic summary — the big picture, core pillars, frameworks, and a quick-reference techniques table |
| `chapter-summary.md` | Chapter-by-chapter breakdown — core question, key concepts, and single takeaway per chapter |
| `notes.md` | Empty structured notes file — all chapter headings pre-filled, content left blank for you to write |
| `concepts.md` | A glossary of all key terms, models, and concepts defined in the book with 1-line definitions |

### Optional 6th File (include only if highly applicable)

| File | Include When |
|---|---|
| `quotes.md` | The book is famous for memorable, standalone quotes worth re-reading (biographies, philosophy, stoicism, mindset books) |

---

## The Prompt Template

Copy everything inside the triple backtick block below:

---

```
You are building a book knowledge file system for a personal Library of Alexandria.
The book folder already exists at:

  [FULL FOLDER PATH]
  Example: 02-non-fiction/01-mind/01-learning/01-learning-science/03-make-it-stick

---

BOOK DETAILS:

- Title: [FULL BOOK TITLE]
- Authors: [AUTHOR NAME(S)]
- Year Published: [YEAR]
- Edition: [e.g. 1st, 2nd, Updated — write "1st" if unknown]
- Genre / Category: [e.g. Learning Science, Cognitive Psychology, Personal Finance, etc.]
- Companion Books (if any): [related books in the same series or by the same author]

---

TASK: Search the web MULTIPLE TIMES to find accurate, detailed information about this book.
You must perform separate web searches for each file you create — do not rely on one search
for everything. Every file must be complete and substantive. No placeholders or stubs.

---

FILE 1: README.md

BEFORE WRITING: Search the web for:
  (a) "[BOOK TITLE] [AUTHOR] overview summary" — to get the authoritative description
  (b) "[BOOK TITLE] who should read" OR "[BOOK TITLE] is it worth reading" — for the reading verdict

Content:
- Book title as H1 heading
- Metadata section: Authors, Published, Edition, Genre
- Description: 2-3 sentences on what the book is about
- "Should You Read the Full Book?" section with a clear verdict:
    * WHO should read every word of the book (ideal reader profile)
    * WHO can rely on the summaries instead (reader who wants the ideas, not the stories)
    * ONE sentence verdict: "Read the full book if [condition]. Use the summaries if [condition]."
- Navigation section with markdown links to all 4 other files in the same folder:
    * summary.md (label: Combined Book Summary)
    * chapter-summary.md (label: Chapter-by-Chapter Summary)
    * notes.md (label: Personal Study Notes)
    * concepts.md (label: Key Concepts Glossary)

---

FILE 2: summary.md

BEFORE WRITING: Search the web for:
  (a) "[BOOK TITLE] key concepts summary" — for thematic pillars
  (b) "[BOOK TITLE] [AUTHOR] main ideas frameworks" — for named frameworks and models
  (c) "[BOOK TITLE] best takeaways" — to verify coverage is comprehensive

Content:
- Title: "# [BOOK TITLE] — Combined Book Summary"
- Metadata block: Authors, Year, Genre, Core Philosophy (1 sentence)
- "The Big Idea in One Paragraph" section
- 5–8 major thematic PILLARS that represent the book's core frameworks.
  For each pillar:
  * H2 heading with pillar name and emoji
  * 3–6 bullet points or sub-sections explaining the concept deeply
  * Where relevant: comparison tables, numbered protocols, metaphors used in the book
- A final "Quick Reference" table summarizing all techniques/strategies vs. the problem they solve
- Write in a dense, analytical style — no fluff. Every sentence must add information.

---

FILE 3: chapter-summary.md

BEFORE WRITING: Search the web for:
  (a) "[BOOK TITLE] table of contents" — to get the EXACT chapter titles (do not invent them)
  (b) "[BOOK TITLE] chapter [N] summary" — search for EACH chapter individually if needed
  (c) "[BOOK TITLE] [AUTHOR] chapter by chapter" — for structured chapter breakdowns
  (d) Cross-reference multiple sources to confirm chapter titles and content are accurate

Content:
- Title: "# [BOOK TITLE] — Chapter-by-Chapter Summary"
- Brief intro note: "Each chapter is summarized with the core question it answers, key concepts, and single most important takeaway."
- For EVERY chapter (search the web to find the exact table of contents):
  * H2 heading: "## Chapter [N]: [EXACT CHAPTER TITLE]"
  * "**Core Question**:" — The specific question this chapter addresses
  * "### What the Chapter Covers" — 3–6 bullet points or paragraphs covering the chapter's substance
  * "### Key Concepts" — Named concepts introduced or deepened in this chapter
  * "### Core Takeaway" — One bold italic sentence (the single most important lesson)
  * A horizontal rule (---) between chapters
- Final section: "## Full Chapter Summary Table" — a markdown table mapping every chapter to its core tool/concept

---

FILE 4: notes.md

Content:
- Title: "# Study Notes: [BOOK TITLE]"
- Introductory paragraph: "This file is reserved for your custom insights, quotes, and lessons that you do not want to forget. The structure below mirrors the exact chapters of the book. Fill in the content under each heading as you progress."
- A horizontal rule
- For EVERY chapter (same list as chapter-summary.md):
  * H2 heading: "## [EXACT CHAPTER TITLE]"
  * Single italic line: "*Add your personal study notes and core insights here...*"
  * A horizontal rule (---)
- Leave NO content under the headings. The user will fill this in themselves.
- DO NOT pre-fill any bullet points, frameworks, or summaries under the chapter headings.

---

FILE 5: concepts.md

BEFORE WRITING: Search the web for:
  (a) "[BOOK TITLE] glossary key terms" — for any official term definitions
  (b) "[BOOK TITLE] [specific named concept]" — search each important concept individually
  (c) "[BOOK TITLE] [AUTHOR] concepts explained" — for thorough concept coverage

Content:
- Title: "# Key Concepts Glossary: [BOOK TITLE]"
- Introductory line: "All key terms, mental models, frameworks, and named concepts introduced in this book — defined in plain language."
- A horizontal rule
- For every named concept, model, law, technique, or term introduced in the book:
  * H3 heading: "### [Concept Name]"
  * "**Definition**:" — 1-2 sentences defining it precisely
  * "**In the Book**:" — 1 sentence explaining how/where the author uses it
  * "**Real-World Application**:" — 1 sentence on how to apply it in practice
- Group concepts by chapter or theme if the book has a large number of them
- Minimum 10 concepts, maximum as many as the book genuinely introduces

---

SEARCH INSTRUCTIONS (MANDATORY — DO NOT SKIP):

You MUST perform ALL of the following web searches before and during file creation.
Do not rely on a single search or on prior knowledge alone. Books change between editions
and popular summaries often contain errors — always verify against multiple sources.

REQUIRED SEARCHES:
1. "[BOOK TITLE] [AUTHOR] table of contents" — for exact chapter titles
2. "[BOOK TITLE] [AUTHOR] chapter by chapter summary" — for chapter content
3. "[BOOK TITLE] [AUTHOR] key concepts" — for named frameworks and terms
4. "[BOOK TITLE] [AUTHOR] main ideas" — for thematic pillars
5. "[BOOK TITLE] who should read it" OR "[BOOK TITLE] is it worth reading" — for README verdict
6. "[BOOK TITLE] [specific chapter N] summary" — for any chapter where content is unclear
7. "[BOOK TITLE] [AUTHOR] criticism" OR "[BOOK TITLE] limitations" — for balanced README verdict
8. "[BOOK TITLE] [AUTHOR] best quotes" — to verify major claims and memorable lines

DO NOT:
- Invent chapter titles — use only verified real titles from web searches
- Use a single search for everything — each file requires its own targeted searches
- Skip the README "Should You Read?" section — it is required in every README

STYLE RULES:
- No placeholders. No "Add content here" in summary.md or chapter-summary.md.
- No filler sentences. Every line must be informative.
- Use markdown tables where comparison adds clarity.
- Use emoji sparingly and only on H2 pillar headings in summary.md.
- notes.md is the ONLY file where content is intentionally left blank under headings.
```

---

## Example Invocation

> "Use the book-files-generator prompt for the following book:
>
> - Folder: `02-non-fiction/01-mind/01-learning/01-learning-science/03-make-it-stick`
> - Title: Make It Stick: The Science of Successful Learning
> - Authors: Peter C. Brown, Henry L. Roediger III, Mark A. McDaniel
> - Year: 2014
> - Genre: Learning Science / Cognitive Psychology"

---

## Naming Conventions for Book Folders

Folder names follow this pattern: `[NN]-[book-title-slug]`

- `NN` = zero-padded 2-digit number (e.g. `01`, `14`)
- slug = lowercase, hyphens instead of spaces, no punctuation
- Examples:
  - `03-make-it-stick`
  - `05-ultralearning`
  - `07-the-cambridge-handbook-of-expertise`
  - `13-the-only-study-guide-youll-ever-need`

---

## Adding the Optional quotes.md File

If the book warrants it (biographies, philosophy, mindset, stoicism, social science), add this to the prompt:

```
OPTIONAL FILE: quotes.md

BEFORE WRITING: Search the web for:
  (a) "[BOOK TITLE] [AUTHOR] best quotes"
  (b) "[BOOK TITLE] memorable passages"

Content:
- Title: "# Memorable Quotes: [BOOK TITLE]"
- Grouped by chapter or theme
- For each quote:
  * The exact quote in a markdown blockquote (> )
  * Attribution: — [Author Name], Chapter [N]
  * 1-sentence explanation of why this quote matters
```

---

## Maintenance Notes

- Run this prompt whenever you add a new book to any subfolder in `02-non-fiction/` or `01-fiction/`.
- Always verify the chapter list online before generating files — chapter titles must be exact.
- After generating all files, update the parent folder's `README.md` to add the new book as a numbered entry in the library index.
- The "Should You Read the Full Book?" section in README.md must be updated if you later discover the book has changed significantly in a newer edition.
