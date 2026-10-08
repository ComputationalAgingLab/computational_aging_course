# Aging Research Digest: A Daily AI-Powered Literature Alert for Geroscience

## Introduction

Keeping up with the rapidly expanding field of aging research is a significant challenge. Thousands of new papers are published each year across PubMed, bioRxiv, and other repositories—covering molecular hallmarks of aging, senolytics, epigenetic clocks, longevity interventions, and more. Researchers, clinicians, and longevity enthusiasts alike struggle to filter signal from noise.

Aging Research Digest is an open-source Telegram bot designed to solve this problem. Every day, it automatically:

* Fetches newly published articles related to aging from PubMed (with optional bioRxiv support),
* Uses zero-shot classification to tag papers by biological hallmarks (e.g., cellular senescence, mitochondrial dysfunction), data types (e.g., DNA methylation, RNA-seq), species, and article type,
* Generates concise, two-paragraph summaries using a local open-weight LLM (Phi-3-mini), highlighting key findings and methodologies,
* Ranks articles by scientific impact (journal prestige) and use of computational methods,
* Sends the top 3 most relevant papers directly to your Telegram,
* Archives all discovered articles in a searchable Google Sheet for long-term reference.
* Unlike general-purpose research bots (e.g., Papers With Code Bot, arXiv Sanity Preserver, or Connected Papers), this tool is domain-specialized for geroscience and integrates multi-dimensional semantic labeling aligned with the Hallmarks of Aging framework. It requires no cloud APIs or paid subscriptions—everything runs locally using open-source models.

By automating discovery, classification, and distillation of aging literature, Aging Research Digest empowers scientists, students, and longevity advocates to stay informed without spending hours sifting through abstracts.

## Implementation of the Aging Research Digest Bot

The Aging Research Digest bot is an automated system designed to help researchers and enthusiasts stay updated with the latest scientific literature on aging. The core idea is simple: every day, the bot discovers newly published papers related to aging, analyzes them using artificial intelligence, summarizes their key findings, and delivers the most relevant ones directly to a Telegram channel—while also archiving everything in a shared online spreadsheet for long-term reference.

The entire system is built using open-source tools and runs locally without relying on commercial APIs or cloud-based LLM services. This ensures privacy, sustainability, and full compliance with the project requirement to use pre-trained, non-finetuned language models.

### Architecture Overview

The implementation follows a clean, modular design. Instead of a single monolithic script, the codebase is split into logical components that each handle a specific part of the pipeline: fetching articles, classifying them, generating summaries, storing results, and sending notifications. This separation makes the system easier to test, debug, and extend.

At the center of everything is `main.py`, which orchestrates the daily workflow. It starts by retrieving recent publications from PubMed, processes each one through classification and summarization, saves the enriched data to Google Sheets, selects the top three papers based on relevance and scientific impact, and finally sends them via Telegram.

### Article Retrieval

We focused on PubMed as the primary data source because it provides a reliable, official API (NCBI E-utilities) and rich metadata for biomedical literature. The fetcher constructs a search query using key terms like “aging,” “senescence,” and “longevity,” limited to articles published in the last few days. It retrieves the title, authors, journal, publication date, abstract, and a direct link to the article. We avoided Google Scholar due to its lack of a public API and the high risk of IP blocks from aggressive scraping.

As a complementary approach, we have also developed a Selenium-based crawler for Springer Nature Link to access recent publications that may not yet be indexed in PubMed. This crawler navigates search results, visits individual article pages, and extracts comparable metadata, including abstracts and DOIs. However, this method is still under active testing and optimization due to challenges related to page structure variability, access restrictions, and performance overhead compared to API-based retrieval.

### Semantic Classification

To understand what each paper is about, we implemented a multi-label classifier that tags articles along four meaningful dimensions without any custom training. Using the `facebook/bart-large-mnli` model from Hugging Face in zero-shot mode, the system analyzes the title and abstract to assign labels such as article type (e.g., research article or review), relevance to the established hallmarks of aging (like mitochondrial dysfunction or cellular senescence), types of data used (e.g., RNA-seq or DNA methylation), and biological species studied (using Latin names like *Homo sapiens* or *Mus musculus*). A confidence threshold ensures only reliable labels are retained.

### Scientific Summarization

For summarization, we leverage the free tier of OpenRouter, which provides access to capable large language models without cost. Specifically, we use the model `qwen/qwen3-235b-a22b:free`, a high-performing variant of Alibaba’s Qwen3 series offered under OpenRouter’s free usage limits. This model is prompted with a clear, structured instruction to generate exactly two paragraphs: the first focusing on the key biological findings, and the second concisely describing the methods and data types used. To ensure reliability and minimize hallucination, we disable sampling and apply a low temperature during inference. The resulting summaries are succinct, scientifically coherent, and grounded in the source text, all while operating within accessible, no-cost infrastructure.

