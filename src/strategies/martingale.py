def martingale_bettor(initial_funds, initial_stake, n_rounds, rng_fn):
    funds = initial_funds
    stake = initial_stake
    base_stake = initial_stake

    wagers = []
    values = []

    previous = "win"

    for t in range(1, n_rounds + 1):
        if funds <= 0:
            break

        if stake > funds:
            stake = funds

        if rng_fn():
            funds += stake
            previous = "win"
            stake = base_stake
        else:
            funds -= stake
            previous = "loss"
            stake = stake * 2

        wagers.append(t)
        values.append(funds)

        if funds <= 0:
            break

    return wagers, values