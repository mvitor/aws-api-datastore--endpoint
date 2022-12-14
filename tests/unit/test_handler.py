import json

import pytest

from user_log import app


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
  "resource": "/{proxy+}",
  "httpMethod": "POST",
  "isBase64Encoded": true,
  "queryStringParameters": {
    "id": 1,
    "name": "marcio"
  },
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "en-US,en;q=0.8",
    "Cache-Control": "max-age=0",
    "X-Forwarded-Port": "443",
    "X-Forwarded-Proto": "https"
  },
  "requestContext": {
    "stage": "prod",
    "resourcePath": "/{proxy+}",
    "httpMethod": "POST",
    "protocol": "HTTP/1.1"
  }
}


def test_lambda_handler_write_file(apigw_event, mocker):
    file_mock = mocker.patch.object(app, 'FILE')
    file_mock.is_file.return_value = False

    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "status" in ret["body"]
    assert "uid" in ret["body"]
    assert data["status"] == "success"
    assert data["name"] == "Marcio"
