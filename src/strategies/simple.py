def simple_bettor(initial_funds, stake, n_rounds, rng_fn):
    funds = initial_funds
    wager = stake

    wagers = []
    values = []

    for t in range(1, n_rounds + 1):
        if funds <= 0:
            break

        if funds < wager:
            wager = funds

        if rng_fn():
            funds += wager
        else:
            funds -= wager

        wagers.append(t)
        values.append(funds)

        if funds <= 0:
            break

    return wagers, values