# Personal Development Guidelines for Scientific & Engineering Projects

## Core Principles - ALWAYS Follow

### 1. Single Source of Truth
- **ONE main script/file per functionality** - never create `script_v2.py`, `script_enhanced.py`, `script_robust.py`
- When fixing bugs or adding features, modify the existing file
- Use git branches for experimental changes, not new files
- Consolidate redundant files immediately when discovered

### 2. Systematic Testing Strategy
- **ALWAYS test on small datasets/samples first** (5-10% of full data)
- Never run full experiments until small tests pass
- Create test datasets that run in < 2 minutes
- For long-running processes (>10 min), implement checkpointing/progress tracking

### 3. Incremental Development
- **One change at a time** - never mix multiple features/fixes
- Document what each change is intended to do before making it
- Test each change independently
- If something breaks, you know exactly what caused it

### 4. Proper Version Control Workflow
- `git init` at project start, not after problems occur
- Commit working state before making ANY changes
- Create meaningful commit messages explaining WHY, not just what
- Use `.gitignore` properly - never track large data files, only code and metadata

## File Organization Standards

### Naming Conventions
- Use consistent, descriptive names: `analyze_data.py`, not `script1.py`
- Prefix related files consistently: `train_model.py`, `test_model.py`, `evaluate_model.py`
- No version numbers in filenames: use git tags instead
- Data files: use metadata files instead of tracking raw data in git

### Project Structure
```
project/
├── src/           # Main code
├── data/          # Raw data (gitignored)
├── results/       # Outputs (gitignored)  
├── docs/          # Documentation
├── tests/         # Test scripts
└── metadata/      # Data descriptions, sample lists
```

## Before Making Changes - Mandatory Checklist

### Understanding Phase
1. **Read ALL existing code** in the project before modifying anything
2. **Identify the working approach** - trace back from successful results
3. **Document current state** - what works, what doesn't, and why
4. **Create git commit** of current working state

### Planning Phase
1. **Define EXACTLY what you want to change** in one sentence
2. **Identify the minimal change needed** - don't over-engineer
3. **Plan testing strategy** - small dataset, expected results
4. **Estimate time** - if >30 min, break into smaller steps

### Implementation Phase
1. **Test on small data first** - never start with full dataset
2. **Make one change at a time** - resist the urge to "improve while you're at it"
3. **Verify each step works** before proceeding
4. **Document any new patterns or solutions**

## Error Recovery Protocols

### When Things Go Wrong
1. **STOP immediately** - don't try "quick fixes"
2. **Identify the last working state** - use git history if needed
3. **Revert to working state** before debugging
4. **Reproduce the problem on small data** before fixing

### Before Asking for Help
1. **Document exactly what you tried** and what happened
2. **Identify the specific error/problem** - not just "it doesn't work"
3. **Show the working vs non-working approaches** side by side
4. **Prepare minimal reproducible example**

## Data Management Best Practices

### Version Control for Data
- **Never track large data files in git** - use metadata files instead
- Create `samples_metadata.txt` with: filename, source, time_range, label, parameters
- Write scripts to regenerate data from metadata when needed
- Track data processing parameters and decisions

### Long-Running Processes
- **Always implement progress logging** for processes >5 minutes
- **Add checkpointing** for processes >30 minutes  
- **Create background runners** with PID tracking and clean shutdown
- **Monitor resource usage** - memory, CPU, disk space

## Communication Standards

### Code Documentation
- **Comment WHY, not what** - explain the reasoning behind decisions
- **Document failed approaches** - what didn't work and why
- **Include examples** in function docstrings
- **Update docs when code changes**

### Problem Reporting
- **Be specific**: "Function X fails on data type Y with error Z"
- **Not vague**: "The code doesn't work" or "Something is wrong"
- **Include context**: what you were trying to accomplish
- **Show what you've tried**: failed approaches with results

## Tools and Commands to Remember
- Testing: Create 5-minute test datasets from full data
- Git workflow: `git status`, `git diff`, `git log --oneline`
- Process monitoring: `ps aux | grep python`, `tail -f logfile.log`
- Resource monitoring: `top`, `df -h`, `du -sh`

## Red Flags - When to Stop and Reconsider
- Creating files with version numbers or variants in names
- Running the same failing command repeatedly hoping it works
- Making multiple changes without testing each one
- Processes running >2x expected time without clear progress
- Memory or disk usage growing unexpectedly
- More than 3 similar error messages in a row

Remember: **Slow and systematic beats fast and chaotic every time.**