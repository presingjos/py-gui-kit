"""MODEL: Contains data and buisness logic"""
import os
from runpy import run_path

class Model():
    def __init__(self):
        """Handles the buisness logic"""
        print("Model Initialzed")

    def feature_data(self, feature):
        """Try to run the feature specified and
        return feature data.

        Parameters
        ----------
        feature : string
            The feature to try to load

        Returns
        -------
        dict
            Python dictionary of feature specific data

        """

        path = os.path.join(os.getcwd(), "model/features", feature+".py")
        feature = run_path(path)['Feature']
        return feature.data()

    def feature_action(self, feature):
        path = os.path.join(os.getcwd(), "model/features", feature+".py")
        feature = run_path(path)['Feature']
        return feature.action()

if __name__ == "__main__":
    model = Model()
    print(model.feature_data("expandable_table"))
