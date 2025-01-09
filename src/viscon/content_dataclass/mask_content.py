"""Dataclass for mask content."""

from dataclasses import dataclass
from os import PathLike
from typing import Optional, Union

from viscon.content_dataclass.base import Content, ContentLicense, ContentSize, ContentURL, Metadata


@dataclass
class MaskMetadata(Metadata):
    """Stores mask metadata.

    Args:
        origin_dataset: The dataset name if any.
        origin_url: The original url if any.
    """

    origin_dataset: Optional[str] = None
    origin_url: Optional[ContentURL] = None


@dataclass
class MaskContent(Content):
    """Base class to store mask content.

    Args:
        mask_path: Either PathLike object of the mask on disk or ContentURL for mask URL.
        license: ContentLicense.
        size: optional ContentSize.
    """

    mask_path: Union[PathLike, ContentURL]
    license: ContentLicense
    metadata: MaskMetadata
    size: Optional[ContentSize] = None
