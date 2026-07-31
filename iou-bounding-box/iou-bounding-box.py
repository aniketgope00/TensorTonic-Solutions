def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    x1_inter, y1_inter = max(box_a[0], box_b[0]), max(box_a[1], box_b[1])
    x2_inter, y2_inter = min(box_a[2], box_b[2]), min(box_a[3], box_b[3])
    w_inter, h_inter   = max(0, x2_inter - x1_inter), max(0, y2_inter - y1_inter)
    area_inter         = w_inter * h_inter
    area_union         = ((box_a[2] - box_a[0]) * (box_a[3] - box_a[1]) + (box_b[2] - box_b[0]) * (box_b[3] - box_b[1]) ) - area_inter

    return area_inter/area_union
