import numpy as np


def simulate_single_random_walk(n_steps, step_size=1.0):
    """
    Simulate a single path of a symmetric random walk.
    
    This function implements the basic mathematical definition of a random walk:
    starting from zero, at each time step we move either +1 or -1 with equal
    probability. The position at any time is the cumulative sum of all steps
    taken so far.
    
    Parameters
    ----------
    n_steps : int
        Number of steps in the random walk. Must be a positive integer.
        This determines how long the walk runs.
    step_size : float, optional
        Size of each individual step. Default is 1.0.
        This allows us to scale the walk - if step_size is 0.5, each step
        is +0.5 or -0.5 instead of +1 or -1.
        
    Returns
    -------
    positions : numpy.ndarray
        Array of positions at each time step, including the initial position.
        Shape is (n_steps + 1,) because we include time 0.
        positions[0] is always 0 (starting position).
        positions[i] for i > 0 is the position after i steps.
        
    Examples
    --------
    >>> np.random.seed(42)  # For reproducibility
    >>> path = simulate_single_random_walk(n_steps=5)
    >>> print(path)
    [0. -1. 0. 1. 0. -1.]
    
    >>> # With custom step size
    >>> path = simulate_single_random_walk(n_steps=5, step_size=0.5)
    >>> print(path)
    [0. -0.5 0. 0.5 0. -0.5]
    
    Notes
    -----
    The random walk has the following key properties (see theory.md):
    - Expected position at any time is zero: E[S_n] = 0
    - Variance grows linearly with time: Var(S_n) = n * step_size^2
    - Distribution approaches normal for large n
    - Has independent increments (Markov property)
    """
    # Step 1: Generate random steps (+1 or -1 with equal probability)
    # np.random.choice selects randomly from the given array
    # size=n_steps means we do this n_steps times
    steps = np.random.choice([-1, 1], size=n_steps)
    
    # Step 2: Scale the steps by step_size if it's not 1.0
    # This allows flexibility - we can have steps of any size
    # If step_size is 1.0, this multiplication doesn't change anything
    steps = steps * step_size
    
    # Step 3: Calculate cumulative sum to get positions over time
    # np.cumsum([a, b, c]) returns [a, a+b, a+b+c]
    # This gives us the position after each step
    cumulative_positions = np.cumsum(steps)
    
    # Step 4: Add the starting position (0) at the beginning
    # We use np.concatenate to join [0] with the cumulative positions
    # This ensures that positions[0] = 0 (starting point)
    # and positions[i] = sum of first i steps for i > 0
    positions = np.concatenate([[0], cumulative_positions])
    
    return positions
