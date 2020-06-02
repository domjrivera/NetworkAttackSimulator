from .environment import NASimEnv
import nasim.scenarios.benchmark as bm


def make_benchmark_env(scenario_name, seed=None, partially_obs=False):
    """Make a new benchmark NASim environment.

    Parameters
    ----------
    scenario_name : str
        the name of the benchmark environment
    seed : int, optional
        random seed to use to generate environment (default=None)
    partially_obs : bool, optional
        whether to use partially observable mode (True) or not (False)
        (default=False)

    Returns
    -------
    NASimEnv
        a new environment instance

    Raises
    ------
    NotImplementederror
        if scenario_name does no match any implemented benchmark scenarios.
    """

    if scenario_name in bm.AVAIL_GEN_BENCHMARKS:
        scenario = bm.AVAIL_GEN_BENCHMARKS[scenario_name]
        scenario['seed'] = seed
        env = NASimEnv.from_params(partially_obs=partially_obs, **scenario)
    elif scenario_name in bm.AVAIL_STATIC_BENCHMARKS:
        scenario_file = bm.AVAIL_STATIC_BENCHMARKS[scenario_name]["file"]
        env = NASimEnv.from_file(scenario_file, partially_obs)
    else:
        raise NotImplementedError(
            f"Benchmark scenario '{scenario_name}' not available."
            f"Available scenarios are: {bm.AVAIL_BENCHMARKS}"
        )
    return env


def get_scenario_max(scenario_name):
    if scenario_name in bm.AVAIL_GEN_BENCHMARKS:
        return bm.AVAIL_GEN_BENCHMARKS[scenario_name]["max_score"]
    elif scenario_name in bm.AVAIL_STATIC_BENCHMARKS:
        return bm.AVAIL_STATIC_BENCHMARKS[scenario_name]["max_score"]
    return None
