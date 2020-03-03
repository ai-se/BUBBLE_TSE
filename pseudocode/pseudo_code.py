def General(project):
    feature_vectors = get_featrures(projects)
    h_clusters = BIRCH(projects,feature_vectors)
    for level in h_clusters.levels:
        if level.depth == h_clusters.max_depth:
            for cluster in level.clusters:
                level.cluster.bell = bellwether(cluster.projects)
        else:
            for cluster in h_clusters.level.clusters:
                bell_projects = cluster.child.get_bellwethers()
                level.cluster.bell = bellwether(bell_projects)
    return h_clusters
