# -*- coding: utf-8 -*-
"""Glassdoor scraper module"""

import pandas as pd

def get_jobs(keyword: str, num_jobs: int = 15, verbose: bool = False, slp_time: int = 15):
    # TEMP: return a tiny dataframe just to prove the import works
    return pd.DataFrame([{"keyword": keyword, "num_jobs": num_jobs, "ok": True}])
