# The Full Book

The full book puts all 12 sections of Security Fundamentals in one PDF, in English and (after translation) Khmer:

- one cover: navy "blueprint" grid, the course title, the course mark, author and date
- one contents page, with the page number of every section and topic
- "How to Use This Book" (`how-to-use.en.md`, and `how-to-use.km.md` once translated)
- "References" at the end (`references.en.md`, and `references.km.md` once translated)
- the 12 sections, each starting with a divider page (section number, title, and its topics with page numbers), and with its name in the page header

Build it from the repo root (once the shared `tools/` are brought over from mobile-development and adapted):

    python3 tools/build_lessons.py security-fundamentals --book

The PDFs are written to `output/01-security-fundamentals/security-fundamentals/` and committed, like the section PDFs. The contents page leaves out the headings every section repeats, such as "Summary" and "Practice"; the PDF bookmarks still list them.
