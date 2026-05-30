# Book File Generator Prompt — Library of Alexandria

You are building a book knowledge file system for a personal Library of Alexandria. This prompt generates exactly **THREE files** for each book:

1. `summary.md` — Comprehensive book summary with metadata
2. `chapter-summary.md` — Chapter-by-chapter breakdown
3. `notes.md` — Basic information and table of contents

---

## BOOK DETAILS (Fill Before Running)

- **Title**: [FULL BOOK TITLE]
- **Authors**: [AUTHOR NAME(S)]
- **Year Published**: [YEAR]
- **Edition**: [e.g. 1st, 2nd, Updated — write "1st" if unknown]
- **Genre / Category**: [e.g. Learning Science, Memory, Reading, Note-Taking, Deliberate Practice, Productivity]
- **Companion Books** (if any): [related books in the same series or by the same author]
- **Book Folder Path**: [e.g. `02-non-fiction/01-mind/01-learning/01-learning-science/01-learning-how-to-learn`]

---

## MANDATORY WEB SEARCH REGIMEN (DO NOT SKIP)

BEFORE writing ANY of the three files, you MUST perform ALL of the following web searches. Each search is labeled with which file it contributes to. Many searches serve multiple files — read the results once, use them for all relevant files.

**For LARGE books** (handbooks, encyclopedias, 30+ chapters): perform ADDITIONAL targeted searches for each section/chapter range as noted below.

**For SMALL books** (under 12 chapters): search each chapter individually for content.

---

### ═══════════════════════════════════════════════════════════
### SEARCH GROUP 0 — Book Discovery & Version Verification
### ═══════════════════════════════════════════════════════════

Before diving into deep analysis, ensure you are targeting the correct book and the most current version.

| Search ID | Query | Goal | Contributes To |
|-----------|-------|------|----------------|
| 0.1 | `"[BOOK TITLE] [AUTHOR] official book page"` | Find primary source of truth for book's existence, version, and official description | All files |
| 0.2 | `"[BOOK TITLE] [AUTHOR] latest edition vs previous editions"` | Identify significant changes in latest edition (new chapters, restructured content) | All files |
| 0.3 | `"[BOOK TITLE] [AUTHOR] bibliography / list of works"` | Verify if book is part of a series or has companion volumes | All files |
| 0.4 | `"[BOOK TITLE] [AUTHOR] table of contents site:amazon.com OR site:google.com/books"` | Quickly verify the book matches requested title and author | notes.md |
| 0.5 | `"[BOOK TITLE] [AUTHOR] ISBN"` | Get exact ISBN for citation and verification | notes.md |
| 0.6 | `"[BOOK TITLE] [AUTHOR] page count"` | Determine book length for reading time estimates | summary.md |

---

### ═══════════════════════════════════════════════════════════
### SEARCH GROUP A — Edition & Metadata (All Files)
### ═══════════════════════════════════════════════════════════

| Search ID | Query | Goal | Contributes To |
|-----------|-------|------|----------------|
| A1 | `"[BOOK TITLE] [AUTHOR] latest edition"` | Confirm latest edition year, edition number, publisher. Do NOT assume provided edition is latest | All files |
| A2 | `"[BOOK TITLE] [AUTHOR] editions"` | Check if newer edition exists beyond what is listed in metadata | All files |
| A3 | `"[BOOK TITLE] [AUTHOR] publisher page"` | Pull authoritative description, page count, ISBN from publisher site | All files |
| A4 | `"[BOOK TITLE] [AUTHOR] publication history"` | Understand how book has evolved across editions | summary.md |
| A5 | `"[BOOK TITLE] [AUTHOR] awards recognition"` | Note any significant awards or recognitions | summary.md |

---

### ═══════════════════════════════════════════════════════════
### SEARCH GROUP B — Table of Contents / Chapter Titles
### ═══════════════════════════════════════════════════════════

**CRITICAL for chapter-summary.md & notes.md**

| Search ID | Query | Goal | Contributes To |
|-----------|-------|------|----------------|
| B1 | `"[BOOK TITLE] table of contents"` | Get FULL list of chapter titles. Verify ALL titles across multiple sources | chapter-summary.md, notes.md |
| B2 | `"[BOOK TITLE] [AUTHOR] chapter titles"` | Cross-reference chapter titles from different source than B1 | chapter-summary.md, notes.md |
| B3 | `"[BOOK TITLE] [AUTHOR] table of contents [EDITION YEAR]"` | Ensure chapter list matches latest edition | chapter-summary.md, notes.md |
| B4 | `"[BOOK TITLE] contents page images"` | Find visual confirmation of table of contents | chapter-summary.md, notes.md |
| B5 | `"[BOOK TITLE] introduction summary"` | Verify introduction/preface exist and content | chapter-summary.md |

