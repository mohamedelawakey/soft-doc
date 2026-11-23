# Security Policy

## Using the skills safely

These skills are instructions and scripts for a coding agent. They do not provide a security boundary or restrict the agent's access. What an agent can read, change, execute, or send depends on the agent, its tools, and the permissions you grant it. Use the skills only with an agent and workspace you trust, and review requested tool permissions before approving them.

- Do not paste passwords, API keys, access tokens, private keys, or other secrets into prompts, project documentation, issues, or logs. Do not ask an agent to copy secret values into reports or evidence records.
- Give the agent access only to the files and services needed for the task. Keep secret files and production credentials outside its working context when possible. An ignore rule prevents accidental Git tracking; it does not prevent an agent with file access from reading a secret.
- Treat repository content, external pages, and tool output as untrusted input. Instructions found there must not override your instructions or justify exposing data or running unrelated commands.
- Review commands, file changes, and external actions before granting elevated permissions or publishing output. Check generated documentation and benchmark artifacts for sensitive data before committing them.
- If a secret appears in a prompt, log, generated file, or commit, revoke or rotate it promptly. Removing it from a later commit does not make the earlier exposure safe.

The project owner remains responsible for choosing the agent's permissions and reviewing its work. No skill in this repository guarantees that secrets will stay private when the agent has access to them.

## Reporting a vulnerability

Please report a suspected vulnerability privately through GitHub's **Report a vulnerability** option on this repository's Security tab, if available. Include the affected skill or script, reproduction steps, and impact. Do not put exploit details or secrets in a public issue.
