def load_metereological_data(path):
    data = pd.read_csv(
    path,
    skiprows=5,             # skip the metadata rows
    header=0,               # use the first non-skipped row as the header
    encoding="utf-8-sig"
    )
    return data

print("Helper code loaded")