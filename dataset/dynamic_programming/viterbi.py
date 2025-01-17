from typing import Any


def viterbi(
    observations_space: list,
    states_space: list,
    initial_probabilities: dict,
    transition_probabilities: dict,
    emission_probabilities: dict,
) -> list:
    _validation(
        observations_space,
        states_space,
        initial_probabilities,
        transition_probabilities,
        emission_probabilities,
    )
    
    probabilities: dict = {}
    pointers: dict = {}
    for state in states_space:
        observation = observations_space[0]
        probabilities[(state, observation)] = (
            initial_probabilities[state] * emission_probabilities[state][observation]
        )
        pointers[(state, observation)] = None

    
    
    for o in range(1, len(observations_space)):
        observation = observations_space[o]
        prior_observation = observations_space[o - 1]
        for state in states_space:
            
            arg_max = ""
            max_probability = -1
            for k_state in states_space:
                probability = (
                    probabilities[(k_state, prior_observation)]
                    * transition_probabilities[k_state][state]
                    * emission_probabilities[state][observation]
                )
                if probability > max_probability:
                    max_probability = probability
                    arg_max = k_state

            
            probabilities[(state, observation)] = (
                probabilities[(arg_max, prior_observation)]
                * transition_probabilities[arg_max][state]
                * emission_probabilities[state][observation]
            )

            pointers[(state, observation)] = arg_max

    
    final_observation = observations_space[len(observations_space) - 1]

    
    arg_max = ""
    max_probability = -1
    for k_state in states_space:
        probability = probabilities[(k_state, final_observation)]
        if probability > max_probability:
            max_probability = probability
            arg_max = k_state
    last_state = arg_max

    
    previous = last_state
    result = []
    for o in range(len(observations_space) - 1, -1, -1):
        result.append(previous)
        previous = pointers[previous, observations_space[o]]
    result.reverse()

    return result


def _validation(
    observations_space: Any,
    states_space: Any,
    initial_probabilities: Any,
    transition_probabilities: Any,
    emission_probabilities: Any,
) -> None:
    _validate_not_empty(
        observations_space,
        states_space,
        initial_probabilities,
        transition_probabilities,
        emission_probabilities,
    )
    _validate_lists(observations_space, states_space)
    _validate_dicts(
        initial_probabilities, transition_probabilities, emission_probabilities
    )


def _validate_not_empty(
    observations_space: Any,
    states_space: Any,
    initial_probabilities: Any,
    transition_probabilities: Any,
    emission_probabilities: Any,
) -> None:
    if not all(
        [
            observations_space,
            states_space,
            initial_probabilities,
            transition_probabilities,
            emission_probabilities,
        ]
    ):
        raise ValueError("There's an empty parameter")


def _validate_lists(observations_space: Any, states_space: Any) -> None:
    _validate_list(observations_space, "observations_space")
    _validate_list(states_space, "states_space")


def _validate_list(_object: Any, var_name: str) -> None:
    if not isinstance(_object, list):
        msg = f"{var_name} must be a list"
        raise ValueError(msg)
    else:
        for x in _object:
            if not isinstance(x, str):
                msg = f"{var_name} must be a list of strings"
                raise ValueError(msg)


def _validate_dicts(
    initial_probabilities: Any,
    transition_probabilities: Any,
    emission_probabilities: Any,
) -> None:
    _validate_dict(initial_probabilities, "initial_probabilities", float)
    _validate_nested_dict(transition_probabilities, "transition_probabilities")
    _validate_nested_dict(emission_probabilities, "emission_probabilities")


def _validate_nested_dict(_object: Any, var_name: str) -> None:
    _validate_dict(_object, var_name, dict)
    for x in _object.values():
        _validate_dict(x, var_name, float, True)


def _validate_dict(
    _object: Any, var_name: str, value_type: type, nested: bool = False
) -> None:
    if not isinstance(_object, dict):
        msg = f"{var_name} must be a dict"
        raise ValueError(msg)
    if not all(isinstance(x, str) for x in _object):
        msg = f"{var_name} all keys must be strings"
        raise ValueError(msg)
    if not all(isinstance(x, value_type) for x in _object.values()):
        nested_text = "nested dictionary " if nested else ""
        msg = f"{var_name} {nested_text}all values must be {value_type.__name__}"
        raise ValueError(msg)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
