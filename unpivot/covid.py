# -*- coding: utf-8 -*

import pandas as pd
from pathlib import Path

datadirectory = Path().cwd().parent / 'COVID-19' / 'csse_covid_19_data' / 'csse_covid_19_time_series'

CONFNM = 'time_series_19-covid-Confirmed.csv'
DEATHSNM = 'time_series_19-covid-Deaths.csv'
RECONM = 'time_series_19-covid-Recovered.csv'

CONFFILE = datadirectory / CONFNM
DEATHSFILE = datadirectory / DEATHSNM
RECOFILE = datadirectory / RECONM

conf = pd.read_csv(CONFFILE)
deaths = pd.read_csv(DEATHSFILE)
reco = pd.read_csv(RECOFILE)


def make_long(df, varname):
    """
    accepts conf, deaths, reco dataframes in turn, and
    unpivots them

    Parameters
    ----------
    df : one of conf, deaths, or reco.
    varname : the name to give to the count variable resulting from
    the unpivot.

    Returns
    -------
    df_long : the unpivoted dataframe

    """

    # create list of dates to turn into value variables
    dates = list(df.columns[4:])

    df.rename(columns={'Province/State': 'region',
                       'Country/Region': 'country'}, inplace=True)

    # create list of id variables for the unpivot
    ids = list(df.columns[0:4])

    df_long = pd.melt(df, id_vars=ids,
                      value_vars=dates,
                      var_name='date',
                      value_name=varname)

    # in order to merge confirmed, recovered, deaths files later on,
    # missing region values are converted to empty strings.
    df_long['region'] = df_long['region'].fillna('')

    # I don't need latitude or longitude, and these cols would just get
    # duplicated in the merge, below.
    df_long.drop(['Lat', 'Long'], axis=1, inplace=True)
    return df_long


conf_long = make_long(conf, 'confirmed')
deaths_long = make_long(deaths, 'deaths')
reco_long = make_long(reco, 'recovered')

# combine the 3 unpivoted dataframes into one
combo = conf_long.merge(deaths_long,
                        how='left',
                        on=['region', 'country', 'date']).merge(
                            reco_long,
                            how='left',
                            on=['region', 'country', 'date'])

combo.to_excel('unpivoted.xlsx', na_rep='N/A', index=False)
