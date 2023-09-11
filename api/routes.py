from datetime import datetime
import logging
from http import HTTPStatus
from flask import request
from flask_restx import Api, Resource, fields, reqparse

rest_api = Api(title="HNG Task 1 ", version="0.1.0", doc="/docs", description=" This is a dedicated backend for HNG TASK1.")

# configurations for logging file handler for this api.
rest_api.logger.setLevel(logging.INFO)
fh = logging.FileHandler("v1.log") # creates a v1.log file on app start
rest_api.logger.addHandler(fh)

parser = reqparse.RequestParser()
parser.add_argument('slack_name', type=str, help='Slack name is a string')
parser.add_argument('track', type=str, help='Track is a string')

# defining a default response Schema validation
response_schema = rest_api.model('Resp_model', {
  "slack_name": fields.String(),
  "current_day": fields.String(),
  "utc_time": fields.String(),
  "track": fields.String(),
  "github_file_url": fields.String(),
  "github_repo_url": fields.String(),
  "status_code": fields.Integer()
})

res_input = rest_api.model('Input_model', {"slack_name": fields.String(),"track": fields.String()})

# endpoint to return expected response.

@rest_api.route('/api')
class Endpoint(Resource):
    '''Resource endpoint to return expected response'''

    @rest_api.marshal_with(response_schema)
    # @rest_api.expect(res_input)
    @rest_api.expect(parser)
    @rest_api.response(200, 'Success')
    @rest_api.response(400, 'Validation Error')
    def get(self):
        '''Endpoint to return expected data.'''

        # req_data = request.get_json()

        # slack_name = req_data.get('slack_name')
        # track = req_data.get('track')
        args = parser.parse_args()

        slack_name = args['slack_name']
        track = args['track']
        
        current_day = datetime.now().strftime('%A')
        date_time = datetime.utcnow()
        resp = {
                "slack_name": f"{slack_name}",#"Bessong Atabe Junior",
                "current_day": f"{current_day}",
                "utc_time": f'{date_time}',#"2023-08-21T15:04:05Z",
                "track": f"{track}",
                "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
                "github_repo_url": "https://github.com/bessongjunior/hng_task1",
                "status_code": 200
            }
        
        print(resp)

        return resp, HTTPStatus.OK
    

@rest_api.errorhandler
def default_error_handler(error):
    '''Default error handler'''

    rest_api.logger.info(f"An internal server error occurred! This message is to be addressed quickly.")
    return {'message': str(error)}, getattr(error, 'code', 500)