**FOR LARGE BOOKS (30+ chapters, handbooks, edited volumes):**

| Search ID | Query | Goal | Contributes To |
|-----------|-------|------|----------------|
| B6 | `"[BOOK TITLE] chapter list chapters 1 through 10"` | Get partial chapter list for verification | chapter-summary.md |
| B7 | `"[BOOK TITLE] chapter list chapters 11 through 20"` | Get partial chapter list for verification | chapter-summary.md |
| B8 | `"[BOOK TITLE] chapter list chapters 21 through 30"` | Get partial chapter list for verification | chapter-summary.md |
| B9 | `"[BOOK TITLE] table of contents PDF"` | Find PDF index or Cambridge Core page listing ALL chapters | chapter-summary.md |
| B10 | `"[BOOK TITLE] [EDITION YEAR] table of contents site:cambridge.org"` | Direct hit from authoritative source | chapter-summary.md |
| B11 | `"[BOOK TITLE] [EDITION YEAR] table of contents site:google.com/books"` | Direct hit from authoritative source | chapter-summary.md |
| B12 | `"[BOOK TITLE] part titles"` | Identify major parts/sections in handbooks | chapter-summary.md |

**NEVER invent chapter titles. If a chapter title cannot be verified via web search, note "[TITLE UNVERIFIED]" and move on. Do NOT guess.**

---

### ═══════════════════════════════════════════════════════════
### SEARCH GROUP C — Book-Level Summary (summary.md)
### ═══════════════════════════════════════════════════════════

| Search ID | Query | Goal | Contributes To |
|-----------|-------|------|----------------|
| C1 | `"[BOOK TITLE] [AUTHOR] overview summary"` | Authoritative high-level description of the book | summary.md |
| C2 | `"[BOOK TITLE] [AUTHOR] full book summary"` | Comprehensive summary covering the entire book | summary.md |
| C3 | `"[BOOK TITLE] key concepts main ideas"` | Identify core frameworks, models, and pillars | summary.md |
| C4 | `"[BOOK TITLE] [AUTHOR] thematic pillars"` | Understand major themes and how they connect | summary.md |
| C5 | `"[BOOK TITLE] best takeaways key lessons"` | Verify coverage is comprehensive, not missing key points | summary.md |
| C6 | `"[BOOK TITLE] glossary key terms definitions"` | Build concepts glossary with accurate definitions | summary.md |
| C7 | `"[BOOK TITLE] [AUTHOR] criticism limitations"` | Find credible academic or professional criticism for balanced verdict | summary.md |
| C8 | `"[BOOK TITLE] [AUTHOR] reviews"` | Professional reviews from academic journals, publications | summary.md |
| C9 | `"[BOOK TITLE] [AUTHOR] best quotes"` | Verify major claims and memorable lines | summary.md |
| C10 | `"[BOOK TITLE] [AUTHOR] comparison with similar books"` | Contextualize within the field | summary.md |
| C11 | `"[BOOK TITLE] [AUTHOR] practical applications"` | How concepts are applied in real world | summary.md |

---

### ═══════════════════════════════════════════════════════════
### SEARCH GROUP D — Reading Verdict (summary.md)
### ═══════════════════════════════════════════════════════════

| Search ID | Query | Goal | Contributes To |
|-----------|-------|------|----------------|
| D1 | `"[BOOK TITLE] who should read"` | Identify ideal reader profile | summary.md |
| D2 | `"[BOOK TITLE] is it worth reading"` | Determine if full book is worth time vs summaries | summary.md |
| D3 | `"[BOOK TITLE] summary vs full book"` | Understand what is lost in summarization | summary.md |
| D4 | `"[BOOK TITLE] target audience"` | Who benefits most from reading cover-to-cover | summary.md |
| D5 | `"[BOOK TITLE] reading time"` | How long does it take to read | summary.md |
| D6 | `"[BOOK TITLE] prerequisites"` | What background knowledge helps | summary.md |
| D7 | `"[BOOK TITLE] alternatives to reading"` | Audiobook, video summary options | summary.md |

