import cv2
import glob
import os
import unittest
from src.main import get_most_similar_image


class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Load the test image files before running tests"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        query_ident_filenames = glob.glob(os.path.join(current_dir, 'test_images', 'query_identical_images', '*.jpg'))
        query_ident_filenames.sort()
        cls.query_identical_images = [cv2.imread(filename) for filename in query_ident_filenames if cv2.imread(filename) is not None]

        query_sim_filenames = glob.glob(os.path.join(current_dir, 'test_images', 'query_similar_images', '*.jpg'))
        query_sim_filenames.sort()
        cls.query_similar_images = [cv2.imread(filename) for filename in query_sim_filenames if cv2.imread(filename) is not None]

        candidate_filenames = glob.glob(os.path.join(current_dir, 'test_images', 'candidate_images', '*.jpg'))
        candidate_filenames.sort()
        cls.candidate_images = [cv2.imread(filename) for filename in candidate_filenames if cv2.imread(filename) is not None]

    def test_identical_image_A(self):
        """Test search with image identical to candidate Image A"""
        image = self.query_identical_images[0]
        result_index = get_most_similar_image(image, self.candidate_images, compare_with_color=True)
        self.assertEqual(result_index, 0)

    def test_similar_image_A(self):
        """Test search with image similar to candidate Image A"""
        image = self.query_similar_images[0]
        result_index = get_most_similar_image(image, self.candidate_images, compare_with_color=True)
        self.assertEqual(result_index, 0)

    def test_identical_image_B(self):
        """Test search with image identical to candidate Image B"""
        image = self.query_identical_images[1]
        result_index = get_most_similar_image(image, self.candidate_images, compare_with_color=True)
        self.assertEqual(result_index, 1)

    def test_similar_image_B(self):
        """Test search with image similar to candidate Image B"""
        image = self.query_similar_images[1]
        result_index = get_most_similar_image(image, self.candidate_images, compare_with_color=True)
        self.assertEqual(result_index, 1)

    def test_identical_image_C(self):
        """Test search with image identical to candidate Image C"""
        image = self.query_identical_images[2]
        result_index = get_most_similar_image(image, self.candidate_images, compare_with_color=True)
        self.assertEqual(result_index, 2)

    def test_similar_image_C(self):
        """Test search with image similar to candidate Image C"""
        image = self.query_similar_images[2]
        result_index = get_most_similar_image(image, self.candidate_images, compare_with_color=True)
        self.assertEqual(result_index, 2)

    def test_identical_image_D(self):
        """Test search with image identical to candidate Image D"""
        image = self.query_identical_images[3]
        result_index = get_most_similar_image(image, self.candidate_images, compare_with_color=True)
        self.assertEqual(result_index, 3)

    def test_similar_image_D(self):
        """Test search with image similar to candidate Image D"""
        image = self.query_similar_images[3]
        result_index = get_most_similar_image(image, self.candidate_images, compare_with_color=True)
        self.assertEqual(result_index, 3)

    def test_identical_image_E(self):
        """Test search with image identical to candidate Image E"""
        image = self.query_identical_images[4]
        result_index = get_most_similar_image(image, self.candidate_images, compare_with_color=True)
        self.assertEqual(result_index, 4)

    def test_similar_image_E(self):
        """Test search with image similar to candidate Image E"""
        image = self.query_similar_images[4]
        result_index = get_most_similar_image(image, self.candidate_images, compare_with_color=True)
        self.assertEqual(result_index, 4)


if __name__ == '__main__':
    unittest.main()
