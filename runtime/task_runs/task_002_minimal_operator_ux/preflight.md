# Preflight Record

Route class:
kernel_capability_path

Action path required? yes

Side effect? yes

Gate decision:
sandbox_only

Approval required? no

Allowed scope:
create local static UX files under <repo-root>/runtime/operator_ux/

Forbidden scope:
no remote publish, no external API, no external knowledge-store writes, no autonomous execution

Evidence handle expected:
<repo-root>/runtime/operator_ux/index.html

Verification method:
readback file existence + content sections check

Completion wording before verification:
forbidden

Completion wording after verification:
allowed only if readback passes

Risk notes:
The UX must remain a passive viewer only and must not add hidden execution authority.
