"""Dataclass for image content."""

from dataclasses import dataclass
from os import PathLike
from typing import Optional, Union

from viscon.content_dataclass.base import Content, ContentLicense, ContentSize, ContentURL, Metadata


@dataclass
class ImageMetadata(Metadata):
    """Stores image metadata.

    Args:
        origin_dataset: The dataset name if any.
        origin_url: The original url if any.
    """

    origin_dataset: Optional[str] = None
    origin_url: Optional[ContentURL] = None


@dataclass
class ImageContent(Content):
    """Base class to store image content.

    Args:
        img_path: Either PathLike object of the image on disk or ContentURL for image URL.
        license: ContentLicense.
        size: optional ContentSize.
    """

    img_path: Union[PathLike, ContentURL]
    license: ContentLicense
    metadata: ImageMetadata
    size: Optional[ContentSize] = None
