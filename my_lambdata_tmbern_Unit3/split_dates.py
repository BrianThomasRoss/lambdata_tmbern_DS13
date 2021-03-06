def split_dates(df, column):
    
    # create a copy to prevent copy warnings
    df = df.copy()

    # convert the column to a date time format
    df[column] = pandas.to_datetime(df[column], infer_datetime_format=True)

    # create new columns for the month day and year of the given date column
    df['Month'] = df[column].dt.month
    df['Day'] = df[column].dt.day
    df['Year'] = df[column].dt.year

    return(df)