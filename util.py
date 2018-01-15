def lerp(color_1, color_2, steps):
    step = 0
    r_step = (color_2[0] - color_1[0]) / steps
    g_step = (color_2[1] - color_1[1]) / steps
    b_step = (color_2[2] - color_1[2]) / steps
    while step <= steps:
        yield (
            int(color_1[0] + (r_step * step)),
            int(color_1[1] + (g_step * step)),
            int(color_1[2] + (b_step * step))
        )
        step += 1
