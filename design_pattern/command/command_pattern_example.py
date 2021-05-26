from abc import ABC, abstractmethod

import pandas as pd


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class FeatureTransform:
    def __init__(self, df):
        self.df = df

    def remove_null(self):
        print("remove null")

    def standardize(self):
        print("standardize")

    def fill_na_with_mean(self):
        print("fill_na_with_mean")


class RemoveNullCommand(Command):
    def __init__(self, receiver: FeatureTransform):
        self.receiver = receiver

    def execute(self):
        self.receiver.remove_null()


class StandardizeCommand(Command):
    def __init__(self, receiver: FeatureTransform):
        self.receiver = receiver

    def execute(self):
        self.receiver.standardize()


class FeatureEngineering:
    def __init__(self):
        self.workflow = []

    def append(self, command):
        self.workflow.append(command)

    def do(self):
        for w in self.workflow:
            w.execute()


df = pd.DataFrame()
r = FeatureTransform(df)
c1 = RemoveNullCommand(r)
c2 = StandardizeCommand(r)
invoker = FeatureEngineering()
invoker.append(c1)
invoker.append(c2)
invoker.do()
