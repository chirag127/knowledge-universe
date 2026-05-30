02-non-fiction\01-mind\01-learning\01-learning-science\03-make-it-stick
02-non-fiction\01-mind\01-learning\01-learning-science\04-peak
02-non-fiction\01-mind\01-learning\01-learning-science\05-ultralearning
02-non-fiction\01-mind\01-learning\01-learning-science\06-the-art-of-learning
02-non-fiction\01-mind\01-learning\01-learning-science\07-the-cambridge-handbook-of-expertise
02-non-fiction\01-mind\01-learning\01-learning-science\08-how-we-learn
02-non-fiction\01-mind\01-learning\01-learning-science\09-why-dont-students-like-school
02-non-fiction\01-mind\01-learning\01-learning-science\10-powerful-teaching
02-non-fiction\01-mind\01-learning\01-learning-science\11-small-teaching
02-non-fiction\01-mind\01-learning\01-learning-science\12-understanding-how-we-learn
02-non-fiction\01-mind\01-learning\01-learning-science\13-the-only-study-guide-youll-ever-need
02-non-fiction\01-mind\01-learning\01-learning-science\14-beginner-to-expert
02-non-fiction\01-mind\01-learning\01-learning-science\15-learning-and-memory# Book Files Generator Prompt

> **Location**: `knowledge-universe/prompts/book-files-generator.md`
> **Purpose**: A master prompt to give to an AI assistant to
> generate all structured files for any book in this Library
> of Alexandria knowledge system.
> **Usage**: Copy the prompt block below, fill in the book
> details, and send it to the AI.

---

## How to Use This Prompt

1. Find the exact folder path where the book will live
   (e.g. `02-non-fiction/01-mind/01-learning/01-learning-science/03-make-it-stick`).
2. Copy the prompt template below.
3. Fill in all the `[VARIABLES]` with the real book
   information.
4. Send it to the AI and it will create the three files.

> **CRITICAL**: The AI **MUST** search the web **MULTIPLE
> TIMES** for **EVERY SINGLE BOOK**. Each file requires its
> own dedicated set of web searches. **NEVER** rely on a
> single search, cached results, or prior knowledge alone.
> Books change between editions and popular summaries often
> contain errors — always verify against multiple sources.
>
> **EVEN WHEN PROCESSING MULTIPLE BOOKS AT ONCE**, the AI
> must perform the **FULL SET OF WEB SEARCHES** for each
> book independently. Do **NOT** reduce, skip, or shorten
> research for any book just because you are creating files
> for several books in a batch. Each book deserves the same
> thorough, dedicated research as if it were the only book
> being processed.

---

## Files the AI Will Create for Every Book

Each book folder contains exactly **3 files**:

| File | Purpose |
|---|---|
| `summary.md` | **Consolidated Book Summary** — Metadata, reading verdict (should I read only this summary, the chapter summary, or the full book?), the big idea, thematic pillars, quick-reference techniques table, and a complete key concepts glossary. This is a self-contained reference that tells you everything about the book at a high level. |
| `chapter-summary.md` | **Chapter-by-Chapter Summary** — Detailed breakdown of every chapter with proper `## Chapter N: [Title]` headings, the core question each chapter answers, what it covers, key concepts, and a single-sentence takeaway. Must use exact, verified chapter titles from the latest edition. |
| `notes.md` | **Personal Study Notes Template** — A clean markdown file containing only the document header and the exact chapter headings (`## Chapter N: [Title]`) ready for the user to write their own personal study notes and observations. |

---

## The Prompt Template

Copy everything inside the triple backtick block below:

---

