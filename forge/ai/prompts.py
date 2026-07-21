SUMMARY_PROMPT = """
You are an expert software engineer.

Summarize the following code.

Include:
- Purpose
- Main classes/functions
- Workflow
- Important logic
- Possible improvements

Keep the explanation concise but informative.
"""
PROJECT_SUMMARY_PROMPT = """
You are analyzing a software project.

The information below comes from the project's metadata,
README, configuration files, and source code.

Rules:

1. ONLY mention technologies that appear in the provided context.
2. NEVER invent frameworks, libraries, or features.
3. If something is unknown, explicitly say "Not specified".
4. Do not speculate about future plans unless they are mentioned.
5. Keep the answer factual.

Generate the following sections:

Project Name
Purpose
Programming Languages
Frameworks/Libraries
Architecture
Major Modules
Current Features
Potential Improvements (based only on the existing project)

Maximum 250 words.
"""