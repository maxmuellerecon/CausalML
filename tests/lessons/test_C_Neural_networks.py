# Test file for C_Neural_networks

import pandas as pd
import pytest

pytestmark = pytest.mark.filterwarnings("ignore")
import pandas as pd
import keras
import unittest

from causalmachinelearning.config import BLD, SRC
from causalmachinelearning.lessons.C_Neural_networks import (
    preprocess_data,
    scale_datasets,
    build_model_using_sequential,
    predict_house_value,
    assess_performance,
)


class TestPreprocessData(unittest.TestCase):
    def setUp(self):
        self.train_data = pd.DataFrame(
            {
                "median_house_value": [100000, 200000, 300000],
                "feature1": [1, 2, 3],
                "feature2": [4, 5, 6],
            }
        )
        self.test_data = pd.DataFrame(
            {
                "median_house_value": [400000, 500000, 600000],
                "feature1": [7, 8, 9],
                "feature2": [10, 11, 12],
            }
        )

    def test_preprocess_data_shape_x_train(self):
        x_train, _, _, _ = preprocess_data(self.train_data, self.test_data)
        self.assertEqual(x_train.shape, (3, 2))

    def test_preprocess_data_shape_y_train(self):
        _, y_train, _, _ = preprocess_data(self.train_data, self.test_data)
        self.assertEqual(y_train.shape, (3,))

    def test_preprocess_data_shape_x_test(self):
        _, _, x_test, _ = preprocess_data(self.train_data, self.test_data)
        self.assertEqual(x_test.shape, (3, 2))

    def test_preprocess_data_shape_y_test(self):
        _, _, _, y_test = preprocess_data(self.train_data, self.test_data)
        self.assertEqual(y_test.shape, (3,))


def test_preprocess_data_shape_x_train():
    """Test preprocess_data function for x_train shape."""
    train_data = pd.read_csv(SRC / "data" / "california_housing_train.csv")
    test_data = pd.read_csv(SRC / "data" / "california_housing_test.csv")
    x_train, _, _, _ = preprocess_data(train_data, test_data)
    assert x_train.shape == (17000, 8)


def test_preprocess_data_shape_y_train():
    """Test preprocess_data function for y_train shape."""
    train_data = pd.read_csv(SRC / "data" / "california_housing_train.csv")
    test_data = pd.read_csv(SRC / "data" / "california_housing_test.csv")
    _, y_train, _, _ = preprocess_data(train_data, test_data)
    assert y_train.shape == (17000,)


def test_preprocess_data_shape_x_test():
    """Test preprocess_data function for x_test shape."""
    train_data = pd.read_csv(SRC / "data" / "california_housing_train.csv")
    test_data = pd.read_csv(SRC / "data" / "california_housing_test.csv")
    _, _, x_test, _ = preprocess_data(train_data, test_data)
    assert x_test.shape == (3000, 8)


def test_preprocess_data_shape_y_test():
    """Test preprocess_data function for y_test shape."""
    train_data = pd.read_csv(SRC / "data" / "california_housing_train.csv")
    test_data = pd.read_csv(SRC / "data" / "california_housing_test.csv")
    _, _, _, y_test = preprocess_data(train_data, test_data)
    assert y_test.shape == (3000,)


def test_scale_datasets_shape_x_train_scaled():
    """Test scale_datasets function for x_train_scaled shape."""
    train_data = pd.read_csv(SRC / "data" / "california_housing_train.csv")
    test_data = pd.read_csv(SRC / "data" / "california_housing_test.csv")
    x_train, _ = scale_datasets(train_data, test_data)
    assert x_train.shape == (17000, 9)


def test_scale_datasets_shape_x_test_scaled():
    """Test scale_datasets function for x_test_scaled shape."""
    train_data = pd.read_csv(SRC / "data" / "california_housing_train.csv")
    test_data = pd.read_csv(SRC / "data" / "california_housing_test.csv")
    _, x_test = scale_datasets(train_data, test_data)
    assert x_test.shape == (3000, 9)


class TestBuildModelUsingSequential(unittest.TestCase):
    def test_build_model_using_sequential_numer_layers(self):
        """Test build_model_using_sequential function for layer 0 shape."""
        model = build_model_using_sequential()
        actual = len(model.layers)
        expected = 6
        self.assertEqual(actual, expected)


def test_build_model_using_sequential_number_layers():
    """Test build_model_using_sequential function for layer 0 shape."""
    model = build_model_using_sequential()
    actual = len(model.layers)
    expected = 6
    assert actual == expected


def test_predict_house_value_shape():
    """Test predict_house_value function for prediction shape."""
    model = keras.models.load_model(
        BLD / "python" / "Lesson_C" / "model" / "model.keras"
    )
    x_test = pd.read_csv(SRC / "data" / "california_housing_test.csv")
    x_test_scaled = pd.read_csv(
        BLD / "python" / "Lesson_C" / "data" / "x_test_scaled.csv"
    )
    prediction = predict_house_value(model, x_test, x_test_scaled)
    assert prediction.shape == (3000, 11)


def test_assess_performance_sample_data():
    """Test assess_performance function."""
    x_test_pred = pd.DataFrame(
        {
            "prediction": [100000, 200000, 300000],
            "feature1": [1, 2, 3],
            "feature2": [4, 5, 6],
        }
    )
    y_test = pd.DataFrame({"median_house_value": [400000, 500000, 600000]})
    actual = assess_performance(x_test_pred, y_test)
    expected = 300000.0
    assert actual == expected


def test_assess_performance_shape():
    """Test assess_performance function for performance shape."""
    x_test_pred = pd.read_csv(BLD / "python" / "Lesson_C" / "data" / "x_test_pred.csv")
    y_test = pd.read_csv(BLD / "python" / "Lesson_C" / "data" / "y_test.csv")
    actual = assess_performance(x_test_pred, y_test)
    expected = 200000
    assert actual >= expected