### Persistent Storage

All processed articles — whether delivered or not — are saved to a Google Sheet. This fulfills the requirement to maintain a continuously updated, web-hosted archive. The system automatically creates the spreadsheet on first run, defines appropriate columns (including PMID, title, labels, and summary), and avoids duplicates by checking existing PMIDs. Authentication is handled via a Google Cloud service account, eliminating the need for interactive OAuth during automated runs.

### Telegram Delivery

The top three papers—ranked by a combination of journal prestige, relevance (e.g., *Aging Cell*, *Nature Aging*) and presence of computational methods (detected via keywords like “machine learning” or “algorithm”) — are formatted into clean, visually scannable messages and sent to a Telegram channel. The messages use MarkdownV2 formatting with proper escaping to ensure titles appear in bold, journals in italics, and key metadata like data types or species in inline code blocks. Links point directly to the PubMed page for easy access.

### Configuration and Deployment

All sensitive credentials and tunable parameters are managed through environment variables, with optional support for a `.env` file during development. This includes the Telegram bot token, chat ID, Google service account JSON, and NCBI email. The system is designed to run once per day via a cron job or similar scheduler and typically completes within 5–10 minutes on a modern laptop, with the LLM inference being the main time cost.

In summary, the Aging Research Digest bot demonstrates how open-source AI, scientific APIs, and automation can be combined to build a useful, domain-specific tool that addresses information overload in aging research—fully transparently, locally, and without reliance on proprietary services.

## Discussion and Future Work

The Aging Research Digest bot demonstrates a practical and scalable approach to keeping up with the rapidly evolving field of geroscience. By combining open-access literature APIs, zero-shot classification, and efficient local language models, it delivers targeted, high-quality scientific updates without relying on external paid services or cloud inference. This design aligns well with academic values of reproducibility, transparency, and accessibility.

One key strength of the current implementation is its **domain specificity**. Unlike generic research alert tools (e.g., arXiv bots or broad PubMed keyword alerts), this system understands the conceptual framework of aging biology—particularly the hallmarks of aging—and uses that structure to enrich and filter content. This allows users to quickly assess whether a paper addresses mitochondrial dysfunction, epigenetic drift, senescence, or other mechanisms of interest.

However, several limitations remain. The system currently relies solely on **abstracts**, which may omit critical methodological details or nuanced findings only described in the full text. While full-text parsing is technically possible (e.g., via Europe PMC or Unpaywall), it introduces complexity around access rights, PDF parsing errors, and copyright considerations. Future versions could integrate open-access full texts where legally available, or use hybrid approaches that prioritize abstracts but supplement with full-text snippets when possible.

Another area for improvement is **temporal coverage**. PubMed indexing can lag by several days, meaning truly “hot off the press” preprints on bioRxiv may not appear in our feed immediately. Although bioRxiv support was planned, it was not fully integrated in the initial release. Adding a robust bioRxiv fetcher—with deduplication against future PubMed entries—would significantly enhance timeliness and comprehensiveness.

The classification system, while effective, is currently limited to predefined label sets. Expanding it to **detect emerging topics** (e.g., new interventions like epigenetic reprogramming or novel biomarkers) would require either dynamic label generation or periodic manual updates to the candidate categories. Similarly, species detection could be enhanced by linking to taxonomic databases rather than relying on keyword matching.

On the infrastructure side, the current Google Sheets backend is user-friendly but not optimized for large-scale querying or long-term analytics. Migrating to a lightweight database (e.g., SQLite or Airtable) could enable advanced features like trend analysis, author tracking, or personalized recommendations based on user feedback. Additionally, while the Phi-3-mini model performs well, newer open models (e.g., Llama-3.1 or Mistral-Nemo) may offer improved scientific reasoning and should be evaluated as drop-in replacements.

Finally, user interaction remains one-directional. A natural next step would be to add **Telegram command support**, allowing users to request papers on specific hallmarks (“/hallmark senescence”), filter by species (“/species Mus musculus”), or toggle delivery preferences. Over time, this could evolve into a conversational agent that answers questions about aging biology using the curated literature corpus.

In conclusion, while the current bot fulfills the core requirements of automated discovery, summarization, and delivery, it also serves as a foundation for a more intelligent, interactive, and comprehensive aging research assistant—one that not only informs but also adapts to the evolving needs of the longevity science community.