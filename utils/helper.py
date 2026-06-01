import pandas as pd


# =========================
# TEAM ANALYSIS
# =========================

def team_stats(matches, team):

    played = matches[
        (matches['team1'] == team) |
        (matches['team2'] == team)
    ].shape[0]

    won = matches[
        matches['winner'] == team
    ].shape[0]

    lost = played - won

    win_percent = round((won / played) * 100, 2)

    return played, won, lost, win_percent


def team_wins(matches):

    wins = matches['winner'].value_counts()

    wins_df = wins.reset_index()

    wins_df.columns = ['Team', 'Wins']

    wins_df = wins_df.sort_values(
        by='Wins',
        ascending=False
    )

    return wins_df


def season_wins(matches, team):

    matches_copy = matches.copy()

    matches_copy['date'] = pd.to_datetime(
        matches_copy['date']
    )

    matches_copy['Season'] = (
        matches_copy['date'].dt.year
    )

    season_df = matches_copy[
        matches_copy['winner'] == team
    ]

    season_df = (
        season_df
        .groupby('Season')
        .size()
        .reset_index(name='Wins')
    )

    return season_df


def head_to_head(matches, team1, team2):

    h2h = matches[
        (
            (matches['team1'] == team1)
            &
            (matches['team2'] == team2)
        )
        |
        (
            (matches['team1'] == team2)
            &
            (matches['team2'] == team1)
        )
    ]

    total_matches = h2h.shape[0]

    team1_wins = h2h[
        h2h['winner'] == team1
    ].shape[0]

    team2_wins = h2h[
        h2h['winner'] == team2
    ].shape[0]

    return (
        total_matches,
        team1_wins,
        team2_wins
    )


# =========================
# BATTER ANALYSIS
# =========================

def batter_stats(deliveries, batter):

    batter_df = deliveries[
        deliveries['batsman'] == batter
    ]

    runs = batter_df[
        'batsman_runs'
    ].sum()

    balls = batter_df.shape[0]

    fours = batter_df[
        batter_df['batsman_runs'] == 4
    ].shape[0]

    sixes = batter_df[
        batter_df['batsman_runs'] == 6
    ].shape[0]

    strike_rate = round(
        (runs / balls) * 100,
        2
    )

    return (
        runs,
        balls,
        fours,
        sixes,
        strike_rate
    )


