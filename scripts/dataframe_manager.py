from envtest import get_dataframe_head

import pandas as pd
import numpy as np

#my_df = pd.read_csv("test_data.csv")
my_df = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

print(get_dataframe_head(my_df))