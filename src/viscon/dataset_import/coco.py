"""Code to downlaod and import the COCO dataset."""

from enum import Enum


class COCOSplit(Enum):
    TRAIN2014 = "train2014"
    VAL2014 = "val2014"
    TEST2014 = "test2014"
    TEST2015 = "test2015"
    TRAIN2017 = "train2017"
    VAL2017 = "val2017"
    TEST2017 = "test2017"


class COCODataset:
    """The class for handling the COCO dataset."""

    def __init__(self, split: COCOSplit, dataset_dir: str = "dataset_data/coco/"):
        """Constructs a COCODataset object.

        Args:
            split: The split for the COCO dataset.
            dataset_dir: The path where the dataset gets stored.
        """
        self.split = split
        self.dataset_dir = dataset_dir
