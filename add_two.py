# Function to find a valid way to climb stairs
def climb_stairs(N, stairs):

    # Empty list to store the steps
    steps_taken = []

    # Store the previous step
    previous_step = 0

    # Continue until no stairs are left
    while stairs > 0:

        # Check possible steps
        for step in [1, 2, 3]:

            # Step must not repeat
            # and must fit into remaining stairs
            if step != previous_step and step <= stairs:

                # Add step to the list WITHOUT append()
                steps_taken = steps_taken + [step]

                # Remove steps from remaining stairs
                stairs = stairs - step

                # Save current step
                previous_step = step

                break

    # Return the final list
    return steps_taken


# Example
print(climb_stairs(3, 7))