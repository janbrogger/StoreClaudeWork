# Prior art: LLM provenance, traceability and agent-filed issues

Web survey, 2026-09-30, made while this template was being built (see the
session in `llm-logs/`). The question was who else combines **(a)** hooks that
archive and commit every coding-agent session transcript, **(b)** a
requirements traceability chain (here Doorstop NEED -> REQ -> DES -> TST) and
**(c)** agent instructions to elicit requirements, design and tests and to file
GitHub issues. Every entry was found by web search. arXiv and a few other
sites were blocked during the survey, so the paper summaries come from search
snippets only.

## 1. Prompts, transcripts and attribution in the repository

| Name | Link | What it is | Compared with this template |
|---|---|---|---|
| SpecStory | https://specstory.com/claude-code, https://github.com/specstoryai/getspecstory | Saves Cursor, Copilot and Claude Code chats as Markdown in `.specstory/history/` | Closest product to (a). Runs as a wrapper (`specstory run claude`), not hooks. Stores Markdown, not the raw JSONL. You commit it yourself. |
| Aider chat history | https://aider.chat/docs/config/options.html | `.aider.chat.history.md` at the repo root | Built into Aider, but Aider suggests gitignoring it. One growing file, not one folder per session. |
| turbocommit | https://github.com/searlsco/turbocommit | Claude Code/Codex hooks that commit after each turn and put the transcript in the commit message (cut to 16 KB) | Also hook-driven. Keeps a shortened transcript in commit messages, not files. |
| Git Prompt Story | https://github.com/QuesmaOrg/git-prompt-story | Claude Code sessions in git notes, with redaction and PII scrubbing | Uses git notes, not tracked files. Its redaction step is worth copying. |
| git-ai | https://github.com/git-ai-project/git-ai | Line-level AI attribution (agent, model, prompt) in git notes that survives rebase and squash | Finer-grained (per line). No readable full transcripts. |
| Agent Trace | https://agent-trace.dev/, https://github.com/cursor/agent-trace | Open JSON spec (Cursor, Cognition and others, 2026) that links code ranges to conversations | A format, not a tool. `llmlog.py` could emit it. |
| Entire (Checkpoints) | https://github.com/entireio/cli | Stores transcripts, prompts and tool calls at each commit on a hidden branch | Closest funded product. Keeps logs off the main branch. |
| claude-code-transcripts | https://github.com/simonw/claude-code-transcripts | Renders Claude Code JSONL to HTML or Gists | A viewer for `llm-logs/`, not a capture tool. |
| claude-code-log | https://github.com/daaain/claude-code-log | Converts JSONL to HTML or Markdown | Same role as the previous row. |
| Claude Code hooks | https://code.claude.com/docs/en/hooks, https://github.com/disler/claude-code-hooks-mastery | The official hook events and community hook collections | The building blocks of (a). None of these packages per-session archiving in the repository. |
| `Assisted-by:` trailer | https://github.com/bcmyguest/assisted-by | `Assisted-by: AGENT:MODEL` commit trailer used in Linux-kernel-style policies | A one-line disclosure that complements full transcripts. |

## 2. Spec-driven development and traceability with agents

