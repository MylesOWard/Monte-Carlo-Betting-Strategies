def dalembert_bettor(initial_funds, initial_stake, n_rounds, rng_fn):
    funds = initial_funds
    stake = initial_stake
    base = initial_stake

    wagers = []
    values = []

    previous = "win"

    for t in range(1, n_rounds + 1):
        if funds <= 0:
            break

        if stake > funds:
            stake = funds

        win = rng_fn()

        if win:
            funds += stake
            previous = "win"
            stake = stake - base
            if stake < base:
                stake = base
        else:
            funds -= stake
            previous = "loss"
            stake = stake + base

        wagers.append(t)
        values.append(funds)

        if funds <= 0:
            break

    return wagers, values