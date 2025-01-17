import numpy as np




def mae(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    difference = abs(predict - actual)
    score = difference.mean()

    return score



def mse(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    square_diff = np.square(difference)

    score = square_diff.mean()
    return score



def rmse(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    square_diff = np.square(difference)
    mean_square_diff = square_diff.mean()
    score = np.sqrt(mean_square_diff)
    return score



def rmsle(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    log_predict = np.log(predict + 1)
    log_actual = np.log(actual + 1)

    difference = log_predict - log_actual
    square_diff = np.square(difference)
    mean_square_diff = square_diff.mean()

    score = np.sqrt(mean_square_diff)

    return score



def mbd(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    numerator = np.sum(difference) / len(predict)
    denumerator = np.sum(actual) / len(predict)
    
    score = float(numerator) / denumerator * 100

    return score


def manual_accuracy(predict, actual):
    return np.mean(np.array(actual) == np.array(predict))