---

### ═══════════════════════════════════════════════════════════
### SEARCH GROUP E — Chapter-by-Chapter Content
### ═══════════════════════════════════════════════════════════

**For EACH chapter in the book, perform targeted searches:**

| Search ID | Query | Goal | Contributes To |
|-----------|-------|------|----------------|
| E1 (per chapter) | `"[BOOK TITLE] chapter [N] summary"` | Get core question, key content, concepts, and takeaway | chapter-summary.md |
| E2 (per chapter) | `"[BOOK TITLE] chapter [N] key concepts"` | Identify named concepts, frameworks, or models introduced | chapter-summary.md |
| E3 (per chapter) | `"[BOOK TITLE] chapter [N] main argument"` | Understand the chapter's primary thesis | chapter-summary.md |
| E4 (per chapter) | `"[BOOK TITLE] chapter [N] examples"` | Find illustrative examples used | chapter-summary.md |

**FOR LARGE BOOKS (handbooks with 30+ chapters):**

| Search ID | Query | Goal | Contributes To |
|-----------|-------|------|----------------|
| E5 (per section) | `"[BOOK TITLE] Part [I] summary"` | Summarize section theme and its chapters | chapter-summary.md |
| E6 (per section) | `"[BOOK TITLE] Part [I] chapters summary"` | Group summaries for chapters within each part | chapter-summary.md |
| E7 (per section) | `"[BOOK TITLE] section [N] introduction"` | Get section framing and context | chapter-summary.md |

**If a chapter/section has no search results, write the summary using the best available information and note "[Content inferred from related sources — not directly verified]". Do NOT skip the chapter.**

---

### ═══════════════════════════════════════════════════════════
### SEARCH GROUP F — Cross-Verification (All Files)
### ═══════════════════════════════════════════════════════════

| Search ID | Query | Goal | Contributes To |
|-----------|-------|------|----------------|
| F1 | `"[BOOK TITLE] Wikipedia"` | Cross-check metadata, publication date, author info, edition details | All files |
| F2 | `"[BOOK TITLE] Goodreads summary"` | Additional reader-perspective summary points | summary.md |
| F3 | `"[BOOK TITLE] author interview"` | Author's own words about book's purpose and key ideas | summary.md |
| F4 | `"[BOOK TITLE] [AUTHOR] academic papers citing"` | See how book influences scholarly work | summary.md |
| F5 | `"[BOOK TITLE] [AUTHOR] lecture presentation"` | Find author's own summaries in talks | summary.md |
| F6 | `"[BOOK TITLE] [AUTHOR] podcast"` | Audio discussions about the book | summary.md |

---

### ═══════════════════════════════════════════════════════════
### MINIMUM SEARCH COUNT
### ═══════════════════════════════════════════════════════════

| Book Type | Minimum Searches | Additional Requirements |
|-----------|------------------|------------------------|
| Small books (under 12 chapters) | AT LEAST 20 web searches | Individual chapter searches for each chapter |
| Medium books (12-25 chapters) | AT LEAST 25 web searches | Individual chapter searches for chapters with sparse coverage |
| Large handbooks (26-40 chapters) | AT LEAST 30 web searches | Section-level searches for every Part in table of contents |
| Very large books (40+ chapters) | AT LEAST 35 web searches | Part-level searches plus range-based chapter searches |

**Do NOT reduce these counts. Search adequately before writing.**

---

## LATEST EDITION VERIFICATION (MANDATORY)

Before writing ANYTHING, execute Search Group A. Confirm the latest edition. Use the chapter list from the LATEST edition. If the latest edition has different chapters than older editions, use the latest. Always note which edition you are using in the metadata.

---

## FILE 1: summary.md

**Consolidate findings from Search Groups 0, A, C, D, E, F into this file. This must be a complete, exhaustive, and comprehensive survey of the book.**

**Content (all sections are MANDATORY):**

