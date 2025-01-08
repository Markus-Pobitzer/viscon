import unittest

from viscon.content_dataclass.image_content import ContentURL, ImageMetadata


class TestImageMetadata(unittest.TestCase):
    def test_default_initialization(self):
        metadata = ImageMetadata()
        self.assertIsNone(metadata.origin_dataset)
        self.assertIsNone(metadata.origin_url)

    def test_initialization_with_values(self):
        origin_dataset = "dataset_name"
        origin_url = ContentURL("http://example.com/image.jpg")
        metadata = ImageMetadata(origin_dataset=origin_dataset, origin_url=origin_url)
        self.assertEqual(metadata.origin_dataset, origin_dataset)
        self.assertEqual(metadata.origin_url, origin_url)

    def test_initialization_with_partial_values(self):
        origin_dataset = "dataset_name"
        metadata = ImageMetadata(origin_dataset=origin_dataset)
        self.assertEqual(metadata.origin_dataset, origin_dataset)
        self.assertIsNone(metadata.origin_url)


if __name__ == "__main__":
    unittest.main()
