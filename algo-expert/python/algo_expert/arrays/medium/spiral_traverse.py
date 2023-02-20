def spiral_traverse(array: list) -> list:
    n_min = 0
    m_min = 0
    n_max = len(array)
    m_max = len(array[0])

    result = []

    while m_min < len(array[0]) / 2 and n_min < len(array) and not m_min >= m_max and not n_min >= n_max:
        for m in range(m_min, m_max):
            result.append(array[n_min][m])
        n_min += 1

        for n in range(n_min, n_max):
            result.append(array[n][m_max - 1])
        m_max -= 1

        if n_min >= n_max:
            break

        for m in reversed(range(m_min, m_max)):
            result.append(array[n_max - 1][m])
        n_max -= 1

        if m_min >= m_max:
            break

        for n in reversed(range(n_min, n_max)):
            result.append(array[n][m_min])
        m_min += 1

    return result
