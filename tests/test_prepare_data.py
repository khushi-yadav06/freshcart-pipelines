
from iris_project.prepare_data import prepare_data


def test_prepare_data():
    X_train, X_test, y_train, y_test = prepare_data()

    assert len(X_train) == 120
    assert len(X_test) == 30

    assert len(y_train) == 120
    assert len(y_test) == 30

    assert X_train.shape[1] == 4
    assert X_test.shape[1] == 4

