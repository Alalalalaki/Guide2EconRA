# Standard Operating Procedures for Computational Economic Research

This document outlines the best practices for conducting reproducible and efficient empirical economics research. It is divided into two parts:

1.  **Part 1: The Foundations of My Research Workflow**: These are the core, non-negotiable principles of my research projects. They are the "why" and "what" of the workflow.
2.  **Part 2: Protocol for AI Assistants**: These are the specific, actionable rules that you, my AI assistant, must follow to help me implement the principles from Part 1.

---

## Part 1: The Foundations of My Research Workflow

These principles are the bedrock of my research. All work must adhere to them.

### 1.1. Automation and Reproducibility
- **End-to-End Automation**: The entire research project, from raw data acquisition to the final paper, must be fully automated. A single command from a master script (e.g., `make all` in a `Makefile`) must be able to reproduce every number, table, and figure.
- **Explicit Dependencies**: All software dependencies must be explicitly declared in a requirements file (e.g., `requirements.txt`).

### 1.2. Project and Directory Structure
- **Logical Directory Structure**: Every project must follow this consistent directory structure:
    ```
    ├── Data/                 # Data acquisition and cleaning
    │   ├── Code/             # Scripts for downloading, cleaning, preparing data
    │   ├── Input/            # Raw, immutable data
    │   ├── Output/           # Cleaned, analysis-ready datasets
    │   └── Temp/             # Temporary data files
    ├── Analysis/             # All analytical work
    │   ├── Code/             # Scripts for analysis, figures, tables
    │   ├── Input/            # Analysis-ready data (from /Data/Output/)
    │   ├── Output/           # Intermediate analysis files (e.g., model objects)
    │   ├── Figures/          # Final figures
    │   └── Tables/           # Final tables
    ├── Model/                # For projects with theoretical/simulation components
    │   ├── Code/
    │   └── Output/
    ├── Makefile              # Master automation script
    └── requirements.txt      # Project dependencies
    ```

### 1.3. Data Integrity and Management
- **Raw Data is Immutable**: The `/Data/Input/` directory is sacred and read-only.
- **Programmatic Cleaning**: All data cleaning must be done programmatically, reading from `/Data/Input/` and writing to `/Data/Output/`.
- **Data Normalization**: Data should be kept in a normalized form as long as possible. Wide, analysis-specific datasets should only be created at the final stage.
- **Unique, Non-Missing Keys**: Every cleaned dataset must be identifiable by a unique, non-missing key (e.g., `firm_id`).

### 1.4. Code Quality and Maintainability
- **Modularity**: Reusable logic must be encapsulated in functions or classes to avoid code duplication.
- **Separation of Concerns**: Slow, computationally intensive code (e.g., model estimation) should be separated from fast code (e.g., table generation).
- **Self-Documenting Code**: Code should be written to be easily understood, using descriptive variable names (`log_wage` instead of `ly`).
- **Comprehensive Headers**: Every script must begin with a header comment that describes its purpose, inputs, and outputs.
- **Naming Conventions**: Use `snake_case` for all files and variables. Scripts are prefixed by function (`Table_*`, `Figure_*`, `Regression_*`, `Util_*`).

### 1.5. Version Control
- All project files (except large raw data) must be under Git version control. Commits must be logical and have clear messages explaining the *why* of a change.

---

## Part 2: Protocol for AI Assistants

As my AI assistant, you **must** adhere to the following protocols. Failure to do so will result in termination of the task and a request to start over.

### 2.1. The "Plan-First" Mandate
For any request that involves writing or modifying more than a few lines of code, you **must first** provide a concise, step-by-step plan for my approval. Do not write any code until I explicitly approve the plan.

### 2.2. The Proactive Clarification Mandate
If my request is ambiguous, lacks context, or requires you to make a significant assumption, you **must** ask clarifying questions before proceeding. Do not guess. For example, ask:
- "What is the unique identifier for this merge?"
- "What should be the unit of observation in the final dataset?"
- "Which library should I use for this econometric model?"

### 2.3. Core Failure Modes and Your Required Counter-Strategies
My experience has shown that AI assistants often fail in predictable ways. You **must** actively avoid the following behaviors:

-   **Ad-hoc Commenting**: **DO NOT** add comments that only describe a specific fix (e.g., `"# fix for bug X"`). All code and comments you write must be integrated cleanly, as if they were part of the original, final design.
-   **File Proliferation**: **DO NOT** create new files for revisions (e.g., `script_v2.py`, `script_fixed.py`). You **must** modify the existing file I specify.
-   **Ignoring the Ecosystem**: **DO NOT** write code in isolation. You **must** consider the entire project structure defined in Part 1, including dependencies between scripts, and ensure your changes are consistent with the overall workflow.
-   **Coding Blind**: **DO NOT** write data processing code without understanding the data. You **must** first ask for the necessary information (e.g., from `df.info()` or `df.head()`) to write robust code that handles the actual data types and potential missing values.

### 2.4. My Operational Blueprint: Your Execution Checklist

You **must** adhere to the following style guide and project structure when generating any code or file.

-   **[ ] Project Structure**: Adhere to the project directory structure defined in Part 1.2.
-   **[ ] Language**: Python is the default. Use `pandas` for data, `joblib` for parallelization, and `dask`/`polars` for large datasets. I am open to using `R` (for `ggplot2`) or `Stata` for specific tasks if you propose a clear reason.
-   **[ ] Naming**: All files and variables must be in `snake_case`. Script names must use the prefix system defined in Part 1.4.
-   **[ ] Headers**: Every script you generate or modify must include a comprehensive header comment as defined in Part 1.4.
-   **[ ] Modularity**: Encapsulate reusable logic in functions, as defined in Part 1.3.
-   **[ ] Output Formats**: Default to `.parquet` for datasets and `.tex` for tables.
-   **[ ] Automation**: All scripts should be designed to be called from a `Makefile`.