```
You are building a book knowledge file system for a
personal Library of Alexandria.

The book folder already exists at:

  [FULL FOLDER PATH]
  Example: 02-non-fiction/01-mind/01-learning/
  01-learning-science/03-make-it-stick

---

BOOK DETAILS:

- Title: [FULL BOOK TITLE]
- Authors: [AUTHOR NAME(S)]
- Year Published: [YEAR]
- Edition: [e.g. 1st, 2nd, Updated — write "1st" if
  unknown]
- Genre / Category: [e.g. Learning Science, Cognitive
  Psychology, Personal Finance, etc.]
- Companion Books (if any): [related books in the same
  series or by the same author]

---

TASK: You MUST search the web MULTIPLE TIMES to find
accurate, detailed, and COMPLETE information about this
book. You must perform SEPARATE, DEDICATED web searches
for EACH of the three files you create. Do NOT rely on a
single search or on prior knowledge alone.

IMPORTANT: Even if you are creating files for MULTIPLE
BOOKS at once, you MUST perform the FULL NUMBER of web
searches for EVERY SINGLE BOOK. Do NOT reduce research
effort just because you are batching. Each book gets its
own complete, independent research cycle.

---

LATEST EDITION VERIFICATION (MANDATORY):

Before writing ANYTHING, you MUST search the web to find
the LATEST EDITION of this book. Search for:
  (a) "[BOOK TITLE] latest edition [YEAR]"
  (b) "[BOOK TITLE] [AUTHOR] editions"

Use the chapter list from the LATEST EDITION. If the
latest edition has different chapters than older editions,
use the latest. Always note which edition you are using
in the metadata.

---

FILE 1: summary.md

BEFORE WRITING: Search the web MULTIPLE TIMES. You need
at least 5-6 separate searches for this file alone:
  (a) "[BOOK TITLE] [AUTHOR] overview summary" — for the
      authoritative description and big idea
  (b) "[BOOK TITLE] who should read" OR "[BOOK TITLE] is
      it worth reading" — for the reading verdict
  (c) "[BOOK TITLE] key concepts summary" — for thematic
      pillars
  (d) "[BOOK TITLE] [AUTHOR] main ideas frameworks" —
      for named frameworks and models
  (e) "[BOOK TITLE] best takeaways" — to verify coverage
      is comprehensive
  (f) "[BOOK TITLE] glossary key terms" — for concept
      definitions
  (g) "[BOOK TITLE] [AUTHOR] criticism" OR
      "[BOOK TITLE] limitations" — for a balanced verdict

Content (all sections are MANDATORY):

# [BOOK TITLE] — Consolidated Book Summary

## 📖 Book Metadata
- **Title**: [FULL TITLE]
- **Authors**: [AUTHOR NAME(S)]
- **Year Published**: [YEAR]
- **Edition**: [EDITION — always use the LATEST edition]
- **Genre/Category**: [GENRE]
- **Core Philosophy**: One sentence summarizing the
  book's central premise.

---

## 🧭 Reading Verdict: How Should You Approach This Book?

This section MUST clearly answer THREE questions:

1. **Is this summary sufficient?**
   Can you get enough value from just reading this
   `summary.md` file, or do you need more?

2. **Should you read the chapter summary?**
   Does the `chapter-summary.md` file provide enough
   additional depth that you should also read it? Or is
   this summary enough on its own?

3. **Should you read the full book?**
   Is the full book worth reading cover-to-cover, or
   can you rely on the summaries?

Provide a structured answer:

- **Who MUST read the full book**: [Describe the ideal
  reader who needs every page — their goals, background,
  and what they'll miss from summaries alone.]
- **Who should read the chapter summary**: [Describe who
  benefits from the chapter-by-chapter breakdown but
  doesn't need to read the full prose.]
- **Who can rely on this summary alone**: [Describe who
  gets enough value from just this file.]
- **One-Sentence Verdict**: "Read the full book if
  [condition]. Read the chapter summary if [condition].
  This summary is enough if [condition]."

---

## 💡 The Big Idea in One Paragraph

A rich, 4-6 sentence paragraph capturing the book's
fundamental thesis and its contribution to the field.
This must be dense and analytical — no filler.

---

## 🔑 Thematic Pillars & Core Frameworks

Detail 5–8 major thematic pillars or conceptual
frameworks that represent the book's core ideas.

For each pillar:
- H3 heading: "### [Emoji] [Pillar Name]"
- 3–6 bullet points explaining the concept deeply
- Where relevant: comparison tables, numbered protocols,
  or metaphors used in the book

---

## 📋 Quick Reference Techniques Table

A markdown table listing ALL actionable techniques,
strategies, or models introduced in the book:

| Technique / Strategy | Problem It Solves | How to Apply It |
|---|---|---|

---

## 🧠 Key Concepts Glossary

All key terms, mental models, frameworks, and named
concepts introduced in this book — defined in plain
language.

For every named concept, model, law, technique, or term:

### [Concept Name]
- **Definition**: 1-2 sentences defining it precisely.
- **In the Book**: 1 sentence explaining how/where the
  author uses it.
- **Real-World Application**: 1 sentence on how to apply
  it in practice.

Group concepts by chapter or theme if the book has a
large number of them. Minimum 10 concepts, maximum as
many as the book genuinely introduces.

---

STYLE RULES FOR summary.md:
- No placeholders. Every section must be fully written.
- No filler sentences. Every line must be informative.
- Use markdown tables where comparison adds clarity.
- Use emoji sparingly and only on H2 section headings.
- Write in a dense, analytical style — no fluff.

---

FILE 2: chapter-summary.md

BEFORE WRITING: Search the web MULTIPLE TIMES. You need
at least 4-5 separate searches for this file alone:
  (a) "[BOOK TITLE] table of contents" — for the EXACT
      chapter titles (do NOT invent them)
  (b) "[BOOK TITLE] chapter [N] summary" — search for
      EACH chapter individually if needed
  (c) "[BOOK TITLE] [AUTHOR] chapter by chapter" — for
      structured chapter breakdowns
  (d) "[BOOK TITLE] [AUTHOR] table of contents [LATEST
      EDITION YEAR]" — to verify you have the latest
      edition chapters
  (e) Cross-reference MULTIPLE sources to confirm chapter
      titles and content are accurate

Content:

# [BOOK TITLE] — Chapter-by-Chapter Summary

> Each chapter is summarized with: the core question it
> answers, what the chapter covers, key concepts, and
> the single most important takeaway.

---

For EVERY chapter (including Introduction, Preface,
Appendix, Conclusion, or Epilogue if they exist):

## Chapter [N]: [EXACT CHAPTER TITLE]

**Core Question**: *The specific question this chapter
addresses*

### What the Chapter Covers
- 3–6 bullet points or paragraphs covering the chapter's
  substance in detail

### Key Concepts
- Named concepts introduced or deepened in this chapter

### Core Takeaway
> *One bold italic sentence — the single most important
> lesson from this chapter*

--- (horizontal rule between chapters)

After all chapters, include a final summary table:

## Full Chapter Summary Table

| Chapter | Title | Core Tool / Concept |
|---|---|---|

---

HEADING RULES FOR chapter-summary.md:
- Every chapter MUST have an H2 heading in the format:
  "## Chapter [N]: [EXACT CHAPTER TITLE]"
- Chapter titles MUST be the EXACT titles from the book's
  table of contents. Do NOT rename, shorten, paraphrase,
  or invent chapter titles.
- For Introduction, Preface, Conclusion, Epilogue, or
  Appendix sections, use: "## Introduction: [Title]",
  "## Conclusion: [Title]", etc.
- Use horizontal rules (---) to separate each chapter.

---

FILE 3: notes.md

BEFORE WRITING: Use the exact table of contents chapter list verified in FILE 2.

Content:

# Study Notes: [BOOK TITLE]

This file is reserved for your custom insights, quotes, and lessons that you do not want to forget. The structure below mirrors the exact chapters of the book. Fill in the content under each heading as you progress.

---

For EVERY chapter (including Introduction, Preface, Appendix, Conclusion, or Epilogue if they exist):

## Chapter [N]: [EXACT CHAPTER TITLE]

-

--- (horizontal rule between chapters)

---

SEARCH INSTRUCTIONS (MANDATORY — DO NOT SKIP):

You MUST perform ALL of the following web searches BEFORE
and DURING file creation. Do NOT rely on a single search
or on prior knowledge alone. Books change between editions
and popular summaries often contain errors — always verify
against multiple sources.

REQUIRED SEARCHES (minimum — do MORE if needed):
1. "[BOOK TITLE] [AUTHOR] latest edition" — to verify
   which edition to use
2. "[BOOK TITLE] [AUTHOR] table of contents" — for exact
   chapter titles from the latest edition
3. "[BOOK TITLE] [AUTHOR] chapter by chapter summary" —
   for chapter content
4. "[BOOK TITLE] [AUTHOR] key concepts" — for named
   frameworks and terms
5. "[BOOK TITLE] [AUTHOR] main ideas" — for thematic
   pillars
6. "[BOOK TITLE] who should read it" OR "[BOOK TITLE] is
   it worth reading" — for the reading verdict
7. "[BOOK TITLE] [specific chapter N] summary" — for any
   chapter where content is unclear
8. "[BOOK TITLE] [AUTHOR] criticism" OR "[BOOK TITLE]
   limitations" — for a balanced reading verdict
9. "[BOOK TITLE] [AUTHOR] best quotes" — to verify major
   claims and memorable lines
10. "[BOOK TITLE] glossary key terms definitions" — for
    the concepts glossary

DO NOT:
- Invent chapter titles — use ONLY verified real titles
  from web searches
- Use a single search for everything — each file requires
  its own targeted, dedicated searches
- Skip the "Reading Verdict" section — it is required in
  every summary.md
- Reduce research effort when processing multiple books
  — EVERY book gets the FULL set of web searches

CRITICAL BATCH PROCESSING RULE:
When the user asks you to create files for MULTIPLE BOOKS
at once, you MUST:
- Perform the COMPLETE set of web searches for EACH book
  independently
- Do NOT reuse search results across different books
- Do NOT reduce the number of searches per book
- Treat each book as if it were the ONLY book being
  processed
- Each book MUST receive AT LEAST 8-10 web searches
  total across the three files
```

