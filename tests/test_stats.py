from recycle import stats


def test_gen_histogram_mem_eff():
    numbers = range(0, 110)

    idxs = []

    def progress_callback(idx):
        idxs.append(idx)

    hist, bins = stats.gen_histogram_mem_eff(
        numbers, min_value=10, max_value=100, num_bins=10,
        progress_callback=progress_callback, progress_size=10
    )
    assert set(hist) == {10, 11}
    assert len(bins) == 10
    assert len(idxs) == 11
    assert idxs[0] == 10
    assert idxs[-1] == 110
    # assert False
