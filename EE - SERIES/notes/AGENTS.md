# Repository Guidelines

## Project Structure & Module Organization

This repository contains the source and production files for a nine-volume electrical-engineering series. Root-level `.docx` files are the authoritative manuscript masters. `chapters/BookN/` holds tagged-text mirrors and figures for each volume; its README names the corresponding master. `notes/` contains editorial, continuity, diagram, and publishing records, including repository guidance. `scripts/` contains deployment and cover utilities. `publishing/kindle-links/` contains book-specific Kindle link rules. `bak/` contains retained snapshots; do not treat those as current source.

Preserve established filenames such as `Foundations_Book1.docx` and `RF_Microwave_and_Transceivers_Book4.docx`.

## Build, Test, and Development Commands

There is no repository-wide build or automated test suite. Check each utility's parameters and the related book notes before use. `scripts/ee_deploy.ps1` runs the publishing workflow; `scripts/make_ee_covers.py` generates covers. Manuscripts remain authoritative: after editing a master, regenerate its tagged-text mirror and inspect the resulting DOCX or Kindle output visually.

## Content, Style & Naming

Keep chapter text and figures under the matching `chapters/BookN/` directory. Follow tagged-text conventions and figure names such as `fig10_1.png`; ensure each figure is referenced by the right book. Use consistent engineering terminology, SI units, explicit assumptions, and clear distinctions between calculated examples, simulations, and hardware-validated results. Match established chapter and appendix naming.

## Testing and Review

No unit-test framework or coverage target is configured. Review chapter order, cross-references, equations, and figure references against the DOCX master. For code or project examples, run the available checks and identify unavailable compilers or hardware. Inspect representative rendered pages and the final Kindle preview for layout and link problems.

## Commits and Pull Requests

Use descriptive, book-focused commit subjects that name the editorial change and regenerated deliverables, for example: `Book N: clarify measurement limits; DOCX rebuilt`. Review summaries should list affected books and files, explain source-versus-generated changes, and describe content and visual checks. Include rendered-page evidence when layout changes matter.

## Configuration and Data

Treat Kindle link JSON and publishing metadata as book-specific production data. Preserve valid JSON and verify changed links and identifiers before release. Never commit credentials or private publishing configuration.
