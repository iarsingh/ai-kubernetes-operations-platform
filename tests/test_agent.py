from fastapi.testclient import TestClient
from aik8sops.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'stabilize the cluster', **{'payload': {}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert "plan" in payload["steps"]
    refused = client.post("/agent/run", json={"goal": 'kubectl apply -f prod.yaml'}).json()
    assert refused["refused"] is True
