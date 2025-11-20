def multiples_bettor(initial_funds, initial_stake, n_rounds, multiplier, rng_fn):
    funds = initial_funds
    stake = initial_stake
    base_stake = initial_stake

    wagers = []
    values = []

    for t in range(1, n_rounds + 1):
        if funds <= 0:
            break

        if stake > funds:
            stake = funds

        if rng_fn():
            funds += stake
            stake = base_stake
        else:
            funds -= stake
            stake = stake * multiplier

        wagers.append(t)
        values.append(funds)

        if funds <= 0:
            break

    return wagers, values
