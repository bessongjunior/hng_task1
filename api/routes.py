from datetime import datetime, timezone, timedelta
import logging
from http import HTTPStatus
from flask_restx import Api, Resource, fields

rest_api = Api(title="HNG Task 1 ", version="0.1.0", doc="/docs", description=" This is a dedicated backend for HNG TASK1.")

# configurations for logging file handler for this api.
rest_api.logger.setLevel(logging.INFO)
fh = logging.FileHandler("v1.log") # creates a v1.log file on app start
rest_api.logger.addHandler(fh)


# defining a default response Schema validation
response_schema = rest_api.model('Resp_model', {
  "slack_name": fields.String(),
  "current_day": fields.String(),
  "utc_time": fields.Datetime(),
  "track": fields.String(),
  "github_file_url": fields.String(),
  "github_repo_url": fields.String(),
  "status_code": fields.Integer()
})

# endpoint to return expected response.

@rest_api.route('/endpoint')
class Endpoint(Resource):
    '''Resource endpoint to return expected response'''

    @rest_api.marshal_with(response_schema)
    def get(self):
        '''Endpoint to return expected data.'''
        resp = {
                "slack_name": "Bessong Atabe Junior",
                "current_day": f"{datetime.now().strftime('%A')}",
                "utc_time": f'{datetime.now()}',#"2023-08-21T15:04:05Z",
                "track": "backend",
                "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
                "github_repo_url": "https://github.com/username/repo",
                "status_code": f'{HTTPStatus.OK}'
            }

        return resp, HTTPStatus.OK