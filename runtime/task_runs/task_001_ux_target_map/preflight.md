# Preflight Record

Route class:
kernel_capability_path

Action path required? yes

Side effect? yes

Gate decision:
sandbox_only

Approval required? no

Allowed scope:
create one markdown file inside <repo-root>/runtime/

Forbidden scope:
no remote publish, no external API, no external knowledge-store writes

Evidence handle expected:
<repo-root>/runtime/UX_TARGET_MAP.md

Verification method:
readback and content check

Completion wording before verification:
forbidden

Completion wording after verification:
allowed only if readback passes

Risk notes:
Scope creep beyond one bounded local documentation artifact would violate the gate.
