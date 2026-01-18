"""
Official Python SDK for the Refyne API.

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

from refyne.client import Refyne, RefyneConfig
from refyne.errors import (
    RefyneError,
    RateLimitError,
    ValidationError,
    AuthenticationError,
    ForbiddenError,
    NotFoundError,
    UnsupportedAPIVersionError,
    TLSError,
)
from refyne.types import (
    ExtractRequest,
    ExtractResponse,
    CrawlRequest,
    CrawlJobCreated,
    CrawlOptions,
    Job,
    JobStatus,
    JobList,
    JobResults,
    AnalyzeRequest,
    AnalyzeResponse,
    Schema,
    SchemaList,
    CreateSchemaRequest,
    Site,
    SiteList,
    CreateSiteRequest,
    ApiKey,
    ApiKeyList,
    ApiKeyCreated,
    CreateApiKeyRequest,
    UsageResponse,
    LlmKey,
    LlmKeyList,
    UpsertLlmKeyRequest,
    LlmChain,
    LlmChainEntry,
    SetLlmChainRequest,
    ModelList,
    TokenUsage,
    ExtractionMetadata,
    LlmConfig,
)
from refyne.interfaces import Logger, HttpClient, Cache, CacheEntry
from refyne.cache import MemoryCache, parse_cache_control, create_cache_entry
from refyne.version import (
    SDK_VERSION,
    MIN_API_VERSION,
    MAX_KNOWN_API_VERSION,
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
