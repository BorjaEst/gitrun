# gitrun

Container to run CICD on self hosted machine on demand.

# Redirect

- Port 5000: api.#id -> Used at default.conf
- Port 6006: monitor.#id
- Port 8888, ide.#id

# MyToken

1. Go to [mytoken.data.kit.edu](https://mytoken.data.kit.edu/home) and create a new mytoken.
2. Use "web-default" profile.
3. Under restrictions, change "Easy Editor" by JSON Editor.
4. Configure the following JSON: `[{"exp":1707345797,"audience":["https://api.cloud.ai4eosc.eu"]}]`
5. Confirm the creation of the token and copy the token.
6. Go to your Github repository and go to `Settings` -> `Secrets` -> `New repository secret`.
7. Name the secret `MYTOKEN` and paste the token in the value field, confirm.

# Registration tokens:

1. Go to Github user `settings` -> `Developer settings` -> `Personal access tokens` -> `Fine-grained tokens`.
2. Name the token and set an expiration date.
3. Under `Repository access`, select `Only select repositories` and choose the repository to add runners.
4. Under `Permissions`, set `Administration` to `Read and write`.
5. Confirm the creation of the token and copy the token.
6. Go to your Github repository and go to `Settings` -> `Secrets` -> `New repository secret`.
7. Name the secret `APITOKEN` and paste the token in the value field, confirm.
