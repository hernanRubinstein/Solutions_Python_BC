import assignment_d6 as dge_pack

# This test asserts that the name of most differentially expressed gene is different for both columns in two matrices
def test_calculate_dge1():
    result = dge_pack.calculate_fold_change("mat_test_1.csv","mat_test_2.csv")
    output = list(result.values())
    assert output[0][0] != output[1][0]

# This test asserts that the value of fold change is equal for both columns in two matrices
def test_calculate_dge2():
    result = dge_pack.calculate_fold_change("mat_test_1.csv","mat_test_2.csv")
    output = list(result.values())
    assert output[0][1] == output[1][1]