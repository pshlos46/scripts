## Migrate all your Heroku Dataclips

If you started with Heroku and you used extensively the Dataclips functionality, at some point you may need to migrate the queries to another system.

Heroku does not provide an API or a way to grab all of your queries. Use `dataclips-snatch.py` and a valid cookie from your account and get them through HTTP.

You will provided with 2 JSONs with the below fields:

`all-dataclips-summary.json`

    "slug"
    "favorited_at"
    "name"
    "author"
    "created_at"
    "updated_at"
    "heroku_id"
    "viewed_at"
    "heroku_resource_name"
    "heroku_app_name"

`all-dataclips-detailed.json`

	
    "author"
    "authorized_emails"
    "checksum"
    "created_at"
    "current_slug"
    "editable"
    "favorited_at"
    "heroku_app_name"
    "heroku_id"
    "heroku_resource_name"
    "last_ran_at"
    "latest_version_author"
    "name"
    "requires_authorization"
    "result_slug"
    "securable"
    "shares"
    "single_access_token"
    "slug"
    "sql"
    "updated_at"
    "version_number"
    "versions":	   
    "viewed_at": 


`dataclips-print-onlyqueries.py` is a helper to print only the queries in some human readable format, if that is what you need.