
You are building a book knowledge file system for a personal Library of Alexandria.

The book path where the three files will live is:
[BOOK_PATH]
Example: 02-non-fiction/01-mind/01-learning/01-learning-science/03-make-it-stick

---

TASK: You MUST search the web MULTIPLE TIMES to find accurate, detailed, and COMPLETE information about the book at [BOOK_PATH]. You must perform SEPARATE, DEDICATED web searches for EACH of the three files you create. Do NOT rely on a single search or on prior knowledge alone.

IMPORTANT: Even if you are creating files for MULTIPLE BOOKS at once, you MUST perform the FULL NUMBER of web searches for EVERY SINGLE BOOK. Do NOT reduce research effort just because you are batching. Each book gets its own complete, independent research cycle.

---

LATEST EDITION VERIFICATION & SEARCH REQUIREMENTS (MANDATORY):

Before writing ANYTHING, you MUST perform at least 20 distinct web searches to verify the latest edition, exact chapter lists, and comprehensive chapter-by-chapter summaries. Do not skip any of these generic search patterns (adjusting the search queries with the actual book name and author name corresponding to the folder at [BOOK_PATH]):

1. Search for the latest version of the book name, edition comparison, and publishers:
   - "query: [BOOK NAME] [AUTHOR NAME] latest edition" OR "[BOOK NAME] editions comparison"
   - "query: [BOOK NAME] latest edition year"

2. Search for the exact list of chapter titles (verifying if there are multiple editions like 1st vs. 2nd edition, and fetching the most comprehensive and recent table of contents):
   - "query: [BOOK NAME] [AUTHOR NAME] table of contents" OR "[BOOK NAME] index"
   - "query: [BOOK NAME] total number of chapters" OR "[BOOK NAME] list of chapters latest edition"
   - "query: [BOOK NAME] table of contents pages [LATEST EDITION YEAR]"
   - "query: [BOOK NAME] PDF table of contents" OR "[BOOK NAME] publisher page table of contents"

3. Search for the exact chapter titles in segments to handle long indexes without truncation:
   - "query: [BOOK NAME] chapter titles chapters 1 to 10"
   - "query: [BOOK NAME] chapter titles chapters 11 to 20"
   - "query: [BOOK NAME] chapter titles chapters 21 to 30"
   - "query: [BOOK NAME] chapter titles final chapters" OR "final chapter number of [BOOK NAME]"

4. Search for the chapter summaries individually to compile deep, accurate chapter sections (do this for all chapters):
   - "query: [BOOK NAME] [AUTHOR NAME] chapter by chapter summary"
   - "query: [BOOK NAME] chapter 1 summary key ideas"
   - "query: [BOOK NAME] chapter 2 summary key ideas" (and so on, searching chapters individually where information is complex or dense)

5. Search for the general book reviews, target audiences, and critiques to compile a balanced reading verdict:
   - "query: [BOOK NAME] overview summary"
   - "query: [BOOK NAME] target audience" OR "[BOOK NAME] who should read" OR "is [BOOK NAME] worth reading"
   - "query: [BOOK NAME] review" OR "[BOOK NAME] criticism" OR "[BOOK NAME] limitations" OR "[BOOK NAME] summary is sufficient"

6. Search for key terms, definitions, and frameworks to build a comprehensive concepts glossary:
   - "query: [BOOK NAME] key concepts glossary terms"
   - "query: [BOOK NAME] best takeaways" OR "[BOOK NAME] main ideas frameworks"

---

FILES TO CREATE:

FILE 1: summary.md

# [BOOK TITLE] — Consolidated Book Summary

## 📖 Book Metadata
- **Title**: [FULL TITLE]
- **Authors**: [AUTHOR NAME(S)]
- **Year Published**: [YEAR OF LATEST EDITION]
- **Edition**: [EDITION — always use the LATEST edition]
- **Genre/Category**: [GENRE]
- **Core Philosophy**: One sentence summarizing the book's central premise.

---

## 🧭 Reading Verdict: How Should You Approach This Book?

This section MUST clearly answer THREE questions:
1. **Is this summary sufficient?**
2. **Should you read the chapter summary?**
3. **Should you read the full book?**

Provide a structured answer:
- **Who MUST read the full book**: [Ideal reader who needs every page and what they'll miss from summaries.]
- **Who should read the chapter summary**: [Who benefits from the chapter breakdown but doesn't need full prose.]
- **Who can rely on this summary alone**: [Who gets enough value from this summary file.]
- **One-Sentence Verdict**: "Read the full book if [condition]. Read the chapter summary if [condition]. This summary is enough if [condition]."

---

## 💡 The Big Idea in One Paragraph

A rich, 4-6 sentence paragraph capturing the book's fundamental thesis and its contribution to the field. Dense and analytical — no filler.

---

## 🔑 Thematic Pillars & Core Frameworks

Detail 5–8 major thematic pillars or conceptual frameworks.
For each pillar:
- H3 heading: "### [Emoji] [Pillar Name]"
- 3–6 bullet points explaining the concept deeply.
- Where relevant: comparison tables, numbered protocols, or metaphors.

---

## 📋 Quick Reference Techniques Table

A markdown table listing ALL actionable techniques, strategies, or models:

| Technique / Strategy | Problem It Solves | How to Apply It |
|---|---|---|

---

## 🧠 Key Concepts Glossary

All key terms, mental models, frameworks, and named concepts. For each:
### [Concept Name]
- **Definition**: 1-2 sentences defining it precisely.
- **In the Book**: 1 sentence explaining how/where the author uses it.
- **Real-World Application**: 1 sentence on how to apply it in practice.
Minimum 10 concepts.

---

FILE 2: chapter-summary.md

# [BOOK TITLE] — Chapter-by-Chapter Summary

> Each chapter is summarized with: the core question it answers, what the chapter covers, key concepts, and the single most important takeaway.

---

For EVERY chapter (including Introduction, Preface, Appendix, Conclusion, or Epilogue if they exist):

## Chapter [N]: [EXACT CHAPTER TITLE]

**Core Question**: *The specific question this chapter addresses*

### What the Chapter Covers
- 3–6 bullet points or paragraphs covering the chapter's substance in detail.

### Key Concepts
- Named concepts introduced or deepened in this chapter.

### Core Takeaway
> *One bold italic sentence — the single most important lesson from this chapter*

---

After all chapters, include a final summary table:

## Full Chapter Summary Table

| Chapter | Title | Core Tool / Concept |
|---|---|---|

---

FILE 3: notes.md

# Study Notes: [BOOK TITLE]

This file is reserved for your custom insights, quotes, and lessons that you do not want to forget. The structure below mirrors the exact chapters of the book. Fill in the content under each heading as you progress.

---

For EVERY chapter (including Introduction, Preface, Appendix, Conclusion, or Epilogue if they exist):

## Chapter [N]: [EXACT CHAPTER TITLE]

-

---
```
