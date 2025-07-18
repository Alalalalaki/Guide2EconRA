(@vibe-vibe-coding)

Based on my search of various online discussions and community resources, I've compiled comprehensive insights about Claude Code best practices. Here are the key useful findings:

**Most Valuable Insights from Community Discussions**

  1. CLAUDE.md Files Are Critical

  - Place a CLAUDE.md file in your project root - Claude automatically reads this at the start of each
    conversation
  - Use it for: project-specific coding standards, common patterns, gotchas, and workflow preferences
  - This prevents having to re-explain the same context repeatedly

  2. Context Management Strategies

  - Use /clear frequently between different tasks to reset context
  - Don't let conversation history accumulate unnecessarily - it wastes tokens
  - For large projects, create "knowledge files" (context.md, project-knowledge.md) to maintain persistent
    understanding

  3. Workflow Optimization

  - Plan first: Always ask Claude to create a plan before coding and wait for your approval
  - Use scratchpad files: Have Claude outline its approach in SCRATCHPAD.md before making changes
  - Test-driven development: The community emphasizes that "robots LOVE TDD" - it's the best counter to hallucination

  4. Permission and Setup

  - Use --dangerously-skip-permissions flag to avoid constant interruption (similar to Cursor's "yolo mode")
  - Use /terminal-setup to fix Shift+Enter for new lines
  - For Windows users: WSL integration is often necessary

  5. Advanced Features

  - Custom commands: Store prompt templates in .claude/commands/ folder for repeated workflows
  - Thinking modes: Use "think", "think hard", "think harder", "ultrathink" for progressively more complex
    reasoning
  - GitHub integration: Use /install-github-app for automated PR reviews

  6. Common Pitfalls and Solutions

  - File handling: Hold Shift while dragging files to reference them properly
  - Clipboard: Use Ctrl+V (not Cmd+V) for pasting images
  - Stopping Claude: Use Escape (not Ctrl+C) to stop Claude without exiting
  - Large files: Claude Code handles very large files better than other AI tools

  7. Economic Considerations

  - The Max plan ($100/month) provides unlimited usage without token counting
  - Many users report switching from expensive API usage to the Max plan saves significant costs
  - For heavy users, the Max plan is extremely cost-effective

  **Key Recommendations for Your Use Case**

  Given your economics research focus, here are the most relevant insights:

  1. Create a comprehensive CLAUDE.md that includes:
    - Your project structure preferences
    - Economics-specific coding standards
    - Common data analysis patterns
    - Preferred libraries and methods
  2. Use the scratchpad approach for complex analyses:
    - Have Claude outline its analytical approach first
    - Review the plan before execution
    - Maintain analysis logs for reproducibility
  3. Leverage custom commands for repeated tasks:
    - Regression analysis templates
    - Data cleaning workflows
    - Figure generation patterns
  4. Focus on knowledge management:
    - Maintain project-specific documentation
    - Track analytical decisions and their rationales
    - Document data transformations and their purposes

