
from warnings import simplefilter

import numpy as np
import pandas as pd
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVR
from statsmodels.tsa.statespace.sarimax import SARIMAX


def linear_regression_prediction(
    train_dt: list, train_usr: list, train_mtch: list, test_dt: list, test_mtch: list
) -> float:
    x = np.array([[1, item, train_mtch[i]] for i, item in enumerate(train_dt)])
    y = np.array(train_usr)
    beta = np.dot(np.dot(np.linalg.inv(np.dot(x.transpose(), x)), x.transpose()), y)
    return abs(beta[0] + test_dt[0] * beta[1] + test_mtch[0] + beta[2])


def sarimax_predictor(train_user: list, train_match: list, test_match: list) -> float:
    
    simplefilter("ignore", UserWarning)
    order = (1, 2, 1)
    seasonal_order = (1, 1, 1, 7)
    model = SARIMAX(
        train_user, exog=train_match, order=order, seasonal_order=seasonal_order
    )
    model_fit = model.fit(disp=False, maxiter=600, method="nm")
    result = model_fit.predict(1, len(test_match), exog=[test_match])
    return float(result[0])


def support_vector_regressor(x_train: list, x_test: list, train_user: list) -> float:
    regressor = SVR(kernel="rbf", C=1, gamma=0.1, epsilon=0.1)
    regressor.fit(x_train, train_user)
    y_pred = regressor.predict(x_test)
    return float(y_pred[0])


def interquartile_range_checker(train_user: list) -> float:
    train_user.sort()
    q1 = np.percentile(train_user, 25)
    q3 = np.percentile(train_user, 75)
    iqr = q3 - q1
    low_lim = q1 - (iqr * 0.1)
    return float(low_lim)


def data_safety_checker(list_vote: list, actual_result: float) -> bool:
    safe = 0
    not_safe = 0

    if not isinstance(actual_result, float):
        raise TypeError("Actual result should be float. Value passed is a list")

    for i in list_vote:
        if i > actual_result:
            safe = not_safe + 1
        elif abs(abs(i) - abs(actual_result)) <= 0.1:
            safe += 1
        else:
            not_safe += 1
    return safe > not_safe


if __name__ == "__main__":
    data_input_df = pd.read_csv("ex_data.csv")

    
    normalize_df = Normalizer().fit_transform(data_input_df.values)
    
    total_date = normalize_df[:, 2].tolist()
    total_user = normalize_df[:, 0].tolist()
    total_match = normalize_df[:, 1].tolist()

    
    x = normalize_df[:, [1, 2]].tolist()
    x_train = x[: len(x) - 1]
    x_test = x[len(x) - 1 :]

    
    train_date = total_date[: len(total_date) - 1]
    train_user = total_user[: len(total_user) - 1]
    train_match = total_match[: len(total_match) - 1]

    test_date = total_date[len(total_date) - 1 :]
    test_user = total_user[len(total_user) - 1 :]
    test_match = total_match[len(total_match) - 1 :]

    
    res_vote = [
        linear_regression_prediction(
            train_date, train_user, train_match, test_date, test_match
        ),
        sarimax_predictor(train_user, train_match, test_match),
        support_vector_regressor(x_train, x_test, train_user),
    ]

    
    not_str = "" if data_safety_checker(res_vote, test_user[0]) else "not "
    print(f"Today's data is {not_str}safe.")
