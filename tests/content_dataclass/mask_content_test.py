import unittest
from pathlib import Path

from viscon.content_dataclass.base import ContentLicense, ContentSize, ContentURL
from viscon.content_dataclass.mask_content import MaskContent, MaskMetadata


class TestMaskContent(unittest.TestCase):
    def test_mask_metadata_creation(self):
        metadata = MaskMetadata(origin_dataset="Dataset1", origin_url=ContentURL("http://example.com"))
        self.assertEqual(metadata.origin_dataset, "Dataset1")
        self.assertEqual(metadata.origin_url, ContentURL("http://example.com"))

    def test_mask_content_creation(self):
        metadata = MaskMetadata(origin_dataset="Dataset1", origin_url=ContentURL("http://example.com"))
        mask_content = MaskContent(
            mask_path=Path("path/to/mask"),
            license=ContentLicense("license"),
            metadata=metadata,
            size=ContentSize(100, 200, 1),
        )
        self.assertEqual(mask_content.mask_path, Path("path/to/mask"))
        self.assertEqual(mask_content.license, ContentLicense("license"))
        self.assertEqual(mask_content.metadata, metadata)
        self.assertEqual(mask_content.size, ContentSize(100, 200, 1))

    def test_mask_content_default_size(self):
        metadata = MaskMetadata(origin_dataset="Dataset1", origin_url=ContentURL("http://example.com"))
        mask_content = MaskContent(
            mask_path=Path("path/to/mask"), license=ContentLicense("license"), metadata=metadata
        )
        self.assertIsNone(mask_content.size)


if __name__ == "__main__":
    unittest.main()
