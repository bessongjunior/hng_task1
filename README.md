## HNG TASK 1

### Description
- Create and host an endpoint using any programming language of your choice.
- The endpoint should take two GET request query parameters and return specific information in JSON format.

```
{
  "slack_name": "example_name",
  "current_day": "Monday",
  "utc_time": "2023-08-21T15:04:05Z",
  "track": "backend",
  "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
  "github_repo_url": "https://github.com/username/repo",
  "status_code": 200
}
```

### To run the app
```
- clone the repo
- create a virtual env by entering :: python -m venv env
- Activate the virtual env by entering :: source/bin/activate
- Install requirements by entering :: pip install -r requirements.txt
- Run the app either by entering :: python run.py or :: hypercorn app:run.py
```

The end.
