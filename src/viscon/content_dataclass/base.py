"""File to store the data classes for the base content."""

from dataclasses import dataclass
from typing import List


@dataclass
class Content:
    """Base class to store content related to a visual object.

    The content is an object containing information.
    This can be an image, a mask, text description, bounding boxes, ...
    """


@dataclass
class VisualObject:
    """Class to store a collection of contents related to a visual object.

    This includes images, segmentation masks, bounding boxes, etc.

    Args:
        content_list: List of Content objects.
        object_index: The index of the VisualObject, used if it is part of
            an object sequence.
    """

    content_list: List[Content]
    object_index: int = -1


@dataclass
class VisualObjectSequence:
    """Class to store a sequence of visual objects.

    This includes videos as a sequence of Visual Objects.

    Args:
        visual_object_list: List of VisualObject objects.
    """

    visual_object_list: List[Content]


@dataclass
class Metadata:
    """Stores metadata."""


@dataclass
class ContentURL:
    """Stores the URL for a content.

    Args:
        url: The URL.
    """

    url: str

    def __str__(self):
        """Returns the url."""
        return self.url


@dataclass
class ContentLicense:
    """Stores the license for a content.

    Args:
        license: The license.
    """

    license: str = "Unknown"

    def __str__(self):
        """Returns the license."""
        return self.license


@dataclass
class ContentSize:
    """Stores the size of a content.

    Size is indicated by Width, Height and number of channels.

    Args:
        width: The width.
        height: The height.
        channels: The number of channels.
    """

    width: int
    height: int
    channels: int