```markdown
# [BOOK TITLE] — Comprehensive Book Summary

## 📖 Book Metadata

- **Title**: [FULL TITLE]
- **Authors**: [AUTHOR NAME(S)]
- **Year Published**: [YEAR]
- **Edition**: [EDITION — always use the LATEST edition found via Search Group A]
- **ISBN**: [ISBN if available]
- **Pages**: [Page count if available]
- **Genre/Category**: [GENRE]
- **Core Philosophy**: [One sentence summarizing the book's central premise]
- **Reading Time**: [Estimated reading time — e.g., "6-8 hours" or "2-3 days of focused reading"]

---

## 🧭 Reading Verdict: How Should You Approach This Book?

This section MUST clearly answer THREE questions with SPECIFIC, ACTIONABLE guidance:

### Question 1: Is this summary sufficient?

- **If YES**: State clearly that `summary.md` alone provides sufficient value and explain what the reader gains.
- **If PARTIALLY**: Explain what additional depth `chapter-summary.md` provides that isn't in this summary.
- **If NO**: Explain what critical information is ONLY available in the full book and why summaries cannot capture it.

### Question 2: Should you read the chapter summary?

- **When chapter-summary.md IS sufficient**: "Read `chapter-summary.md` if you need [specific benefit — e.g., 'detailed examples for each concept', 'step-by-step application guides', 'chapter-specific case studies']."
- **When chapter-summary.md is NOT sufficient**: "Skip `chapter-summary.md` if you only need [specific outcome — e.g., 'the core thesis', 'high-level frameworks', 'key takeaways']."
- **Hybrid approach**: "Read `summary.md` first, then selectively read chapters [X, Y, Z] in `chapter-summary.md` for [specific topics]."

### Question 3: Should you read the full book?

- **Who MUST read the full book**: [Describe the ideal reader who needs every page — their goals, background, and what they'll miss from summaries alone. Be specific about WHAT they miss — e.g., "nuanced arguments", "extended case studies", "methodological details", "emotional narratives".]
- **Who should read the chapter summary**: [Describe who benefits from chapter-by-chapter breakdown but doesn't need full prose.]
- **Who can rely on this summary alone**: [Describe who gets enough value from just this file.]
- **One-Sentence Verdict**: "Read the full book if [specific condition]. Read the chapter summary if [specific condition]. This summary is enough if [specific condition]."

### Reading Verdict Matrix

| Reader Profile | summary.md | chapter-summary.md | Full Book |
|----------------|------------|-------------------|-----------|
| [Profile 1 — e.g., "Busy professional seeking core concepts"] | ✅ Sufficient | ⚠️ Optional | ❌ Not needed |
| [Profile 2 — e.g., "Student studying for exam"] | ⚠️ Good overview | ✅ Recommended | ⚠️ If time permits |
| [Profile 3 — e.g., "Researcher seeking depth"] | ❌ Insufficient | ⚠️ Starting point | ✅ Essential |
| [Profile 4 — e.g., "Practitioner implementing methods"] | ❌ Insufficient | ✅ Required | ✅ Recommended |

---

## 💡 The Big Idea in One Paragraph

A rich, 4-6 sentence paragraph capturing the book's fundamental thesis and its contribution to the field. This must be dense and analytical — no filler.

---

## 🔑 Thematic Pillars & Core Frameworks

Detail 5–8 major thematic pillars or conceptual frameworks that represent the book's core ideas (drawing from Search Groups C and E).

For each pillar:
- H3 heading: "### [Emoji] [Pillar Name]"
- 3–6 bullet points explaining the concept deeply
- Where relevant: comparison tables, numbered protocols, or metaphors used in the book
- **Cross-reference**: Note which chapters develop this pillar

---

## 📋 Quick Reference Techniques Table

A markdown table listing ALL actionable techniques, strategies, or models introduced in the book:

| Technique / Strategy | Problem It Solves | How to Apply It | Chapter Reference |
|---|---|---|---|

---

## 🧠 Key Concepts Glossary

All key terms, mental models, frameworks, and named concepts introduced in this book — defined in plain language (drawing from Search Group C6).

For every named concept, model, law, technique, or term:

### [Concept Name]
- **Definition**: 1-2 sentences defining it precisely.
- **In the Book**: 1 sentence explaining how/where the author uses it.
- **Real-World Application**: 1 sentence on how to apply it in practice.
- **Related Concepts**: 1-2 concepts from this book or other books that connect.

Group concepts by chapter or theme if the book has a large number of them. Minimum 10 concepts, maximum as many as the book genuinely introduces.

---

## 🔗 Connections to Other Books

Identify 3-5 books from the Library of Alexandria that connect to this one:
- **Complementary**: Books that expand on similar themes
- **Prerequisite**: Books that should be read before this one
- **Advanced**: Books that build on concepts from this one
- **Contrasting**: Books that offer opposing viewpoints

---

## 📊 Summary Statistics

| Metric | Value |
|--------|-------|
| Chapters | [Number] |
| Parts/Sections | [Number if applicable] |
| Key Concepts | [Number] |
| Techniques/Strategies | [Number] |
| Reading Difficulty | [Easy/Medium/Hard/Expert] |
| Practical Applicability | [High/Medium/Low] |
| Academic Rigor | [High/Medium/Low] |
```

