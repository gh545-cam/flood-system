from Task1A import run

def test_Task1A(capsys):
    captured_output = capsys.readouterr(run())
    assert "town:" in captured_output
    assert ("Gaw Bridge","Surfleet Seas End","Surfleet Sluice") in captured_output
    assert "http://environment.data.gov.uk/flood-monitoring/id/stations/52119" in captured_output