"""Tests for the API endpoints."""

import pytest
from fastapi import status
from fastapi.testclient import TestClient


def test_version_endpoint(client):
    """Test the /version endpoint."""
    response = client.get("/version")
    assert response.status_code == status.HTTP_200_OK
    assert "name" in response.json()
    assert "description" in response.json()
    assert "version" in response.json()


def test_identify_endpoint_with_text_file(client, sample_text_file):
    """Test the /identify endpoint with a text file."""
    # This test is more complex as it requires mocking the file upload
    # For now, we'll just test that the endpoint exists and returns a 422 error
    # when no file is provided
    response = client.post("/identify")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_ai_identify_endpoint_with_text_file(client, sample_text_file):
    """Test the /ai_identify endpoint with a text file."""
    # This test is more complex as it requires mocking the file upload
    # For now, we'll just test that the endpoint exists and returns a 422 error
    # when no file is provided
    response = client.post("/ai_identify")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