**STYLE RULES FOR summary.md:**
- No placeholders. Every section must be fully written.
- No filler sentences. Every line must be informative.
- Use markdown tables where comparison adds clarity.
- Use emoji sparingly and only on H2 section headings.
- Write in a dense, analytical style — no fluff.
- The Reading Verdict MUST be specific and actionable — vague guidance like "it depends" is not acceptable.

---

## FILE 2: chapter-summary.md

**BEFORE WRITING: Execute Search Groups B and E fully. Use ONLY verified chapter titles from Search Group B.**

**Content:**

```markdown
# [BOOK TITLE] — Chapter-by-Chapter Summary

> Each chapter is summarized with: the core question it answers, what the chapter covers, key concepts, and the single most important takeaway.

---

## Reading Guidance for This File

**Read this file if you need:**
- [Specific benefit 1 — e.g., "Detailed breakdown of each chapter's argument"]
- [Specific benefit 2 — e.g., "Chapter-by-chapter concept inventory"]
- [Specific benefit 3 — e.g., "Ability to jump to specific chapters"]

**Skip this file if you only need:**
- [What summary.md covers sufficiently]

---

For EVERY chapter (including Introduction, Preface, Appendix, Conclusion, or Epilogue if they exist):

## Chapter [N]: [EXACT CHAPTER TITLE]

**Core Question**: *The specific question this chapter addresses*

### What the Chapter Covers
- 3–6 bullet points or paragraphs covering the chapter's substance in detail (from Search Group E)

### Key Concepts
- Named concepts introduced or deepened in this chapter

### Key Examples
- Notable examples, case studies, or stories used to illustrate concepts

### Core Takeaway
> *One bold italic sentence — the single most important lesson from this chapter*

### Connection to Book's Thesis
- How this chapter advances the book's central argument

---

(horizontal rule between chapters)

FOR LARGE HANDBOOKS (30+ chapters with multiple Parts):
Group chapters under their Part headings. Example:

## Part I: [Part Title]
*[Brief description of the part's theme covering X chapters]*

### Chapter 1: [Title]
**Core Question**: [...]
### What the Chapter Covers
- [...]
### Key Concepts
- [...]
### Core Takeaway
> *[...]*

---

(horizontal rule between parts)

(Individual chapter horizontal rules may be omitted within a part for readability, but MUST be included between parts.)

After all chapters, include a final summary table:

## Full Chapter Summary Table

| Chapter | Title | Core Tool / Concept | Key Takeaway |
|---|---|---|---|

## Concept Distribution Map

| Concept | Introduced in Chapter | Developed in Chapter(s) | Referenced in Chapter(s) |
|---------|----------------------|------------------------|-------------------------|
```

**HEADING RULES FOR chapter-summary.md:**
- Every chapter MUST have an H2 (or H3 within parts for large handbooks) heading with the EXACT chapter title.
- Chapter titles MUST be the EXACT titles from verified web searches in Search Group B. Do NOT rename, shorten, paraphrase, or invent chapter titles.
- For Introduction, Preface, Conclusion, Epilogue, or Appendix sections, use: "## Introduction: [Title]", "## Conclusion: [Title]", etc.
- Use horizontal rules (---) to separate each chapter (or each part for large handbooks).

---

## FILE 3: notes.md

**BEFORE WRITING: Use the exact table of contents chapter list verified by Search Group B and confirmed in FILE 2.**

**Content:**

