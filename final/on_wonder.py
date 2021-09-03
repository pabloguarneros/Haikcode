for tree in ocean:
    ocean.is_gone()
    tree.falls_down()


def future_trees(dirt):
    if "graffiti_particles" in dirt.materials:
        dirt.grow_teleportation_portals()