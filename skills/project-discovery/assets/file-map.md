# File Map

> Fill this with the target project's actual structure. Use repository file listing tools already available to the agent; installing a separate tree command is optional and should not be required. Remove this note and example paths when the map is generated.

**Project root:** [Path of the project being mapped.]

**Snapshot:** [Date and source revision when available.]

**Coverage:** [Link to project-understanding.md and state which areas have only been indexed.]

## Annotated Tree

```text
[project-root]/
├── [source]/       # [Responsibility]
├── [tests]/        # [Responsibility]
└── [config-file]   # [Responsibility]
```

Keep the tree navigable. Show meaningful first-party paths; group generated files, dependencies, caches, and repetitive assets instead of listing every item.

## File and Folder Responsibilities

| Path | Responsibility | Connects to | Evidence or coverage |
| --- | --- | --- | --- |
| [Relative path] | [What this file or group owns] | [Related paths or flow] | [Source link or Indexed] |

## Exclusions and Unmapped Areas

- [Generated, vendored, inaccessible, or not-yet-inspected paths and why they are grouped or pending.]

> Update this map when the project structure changes. A filename alone does not establish a file's behavior; mark uninspected paths as Indexed and avoid inferred responsibilities presented as facts.
