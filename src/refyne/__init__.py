"""Official Python SDK for the Refyne API.

Refyne is an LLM-powered web extraction API that transforms unstructured
websites into clean, typed data.

Example:
    >>> from refyne import Refyne
    >>>
    >>> client = Refyne(api_key="your_api_key")
    >>>
    >>> result = await client.extract(
    ...     url="https://example.com/product",
    ...     schema={"name": "string", "price": "number"},
    ... )
    >>> print(result.data)
"""

from refyne.cache import MemoryCache, create_cache_entry, parse_cache_control
from refyne.client import JobResultEntry, JobResults, Refyne, RefyneConfig
from refyne.errors import (
    AuthenticationError,
    ForbiddenError,
    NotFoundError,
    RateLimitError,
    RefyneError,
    TLSError,
    UnsupportedAPIVersionError,
    ValidationError,
)
from refyne.interfaces import Cache, CacheEntry, HttpClient, Logger
from refyne.types import (
    AnalyzeRequest,
    AnalyzeResponse,
    ApiKey,
    ApiKeyCreated,
    ApiKeyList,
    CrawlJobCreated,
    CrawlOptions,
    CrawlRequest,
    CreateApiKeyRequest,
    CreateSchemaRequest,
    CreateSiteRequest,
    ExtractionMetadata,
    ExtractRequest,
    ExtractResponse,
    Job,
    JobList,
    JobStatus,
    LlmChain,
    LlmChainEntry,
    LlmConfig,
    LlmKey,
    LlmKeyList,
    ModelList,
    Schema,
    SchemaList,
    SetLlmChainRequest,
    Site,
    SiteList,
    TokenUsage,
    UpsertLlmKeyRequest,
    UsageResponse,
)
from refyne.version import (
    MAX_KNOWN_API_VERSION,
    MIN_API_VERSION,
    SDK_VERSION,
)

__version__ = SDK_VERSION

__all__ = [
    # Client
    "Refyne",
    "RefyneConfig",
    # Errors
    "RefyneError",
    "RateLimitError",
    "ValidationError",
    "AuthenticationError",
    "ForbiddenError",
    "NotFoundError",
    "UnsupportedAPIVersionError",
    "TLSError",
    # Types
    "ExtractRequest",
    "ExtractResponse",
    "CrawlRequest",
    "CrawlJobCreated",
    "CrawlOptions",
    "Job",
    "JobStatus",
    "JobList",
    "JobResults",
    "JobResultEntry",
    "AnalyzeRequest",
    "AnalyzeResponse",
    "Schema",
    "SchemaList",
    "CreateSchemaRequest",
    "Site",
    "SiteList",
    "CreateSiteRequest",
    "ApiKey",
    "ApiKeyList",
    "ApiKeyCreated",
    "CreateApiKeyRequest",
    "UsageResponse",
    "LlmKey",
    "LlmKeyList",
    "UpsertLlmKeyRequest",
    "LlmChain",
    "LlmChainEntry",
    "SetLlmChainRequest",
    "ModelList",
    "TokenUsage",
    "ExtractionMetadata",
    "LlmConfig",
    # Interfaces
    "Logger",
    "HttpClient",
    "Cache",
    "CacheEntry",
    # Cache
    "MemoryCache",
    "parse_cache_control",
    "create_cache_entry",
    # Version
    "SDK_VERSION",
    "MIN_API_VERSION",
    "MAX_KNOWN_API_VERSION",
]
