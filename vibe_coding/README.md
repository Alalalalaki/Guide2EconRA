

(unsorted)

### Prompt Engineering

- [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
- [Claude 4 prompt engineering best practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#example-formatting-preferences)



### Claude Code

- [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices) / [How Anthropic teams use Claude Code](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf) / [Code w/ Claude](https://www.youtube.com/watch?v=gv0WHhKelSE)
- [ClaudeLog](https://claudelog.com/)



### Context Engineering

- [How to Fix Your Context](https://github.com/langchain-ai/how_to_fix_your_context)



### MCP

- [Serena](https://github.com/oraios/serena): A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & Agno integration)

- [GitMCP](https://github.com/idosal/git-mcp)

- [Claude-Flow v2.0.0 Alpha](https://github.com/ruvnet/claude-flow) / [Ultra MCP](https://github.com/realmikechong/ultra-mcp)

- [Code Context](https://github.com/zilliztech/code-context)

  

### Agent

- [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code)



---

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

