import matplotlib.pyplot as plt
import numpy as np
import util
import os

from cmath import inf

from p05b_lwr import LocallyWeightedLinearRegression as LWLR


def main():
    """Problem 5(b): Tune the bandwidth paramater tau for LWR.

    Args:
        tau_values: List of tau values to try.
        train_path: Path to CSV file containing training set.
        valid_path: Path to CSV file containing validation set.
        test_path: Path to CSV file containing test set.
        pred_path: Path to save predictions.
    """
    # get data and output paths
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    train_path = os.path.join(data_dir, 'ds5_train.csv')
    valid_path = os.path.join(data_dir, 'ds5_valid.csv')
    pred_path = os.path.join(os.path.dirname(__file__), 'output')

    # Load training set
    x_train, y_train = util.load_dataset(train_path, add_intercept=True)
    x_valid, y_valid = util.load_dataset(train_path, add_intercept=True)

    # Search tau_values for the best tau (lowest MSE on the validation set)
    tau = 1
    mse_best = inf
    tau_best = 1
    for i in range(10): 
        Model = LWLR(tau)
        Model.fit(x_train, y_train)

        predictions = Model.predict(x_valid)
        mse = np.mean((predictions - y_valid)**2)

        if mse < mse_best: 
            mse_best = mse
            tau_best = tau

        plt.figure()
        plt.plot(x_valid, y_valid, 'bx')
        plt.plot(x_valid, predictions, 'go')
        plt.savefig(os.path.join(pred_path, 'p05c_lwr_tau={}.jpeg'.format(tau))) 

        # this tau was a random choice; I didn't have access to the given values to be tested 
        # so I just chose to continually divide by this number to be honest
        # It's not very scientific but I'm still learning
        tau /= 1.4

    print("Best tau =", tau_best, "with MSE of", mse_best)

    # should test on test set here, need to move on though unfortunately 
if __name__ == "__main__": 
    main()