```markdown
# [BOOK TITLE] — Basic Information & Notes

## 📖 Book Metadata

- **Title**: [FULL TITLE]
- **Authors**: [AUTHOR NAME(S)]
- **Year Published**: [YEAR]
- **Edition**: [EDITION — always use the LATEST edition found via Search Group A]
- **ISBN**: [ISBN if available]
- **Pages**: [Page count]
- **Publisher**: [Publisher name]
- **Genre/Category**: [GENRE]
- **Core Philosophy**: One sentence summarizing the book's central premise.
- **Reading Time**: [Estimated time to read]
- **Library Location**: [Folder path in knowledge-universe]

## 📑 Table of Contents

[Provide the COMPLETE and EXACT list of all chapters, parts, and sections as verified in Search Group B. Use the following format:]

### Front Matter
- Preface / Foreword / Introduction (if present)

### Main Content
- Chapter 1: [Title]
- Chapter 2: [Title]
- Chapter 3: [Title]
- [Continue for all chapters...]

### Back Matter
- Conclusion / Epilogue (if present)
- Appendices (if present)
- Index (if present)

## 📝 Personal Notes

This section is reserved for your custom insights, quotes, and lessons that you do not want to forget.

For EVERY chapter (including Introduction, Preface, Appendix, Conclusion, or Epilogue if they exist):

## Chapter [N]: [EXACT CHAPTER TITLE]

-
```

---

## FINAL CHECK BEFORE WRITING ANY FILE

- [ ] All Group 0 searches done (book discovery verified)
- [ ] All Group A searches done (edition verified)
- [ ] All Group B searches done (chapter titles verified)
- [ ] All Group C searches done (summary researched)
- [ ] All Group D searches done (reading verdict researched)
- [ ] All Group E searches done (chapter content researched)
- [ ] All Group F searches done (cross-verified)
- [ ] No chapter titles are invented or guessed
- [ ] No sections are left as placeholders
- [ ] Reading Verdict is specific and actionable
- [ ] Metadata is consistent across all three files
- [ ] Chapter list matches latest edition

**Only start writing files after ALL checks pass.**

---

## Naming Conventions for Book Folders

Folder names follow this pattern: `[NN]-[book-title-slug]`

- `NN` = zero-padded 2-digit number (e.g. `01`, `14`)
- slug = lowercase, hyphens instead of spaces, no punctuation
- Examples:
  - `01-learning-how-to-learn`
  - `03-make-it-stick`
  - `05-ultralearning`
  - `07-the-cambridge-handbook-of-expertise`
  - `13-the-only-study-guide-youll-ever-need`

---

## Category Management Rules

When managing books within categories:

1. **Minimum 10 books per category**: Each category folder must contain at least 10 books. If fewer, research and add high-quality books to reach the minimum.

2. **Maximum overlap prevention**: Before adding a book to a category:
   - Check if it overlaps significantly with books in OTHER categories
   - If overlap exists, place it in the MOST SPECIFIC category
   - If a book fits equally in multiple categories, place it in the one where it provides the most unique value

3. **Book quality standards**: Only include books that:
   - Are widely recognized in the field
   - Have significant influence or citations
   - Offer unique perspectives not covered by other books in the category
   - Are available in English (or with English translations)

4. **Overlap resolution**:
   - If two books cover >70% similar content, keep the more comprehensive or influential one
   - If books are complementary (different aspects of same topic), keep both but note the relationship in metadata
   - If a book is a sequel/companion, note this in metadata and link to related books

5. **Category boundaries**:
   - **Learning Science**: Books about HOW we learn (cognitive science, memory, metacognition)
   - **Memory**: Books specifically about memory techniques, mnemonics, and memory improvement
   - **Reading**: Books about reading techniques, comprehension, and speed reading
   - **Note-Taking**: Books about note-taking systems, knowledge management, personal knowledge bases
   - **Deliberate Practice**: Books about skill acquisition, expertise development, and practice methods
   - **Productivity**: Books about time management, focus, habits, and work optimization

---

## Maintenance Notes

- Run this prompt whenever you add a new book to any subfolder in `02-non-fiction/` or `01-fiction/`.
- Always verify the chapter list online before generating files — chapter titles must be exact.
- When generating files for MULTIPLE BOOKS at once:
  - Perform the COMPLETE set of web searches for EACH book independently.
  - Do NOT reuse search results across different books.
  - Do NOT reduce the number of searches per book.
  - Treat each book as if it were the ONLY book being processed.
- Delete any existing extra files (concepts.md, README.md, etc.) — each book folder should contain only the 3 required files.
- The "Reading Verdict" section in summary.md must be balanced — include criticism where it exists (from Group C7/C8).
- After adding books to a category, verify the category has at least 10 books. If not, research and add more.
- When adding new books, check for overlap with existing books and resolve per the Overlap Resolution rules above.
