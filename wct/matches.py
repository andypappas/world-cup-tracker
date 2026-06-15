def update_finished_group_match(df, match_num, score1, score2):
    df.loc[match_num, "Home Score"] += score1
    df.loc[match_num, "Away Score"] += score2
    df.loc[match_num, "Status"] = "Finished"
    return df
