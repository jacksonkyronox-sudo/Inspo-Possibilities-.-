import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import app


class ImageUrlBuilderTests(unittest.TestCase):
    def test_build_image_urls_contains_profession_and_location(self):
        urls = app.build_image_urls("Robotics Engineer", "Tokyo, Japan")

        self.assertEqual(len(urls), 4)
        self.assertTrue(all(url.startswith("data:image/svg+xml") for url in urls))
        self.assertTrue(any("Robotics+Engineer+lifestyle" in url or "Robotics%20Engineer" in url for url in urls))
        self.assertTrue(any("Tokyo%2C%20Japan" in url or "Tokyo+lifestyle" in url for url in urls))

    def test_build_image_urls_percent_encodes_svg_fragments(self):
        urls = app.build_image_urls("Robotics Engineer", "Tokyo, Japan")

        self.assertTrue(all("#grad" not in url.split(",", 1)[1] for url in urls))


if __name__ == "__main__":
    unittest.main()
