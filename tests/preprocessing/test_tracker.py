import numpy as np
import pandas as pd
import math

import niimpy.preprocessing.tracker as tracker
from niimpy import config


def test_step_summary():
    df = pd.read_csv(config.STEP_SUMMARY_PATH, index_col=0)
    # Converting the index as date
    df.index = pd.to_datetime(df.index)

    summary_df = tracker.step_summary(df, value_col='steps')
    assert summary_df['max_sum_step'].values[0] == 13025
    assert summary_df['min_sum_step'].values[0] == 5616
    assert round(summary_df['avg_sum_step'].values[0], 2) == 8437.38
    assert round(summary_df['std_sum_step'].values[0], 2) == 3352.35
    assert summary_df['median_sum_step'].values[0], 2 == 6480.0


def test_daily_step_distribution():
    df = pd.read_csv(config.STEP_SUMMARY_PATH, index_col=0)
    # Converting the index as date
    df.index = pd.to_datetime(df.index)

    res = tracker.extract_features_tracker(df)

    assert isinstance(res, pd.DataFrame)
    assert math.isclose(res.loc[(res.index == 'wiam9xme') & (res['time'] == '2021-07-03 19:00:00')][
               'daily_distribution'].values[0], 0.025162, rel_tol = 0.0001), "Incorrect daily distribution calculation"