| Name | Link | What it is | Compared with this template |
|---|---|---|---|
| GitHub Spec Kit | https://github.com/github/spec-kit | `/specify`, `/plan`, `/tasks` commands plus a "constitution" file | Markdown files per feature. No stable item IDs and no link validation. |
| Kiro (AWS) | https://kiro.dev/docs/specs/ | IDE that writes `requirements.md` (EARS), `design.md` and `tasks.md` | A three-level chain whose last level is tasks, not tests. Traceability stays inside the IDE. |
| BMAD Method | https://www.augmentcode.com/guides/bmad-method-ai-development | Agent personas that produce a PRD, then architecture, then stories | Agile documents. No checked links. |
| Tessl | https://docs.tessl.io/use/spec-driven-development-with-tessl | Specs kept in the repo and paired with tests. Edit the spec first. | Same spirit as (c). Not a formal chain. |
| Agent OS | https://github.com/buildermethods/agent-os | Standards, product and spec layers. `/shape-spec` asks targeted questions. | Similar to the "elicit first" rule. No IDs. |
| OpenFastTrace AI Skills | https://github.com/itsallcode/openfasttrace-ai-skills | Agent skills that take issues through traced requirements, design and implementation | Closest to (b)+(c), using OpenFastTrace instead of Doorstop. OFT itself is GPL. |
| C5-DEC | https://github.com/AbstractionsLab/c5dec/blob/main/docs/manual/ssdlc.md | Secure SDLC on Doorstop, with artifacts shaped so LLMs can query and edit them | Closest use of Doorstop with LLMs. No agent rules and no session logs. |
| sphinx-needs, StrictDoc | https://strictdoc-project.github.io/ | Docs-as-code traceability | Alternatives to Doorstop. |
| AGENTS.md | https://agents.md/ | Vendor-neutral instruction file for agents | A mirror of `CLAUDE.md` would bring Codex, Cursor and Gemini under the same rules. |

## 3. Agents that file GitHub issues

| Name | Link | What it is | Compared with this template |
|---|---|---|---|
| sync-claude-code-with-github-issues | https://github.com/rdmolony/sync-claude-code-with-github-issues | CLAUDE.md tells Claude to open an issue per goal and log prompts to it | Very close to (c). The author notes it is non-deterministic because only instructions enforce it. The hooks in (a) avoid that. |
| claude-code-action | https://github.com/anthropics/claude-code-action | `@claude` in CI, including issue triage | Acts on the server after an issue exists. |
| Copilot "create issues" | https://github.blog/changelog/2025-05-19-creating-issues-with-copilot-on-github-com-is-in-public-preview/ | Drafts issues from chat, and the user confirms each one | Only on request. (c) makes the agent file issues on its own initiative. |
| anthropics/claude-code#13797 | https://github.com/anthropics/claude-code/issues/13797 | Report of issues filed in the wrong (vendor) repository | Why `CLAUDE.md` restricts filing to `origin`. |

## 4. Research on provenance and reproducibility

- Bhave et al. (INL), *Bridging the Gap on AI-Assisted Scientific Software
  Development Through Transparency and Traceability*, arXiv 2605.17675:
  commit metadata on AI involvement, session logs linked to issues, and
  AGENTS.md rules, under NQA-1 quality assurance. It is the closest in spirit
  to this template. The survey could not fetch the full text.
- Palmblad, Ragland and Neely, *GROUNDING.md*, J. Proteome Res. 2026
  (arXiv 2604.21744): a file of domain constraints that overrides other agent
  context.
- PROV-AGENT, arXiv 2508.02866: a W3C PROV extension for agent interactions.
- *Guidelines for Empirical Studies in SE involving LLMs*, arXiv 2508.15503:
  publish full prompt and response logs.
- *LLMs for Software Engineering: A Reproducibility Crisis*, arXiv 2512.00651.
- JOSS generative-AI disclosure policy (2026):
  https://blog.joss.theoj.org/2026/01/preparing-joss-for-a-generative-ai-future
- TRIPOD-LLM, Nature Medicine 2025: https://www.nature.com/articles/s41591-024-03425-5

## What is uncommon here

Each part exists elsewhere, but the survey found nothing that combines all
three. Transcript archivers do not connect to a requirements model.
Spec-driven tools use loose Markdown, not a validated NEED -> REQ -> DES -> TST
graph with stable IDs.

Several things look distinctive:

- Capture is enforced by hooks, not left to the model's instructions.
- Full per-session transcripts are ordinary tracked files, not git notes, a
  hidden branch or commit messages.
- Doorstop, including a test level, is the target the agent writes to.

Ideas worth borrowing:

- Automatic redaction of secrets and PII before a transcript is committed
  (Git Prompt Story).
- An `AGENTS.md` mirror of `CLAUDE.md`.
- `Assisted-by:` trailers or Agent Trace records.
- EARS wording for REQ items (Kiro).
