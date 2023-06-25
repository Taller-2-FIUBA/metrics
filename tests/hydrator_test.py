# pylint: disable= missing-module-docstring, missing-function-docstring


from metrics.hydrator import hydrate


def test_when_there_are_no_documents_expect_empty_list():
    assert not hydrate([])


def test_when_there_are_two_documents_expect_two_metrics():
    documents = [{"_id": "arm", "count": 33}, {"_id": "leg", "count": 3}]
    metrics = hydrate(documents)
    assert metrics[0].label == "arm"
    assert metrics[0].count == 33
    assert metrics[1].label == "leg"
    assert metrics[1].count == 3
