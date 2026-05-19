def execution_accuracy(predicted_result, expected_result):

    return predicted_result == expected_result


def valid_sql(success_flag):

    return success_flag


def exact_match(predicted_sql, expected_sql):

    predicted_sql = predicted_sql.strip().lower()
    expected_sql = expected_sql.strip().lower()

    return predicted_sql == expected_sql