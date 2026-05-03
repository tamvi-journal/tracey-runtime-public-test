from typing import Literal, NotRequired, TypedDict

from runtime.contracts.enums import LifecycleStatus, ObsidianCanonicalStatus

MemoryKind = Literal[
    "user_profile",
    "project",
    "skill",
    "ontology",
    "interaction_trace",
    "identity_axis",
    "canonical_candidate",
]

MemorySource = Literal[
    "conversation",
    "spec",
    "task_run",
    "manual",
    "import",
]

AuthorityStatus = ObsidianCanonicalStatus


class SemanticMemoryRecord(TypedDict):
    id: str
    user_id: str
    kind: MemoryKind
    title: str
    content: str
    tags: list[str]
    strength: float
    source: MemorySource
    source_handles: list[str]
    lifecycle_status: LifecycleStatus
    authority_status: AuthorityStatus
    created_at: str
    last_accessed: str | None
    embedding_model: str
    embedding: list[float]
    metadata: NotRequired[dict[str, object]]


class SemanticMemoryCandidate(TypedDict):
    record: SemanticMemoryRecord
    similarity: float
    rerank_score: float
    blocked: bool
    block_reason: str


class MemoryRetrievalRequest(TypedDict):
    user_id: str
    query: str
    query_embedding: list[float]
    allowed_kinds: list[MemoryKind]
    top_k: int
    min_similarity: float
    include_deprecated: bool


class MemoryRetrievalResult(TypedDict):
    query: str
    candidates: list[SemanticMemoryCandidate]
    retrieval_status: Literal["passed", "empty", "blocked", "partial"]
    notes: str


class ConsolidationCandidate(TypedDict):
    user_id: str
    kind: MemoryKind
    title: str
    content: str
    tags: list[str]
    source: MemorySource
    source_handles: list[str]
    strength: float
    reason: str
    requires_approval: bool
