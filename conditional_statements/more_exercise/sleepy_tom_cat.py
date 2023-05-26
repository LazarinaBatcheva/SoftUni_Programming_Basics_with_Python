days_off = int(input())

NORM_FOR_GAME_OF_TOM = 30000
DAYS_IN_YEAR = 365
MINUTES_GAME_FOR_WORK_DAY = 63
MINUTES_GAME_FOR_DAY_OFF = 127

minutes_game_for_days_off = days_off * MINUTES_GAME_FOR_DAY_OFF
minutes_game_for_work_day = (DAYS_IN_YEAR - days_off) * MINUTES_GAME_FOR_WORK_DAY

total_time_for_game = minutes_game_for_days_off + minutes_game_for_work_day

difference_between_game_time = abs(NORM_FOR_GAME_OF_TOM - total_time_for_game)
games_time_in_hours = difference_between_game_time // 60
games_time_in_minutes = difference_between_game_time % 60

if total_time_for_game > NORM_FOR_GAME_OF_TOM:
    print("Tom will run away")
    print(f"{games_time_in_hours} hours and {games_time_in_minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{games_time_in_hours} hours and {games_time_in_minutes} minutes less for play")