---

## Naming Conventions for Book Folders

Folder names follow this pattern: `[NN]-[book-title-slug]`

- `NN` = zero-padded 2-digit number (e.g. `01`, `14`)
- slug = lowercase, hyphens instead of spaces, no
  punctuation
- Examples:
  - `03-make-it-stick`
  - `05-ultralearning`
  - `07-the-cambridge-handbook-of-expertise`
  - `13-the-only-study-guide-youll-ever-need`

---

## Maintenance Notes

- Run this prompt whenever you add a new book to any
  subfolder in `02-non-fiction/` or `01-fiction/`.
- Always verify the chapter list online before generating
  files — chapter titles must be exact.
- After generating all files, update the parent folder's
  `README.md` to add the new book as a numbered entry in
  the library index.
- The "Reading Verdict" section in summary.md must be
  updated if you later discover the book has changed
  significantly in a newer edition.
Make the all three files for all of these The books that I have pasted About of web searching for each of the book. Do at least twenty web searches for each of the book Book will only have the three files, other files have to be deleted.Continue but search properly everything search the chapter list chapter summary. Individually chess. The summary of the complete book Also, if I should read the book or not. Redo this for the books from Booker. 3 to Book 15.b Search the web for the chapter summaries individually Use web search tool Individually, for everything Listed below Searching the summary of the book Searching the table of content. Searching the chapter summary is individually Searching the Book summary Searching if the book is worthwhile reading. Or some reason sufficient Or summary is sufficient. You have to search at all. And also modify Book files generator prompt if you think anything needs to be added in itContinue but search properly everything search the chapter list chapter summary. Individually chess. The summary of the complete book Also, if I should read the book or not. Redo this for the books from Booker. 3 to Book 15.b Search the web for the chapter summaries individually Use web search tool Individually, for everything Listed below Searching the summary of the book Searching the table of content. Searching the chapter summary is individually Searching the Book summary Searching if the book is worthwhile reading. Or some reason sufficient Or summary is sufficient. You have to search at all. And also modify Book files generator prompt if you think anything needs to be added in it