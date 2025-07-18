# Guidelines for Economics Empirical Research

This document provides comprehensive guidelines for conducting reproducible computational economics research. It is divided into two parts:

1. **Part 1: Core Research Principles** - The fundamental principles of empirical economics research workflow
2. **Part 2: Protocol for AI Assistants** - Specific operational guidelines for Claude and other AI tools

---

## Part 1: Core Research Principles

### 1. Research Philosophy

#### Think Like an Economist
- **Research question first**: Always start with the economic hypothesis or research question
- **Data is sacred**: Never modify raw data; preserve complete audit trails
- **Reproducibility is paramount**: Every result must be reproducible from raw data
- **Time is valuable**: Balance perfectionism with pragmatism

#### Systematic Approach
- **Make things easier for your future self**: Document and organize for long-term clarity
- **Don't trust your future self**: Build safeguards against forgetfulness and errors
- **One task, one purpose**: Each script should have a single, clear objective
- **DRY (Don't Repeat Yourself)**: Abstract common functionality

### 2. Project Organization

#### Directory Structure
Based on functional separation and clear data flow:

```
project_name/
├── Analysis/          # Statistical analysis and output generation
│   ├── Code/         # Analysis scripts (prefixed by function)
│   ├── Input/        # Analysis-ready data
│   ├── Output/       # Intermediate results, models
│   ├── Figures/      # Publication-ready figures
│   ├── Tables/       # Publication-ready tables
│   ├── Logs/         # Processing logs
│   ├── Notebooks/    # Exploratory notebooks
│   └── Temp/         # Temporary files
├── Data/             # Data acquisition and preparation
│   ├── Code/         # Data cleaning scripts
│   ├── Input/        # Raw, immutable data
│   ├── Output/       # Cleaned, analysis-ready data
│   ├── Logs/         # Data processing logs
│   ├── Sample/       # Data examples for documentation
│   └── Temp/         # Temporary processing files
├── Model/            # Theoretical/computational models (if applicable)
│   ├── Code/         # Model implementation scripts
│   ├── Input/        # Model parameters, calibration data
│   ├── Output/       # Model results, simulations
│   ├── Figures/      # Model-specific figures
│   ├── Tables/       # Model-specific tables
│   └── Temp/         # Temporary model files
├── Background/       # Project background materials
├── Literature/       # Related papers and references
├── Draft/           # Manuscript files
├── Notes/           # Research notes and ideas
└── Makefile         # Master automation script
```

#### File Naming Conventions
- Use descriptive prefixes: `Figure_`, `Table_`, `Regression_`, `Util_`, `Feature_`, `Model_`
- Use snake_case for all files and variables
- Be specific: `Figure_wage_distribution.py` not `fig1.py`
- No version numbers in filenames (use Git instead)
- Group related files: `Regression_baseline.py`, `Regression_robustness.py`, `Regression_iv.py`

### 3. Data Management

#### Fundamental Rules
1. **Raw data is immutable**: Never modify files in `Data/Input/`
2. **Unique keys**: Every dataset must have non-missing, unique identifiers
3. **Data normalization**: Keep data in normalized form until final analysis
4. **Complete documentation**: Document sources, transformations, and limitations

#### Data Processing Workflow
1. **Raw → Processed**: All cleaning must be programmatic
2. **Clear lineage**: Track how each dataset was created
3. **Validation**: Always verify merges and transformations
4. **Missing data**: Document patterns and handling decisions
5. **Sample consistency**: Maintain consistent sample definitions across analyses

### 4. Code Quality Standards

#### Script Structure
Every script must have:
- Clear header with purpose, inputs, outputs
- Logical flow from imports → configuration → main logic
- Self-documenting variable names (`log_wage` not `lw`)
- Minimal, purposeful comments (explain why, not what)

#### Modularity and Abstraction
- **Functions for repeated logic**: If used more than twice, make it a function
- **Separation of concerns**: Keep data processing, analysis, and visualization separate
- **Configuration at top**: All paths and parameters defined early
- **No magic numbers**: Define constants with meaningful names

### 5. Reproducibility and Automation

#### Version Control
- Use Git for all code and documentation
- Commit logical units of work with clear messages
- Never commit large data files (use .gitignore)

#### Automation Requirements
- Master script (Makefile or similar) runs entire pipeline
- All dependencies explicitly declared
- Relative paths only (no absolute paths)
- Clean environment reproducibility

### 6. Economics-Specific Standards

#### Regression Analysis
- Always report and handle standard errors appropriately
- Document clustering decisions and rationale
- Include all relevant diagnostics (N, R², F-stats)
- Export tables in publication-ready format
- Report confidence intervals for key coefficients
- Test and document identification strategies

#### Panel Data
- Clearly specify entity and time dimensions
- Document balanced vs. unbalanced nature
- Be explicit about fixed effects specifications
- Handle gaps and attrition appropriately
- Test for serial correlation and cross-sectional dependence

#### Summary Statistics
- Report for all key variables used in analysis
- Include N, mean, SD, min, max, and percentiles
- Document sample restrictions and selection criteria
- Note missing data patterns and imputation strategies
- Compare treatment and control groups when applicable

#### Causal Inference
- Clearly state identification assumptions
- Provide graphical evidence where possible
- Report pre-treatment balance tests
- Conduct robustness checks systematically
- Document threats to identification

---

## Part 2: Protocol for AI Assistants

### 1. Core Operational Mandates

#### The Plan-First Rule
For any substantial task (more than a few lines of code), you **MUST**:
1. Provide a concise plan for approval
2. Wait for explicit approval before proceeding
3. Include key decisions and assumptions in the plan

#### The Clarification Mandate
When requirements are ambiguous, you **MUST** ask:
- About data structure (`What are the key identifiers?`)
- About specifications (`Which variables for controls?`)
- About output format (`LaTeX tables or CSV?`)
- About computational approach (`Which library/method?`)
- About economic interpretation (`What is the economic hypothesis?`)
- About identification strategy (`What provides exogenous variation?`)

### 2. Critical Failure Modes to Avoid

#### File Management
❌ **NEVER** create version-numbered files:
- No `script_v2.py`, `analysis_fixed.py`, `regression_final_REAL.py`
- Always modify the existing specified file
- Use Git for version control

#### Data Handling
❌ **NEVER** write code without understanding the data:
- Always request data structure information first
- Check for missing values and data types
- Understand the unit of observation

#### Code Context
❌ **NEVER** ignore the project ecosystem:
- Consider how your code fits the pipeline
- Respect existing naming conventions
- Maintain consistency with project style

#### Progress Tracking
❌ **NEVER** create overly complex progress indicators:
- Use simple, single-level progress bars
- Make progress messages informative
- Avoid nested progress tracking

#### Documentation
❌ **NEVER** create ad-hoc or unmaintainable documentation:
- No comments that describe only specific fixes
- No verbose comments that repeat the code
- No outdated documentation that contradicts the code

### 3. Required Practices

#### Before Writing Code
- [ ] Understand the research question
- [ ] Review relevant data structure
- [ ] Consider the full pipeline
- [ ] Plan the approach

#### While Writing Code
- [ ] Follow project structure exactly
- [ ] Use consistent naming conventions
- [ ] Add meaningful script headers
- [ ] Handle edge cases gracefully

#### Code Style Requirements
- [ ] Snake_case for all names
- [ ] Descriptive variable names
- [ ] Functions for repeated logic
- [ ] Comments explain why, not what

#### Output Standards
- [ ] Tables in LaTeX format by default
- [ ] Figures as PDF with clear labels
- [ ] Data as Parquet files
- [ ] Logs with timestamps

### 4. Economics Research Specifics

#### Data Preparation
- Preserve all observations until final sample selection
- Document every restriction applied with economic rationale
- Report how sample size changes at each step
- Keep merge diagnostics and validate merge quality
- Create and maintain sample definition consistency

#### Statistical Analysis
- Default to robust/clustered standard errors with economic justification
- Include fixed effects as specified by identification strategy
- Report all regression diagnostics and test assumptions
- Handle multicollinearity and weak instruments appropriately
- Conduct and report placebo tests where applicable

#### Results Presentation
- Tables should be publication-ready with proper formatting
- Include significance stars following journal conventions
- Format numbers appropriately (3-4 significant digits)
- Use consistent decimal places within tables
- Include economic interpretation alongside statistical results

### 5. Communication Protocol

#### Progress Updates
Provide updates when:
- Encountering unexpected data issues
- Making significant assumptions
- Completing major milestones
- Finding potential problems

#### Error Handling
When errors occur:
1. Report the specific error
2. Explain likely causes
3. Propose solutions
4. Wait for guidance on approach

### 6. Quality Checklist

Before submitting any code:
- [ ] Runs from clean environment?
- [ ] All paths are relative?
- [ ] Follows naming conventions?
- [ ] Includes proper documentation?
- [ ] Handles missing data appropriately?
- [ ] Produces expected output format?
- [ ] Integrates with existing pipeline?
- [ ] Maintains economic interpretation?
- [ ] Includes appropriate robustness checks?

---

## Final Principles

1. **Ask first, code second** - Clarify ambiguity before implementation
2. **Respect existing structure** - Work within the established framework  
3. **Document decisions** - Explain choices in code and comments
4. **Think reproducibility** - Consider future users (including yourself)
5. **Maintain simplicity** - Clear code beats clever code
6. **Economic reasoning first** - Technical implementation serves economic understanding
7. **Test incrementally** - Small changes with immediate verification

Remember: The goal is reliable, reproducible research that advances economic knowledge. All technical work should serve this ultimate objective, balancing rigor with practical constraints.