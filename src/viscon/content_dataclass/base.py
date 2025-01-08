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
    """

    content_list: List[Content]


@dataclass
class VisualObjectSequence:
    """Class to store a sequence of visual objects.

    This includes videos as a sequence of Visual Objects.

    Args:
        visual_object_list: List of VisualObject objects.
    """

    visual_object_list: List[Content]
