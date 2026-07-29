def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = set(recommended[:k])
    intersect = len(top_k & set(relevant))
    return [intersect/k, intersect/len(relevant)]