def top_batters(deliveries):

    top = (
        deliveries
        .groupby('batsman')['batsman_runs']
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    top.columns = [
        'Batter',
        'Runs'
    ]

    return top


def boundary_percentage(deliveries, batter):

    batter_df = deliveries[
        deliveries['batsman'] == batter
    ]

    total_runs = batter_df[
        'batsman_runs'
    ].sum()

    if total_runs == 0:
        return 0

    boundary_runs = batter_df[
        batter_df['batsman_runs'].isin([4, 6])
    ]['batsman_runs'].sum()

    percentage = round(
        (boundary_runs / total_runs) * 100,
        2
    )

    return percentage


def run_distribution(deliveries, batter):

    batter_df = deliveries[
        deliveries['batsman'] == batter
    ]

    return (
        batter_df['batsman_runs']
        .value_counts()
        .reset_index()
    )


# =========================
# BOWLER ANALYSIS
# =========================

def bowler_stats(deliveries, bowler):

    bowler_df = deliveries[
        deliveries['bowler'] == bowler
    ]

    wickets = bowler_df[
        'is_wicket'
    ].sum()

    balls = bowler_df.shape[0]

    runs = bowler_df[
        'total_runs'
    ].sum()

    economy = round(
        runs / (balls / 6),
        2
    )

    return (
        wickets,
        balls,
        runs,
        economy
    )


def top_bowlers(deliveries):

    bowlers = (
        deliveries
        .groupby('bowler')['is_wicket']
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    bowlers.columns = [
        'Bowler',
        'Wickets'
    ]

    return bowlers


# =========================
# VENUE ANALYSIS
# =========================

def venue_stats(matches):

    venues = (
        matches['venue']
        .value_counts()
        .head(10)
        .reset_index()
    )

    venues.columns = [
        'Venue',
        'Matches'
    ]

    return venues


# =========================
# RECORDS PAGE
# =========================

def most_runs(deliveries):

    return (
        deliveries
        .groupby('batsman')['batsman_runs']
        .sum()
        .sort_values(ascending=False)
        .head(1)
    )


def most_wickets(deliveries):

    return (
        deliveries
        .groupby('bowler')['is_wicket']
        .sum()
        .sort_values(ascending=False)
        .head(1)
    )


def most_sixes(deliveries):

    sixes = deliveries[
        deliveries['batsman_runs'] == 6
    ]

    return (
        sixes
        .groupby('batsman')
        .size()
        .sort_values(ascending=False)
        .head(1)
    )


def most_fours(deliveries):

    fours = deliveries[
        deliveries['batsman_runs'] == 4
    ]

    return (
        fours
        .groupby('batsman')
        .size()
        .sort_values(ascending=False)
        .head(1)
    )
    
def top_six_hitters(deliveries):

    sixes = deliveries[
        deliveries['batsman_runs'] == 6
    ]

    six_df = (
        sixes
        .groupby('batsman')
        .size()
        .sort_values(ascending=False)
        .head(10)
        .reset_index(name='Sixes')
    )

    return six_df

def top_boundary_hitters(deliveries):

    boundary_df = deliveries[
        deliveries['batsman_runs'].isin([4, 6])
    ]

    boundary_df = (
        boundary_df
        .groupby('batsman')
        .size()
        .sort_values(ascending=False)
        .head(10)
        .reset_index(name='Boundaries')
    )

    return boundary_df

def top_strike_rate_batters(deliveries):

    sr_df = (
        deliveries
        .groupby('batsman')
        .agg(
            Runs=('batsman_runs', 'sum'),
            Balls=('batsman_runs', 'count')
        )
        .reset_index()
    )

    sr_df = sr_df[
        sr_df['Balls'] >= 500
    ]

    sr_df['Strike Rate'] = round(
        (sr_df['Runs'] / sr_df['Balls']) * 100,
        2
    )

    sr_df = (
        sr_df
        .sort_values(
            by='Strike Rate',
            ascending=False
        )
        .head(10)
    )

    return sr_df

def orange_cap(deliveries):

    orange_df = (
        deliveries
        .groupby('batsman')['batsman_runs']
        .sum()
        .sort_values(ascending=False)
        .head(20)
        .reset_index()
    )

    orange_df.columns = [
        'Batter',
        'Runs'
    ]

    return orange_df

def top_economy_bowlers(deliveries):

    eco_df = (
        deliveries
        .groupby('bowler')
        .agg(
            Runs=('total_runs', 'sum'),
            Balls=('total_runs', 'count')
        )
        .reset_index()
    )

    eco_df = eco_df[
        eco_df['Balls'] >= 500
    ]

    eco_df['Economy'] = round(
        eco_df['Runs'] / (eco_df['Balls'] / 6),
        2
    )

    eco_df = (
        eco_df
        .sort_values(
            by='Economy',
            ascending=True
        )
        .head(10)
    )

    return eco_df


def top_dot_ball_bowlers(deliveries):

    dot_df = deliveries[
        deliveries['total_runs'] == 0
    ]

    dot_df = (
        dot_df
        .groupby('bowler')
        .size()
        .sort_values(ascending=False)
        .head(10)
        .reset_index(name='Dot Balls')
    )

    return dot_df


def purple_cap(deliveries):

    purple_df = (
        deliveries
        .groupby('bowler')['is_wicket']
        .sum()
        .sort_values(ascending=False)
        .head(20)
        .reset_index()
    )

    purple_df.columns = [
        'Bowler',
        'Wickets'
    ]

    return purple_df

def venue_details(matches, venue):

    venue_df = matches[
        matches['venue'] == venue
    ]

    total_matches = venue_df.shape[0]

    most_successful_team = (
        venue_df['winner']
        .value_counts()
        .idxmax()
    )

    wins = (
        venue_df['winner']
        .value_counts()
        .max()
    )

    return (
        total_matches,
        most_successful_team,
        wins
    )
    
def venue_match_type(matches, venue):

    venue_df = matches[
        matches['venue'] == venue
    ]

    batting_first = venue_df[
        venue_df['win_by_runs'] > 0
    ].shape[0]

    chasing = venue_df[
        venue_df['win_by_wickets'] > 0
    ].shape[0]

    return batting_first, chasing